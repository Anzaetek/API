from dataclasses import dataclass
from typing import Any, Dict, List, Union, cast
import numpy as np
from UserTokenSerde import *
import orjson
import json
from dataclasses_serialization.json import JSONSerializer

# program is min x Q x + L x, st Ax >= b
@dataclass
class SacadosQuadratique:
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde    
    version: str
    # 1D
    b: np.ndarray
    A: np.ndarray
    Q: np.ndarray
    # 1D
    L: np.ndarray
    name: str
    # put 0 if unsure
    itemCount: int
    # put 0 if unsure
    capacity: int
    # put "quadratic"
    solver: str
    items: Dict[str, Any]

@dataclass 
class SacadosQuadratiqueResult:
    rejectedItemIds: List[str]
    status: str
    id: str
    totalValue: Union[float,int]
    totalWeight: Union[float,int]
    solver: str
    selectedItemIds: List[str]
    version: str

#{"rejectedItemIds":["item-2"],"status":"Success","id":"X","totalValue":2.0,"totalWeight":0,"solver":"quadratic","selectedItemIds":["item-1"],"version":"0.1.0"}

@dataclass
class SacadosQuadratiqueSerde:
    Config: Dict[str, Union[str,float,int,dict]]
    Info: UserTokenSerde    
    version: str
    b: List[Union[float,int]]
    A: List[List[Union[float,int]]]
    Q: List[List[Union[float,int]]]
    L: List[Union[float,int]]
    name:str
    itemCount: int
    capacity: int
    solver: str
    items: Dict[str, Dict[str,Union[float,int]]]

def makeSacadosQuadratiqueSerde(m: SacadosQuadratique) -> SacadosQuadratiqueSerde:
    # TODO remove
    # m.Config = {}
    # m.Info = UserTokenSerde("", "")
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    print("s=", s, "m=", m)
    return cast(SacadosQuadratiqueSerde, JSONSerializer.deserialize(SacadosQuadratiqueSerde, json.loads(s)))

def makeSacadosQuadratique(m: SacadosQuadratiqueSerde) -> SacadosQuadratique:
    print("makeSacadosQuadratique", m)
    return SacadosQuadratique(m.Config, m.Info, m.version, # type: ignore
                              np.array(m.b, dtype=np.float64),
                              np.array(m.A, dtype=np.float64),
                              np.array(m.Q, dtype=np.float64),
                              np.array(m.L, dtype=np.float64),
                              m.name, m.itemCount, m.capacity, 
                              m.solver, 
                              m.items)

def serializeSacadosQuadratique(m: SacadosQuadratique) -> str:
    print("serializeSacadosQuadratique", m)
    m2 = makeSacadosQuadratiqueSerde(m) 
    print("m2", m2)  
    query = orjson.dumps(m2).decode("utf-8") 
    print("m2 done")
    return query

def deserializeSacadosQuadratiqueResult(r: str) -> SacadosQuadratiqueResult:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(SacadosQuadratiqueResult, rv)
    print("p1=", p1)
    return cast(SacadosQuadratiqueResult, p1)

def serializeSacadosQuadratiqueProblemQuery(q1: SacadosQuadratique) -> str:
    p2 = makeSacadosQuadratiqueSerde(q1)
    query = '{ "__class__":"SacadosQuadratiqueProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query

def deserializeSacadosQuadratiqueResponse(r: str) -> SacadosQuadratiqueResult:
    return deserializeSacadosQuadratiqueResult(r)
