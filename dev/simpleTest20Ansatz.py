from LaplaceAPIClient import *
import os

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

ref_matrix_20 = [
      [
        -69.0,
        20.0,
        30.0,
        30.0,
        20.0,
        20.0,
        20.0,
        60.0,
        60.0,
        50.0
      ],
      [
        20.0,
        -30.0,
        10.0,
        30.0,
        10.0,
        30.0,
        20.0,
        20.0,
        20.0,
        20.0
      ],
      [
        30.0,
        10.0,
        -29.0,
        20.0,
        0.0,
        10.0,
        10.0,
        20.0,
        30.0,
        20.0
      ],
      [
        30.0,
        30.0,
        20.0,
        -36.0,
        10.0,
        30.0,
        20.0,
        30.0,
        30.0,
        30.0
      ],
      [
        20.0,
        10.0,
        0.0,
        10.0,
        -24.0,
        10.0,
        10.0,
        20.0,
        10.0,
        20.0
      ],
      [
        20.0,
        30.0,
        10.0,
        30.0,
        10.0,
        -21.0,
        20.0,
        20.0,
        20.0,
        20.0
      ],
      [
        20.0,
        20.0,
        10.0,
        20.0,
        10.0,
        20.0,
        -26.0,
        20.0,
        20.0,
        20.0
      ],
      [
        60.0,
        20.0,
        20.0,
        30.0,
        20.0,
        20.0,
        20.0,
        -51.0,
        50.0,
        40.0
      ],
      [
        60.0,
        20.0,
        30.0,
        30.0,
        10.0,
        20.0,
        20.0,
        50.0,
        -60.0,
        50.0
      ],
      [
        50.0,
        20.0,
        20.0,
        30.0,
        20.0,
        20.0,
        20.0,
        40.0,
        50.0,
        -59.0
      ]
    ]

tag1f = 'qubo-f0/VQE01-ann-' + str(len(ref_matrix_20)) +'-p-c-tw'
tag2f = 'qubo-f0/VQE01-xgboost-' + str(len(ref_matrix_20)) + '-p-c-tw'    

def queryDone20_2(res: QUBOSolverSolution) -> None:
    print("qubo result", res)
    if not "bestBinaryVector" in res.Results:
        raise Exception('failure')
    if not len(res.Results["bestBinaryVector"]) == 10:
        raise Exception('failure')
    # result is trivial in this particular case!
    if not abs(res.Results["bestBinaryVector"][0] - 1.0) < 1e-12:
        raise Exception('failure')
    if not abs(res.Results["bestBinaryVector"][1] - 0.0) < 1e-12:
        raise Exception('failure')
    if not abs(res.Results["bestBinaryVector"][2] - 0.0) < 1e-12:
        raise Exception('failure')

def queryDone20(res: MLInferenceSolution) -> None:
    print(res)
    print(res.Labels)
    print(res.Labels[0])
    ansatz = 'twolocal'
    # choose Ansazt
    # of course, other ansatz are available in reality... did you subscribe to our services?
    if cast(float, res.Labels[0]) > 0.5:
        ansatz = 'twolocal'
    else:
        ansatz = 'alternating_ry_rz'
    print('ansatz is', ansatz)
    config_20 = {
      "backend": "VQESimulatorBackend",
      "ninit": 5,
      "nshots": 5, 
      "ansatz": ansatz           
    }
    print("sending QUBO")
    q20_2 = QUBOSolverProblem(QUBO(np.array(ref_matrix_20, dtype=np.float64)), config_20, UserTokenSerde(user1, token1)) # type: ignore
    pqueryQUBOSolverProblem("http://localhost:5000/execute", q20_2, queryDone20_2)

    if False:
      config_solver01_fujitsuda_20 = {
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
      q20_3 = QUBOSolverProblem(QUBO(np.array(ref_matrix_20, dtype=np.float64)), config_solver01_fujitsuda_20, UserTokenSerde(user1, token1)) # type: ignore
      pqueryQUBOSolverProblem("http://localhost:5000/execute", q20_3, queryDone20_2)

print(tag1f)
print(tag2f)

config : dict = {}
q20 = MLInferenceProblem(config, UserTokenSerde(user1, token1), tag1f, [np.array(ref_matrix_20).flatten().tolist()]) # type: ignore
pqueryMLInferenceProblem("http://localhost:5000/execute", q20, queryDone20)
