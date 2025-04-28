# Ontology of Memristor Technology – Tools

This repo contains tools for the creation and maintenance of the Ontology of Memristor Technology (OMT).
The OMT itself is maintained at <https://github.com/fkr4eng/omt>.

## General Information

The OMT consists of bot hand-coded and auto-generated parts.
This repo describes how to reproduce the auto-generated part based on three overview papers:

- Lanza et al. (2019)
- Xia et al. (2019)
- Aguirre et al. (2024)




## Prepare Directory Structure and Documents

**Note:** these steps have already been executed and are committed to the repo.
They are documented for reference and to incorporate further sources for the future.

1. Create the following folder structure (files will be create below):
````
./data
├── 2019_lanza
│   ├── bib.md
│   ├── meta.json
│   └── table.md
├── 2019_xia
│   ├── bib.md
│   ├── meta.json
│   └── table.md
└── 2024_aguirre
    ├── bib.md
    ├── meta.json
    └── table.md
````
1. convert pdf to markdown (using [link](https://github.com/VikParuchuri/marker))
1. extract relevant tables from papers -> `table.md`
    - make sure there is a at least "Source" column with the citation numbers and a "Stack" column with the chemical compounds like this (order does not matter):

        | Source | Stack          | ...  |
        |:-------|:---------------|:-----|
        | 57     | Au/Pd/WOx/Au   | ...  |

    - if nec. use script `sort_table.py` to polish table (only necessary for table 2019_xia)
        - then polish by hand (delete lines with incomplete data, look for exceptions)
1. manually extract bibliography -> `bib.md`
1. fill out `meta.json` (title authors year)

## Generate Knowledge Graphs
1. use formalized natural language to create a statement file with relevant classes and relations, e.g.:
    ```
    - There is a class: 'memristor stack'
    - There is a class: 'stack component'
    - There is a relation: 'has stack component'
    - The type of argument1 of 'has stack component' is 'memristor stack'
    - The result type of 'has stack component' is 'stack component'
    ```
1. parse tables using stafo
    - run `create_memristor_ontology.py` to generate knowledge graph from formalized natural language and extract information from table
        - if the input format is right, this should be completely automatic
    - this generates an output file (`output.py`) with the pyirk knowledge graph
## Pose Queries
1. run `sparql.py` to see some example queries
    - use `p.rdfstack.query_result_to_table(res)` for pretty results

## Visualization
- configure `visu.py` with label und radius