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

p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True)

IPS()
exit()

################################################################################
# queries
################################################################################

print("papers with the same authors")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?o1 ?o2 ?aut
WHERE {{
    mem:{paper_2019_xia} ag:R8440__cites ?o1.
    ?o1 ag:R8433__has_authors ?aut.
    mem:{paper_2024_aguirre} ag:R8440__cites ?o2.
    ?o2 ag:R8433__has_authors ?aut.
}}
"""
res2 = res1 = p.rdfstack.perform_sparql_query(qsrc)
print("Results:", len(res2))

# IPS()

print("papers with same memristor stacks")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?paper1 ?paper2 ?pub1 ?pub2 ?stack
WHERE {{
    ?paper1 ag:R8440__cites ?pub1.
    ?paper2 ag:R8440__cites ?pub2.
    ?pub1 mem:{R_has_mem_st} ?stack.
    ?pub2 mem:{R_has_mem_st} ?stack.
}}
"""
res = p.ds.rdfgraph.query(qsrc)
res2 = p.aux.apply_func_to_table_cells(p.rdfstack.convert_from_rdf_to_pyirk, res)
print("Results:", len(res2))

print("papers from both tables with 2 overlapping components in stack, discounting order")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?pub1 ?pub2 ?stack1 ?stack2 ?comp1 ?comp2
WHERE {{
    mem:{paper_2019_xia} ag:R8440__cites ?pub1.
    ?pub1 mem:{R_has_mem_st} ?stack1.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp1.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp2.

    mem:{paper_2024_aguirre} ag:R8440__cites ?pub2.
    ?pub2 mem:{R_has_mem_st} ?stack2.
    ?stack2 mem:{R_has_st_com}__has_stack_component ?comp1.
    ?stack2 mem:{R_has_st_com}__has_stack_component ?comp2.

    FILTER(?comp1 != ?comp2)
}}
"""

print("Stacks with Ti as top electrode")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?stack1 ?comp1
WHERE {{
    ?pub1 mem:{R_has_mem_st} ?stack1.
    ?stack1 :R4 mem:{I_mem_stack}.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp1.

    ?comp1 :R1


}}
"""


res = p.ds.rdfgraph.query(qsrc)
res2 = p.aux.apply_func_to_table_cells(p.rdfstack.convert_from_rdf_to_pyirk, res)
print("Results:", len(res2))

print("papers from both tables with 3 overlapping components in stack, discounting order")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?pub1 ?pub2 ?stack1 ?stack2 ?comp1 ?comp2 ?comp3
WHERE {{
    mem:{paper_2019_xia} ag:R8440__cites ?pub1.
    ?pub1 mem:{R_has_mem_st} ?stack1.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp1.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp2.
    ?stack1 mem:{R_has_st_com}__has_stack_component ?comp3.

    mem:{paper_2024_aguirre} ag:R8440__cites ?pub2.
    ?pub2 mem:{R_has_mem_st} ?stack2.
    ?stack2 mem:{R_has_st_com}__has_stack_component ?comp1.
    ?stack2 mem:{R_has_st_com}__has_stack_component ?comp2.
    ?stack2 mem:{R_has_st_com}__has_stack_component ?comp3.

    FILTER(?comp1 != ?comp2)
    FILTER(?comp1 != ?comp3)
    FILTER(?comp3 != ?comp3)
}}
"""
res = p.ds.rdfgraph.query(qsrc)
res2 = p.aux.apply_func_to_table_cells(p.rdfstack.convert_from_rdf_to_pyirk, res)
print("Results:", len(res2))

print("stacks with 3 components")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
SELECT ?stack1 ?comp1
WHERE {{
    SELECT (COUNT(*) AS ?comp1Count)
    WHERE {{
        ?stack1 mem:{R_has_st_com}__has_stack_component ?comp1 .
    }}
    GROUP BY ?stack1
    HAVING (?comp1Count = 3)
}}
"""
res = p.ds.rdfgraph.query(qsrc)
res2 = p.aux.apply_func_to_table_cells(p.rdfstack.convert_from_rdf_to_pyirk, res)
print("Results:", len(res2))

