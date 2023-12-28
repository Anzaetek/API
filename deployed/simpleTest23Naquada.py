from LaplaceAPIClient import *
import os

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

code = """
section .config
photon-number: 6
shots: 1000
max-shots: 10000

section .driver
qubo [[-10.992680373440555, 3.1207718881750637, 1.5603859440875318, 1.5603831773087988, 3.1207663546175977, 1.5603831773087988], \
      [ 3.1207718881750637, -18.864588858706046, 3.1207718881750637, 3.1207663546175977, 6.241532709235195, 3.1207663546175977], \
      [ 1.5603859440875318, 3.1207718881750637, -10.992680373440555, 1.5603831773087988, 3.1207663546175977, 1.5603831773087988], \
      [ 1.5603831773087988, 3.1207663546175977, 1.5603831773087988, -10.992686168287307, 3.1207912043308967, 1.5603956021654484], \
      [ 3.1207663546175977, 6.241532709235195, 3.1207663546175977, 3.1207912043308967, -18.864581132243714, 3.1207912043308967], \
      [ 1.5603831773087988, 3.1207663546175977, 1.5603831773087988, 1.5603956021654484, 3.1207912043308967, -10.992686168287307]];
driver "SLOS";
// "qpu:ascella";
filter-heuristic none;
optimize $all;
section .openoqasm
OPTICQASM 1.0;
generic_interferometer ps($phi) bs_rx($theta, $phi_tr) q[0], q[1], q[2], q[3], q[4], q[5];

"""

circuit1 = code 
url = "https://api2.anzaetek.com:443/execute"

def interpret_result(y):
    x = json.loads(y)
    #print(repr(x))
    #print(repr(x["samples"]))
    #print(x["samples"]["naquada"])
    bestX = []
    bestE = 0.0
    for n in x["samples"]["naquada"]:
        #print(repr(n), n[1])
        for k in n[1]:
            #print(k)
            if k[1] < bestE:
                bestE = k[1]
                bestX = k[0]
    print("best: ", bestX, "energy @", bestE)

pqueryAssembly(url, UserTokenSerde(user1, token1), 1, "perceval", {"naquada":1}, circuit1, 1000, interpret_result) # type: ignore
