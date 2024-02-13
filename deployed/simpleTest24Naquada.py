from LaplaceAPIClient import *
import os
import json 

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

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
generic_interferometer ps($phi) bsrx($theta, phi_tr=$phi_tr) q[0], q[1], q[2], q[3];

"""

circuit1 = code 
url = "https://api2.anzaetek.com:443/execute"

def interpret_result(y):
    x = json.loads(y)
    #print(repr(x))
    #print(repr(x["samples"]))
    #print(x["samples"]["naquada"])
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

pqueryAssembly(url, UserTokenSerde(user1, token1), 1, "perceval", {"naquada":1}, circuit1, 1000, interpret_result) # type: ignore
