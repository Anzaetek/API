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

knapsack = {
  "version": "0.1.0",
  "name": "Knapsack 1",    
  "itemCount": 20, # should be equal to len(items.keys())
  "capacity" : 600,
  "items": {
    "my-item-0": {
      "value": 8,
      "weight": 76
    },
    "my-item-1": {
      "value": 40,
      "weight": 32
    },
    "my-item-2": {
      "value": 54,
      "weight": 1
    },
    "my-item-3": {
      "value": 55,
      "weight": 34
    },
    "my-item-4": {
      "value": 83,
      "weight": 53
    },
    "my-item-5": {
      "value": 2,
      "weight": 51
    },
    "my-item-6": {
      "value": 78,
      "weight": 59
    },
    "my-item-7": {
      "value": 69,
      "weight": 33
    },
    "my-item-8": {
      "value": 38,
      "weight": 30
    },
    "my-item-9": {
      "value": 30,
      "weight": 53
    },
    "my-item-10": {
      "value": 41,
      "weight": 7
    },
    "my-item-11": {
      "value": 46,
      "weight": 57
    },
    "my-item-12": {
      "value": 19,
      "weight": 80
    },
    "my-item-13": {
      "value": 51,
      "weight": 95
    },
    "my-item-14": {
      "value": 99,
      "weight": 76
    },
    "my-item-15": {
      "value": 44,
      "weight": 27
    },
    "my-item-16": {
      "value": 77,
      "weight": 21
    },
    "my-item-17": {
      "value": 82,
      "weight": 10
    },
    "my-item-18": {
      "value": 37,
      "weight": 87
    },
    "my-item-19": {
      "value": 96,
      "weight": 71
    }
  }
}

solution = solveKnapsack2(knapsack)

print(solution.keys())
totalValue = solution["totalValue"]
totalWeight = solution["totalWeight"]
rejectedItemIds = solution["rejectedItemIds"]
selectedItemIds = solution["selectedItemIds"]

print("totalValue", totalValue)
print("totalWeight", totalWeight)
print("rejectedItemsIds", rejectedItemIds)
print("selectedItemIds", selectedItemIds)

expectedTotalValue = 939
expectedTotalWeight = 598
expectedRejectedItemsIds = ['my-item-9', 'my-item-13', 'my-item-12', 'my-item-0', 'my-item-5']
expectedSelectedItemsIds = ['my-item-18', 'my-item-11', 'my-item-1', 'my-item-8', 'my-item-14', 'my-item-6', 'my-item-19', 'my-item-4', 'my-item-3', 'my-item-15', 'my-item-7', 'my-item-16', 'my-item-10', 'my-item-17', 'my-item-2']

assert(expectedTotalValue == totalValue)
assert(expectedTotalWeight == totalWeight)

for i in expectedRejectedItemsIds:
    assert(i in rejectedItemIds)
for i in rejectedItemIds:
    assert(i in expectedRejectedItemsIds)

for i in expectedSelectedItemsIds:
    assert(i in selectedItemIds)
for i in selectedItemIds:
    assert(i in expectedSelectedItemsIds)
print("ok")