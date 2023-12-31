from LaplaceAPIClient import *
import os

from sys import platform
if platform == "linux" or platform == "linux2":
    print("ok")
else:
    print("ok?") # exit(0)     

path = "./simplifiedJob10_cmd.json"
txt = ""
with open(path, "r") as file:
    txt = file.read()

user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

qsP = SibeliusProblem({}, UserTokenSerde(user=user1, token=token1), txt) # type: ignore

def queryDone16(res: SibeliusSolution) -> None:
    print(res) 
    print(res.Results.keys())
    print(json.loads(res.Results["analytics"])["values"][0][0]) # type: ignore
    ref = 0.99886490187506194
    if abs(json.loads(res.Results["analytics"])["values"][0][0] - ref) < 1e-3: #type: ignore
        print("ok")
    else:
        raise Exception('failure')

pquerySibeliusProblem("https://api2.anzaetek.com:443/execute", qsP, queryDone16)
