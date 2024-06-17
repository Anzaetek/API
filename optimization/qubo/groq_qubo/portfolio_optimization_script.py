import requests
import time
import numpy as np
import sys

BASE_URL = "https://qubo.belgrade.maxeler.com"

import utilsg
API_USER = utilsg.getenvcached("API_USER")
API_PASSWORD = utilsg.getenvcached("API_PASSWORD")
JOB_STATUS_QUERY_INTERVAL = 5  # how often to query for job status updates - 5 seconds

# Function to submit a job
def submit_job(
    assets, budget, risk_aversion, Lh, Uh, Kmin, Kmax, psi, zeta, use_milp=False):
    url = f"{BASE_URL}/api/v1/portfolio_optimization/submit_job"


    h0 = [0] * len(assets)

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
        "Kmin": Kmin,  # measured in the number of stocks, Eq(5)
        "Kmax": Kmax,  # measured in the number of stocks, Eq(5)
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


def print_out_result(result):
    print("{:^8} | {:^15} | {:^15}".format("Asset", "Num Stocks", "Stock Price"))
    print("-" * 42)

    total_price = 0
    for asset, data in result.items():
        num_stocks, stock_price = data.values()
        print("{:^8} | {:^15} | {:^15.3f}".format(asset, num_stocks, stock_price))

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

    assets = assets25

    budget = 504055
    risk_aversion = 0.9                              # = lambda in Eq (1)

    Lh = 0 						# measured in the number of stocks, Eq (4)
    Uh = 400 * np.ones((len(assets),), dtype=np.int64) 	# measured in the number of stocks, Eq (4)

    Kmin = 5           # measured in the number of stocks, Eq5)
    Kmax = 10          # measured in the number of stocks, Eq5)
    psi = 5000         # measured in price of the changed stocks, Eq (7a)
    zeta = 0           # measured in price of the changed stocks, Eq (7b)


    # Submit the job
    job_id = submit_job(
        assets,
        budget,
        risk_aversion,
        Lh,
        Uh,
        Kmin,
        Kmax,
        psi,
        zeta,
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
        if status["status"] == "SUCCESS":
            print("\nResult:")
            result = status["result_list"]
            print_out_result(result)
            break
        elif status["status"] == "FAILURE":
            print(f"\n{status['result_list']}")
            break
        time.sleep(JOB_STATUS_QUERY_INTERVAL)


if __name__ == "__main__":
    main()
