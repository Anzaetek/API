from dataclasses import dataclass
from typing import Any, Dict, List, Union, cast
import numpy as np
from UserTokenSerde import *
import orjson
import json
from dataclasses_serialization.json import JSONSerializer

@dataclass
class Markowitz:
    # min_p (w - p)^T S (w-p)
    # s.t. sum_i(p_i) = 1
    S: np.ndarray
    w: np.ndarray

@dataclass
class MarkowitzSerde:
    S: List[List[Union[float,int]]]
    w: List[Union[float,int]]

def makeMarkowitzSerde(m: Markowitz) -> MarkowitzSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(MarkowitzSerde, JSONSerializer.deserialize(MarkowitzSerde, json.loads(s)))

def makeMarkowizt(m: MarkowitzSerde) -> Markowitz:
    return Markowitz(np.array(m.S, dtype=float), np.array(m.w, dtype=float))

@dataclass
class MarkowitzSolution:
    p: np.ndarray
    status: OperationStatusSerde

@dataclass
class MarkowitzSolutionSerde:
    p: List[Union[float,int]]
    status: OperationStatusSerde

def makeMarkowitzSolutionSerde(m: MarkowitzSolution) -> MarkowitzSolutionSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    #print("mms:", s)
    return cast(MarkowitzSolutionSerde, JSONSerializer.deserialize(MarkowitzSolutionSerde, json.loads(s)))

def makeMarkowitzSolution(m: MarkowitzSolutionSerde) -> MarkowitzSolution:
    #print("solution => ", ParamSpec)
    return MarkowitzSolution(np.array(m.p, dtype=float), m.status)

@dataclass
class MarkowitzProblem:
    m: Markowitz
    config: Dict[str, Union[str,float,int]]
    info: UserTokenSerde

@dataclass 
class MarkowitzProblemSerde:
    m: MarkowitzSerde
    config: Dict[str, Union[str,float,int]]
    info: UserTokenSerde

def makeMarkowitzProblemSerde(m: MarkowitzProblem) -> MarkowitzProblemSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(MarkowitzProblemSerde, JSONSerializer.deserialize(MarkowitzProblemSerde, json.loads(s)))

def makeMarkowitzProblem(m: MarkowitzProblemSerde) -> MarkowitzProblem:
    return MarkowitzProblem(makeMarkowizt(m.m), m.config, m.info)

def serializeMarkowitzProblemQuery(m: MarkowitzProblem) -> str:
    m2 = makeMarkowitzProblemSerde(m)   
    query = '{ "__class__":"MarkowitzProblem", "query":' + orjson.dumps(m2).decode("utf-8")  + '}'
    return query

def deserializeMarkowitzSolutionResponse(r: str) -> MarkowitzSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(MarkowitzSolutionSerde, rv)
    print("p1=", p1)
    s2 = makeMarkowitzSolution(p1)
    return s2