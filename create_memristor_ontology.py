import pyirk as p
import os, sys
import re
from ipydex import IPS, Container
try:
    from scholarly import scholarly
except:
    use_scholarly = False
import google.generativeai as genai
import json
import pandas as pd
import cachewrapper as cw
import random

from stafo.utils import BASE_DIR, CONFIG_PATH, render_template, config_data
from stafo.core import llm_api
from stafo.statement_to_kg import ConversionManager

random.seed(42)
# llm_cache_path = "llm_cache.pcl"


if omt_path := config_data.get("omt_path"):
    omt_path = os.path.join(omt_path, "omt.py")
    assert os.path.isfile(omt_path)
else:
    # use hardcoded fallback
    omt_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "omt")), "omt.py")

omt_load_dict = {"path": omt_path, "prefix": "omt", "module_name": "omt"}
ag_load_dict = {"path": os.path.join(config_data["ocse_path"], "agents1.py"), "prefix": "ag", "module_name": "agents"}

def main():
    CM = ConversionManager("formalized_statements.md", num_keys=1000,
        load_irk_modules=[omt_load_dict, ag_load_dict])
    CM.step1_init()
    CM.step2_parse_fnl()
    CM.current_snippet = "mem"
    CM.default_language = "en"
    # step 1
    # parse Bibliography and return Authors and Titles

    compare_publication_folders = ["2019_lanza","2019_xia", "2024_aguirre", ]
    publist = ""

    for name in compare_publication_folders:
        llm_cache_path = f"llm_cache_{name}.pcl"
        publist += "\n"
        bib_path = f"data/{name}/bib.md"
        table_path = f"data/{name}/table.md"
        meta_path = f"data/{name}/meta.json"

        temp_path = f"data/temp/tmp.json"
        CM.current_snippet = name

        citation_dict = {}

        # read table
        ########################################################################
        with open(table_path, "rt", encoding="utf-8") as f:
            df = pd.read_csv(f, delimiter="|")
        d = {}
        for head in df.columns:
            d[head] = head.strip()
        df = df.rename(columns=d, errors="raise")

        assert "Source" in df.columns, "table is missing Source column"
        assert "Stack" in df.columns, "table is missing Stack column"

        # drop separation row
        df = df.drop(index=0)

        # extract citation numbers
        _relevant_citations = []
        for cite in df["Source"]:
            if "," in cite:
                _relevant_citations.extend(cite.split(","))
            else:
                _relevant_citations.append(cite)
        # convert to int
        relevant_citations = []
        for i, rc in enumerate(_relevant_citations):
            try:
                relevant_citations.append(int(rc))
            except ValueError:
                # this happens when in the source column the entry looks like this: "219,"
                pass

        # create publication entry
        with open(meta_path, "rt") as f:
            meta_infos = json.load(f)
        pub_dict = {"R4": 'ag.I6591["source document"]'}
        if meta_infos["author"]:
            pub_dict["R8433"] = meta_infos["author"]
        if meta_infos["title"]:
            pub_dict["R8434"] = meta_infos["title"]
        if meta_infos["year"]:
            pub_dict["R8435"] = meta_infos["year"]
        og_pub_id = "publication: " + meta_infos["title"]
        CM.add_new_item(CM.d, og_pub_id, "en", pub_dict)




        # parse citations
        ########################################################################
        with open(bib_path, "rt", encoding="utf-8") as f:
            content = f.read()

        use_scholarly = False

        llm_container = Container()
        llm_container.llm_api = llm_api
        cached_llm_container = cw.CacheWrapper(llm_container)

        for i, line in enumerate(content.split("\n")):
            if i < 120:
                # continue
                pass
            if i == 23:
                pass
            if line.startswith("-"):

                message = f"read the bib entry and generate a json file with the fields: citation_number, author, title, \
                    year, journal and fills those if possible. The data type of the field author is always a list \
                    (it might only have one entry or even zero entries). The data type of citation_number is int. \
                    Dont write ````json, just clean json code. \
                    Bib entry: {line}"

                if os.path.isfile(llm_cache_path):
                # todo make a cache for each file, so that you can indepenantly delete them
                    cached_llm_container.load_cache(llm_cache_path)
                res = cached_llm_container.llm_api(message)
                cached_llm_container.save_cache(llm_cache_path)
                # print(res)

                if "`json" in res:
                    res = res.replace("`json", "").replace("`", "")
                info = json.loads(res)

                # skip if dict is empty for some reason (probably bad bib file)
                if not info:
                    continue
                # skip if citation is not in table
                if info["citation_number"] not in relevant_citations:
                    continue

                # get coauthors
                if use_scholarly:
                    pubs = scholarly.search_pubs(info["title"] + " " + info["author"])
                    pub = next(pubs)
                    info["author"] = pub["bib"]["author"]
                else:
                    # get rid of et al
                    if 'et al.' in info["author"]:
                        info["author"].remove('et al.')
                    # ensure compatibility with scholarly
                    pub = {"author_id": ["" for a in info["author"]]}

                # create new author item
                if not isinstance(info["author"], list): info["author"] = [info["author"]]
                for author, author_id in zip(info["author"], pub["author_id"]):
                    if not author in CM.d["items"].keys():
                        if use_scholarly and author_id:
                            auth = scholarly.search_author_id(author_id)
                            message = f"read the following name and generate json code with the fields: title, family_name, given_name and fills those if possible. Dont write ````json, just clean json code. {auth['name']}"
                            res = llm_api(message)
                            name_json = json.loads(res)
                            CM.add_new_item(CM.d, author, "en", {
                                "R4": 'ag.I7435["human"]',
                                "R7781": name_json["family_name"],
                                "R7782": name_json["given_name"],
                                "R3476": author_id,
                                })
                        else:
                            CM.add_new_item(CM.d, author, "en", {"R4": 'ag.I7435["human"]', "R7781": author})

                # create new publication item
                pub_dict = {"R4": 'ag.I6591["source document"]', "citation_number": info["citation_number"]}
                if info["author"]:
                    pub_dict["R8433"] = info["author"]
                if info["title"]:
                    pub_dict["R8434"] = info["title"]
                else:
                    pub_dict["R8434"] = f"No title given {random.randint(int(1e10), int(1e11))}"
                if info["year"]:
                    pub_dict["R8435"] = info["year"]
                pub_id = "publication: " + pub_dict["R8434"]
                CM.add_new_item(CM.d, pub_id, "en", pub_dict)

                # add citation to examined publication
                CM.add_relation_inplace(CM.d["items"][og_pub_id], "R8440", pub_id)


                publist += line + "\n"
                citation_dict[info["citation_number"]] = pub_id

                # save dict
                with open(temp_path, "wt", encoding="utf-8") as f:
                    json.dump(CM.d, f)

        # examine the stacks
        for i, row in df.iterrows():

            cit_numbers = []
            for cn in row["Source"].split(","):
                try:
                    cit_numbers.append(int(cn))
                except ValueError:
                    pass

            # skip row if no stack present
            if row["Stack"].count("/") < 2:
                continue
            # multiple stacks in row
            for stack in row["Stack"].strip().split(","):
                stack = stack.strip().replace("*", "")
                # todo do something with *
                d = {"R4": CM.build_reference("memristor stack", CM.d)}
                CM.add_new_item(CM.d, stack, "en", d)
                for cn in cit_numbers:
                    CM.add_relation_inplace(CM.d["items"][citation_dict[cn]], CM.d["relations"]["has memristor stack"]["key"], stack)

                for i, compound in enumerate(stack.split("/")):
                    d = {"R4": CM.build_reference("stack component", d)}
                    # check if compound already exists
                    ## check if compund is element from omt, elements have R1 full name (eg nickel) and R2060_has_element_symbol relation (eg Ni)
                    for stm in p.ds.relation_statements.get(f"{CM.loaded_modules.omt.__URI__}#R2060"):
                        if stm.object == compound:
                            compound = stm.subject.R1.value
                            break
                    CM.add_new_item(CM.d, compound, "en", d)
                    q = [{CM.d["relations"]["has position"]["key"]: i,
                         CM.d["relations"]["is at outer position"]["key"]: (i==0 or i==len(stack.split("/"))-1)}]
                    CM.add_relation_inplace(CM.d["items"][stack], CM.d["relations"]["has stack component"]["key"], compound, qualifier=q)





    print(CM.render())

if __name__ == "__main__":
    main()