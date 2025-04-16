import os

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
visualize("Pt", 1)
visualize("Pt", 2)

IPS()