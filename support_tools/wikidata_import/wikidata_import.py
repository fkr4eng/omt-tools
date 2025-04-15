import os
import json
import requests

import time

import cachewrapper as cw


from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()

# SPARQL query to retrieve chemical elements with their symbol, atomic number, and group number
query_elements = """
SELECT ?element ?elementLabel ?symbol ?atomicNumber ?groupNumber WHERE {
    ?element wdt:P31 wd:Q11344;  # Instance of chemical element
        wdt:P246 ?symbol;   # Element symbol
        wdt:P1086 ?atomicNumber.  # Atomic number

OPTIONAL {
    ?element wdt:P361 ?mainGroup.       # Main group

    ?mainGroup p:P31 ?statement1.
    ?statement1 ps:P31 wd:Q83306.  # group
    ?statement1 pq:P1545 ?groupNumber.  # serial

}



    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY ASC(?atomicNumber)
"""

# SPARQL query to retrieve boiling point and melting point for a specific element

# P2101 melting point
# P2102 boiling point
query_properties_template = """

SELECT DISTINCT ?element ?elementLabel ?_temperature ?unit ?unitLabel
WHERE
{


VALUES ?element { __element__ }

# get boiling point with unit
?element p:__temp_property__ ?statement1.
?statement1 ps:__temp_property__ ?_temperature.

?statement1 psv:__temp_property__ ?valueNode.
?valueNode wikibase:quantityUnit ?unit.

SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }

}
"""

# Function to execute SPARQL queries against Wikidata
def execute_sparql_query(query):
    url = "https://query.wikidata.org/sparql"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params={"query": query})
    response.raise_for_status()
    return response.json()

execute_sparql_query = cw.CacheWrapper(execute_sparql_query)

wikidata_sparql_cache = "wikidata_sparql_cache.pcl"

if os.path.isfile(wikidata_sparql_cache):
    execute_sparql_query.load_cache(wikidata_sparql_cache)


# Fetch the list of chemical elements
elements_data = execute_sparql_query(query_elements)

# Process the results to gather additional properties (boiling/melting points)
elements = []
for item in elements_data["results"]["bindings"]:
    element_info = {
        "name": item["elementLabel"]["value"],
        "symbol": item["symbol"]["value"],
        "atomic_number": int(item["atomicNumber"]["value"]),
        "group_number": int(item["groupNumber"]["value"]) if "groupNumber" in item else None,
    }

    print(element_info["symbol"], element_info["atomic_number"])

    # Query for boiling and melting points using the element's Wikidata ID
    element_id = item["element"]["value"].split("/")[-1]

    tmp = query_properties_template.replace("__element__", f"wd:{element_id}")

    query_melting = tmp.replace("__temp_property__", "P2101")
    query_boiling = tmp.replace("__temp_property__", "P2102")

    properties_data_melting = execute_sparql_query(query_melting)
    properties_data_boiling = execute_sparql_query(query_boiling)

    if not execute_sparql_query._last_cache_status:
        time.sleep(3)
        execute_sparql_query.save_cache(wikidata_sparql_cache)

    res = properties_data_melting["results"]["bindings"]
    if res:
      res = res[0]
      element_info["melting_point"] = (res["_temperature"]["value"], res["unitLabel"]["value"])

    res = properties_data_boiling["results"]["bindings"]
    if res:
      res = res[0]
      element_info["boiling_point"] = (res["_temperature"]["value"], res["unitLabel"]["value"])

    elements.append(element_info)

# Save the data to a JSON file with pretty formatting
with open("chemical_elements.json", "w") as json_file:
    json.dump(elements, json_file, indent=4)



print("Data has been saved to 'chemical_elements.json'.")
