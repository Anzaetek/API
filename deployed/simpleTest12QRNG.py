from LaplaceAPIClient import *
import os

user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")
qrngP = QRNGProblem({}, UserTokenSerde(user=user1, token=token1)) # type: ignore

def queryDone12(x: QRNGSolution) -> None:
    try:
        print(x)
        print(len(x.Results["random"])) # type: ignore
        if len(x.Results["random"]) < 65536: # type: ignore
            raise Exception('failure')
    except:
        pass

pqueryQRNGProblem("https://api2.anzaetek.com:443/execute", qrngP, queryDone12)
