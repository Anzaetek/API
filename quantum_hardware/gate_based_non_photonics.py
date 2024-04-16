# This example shows the execution of the same quantum program with a variety of backends 

import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

import requests
import json

url = "https://api2.anzaetek.com:443/execute"

def query22(executor, nqubits, config, nshots, circuit):
    q = {"__class__": "Assembly", 
        "nqubits": nqubits, 
        "executor": executor, 
        "config": config, 
        "circuit": circuit, 
        "nshots": nshots, 
        "user": user1, 
        "token": token1}
    query = {
        'user': user1, 
        'token': token1, 
        'query': json.dumps(q)}

    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    return json.loads(rv)

circuit = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[8];
creg c[8];
rx(4.291410390018364) q[0];
ry(4.291410390018364) q[0];
rz(4.291410390018364) q[0];
rx(4.75305282790762) q[1];
ry(4.75305282790762) q[1];
rz(4.75305282790762) q[1];
rx(5.017046899019829) q[2];
ry(5.017046899019829) q[2];
rz(5.017046899019829) q[2];
rx(5.586875682213167) q[3];
ry(5.586875682213167) q[3];
rz(5.586875682213167) q[3];
rx(5.370948646748333) q[4];
ry(5.370948646748333) q[4];
rz(5.370948646748333) q[4];
rx(4.383400696634489) q[5];
ry(4.383400696634489) q[5];
rz(4.383400696634489) q[5];
rx(1.0040798048277215) q[6];
ry(1.0040798048277215) q[6];
rz(1.0040798048277215) q[6];
rx(4.816347882071221) q[7];
ry(4.816347882071221) q[7];
rz(4.816347882071221) q[7];
cz q[0],q[1];
cz q[1],q[2];
cz q[2],q[3];
cz q[3],q[4];
cz q[4],q[5];
cz q[5],q[6];
cz q[6],q[7];
rx(0.6767931740293136) q[0];
ry(0.6767931740293136) q[0];
rz(0.6767931740293136) q[0];
rx(6.245448590863338) q[1];
ry(6.245448590863338) q[1];
rz(6.245448590863338) q[1];
rx(2.1306355034269515) q[2];
ry(2.1306355034269515) q[2];
rz(2.1306355034269515) q[2];
rx(2.7255783980590667) q[3];
ry(2.7255783980590667) q[3];
rz(2.7255783980590667) q[3];
rx(1.750832501632983) q[4];
ry(1.750832501632983) q[4];
rz(1.750832501632983) q[4];
rx(0.1346639658807586) q[5];
ry(0.1346639658807586) q[5];
rz(0.1346639658807586) q[5];
rx(3.978473802232576) q[6];
ry(3.978473802232576) q[6];
rz(3.978473802232576) q[6];
rx(4.664170750737341) q[7];
ry(4.664170750737341) q[7];
rz(4.664170750737341) q[7];
cz q[0],q[1];
cz q[1],q[2];
cz q[2],q[3];
cz q[3],q[4];
cz q[4],q[5];
cz q[5],q[6];
cz q[6],q[7];
rx(3.4968206361109244) q[0];
ry(3.4968206361109244) q[0];
rz(3.4968206361109244) q[0];
rx(0.3982901374070522) q[1];
ry(0.3982901374070522) q[1];
rz(0.3982901374070522) q[1];
rx(5.801403824910094) q[2];
ry(5.801403824910094) q[2];
rz(5.801403824910094) q[2];
rx(1.966614047420217) q[3];
ry(1.966614047420217) q[3];
rz(1.966614047420217) q[3];
rx(2.542011335754404) q[4];
ry(2.542011335754404) q[4];
rz(2.542011335754404) q[4];
rx(5.627844325594348) q[5];
ry(5.627844325594348) q[5];
rz(5.627844325594348) q[5];
rx(4.434611341550521) q[6];
ry(4.434611341550521) q[6];
rz(4.434611341550521) q[6];
rx(1.506855057004407) q[7];
ry(1.506855057004407) q[7];
rz(1.506855057004407) q[7];
cz q[0],q[1];
cz q[1],q[2];
cz q[2],q[3];
cz q[3],q[4];
cz q[4],q[5];
cz q[5],q[6];
cz q[6],q[7];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
measure q[6] -> c[6];
measure q[7] -> c[7];
"""

executor = "qiskit"
nqubits = 8
config = {}
nshots = 1024

res = query22(executor, nqubits, config, nshots, circuit)
print(repr(res))

executor = "circ"
res = query22(executor, nqubits, config, nshots, circuit)
print(repr(res))

executor = "qadence"
res = query22(executor, nqubits, config, nshots, circuit)
print(repr(res))

executor = "spinqit"
res = query22(executor, nqubits, config, nshots, circuit)
print(repr(res))

executor = "qpanda2"
res = query22(executor, nqubits, config, nshots, circuit)
print(repr(res))