print("stacks with TiN in the first layer")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?stack1 ?comp1 ?pos
WHERE {{
    ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm.
    ?stm mem_p:{R_has_st_com}__has_stack_component omt:I6118.
    ?stm qf:{R_has_pos}__has_position 0.
    ?stm qf:{R_is_outer}__is_at_outer_position True.
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True, modfilter=mod1.__URI__)
res1 = p.rdfstack.perform_sparql_query(qsrc)
print("Results:", len(res1))


print("stacks with alloy in the first layer")
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?stack1 ?comp1 ?pos
WHERE {{
    ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm.
    ?stm mem_p:{R_has_st_com}__has_stack_component ?comp1.
    ?stm qf:{R_has_pos}__has_position 0.
    ?stm qf:{R_is_outer}__is_at_outer_position True.
    ?comp1 ?p omt:I5340__alloy. # alloy
    FILTER (?p IN (:R4, :R30))
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True, modfilter=set((mod1.__URI__, omt_mod.__URI__)))
res1 = p.rdfstack.perform_sparql_query(qsrc)

print("From both tables, find a publication that describes a stack. Both of those stacks shall have the same first component and same last component and the same number of components.")
#! working ~1minute
qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?pub1 ?pub2 ?stack1 ?stack2 ?comp1 ?comp2 ?pos1a ?pos2a ?pos1b ?pos2b
WHERE {{
  mem:{paper_2019_xia} ag:R8440__cites ?pub1.
  ?pub1 mem:{R_has_mem_st} ?stack1.

  mem:{paper_2024_aguirre} ag:R8440__cites ?pub2.
  ?pub2 mem:{R_has_mem_st} ?stack2.

  {{
    SELECT ?stack1 ?comp1 ?comp2 ?pos1a ?pos2a
    WHERE {{
      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm1.
      ?stm1 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position ?pos1a;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm2.
      ?stm2 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos2a;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(?pos1a != ?pos2a)
    }}
  }}

  {{
    SELECT ?stack2 ?comp1 ?comp2 ?pos1b ?pos2b
    WHERE {{
      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm3.
      ?stm3 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position ?pos1b;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm4.
      ?stm4 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos2b;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(?pos1b != ?pos2b)
    }}
  }}
  FILTER(?pos1a = ?pos1b && ?pos2a = ?pos2b)
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True, modfilter=mod1.__URI__)
res2 = p.rdfstack.perform_sparql_query(qsrc)


print("From both tables, find a publication that describes a stack. Both of those stacks shall have the same first component and same last component.")

qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?pub1 ?pub2 ?stack1 ?stack2 ?comp1 ?comp2 ?pos1b ?pos2b
WHERE {{
  mem:{paper_2019_xia} ag:R8440__cites ?pub1.
  ?pub1 mem:{R_has_mem_st}__has_memristor_stack ?stack1.

  mem:{paper_2024_aguirre} ag:R8440__cites ?pub2.
  ?pub2 mem:{R_has_mem_st}__has_memristor_stack ?stack2.

  {{
    SELECT ?stack1 ?comp1 ?comp2 ?pos1b
    WHERE {{
      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm1.
      ?stm1 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position 0;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm2.
      ?stm2 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos1b;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(0 != ?pos1b)
    }}
  }}

  {{
    SELECT ?stack2 ?comp1 ?comp2 ?pos2b
    WHERE {{
      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm3.
      ?stm3 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position 0;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm4.
      ?stm4 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos2b;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(0 != ?pos2b)
    }}
  }}
#   FILTER(?pos1b = ?pos2b) # remove this to match stacks of different lengths
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True, modfilter=mod1.__URI__)
res2 = p.rdfstack.perform_sparql_query(qsrc)
table = p.rdfstack.query_result_to_table(res2)



print("From two different overview papers, find a publication each that describes a stack. Both of those stacks shall have the same first component and the same last component.")

qsrc = f"""
PREFIX : <{p.rdfstack.IRK_URI}>
PREFIX qf: <{mod1.__URI__}/QUALIFIERS#>
PREFIX mem: <{mod1.__URI__}#>
PREFIX ag: <{ag_mod.__URI__}#>
PREFIX omt: <{omt_mod.__URI__}#>
PREFIX mem_s: <{mod1.__URI__}/STATEMENTS#>
PREFIX mem_p: <{mod1.__URI__}/PREDICATES#>
SELECT ?paper1 ?paper2 ?pub1 ?pub2 ?stack1 ?stack2 ?comp1 ?comp2 ?pos1b ?pos2b
WHERE {{
  ?paper1 ag:R8440__cites ?pub1.
  ?pub1 mem:{R_has_mem_st}__has_memristor_stack ?stack1.

  ?paper2 ag:R8440__cites ?pub2.
  ?pub2 mem:{R_has_mem_st}__has_memristor_stack ?stack2.

  FILTER (?paper1 != ?paper2)

  {{
    SELECT ?stack1 ?comp1 ?comp2 ?pos1b
    WHERE {{
      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm1.
      ?stm1 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position 0;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack1 mem_s:{R_has_st_com}__has_stack_component ?stm2.
      ?stm2 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos1b;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(0 != ?pos1b)
    }}
  }}

  {{
    SELECT ?stack2 ?comp1 ?comp2 ?pos2b
    WHERE {{
      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm3.
      ?stm3 mem_p:{R_has_st_com}__has_stack_component ?comp1;
             qf:{R_has_pos}__has_position 0;
             qf:{R_is_outer}__is_at_outer_position True.

      ?stack2 mem_s:{R_has_st_com}__has_stack_component ?stm4.
      ?stm4 mem_p:{R_has_st_com}__has_stack_component ?comp2;
             qf:{R_has_pos}__has_position ?pos2b;
             qf:{R_is_outer}__is_at_outer_position True.

      FILTER(0 != ?pos2b)
    }}
  }}
#   FILTER(?pos1b = ?pos2b) # remove this to match stacks of different lengths
}}
"""
p.ds.rdfgraph = p.rdfstack.create_rdf_triples(add_qualifiers=True, modfilter=mod1.__URI__)
res2 = p.rdfstack.perform_sparql_query(qsrc)
table = p.rdfstack.query_result_to_table(res2)
with open("sparql_res/From two different overview papers, find a publication that describes a stack. Both of those stacks shall have the same first component and same last component.csv", "wt") as f:
    table.to_csv(f)


IPS()
