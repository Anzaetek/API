from LaplaceAPIClient import *
import os

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

def queryDone21(r1: SacadosQuadratiqueResult) -> None:
    print("knapsack result", r1)
    xref = {'rejectedItemIds': ['my-item-0', 'my-item-12', 'my-item-13', 'my-item-5', 'my-item-9'], 'status': 'Success', 'id': 'X', 'totalValue': 939, 'totalWeight': 0, 'solver': 'linear', 'selectedItemIds': ['my-item-1', 'my-item-10', 'my-item-11', 'my-item-14', 'my-item-15', 'my-item-16', 'my-item-17', 'my-item-18', 'my-item-19', 'my-item-2', 'my-item-3', 'my-item-4', 'my-item-6', 'my-item-7', 'my-item-8'], 'version': '0.1.0'}
    if not (r1.totalValue == xref["totalValue"]):
        raise Exception('failure')
    if not (len(r1.selectedItemIds) == len(xref["selectedItemIds"])): # type: ignore
        raise Exception('failure')
    for i in xref["selectedItemIds"]: # type: ignore
        if not(i in r1.selectedItemIds):
            raise Exception('failure')
    if not(len(r1.rejectedItemIds) == len(xref["rejectedItemIds"])): # type: ignore
        raise Exception('failure')
    for i in xref["rejectedItemIds"]: #type: ignore
        if not(i in r1.rejectedItemIds):
            raise Exception('failure')

config : dict = {}
q21 = SacadosQuadratique(config, UserTokenSerde(user1, token1),  version="0", # type: ignore
                            b=np.array([], dtype=float),
                            A=np.array([], dtype=float),
                            Q=np.array([], dtype=float),
                            L=np.array([], dtype=float),
                            name="", itemCount=20, capacity=600, solver="linear", items={"my-item-0": {
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
                            })

pquerySacadosQuadratiqueProblem("https://api2.anzaetek.com:443/execute", q21, queryDone21)
