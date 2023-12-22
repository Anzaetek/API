from LaplaceAPIClient import *
import Target as tg
from dataclasses_serialization.json import JSONSerializer
from numpy import array
import os

user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

config_m01_03bis = {
    "configSelect": "gekkoConfig"
}

config_m02_03bis = {
    "configSelect": "defaultConfig",
    "nbits": 8
}

q0 = SolverProblem(tg.Target([], [], {}, {}, {}), 
                   "label('l', minimize(list(x1,x2), (x1 - 0.1)**2)) & label('v', x2 == 1.0) & label('v2', x1 > 0.2)", 
                   ['x1', 'x2'], 
                   {'l': 1.0, 'v': 100.0, 'v2': 1000.0},
                   config_m01_03bis, UserTokenSerde(user1, token1)) # type: ignore
q1 = makeSolverProblemSerde(q0)
print(q1)
print(JSONSerializer.serialize(q1))
q2 = makeSolverProblem(q1)
print(q2)

def queryDone(x: Any) -> None:
    print(x)
    print(x.Results)
    print(x.Results['p'])
    print(x.Results['x1'])
    print(x.Results['x2'])            
    if np.allclose(x.Results['p'], np.array([1.0, 0.2])):
        print("ok")
    else:
        raise Exception('failure')
    if np.allclose(x.Results['x1'], np.array([0.2])):
        print("ok")
    else:
        raise Exception('failure x1')
    if np.allclose(x.Results['x2'], np.array([1.0])):
        print("ok")
    else:
        raise Exception('failure x2')  

pquerySolverProblem("https://api2.anzaetek.com:443/execute", q0, queryDone) 