# This program is a short demo of the usage of the HyperSolver API for Knapsack optimization.
# TODO add bigger examples ~ cf. benchmarks with 'A' + doc: the node version and the Julia version /=

import os
import json
import requests
from typing import cast

HYPERSOLVER_API_URL = 'https://solver.hypersolver.eu:443'
# token = os.getenv("ANZAETEK_HYPERSOLVER_TOKEN")

def solveKnapsack2(ks: dict) -> dict:
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': '_/_',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    url = HYPERSOLVER_API_URL + '/computations/solve'
    payload= json.dumps({ "processingMethodId": "fatal-error", "knapsack": ks})
    r = requests.post(url, data=payload, headers = headers, verify=False)
    data = r.json()
    return cast(dict, data)

path = "examples_knapsacks/knapsack-1961.json"
with open(path, "r") as f:
    ks = json.loads(f.read())

knapsack = ks[0]
print(knapsack.keys())

solution = solveKnapsack2(knapsack)

print(solution.keys())
totalValue = solution["totalValue"]
totalWeight = solution["totalWeight"]
rejectedItemIds = solution["rejectedItemIds"]
selectedItemIds = solution["selectedItemIds"]

assert(len(rejectedItemIds) > 1)
assert(len(selectedItemIds) > 1)

print("totalValue", totalValue)
print("totalWeight", totalWeight)
print("selectedItemIds", selectedItemIds)
print("rejectedItemsIds", rejectedItemIds)

print("ok")