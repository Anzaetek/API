# This example shows how to use our DSL for building specific programs

import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

code = """
let qubomatrix = [
      [
        -10.992680373440555,
        3.1207718881750637,
        1.5603859440875318,
        1.5603831773087988,
        3.1207663546175977,
        1.5603831773087988
      ],
      [
        3.1207718881750637,
        -18.864588858706046,
        3.1207718881750637,
        3.1207663546175977,
        6.241532709235195,
        3.1207663546175977
      ],
      [
        1.5603859440875318,
        3.1207718881750637,
        -10.992680373440555,
        1.5603831773087988,
        3.1207663546175977,
        1.5603831773087988
      ],
      [
        1.5603831773087988,
        3.1207663546175977,
        1.5603831773087988,
        -10.992686168287307,
        3.1207912043308967,
        1.5603956021654484
      ],
      [
        3.1207663546175977,
        6.241532709235195,
        3.1207663546175977,
        3.1207912043308967,
        -18.864581132243714,
        3.1207912043308967
      ],
      [
        1.5603831773087988,
        3.1207663546175977,
        1.5603831773087988,
        1.5603956021654484,
        3.1207912043308967,
        -10.992686168287307
      ]
    ] in 
let num_qubits = 6 in 
let samples = 400 in 
let x0 = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5] in
vqeQUBO(x0,qubomatrix,num_qubits,samples)
"""

context = {}

import requests
import json

url = "https://api2.anzaetek.com:443/execute"

def query24A(code, context):
    q = {"__class__": "Axolotl", 
        "query": {"operation": "execute", 
                "program": code,
                "context": context}, 
        "user": user1, "token": token1 }
    query = {'user': user1, 
            'token': token1, 
            'query': json.dumps(q) }
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    x = json.loads(rv)
    return x

res = query24A(code, context)
print(repr(res))
