import requests
import time
import numpy as np
import sys
import utilsg

BASE_URL = "https://qubo.belgrade.maxeler.com"

import utilsg
API_USER = utilsg.getenvcached("API_USER") 
API_PASSWORD = utilsg.getenvcached("API_PASSWORD")
# how often to query for job status updates - 5 seconds
JOB_STATUS_QUERY_INTERVAL = 5

# Function to submit a job
def submit_job(
    assets, budget, risk_aversion, h0, Lh, Uh, Tmin, Tmax, psi, zeta, use_milp=False):
    url = f"{BASE_URL}/api/v1/portfolio_optimization/submit_job"

    print(url)
    assets = assets.tolist() if isinstance(assets, np.ndarray) else assets
    Lh = Lh.tolist() if isinstance(Lh, np.ndarray) else Lh
    Uh = Uh.tolist() if isinstance(Uh, np.ndarray) else Uh
    data = {
        "assets": assets,                # list of asset labels
        "budget": budget,                # the total budged of the portfolio: stock weigths x price list
        "risk_aversion": risk_aversion,  # = lambda in Eq (1)
        "h0": h0,      # initial weigths in the portfolio
        "Lh": Lh,      # measured in the number of stocks, Eq (4)
        "Uh": Uh,      # measured in the number of stocks, Eq (4)
        "Tmin": Tmin,  # measured in the number of stocks, Eq(6)
        "Tmax": Tmax,  # measured in the number of stocks, Eq(6)
        "psi": psi,    # measured in price of the changed stocks, Eq (7a)
        "zeta": zeta,  # measured in price of the changed stocks, Eq (7b)
        "use_milp": use_milp, # experimental input: set to false to solve PO woth MILP, or False to use QUBO
    }
    response = requests.post(url, json=data, auth=(API_USER, API_PASSWORD))
    # print(f"Response status code: {response.status_code}")
    # print(f"Response text: {response.text}")
    if response.status_code == 201:
        return response.json()["job_id"]
    else:
        print("Failed to submit job")
        print(response.json())
        return None


# Function to query job status
def query_job_status(job_id):
    url = f"{BASE_URL}/api/v1/job_status/{job_id}"
    response = requests.get(url, auth=(API_USER, API_PASSWORD))
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to query job status")
        print(response.json())
        return None

# Function to display the result
def print_out_result(result, initial_weights):
    print("{:^8} | {:^15} | {:^15} | {:^15}".format(
        "Asset", "Num of Stocks", "Stock Price", "Initial num of stocks"))
    print("-" * 62)

    total_price = 0
    for asset, data in result.items():
        num_stocks, stock_price = data.values()
        initial_stocks          = initial_weights.get( asset, 0 )
        print("{:^8} | {:^15} | {:^15.3f} | {:^15} ".format(
            asset, num_stocks, stock_price, initial_stocks))

        total_price = total_price + num_stocks*stock_price

    print("Total price of the assets: ", total_price)


def main():

    # Job parameters
    assets25 = [
        "AAPL",
        "MSFT",
        "AMZN",
        "NVDA",
        "GOOGL",
        "TSLA",
        "GOOG",
        "BRK-B",
        "META",
        "UNH",
        "XOM",
        "LLY",
        "JPM",
        "JNJ",
        "V",
        "PG",
        "MA",
        "AVGO",
        "HD",
        "CVX",
        "MRK",
        "ABBV",
        "COST",
        "PEP",
        "ADBE",
    ]

    # initial weights
    weights_dict = {
        "AAPL": 27, "MSFT": 0, "AMZN": 0, "NVDA": 140, "GOOGL": 0,
        "TSLA": 0, "GOOG": 0, "BRK-B": 361, "META": 0, "UNH": 0,
        "XOM": 0, "LLY": 16, "JPM": 0, "JNJ": 0, "V": 19,
        "PG": 0, "MA": 0, "AVGO": 0, "HD": 0, "CVX": 0,
        "MRK": 41, "ABBV": 235, "COST": 159, "PEP": 30, "ADBE": 0
    }

    assets = assets25

    weights_list = [weights_dict[asset] for asset in assets]



    # mathematical model behind portfolio optimization is described in https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1823627&download=yes
    budget = 504055
    risk_aversion = 0.9 				# = lambda in Eq (1)

    h0 = weights_list					# initial weigths in the portfolio

    Lh = 0 						# measured in the number of stocks, Eq (4)
    Uh = 400 * np.ones((len(assets),), dtype=np.int64) 	# measured in the number of stocks, Eq (4)
    Tmin = 2 		# measured in the number of stocks, Eq(6)
    Tmax = 6		# measured in the number of stocks, Eq(6)
    psi = 5000 		# measured in price of the changed stocks, Eq (7a)
    zeta = 13328 	# measured in price of the changed stocks, Eq (7b)

    # Submit the job
    job_id = submit_job(
        assets,
        budget,
        risk_aversion,
        h0,
        Lh,
        Uh,
        Tmin,
        Tmax,
        psi,
        zeta
    )
    if not job_id:
        return

    print("Job submitted successfully. Job ID:", job_id)
    # Query job status every 5 seconds until it's completed
    while True:
        status = query_job_status(job_id)
        if not status:
            break
        sys.stdout.write(f"\rJob Status: {status['status']}")
        if status["status"] in ["SUCCESS", "FAILURE"]:
            print("\nResult:")
            result = status["result_list"]
            print_out_result(result, weights_dict)
            break
        time.sleep(JOB_STATUS_QUERY_INTERVAL)


if __name__ == "__main__":
    main()
