from LaplaceAPIClient import *
import os

# Get configuration
user1=os.getenv("QUETZALCOATL_USER1")
token1=os.getenv("QUETZALCOATL_TOKEN1")

q00 = {
    "use_covar": [[0.12055772584937176, 0.0434040736259131, 0.03657016444844578], 
                                [0.0434040736259131, 0.13147949152864283, 0.03381911680330686], 
                                [0.03657016444844578, 0.03381911680330686, 0.10987923580316178]],
    "from_date_yyyy_m_d": "2022-1-1",
    "to_date_yyyy_m_d": "2023-1-1",
    "ticker_list": [
        #"ABBV",
        #"C",
        "ADBE",
        "EQIX",
        "EXPE"
    ],
    "constraint_weight": 50
}

url = "https://api2.anzaetek.com:443/execute"

def onResult25(rv1:Any) -> None:
    print(rv1)
    print(json.dumps(rv1))
    assert("allocation" in rv1)
    assert("perm" in rv1)
    assert("used_covar" in rv1)
    err1 = np.sum(np.array(rv1["allocation"]) - np.array( [0.3886161009578426, 0.27833423034567584, 0.3330496686964816]))
    print(err1)
    err2 = np.sum(np.array(rv1["perm"]) - np.array( [3,1,2]))
    print(err2)
    err3 = np.sum(np.array(rv1["used_covar"]) 
                    - np.array([[0.12055772584937176, 0.0434040736259131, 0.03657016444844578], 
                                [0.0434040736259131, 0.13147949152864283, 0.03381911680330686], 
                                [0.03657016444844578, 0.03381911680330686, 0.10987923580316178]]))
    print(err3)
    assert(err1 < 1e-12)
    assert(err2 < 1e-12)
    assert(err3 < 1e-12)

pqueryQHRP(url, UserTokenSerde(user1, token1), # type: ignore
           QHRPProblem(q00["use_covar"], # type: ignore
                       q00["from_date_yyyy_m_d"], # type: ignore
                       q00["to_date_yyyy_m_d"], # type: ignore
                       q00["ticker_list"], # type: ignore
                       q00["constraint_weight"]), onResult25) # type: ignore
