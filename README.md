# Workflow
## prepare documents
1. convert pdf to markdown (using [link](https://github.com/VikParuchuri/marker))
1. extract relevant tables from papers -> `table.md`
    - make sure there is a at least "Source" column with the citation numbers and a "Stack" column with the chemical compounds like this (order does not matter):

        | Source | Stack          | ...  |
        |:-------|:---------------|:-----|
        | 57     | Au/Pd/WOx/Au   | ...  |

    - if nec. use script `sort_table.py` to polish table (only works for table 2019)
        - then polish by hand (delete lines with incomplete data, look for exceptions)
1. manually extract bibliography -> `bib.md`
1. fill out `meta.json` (title authors year)
1. create the following folder structure
````
TODO Treestructure
````
## generate knowledge graphs
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
    - this generates an output file (`output.py`) with the pyirk knowlegde graph
## pose queries
1. run `sparql.py` to see some example queries
    - use `p.rdfstack.query_result_to_table(res)` for pretty results

## visualization
- configure `visu.py` with label und radius