import os

import pyirk as p
from ipydex import IPS

from stafo.utils import config_data

path = "output.py"

mod1 = p.irkloader.load_mod_from_path(path, "mem")
ag_mod = mod1.ag
omt_mod = mod1.omt

# dynamically get the short keys since they might change if the knowledge graph is updated
paper_2019_xia = p.ds.get_item_by_label("publication: Memristive crossbar arrays for brain-inspired computing").short_key
paper_2024_aguirre = p.ds.get_item_by_label("publication: Hardware implementation of memristorbased artificial neural networks").short_key
paper_2019_lanza = p.ds.get_item_by_label("publication: Recommended Methods to Study Resistive Switching Devices").short_key
I_mem_stack = p.ds.get_item_by_label("memristor stack")
I_stack_comp = p.ds.get_item_by_label("stack component")
for k, v in p.ds.relations.items():
    if mod1.__URI__ in k:
        if "has stack component" in v.R1:
            R_has_st_com = k.split("#")[-1]
        elif "has memristor stack" in v.R1:
            R_has_mem_st = k.split("#")[-1]
        elif "has position" in v.R1:
            R_has_pos = k.split("#")[-1]
        elif "is at outer position" in v.R1:
            R_is_outer = k.split("#")[-1]
        elif "has citation id" in v.R1:
            R_cit_id = k.split("#")[-1]
        elif "has internal reference" in v.R1:
            R_int_ref = k.split("#")[-1]

p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True)

################################################################################
# query for Q1
################################################################################

print("Search for publications that appear in multiple overview papers.")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX ag_s: <{ag_mod.__URI__}/STATEMENTS#>
PREFIX ag_p: <{ag_mod.__URI__}/PREDICATES#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?overview_paper1 ?overview_paper2 ?citation_number ?component ?stack
WHERE {{
    ?paper1 ag:R8440__cites ?pub.
    ?paper2 ag:R8440__cites ?pub.

    FILTER (?paper1 != ?paper2)

    ?paper1 mem:{R_int_ref}__has_internal_reference ?overview_paper1.
    ?paper2 mem:{R_int_ref}__has_internal_reference ?overview_paper2.
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True)
res1 = p.rdfstack.perform_sparql_query(qsrc)
table = p.rdfstack.query_result_to_table(res1, labels_only=True)
print(table)
table.to_csv("sparql/res/queryQ1.csv")

#! This might fail, if there are typos in the paper titles.
# Here we checked this manually to make sure.


# determine it programmatically:

p1 = p.ds.get_item_by_label("publication: Memristive crossbar arrays for brain-inspired computing")
p2 = p.ds.get_item_by_label("publication: Hardware implementation of memristorbased artificial neural networks")
p3 =  p.ds.get_item_by_label("publication: Recommended Methods to Study Resistive Switching Devices")

s1 = set(p1.ag__R8440)
s2 = set(p2.ag__R8440)
s3 = set(p3.ag__R8440)

print(s1.intersection(s2))
print(s1.intersection(s3))
print(s2.intersection(s3))

IPS()
