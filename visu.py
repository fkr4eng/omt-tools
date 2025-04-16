import os

from packaging import version
import pyirk as p

from ipydex import IPS


path = "output.py"

mod1 = p.irkloader.load_mod_from_path(path, "mem")

os.makedirs("vis", exist_ok=True)

def visualize(label, radius):
    uri = p.ds.get_item_by_label(label).uri
    vis = p.visualize_entity(uri, radius=radius)
    with open(f"vis/visu_{label}_r{radius}.svg", "wt", encoding="utf-8") as f:
        f.write(vis)

###################
visualize("platinum", 1)
visualize("platinum", 2)



def prepare_graph():
    """
    Delete some entities from OCSE (e.g. control-theory related persons).

    Motivation: We use the ocse-agent-module e.g. to model authors of Memristor-papers;
    However we do not need to include the humans modeled in that module.
    """

    print("select human-instances from ocse/agents1.py")
    humans_to_delete = []

    assert version.parse(p.__version__) >= version.parse("0.14.2")


    for human in mod1.ag.I7435.get_inv_relations("R4", return_subj=True):
        if mod1.ag.__URI__ in human.uri:
            humans_to_delete.append(human)

    for human in humans_to_delete:
        p.ds.statements.pop(human.uri)
        p.ds.items.pop(human.uri)

    return None



def visualize_whole_graph():
    prepare_graph()

    vis = p.visualize_all_entities()
    with open(f"vis/whole_graph.svg", "wt", encoding="utf-8") as f:
        f.write(vis)

visualize_whole_graph()



literal_statements = []
entity_statements = []
qualifier_statements = []
remaining_statements = []

for stm_dict in p.ds.statements.values():
    for stm_list in stm_dict.values():
        for stm in stm_list:
            if isinstance(stm, p.QualifierStatement):
                qualifier_statements.append(stm)
            elif isinstance(stm.object, (p.Literal, bool, str, int, float)):
                literal_statements.append(stm)
            elif isinstance(stm.object, p.Entity):
                entity_statements.append(stm)
            else:
                remaining_statements.append(stm)

print(f"{len(literal_statements)=}")
print(f"{len(entity_statements)=}")
print(f"{len(qualifier_statements)=}")
print(f"{len(remaining_statements)=}")
print(f"{len(p.ds.items)=}")
IPS()
