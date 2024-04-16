# This exmaple shows a discrete quantum photonics using our emergfing OQasm standard

import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

code = """
section .config
photon-number: 3
shots: 1000
max-shots: 10000

section .driver
qubo [[-1.0,0.2,2.0], \
      [0.2,-1.1,2.1], \
      [2.0, 2.1,-0.6]];
driver "SLOS";
// "SLOS";
// "qpu:ascella";
// "sim:slos";
// "sim:ascella";
filter-heuristic none;
optimize $all;
section .openoqasm
OPTICQASM 1.0;
generic_interferometer ps($phi) bsrx($theta, phi_tr=$phi_tr) q[0], q[1], q[2];
"""

executor = "perceval"
nqubits = 1
config = {"naquada":1}
nshots = 1000

import requests
import json

url = "https://api2.anzaetek.com:443/execute"

def query24(executor, nqubits, config, nshots, circuit):
    q = {"__class__": "Assembly", 
        "nqubits": nqubits, 
        "executor": executor, 
        "config": config, 
        "circuit": circuit, 
        "nshots": nshots, 
        "user": user1, 
        "token": token1}
    query = {
        'user': user1, 
        'token': token1, 
        'query': json.dumps(q)}

    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    x = json.loads(rv)
    bestX = []
    bestE = 0.0
    for n in x["samples"]["naquada"]:
        #print(repr(n), n[1])
        for k in n[1]:
            #print(k)
            if k[1] < bestE:
                bestE = k[1]
                bestX = k[0]
    print("best: ", bestX, "energy @", bestE)
    return bestX, bestE

res = query24(executor, nqubits, config, nshots, code)
print(repr(res))
