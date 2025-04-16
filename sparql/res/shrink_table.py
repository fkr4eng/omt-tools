import pandas as pd
import os
from ipydex import IPS


with open("sparql_res/From two tables, find a publication each that describes a stack. Both of those stacks shall have the same first component and same last component.csv", "rt")as f:
    df = pd.read_csv(f)

df = df.drop("Unnamed: 0", axis=1)
for i, row in df.iterrows():
    if i == 0:
        last_row = row
    else:
        if all(row == last_row):
            df = df.drop(i)
        else:
            last_row = row
IPS()
with open("sparql_res/pairwise same ends.csv", "wt") as f:
    df.to_csv(f)