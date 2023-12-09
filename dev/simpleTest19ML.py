from LaplaceAPIClient import *
import os

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
import random
import math

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

# Generate some train & test data, using sklearn here but no obligation really
st = random.getstate()
random.seed(42)
w = 3.14*20
features = [
    (math.sin(x*w) + random.uniform(-0.05, 0.05),
    math.cos(x*w) + random.uniform(-0.01, 0.03))
    for x in [
        k * 0.001
        for k in range(1000)
    ]
]
labels = [1 if x+y + random.uniform(-0.01, 0.01) >= 0.7 else 0 for (x,y) in features]
random.setstate(st)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# running remote inference
config = {
    "n_estimators":50, 
    "learning_rate":0.2, 
    "random_state":42,
    "early_stopping_rounds":10, 
    "eval_metric":"error",
    "model_type":"onnx/xgboost"
}

q19 = MLTrainingProblem(config, UserTokenSerde(user1, token1), "TestOnly#TestML19", # type: ignore
                        np.array(X_train).tolist(), np.array(y_train).tolist(),
                        np.array(X_test).tolist(), np.array(y_test).tolist())

def queryDone19_2(res: MLInferenceSolution) -> None:
    print(res)
    accuracy4 = accuracy_score(y_test, res.Labels)
    print("Accuracy:", accuracy4)
    if accuracy4 < 0.98:
        raise Exception("failed")
    print("ok!!")

def queryDone19(res: MLTrainingSolution) -> None:
    print(res)
    print(res.Results["report"]["accuracy"]) # type: ignore
    if res.Results["report"]["accuracy"] < 0.98: # type: ignore
        raise Exception("failed")
    q19_2 = MLInferenceProblem(config, UserTokenSerde(user1, token1), "TestOnly#TestML19", np.array(X_test).tolist()) # type: ignore
    pqueryMLInferenceProblem("http://localhost:5000/execute", q19_2, queryDone19_2)

pqueryMLTrainingProblem("http://localhost:5000/execute", q19, queryDone19)