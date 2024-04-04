# GET THE CONFIG
import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

import pandas as pd
import numpy as np

training_set = pd.read_csv("training_set.csv")
print(training_set)
testing_set = pd.read_csv("testing_set.csv")
print(testing_set)

xfeatures = [np.fromstring(x[1:-1], sep=' ', dtype=float).tolist() for x in training_set['X'].to_list()]
print(repr(xfeatures[0:2]))
xlabels = training_set['y'].to_list()
print(repr(xlabels[0:10]))

tfeatures = [np.fromstring(x[1:-1], sep=' ', dtype=float).tolist() for x in testing_set['X'].to_list()]
print(repr(tfeatures[0:2]))
tlabels = testing_set['y'].to_list()
print(repr(tlabels[0:10]))

tag = "TestOnly#API_QML_01"
config = {
            'num_classes': 2,
            'n_qubits': 6,
            'max_depth': 4,
            'pqc_sample_num': 2024,
            'model_type': 'QRF'
    }

import requests
import json

url = "http://localhost:5000/execute"

def query_ml01_train(config, tag, xfeatures, xlabels, tfeatures, tlabels):
    train_q = { "__class__":"MLTrainingProblem", 
                "query":{
                    "Config":config,
                    "Info":{"user":user1,"token":token1},"Tag":tag,
                    "Features":xfeatures,"Labels":xlabels,
                    "TestFeatures":tfeatures,"TestLabels":tlabels}}

    train_query = {'user': user1, 'token': token1, 'query': json.dumps(train_q)}

    post_response = requests.post(url = url, json=train_query)
    rv = post_response.json()
    #print(rv)
    return rv['Results']['report']

status = query_ml01_train(config, tag, xfeatures, xlabels, tfeatures, tlabels)
print(status)

tag = "TestOnly#TestML19"
ifeatures = tfeatures

import requests
import json

url = "https://api2.anzaetek.com:443/execute"

def query_ml01_infer(tag, ifeatures):
    infer_q = { "__class__":"MLInferenceProblem", 
            "query": {
                "Config": {},
                "Info":{"user":user1,"token":token1},
                "Tag": tag,
                "Features":ifeatures
                }
            }
    infer_query = {'user': user1, 'token': token1, 
                'query': json.dumps(infer_q) }
    post_response = requests.post(url = url, json=infer_query)
    rv = post_response.json()
    #print(rv)
    return rv['Labels']

ir = query_ml01_infer(tag, ifeatures)
print(ir)