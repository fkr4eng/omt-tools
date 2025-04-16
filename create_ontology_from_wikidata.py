import pyirk as p
import os, sys
import re
from ipydex import IPS, Container, activate_ips_on_exception
import json
import pandas as pd
import cachewrapper as cw


from stafo.utils import BASE_DIR, CONFIG_PATH, render_template, config_data
from stafo.core import llm_api
from stafo.statement_to_kg import ConversionManager

activate_ips_on_exception()


llm_cache_path = "llm_cache.pcl"


if omt_path := config_data.get("omt_path"):
    omt_path = os.path.join(omt_path, "omt.py")
    assert os.path.isfile(omt_path)
else:
    # use hardcoded fallback
    omt_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "omt")), "omt.py")


omt_load_dict = {"path": omt_path, "prefix": "omt", "module_name": "omt"}

# not so elegant but we load the omt module already to get its uri, to generate keys compatible with that module
omt = p.irkloader.load_mod_from_path(omt_path, "omt")
mod_uri = omt.__URI__


def set_temperature(source_dict: dict, key: str, target_dict: dict, new_key: str):
    """
    Assign melting_temperature or boiling_temperature in `target_dict` if it exists in the source_dict
    Also: convert all units to Kelvin
    """

    assert key in ("melting_point", "boiling_point")
    res = source_dict.get(key)
    if not res:
        return

    # expect res to be like ['-363', 'degree Fahrenheit']
    value, unit_label = res

    # unfortunately unit_labels do not follow a strict schema
    # assert unit_label in ("degree Fahrenheit", "degree Celsius", "degree Kelvin")

    unit_label = unit_label.split(" ")[-1].lower()
    assert unit_label in ("fahrenheit", "celsius", "kelvin")

    value = float(value)
    if unit_label == "fahrenheit":
        value = (value - 32)*5/9 + 273.15
    elif unit_label == "celsius":
        value += 273.15
        pass

    target_dict[new_key] = round(value, 2)



def main():
    ag_load_dict = {"path": os.path.join(config_data["ocse_path"], "agents1.py"), "prefix": "ag", "module_name": "agents"}

    CM = ConversionManager(
        "formalized_statements.md",
        num_keys=1000,
        load_irk_modules=[ag_load_dict, omt_load_dict],
        mod_uri=mod_uri,
    )

    with p.uri_context(mod_uri):
        CM.step1_init()
        # CM.step2_parse_fnl()

    CM.current_snippet = "mem"
    CM.default_language = "en"

    json_fpath = "./support_tools/wikidata_import/chemical_elements.json"
    with open(json_fpath) as fp:
        data: list[dict] = json.load(fp)

    # elements above this number are not interesting (they are unstable anyway)
    limit_atomic_number = 100
    entry: dict
    for entry in data[:limit_atomic_number]:
        # d__XXX = {"R4": CM.build_reference("chemical element", CM.d)}


        # TODO: this should probably be taken from `omt` directly?
        add_stmts = {
            "R4": 'omt.I6205["chemical element"]',

            # this requires stafo >= 0.1.1 (due to hardcoded relations)
            "R2060": f'"{entry["symbol"]}"',
            "R2061": entry["atomic_number"],
            "R2062": entry["group_number"],
        }

        set_temperature(entry, "melting_point", add_stmts, "R2063")
        set_temperature(entry, "boiling_point", add_stmts, "R2064")

        CM.add_new_item(CM.d, entry["name"], "en", additional_relations=add_stmts)
        CM.add_relation_inplace(CM.d["items"][entry["name"]], "omt__R2061__has_atomic_number", entry["atomic_number"])

    # apply replacements which simplify copy-pasting
    CM.render(final_replacements=[("=omt.", "="), ("omt__", ""), ("\n\n# mem", "")])

    IPS()


if __name__ == "__main__":
    main()
