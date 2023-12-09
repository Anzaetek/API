import asyncio
from dataclasses_serialization.serializer_base.serializer import Serializer
import websockets
import requests
import json
from MarkowitzSerde import *
from TargetSerde import *
from SacadosQuadratiqueSerde import *

def pquery(uri: str, m: MarkowitzProblem, onCompletion: Callable[[MarkowitzSolution],None]) -> None:
    qs = serializeMarkowitzProblemQuery(m)
    query = {
        "user": m.info.user,
        "token": m.info.token,
        "query": qs,
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeMarkowitzSolutionResponse(json.dumps(rv))
    print("result=", r)
    onCompletion(r)

def pqueryAny(uri: str, q:Dict[str, Any], n:str, onCompletion: Callable[[Dict[str,Any]],None]) -> None:
    qs = '{ "__class__":\"' + n + '\", "query":' + json.dumps(q)  + '}'
    query = {
        "user": q["info"]["user"],
        "token": q["info"]["token"],
        "query": qs,
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    onCompletion(rv)

def pquerySolverProblem(uri: str, m: SolverProblem, onCompletion: Callable[[SolverSolution],None]) -> None:
    qs = serializeSolverProblemQuery(m)
    query = {
        "user": m.Info.user,
        "token": m.Info.token,
        "query": qs,
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeSolverSolutionResponse(json.dumps(rv))
    v = r.Results['p']
    for k in m.Description.Interpretation:
        r.Results[k] = m.Description.Interpretation[k](v)    
    print("result=", r)    
    onCompletion(r) 

def pqueryExtraQUBO(uri: str, m: ExtractQUBO, onCompletion: Callable[[QUBOSolution],None]) -> None:
    qs = serializeExtractQUBOQuery(m)
    query = {
        "user": m.Info.user,
        "token": m.Info.token,
        "query": qs,
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeQUBOSolutionResponse(json.dumps(rv))   
    print("result=", r)    
    onCompletion(r)     

def pqueryQUBOSolverProblem(uri: str, q: QUBOSolverProblem, onCompletion: Callable[[QUBOSolverSolution],None]) -> None:
    qs = serializeQUBOSolverProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeQUBOSolverSolutionResponse(json.dumps(rv))
    print("result=")
    onCompletion(r)

def pqueryQRNGProblem(uri: str, q: QRNGProblem, onCompletion: Callable[[QRNGSolution],None]) -> None:
    qs = serializeQRNGProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeQRNGSolutionResponse(json.dumps(rv))
    print("result=")
    onCompletion(r)    

def pquerySibeliusProblem(uri: str, q: SibeliusProblem, onCompletion: Callable[[SibeliusSolution],None]) -> None:
    qs = serializeSibeliusProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeSibeliusSolutionResponse(json.dumps(rv))
    print("result=",r)
    onCompletion(r)  

def pqueryMLTrainingProblem(uri: str, q: MLTrainingProblem, onCompletion: Callable[[MLTrainingSolution],None]) -> None:
    qs = serializeMLTrainingProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeMLTrainingSolutionResponse(json.dumps(rv))
    print("result=",r)
    onCompletion(r)  
 
def pqueryMLInferenceProblem(uri: str, q: MLInferenceProblem, onCompletion: Callable[[MLInferenceSolution],None]) -> None:
    qs = serializeMLInferenceProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeMLInferenceSolutionResponse(json.dumps(rv))
    print("result=",r)
    onCompletion(r)  

def pquerySacadosQuadratiqueProblem(uri: str, q: SacadosQuadratique, onCompletion: Callable[[SacadosQuadratiqueResult],None]) -> None:
    qs = serializeSacadosQuadratiqueProblemQuery(q)
    query = {
        "user": q.Info.user,
        "token": q.Info.token,
        "query": qs,        
    }
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    r = deserializeSacadosQuadratiqueResponse(json.dumps(rv))
    print("result=",r)
    onCompletion(r)  

if __name__ == '__main__':
    print("testing")
    config_m01_ut = {
        "user": "echo1",
        "token": "e06da647bfdf8107bb049cd5578d179aeeff2eac10a8f08700af6ea3ae2f4dea2b929e0f8403922b759f5544ffb19d2cb59ddca7448fa26c3405dba31841c962"
    }

    config_m01: Dict[str, Any] = {
        "configSelect": "gekkoConfig"
    }

    query = MarkowitzProblem(Markowitz(np.array([[1.0,0.2,0.1],[0.2,1.0,0.3],[0.1,0.3,1.0]], dtype=float), 
                            np.array([0.05,0.05,0.05], dtype=float)), config_m01, UserTokenSerde(config_m01_ut["user"], config_m01_ut["token"]))
    url = "http://localhost:5000/execute"
    pquery(url, query, lambda x: print(x))