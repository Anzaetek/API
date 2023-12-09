from dataclasses import dataclass
from typing import Any, Dict, List, Union, cast
import numpy as np
from Operators import evalExpr
from TargetOperators import expressionToTarget
from UserTokenSerde import *
import orjson
import json
from dataclasses_serialization.json import JSONSerializer
from Target import *

@dataclass
class QUBOSerde:
    W: List[List[float]]

def makeQUBOSerde(m: QUBO) -> QUBOSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    ## print(m, s)
    return cast(QUBOSerde, JSONSerializer.deserialize(QUBOSerde, json.loads(s)))

def makeQUBO(m: QUBOSerde) -> QUBO:
    return QUBO(np.array(m.W, dtype=float))

# not really serializable
#"""
#@dataclass
#class EmbeddedQUBO:
#    Qubo: QUBO
#    Interpretation: Dict[str, Callable[[np.ndarray],np.ndarray]]
#"""

@dataclass
class EmbeddingSerde:
    Name: str
    W: List[List[float]]

def makeEmbeddingSerde(e: Embedding) -> EmbeddingSerde:
    s = orjson.dumps(e, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(EmbeddingSerde, JSONSerializer.deserialize(EmbeddingSerde, json.loads(s)))    

def makeEmbedding(e: EmbeddingSerde) -> Embedding:
    return Embedding(e.Name, np.array(e.W, dtype=float))

@dataclass 
class TermSerde:
    pass

@dataclass
class MinSerde(Term):
    Coef: str
    Embed: EmbeddingSerde
    Quadratic: List[List[float]]
    Linear: Union[List[float],List[List[float]]]

def makeMinSerde(m: Min) -> MinSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(MinSerde, JSONSerializer.deserialize(MinSerde, json.loads(s)))  

def makeMin(m: MinSerde) -> Min:
    return Min(m.Coef,makeEmbedding(m.Embed), 
                    np.array(m.Quadratic, dtype=float),
                    np.array(m.Linear, dtype=float))

@dataclass 
class MaxSerde(TermSerde):
    Coef: str
    Embed: EmbeddingSerde
    Quadratic: List[List[float]]
    Linear: Union[List[float],List[List[float]]]

def makeMaxSerde(m: Max) -> MaxSerde:
    s = orjson.dumps(m, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(MaxSerde, JSONSerializer.deserialize(MaxSerde, json.loads(s)))  

def makeMax(m: MaxSerde) -> Max:
    return Max(m.Coef,makeEmbedding(m.Embed), 
                    np.array(m.Quadratic, dtype=float),
                    np.array(m.Linear, dtype=float))

@dataclass 
class EqualSerde(TermSerde):
    Coef: str
    Embed: EmbeddingSerde
    Linear: Union[List[float],List[List[float]]]
    Comparand: Union[List[List[float]],List[float]]

def makeEqualSerde(e: Equal) -> EqualSerde:
    s = orjson.dumps(e, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(EqualSerde, JSONSerializer.deserialize(EqualSerde, json.loads(s)))    

def makeEqual(m: EqualSerde) -> Equal:
    return Equal(m.Coef,makeEmbedding(m.Embed), 
                    np.array(m.Linear, dtype=float),
                    np.array(m.Comparand, dtype=float))    

@dataclass
class LessThanSerde(TermSerde):
    Coef: str
    Embed: EmbeddingSerde
    Linear: Union[List[float],List[List[float]]]   
    Comparand: Union[List[List[float]],List[float]]

def makeLessThanSerde(e: LessThan) -> LessThanSerde:
    s = orjson.dumps(e, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(LessThanSerde, JSONSerializer.deserialize(LessThanSerde, json.loads(s)))  

def makeLessThan(m: LessThanSerde) -> LessThan:
    return LessThan(m.Coef,makeEmbedding(m.Embed), 
                    np.array(m.Linear, dtype=float),
                    np.array(m.Comparand, dtype=float))    

@dataclass
class GreaterThanSerde(TermSerde):
    Coef: str
    Embed: EmbeddingSerde
    Linear: Union[List[float],List[List[float]]]
    Comparand: Union[List[List[float]],List[float]]

def makeGreaterThanSerde(e: GreaterThan) -> GreaterThanSerde:
    s = orjson.dumps(e, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(GreaterThanSerde, JSONSerializer.deserialize(GreaterThanSerde, json.loads(s)))  

def makeGreaterThan(m: GreaterThanSerde) -> GreaterThan:
    return GreaterThan(m.Coef,makeEmbedding(m.Embed), 
                    np.array(m.Linear, dtype=float),
                    np.array(m.Comparand, dtype=float))    

@dataclass
class TermSerdeNode(TermSerde):
    maxTerm: List[MaxSerde]
    minTerm: List[MinSerde]
    equalTerm: List[EqualSerde]
    lessThanTerm: List[LessThanSerde]
    greaterThanTerm: List[GreaterThanSerde]

def makeTermSerde(t: Term)->TermSerde:
    maxTerm: List[MaxSerde] = []
    minTerm: List[MinSerde] = []
    equalTerm: List[EqualSerde] = []
    lessThanTerm: List[LessThanSerde] = []
    greaterThanTerm: List[GreaterThanSerde] = []

    if isinstance(t, Max):
        maxTerm = [makeMaxSerde(t)]
    if isinstance(t, Min):
        minTerm = [makeMinSerde(t)]
    if isinstance(t,Equal):
        equalTerm = [makeEqualSerde(t)]
    if isinstance(t,LessThan):
        lessThanTerm = [makeLessThanSerde(t)]
    if isinstance(t,GreaterThan):
        greaterThanTerm = [makeGreaterThanSerde(t)]
    return TermSerdeNode(maxTerm, minTerm, equalTerm, lessThanTerm, greaterThanTerm)

def makeTerm(t: TermSerde)->Term:
    #print("makeTerm>", t)
    assert(isinstance(t, TermSerdeNode))
    tsn = t
    if len(tsn.maxTerm) > 0:
        return makeMax(tsn.maxTerm[0])
    if len(tsn.minTerm) > 0:
        return makeMin(tsn.minTerm[0])
    if len(tsn.equalTerm) > 0:
        return makeEqual(tsn.equalTerm[0])
    if len(tsn.lessThanTerm) > 0:
        return makeLessThan(tsn.lessThanTerm[0])
    if len(tsn.greaterThanTerm) > 0:
        return makeGreaterThan(tsn.greaterThanTerm[0])
    raise Exception("structure is void")

# Interpretation is not easily translatable and thus removed!
#@dataclass
#class Target:
#    Terms: List[Term]
#    Parameters: Dict[str, float]
#    Initialization: Dict[str, Tuple[Embedding, np.ndarray]]
#    Interpretation: Dict[str, Callable[[np.ndarray],np.ndarray]]    

@dataclass
class TargetSerde:
    Terms: List[TermSerdeNode]
    ForceNBits: List[int]
    Parameters: Dict[str, float]
    Initialization: Dict[str, Tuple[EmbeddingSerde, Union[List[float],List[List[float]]]]]

def makeTargetSerde(t: Target) -> TargetSerde:
    #t2 = Target(t.Terms, t.Parameters, t.Initialization, {}) ~ no/no/no
    #s = orjson.dumps(t2, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    #return JSONSerializer.deserialize(TargetSerde, json.loads(s)) 
    init: Dict[str, Tuple[EmbeddingSerde, Union[List[float],List[List[float]]] ]] = {}
    for k in t.Initialization:
        embed, value = t.Initialization[k]
        init[k] = (makeEmbeddingSerde(embed), value.tolist())
    return TargetSerde([cast(TermSerdeNode, makeTermSerde(s)) for s in t.Terms], t.ForceNBits, t.Parameters, init)

def makeTarget(t: TargetSerde) -> Target:
    init: Dict[str, Tuple[Embedding,np.ndarray]] = {}
    for k in t.Initialization:
        embed, value = t.Initialization[k]
        init[k] = (makeEmbedding(embed), np.ndarray(value, dtype=float)) # type: ignore
    return Target([makeTerm(s) for s in t.Terms], t.ForceNBits, t.Parameters, init, {})

# not for now
#"""
#@dataclass
#class EigenSystem:
#    W: np.ndarray
#"""

@dataclass
class SolverProblemSerde:
    Description: TargetSerde
    DescriptionString: str
    DescriptionSymbolList: List[str]
    DescriptionParameters: Dict[str, Union[float,int]]
    Config: Dict[str, Union[str,float,int,dict]]
    Info: UserTokenSerde

def makeSolverProblemSerde(p: SolverProblem) -> SolverProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return SolverProblemSerde(makeTargetSerde(p.Description), p.DescriptionString, p.DescriptionSymbolList, p.DescriptionParameters, p.Config, p.Info) # type: ignore

def makeSolverProblem(p: SolverProblemSerde) -> SolverProblem:
    sp = SolverProblem(makeTarget(p.Description), p.DescriptionString, p.DescriptionSymbolList, p.DescriptionParameters, p.Config, p.Info) # type: ignore
    if p.DescriptionString != "":
        t2 = evalExpr(p.DescriptionString, p.DescriptionSymbolList, {})
        sp.Description = expressionToTarget(t2, p.DescriptionParameters) 
    sp.Description.Interpretation['p'] = lambda x:x
    return sp

# solve:  -> Dict[str,np.ndarray]:
@dataclass
class SolverSolutionSerde:
    Results: Dict[str, Union[List[float],List[List[float]]]]
    Status: OperationStatusSerde

def makeSolverSolutionSerde(s: SolverSolution) -> SolverSolutionSerde:
    ss = orjson.dumps(s, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(SolverSolutionSerde, JSONSerializer.deserialize(SolverSolutionSerde, json.loads(ss)))

def makeSolverSolution(s: SolverSolutionSerde) -> SolverSolution:
    res: Dict[str,np.ndarray] = {}
    for k in s.Results:
        res[k] = np.array(s.Results[k], dtype=float)
    return SolverSolution(res, s.Status)

@dataclass
class ExtractQUBOSerde:
    Description: TargetSerde
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde

def makeExtractQUBOSerde(e: ExtractQUBO) -> ExtractQUBOSerde:
    #s = orjson.dumps(e, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    #return JSONSerializer.deserialize(SolverSolutionSerde, json.loads(s))   
    return ExtractQUBOSerde(makeTargetSerde(e.Description), e.Config, e.Info)

def makeExtractQUBO(e: ExtractQUBOSerde) -> ExtractQUBO:
    return ExtractQUBO(makeTarget(e.Description), e.Config, e.Info)

@dataclass
class QUBOSolutionSerde:
    Qubo: QUBOSerde
    Status: OperationStatusSerde

def makeQUBOSolutionSerde(q: QUBOSolution) -> QUBOSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(QUBOSolutionSerde, JSONSerializer.deserialize(QUBOSolutionSerde, json.loads(s)))

def makeQUBOSolution(q: QUBOSolutionSerde) -> QUBOSolution:
    return QUBOSolution(makeQUBO(q.Qubo), q.Status)

def serializeSolverProblemQuery(p: SolverProblem) -> str:
    p2 = makeSolverProblemSerde(p)
    query = '{ "__class__":"SolverProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query

def serializeExtractQUBOQuery(q: ExtractQUBO) -> str:
    q2 = makeExtractQUBOSerde(q)
    query = '{ "__class__":"ExtractQUBO", "query":' + orjson.dumps(q2).decode("utf-8") + '}'
    #print(query)
    return query    

def deserializeSolverSolutionResponse(r: str) -> SolverSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(SolverSolutionSerde, rv)
    #print(p1)
    p2 = makeSolverSolution(p1)
    return p2

def deserializeQUBOSolutionResponse(r: str) -> QUBOSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(QUBOSolutionSerde, rv)
    p2 = makeQUBOSolution(p1)
    return p2    

@dataclass 
class QUBOSolverProblemSerde:
    Qubo: QUBOSerde
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde

def makeQUBOSolverProblemSerde(p: QUBOSolverProblem) -> QUBOSolverProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return QUBOSolverProblemSerde(makeQUBOSerde(p.Qubo), p.Config, p.Info)

def makeQUBOSolverProblem(p: QUBOSolverProblemSerde) -> QUBOSolverProblem:
    sp = QUBOSolverProblem(makeQUBO(p.Qubo),p.Config, p.Info)
    return sp

@dataclass
class QUBOSolverSolutionSerde:
    Results: Dict[str, Union[List[float],List[List[float]]]]
    Status: OperationStatusSerde

def makeQUBOSolverSolutionSerde(q: QUBOSolverSolution) -> QUBOSolverSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(QUBOSolverSolutionSerde, JSONSerializer.deserialize(QUBOSolverSolutionSerde, json.loads(s)))

def makeQUBOSolverSolution(q: QUBOSolverSolutionSerde) -> QUBOSolverSolution:
    res: Dict[str,np.ndarray] = {}
    for k in q.Results:
        res[k] = np.array(q.Results[k], dtype=float)
    return QUBOSolverSolution(res, q.Status)

def serializeQUBOSolverProblemQuery(p: QUBOSolverProblem) -> str:
    p2 = makeQUBOSolverProblemSerde(p)
    query = '{ "__class__":"QUBOSolverProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query
 
def deserializeQUBOSolverSolutionResponse(r: str) -> QUBOSolverSolution:
    print(r)
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(QUBOSolverSolutionSerde, rv)
    #print(p1)
    p2 = makeQUBOSolverSolution(p1)
    return p2

@dataclass
class QRNGProblemSerde:
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde

def makeQRNGProblemSerde(p: QRNGProblem) -> QRNGProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return QRNGProblemSerde(p.Config, p.Info)

def makeQRNGProblem(p: QRNGProblemSerde) -> QRNGProblem:
    sp = QRNGProblem(p.Config, p.Info)
    return sp

@dataclass 
class QRNGSolutionSerde:
    Results: Dict[str, Union[str, float, int, List[float],List[List[float]]]]
    Status: OperationStatusSerde   

def makeQRNGSolutionSerde(q: QRNGSolution) -> QRNGSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(QRNGSolutionSerde, JSONSerializer.deserialize(QRNGSolutionSerde, json.loads(s)))

def makeQRNGSolution(q: QRNGSolutionSerde) -> QRNGSolution:
    #res: Dict[str,np.ndarray] = {}
    #for k in s.Results:
    #    res[k] = np.array(q.Results[k], dtype=float)
    oups = cast(Dict[str, Union[str, float, int, np.ndarray]], q.Results) # TODO: one day we will fix
    return QRNGSolution(oups, q.Status)

def serializeQRNGProblemQuery(p: QRNGProblem) -> str:
    p2 = makeQRNGProblemSerde(p)
    query = '{ "__class__":"QRNGProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query
 
def deserializeQRNGSolutionResponse(r: str) -> QRNGSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(QRNGSolutionSerde, rv)
    #print(p1)
    p2 = makeQRNGSolution(p1)
    return p2

@dataclass
class SibeliusProblemSerde:
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde
    SibeliusString: str

def makeSibeliusProblemSerde(p: SibeliusProblem) -> SibeliusProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return SibeliusProblemSerde(p.Config, p.Info, p.SibeliusString)

def makeSibeliusProblem(p: SibeliusProblemSerde) -> SibeliusProblem:
    sp = SibeliusProblem(p.Config, p.Info, p.SibeliusString)
    return sp

@dataclass 
class SibeliusSolutionSerde:
    Results: Dict[str, Union[str, float, int, List[float],List[List[float]]]]
    Status: OperationStatusSerde   

def makeSibeliusSolutionSerde(q: SibeliusSolution) -> SibeliusSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(SibeliusSolutionSerde, JSONSerializer.deserialize(SibeliusSolutionSerde, json.loads(s)))

def makeSibeliusSolution(q: SibeliusSolutionSerde) -> SibeliusSolution:
    #res: Dict[str,np.ndarray] = {}
    #for k in s.Results:
    #    res[k] = np.array(q.Results[k], dtype=float)
    oups = cast(Dict[str, Union[str, float, int, np.ndarray]], q.Results) # TODO: one day we will fix
    return SibeliusSolution(oups, q.Status)

def serializeSibeliusProblemQuery(p: SibeliusProblem) -> str:
    p2 = makeSibeliusProblemSerde(p)
    query = '{ "__class__":"SibeliusProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query
 
def deserializeSibeliusSolutionResponse(r: str) -> SibeliusSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(SibeliusSolutionSerde, rv)
    #print(p1)
    p2 = makeSibeliusSolution(p1)
    return p2

@dataclass
class MLTrainingProblemSerde:
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde
    Tag: str
    Features: List[Union[str,float,int, List[Union[str,float,int]]]]
    Labels: List[Union[str,float,int, List[Union[str,float,int]]]]
    TestFeatures: List[Union[str,float,int, List[Union[str,float,int]]]]
    TestLabels: List[Union[str,float,int, List[Union[str,float,int]]]]

def makeMLTrainingProblemSerde(p: MLTrainingProblem) -> MLTrainingProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return MLTrainingProblemSerde(p.Config, p.Info, p.Tag, p.Features, p.Labels, p.TestFeatures, p.TestLabels)

def makeMLTrainingProblem(p: MLTrainingProblemSerde) -> MLTrainingProblem:
    sp = MLTrainingProblem(p.Config, p.Info, p.Tag, p.Features, p.Labels, p.TestFeatures, p.TestLabels)
    return sp
    
@dataclass 
class MLTrainingSolutionSerde:
    Results: Dict[str, Union[str, float, int, dict, List[float],List[List[float]]]]
    Status: OperationStatusSerde   

def makeMLTrainingSolutionSerde(q: MLTrainingSolution) -> MLTrainingSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    return cast(MLTrainingSolutionSerde, JSONSerializer.deserialize(MLTrainingSolutionSerde, json.loads(s)))

def makeMLTrainingSolution(q: MLTrainingSolutionSerde) -> MLTrainingSolution:
    #res: Dict[str,np.ndarray] = {}
    #for k in s.Results:
    #    res[k] = np.array(q.Results[k], dtype=float)
    oups = cast(Dict[str, Union[str, float, int, np.ndarray, dict, list]], q.Results) # TODO: one day we will fix
    return MLTrainingSolution(oups, q.Status)

def serializeMLTrainingProblemQuery(p: MLTrainingProblem) -> str:
    p2 = makeMLTrainingProblemSerde(p)
    query = '{ "__class__":"MLTrainingProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query
 
def deserializeMLTrainingSolutionResponse(r: str) -> MLTrainingSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(MLTrainingSolutionSerde, rv)
    #print(p1)
    p2 = makeMLTrainingSolution(p1)
    return p2

@dataclass
class MLInferenceProblemSerde:
    Config: Dict[str, Union[str,float,int]]
    Info: UserTokenSerde
    Tag: str
    Features: List[Union[str,float,int, List[Union[str,float,int]]]]
  
def makeMLInferenceProblemSerde(p: MLInferenceProblem) -> MLInferenceProblemSerde:
    # orjson.dumps(p, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    # return JSONSerializer.deserialize(SolverProblemSerde, json.loads(s))  
    return MLInferenceProblemSerde(p.Config, p.Info, p.Tag, p.Features)

def makeMLInferenceProblem(p: MLInferenceProblemSerde) -> MLInferenceProblem:
    sp = MLInferenceProblem(p.Config, p.Info, p.Tag, p.Features)
    return sp
 
@dataclass 
class MLInferenceSolutionSerde:
    Results: Dict[str, Union[str, float, int, List[float],List[List[float]], dict]]
    Status: OperationStatusSerde
    Labels: List[Union[str,float,int, List[Union[str,float,int]]]]

def makeMLInferenceSolutionSerde(q: MLInferenceSolution) -> MLInferenceSolutionSerde:
    s = orjson.dumps(q, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
    #print("deserialize ~ ", s)
    return cast(MLInferenceSolutionSerde, JSONSerializer.deserialize(MLInferenceSolutionSerde, json.loads(s)))

def makeMLInferenceSolution(q: MLInferenceSolutionSerde) -> MLInferenceSolution:
    #res: Dict[str,np.ndarray] = {}
    #for k in s.Results:
    #    res[k] = np.array(q.Results[k], dtype=float)
    oups = cast(Dict[str, Union[str, float, int, np.ndarray, dict]], q.Results) # TODO: one day we will fix
    return MLInferenceSolution(oups, q.Status, q.Labels)

def serializeMLInferenceProblemQuery(p: MLInferenceProblem) -> str:
    p2 = makeMLInferenceProblemSerde(p)
    query = '{ "__class__":"MLInferenceProblem", "query":' + orjson.dumps(p2).decode("utf-8") + '}'
    return query
 
def deserializeMLInferenceSolutionResponse(r: str) -> MLInferenceSolution:
    rv = json.loads(r)
    p1 = JSONSerializer.deserialize(MLInferenceSolutionSerde, rv)
    #print(p1)
    p2 = makeMLInferenceSolution(p1)
    return p2
