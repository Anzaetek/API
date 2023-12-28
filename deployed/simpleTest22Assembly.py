from LaplaceAPIClient import *
import os

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

fn = "8.qasm2"
with open(fn, "r") as f:
    circuit1 = f.read()
    print(circuit1) 
    url = "https://api2.anzaetek.com:443/execute"
    pqueryAssembly(url, UserTokenSerde(user1, token1), 8, "qiskit", {}, circuit1, 1024, lambda x: print("qiskit>", x)) # type: ignore
    pqueryAssembly(url, UserTokenSerde(user1, token1), 8, "circ", {}, circuit1, 1024, lambda x: print("circ>", x)) # type: ignore
    pqueryAssembly(url, UserTokenSerde(user1, token1), 8, "qadence", {}, circuit1, 1024, lambda x: print("qadence>", x)) # type: ignore
    pqueryAssembly(url, UserTokenSerde(user1, token1), 4, "spinqit", {}, circuit1, 1024, lambda x: print("spinqit>", x)) # type: ignore
