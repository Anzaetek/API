from LaplaceAPIClient import *
import os

config_solver01_2000_13 = {
    "backend": "QUBOSimulatorBackend",
    "nshots": 2000,      
}

config_solver01_fujitsuda_13 = {
    "backend": "FujitsuDASimulatorBackend",
    "nshots": 1,
    "number_iterations": 1000,   #  = 1000,               # total number of itrations per run
    "number_runs": 16,           #  = 16,                  # number of stochastically independant runs
    "temperature_start": 5000,   # = 5000,               # start temperature for annealing as float value
    "temperature_end": 10,       # = 10,                 # end temperature for annealing as float value 
    "temperature_mode": 0,      # = 0,                         # 0: reduce temperature by factor (1-temperature_decay) every temperature_interval steps
                                                      # 1: reduce temperature by factor (1-temperature_decay*temperature) every temperature_interval steps
                                                      # 2: reduce temperature by factor (1-temperature_decay*temperature^2) every temperature_interval steps
    "temperature_decay": 0.0095, # = 0.0095,             # see temperature_mode 0
    "temperature_interval": 1,   # = 1,                  # see temperature_mode 0
    "offset_increase_rate": 5000.0, # = 5000.0,             # increase of dynamic offset when no bit selected, set to 0.0 to switch off dynamic offset
    #"graphics": True,               # = True                # create data for graphics output 
    "rescale": 100.0
}

config_solver01_VQE_13 = {
    "backend": "VQESimulatorBackend",
    "ninit": 1,
    "nshots": 5,     
}

user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

qubo13q = QUBO(np.array([
    [0.0, -1.0,  4.0],
    [-1.0, 5.0, -9.0],
    [4.0, -9.0, -5.0]
]))

qubo13 = QUBOSolverProblem(qubo13q, config_solver01_2000_13, UserTokenSerde(user=user1, token=token1)) # type: ignore

def queryDone13(res: QUBOSolverSolution) -> None:
    print(res)
    if not "bestBinaryVector" in res.Results:
        raise Exception('failure')
    if not len(res.Results["bestBinaryVector"]) == 3:
        raise Exception('failure')
    if not abs(res.Results["bestBinaryVector"][0] - 0.0) < 1e-12:
        raise Exception('failure')
    if not abs(res.Results["bestBinaryVector"][1] - 1.0) < 1e-12:
        raise Exception('failure')
    if not abs(res.Results["bestBinaryVector"][2] - 1.0) < 1e-12:
        raise Exception('failure')

pqueryQUBOSolverProblem("https://api2.anzaetek.com:443/execute", qubo13, queryDone13)

print("vqe")
qubo13_vqe = QUBOSolverProblem(qubo13q, config_solver01_VQE_13, UserTokenSerde(user=user1, token=token1)) # type: ignore
pqueryQUBOSolverProblem("https://api2.anzaetek.com:443/execute", qubo13_vqe, queryDone13)
print("vqe done")

print("fujitsu")

from sys import platform
fda=os.getenv("FORCE_FUJITSU")
print("fda", fda)
if platform == "linux" or platform == "linux2" or fda == "TRUE":
    qubo13_fujitsu = QUBOSolverProblem(qubo13q, config_solver01_fujitsuda_13, UserTokenSerde(user=user1, token=token1)) # type: ignore
    pqueryQUBOSolverProblem("https://api2.anzaetek.com:443/execute", qubo13_fujitsu, queryDone13)
else:
    print("skip: not linux/amd64 platform")

print("fujitsu done")

