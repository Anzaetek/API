# This program is a short demo of the usage of the HyperSolver API for Knapsack optimization.
# TODO add bigger examples ~ cf. benchmarks with 'A' + doc: the node version and the Julia version /=

import os
import json
import requests
from typing import cast

HYPERSOLVER_API_URL = 'https://solver.hypersolver.eu:443'
# token = os.getenv("ANZAETEK_HYPERSOLVER_TOKEN")

def solveKnapsack2(ks: dict) -> dict:
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': '_/_',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    url = HYPERSOLVER_API_URL + '/computations/solve'
    payload= json.dumps({ "processingMethodId": "fatal-error", "knapsack": ks})
    r = requests.post(url, data=payload, headers = headers, verify=False)
    data = r.json()
    return cast(dict, data)

knapsack =   {
    "version": "0.1.0",
    "name": "Knapsack 1",
    "itemCount": 25829,
    "capacity": 9964,
    "items": {
      "item-0": {
        "value": 2,
        "weight": 5
      },
      "item-1": {
        "value": 6,
        "weight": 9
      },
      "item-2": {
        "value": 7,
        "weight": 1
      },
      "item-3": {
        "value": 4,
        "weight": 9
      },
      "item-4": {
        "value": 5,
        "weight": 3
      },
      "item-5": {
        "value": 2,
        "weight": 2
      },
      "item-6": {
        "value": 4,
        "weight": 8
      },
      "item-7": {
        "value": 9,
        "weight": 8
      },
      "item-8": {
        "value": 3,
        "weight": 2
      },
      "item-9": {
        "value": 2,
        "weight": 3
      },
      "item-10": {
        "value": 1,
        "weight": 6
      },
      "item-11": {
        "value": 1,
        "weight": 7
      },
      "item-12": {
        "value": 7,
        "weight": 8
      },
      "item-13": {
        "value": 7,
        "weight": 5
      },
      "item-14": {
        "value": 8,
        "weight": 5
      },
      "item-15": {
        "value": 7,
        "weight": 9
      },
      "item-16": {
        "value": 4,
        "weight": 4
      },
      "item-17": {
        "value": 3,
        "weight": 6
      },
      "item-18": {
        "value": 1,
        "weight": 1
      },
      "item-19": {
        "value": 8,
        "weight": 5
      },
      "item-20": {
        "value": 4,
        "weight": 7
      },
      "item-21": {
        "value": 7,
        "weight": 3
      },
      "item-22": {
        "value": 7,
        "weight": 9
      },
      "item-23": {
        "value": 1,
        "weight": 2
      },
      "item-24": {
        "value": 7,
        "weight": 5
      },
      "item-25": {
        "value": 3,
        "weight": 2
      },
      "item-26": {
        "value": 2,
        "weight": 9
      },
      "item-27": {
        "value": 5,
        "weight": 5
      },
      "item-28": {
        "value": 9,
        "weight": 5
      },
      "item-29": {
        "value": 3,
        "weight": 7
      },
      "item-30": {
        "value": 4,
        "weight": 5
      },
      "item-31": {
        "value": 9,
        "weight": 6
      },
      "item-32": {
        "value": 9,
        "weight": 2
      },
      "item-33": {
        "value": 8,
        "weight": 6
      },
      "item-34": {
        "value": 7,
        "weight": 2
      },
      "item-35": {
        "value": 8,
        "weight": 3
      },
      "item-36": {
        "value": 9,
        "weight": 7
      },
      "item-37": {
        "value": 4,
        "weight": 7
      },
      "item-38": {
        "value": 7,
        "weight": 3
      },
      "item-39": {
        "value": 9,
        "weight": 1
      },
      "item-40": {
        "value": 4,
        "weight": 7
      },
      "item-41": {
        "value": 9,
        "weight": 2
      },
      "item-42": {
        "value": 9,
        "weight": 9
      },
      "item-43": {
        "value": 9,
        "weight": 9
      },
      "item-44": {
        "value": 4,
        "weight": 1
      },
      "item-45": {
        "value": 8,
        "weight": 5
      },
      "item-46": {
        "value": 6,
        "weight": 7
      },
      "item-47": {
        "value": 4,
        "weight": 5
      },
      "item-48": {
        "value": 3,
        "weight": 7
      },
      "item-49": {
        "value": 4,
        "weight": 2
      },
      "item-50": {
        "value": 1,
        "weight": 9
      },
      "item-51": {
        "value": 1,
        "weight": 9
      },
      "item-52": {
        "value": 2,
        "weight": 1
      },
      "item-53": {
        "value": 2,
        "weight": 9
      },
      "item-54": {
        "value": 9,
        "weight": 2
      },
      "item-55": {
        "value": 9,
        "weight": 6
      },
      "item-56": {
        "value": 6,
        "weight": 3
      },
      "item-57": {
        "value": 2,
        "weight": 3
      },
      "item-58": {
        "value": 8,
        "weight": 2
      },
      "item-59": {
        "value": 4,
        "weight": 9
      },
      "item-60": {
        "value": 6,
        "weight": 9
      },
      "item-61": {
        "value": 1,
        "weight": 8
      },
      "item-62": {
        "value": 1,
        "weight": 1
      },
      "item-63": {
        "value": 8,
        "weight": 6
      },
      "item-64": {
        "value": 2,
        "weight": 2
      },
      "item-65": {
        "value": 8,
        "weight": 3
      },
      "item-66": {
        "value": 2,
        "weight": 3
      },
      "item-67": {
        "value": 9,
        "weight": 8
      },
      "item-68": {
        "value": 3,
        "weight": 1
      },
      "item-69": {
        "value": 9,
        "weight": 5
      },
      "item-70": {
        "value": 8,
        "weight": 9
      },
      "item-71": {
        "value": 5,
        "weight": 8
      },
      "item-72": {
        "value": 8,
        "weight": 3
      },
      "item-73": {
        "value": 5,
        "weight": 8
      },
      "item-74": {
        "value": 2,
        "weight": 6
      },
      "item-75": {
        "value": 3,
        "weight": 8
      },
      "item-76": {
        "value": 2,
        "weight": 2
      },
      "item-77": {
        "value": 7,
        "weight": 8
      },
      "item-78": {
        "value": 1,
        "weight": 2
      },
      "item-79": {
        "value": 7,
        "weight": 5
      },
      "item-80": {
        "value": 8,
        "weight": 9
      },
      "item-81": {
        "value": 2,
        "weight": 2
      },
      "item-82": {
        "value": 8,
        "weight": 9
      },
      "item-83": {
        "value": 4,
        "weight": 8
      },
      "item-84": {
        "value": 2,
        "weight": 6
      },
      "item-85": {
        "value": 7,
        "weight": 5
      },
      "item-86": {
        "value": 2,
        "weight": 5
      },
      "item-87": {
        "value": 3,
        "weight": 1
      },
      "item-88": {
        "value": 6,
        "weight": 4
      },
      "item-89": {
        "value": 5,
        "weight": 1
      },
      "item-90": {
        "value": 3,
        "weight": 5
      },
      "item-91": {
        "value": 6,
        "weight": 7
      },
      "item-92": {
        "value": 8,
        "weight": 4
      },
      "item-93": {
        "value": 1,
        "weight": 5
      },
      "item-94": {
        "value": 2,
        "weight": 4
      },
      "item-95": {
        "value": 1,
        "weight": 2
      },
      "item-96": {
        "value": 1,
        "weight": 2
      },
      "item-97": {
        "value": 5,
        "weight": 7
      },
      "item-98": {
        "value": 5,
        "weight": 7
      },
      "item-99": {
        "value": 3,
        "weight": 8
      },
      "item-100": {
        "value": 1,
        "weight": 5
      },
      "item-101": {
        "value": 5,
        "weight": 9
      },
      "item-102": {
        "value": 7,
        "weight": 8
      },
      "item-103": {
        "value": 8,
        "weight": 7
      },
      "item-104": {
        "value": 3,
        "weight": 7
      },
      "item-105": {
        "value": 9,
        "weight": 7
      },
      "item-106": {
        "value": 9,
        "weight": 9
      },
      "item-107": {
        "value": 7,
        "weight": 8
      },
      "item-108": {
        "value": 6,
        "weight": 7
      },
      "item-109": {
        "value": 6,
        "weight": 5
      },
      "item-110": {
        "value": 4,
        "weight": 7
      },
      "item-111": {
        "value": 7,
        "weight": 4
      },
      "item-112": {
        "value": 8,
        "weight": 8
      },
      "item-113": {
        "value": 7,
        "weight": 8
      },
      "item-114": {
        "value": 2,
        "weight": 7
      },
      "item-115": {
        "value": 9,
        "weight": 6
      },
      "item-116": {
        "value": 7,
        "weight": 1
      },
      "item-117": {
        "value": 9,
        "weight": 5
      },
      "item-118": {
        "value": 6,
        "weight": 5
      },
      "item-119": {
        "value": 3,
        "weight": 8
      },
      "item-120": {
        "value": 2,
        "weight": 9
      },
      "item-121": {
        "value": 6,
        "weight": 8
      },
      "item-122": {
        "value": 2,
        "weight": 3
      },
      "item-123": {
        "value": 4,
        "weight": 6
      },
      "item-124": {
        "value": 4,
        "weight": 4
      },
      "item-125": {
        "value": 2,
        "weight": 1
      },
      "item-126": {
        "value": 9,
        "weight": 4
      },
      "item-127": {
        "value": 4,
        "weight": 7
      },
      "item-128": {
        "value": 3,
        "weight": 9
      },
      "item-129": {
        "value": 6,
        "weight": 6
      },
      "item-130": {
        "value": 5,
        "weight": 5
      },
      "item-131": {
        "value": 3,
        "weight": 1
      },
      "item-132": {
        "value": 1,
        "weight": 9
      },
      "item-133": {
        "value": 7,
        "weight": 6
      },
      "item-134": {
        "value": 2,
        "weight": 2
      },
      "item-135": {
        "value": 8,
        "weight": 3
      },
      "item-136": {
        "value": 7,
        "weight": 4
      },
      "item-137": {
        "value": 5,
        "weight": 9
      },
      "item-138": {
        "value": 8,
        "weight": 8
      },
      "item-139": {
        "value": 5,
        "weight": 9
      },
      "item-140": {
        "value": 4,
        "weight": 4
      },
      "item-141": {
        "value": 4,
        "weight": 6
      },
      "item-142": {
        "value": 1,
        "weight": 7
      },
      "item-143": {
        "value": 4,
        "weight": 5
      },
      "item-144": {
        "value": 1,
        "weight": 4
      },
      "item-145": {
        "value": 1,
        "weight": 2
      },
      "item-146": {
        "value": 2,
        "weight": 2
      },
      "item-147": {
        "value": 1,
        "weight": 3
      },
      "item-148": {
        "value": 5,
        "weight": 6
      },
      "item-149": {
        "value": 7,
        "weight": 4
      },
      "item-150": {
        "value": 3,
        "weight": 9
      },
      "item-151": {
        "value": 7,
        "weight": 1
      },
      "item-152": {
        "value": 2,
        "weight": 4
      },
      "item-153": {
        "value": 7,
        "weight": 7
      },
      "item-154": {
        "value": 4,
        "weight": 1
      },
      "item-155": {
        "value": 4,
        "weight": 8
      },
      "item-156": {
        "value": 2,
        "weight": 3
      },
      "item-157": {
        "value": 9,
        "weight": 9
      },
      "item-158": {
        "value": 2,
        "weight": 1
      },
      "item-159": {
        "value": 8,
        "weight": 7
      },
      "item-160": {
        "value": 1,
        "weight": 3
      },
      "item-161": {
        "value": 2,
        "weight": 9
      },
      "item-162": {
        "value": 5,
        "weight": 4
      },
      "item-163": {
        "value": 5,
        "weight": 2
      },
      "item-164": {
        "value": 5,
        "weight": 4
      },
      "item-165": {
        "value": 1,
        "weight": 2
      },
      "item-166": {
        "value": 6,
        "weight": 5
      },
      "item-167": {
        "value": 7,
        "weight": 4
      },
      "item-168": {
        "value": 8,
        "weight": 4
      },
      "item-169": {
        "value": 2,
        "weight": 6
      },
      "item-170": {
        "value": 5,
        "weight": 1
      },
      "item-171": {
        "value": 7,
        "weight": 8
      },
      "item-172": {
        "value": 6,
        "weight": 9
      },
      "item-173": {
        "value": 5,
        "weight": 3
      },
      "item-174": {
        "value": 5,
        "weight": 4
      },
      "item-175": {
        "value": 7,
        "weight": 6
      },
      "item-176": {
        "value": 7,
        "weight": 9
      },
      "item-177": {
        "value": 8,
        "weight": 2
      },
      "item-178": {
        "value": 1,
        "weight": 7
      },
      "item-179": {
        "value": 8,
        "weight": 1
      },
      "item-180": {
        "value": 5,
        "weight": 3
      },
      "item-181": {
        "value": 5,
        "weight": 1
      },
      "item-182": {
        "value": 2,
        "weight": 3
      },
      "item-183": {
        "value": 2,
        "weight": 2
      },
      "item-184": {
        "value": 3,
        "weight": 4
      },
      "item-185": {
        "value": 3,
        "weight": 9
      },
      "item-186": {
        "value": 7,
        "weight": 9
      },
      "item-187": {
        "value": 3,
        "weight": 6
      },
      "item-188": {
        "value": 7,
        "weight": 1
      },
      "item-189": {
        "value": 8,
        "weight": 7
      },
      "item-190": {
        "value": 5,
        "weight": 6
      },
      "item-191": {
        "value": 9,
        "weight": 1
      },
      "item-192": {
        "value": 7,
        "weight": 1
      },
      "item-193": {
        "value": 4,
        "weight": 7
      },
      "item-194": {
        "value": 7,
        "weight": 1
      },
      "item-195": {
        "value": 5,
        "weight": 6
      },
      "item-196": {
        "value": 8,
        "weight": 5
      },
      "item-197": {
        "value": 7,
        "weight": 9
      },
      "item-198": {
        "value": 8,
        "weight": 8
      },
      "item-199": {
        "value": 2,
        "weight": 5
      },
      "item-200": {
        "value": 8,
        "weight": 6
      },
      "item-201": {
        "value": 3,
        "weight": 5
      },
      "item-202": {
        "value": 8,
        "weight": 6
      },
      "item-203": {
        "value": 2,
        "weight": 5
      },
      "item-204": {
        "value": 4,
        "weight": 8
      },
      "item-205": {
        "value": 2,
        "weight": 9
      },
      "item-206": {
        "value": 8,
        "weight": 1
      },
      "item-207": {
        "value": 7,
        "weight": 7
      },
      "item-208": {
        "value": 3,
        "weight": 5
      },
      "item-209": {
        "value": 7,
        "weight": 3
      },
      "item-210": {
        "value": 2,
        "weight": 3
      },
      "item-211": {
        "value": 3,
        "weight": 7
      },
      "item-212": {
        "value": 7,
        "weight": 4
      },
      "item-213": {
        "value": 3,
        "weight": 6
      },
      "item-214": {
        "value": 8,
        "weight": 2
      },
      "item-215": {
        "value": 8,
        "weight": 5
      },
      "item-216": {
        "value": 7,
        "weight": 9
      },
      "item-217": {
        "value": 1,
        "weight": 4
      },
      "item-218": {
        "value": 4,
        "weight": 1
      },
      "item-219": {
        "value": 8,
        "weight": 5
      },
      "item-220": {
        "value": 5,
        "weight": 1
      },
      "item-221": {
        "value": 2,
        "weight": 2
      },
      "item-222": {
        "value": 9,
        "weight": 4
      },
      "item-223": {
        "value": 3,
        "weight": 5
      },
      "item-224": {
        "value": 1,
        "weight": 9
      },
      "item-225": {
        "value": 9,
        "weight": 3
      },
      "item-226": {
        "value": 5,
        "weight": 7
      },
      "item-227": {
        "value": 3,
        "weight": 6
      },
      "item-228": {
        "value": 3,
        "weight": 6
      },
      "item-229": {
        "value": 9,
        "weight": 9
      },
      "item-230": {
        "value": 2,
        "weight": 4
      },
      "item-231": {
        "value": 5,
        "weight": 8
      },
      "item-232": {
        "value": 6,
        "weight": 8
      },
      "item-233": {
        "value": 9,
        "weight": 3
      },
      "item-234": {
        "value": 8,
        "weight": 8
      },
      "item-235": {
        "value": 1,
        "weight": 1
      },
      "item-236": {
        "value": 2,
        "weight": 1
      },
      "item-237": {
        "value": 8,
        "weight": 8
      },
      "item-238": {
        "value": 9,
        "weight": 4
      },
      "item-239": {
        "value": 4,
        "weight": 1
      },
      "item-240": {
        "value": 1,
        "weight": 6
      },
      "item-241": {
        "value": 7,
        "weight": 7
      },
      "item-242": {
        "value": 8,
        "weight": 2
      },
      "item-243": {
        "value": 8,
        "weight": 4
      },
      "item-244": {
        "value": 7,
        "weight": 2
      },
      "item-245": {
        "value": 4,
        "weight": 6
      },
      "item-246": {
        "value": 9,
        "weight": 1
      },
      "item-247": {
        "value": 9,
        "weight": 1
      },
      "item-248": {
        "value": 7,
        "weight": 6
      },
      "item-249": {
        "value": 5,
        "weight": 5
      },
      "item-250": {
        "value": 2,
        "weight": 1
      },
      "item-251": {
        "value": 4,
        "weight": 7
      },
      "item-252": {
        "value": 2,
        "weight": 2
      },
      "item-253": {
        "value": 5,
        "weight": 2
      },
      "item-254": {
        "value": 3,
        "weight": 5
      },
      "item-255": {
        "value": 6,
        "weight": 2
      },
      "item-256": {
        "value": 7,
        "weight": 8
      },
      "item-257": {
        "value": 5,
        "weight": 4
      },
      "item-258": {
        "value": 6,
        "weight": 7
      },
      "item-259": {
        "value": 7,
        "weight": 3
      },
      "item-260": {
        "value": 3,
        "weight": 8
      },
      "item-261": {
        "value": 6,
        "weight": 3
      },
      "item-262": {
        "value": 1,
        "weight": 5
      },
      "item-263": {
        "value": 5,
        "weight": 7
      },
      "item-264": {
        "value": 3,
        "weight": 4
      },
      "item-265": {
        "value": 5,
        "weight": 5
      },
      "item-266": {
        "value": 8,
        "weight": 6
      },
      "item-267": {
        "value": 6,
        "weight": 9
      },
      "item-268": {
        "value": 2,
        "weight": 7
      },
      "item-269": {
        "value": 2,
        "weight": 6
      },
      "item-270": {
        "value": 9,
        "weight": 2
      },
      "item-271": {
        "value": 6,
        "weight": 7
      },
      "item-272": {
        "value": 4,
        "weight": 4
      },
      "item-273": {
        "value": 1,
        "weight": 3
      },
      "item-274": {
        "value": 1,
        "weight": 6
      },
      "item-275": {
        "value": 8,
        "weight": 1
      },
      "item-276": {
        "value": 1,
        "weight": 4
      },
      "item-277": {
        "value": 9,
        "weight": 2
      },
      "item-278": {
        "value": 2,
        "weight": 5
      },
      "item-279": {
        "value": 8,
        "weight": 1
      },
      "item-280": {
        "value": 6,
        "weight": 4
      },
      "item-281": {
        "value": 4,
        "weight": 4
      },
      "item-282": {
        "value": 8,
        "weight": 5
      },
      "item-283": {
        "value": 5,
        "weight": 9
      },
      "item-284": {
        "value": 1,
        "weight": 6
      },
      "item-285": {
        "value": 7,
        "weight": 9
      },
      "item-286": {
        "value": 8,
        "weight": 6
      },
      "item-287": {
        "value": 9,
        "weight": 3
      },
      "item-288": {
        "value": 3,
        "weight": 9
      },
      "item-289": {
        "value": 7,
        "weight": 9
      },
      "item-290": {
        "value": 2,
        "weight": 9
      },
      "item-291": {
        "value": 2,
        "weight": 8
      },
      "item-292": {
        "value": 3,
        "weight": 8
      },
      "item-293": {
        "value": 5,
        "weight": 5
      },
      "item-294": {
        "value": 7,
        "weight": 8
      },
      "item-295": {
        "value": 5,
        "weight": 7
      },
      "item-296": {
        "value": 2,
        "weight": 9
      },
      "item-297": {
        "value": 7,
        "weight": 7
      },
      "item-298": {
        "value": 3,
        "weight": 6
      },
      "item-299": {
        "value": 9,
        "weight": 4
      },
      "item-300": {
        "value": 3,
        "weight": 3
      },
      "item-301": {
        "value": 5,
        "weight": 3
      },
      "item-302": {
        "value": 6,
        "weight": 7
      },
      "item-303": {
        "value": 7,
        "weight": 1
      },
      "item-304": {
        "value": 4,
        "weight": 1
      },
      "item-305": {
        "value": 6,
        "weight": 1
      },
      "item-306": {
        "value": 3,
        "weight": 9
      },
      "item-307": {
        "value": 8,
        "weight": 7
      },
      "item-308": {
        "value": 2,
        "weight": 6
      },
      "item-309": {
        "value": 2,
        "weight": 1
      },
      "item-310": {
        "value": 6,
        "weight": 2
      },
      "item-311": {
        "value": 6,
        "weight": 4
      },
      "item-312": {
        "value": 3,
        "weight": 5
      },
      "item-313": {
        "value": 9,
        "weight": 3
      },
      "item-314": {
        "value": 4,
        "weight": 9
      },
      "item-315": {
        "value": 6,
        "weight": 2
      },
      "item-316": {
        "value": 5,
        "weight": 5
      },
      "item-317": {
        "value": 7,
        "weight": 9
      },
      "item-318": {
        "value": 3,
        "weight": 8
      },
      "item-319": {
        "value": 1,
        "weight": 5
      },
      "item-320": {
        "value": 3,
        "weight": 2
      },
      "item-321": {
        "value": 6,
        "weight": 6
      },
      "item-322": {
        "value": 1,
        "weight": 5
      },
      "item-323": {
        "value": 9,
        "weight": 3
      },
      "item-324": {
        "value": 3,
        "weight": 2
      },
      "item-325": {
        "value": 8,
        "weight": 1
      },
      "item-326": {
        "value": 5,
        "weight": 7
      },
      "item-327": {
        "value": 8,
        "weight": 7
      },
      "item-328": {
        "value": 3,
        "weight": 9
      },
      "item-329": {
        "value": 7,
        "weight": 6
      },
      "item-330": {
        "value": 3,
        "weight": 3
      },
      "item-331": {
        "value": 9,
        "weight": 4
      },
      "item-332": {
        "value": 1,
        "weight": 3
      },
      "item-333": {
        "value": 9,
        "weight": 9
      },
      "item-334": {
        "value": 9,
        "weight": 9
      },
      "item-335": {
        "value": 9,
        "weight": 4
      },
      "item-336": {
        "value": 3,
        "weight": 5
      },
      "item-337": {
        "value": 7,
        "weight": 7
      },
      "item-338": {
        "value": 1,
        "weight": 3
      },
      "item-339": {
        "value": 9,
        "weight": 3
      },
      "item-340": {
        "value": 2,
        "weight": 1
      },
      "item-341": {
        "value": 4,
        "weight": 5
      },
      "item-342": {
        "value": 1,
        "weight": 2
      },
      "item-343": {
        "value": 1,
        "weight": 1
      },
      "item-344": {
        "value": 7,
        "weight": 4
      },
      "item-345": {
        "value": 6,
        "weight": 1
      },
      "item-346": {
        "value": 9,
        "weight": 3
      },
      "item-347": {
        "value": 3,
        "weight": 5
      },
      "item-348": {
        "value": 1,
        "weight": 3
      },
      "item-349": {
        "value": 8,
        "weight": 9
      },
      "item-350": {
        "value": 1,
        "weight": 5
      },
      "item-351": {
        "value": 1,
        "weight": 5
      },
      "item-352": {
        "value": 8,
        "weight": 3
      },
      "item-353": {
        "value": 4,
        "weight": 7
      },
      "item-354": {
        "value": 2,
        "weight": 7
      },
      "item-355": {
        "value": 1,
        "weight": 6
      },
      "item-356": {
        "value": 4,
        "weight": 1
      },
      "item-357": {
        "value": 6,
        "weight": 8
      },
      "item-358": {
        "value": 7,
        "weight": 2
      },
      "item-359": {
        "value": 3,
        "weight": 2
      },
      "item-360": {
        "value": 4,
        "weight": 9
      },
      "item-361": {
        "value": 6,
        "weight": 4
      },
      "item-362": {
        "value": 6,
        "weight": 9
      },
      "item-363": {
        "value": 7,
        "weight": 1
      },
      "item-364": {
        "value": 1,
        "weight": 3
      },
      "item-365": {
        "value": 5,
        "weight": 1
      },
      "item-366": {
        "value": 7,
        "weight": 8
      },
      "item-367": {
        "value": 5,
        "weight": 6
      },
      "item-368": {
        "value": 6,
        "weight": 1
      },
      "item-369": {
        "value": 3,
        "weight": 1
      },
      "item-370": {
        "value": 2,
        "weight": 4
      },
      "item-371": {
        "value": 1,
        "weight": 6
      },
      "item-372": {
        "value": 7,
        "weight": 2
      },
      "item-373": {
        "value": 8,
        "weight": 6
      },
      "item-374": {
        "value": 5,
        "weight": 2
      },
      "item-375": {
        "value": 6,
        "weight": 5
      },
      "item-376": {
        "value": 9,
        "weight": 7
      },
      "item-377": {
        "value": 4,
        "weight": 8
      },
      "item-378": {
        "value": 4,
        "weight": 3
      },
      "item-379": {
        "value": 8,
        "weight": 8
      },
      "item-380": {
        "value": 4,
        "weight": 1
      },
      "item-381": {
        "value": 2,
        "weight": 8
      },
      "item-382": {
        "value": 3,
        "weight": 7
      },
      "item-383": {
        "value": 6,
        "weight": 7
      },
      "item-384": {
        "value": 7,
        "weight": 2
      },
      "item-385": {
        "value": 8,
        "weight": 5
      },
      "item-386": {
        "value": 4,
        "weight": 5
      },
      "item-387": {
        "value": 2,
        "weight": 1
      },
      "item-388": {
        "value": 3,
        "weight": 3
      },
      "item-389": {
        "value": 6,
        "weight": 8
      },
      "item-390": {
        "value": 5,
        "weight": 8
      },
      "item-391": {
        "value": 3,
        "weight": 2
      },
      "item-392": {
        "value": 4,
        "weight": 6
      },
      "item-393": {
        "value": 5,
        "weight": 8
      },
      "item-394": {
        "value": 2,
        "weight": 6
      },
      "item-395": {
        "value": 1,
        "weight": 9
      },
      "item-396": {
        "value": 2,
        "weight": 6
      },
      "item-397": {
        "value": 9,
        "weight": 6
      },
      "item-398": {
        "value": 3,
        "weight": 7
      },
      "item-399": {
        "value": 4,
        "weight": 1
      },
      "item-400": {
        "value": 9,
        "weight": 7
      },
      "item-401": {
        "value": 8,
        "weight": 7
      },
      "item-402": {
        "value": 8,
        "weight": 1
      },
      "item-403": {
        "value": 8,
        "weight": 4
      },
      "item-404": {
        "value": 2,
        "weight": 3
      },
      "item-405": {
        "value": 5,
        "weight": 6
      },
      "item-406": {
        "value": 7,
        "weight": 1
      },
      "item-407": {
        "value": 5,
        "weight": 8
      },
      "item-408": {
        "value": 2,
        "weight": 8
      },
      "item-409": {
        "value": 1,
        "weight": 2
      },
      "item-410": {
        "value": 8,
        "weight": 5
      },
      "item-411": {
        "value": 1,
        "weight": 6
      },
      "item-412": {
        "value": 6,
        "weight": 6
      },
      "item-413": {
        "value": 7,
        "weight": 7
      },
      "item-414": {
        "value": 6,
        "weight": 4
      },
      "item-415": {
        "value": 2,
        "weight": 7
      },
      "item-416": {
        "value": 6,
        "weight": 5
      },
      "item-417": {
        "value": 1,
        "weight": 3
      },
      "item-418": {
        "value": 1,
        "weight": 1
      },
      "item-419": {
        "value": 6,
        "weight": 4
      },
      "item-420": {
        "value": 2,
        "weight": 7
      },
      "item-421": {
        "value": 5,
        "weight": 8
      },
      "item-422": {
        "value": 7,
        "weight": 3
      },
      "item-423": {
        "value": 6,
        "weight": 2
      },
      "item-424": {
        "value": 2,
        "weight": 9
      },
      "item-425": {
        "value": 1,
        "weight": 4
      },
      "item-426": {
        "value": 5,
        "weight": 4
      },
      "item-427": {
        "value": 4,
        "weight": 5
      },
      "item-428": {
        "value": 9,
        "weight": 8
      },
      "item-429": {
        "value": 7,
        "weight": 3
      },
      "item-430": {
        "value": 6,
        "weight": 9
      },
      "item-431": {
        "value": 5,
        "weight": 4
      },
      "item-432": {
        "value": 9,
        "weight": 6
      },
      "item-433": {
        "value": 8,
        "weight": 9
      },
      "item-434": {
        "value": 8,
        "weight": 8
      },
      "item-435": {
        "value": 9,
        "weight": 3
      },
      "item-436": {
        "value": 3,
        "weight": 5
      },
      "item-437": {
        "value": 9,
        "weight": 7
      },
      "item-438": {
        "value": 2,
        "weight": 5
      },
      "item-439": {
        "value": 3,
        "weight": 6
      },
      "item-440": {
        "value": 4,
        "weight": 2
      },
      "item-441": {
        "value": 2,
        "weight": 5
      },
      "item-442": {
        "value": 2,
        "weight": 6
      },
      "item-443": {
        "value": 1,
        "weight": 3
      },
      "item-444": {
        "value": 1,
        "weight": 8
      },
      "item-445": {
        "value": 6,
        "weight": 6
      },
      "item-446": {
        "value": 6,
        "weight": 4
      },
      "item-447": {
        "value": 7,
        "weight": 4
      },
      "item-448": {
        "value": 2,
        "weight": 4
      },
      "item-449": {
        "value": 2,
        "weight": 2
      },
      "item-450": {
        "value": 1,
        "weight": 2
      },
      "item-451": {
        "value": 9,
        "weight": 3
      },
      "item-452": {
        "value": 5,
        "weight": 8
      },
      "item-453": {
        "value": 8,
        "weight": 1
      },
      "item-454": {
        "value": 1,
        "weight": 5
      },
      "item-455": {
        "value": 3,
        "weight": 2
      },
      "item-456": {
        "value": 7,
        "weight": 4
      },
      "item-457": {
        "value": 8,
        "weight": 4
      },
      "item-458": {
        "value": 9,
        "weight": 5
      },
      "item-459": {
        "value": 8,
        "weight": 5
      },
      "item-460": {
        "value": 9,
        "weight": 8
      },
      "item-461": {
        "value": 5,
        "weight": 8
      },
      "item-462": {
        "value": 5,
        "weight": 6
      },
      "item-463": {
        "value": 2,
        "weight": 9
      },
      "item-464": {
        "value": 4,
        "weight": 2
      },
      "item-465": {
        "value": 2,
        "weight": 6
      },
      "item-466": {
        "value": 1,
        "weight": 3
      },
      "item-467": {
        "value": 2,
        "weight": 4
      },
      "item-468": {
        "value": 8,
        "weight": 2
      },
      "item-469": {
        "value": 9,
        "weight": 6
      },
      "item-470": {
        "value": 5,
        "weight": 2
      },
      "item-471": {
        "value": 8,
        "weight": 6
      },
      "item-472": {
        "value": 8,
        "weight": 9
      },
      "item-473": {
        "value": 1,
        "weight": 9
      },
      "item-474": {
        "value": 2,
        "weight": 1
      },
      "item-475": {
        "value": 2,
        "weight": 7
      },
      "item-476": {
        "value": 1,
        "weight": 3
      },
      "item-477": {
        "value": 4,
        "weight": 4
      },
      "item-478": {
        "value": 8,
        "weight": 1
      },
      "item-479": {
        "value": 2,
        "weight": 2
      },
      "item-480": {
        "value": 7,
        "weight": 7
      },
      "item-481": {
        "value": 6,
        "weight": 9
      },
      "item-482": {
        "value": 2,
        "weight": 8
      },
      "item-483": {
        "value": 9,
        "weight": 6
      },
      "item-484": {
        "value": 3,
        "weight": 7
      },
      "item-485": {
        "value": 6,
        "weight": 6
      },
      "item-486": {
        "value": 5,
        "weight": 1
      },
      "item-487": {
        "value": 2,
        "weight": 6
      },
      "item-488": {
        "value": 9,
        "weight": 5
      },
      "item-489": {
        "value": 6,
        "weight": 4
      },
      "item-490": {
        "value": 9,
        "weight": 2
      },
      "item-491": {
        "value": 7,
        "weight": 4
      },
      "item-492": {
        "value": 5,
        "weight": 5
      },
      "item-493": {
        "value": 6,
        "weight": 3
      },
      "item-494": {
        "value": 3,
        "weight": 9
      },
      "item-495": {
        "value": 8,
        "weight": 5
      },
      "item-496": {
        "value": 5,
        "weight": 3
      },
      "item-497": {
        "value": 9,
        "weight": 8
      },
      "item-498": {
        "value": 9,
        "weight": 9
      },
      "item-499": {
        "value": 8,
        "weight": 4
      },
      "item-500": {
        "value": 3,
        "weight": 7
      },
      "item-501": {
        "value": 4,
        "weight": 3
      },
      "item-502": {
        "value": 8,
        "weight": 1
      },
      "item-503": {
        "value": 6,
        "weight": 9
      },
      "item-504": {
        "value": 1,
        "weight": 7
      },
      "item-505": {
        "value": 6,
        "weight": 1
      },
      "item-506": {
        "value": 5,
        "weight": 1
      },
      "item-507": {
        "value": 3,
        "weight": 9
      },
      "item-508": {
        "value": 7,
        "weight": 1
      },
      "item-509": {
        "value": 7,
        "weight": 5
      },
      "item-510": {
        "value": 2,
        "weight": 9
      },
      "item-511": {
        "value": 6,
        "weight": 5
      },
      "item-512": {
        "value": 3,
        "weight": 7
      },
      "item-513": {
        "value": 5,
        "weight": 1
      },
      "item-514": {
        "value": 5,
        "weight": 3
      },
      "item-515": {
        "value": 5,
        "weight": 7
      },
      "item-516": {
        "value": 3,
        "weight": 7
      },
      "item-517": {
        "value": 2,
        "weight": 2
      },
      "item-518": {
        "value": 9,
        "weight": 1
      },
      "item-519": {
        "value": 5,
        "weight": 4
      },
      "item-520": {
        "value": 2,
        "weight": 1
      },
      "item-521": {
        "value": 3,
        "weight": 4
      },
      "item-522": {
        "value": 7,
        "weight": 6
      },
      "item-523": {
        "value": 8,
        "weight": 8
      },
      "item-524": {
        "value": 5,
        "weight": 5
      },
      "item-525": {
        "value": 1,
        "weight": 8
      },
      "item-526": {
        "value": 9,
        "weight": 5
      },
      "item-527": {
        "value": 6,
        "weight": 6
      },
      "item-528": {
        "value": 4,
        "weight": 8
      },
      "item-529": {
        "value": 3,
        "weight": 1
      },
      "item-530": {
        "value": 8,
        "weight": 6
      },
      "item-531": {
        "value": 8,
        "weight": 1
      },
      "item-532": {
        "value": 2,
        "weight": 2
      },
      "item-533": {
        "value": 9,
        "weight": 3
      },
      "item-534": {
        "value": 6,
        "weight": 3
      },
      "item-535": {
        "value": 4,
        "weight": 2
      },
      "item-536": {
        "value": 4,
        "weight": 3
      },
      "item-537": {
        "value": 4,
        "weight": 1
      },
      "item-538": {
        "value": 8,
        "weight": 8
      },
      "item-539": {
        "value": 6,
        "weight": 7
      },
      "item-540": {
        "value": 6,
        "weight": 3
      },
      "item-541": {
        "value": 6,
        "weight": 4
      },
      "item-542": {
        "value": 3,
        "weight": 3
      },
      "item-543": {
        "value": 3,
        "weight": 5
      },
      "item-544": {
        "value": 5,
        "weight": 5
      },
      "item-545": {
        "value": 6,
        "weight": 5
      },
      "item-546": {
        "value": 6,
        "weight": 3
      },
      "item-547": {
        "value": 4,
        "weight": 8
      },
      "item-548": {
        "value": 1,
        "weight": 6
      },
      "item-549": {
        "value": 4,
        "weight": 4
      },
      "item-550": {
        "value": 1,
        "weight": 2
      },
      "item-551": {
        "value": 7,
        "weight": 2
      },
      "item-552": {
        "value": 4,
        "weight": 9
      },
      "item-553": {
        "value": 2,
        "weight": 1
      },
      "item-554": {
        "value": 8,
        "weight": 8
      },
      "item-555": {
        "value": 6,
        "weight": 8
      },
      "item-556": {
        "value": 2,
        "weight": 1
      },
      "item-557": {
        "value": 7,
        "weight": 9
      },
      "item-558": {
        "value": 2,
        "weight": 5
      },
      "item-559": {
        "value": 7,
        "weight": 9
      },
      "item-560": {
        "value": 4,
        "weight": 4
      },
      "item-561": {
        "value": 3,
        "weight": 4
      },
      "item-562": {
        "value": 2,
        "weight": 5
      },
      "item-563": {
        "value": 8,
        "weight": 5
      },
      "item-564": {
        "value": 6,
        "weight": 2
      },
      "item-565": {
        "value": 7,
        "weight": 9
      },
      "item-566": {
        "value": 6,
        "weight": 4
      },
      "item-567": {
        "value": 1,
        "weight": 7
      },
      "item-568": {
        "value": 2,
        "weight": 9
      },
      "item-569": {
        "value": 8,
        "weight": 8
      },
      "item-570": {
        "value": 4,
        "weight": 4
      },
      "item-571": {
        "value": 6,
        "weight": 6
      },
      "item-572": {
        "value": 1,
        "weight": 4
      },
      "item-573": {
        "value": 7,
        "weight": 6
      },
      "item-574": {
        "value": 7,
        "weight": 4
      },
      "item-575": {
        "value": 6,
        "weight": 8
      },
      "item-576": {
        "value": 6,
        "weight": 2
      },
      "item-577": {
        "value": 9,
        "weight": 9
      },
      "item-578": {
        "value": 4,
        "weight": 5
      },
      "item-579": {
        "value": 1,
        "weight": 8
      },
      "item-580": {
        "value": 7,
        "weight": 9
      },
      "item-581": {
        "value": 3,
        "weight": 6
      },
      "item-582": {
        "value": 4,
        "weight": 8
      },
      "item-583": {
        "value": 5,
        "weight": 9
      },
      "item-584": {
        "value": 5,
        "weight": 5
      },
      "item-585": {
        "value": 8,
        "weight": 2
      },
      "item-586": {
        "value": 1,
        "weight": 9
      },
      "item-587": {
        "value": 7,
        "weight": 2
      },
      "item-588": {
        "value": 7,
        "weight": 6
      },
      "item-589": {
        "value": 7,
        "weight": 8
      },
      "item-590": {
        "value": 5,
        "weight": 8
      },
      "item-591": {
        "value": 3,
        "weight": 9
      },
      "item-592": {
        "value": 9,
        "weight": 1
      },
      "item-593": {
        "value": 9,
        "weight": 5
      },
      "item-594": {
        "value": 9,
        "weight": 6
      },
      "item-595": {
        "value": 2,
        "weight": 4
      },
      "item-596": {
        "value": 9,
        "weight": 3
      },
      "item-597": {
        "value": 7,
        "weight": 8
      },
      "item-598": {
        "value": 4,
        "weight": 8
      },
      "item-599": {
        "value": 1,
        "weight": 4
      },
      "item-600": {
        "value": 8,
        "weight": 6
      },
      "item-601": {
        "value": 6,
        "weight": 8
      },
      "item-602": {
        "value": 7,
        "weight": 1
      },
      "item-603": {
        "value": 1,
        "weight": 5
      },
      "item-604": {
        "value": 4,
        "weight": 6
      },
      "item-605": {
        "value": 2,
        "weight": 1
      },
      "item-606": {
        "value": 5,
        "weight": 2
      },
      "item-607": {
        "value": 8,
        "weight": 2
      },
      "item-608": {
        "value": 5,
        "weight": 1
      },
      "item-609": {
        "value": 1,
        "weight": 7
      },
      "item-610": {
        "value": 2,
        "weight": 9
      },
      "item-611": {
        "value": 4,
        "weight": 3
      },
      "item-612": {
        "value": 2,
        "weight": 3
      },
      "item-613": {
        "value": 6,
        "weight": 7
      },
      "item-614": {
        "value": 4,
        "weight": 2
      },
      "item-615": {
        "value": 7,
        "weight": 5
      },
      "item-616": {
        "value": 1,
        "weight": 8
      },
      "item-617": {
        "value": 8,
        "weight": 1
      },
      "item-618": {
        "value": 6,
        "weight": 6
      },
      "item-619": {
        "value": 3,
        "weight": 3
      },
      "item-620": {
        "value": 1,
        "weight": 2
      },
      "item-621": {
        "value": 1,
        "weight": 2
      },
      "item-622": {
        "value": 1,
        "weight": 7
      },
      "item-623": {
        "value": 7,
        "weight": 7
      },
      "item-624": {
        "value": 6,
        "weight": 2
      },
      "item-625": {
        "value": 7,
        "weight": 6
      },
      "item-626": {
        "value": 6,
        "weight": 3
      },
      "item-627": {
        "value": 5,
        "weight": 1
      },
      "item-628": {
        "value": 2,
        "weight": 3
      },
      "item-629": {
        "value": 2,
        "weight": 5
      },
      "item-630": {
        "value": 1,
        "weight": 5
      },
      "item-631": {
        "value": 9,
        "weight": 2
      },
      "item-632": {
        "value": 9,
        "weight": 2
      },
      "item-633": {
        "value": 8,
        "weight": 3
      },
      "item-634": {
        "value": 4,
        "weight": 6
      },
      "item-635": {
        "value": 5,
        "weight": 7
      },
      "item-636": {
        "value": 8,
        "weight": 3
      },
      "item-637": {
        "value": 5,
        "weight": 1
      },
      "item-638": {
        "value": 3,
        "weight": 9
      },
      "item-639": {
        "value": 3,
        "weight": 4
      },
      "item-640": {
        "value": 6,
        "weight": 3
      },
      "item-641": {
        "value": 9,
        "weight": 3
      },
      "item-642": {
        "value": 6,
        "weight": 7
      },
      "item-643": {
        "value": 7,
        "weight": 6
      },
      "item-644": {
        "value": 5,
        "weight": 9
      },
      "item-645": {
        "value": 5,
        "weight": 9
      },
      "item-646": {
        "value": 7,
        "weight": 1
      },
      "item-647": {
        "value": 7,
        "weight": 4
      },
      "item-648": {
        "value": 1,
        "weight": 5
      },
      "item-649": {
        "value": 4,
        "weight": 2
      },
      "item-650": {
        "value": 3,
        "weight": 4
      },
      "item-651": {
        "value": 1,
        "weight": 8
      },
      "item-652": {
        "value": 1,
        "weight": 4
      },
      "item-653": {
        "value": 4,
        "weight": 2
      },
      "item-654": {
        "value": 5,
        "weight": 1
      },
      "item-655": {
        "value": 8,
        "weight": 4
      },
      "item-656": {
        "value": 9,
        "weight": 3
      },
      "item-657": {
        "value": 9,
        "weight": 9
      },
      "item-658": {
        "value": 8,
        "weight": 2
      },
      "item-659": {
        "value": 7,
        "weight": 9
      },
      "item-660": {
        "value": 9,
        "weight": 4
      },
      "item-661": {
        "value": 3,
        "weight": 9
      },
      "item-662": {
        "value": 3,
        "weight": 7
      },
      "item-663": {
        "value": 4,
        "weight": 1
      },
      "item-664": {
        "value": 6,
        "weight": 1
      },
      "item-665": {
        "value": 5,
        "weight": 9
      },
      "item-666": {
        "value": 9,
        "weight": 7
      },
      "item-667": {
        "value": 5,
        "weight": 7
      },
      "item-668": {
        "value": 1,
        "weight": 9
      },
      "item-669": {
        "value": 7,
        "weight": 1
      },
      "item-670": {
        "value": 5,
        "weight": 1
      },
      "item-671": {
        "value": 7,
        "weight": 9
      },
      "item-672": {
        "value": 7,
        "weight": 2
      },
      "item-673": {
        "value": 1,
        "weight": 1
      },
      "item-674": {
        "value": 6,
        "weight": 6
      },
      "item-675": {
        "value": 4,
        "weight": 6
      },
      "item-676": {
        "value": 7,
        "weight": 3
      },
      "item-677": {
        "value": 2,
        "weight": 4
      },
      "item-678": {
        "value": 4,
        "weight": 2
      },
      "item-679": {
        "value": 5,
        "weight": 9
      },
      "item-680": {
        "value": 1,
        "weight": 7
      },
      "item-681": {
        "value": 7,
        "weight": 8
      },
      "item-682": {
        "value": 5,
        "weight": 9
      },
      "item-683": {
        "value": 4,
        "weight": 4
      },
      "item-684": {
        "value": 8,
        "weight": 9
      },
      "item-685": {
        "value": 9,
        "weight": 1
      },
      "item-686": {
        "value": 7,
        "weight": 3
      },
      "item-687": {
        "value": 3,
        "weight": 7
      },
      "item-688": {
        "value": 7,
        "weight": 3
      },
      "item-689": {
        "value": 3,
        "weight": 5
      },
      "item-690": {
        "value": 8,
        "weight": 5
      },
      "item-691": {
        "value": 2,
        "weight": 3
      },
      "item-692": {
        "value": 6,
        "weight": 4
      },
      "item-693": {
        "value": 4,
        "weight": 4
      },
      "item-694": {
        "value": 7,
        "weight": 3
      },
      "item-695": {
        "value": 4,
        "weight": 9
      },
      "item-696": {
        "value": 2,
        "weight": 1
      },
      "item-697": {
        "value": 3,
        "weight": 9
      },
      "item-698": {
        "value": 2,
        "weight": 6
      },
      "item-699": {
        "value": 5,
        "weight": 1
      },
      "item-700": {
        "value": 1,
        "weight": 9
      },
      "item-701": {
        "value": 3,
        "weight": 2
      },
      "item-702": {
        "value": 4,
        "weight": 7
      },
      "item-703": {
        "value": 5,
        "weight": 6
      },
      "item-704": {
        "value": 9,
        "weight": 1
      },
      "item-705": {
        "value": 1,
        "weight": 9
      },
      "item-706": {
        "value": 8,
        "weight": 4
      },
      "item-707": {
        "value": 1,
        "weight": 9
      },
      "item-708": {
        "value": 8,
        "weight": 7
      },
      "item-709": {
        "value": 1,
        "weight": 9
      },
      "item-710": {
        "value": 3,
        "weight": 7
      },
      "item-711": {
        "value": 3,
        "weight": 6
      },
      "item-712": {
        "value": 8,
        "weight": 1
      },
      "item-713": {
        "value": 2,
        "weight": 7
      },
      "item-714": {
        "value": 8,
        "weight": 3
      },
      "item-715": {
        "value": 3,
        "weight": 3
      },
      "item-716": {
        "value": 3,
        "weight": 4
      },
      "item-717": {
        "value": 4,
        "weight": 9
      },
      "item-718": {
        "value": 8,
        "weight": 3
      },
      "item-719": {
        "value": 3,
        "weight": 1
      },
      "item-720": {
        "value": 5,
        "weight": 6
      },
      "item-721": {
        "value": 2,
        "weight": 6
      },
      "item-722": {
        "value": 1,
        "weight": 8
      },
      "item-723": {
        "value": 2,
        "weight": 5
      },
      "item-724": {
        "value": 9,
        "weight": 3
      },
      "item-725": {
        "value": 5,
        "weight": 2
      },
      "item-726": {
        "value": 8,
        "weight": 3
      },
      "item-727": {
        "value": 6,
        "weight": 7
      },
      "item-728": {
        "value": 5,
        "weight": 4
      },
      "item-729": {
        "value": 1,
        "weight": 8
      },
      "item-730": {
        "value": 4,
        "weight": 9
      },
      "item-731": {
        "value": 4,
        "weight": 7
      },
      "item-732": {
        "value": 1,
        "weight": 8
      },
      "item-733": {
        "value": 4,
        "weight": 7
      },
      "item-734": {
        "value": 7,
        "weight": 1
      },
      "item-735": {
        "value": 4,
        "weight": 4
      },
      "item-736": {
        "value": 5,
        "weight": 8
      },
      "item-737": {
        "value": 6,
        "weight": 4
      },
      "item-738": {
        "value": 9,
        "weight": 1
      },
      "item-739": {
        "value": 7,
        "weight": 6
      },
      "item-740": {
        "value": 5,
        "weight": 9
      },
      "item-741": {
        "value": 5,
        "weight": 6
      },
      "item-742": {
        "value": 5,
        "weight": 2
      },
      "item-743": {
        "value": 3,
        "weight": 2
      },
      "item-744": {
        "value": 5,
        "weight": 2
      },
      "item-745": {
        "value": 5,
        "weight": 2
      },
      "item-746": {
        "value": 3,
        "weight": 6
      },
      "item-747": {
        "value": 6,
        "weight": 9
      },
      "item-748": {
        "value": 8,
        "weight": 2
      },
      "item-749": {
        "value": 4,
        "weight": 9
      },
      "item-750": {
        "value": 3,
        "weight": 6
      },
      "item-751": {
        "value": 5,
        "weight": 9
      },
      "item-752": {
        "value": 7,
        "weight": 8
      },
      "item-753": {
        "value": 5,
        "weight": 2
      },
      "item-754": {
        "value": 2,
        "weight": 8
      },
      "item-755": {
        "value": 6,
        "weight": 4
      },
      "item-756": {
        "value": 1,
        "weight": 2
      },
      "item-757": {
        "value": 5,
        "weight": 1
      },
      "item-758": {
        "value": 7,
        "weight": 8
      },
      "item-759": {
        "value": 7,
        "weight": 4
      },
      "item-760": {
        "value": 3,
        "weight": 7
      },
      "item-761": {
        "value": 6,
        "weight": 4
      },
      "item-762": {
        "value": 3,
        "weight": 7
      },
      "item-763": {
        "value": 8,
        "weight": 4
      },
      "item-764": {
        "value": 8,
        "weight": 5
      },
      "item-765": {
        "value": 3,
        "weight": 8
      },
      "item-766": {
        "value": 8,
        "weight": 7
      },
      "item-767": {
        "value": 7,
        "weight": 2
      },
      "item-768": {
        "value": 3,
        "weight": 1
      },
      "item-769": {
        "value": 9,
        "weight": 7
      },
      "item-770": {
        "value": 7,
        "weight": 5
      },
      "item-771": {
        "value": 3,
        "weight": 6
      },
      "item-772": {
        "value": 6,
        "weight": 4
      },
      "item-773": {
        "value": 2,
        "weight": 1
      },
      "item-774": {
        "value": 8,
        "weight": 4
      },
      "item-775": {
        "value": 6,
        "weight": 8
      },
      "item-776": {
        "value": 8,
        "weight": 3
      },
      "item-777": {
        "value": 2,
        "weight": 9
      },
      "item-778": {
        "value": 7,
        "weight": 4
      },
      "item-779": {
        "value": 6,
        "weight": 5
      },
      "item-780": {
        "value": 8,
        "weight": 6
      },
      "item-781": {
        "value": 2,
        "weight": 2
      },
      "item-782": {
        "value": 6,
        "weight": 3
      },
      "item-783": {
        "value": 7,
        "weight": 5
      },
      "item-784": {
        "value": 4,
        "weight": 2
      },
      "item-785": {
        "value": 1,
        "weight": 6
      },
      "item-786": {
        "value": 1,
        "weight": 5
      },
      "item-787": {
        "value": 6,
        "weight": 5
      },
      "item-788": {
        "value": 7,
        "weight": 9
      },
      "item-789": {
        "value": 3,
        "weight": 8
      },
      "item-790": {
        "value": 3,
        "weight": 8
      },
      "item-791": {
        "value": 7,
        "weight": 6
      },
      "item-792": {
        "value": 3,
        "weight": 4
      },
      "item-793": {
        "value": 4,
        "weight": 4
      },
      "item-794": {
        "value": 4,
        "weight": 8
      },
      "item-795": {
        "value": 3,
        "weight": 2
      },
      "item-796": {
        "value": 8,
        "weight": 6
      },
      "item-797": {
        "value": 4,
        "weight": 5
      },
      "item-798": {
        "value": 2,
        "weight": 1
      },
      "item-799": {
        "value": 1,
        "weight": 9
      },
      "item-800": {
        "value": 5,
        "weight": 4
      },
      "item-801": {
        "value": 4,
        "weight": 5
      },
      "item-802": {
        "value": 7,
        "weight": 4
      },
      "item-803": {
        "value": 9,
        "weight": 7
      },
      "item-804": {
        "value": 7,
        "weight": 4
      },
      "item-805": {
        "value": 6,
        "weight": 9
      },
      "item-806": {
        "value": 3,
        "weight": 2
      },
      "item-807": {
        "value": 9,
        "weight": 7
      },
      "item-808": {
        "value": 5,
        "weight": 8
      },
      "item-809": {
        "value": 5,
        "weight": 6
      },
      "item-810": {
        "value": 8,
        "weight": 2
      },
      "item-811": {
        "value": 6,
        "weight": 4
      },
      "item-812": {
        "value": 8,
        "weight": 7
      },
      "item-813": {
        "value": 4,
        "weight": 7
      },
      "item-814": {
        "value": 9,
        "weight": 7
      },
      "item-815": {
        "value": 9,
        "weight": 4
      },
      "item-816": {
        "value": 1,
        "weight": 9
      },
      "item-817": {
        "value": 6,
        "weight": 5
      },
      "item-818": {
        "value": 5,
        "weight": 7
      },
      "item-819": {
        "value": 6,
        "weight": 6
      },
      "item-820": {
        "value": 4,
        "weight": 6
      },
      "item-821": {
        "value": 8,
        "weight": 3
      },
      "item-822": {
        "value": 9,
        "weight": 9
      },
      "item-823": {
        "value": 2,
        "weight": 3
      },
      "item-824": {
        "value": 4,
        "weight": 9
      },
      "item-825": {
        "value": 5,
        "weight": 1
      },
      "item-826": {
        "value": 4,
        "weight": 1
      },
      "item-827": {
        "value": 3,
        "weight": 5
      },
      "item-828": {
        "value": 3,
        "weight": 6
      },
      "item-829": {
        "value": 7,
        "weight": 8
      },
      "item-830": {
        "value": 5,
        "weight": 9
      },
      "item-831": {
        "value": 9,
        "weight": 3
      },
      "item-832": {
        "value": 5,
        "weight": 7
      },
      "item-833": {
        "value": 1,
        "weight": 4
      },
      "item-834": {
        "value": 8,
        "weight": 5
      },
      "item-835": {
        "value": 4,
        "weight": 3
      },
      "item-836": {
        "value": 7,
        "weight": 6
      },
      "item-837": {
        "value": 9,
        "weight": 4
      },
      "item-838": {
        "value": 8,
        "weight": 1
      },
      "item-839": {
        "value": 2,
        "weight": 5
      },
      "item-840": {
        "value": 4,
        "weight": 8
      },
      "item-841": {
        "value": 3,
        "weight": 7
      },
      "item-842": {
        "value": 3,
        "weight": 1
      },
      "item-843": {
        "value": 4,
        "weight": 2
      },
      "item-844": {
        "value": 7,
        "weight": 9
      },
      "item-845": {
        "value": 3,
        "weight": 6
      },
      "item-846": {
        "value": 6,
        "weight": 6
      },
      "item-847": {
        "value": 2,
        "weight": 4
      },
      "item-848": {
        "value": 1,
        "weight": 1
      },
      "item-849": {
        "value": 5,
        "weight": 3
      },
      "item-850": {
        "value": 9,
        "weight": 4
      },
      "item-851": {
        "value": 2,
        "weight": 5
      },
      "item-852": {
        "value": 2,
        "weight": 5
      },
      "item-853": {
        "value": 2,
        "weight": 9
      },
      "item-854": {
        "value": 9,
        "weight": 5
      },
      "item-855": {
        "value": 1,
        "weight": 1
      },
      "item-856": {
        "value": 5,
        "weight": 2
      },
      "item-857": {
        "value": 6,
        "weight": 7
      },
      "item-858": {
        "value": 3,
        "weight": 2
      },
      "item-859": {
        "value": 3,
        "weight": 2
      },
      "item-860": {
        "value": 6,
        "weight": 7
      },
      "item-861": {
        "value": 6,
        "weight": 9
      },
      "item-862": {
        "value": 4,
        "weight": 6
      },
      "item-863": {
        "value": 3,
        "weight": 8
      },
      "item-864": {
        "value": 9,
        "weight": 7
      },
      "item-865": {
        "value": 9,
        "weight": 6
      },
      "item-866": {
        "value": 1,
        "weight": 4
      },
      "item-867": {
        "value": 6,
        "weight": 4
      },
      "item-868": {
        "value": 7,
        "weight": 5
      },
      "item-869": {
        "value": 1,
        "weight": 1
      },
      "item-870": {
        "value": 6,
        "weight": 9
      },
      "item-871": {
        "value": 8,
        "weight": 9
      },
      "item-872": {
        "value": 7,
        "weight": 8
      },
      "item-873": {
        "value": 9,
        "weight": 9
      },
      "item-874": {
        "value": 4,
        "weight": 1
      },
      "item-875": {
        "value": 1,
        "weight": 1
      },
      "item-876": {
        "value": 1,
        "weight": 2
      },
      "item-877": {
        "value": 4,
        "weight": 3
      },
      "item-878": {
        "value": 9,
        "weight": 8
      },
      "item-879": {
        "value": 3,
        "weight": 9
      },
      "item-880": {
        "value": 2,
        "weight": 4
      },
      "item-881": {
        "value": 9,
        "weight": 1
      },
      "item-882": {
        "value": 3,
        "weight": 5
      },
      "item-883": {
        "value": 2,
        "weight": 4
      },
      "item-884": {
        "value": 3,
        "weight": 2
      },
      "item-885": {
        "value": 4,
        "weight": 1
      },
      "item-886": {
        "value": 4,
        "weight": 7
      },
      "item-887": {
        "value": 7,
        "weight": 1
      },
      "item-888": {
        "value": 5,
        "weight": 2
      },
      "item-889": {
        "value": 6,
        "weight": 6
      },
      "item-890": {
        "value": 8,
        "weight": 6
      },
      "item-891": {
        "value": 6,
        "weight": 3
      },
      "item-892": {
        "value": 5,
        "weight": 6
      },
      "item-893": {
        "value": 1,
        "weight": 9
      },
      "item-894": {
        "value": 6,
        "weight": 5
      },
      "item-895": {
        "value": 1,
        "weight": 7
      },
      "item-896": {
        "value": 8,
        "weight": 8
      },
      "item-897": {
        "value": 7,
        "weight": 1
      },
      "item-898": {
        "value": 4,
        "weight": 1
      },
      "item-899": {
        "value": 2,
        "weight": 7
      },
      "item-900": {
        "value": 9,
        "weight": 6
      },
      "item-901": {
        "value": 8,
        "weight": 9
      },
      "item-902": {
        "value": 5,
        "weight": 3
      },
      "item-903": {
        "value": 8,
        "weight": 1
      },
      "item-904": {
        "value": 8,
        "weight": 9
      },
      "item-905": {
        "value": 8,
        "weight": 1
      },
      "item-906": {
        "value": 1,
        "weight": 1
      },
      "item-907": {
        "value": 7,
        "weight": 1
      },
      "item-908": {
        "value": 7,
        "weight": 5
      },
      "item-909": {
        "value": 9,
        "weight": 9
      },
      "item-910": {
        "value": 2,
        "weight": 6
      },
      "item-911": {
        "value": 7,
        "weight": 2
      },
      "item-912": {
        "value": 1,
        "weight": 8
      },
      "item-913": {
        "value": 3,
        "weight": 4
      },
      "item-914": {
        "value": 4,
        "weight": 1
      },
      "item-915": {
        "value": 9,
        "weight": 3
      },
      "item-916": {
        "value": 5,
        "weight": 2
      },
      "item-917": {
        "value": 7,
        "weight": 7
      },
      "item-918": {
        "value": 8,
        "weight": 1
      },
      "item-919": {
        "value": 8,
        "weight": 8
      },
      "item-920": {
        "value": 6,
        "weight": 9
      },
      "item-921": {
        "value": 4,
        "weight": 6
      },
      "item-922": {
        "value": 8,
        "weight": 7
      },
      "item-923": {
        "value": 2,
        "weight": 7
      },
      "item-924": {
        "value": 4,
        "weight": 9
      },
      "item-925": {
        "value": 8,
        "weight": 7
      },
      "item-926": {
        "value": 5,
        "weight": 4
      },
      "item-927": {
        "value": 6,
        "weight": 9
      },
      "item-928": {
        "value": 4,
        "weight": 6
      },
      "item-929": {
        "value": 4,
        "weight": 5
      },
      "item-930": {
        "value": 4,
        "weight": 3
      },
      "item-931": {
        "value": 9,
        "weight": 4
      },
      "item-932": {
        "value": 2,
        "weight": 6
      },
      "item-933": {
        "value": 9,
        "weight": 6
      },
      "item-934": {
        "value": 2,
        "weight": 7
      },
      "item-935": {
        "value": 1,
        "weight": 7
      },
      "item-936": {
        "value": 2,
        "weight": 3
      },
      "item-937": {
        "value": 5,
        "weight": 2
      },
      "item-938": {
        "value": 1,
        "weight": 2
      },
      "item-939": {
        "value": 4,
        "weight": 1
      },
      "item-940": {
        "value": 2,
        "weight": 8
      },
      "item-941": {
        "value": 5,
        "weight": 5
      },
      "item-942": {
        "value": 7,
        "weight": 9
      },
      "item-943": {
        "value": 3,
        "weight": 8
      },
      "item-944": {
        "value": 4,
        "weight": 6
      },
      "item-945": {
        "value": 6,
        "weight": 1
      },
      "item-946": {
        "value": 9,
        "weight": 2
      },
      "item-947": {
        "value": 2,
        "weight": 7
      },
      "item-948": {
        "value": 7,
        "weight": 5
      },
      "item-949": {
        "value": 5,
        "weight": 2
      },
      "item-950": {
        "value": 2,
        "weight": 6
      },
      "item-951": {
        "value": 2,
        "weight": 9
      },
      "item-952": {
        "value": 6,
        "weight": 2
      },
      "item-953": {
        "value": 4,
        "weight": 7
      },
      "item-954": {
        "value": 2,
        "weight": 2
      },
      "item-955": {
        "value": 2,
        "weight": 2
      },
      "item-956": {
        "value": 4,
        "weight": 8
      },
      "item-957": {
        "value": 6,
        "weight": 9
      },
      "item-958": {
        "value": 9,
        "weight": 1
      },
      "item-959": {
        "value": 7,
        "weight": 2
      },
      "item-960": {
        "value": 9,
        "weight": 9
      },
      "item-961": {
        "value": 3,
        "weight": 5
      },
      "item-962": {
        "value": 9,
        "weight": 9
      },
      "item-963": {
        "value": 3,
        "weight": 2
      },
      "item-964": {
        "value": 2,
        "weight": 3
      },
      "item-965": {
        "value": 2,
        "weight": 5
      },
      "item-966": {
        "value": 1,
        "weight": 2
      },
      "item-967": {
        "value": 5,
        "weight": 9
      },
      "item-968": {
        "value": 2,
        "weight": 7
      },
      "item-969": {
        "value": 2,
        "weight": 1
      },
      "item-970": {
        "value": 4,
        "weight": 6
      },
      "item-971": {
        "value": 9,
        "weight": 3
      },
      "item-972": {
        "value": 5,
        "weight": 6
      },
      "item-973": {
        "value": 3,
        "weight": 8
      },
      "item-974": {
        "value": 3,
        "weight": 6
      },
      "item-975": {
        "value": 9,
        "weight": 9
      },
      "item-976": {
        "value": 4,
        "weight": 8
      },
      "item-977": {
        "value": 2,
        "weight": 6
      },
      "item-978": {
        "value": 1,
        "weight": 2
      },
      "item-979": {
        "value": 7,
        "weight": 5
      },
      "item-980": {
        "value": 1,
        "weight": 7
      },
      "item-981": {
        "value": 9,
        "weight": 4
      },
      "item-982": {
        "value": 3,
        "weight": 2
      },
      "item-983": {
        "value": 4,
        "weight": 5
      },
      "item-984": {
        "value": 4,
        "weight": 4
      },
      "item-985": {
        "value": 6,
        "weight": 2
      },
      "item-986": {
        "value": 8,
        "weight": 3
      },
      "item-987": {
        "value": 2,
        "weight": 8
      },
      "item-988": {
        "value": 6,
        "weight": 3
      },
      "item-989": {
        "value": 1,
        "weight": 6
      },
      "item-990": {
        "value": 7,
        "weight": 9
      },
      "item-991": {
        "value": 7,
        "weight": 5
      },
      "item-992": {
        "value": 8,
        "weight": 2
      },
      "item-993": {
        "value": 9,
        "weight": 3
      },
      "item-994": {
        "value": 2,
        "weight": 2
      },
      "item-995": {
        "value": 1,
        "weight": 6
      },
      "item-996": {
        "value": 6,
        "weight": 3
      },
      "item-997": {
        "value": 4,
        "weight": 1
      },
      "item-998": {
        "value": 5,
        "weight": 3
      },
      "item-999": {
        "value": 2,
        "weight": 3
      },
      "item-1000": {
        "value": 4,
        "weight": 5
      },
      "item-1001": {
        "value": 3,
        "weight": 2
      },
      "item-1002": {
        "value": 2,
        "weight": 8
      },
      "item-1003": {
        "value": 6,
        "weight": 2
      },
      "item-1004": {
        "value": 1,
        "weight": 4
      },
      "item-1005": {
        "value": 2,
        "weight": 3
      },
      "item-1006": {
        "value": 1,
        "weight": 2
      },
      "item-1007": {
        "value": 2,
        "weight": 9
      },
      "item-1008": {
        "value": 4,
        "weight": 4
      },
      "item-1009": {
        "value": 6,
        "weight": 3
      },
      "item-1010": {
        "value": 9,
        "weight": 2
      },
      "item-1011": {
        "value": 5,
        "weight": 2
      },
      "item-1012": {
        "value": 3,
        "weight": 2
      },
      "item-1013": {
        "value": 2,
        "weight": 4
      },
      "item-1014": {
        "value": 9,
        "weight": 3
      },
      "item-1015": {
        "value": 3,
        "weight": 2
      },
      "item-1016": {
        "value": 3,
        "weight": 5
      },
      "item-1017": {
        "value": 2,
        "weight": 3
      },
      "item-1018": {
        "value": 9,
        "weight": 5
      },
      "item-1019": {
        "value": 7,
        "weight": 2
      },
      "item-1020": {
        "value": 2,
        "weight": 3
      },
      "item-1021": {
        "value": 3,
        "weight": 3
      },
      "item-1022": {
        "value": 7,
        "weight": 2
      },
      "item-1023": {
        "value": 1,
        "weight": 6
      },
      "item-1024": {
        "value": 4,
        "weight": 7
      },
      "item-1025": {
        "value": 2,
        "weight": 2
      },
      "item-1026": {
        "value": 4,
        "weight": 5
      },
      "item-1027": {
        "value": 1,
        "weight": 7
      },
      "item-1028": {
        "value": 3,
        "weight": 8
      },
      "item-1029": {
        "value": 7,
        "weight": 6
      },
      "item-1030": {
        "value": 8,
        "weight": 5
      },
      "item-1031": {
        "value": 4,
        "weight": 4
      },
      "item-1032": {
        "value": 1,
        "weight": 6
      },
      "item-1033": {
        "value": 3,
        "weight": 5
      },
      "item-1034": {
        "value": 9,
        "weight": 2
      },
      "item-1035": {
        "value": 3,
        "weight": 6
      },
      "item-1036": {
        "value": 8,
        "weight": 7
      },
      "item-1037": {
        "value": 8,
        "weight": 6
      },
      "item-1038": {
        "value": 4,
        "weight": 2
      },
      "item-1039": {
        "value": 5,
        "weight": 9
      },
      "item-1040": {
        "value": 9,
        "weight": 9
      },
      "item-1041": {
        "value": 6,
        "weight": 7
      },
      "item-1042": {
        "value": 4,
        "weight": 1
      },
      "item-1043": {
        "value": 3,
        "weight": 8
      },
      "item-1044": {
        "value": 8,
        "weight": 8
      },
      "item-1045": {
        "value": 9,
        "weight": 1
      },
      "item-1046": {
        "value": 6,
        "weight": 2
      },
      "item-1047": {
        "value": 5,
        "weight": 3
      },
      "item-1048": {
        "value": 1,
        "weight": 2
      },
      "item-1049": {
        "value": 2,
        "weight": 9
      },
      "item-1050": {
        "value": 6,
        "weight": 6
      },
      "item-1051": {
        "value": 3,
        "weight": 1
      },
      "item-1052": {
        "value": 3,
        "weight": 5
      },
      "item-1053": {
        "value": 7,
        "weight": 2
      },
      "item-1054": {
        "value": 4,
        "weight": 7
      },
      "item-1055": {
        "value": 7,
        "weight": 7
      },
      "item-1056": {
        "value": 6,
        "weight": 5
      },
      "item-1057": {
        "value": 5,
        "weight": 6
      },
      "item-1058": {
        "value": 1,
        "weight": 7
      },
      "item-1059": {
        "value": 1,
        "weight": 2
      },
      "item-1060": {
        "value": 1,
        "weight": 8
      },
      "item-1061": {
        "value": 6,
        "weight": 6
      },
      "item-1062": {
        "value": 3,
        "weight": 8
      },
      "item-1063": {
        "value": 9,
        "weight": 1
      },
      "item-1064": {
        "value": 6,
        "weight": 8
      },
      "item-1065": {
        "value": 2,
        "weight": 5
      },
      "item-1066": {
        "value": 3,
        "weight": 5
      },
      "item-1067": {
        "value": 9,
        "weight": 8
      },
      "item-1068": {
        "value": 4,
        "weight": 6
      },
      "item-1069": {
        "value": 9,
        "weight": 1
      },
      "item-1070": {
        "value": 2,
        "weight": 1
      },
      "item-1071": {
        "value": 4,
        "weight": 1
      },
      "item-1072": {
        "value": 4,
        "weight": 3
      },
      "item-1073": {
        "value": 4,
        "weight": 9
      },
      "item-1074": {
        "value": 8,
        "weight": 8
      },
      "item-1075": {
        "value": 2,
        "weight": 2
      },
      "item-1076": {
        "value": 8,
        "weight": 3
      },
      "item-1077": {
        "value": 7,
        "weight": 4
      },
      "item-1078": {
        "value": 7,
        "weight": 5
      },
      "item-1079": {
        "value": 5,
        "weight": 4
      },
      "item-1080": {
        "value": 4,
        "weight": 8
      },
      "item-1081": {
        "value": 3,
        "weight": 7
      },
      "item-1082": {
        "value": 5,
        "weight": 5
      },
      "item-1083": {
        "value": 4,
        "weight": 7
      },
      "item-1084": {
        "value": 6,
        "weight": 8
      },
      "item-1085": {
        "value": 2,
        "weight": 1
      },
      "item-1086": {
        "value": 5,
        "weight": 7
      },
      "item-1087": {
        "value": 8,
        "weight": 2
      },
      "item-1088": {
        "value": 2,
        "weight": 1
      },
      "item-1089": {
        "value": 9,
        "weight": 9
      },
      "item-1090": {
        "value": 5,
        "weight": 3
      },
      "item-1091": {
        "value": 6,
        "weight": 5
      },
      "item-1092": {
        "value": 5,
        "weight": 2
      },
      "item-1093": {
        "value": 6,
        "weight": 1
      },
      "item-1094": {
        "value": 2,
        "weight": 8
      },
      "item-1095": {
        "value": 1,
        "weight": 3
      },
      "item-1096": {
        "value": 3,
        "weight": 1
      },
      "item-1097": {
        "value": 9,
        "weight": 5
      },
      "item-1098": {
        "value": 9,
        "weight": 2
      },
      "item-1099": {
        "value": 1,
        "weight": 9
      },
      "item-1100": {
        "value": 7,
        "weight": 2
      },
      "item-1101": {
        "value": 7,
        "weight": 9
      },
      "item-1102": {
        "value": 6,
        "weight": 8
      },
      "item-1103": {
        "value": 8,
        "weight": 6
      },
      "item-1104": {
        "value": 6,
        "weight": 8
      },
      "item-1105": {
        "value": 5,
        "weight": 4
      },
      "item-1106": {
        "value": 4,
        "weight": 7
      },
      "item-1107": {
        "value": 8,
        "weight": 2
      },
      "item-1108": {
        "value": 6,
        "weight": 5
      },
      "item-1109": {
        "value": 2,
        "weight": 5
      },
      "item-1110": {
        "value": 6,
        "weight": 3
      },
      "item-1111": {
        "value": 5,
        "weight": 1
      },
      "item-1112": {
        "value": 1,
        "weight": 9
      },
      "item-1113": {
        "value": 3,
        "weight": 5
      },
      "item-1114": {
        "value": 2,
        "weight": 3
      },
      "item-1115": {
        "value": 4,
        "weight": 5
      },
      "item-1116": {
        "value": 5,
        "weight": 8
      },
      "item-1117": {
        "value": 8,
        "weight": 8
      },
      "item-1118": {
        "value": 6,
        "weight": 1
      },
      "item-1119": {
        "value": 5,
        "weight": 4
      },
      "item-1120": {
        "value": 5,
        "weight": 7
      },
      "item-1121": {
        "value": 3,
        "weight": 4
      },
      "item-1122": {
        "value": 5,
        "weight": 6
      },
      "item-1123": {
        "value": 7,
        "weight": 2
      },
      "item-1124": {
        "value": 6,
        "weight": 9
      },
      "item-1125": {
        "value": 4,
        "weight": 3
      },
      "item-1126": {
        "value": 9,
        "weight": 1
      },
      "item-1127": {
        "value": 9,
        "weight": 7
      },
      "item-1128": {
        "value": 4,
        "weight": 6
      },
      "item-1129": {
        "value": 7,
        "weight": 3
      },
      "item-1130": {
        "value": 4,
        "weight": 2
      },
      "item-1131": {
        "value": 8,
        "weight": 9
      },
      "item-1132": {
        "value": 9,
        "weight": 4
      },
      "item-1133": {
        "value": 8,
        "weight": 7
      },
      "item-1134": {
        "value": 8,
        "weight": 5
      },
      "item-1135": {
        "value": 8,
        "weight": 5
      },
      "item-1136": {
        "value": 2,
        "weight": 5
      },
      "item-1137": {
        "value": 4,
        "weight": 3
      },
      "item-1138": {
        "value": 9,
        "weight": 1
      },
      "item-1139": {
        "value": 8,
        "weight": 6
      },
      "item-1140": {
        "value": 3,
        "weight": 3
      },
      "item-1141": {
        "value": 7,
        "weight": 6
      },
      "item-1142": {
        "value": 7,
        "weight": 6
      },
      "item-1143": {
        "value": 7,
        "weight": 3
      },
      "item-1144": {
        "value": 1,
        "weight": 9
      },
      "item-1145": {
        "value": 9,
        "weight": 7
      },
      "item-1146": {
        "value": 7,
        "weight": 7
      },
      "item-1147": {
        "value": 8,
        "weight": 7
      },
      "item-1148": {
        "value": 8,
        "weight": 4
      },
      "item-1149": {
        "value": 7,
        "weight": 5
      },
      "item-1150": {
        "value": 8,
        "weight": 9
      },
      "item-1151": {
        "value": 3,
        "weight": 8
      },
      "item-1152": {
        "value": 1,
        "weight": 5
      },
      "item-1153": {
        "value": 7,
        "weight": 3
      },
      "item-1154": {
        "value": 4,
        "weight": 1
      },
      "item-1155": {
        "value": 7,
        "weight": 6
      },
      "item-1156": {
        "value": 8,
        "weight": 7
      },
      "item-1157": {
        "value": 7,
        "weight": 7
      },
      "item-1158": {
        "value": 3,
        "weight": 3
      },
      "item-1159": {
        "value": 9,
        "weight": 2
      },
      "item-1160": {
        "value": 8,
        "weight": 9
      },
      "item-1161": {
        "value": 3,
        "weight": 6
      },
      "item-1162": {
        "value": 6,
        "weight": 2
      },
      "item-1163": {
        "value": 9,
        "weight": 7
      },
      "item-1164": {
        "value": 9,
        "weight": 8
      },
      "item-1165": {
        "value": 8,
        "weight": 6
      },
      "item-1166": {
        "value": 4,
        "weight": 6
      },
      "item-1167": {
        "value": 6,
        "weight": 4
      },
      "item-1168": {
        "value": 9,
        "weight": 4
      },
      "item-1169": {
        "value": 3,
        "weight": 9
      },
      "item-1170": {
        "value": 4,
        "weight": 3
      },
      "item-1171": {
        "value": 1,
        "weight": 7
      },
      "item-1172": {
        "value": 5,
        "weight": 3
      },
      "item-1173": {
        "value": 6,
        "weight": 2
      },
      "item-1174": {
        "value": 8,
        "weight": 4
      },
      "item-1175": {
        "value": 8,
        "weight": 7
      },
      "item-1176": {
        "value": 9,
        "weight": 8
      },
      "item-1177": {
        "value": 4,
        "weight": 3
      },
      "item-1178": {
        "value": 5,
        "weight": 2
      },
      "item-1179": {
        "value": 2,
        "weight": 8
      },
      "item-1180": {
        "value": 7,
        "weight": 8
      },
      "item-1181": {
        "value": 2,
        "weight": 8
      },
      "item-1182": {
        "value": 9,
        "weight": 4
      },
      "item-1183": {
        "value": 9,
        "weight": 7
      },
      "item-1184": {
        "value": 7,
        "weight": 4
      },
      "item-1185": {
        "value": 2,
        "weight": 8
      },
      "item-1186": {
        "value": 7,
        "weight": 1
      },
      "item-1187": {
        "value": 3,
        "weight": 2
      },
      "item-1188": {
        "value": 2,
        "weight": 3
      },
      "item-1189": {
        "value": 5,
        "weight": 3
      },
      "item-1190": {
        "value": 1,
        "weight": 8
      },
      "item-1191": {
        "value": 7,
        "weight": 2
      },
      "item-1192": {
        "value": 3,
        "weight": 6
      },
      "item-1193": {
        "value": 8,
        "weight": 9
      },
      "item-1194": {
        "value": 4,
        "weight": 6
      },
      "item-1195": {
        "value": 4,
        "weight": 7
      },
      "item-1196": {
        "value": 6,
        "weight": 2
      },
      "item-1197": {
        "value": 1,
        "weight": 5
      },
      "item-1198": {
        "value": 8,
        "weight": 8
      },
      "item-1199": {
        "value": 8,
        "weight": 7
      },
      "item-1200": {
        "value": 9,
        "weight": 4
      },
      "item-1201": {
        "value": 7,
        "weight": 1
      },
      "item-1202": {
        "value": 1,
        "weight": 9
      },
      "item-1203": {
        "value": 8,
        "weight": 8
      },
      "item-1204": {
        "value": 6,
        "weight": 8
      },
      "item-1205": {
        "value": 1,
        "weight": 9
      },
      "item-1206": {
        "value": 6,
        "weight": 4
      },
      "item-1207": {
        "value": 7,
        "weight": 4
      },
      "item-1208": {
        "value": 3,
        "weight": 7
      },
      "item-1209": {
        "value": 1,
        "weight": 9
      },
      "item-1210": {
        "value": 9,
        "weight": 6
      },
      "item-1211": {
        "value": 3,
        "weight": 6
      },
      "item-1212": {
        "value": 2,
        "weight": 2
      },
      "item-1213": {
        "value": 5,
        "weight": 6
      },
      "item-1214": {
        "value": 4,
        "weight": 1
      },
      "item-1215": {
        "value": 1,
        "weight": 3
      },
      "item-1216": {
        "value": 1,
        "weight": 6
      },
      "item-1217": {
        "value": 3,
        "weight": 4
      },
      "item-1218": {
        "value": 4,
        "weight": 1
      },
      "item-1219": {
        "value": 5,
        "weight": 8
      },
      "item-1220": {
        "value": 5,
        "weight": 4
      },
      "item-1221": {
        "value": 1,
        "weight": 4
      },
      "item-1222": {
        "value": 5,
        "weight": 5
      },
      "item-1223": {
        "value": 7,
        "weight": 7
      },
      "item-1224": {
        "value": 1,
        "weight": 6
      },
      "item-1225": {
        "value": 4,
        "weight": 8
      },
      "item-1226": {
        "value": 7,
        "weight": 2
      },
      "item-1227": {
        "value": 6,
        "weight": 5
      },
      "item-1228": {
        "value": 1,
        "weight": 2
      },
      "item-1229": {
        "value": 6,
        "weight": 6
      },
      "item-1230": {
        "value": 7,
        "weight": 8
      },
      "item-1231": {
        "value": 3,
        "weight": 1
      },
      "item-1232": {
        "value": 3,
        "weight": 3
      },
      "item-1233": {
        "value": 3,
        "weight": 5
      },
      "item-1234": {
        "value": 8,
        "weight": 6
      },
      "item-1235": {
        "value": 3,
        "weight": 4
      },
      "item-1236": {
        "value": 3,
        "weight": 1
      },
      "item-1237": {
        "value": 8,
        "weight": 5
      },
      "item-1238": {
        "value": 1,
        "weight": 2
      },
      "item-1239": {
        "value": 5,
        "weight": 9
      },
      "item-1240": {
        "value": 3,
        "weight": 8
      },
      "item-1241": {
        "value": 9,
        "weight": 5
      },
      "item-1242": {
        "value": 6,
        "weight": 9
      },
      "item-1243": {
        "value": 2,
        "weight": 9
      },
      "item-1244": {
        "value": 5,
        "weight": 9
      },
      "item-1245": {
        "value": 9,
        "weight": 5
      },
      "item-1246": {
        "value": 4,
        "weight": 2
      },
      "item-1247": {
        "value": 2,
        "weight": 1
      },
      "item-1248": {
        "value": 4,
        "weight": 7
      },
      "item-1249": {
        "value": 8,
        "weight": 5
      },
      "item-1250": {
        "value": 4,
        "weight": 5
      },
      "item-1251": {
        "value": 7,
        "weight": 9
      },
      "item-1252": {
        "value": 2,
        "weight": 9
      },
      "item-1253": {
        "value": 5,
        "weight": 3
      },
      "item-1254": {
        "value": 1,
        "weight": 6
      },
      "item-1255": {
        "value": 9,
        "weight": 7
      },
      "item-1256": {
        "value": 8,
        "weight": 4
      },
      "item-1257": {
        "value": 5,
        "weight": 5
      },
      "item-1258": {
        "value": 2,
        "weight": 1
      },
      "item-1259": {
        "value": 7,
        "weight": 9
      },
      "item-1260": {
        "value": 4,
        "weight": 2
      },
      "item-1261": {
        "value": 8,
        "weight": 4
      },
      "item-1262": {
        "value": 3,
        "weight": 6
      },
      "item-1263": {
        "value": 1,
        "weight": 7
      },
      "item-1264": {
        "value": 9,
        "weight": 9
      },
      "item-1265": {
        "value": 7,
        "weight": 9
      },
      "item-1266": {
        "value": 5,
        "weight": 5
      },
      "item-1267": {
        "value": 4,
        "weight": 3
      },
      "item-1268": {
        "value": 1,
        "weight": 6
      },
      "item-1269": {
        "value": 2,
        "weight": 2
      },
      "item-1270": {
        "value": 7,
        "weight": 8
      },
      "item-1271": {
        "value": 8,
        "weight": 4
      },
      "item-1272": {
        "value": 6,
        "weight": 7
      },
      "item-1273": {
        "value": 7,
        "weight": 1
      },
      "item-1274": {
        "value": 8,
        "weight": 7
      },
      "item-1275": {
        "value": 9,
        "weight": 1
      },
      "item-1276": {
        "value": 5,
        "weight": 8
      },
      "item-1277": {
        "value": 8,
        "weight": 7
      },
      "item-1278": {
        "value": 8,
        "weight": 2
      },
      "item-1279": {
        "value": 1,
        "weight": 8
      },
      "item-1280": {
        "value": 5,
        "weight": 7
      },
      "item-1281": {
        "value": 8,
        "weight": 1
      },
      "item-1282": {
        "value": 4,
        "weight": 3
      },
      "item-1283": {
        "value": 5,
        "weight": 5
      },
      "item-1284": {
        "value": 9,
        "weight": 8
      },
      "item-1285": {
        "value": 1,
        "weight": 2
      },
      "item-1286": {
        "value": 3,
        "weight": 9
      },
      "item-1287": {
        "value": 6,
        "weight": 5
      },
      "item-1288": {
        "value": 6,
        "weight": 9
      },
      "item-1289": {
        "value": 9,
        "weight": 8
      },
      "item-1290": {
        "value": 2,
        "weight": 2
      },
      "item-1291": {
        "value": 3,
        "weight": 6
      },
      "item-1292": {
        "value": 6,
        "weight": 9
      },
      "item-1293": {
        "value": 7,
        "weight": 7
      },
      "item-1294": {
        "value": 9,
        "weight": 2
      },
      "item-1295": {
        "value": 4,
        "weight": 1
      },
      "item-1296": {
        "value": 7,
        "weight": 8
      },
      "item-1297": {
        "value": 1,
        "weight": 2
      },
      "item-1298": {
        "value": 5,
        "weight": 3
      },
      "item-1299": {
        "value": 6,
        "weight": 3
      },
      "item-1300": {
        "value": 2,
        "weight": 7
      },
      "item-1301": {
        "value": 8,
        "weight": 3
      },
      "item-1302": {
        "value": 9,
        "weight": 9
      },
      "item-1303": {
        "value": 8,
        "weight": 9
      },
      "item-1304": {
        "value": 7,
        "weight": 1
      },
      "item-1305": {
        "value": 3,
        "weight": 8
      },
      "item-1306": {
        "value": 5,
        "weight": 1
      },
      "item-1307": {
        "value": 7,
        "weight": 2
      },
      "item-1308": {
        "value": 1,
        "weight": 2
      },
      "item-1309": {
        "value": 8,
        "weight": 5
      },
      "item-1310": {
        "value": 1,
        "weight": 9
      },
      "item-1311": {
        "value": 4,
        "weight": 3
      },
      "item-1312": {
        "value": 9,
        "weight": 9
      },
      "item-1313": {
        "value": 6,
        "weight": 5
      },
      "item-1314": {
        "value": 1,
        "weight": 6
      },
      "item-1315": {
        "value": 2,
        "weight": 5
      },
      "item-1316": {
        "value": 3,
        "weight": 6
      },
      "item-1317": {
        "value": 5,
        "weight": 5
      },
      "item-1318": {
        "value": 4,
        "weight": 6
      },
      "item-1319": {
        "value": 6,
        "weight": 3
      },
      "item-1320": {
        "value": 5,
        "weight": 5
      },
      "item-1321": {
        "value": 3,
        "weight": 9
      },
      "item-1322": {
        "value": 2,
        "weight": 1
      },
      "item-1323": {
        "value": 2,
        "weight": 3
      },
      "item-1324": {
        "value": 2,
        "weight": 3
      },
      "item-1325": {
        "value": 6,
        "weight": 1
      },
      "item-1326": {
        "value": 7,
        "weight": 4
      },
      "item-1327": {
        "value": 5,
        "weight": 5
      },
      "item-1328": {
        "value": 2,
        "weight": 8
      },
      "item-1329": {
        "value": 7,
        "weight": 6
      },
      "item-1330": {
        "value": 6,
        "weight": 3
      },
      "item-1331": {
        "value": 1,
        "weight": 4
      },
      "item-1332": {
        "value": 3,
        "weight": 5
      },
      "item-1333": {
        "value": 8,
        "weight": 9
      },
      "item-1334": {
        "value": 7,
        "weight": 9
      },
      "item-1335": {
        "value": 1,
        "weight": 9
      },
      "item-1336": {
        "value": 5,
        "weight": 5
      },
      "item-1337": {
        "value": 4,
        "weight": 5
      },
      "item-1338": {
        "value": 1,
        "weight": 8
      },
      "item-1339": {
        "value": 6,
        "weight": 5
      },
      "item-1340": {
        "value": 3,
        "weight": 5
      },
      "item-1341": {
        "value": 4,
        "weight": 2
      },
      "item-1342": {
        "value": 5,
        "weight": 9
      },
      "item-1343": {
        "value": 3,
        "weight": 4
      },
      "item-1344": {
        "value": 6,
        "weight": 4
      },
      "item-1345": {
        "value": 9,
        "weight": 8
      },
      "item-1346": {
        "value": 4,
        "weight": 1
      },
      "item-1347": {
        "value": 1,
        "weight": 3
      },
      "item-1348": {
        "value": 7,
        "weight": 3
      },
      "item-1349": {
        "value": 3,
        "weight": 9
      },
      "item-1350": {
        "value": 7,
        "weight": 5
      },
      "item-1351": {
        "value": 7,
        "weight": 3
      },
      "item-1352": {
        "value": 4,
        "weight": 9
      },
      "item-1353": {
        "value": 8,
        "weight": 6
      },
      "item-1354": {
        "value": 7,
        "weight": 5
      },
      "item-1355": {
        "value": 7,
        "weight": 1
      },
      "item-1356": {
        "value": 7,
        "weight": 4
      },
      "item-1357": {
        "value": 8,
        "weight": 9
      },
      "item-1358": {
        "value": 3,
        "weight": 1
      },
      "item-1359": {
        "value": 7,
        "weight": 8
      },
      "item-1360": {
        "value": 5,
        "weight": 4
      },
      "item-1361": {
        "value": 5,
        "weight": 5
      },
      "item-1362": {
        "value": 6,
        "weight": 8
      },
      "item-1363": {
        "value": 3,
        "weight": 8
      },
      "item-1364": {
        "value": 3,
        "weight": 2
      },
      "item-1365": {
        "value": 8,
        "weight": 4
      },
      "item-1366": {
        "value": 6,
        "weight": 7
      },
      "item-1367": {
        "value": 5,
        "weight": 2
      },
      "item-1368": {
        "value": 8,
        "weight": 3
      },
      "item-1369": {
        "value": 4,
        "weight": 8
      },
      "item-1370": {
        "value": 8,
        "weight": 4
      },
      "item-1371": {
        "value": 9,
        "weight": 4
      },
      "item-1372": {
        "value": 8,
        "weight": 2
      },
      "item-1373": {
        "value": 5,
        "weight": 8
      },
      "item-1374": {
        "value": 7,
        "weight": 3
      },
      "item-1375": {
        "value": 2,
        "weight": 2
      },
      "item-1376": {
        "value": 8,
        "weight": 4
      },
      "item-1377": {
        "value": 9,
        "weight": 9
      },
      "item-1378": {
        "value": 7,
        "weight": 7
      },
      "item-1379": {
        "value": 7,
        "weight": 4
      },
      "item-1380": {
        "value": 6,
        "weight": 8
      },
      "item-1381": {
        "value": 4,
        "weight": 3
      },
      "item-1382": {
        "value": 1,
        "weight": 4
      },
      "item-1383": {
        "value": 3,
        "weight": 3
      },
      "item-1384": {
        "value": 7,
        "weight": 8
      },
      "item-1385": {
        "value": 9,
        "weight": 2
      },
      "item-1386": {
        "value": 9,
        "weight": 7
      },
      "item-1387": {
        "value": 9,
        "weight": 6
      },
      "item-1388": {
        "value": 8,
        "weight": 3
      },
      "item-1389": {
        "value": 1,
        "weight": 5
      },
      "item-1390": {
        "value": 1,
        "weight": 7
      },
      "item-1391": {
        "value": 5,
        "weight": 3
      },
      "item-1392": {
        "value": 6,
        "weight": 2
      },
      "item-1393": {
        "value": 8,
        "weight": 2
      },
      "item-1394": {
        "value": 1,
        "weight": 4
      },
      "item-1395": {
        "value": 4,
        "weight": 5
      },
      "item-1396": {
        "value": 8,
        "weight": 1
      },
      "item-1397": {
        "value": 9,
        "weight": 4
      },
      "item-1398": {
        "value": 5,
        "weight": 6
      },
      "item-1399": {
        "value": 7,
        "weight": 6
      },
      "item-1400": {
        "value": 5,
        "weight": 3
      },
      "item-1401": {
        "value": 4,
        "weight": 8
      },
      "item-1402": {
        "value": 7,
        "weight": 5
      },
      "item-1403": {
        "value": 6,
        "weight": 4
      },
      "item-1404": {
        "value": 4,
        "weight": 9
      },
      "item-1405": {
        "value": 5,
        "weight": 6
      },
      "item-1406": {
        "value": 1,
        "weight": 7
      },
      "item-1407": {
        "value": 9,
        "weight": 7
      },
      "item-1408": {
        "value": 9,
        "weight": 2
      },
      "item-1409": {
        "value": 4,
        "weight": 7
      },
      "item-1410": {
        "value": 6,
        "weight": 2
      },
      "item-1411": {
        "value": 1,
        "weight": 3
      },
      "item-1412": {
        "value": 9,
        "weight": 5
      },
      "item-1413": {
        "value": 1,
        "weight": 9
      },
      "item-1414": {
        "value": 3,
        "weight": 4
      },
      "item-1415": {
        "value": 6,
        "weight": 2
      },
      "item-1416": {
        "value": 2,
        "weight": 4
      },
      "item-1417": {
        "value": 4,
        "weight": 4
      },
      "item-1418": {
        "value": 5,
        "weight": 6
      },
      "item-1419": {
        "value": 5,
        "weight": 7
      },
      "item-1420": {
        "value": 9,
        "weight": 8
      },
      "item-1421": {
        "value": 8,
        "weight": 3
      },
      "item-1422": {
        "value": 4,
        "weight": 7
      },
      "item-1423": {
        "value": 1,
        "weight": 8
      },
      "item-1424": {
        "value": 4,
        "weight": 3
      },
      "item-1425": {
        "value": 7,
        "weight": 2
      },
      "item-1426": {
        "value": 3,
        "weight": 2
      },
      "item-1427": {
        "value": 4,
        "weight": 9
      },
      "item-1428": {
        "value": 4,
        "weight": 2
      },
      "item-1429": {
        "value": 4,
        "weight": 7
      },
      "item-1430": {
        "value": 3,
        "weight": 7
      },
      "item-1431": {
        "value": 3,
        "weight": 9
      },
      "item-1432": {
        "value": 7,
        "weight": 9
      },
      "item-1433": {
        "value": 1,
        "weight": 1
      },
      "item-1434": {
        "value": 7,
        "weight": 1
      },
      "item-1435": {
        "value": 7,
        "weight": 7
      },
      "item-1436": {
        "value": 6,
        "weight": 2
      },
      "item-1437": {
        "value": 9,
        "weight": 7
      },
      "item-1438": {
        "value": 1,
        "weight": 5
      },
      "item-1439": {
        "value": 2,
        "weight": 9
      },
      "item-1440": {
        "value": 5,
        "weight": 3
      },
      "item-1441": {
        "value": 2,
        "weight": 1
      },
      "item-1442": {
        "value": 9,
        "weight": 8
      },
      "item-1443": {
        "value": 6,
        "weight": 3
      },
      "item-1444": {
        "value": 2,
        "weight": 4
      },
      "item-1445": {
        "value": 3,
        "weight": 2
      },
      "item-1446": {
        "value": 9,
        "weight": 5
      },
      "item-1447": {
        "value": 8,
        "weight": 5
      },
      "item-1448": {
        "value": 2,
        "weight": 4
      },
      "item-1449": {
        "value": 1,
        "weight": 9
      },
      "item-1450": {
        "value": 2,
        "weight": 9
      },
      "item-1451": {
        "value": 3,
        "weight": 2
      },
      "item-1452": {
        "value": 2,
        "weight": 3
      },
      "item-1453": {
        "value": 5,
        "weight": 3
      },
      "item-1454": {
        "value": 2,
        "weight": 3
      },
      "item-1455": {
        "value": 7,
        "weight": 9
      },
      "item-1456": {
        "value": 5,
        "weight": 6
      },
      "item-1457": {
        "value": 4,
        "weight": 6
      },
      "item-1458": {
        "value": 8,
        "weight": 1
      },
      "item-1459": {
        "value": 7,
        "weight": 8
      },
      "item-1460": {
        "value": 9,
        "weight": 8
      },
      "item-1461": {
        "value": 8,
        "weight": 8
      },
      "item-1462": {
        "value": 1,
        "weight": 5
      },
      "item-1463": {
        "value": 4,
        "weight": 3
      },
      "item-1464": {
        "value": 4,
        "weight": 8
      },
      "item-1465": {
        "value": 3,
        "weight": 7
      },
      "item-1466": {
        "value": 6,
        "weight": 9
      },
      "item-1467": {
        "value": 3,
        "weight": 7
      },
      "item-1468": {
        "value": 1,
        "weight": 5
      },
      "item-1469": {
        "value": 4,
        "weight": 4
      },
      "item-1470": {
        "value": 9,
        "weight": 3
      },
      "item-1471": {
        "value": 5,
        "weight": 1
      },
      "item-1472": {
        "value": 6,
        "weight": 4
      },
      "item-1473": {
        "value": 3,
        "weight": 7
      },
      "item-1474": {
        "value": 7,
        "weight": 7
      },
      "item-1475": {
        "value": 7,
        "weight": 3
      },
      "item-1476": {
        "value": 6,
        "weight": 3
      },
      "item-1477": {
        "value": 6,
        "weight": 4
      },
      "item-1478": {
        "value": 2,
        "weight": 8
      },
      "item-1479": {
        "value": 9,
        "weight": 5
      },
      "item-1480": {
        "value": 8,
        "weight": 9
      },
      "item-1481": {
        "value": 2,
        "weight": 1
      },
      "item-1482": {
        "value": 2,
        "weight": 2
      },
      "item-1483": {
        "value": 3,
        "weight": 6
      },
      "item-1484": {
        "value": 3,
        "weight": 2
      },
      "item-1485": {
        "value": 6,
        "weight": 4
      },
      "item-1486": {
        "value": 9,
        "weight": 8
      },
      "item-1487": {
        "value": 4,
        "weight": 4
      },
      "item-1488": {
        "value": 2,
        "weight": 1
      },
      "item-1489": {
        "value": 7,
        "weight": 7
      },
      "item-1490": {
        "value": 5,
        "weight": 4
      },
      "item-1491": {
        "value": 2,
        "weight": 3
      },
      "item-1492": {
        "value": 9,
        "weight": 1
      },
      "item-1493": {
        "value": 3,
        "weight": 6
      },
      "item-1494": {
        "value": 1,
        "weight": 3
      },
      "item-1495": {
        "value": 1,
        "weight": 5
      },
      "item-1496": {
        "value": 6,
        "weight": 2
      },
      "item-1497": {
        "value": 1,
        "weight": 1
      },
      "item-1498": {
        "value": 8,
        "weight": 3
      },
      "item-1499": {
        "value": 8,
        "weight": 8
      },
      "item-1500": {
        "value": 9,
        "weight": 9
      },
      "item-1501": {
        "value": 1,
        "weight": 5
      },
      "item-1502": {
        "value": 8,
        "weight": 7
      },
      "item-1503": {
        "value": 6,
        "weight": 8
      },
      "item-1504": {
        "value": 7,
        "weight": 9
      },
      "item-1505": {
        "value": 5,
        "weight": 3
      },
      "item-1506": {
        "value": 6,
        "weight": 3
      },
      "item-1507": {
        "value": 9,
        "weight": 4
      },
      "item-1508": {
        "value": 7,
        "weight": 2
      },
      "item-1509": {
        "value": 6,
        "weight": 7
      },
      "item-1510": {
        "value": 4,
        "weight": 5
      },
      "item-1511": {
        "value": 5,
        "weight": 2
      },
      "item-1512": {
        "value": 2,
        "weight": 8
      },
      "item-1513": {
        "value": 1,
        "weight": 5
      },
      "item-1514": {
        "value": 6,
        "weight": 5
      },
      "item-1515": {
        "value": 7,
        "weight": 2
      },
      "item-1516": {
        "value": 6,
        "weight": 9
      },
      "item-1517": {
        "value": 9,
        "weight": 6
      },
      "item-1518": {
        "value": 7,
        "weight": 2
      },
      "item-1519": {
        "value": 1,
        "weight": 3
      },
      "item-1520": {
        "value": 6,
        "weight": 7
      },
      "item-1521": {
        "value": 2,
        "weight": 6
      },
      "item-1522": {
        "value": 2,
        "weight": 1
      },
      "item-1523": {
        "value": 6,
        "weight": 8
      },
      "item-1524": {
        "value": 7,
        "weight": 1
      },
      "item-1525": {
        "value": 4,
        "weight": 2
      },
      "item-1526": {
        "value": 8,
        "weight": 8
      },
      "item-1527": {
        "value": 8,
        "weight": 6
      },
      "item-1528": {
        "value": 6,
        "weight": 4
      },
      "item-1529": {
        "value": 3,
        "weight": 4
      },
      "item-1530": {
        "value": 5,
        "weight": 3
      },
      "item-1531": {
        "value": 2,
        "weight": 4
      },
      "item-1532": {
        "value": 9,
        "weight": 9
      },
      "item-1533": {
        "value": 7,
        "weight": 4
      },
      "item-1534": {
        "value": 1,
        "weight": 1
      },
      "item-1535": {
        "value": 5,
        "weight": 5
      },
      "item-1536": {
        "value": 6,
        "weight": 2
      },
      "item-1537": {
        "value": 4,
        "weight": 3
      },
      "item-1538": {
        "value": 8,
        "weight": 1
      },
      "item-1539": {
        "value": 2,
        "weight": 4
      },
      "item-1540": {
        "value": 7,
        "weight": 5
      },
      "item-1541": {
        "value": 3,
        "weight": 7
      },
      "item-1542": {
        "value": 7,
        "weight": 5
      },
      "item-1543": {
        "value": 2,
        "weight": 1
      },
      "item-1544": {
        "value": 4,
        "weight": 1
      },
      "item-1545": {
        "value": 5,
        "weight": 4
      },
      "item-1546": {
        "value": 4,
        "weight": 5
      },
      "item-1547": {
        "value": 7,
        "weight": 9
      },
      "item-1548": {
        "value": 4,
        "weight": 9
      },
      "item-1549": {
        "value": 2,
        "weight": 8
      },
      "item-1550": {
        "value": 4,
        "weight": 9
      },
      "item-1551": {
        "value": 7,
        "weight": 7
      },
      "item-1552": {
        "value": 1,
        "weight": 3
      },
      "item-1553": {
        "value": 3,
        "weight": 7
      },
      "item-1554": {
        "value": 9,
        "weight": 9
      },
      "item-1555": {
        "value": 7,
        "weight": 6
      },
      "item-1556": {
        "value": 7,
        "weight": 9
      },
      "item-1557": {
        "value": 1,
        "weight": 1
      },
      "item-1558": {
        "value": 5,
        "weight": 4
      },
      "item-1559": {
        "value": 1,
        "weight": 3
      },
      "item-1560": {
        "value": 3,
        "weight": 8
      },
      "item-1561": {
        "value": 7,
        "weight": 6
      },
      "item-1562": {
        "value": 6,
        "weight": 3
      },
      "item-1563": {
        "value": 4,
        "weight": 2
      },
      "item-1564": {
        "value": 9,
        "weight": 7
      },
      "item-1565": {
        "value": 8,
        "weight": 6
      },
      "item-1566": {
        "value": 2,
        "weight": 6
      },
      "item-1567": {
        "value": 5,
        "weight": 3
      },
      "item-1568": {
        "value": 6,
        "weight": 1
      },
      "item-1569": {
        "value": 5,
        "weight": 5
      },
      "item-1570": {
        "value": 4,
        "weight": 3
      },
      "item-1571": {
        "value": 1,
        "weight": 4
      },
      "item-1572": {
        "value": 3,
        "weight": 7
      },
      "item-1573": {
        "value": 5,
        "weight": 9
      },
      "item-1574": {
        "value": 1,
        "weight": 1
      },
      "item-1575": {
        "value": 3,
        "weight": 3
      },
      "item-1576": {
        "value": 4,
        "weight": 4
      },
      "item-1577": {
        "value": 4,
        "weight": 8
      },
      "item-1578": {
        "value": 4,
        "weight": 2
      },
      "item-1579": {
        "value": 3,
        "weight": 3
      },
      "item-1580": {
        "value": 9,
        "weight": 3
      },
      "item-1581": {
        "value": 9,
        "weight": 8
      },
      "item-1582": {
        "value": 6,
        "weight": 9
      },
      "item-1583": {
        "value": 8,
        "weight": 5
      },
      "item-1584": {
        "value": 6,
        "weight": 5
      },
      "item-1585": {
        "value": 7,
        "weight": 7
      },
      "item-1586": {
        "value": 7,
        "weight": 6
      },
      "item-1587": {
        "value": 9,
        "weight": 5
      },
      "item-1588": {
        "value": 6,
        "weight": 2
      },
      "item-1589": {
        "value": 5,
        "weight": 1
      },
      "item-1590": {
        "value": 4,
        "weight": 6
      },
      "item-1591": {
        "value": 2,
        "weight": 2
      },
      "item-1592": {
        "value": 2,
        "weight": 1
      },
      "item-1593": {
        "value": 6,
        "weight": 7
      },
      "item-1594": {
        "value": 6,
        "weight": 3
      },
      "item-1595": {
        "value": 5,
        "weight": 6
      },
      "item-1596": {
        "value": 2,
        "weight": 5
      },
      "item-1597": {
        "value": 2,
        "weight": 7
      },
      "item-1598": {
        "value": 8,
        "weight": 4
      },
      "item-1599": {
        "value": 3,
        "weight": 4
      },
      "item-1600": {
        "value": 5,
        "weight": 2
      },
      "item-1601": {
        "value": 1,
        "weight": 3
      },
      "item-1602": {
        "value": 2,
        "weight": 5
      },
      "item-1603": {
        "value": 1,
        "weight": 9
      },
      "item-1604": {
        "value": 4,
        "weight": 7
      },
      "item-1605": {
        "value": 9,
        "weight": 4
      },
      "item-1606": {
        "value": 3,
        "weight": 1
      },
      "item-1607": {
        "value": 9,
        "weight": 7
      },
      "item-1608": {
        "value": 3,
        "weight": 2
      },
      "item-1609": {
        "value": 2,
        "weight": 2
      },
      "item-1610": {
        "value": 6,
        "weight": 5
      },
      "item-1611": {
        "value": 4,
        "weight": 7
      },
      "item-1612": {
        "value": 1,
        "weight": 8
      },
      "item-1613": {
        "value": 6,
        "weight": 4
      },
      "item-1614": {
        "value": 8,
        "weight": 2
      },
      "item-1615": {
        "value": 4,
        "weight": 4
      },
      "item-1616": {
        "value": 7,
        "weight": 6
      },
      "item-1617": {
        "value": 9,
        "weight": 7
      },
      "item-1618": {
        "value": 2,
        "weight": 7
      },
      "item-1619": {
        "value": 9,
        "weight": 6
      },
      "item-1620": {
        "value": 8,
        "weight": 6
      },
      "item-1621": {
        "value": 5,
        "weight": 6
      },
      "item-1622": {
        "value": 8,
        "weight": 6
      },
      "item-1623": {
        "value": 2,
        "weight": 5
      },
      "item-1624": {
        "value": 9,
        "weight": 6
      },
      "item-1625": {
        "value": 9,
        "weight": 3
      },
      "item-1626": {
        "value": 8,
        "weight": 1
      },
      "item-1627": {
        "value": 9,
        "weight": 3
      },
      "item-1628": {
        "value": 1,
        "weight": 1
      },
      "item-1629": {
        "value": 8,
        "weight": 2
      },
      "item-1630": {
        "value": 4,
        "weight": 3
      },
      "item-1631": {
        "value": 3,
        "weight": 9
      },
      "item-1632": {
        "value": 3,
        "weight": 7
      },
      "item-1633": {
        "value": 8,
        "weight": 9
      },
      "item-1634": {
        "value": 9,
        "weight": 1
      },
      "item-1635": {
        "value": 9,
        "weight": 9
      },
      "item-1636": {
        "value": 3,
        "weight": 5
      },
      "item-1637": {
        "value": 8,
        "weight": 3
      },
      "item-1638": {
        "value": 1,
        "weight": 2
      },
      "item-1639": {
        "value": 6,
        "weight": 1
      },
      "item-1640": {
        "value": 3,
        "weight": 7
      },
      "item-1641": {
        "value": 4,
        "weight": 6
      },
      "item-1642": {
        "value": 5,
        "weight": 6
      },
      "item-1643": {
        "value": 6,
        "weight": 9
      },
      "item-1644": {
        "value": 1,
        "weight": 4
      },
      "item-1645": {
        "value": 7,
        "weight": 6
      },
      "item-1646": {
        "value": 2,
        "weight": 2
      },
      "item-1647": {
        "value": 2,
        "weight": 6
      },
      "item-1648": {
        "value": 6,
        "weight": 5
      },
      "item-1649": {
        "value": 2,
        "weight": 8
      },
      "item-1650": {
        "value": 5,
        "weight": 9
      },
      "item-1651": {
        "value": 9,
        "weight": 4
      },
      "item-1652": {
        "value": 4,
        "weight": 9
      },
      "item-1653": {
        "value": 9,
        "weight": 1
      },
      "item-1654": {
        "value": 4,
        "weight": 4
      },
      "item-1655": {
        "value": 7,
        "weight": 1
      },
      "item-1656": {
        "value": 3,
        "weight": 8
      },
      "item-1657": {
        "value": 1,
        "weight": 4
      },
      "item-1658": {
        "value": 5,
        "weight": 1
      },
      "item-1659": {
        "value": 2,
        "weight": 9
      },
      "item-1660": {
        "value": 7,
        "weight": 7
      },
      "item-1661": {
        "value": 8,
        "weight": 7
      },
      "item-1662": {
        "value": 6,
        "weight": 3
      },
      "item-1663": {
        "value": 4,
        "weight": 1
      },
      "item-1664": {
        "value": 7,
        "weight": 1
      },
      "item-1665": {
        "value": 3,
        "weight": 1
      },
      "item-1666": {
        "value": 3,
        "weight": 1
      },
      "item-1667": {
        "value": 2,
        "weight": 2
      },
      "item-1668": {
        "value": 9,
        "weight": 5
      },
      "item-1669": {
        "value": 1,
        "weight": 1
      },
      "item-1670": {
        "value": 2,
        "weight": 3
      },
      "item-1671": {
        "value": 5,
        "weight": 9
      },
      "item-1672": {
        "value": 3,
        "weight": 4
      },
      "item-1673": {
        "value": 7,
        "weight": 6
      },
      "item-1674": {
        "value": 5,
        "weight": 4
      },
      "item-1675": {
        "value": 6,
        "weight": 8
      },
      "item-1676": {
        "value": 7,
        "weight": 8
      },
      "item-1677": {
        "value": 8,
        "weight": 9
      },
      "item-1678": {
        "value": 7,
        "weight": 7
      },
      "item-1679": {
        "value": 3,
        "weight": 8
      },
      "item-1680": {
        "value": 8,
        "weight": 4
      },
      "item-1681": {
        "value": 8,
        "weight": 5
      },
      "item-1682": {
        "value": 4,
        "weight": 6
      },
      "item-1683": {
        "value": 4,
        "weight": 9
      },
      "item-1684": {
        "value": 9,
        "weight": 7
      },
      "item-1685": {
        "value": 9,
        "weight": 9
      },
      "item-1686": {
        "value": 4,
        "weight": 9
      },
      "item-1687": {
        "value": 4,
        "weight": 2
      },
      "item-1688": {
        "value": 8,
        "weight": 6
      },
      "item-1689": {
        "value": 5,
        "weight": 2
      },
      "item-1690": {
        "value": 6,
        "weight": 5
      },
      "item-1691": {
        "value": 5,
        "weight": 5
      },
      "item-1692": {
        "value": 6,
        "weight": 2
      },
      "item-1693": {
        "value": 1,
        "weight": 5
      },
      "item-1694": {
        "value": 6,
        "weight": 2
      },
      "item-1695": {
        "value": 7,
        "weight": 5
      },
      "item-1696": {
        "value": 4,
        "weight": 1
      },
      "item-1697": {
        "value": 8,
        "weight": 3
      },
      "item-1698": {
        "value": 3,
        "weight": 2
      },
      "item-1699": {
        "value": 5,
        "weight": 1
      },
      "item-1700": {
        "value": 6,
        "weight": 7
      },
      "item-1701": {
        "value": 5,
        "weight": 2
      },
      "item-1702": {
        "value": 7,
        "weight": 2
      },
      "item-1703": {
        "value": 8,
        "weight": 6
      },
      "item-1704": {
        "value": 7,
        "weight": 4
      },
      "item-1705": {
        "value": 8,
        "weight": 9
      },
      "item-1706": {
        "value": 6,
        "weight": 6
      },
      "item-1707": {
        "value": 8,
        "weight": 8
      },
      "item-1708": {
        "value": 4,
        "weight": 2
      },
      "item-1709": {
        "value": 5,
        "weight": 2
      },
      "item-1710": {
        "value": 4,
        "weight": 2
      },
      "item-1711": {
        "value": 2,
        "weight": 9
      },
      "item-1712": {
        "value": 4,
        "weight": 8
      },
      "item-1713": {
        "value": 8,
        "weight": 6
      },
      "item-1714": {
        "value": 8,
        "weight": 1
      },
      "item-1715": {
        "value": 2,
        "weight": 5
      },
      "item-1716": {
        "value": 5,
        "weight": 2
      },
      "item-1717": {
        "value": 2,
        "weight": 1
      },
      "item-1718": {
        "value": 2,
        "weight": 7
      },
      "item-1719": {
        "value": 2,
        "weight": 2
      },
      "item-1720": {
        "value": 6,
        "weight": 6
      },
      "item-1721": {
        "value": 9,
        "weight": 5
      },
      "item-1722": {
        "value": 1,
        "weight": 5
      },
      "item-1723": {
        "value": 3,
        "weight": 8
      },
      "item-1724": {
        "value": 2,
        "weight": 7
      },
      "item-1725": {
        "value": 6,
        "weight": 9
      },
      "item-1726": {
        "value": 7,
        "weight": 2
      },
      "item-1727": {
        "value": 2,
        "weight": 9
      },
      "item-1728": {
        "value": 5,
        "weight": 3
      },
      "item-1729": {
        "value": 1,
        "weight": 4
      },
      "item-1730": {
        "value": 8,
        "weight": 9
      },
      "item-1731": {
        "value": 7,
        "weight": 3
      },
      "item-1732": {
        "value": 1,
        "weight": 5
      },
      "item-1733": {
        "value": 1,
        "weight": 7
      },
      "item-1734": {
        "value": 8,
        "weight": 4
      },
      "item-1735": {
        "value": 4,
        "weight": 6
      },
      "item-1736": {
        "value": 9,
        "weight": 2
      },
      "item-1737": {
        "value": 1,
        "weight": 3
      },
      "item-1738": {
        "value": 4,
        "weight": 5
      },
      "item-1739": {
        "value": 9,
        "weight": 1
      },
      "item-1740": {
        "value": 7,
        "weight": 7
      },
      "item-1741": {
        "value": 4,
        "weight": 5
      },
      "item-1742": {
        "value": 6,
        "weight": 2
      },
      "item-1743": {
        "value": 4,
        "weight": 4
      },
      "item-1744": {
        "value": 7,
        "weight": 7
      },
      "item-1745": {
        "value": 1,
        "weight": 5
      },
      "item-1746": {
        "value": 3,
        "weight": 2
      },
      "item-1747": {
        "value": 4,
        "weight": 2
      },
      "item-1748": {
        "value": 7,
        "weight": 7
      },
      "item-1749": {
        "value": 8,
        "weight": 8
      },
      "item-1750": {
        "value": 7,
        "weight": 9
      },
      "item-1751": {
        "value": 1,
        "weight": 2
      },
      "item-1752": {
        "value": 9,
        "weight": 4
      },
      "item-1753": {
        "value": 7,
        "weight": 5
      },
      "item-1754": {
        "value": 9,
        "weight": 9
      },
      "item-1755": {
        "value": 6,
        "weight": 8
      },
      "item-1756": {
        "value": 4,
        "weight": 4
      },
      "item-1757": {
        "value": 2,
        "weight": 7
      },
      "item-1758": {
        "value": 8,
        "weight": 9
      },
      "item-1759": {
        "value": 5,
        "weight": 8
      },
      "item-1760": {
        "value": 3,
        "weight": 9
      },
      "item-1761": {
        "value": 2,
        "weight": 5
      },
      "item-1762": {
        "value": 5,
        "weight": 8
      },
      "item-1763": {
        "value": 5,
        "weight": 7
      },
      "item-1764": {
        "value": 6,
        "weight": 4
      },
      "item-1765": {
        "value": 4,
        "weight": 6
      },
      "item-1766": {
        "value": 2,
        "weight": 6
      },
      "item-1767": {
        "value": 2,
        "weight": 9
      },
      "item-1768": {
        "value": 1,
        "weight": 1
      },
      "item-1769": {
        "value": 4,
        "weight": 4
      },
      "item-1770": {
        "value": 4,
        "weight": 4
      },
      "item-1771": {
        "value": 6,
        "weight": 6
      },
      "item-1772": {
        "value": 1,
        "weight": 3
      },
      "item-1773": {
        "value": 3,
        "weight": 9
      },
      "item-1774": {
        "value": 7,
        "weight": 5
      },
      "item-1775": {
        "value": 6,
        "weight": 4
      },
      "item-1776": {
        "value": 4,
        "weight": 1
      },
      "item-1777": {
        "value": 6,
        "weight": 4
      },
      "item-1778": {
        "value": 6,
        "weight": 5
      },
      "item-1779": {
        "value": 1,
        "weight": 1
      },
      "item-1780": {
        "value": 3,
        "weight": 5
      },
      "item-1781": {
        "value": 6,
        "weight": 1
      },
      "item-1782": {
        "value": 3,
        "weight": 7
      },
      "item-1783": {
        "value": 7,
        "weight": 7
      },
      "item-1784": {
        "value": 9,
        "weight": 3
      },
      "item-1785": {
        "value": 7,
        "weight": 6
      },
      "item-1786": {
        "value": 6,
        "weight": 3
      },
      "item-1787": {
        "value": 8,
        "weight": 9
      },
      "item-1788": {
        "value": 5,
        "weight": 4
      },
      "item-1789": {
        "value": 5,
        "weight": 7
      },
      "item-1790": {
        "value": 5,
        "weight": 3
      },
      "item-1791": {
        "value": 8,
        "weight": 9
      },
      "item-1792": {
        "value": 8,
        "weight": 8
      },
      "item-1793": {
        "value": 2,
        "weight": 3
      },
      "item-1794": {
        "value": 9,
        "weight": 4
      },
      "item-1795": {
        "value": 2,
        "weight": 4
      },
      "item-1796": {
        "value": 8,
        "weight": 8
      },
      "item-1797": {
        "value": 4,
        "weight": 8
      },
      "item-1798": {
        "value": 7,
        "weight": 4
      },
      "item-1799": {
        "value": 2,
        "weight": 1
      },
      "item-1800": {
        "value": 4,
        "weight": 5
      },
      "item-1801": {
        "value": 1,
        "weight": 5
      },
      "item-1802": {
        "value": 4,
        "weight": 2
      },
      "item-1803": {
        "value": 2,
        "weight": 2
      },
      "item-1804": {
        "value": 6,
        "weight": 1
      },
      "item-1805": {
        "value": 7,
        "weight": 5
      },
      "item-1806": {
        "value": 4,
        "weight": 9
      },
      "item-1807": {
        "value": 6,
        "weight": 6
      },
      "item-1808": {
        "value": 2,
        "weight": 7
      },
      "item-1809": {
        "value": 7,
        "weight": 4
      },
      "item-1810": {
        "value": 7,
        "weight": 9
      },
      "item-1811": {
        "value": 8,
        "weight": 5
      },
      "item-1812": {
        "value": 3,
        "weight": 9
      },
      "item-1813": {
        "value": 4,
        "weight": 9
      },
      "item-1814": {
        "value": 6,
        "weight": 6
      },
      "item-1815": {
        "value": 4,
        "weight": 7
      },
      "item-1816": {
        "value": 3,
        "weight": 8
      },
      "item-1817": {
        "value": 7,
        "weight": 7
      },
      "item-1818": {
        "value": 6,
        "weight": 2
      },
      "item-1819": {
        "value": 7,
        "weight": 5
      },
      "item-1820": {
        "value": 4,
        "weight": 5
      },
      "item-1821": {
        "value": 9,
        "weight": 8
      },
      "item-1822": {
        "value": 9,
        "weight": 8
      },
      "item-1823": {
        "value": 4,
        "weight": 3
      },
      "item-1824": {
        "value": 1,
        "weight": 8
      },
      "item-1825": {
        "value": 9,
        "weight": 8
      },
      "item-1826": {
        "value": 5,
        "weight": 1
      },
      "item-1827": {
        "value": 8,
        "weight": 3
      },
      "item-1828": {
        "value": 6,
        "weight": 7
      },
      "item-1829": {
        "value": 5,
        "weight": 8
      },
      "item-1830": {
        "value": 6,
        "weight": 1
      },
      "item-1831": {
        "value": 2,
        "weight": 7
      },
      "item-1832": {
        "value": 4,
        "weight": 1
      },
      "item-1833": {
        "value": 7,
        "weight": 2
      },
      "item-1834": {
        "value": 8,
        "weight": 7
      },
      "item-1835": {
        "value": 9,
        "weight": 8
      },
      "item-1836": {
        "value": 3,
        "weight": 6
      },
      "item-1837": {
        "value": 3,
        "weight": 9
      },
      "item-1838": {
        "value": 1,
        "weight": 7
      },
      "item-1839": {
        "value": 6,
        "weight": 3
      },
      "item-1840": {
        "value": 6,
        "weight": 6
      },
      "item-1841": {
        "value": 8,
        "weight": 6
      },
      "item-1842": {
        "value": 9,
        "weight": 7
      },
      "item-1843": {
        "value": 8,
        "weight": 4
      },
      "item-1844": {
        "value": 4,
        "weight": 9
      },
      "item-1845": {
        "value": 7,
        "weight": 6
      },
      "item-1846": {
        "value": 5,
        "weight": 3
      },
      "item-1847": {
        "value": 7,
        "weight": 7
      },
      "item-1848": {
        "value": 2,
        "weight": 4
      },
      "item-1849": {
        "value": 6,
        "weight": 5
      },
      "item-1850": {
        "value": 8,
        "weight": 6
      },
      "item-1851": {
        "value": 7,
        "weight": 3
      },
      "item-1852": {
        "value": 9,
        "weight": 2
      },
      "item-1853": {
        "value": 5,
        "weight": 9
      },
      "item-1854": {
        "value": 9,
        "weight": 7
      },
      "item-1855": {
        "value": 9,
        "weight": 9
      },
      "item-1856": {
        "value": 3,
        "weight": 3
      },
      "item-1857": {
        "value": 9,
        "weight": 6
      },
      "item-1858": {
        "value": 2,
        "weight": 9
      },
      "item-1859": {
        "value": 5,
        "weight": 4
      },
      "item-1860": {
        "value": 3,
        "weight": 8
      },
      "item-1861": {
        "value": 1,
        "weight": 5
      },
      "item-1862": {
        "value": 9,
        "weight": 2
      },
      "item-1863": {
        "value": 5,
        "weight": 4
      },
      "item-1864": {
        "value": 6,
        "weight": 4
      },
      "item-1865": {
        "value": 2,
        "weight": 3
      },
      "item-1866": {
        "value": 7,
        "weight": 5
      },
      "item-1867": {
        "value": 7,
        "weight": 5
      },
      "item-1868": {
        "value": 5,
        "weight": 4
      },
      "item-1869": {
        "value": 8,
        "weight": 7
      },
      "item-1870": {
        "value": 7,
        "weight": 7
      },
      "item-1871": {
        "value": 6,
        "weight": 5
      },
      "item-1872": {
        "value": 7,
        "weight": 7
      },
      "item-1873": {
        "value": 5,
        "weight": 2
      },
      "item-1874": {
        "value": 9,
        "weight": 1
      },
      "item-1875": {
        "value": 6,
        "weight": 7
      },
      "item-1876": {
        "value": 6,
        "weight": 3
      },
      "item-1877": {
        "value": 4,
        "weight": 9
      },
      "item-1878": {
        "value": 8,
        "weight": 3
      },
      "item-1879": {
        "value": 3,
        "weight": 8
      },
      "item-1880": {
        "value": 1,
        "weight": 9
      },
      "item-1881": {
        "value": 5,
        "weight": 4
      },
      "item-1882": {
        "value": 6,
        "weight": 7
      },
      "item-1883": {
        "value": 5,
        "weight": 1
      },
      "item-1884": {
        "value": 4,
        "weight": 8
      },
      "item-1885": {
        "value": 1,
        "weight": 5
      },
      "item-1886": {
        "value": 1,
        "weight": 4
      },
      "item-1887": {
        "value": 8,
        "weight": 6
      },
      "item-1888": {
        "value": 6,
        "weight": 4
      },
      "item-1889": {
        "value": 6,
        "weight": 3
      },
      "item-1890": {
        "value": 5,
        "weight": 8
      },
      "item-1891": {
        "value": 1,
        "weight": 3
      },
      "item-1892": {
        "value": 5,
        "weight": 9
      },
      "item-1893": {
        "value": 6,
        "weight": 6
      },
      "item-1894": {
        "value": 4,
        "weight": 9
      },
      "item-1895": {
        "value": 4,
        "weight": 3
      },
      "item-1896": {
        "value": 9,
        "weight": 1
      },
      "item-1897": {
        "value": 8,
        "weight": 7
      },
      "item-1898": {
        "value": 6,
        "weight": 3
      },
      "item-1899": {
        "value": 3,
        "weight": 8
      },
      "item-1900": {
        "value": 4,
        "weight": 9
      },
      "item-1901": {
        "value": 7,
        "weight": 9
      },
      "item-1902": {
        "value": 5,
        "weight": 1
      },
      "item-1903": {
        "value": 4,
        "weight": 1
      },
      "item-1904": {
        "value": 3,
        "weight": 9
      },
      "item-1905": {
        "value": 2,
        "weight": 8
      },
      "item-1906": {
        "value": 3,
        "weight": 7
      },
      "item-1907": {
        "value": 8,
        "weight": 6
      },
      "item-1908": {
        "value": 5,
        "weight": 6
      },
      "item-1909": {
        "value": 6,
        "weight": 3
      },
      "item-1910": {
        "value": 3,
        "weight": 8
      },
      "item-1911": {
        "value": 1,
        "weight": 5
      },
      "item-1912": {
        "value": 7,
        "weight": 3
      },
      "item-1913": {
        "value": 8,
        "weight": 6
      },
      "item-1914": {
        "value": 6,
        "weight": 3
      },
      "item-1915": {
        "value": 5,
        "weight": 4
      },
      "item-1916": {
        "value": 1,
        "weight": 9
      },
      "item-1917": {
        "value": 7,
        "weight": 5
      },
      "item-1918": {
        "value": 5,
        "weight": 9
      },
      "item-1919": {
        "value": 1,
        "weight": 8
      },
      "item-1920": {
        "value": 6,
        "weight": 1
      },
      "item-1921": {
        "value": 9,
        "weight": 5
      },
      "item-1922": {
        "value": 7,
        "weight": 5
      },
      "item-1923": {
        "value": 7,
        "weight": 5
      },
      "item-1924": {
        "value": 3,
        "weight": 6
      },
      "item-1925": {
        "value": 3,
        "weight": 2
      },
      "item-1926": {
        "value": 3,
        "weight": 9
      },
      "item-1927": {
        "value": 2,
        "weight": 8
      },
      "item-1928": {
        "value": 4,
        "weight": 8
      },
      "item-1929": {
        "value": 6,
        "weight": 3
      },
      "item-1930": {
        "value": 3,
        "weight": 7
      },
      "item-1931": {
        "value": 5,
        "weight": 5
      },
      "item-1932": {
        "value": 2,
        "weight": 2
      },
      "item-1933": {
        "value": 2,
        "weight": 1
      },
      "item-1934": {
        "value": 1,
        "weight": 6
      },
      "item-1935": {
        "value": 7,
        "weight": 8
      },
      "item-1936": {
        "value": 7,
        "weight": 9
      },
      "item-1937": {
        "value": 3,
        "weight": 4
      },
      "item-1938": {
        "value": 4,
        "weight": 9
      },
      "item-1939": {
        "value": 2,
        "weight": 9
      },
      "item-1940": {
        "value": 4,
        "weight": 3
      },
      "item-1941": {
        "value": 7,
        "weight": 4
      },
      "item-1942": {
        "value": 8,
        "weight": 1
      },
      "item-1943": {
        "value": 1,
        "weight": 9
      },
      "item-1944": {
        "value": 9,
        "weight": 4
      },
      "item-1945": {
        "value": 7,
        "weight": 4
      },
      "item-1946": {
        "value": 4,
        "weight": 6
      },
      "item-1947": {
        "value": 5,
        "weight": 5
      },
      "item-1948": {
        "value": 2,
        "weight": 4
      },
      "item-1949": {
        "value": 9,
        "weight": 8
      },
      "item-1950": {
        "value": 5,
        "weight": 5
      },
      "item-1951": {
        "value": 7,
        "weight": 2
      },
      "item-1952": {
        "value": 8,
        "weight": 8
      },
      "item-1953": {
        "value": 5,
        "weight": 8
      },
      "item-1954": {
        "value": 9,
        "weight": 9
      },
      "item-1955": {
        "value": 4,
        "weight": 7
      },
      "item-1956": {
        "value": 8,
        "weight": 2
      },
      "item-1957": {
        "value": 1,
        "weight": 8
      },
      "item-1958": {
        "value": 2,
        "weight": 3
      },
      "item-1959": {
        "value": 9,
        "weight": 8
      },
      "item-1960": {
        "value": 5,
        "weight": 4
      },
      "item-1961": {
        "value": 6,
        "weight": 9
      },
      "item-1962": {
        "value": 2,
        "weight": 6
      },
      "item-1963": {
        "value": 2,
        "weight": 6
      },
      "item-1964": {
        "value": 2,
        "weight": 3
      },
      "item-1965": {
        "value": 8,
        "weight": 9
      },
      "item-1966": {
        "value": 5,
        "weight": 9
      },
      "item-1967": {
        "value": 8,
        "weight": 6
      },
      "item-1968": {
        "value": 4,
        "weight": 3
      },
      "item-1969": {
        "value": 4,
        "weight": 3
      },
      "item-1970": {
        "value": 8,
        "weight": 3
      },
      "item-1971": {
        "value": 9,
        "weight": 4
      },
      "item-1972": {
        "value": 3,
        "weight": 8
      },
      "item-1973": {
        "value": 1,
        "weight": 4
      },
      "item-1974": {
        "value": 3,
        "weight": 9
      },
      "item-1975": {
        "value": 5,
        "weight": 3
      },
      "item-1976": {
        "value": 8,
        "weight": 3
      },
      "item-1977": {
        "value": 5,
        "weight": 3
      },
      "item-1978": {
        "value": 7,
        "weight": 4
      },
      "item-1979": {
        "value": 8,
        "weight": 4
      },
      "item-1980": {
        "value": 1,
        "weight": 2
      },
      "item-1981": {
        "value": 8,
        "weight": 1
      },
      "item-1982": {
        "value": 4,
        "weight": 9
      },
      "item-1983": {
        "value": 9,
        "weight": 4
      },
      "item-1984": {
        "value": 3,
        "weight": 9
      },
      "item-1985": {
        "value": 7,
        "weight": 8
      },
      "item-1986": {
        "value": 8,
        "weight": 1
      },
      "item-1987": {
        "value": 2,
        "weight": 1
      },
      "item-1988": {
        "value": 1,
        "weight": 3
      },
      "item-1989": {
        "value": 1,
        "weight": 6
      },
      "item-1990": {
        "value": 8,
        "weight": 5
      },
      "item-1991": {
        "value": 6,
        "weight": 9
      },
      "item-1992": {
        "value": 8,
        "weight": 9
      },
      "item-1993": {
        "value": 5,
        "weight": 4
      },
      "item-1994": {
        "value": 6,
        "weight": 2
      },
      "item-1995": {
        "value": 3,
        "weight": 8
      },
      "item-1996": {
        "value": 8,
        "weight": 4
      },
      "item-1997": {
        "value": 9,
        "weight": 7
      },
      "item-1998": {
        "value": 5,
        "weight": 7
      },
      "item-1999": {
        "value": 5,
        "weight": 9
      },
      "item-2000": {
        "value": 2,
        "weight": 5
      },
      "item-2001": {
        "value": 3,
        "weight": 7
      },
      "item-2002": {
        "value": 9,
        "weight": 1
      },
      "item-2003": {
        "value": 1,
        "weight": 1
      },
      "item-2004": {
        "value": 2,
        "weight": 2
      },
      "item-2005": {
        "value": 4,
        "weight": 7
      },
      "item-2006": {
        "value": 8,
        "weight": 3
      },
      "item-2007": {
        "value": 3,
        "weight": 8
      },
      "item-2008": {
        "value": 7,
        "weight": 7
      },
      "item-2009": {
        "value": 4,
        "weight": 5
      },
      "item-2010": {
        "value": 7,
        "weight": 6
      },
      "item-2011": {
        "value": 1,
        "weight": 6
      },
      "item-2012": {
        "value": 7,
        "weight": 7
      },
      "item-2013": {
        "value": 7,
        "weight": 8
      },
      "item-2014": {
        "value": 1,
        "weight": 5
      },
      "item-2015": {
        "value": 2,
        "weight": 1
      },
      "item-2016": {
        "value": 8,
        "weight": 4
      },
      "item-2017": {
        "value": 9,
        "weight": 9
      },
      "item-2018": {
        "value": 7,
        "weight": 7
      },
      "item-2019": {
        "value": 7,
        "weight": 7
      },
      "item-2020": {
        "value": 6,
        "weight": 1
      },
      "item-2021": {
        "value": 9,
        "weight": 9
      },
      "item-2022": {
        "value": 9,
        "weight": 9
      },
      "item-2023": {
        "value": 1,
        "weight": 6
      },
      "item-2024": {
        "value": 6,
        "weight": 8
      },
      "item-2025": {
        "value": 7,
        "weight": 1
      },
      "item-2026": {
        "value": 3,
        "weight": 9
      },
      "item-2027": {
        "value": 8,
        "weight": 2
      },
      "item-2028": {
        "value": 1,
        "weight": 7
      },
      "item-2029": {
        "value": 6,
        "weight": 2
      },
      "item-2030": {
        "value": 7,
        "weight": 4
      },
      "item-2031": {
        "value": 5,
        "weight": 3
      },
      "item-2032": {
        "value": 7,
        "weight": 4
      },
      "item-2033": {
        "value": 3,
        "weight": 2
      },
      "item-2034": {
        "value": 4,
        "weight": 1
      },
      "item-2035": {
        "value": 9,
        "weight": 9
      },
      "item-2036": {
        "value": 3,
        "weight": 9
      },
      "item-2037": {
        "value": 1,
        "weight": 9
      },
      "item-2038": {
        "value": 1,
        "weight": 1
      },
      "item-2039": {
        "value": 8,
        "weight": 7
      },
      "item-2040": {
        "value": 6,
        "weight": 6
      },
      "item-2041": {
        "value": 4,
        "weight": 5
      },
      "item-2042": {
        "value": 7,
        "weight": 4
      },
      "item-2043": {
        "value": 8,
        "weight": 9
      },
      "item-2044": {
        "value": 8,
        "weight": 4
      },
      "item-2045": {
        "value": 9,
        "weight": 4
      },
      "item-2046": {
        "value": 3,
        "weight": 1
      },
      "item-2047": {
        "value": 5,
        "weight": 7
      },
      "item-2048": {
        "value": 9,
        "weight": 9
      },
      "item-2049": {
        "value": 4,
        "weight": 3
      },
      "item-2050": {
        "value": 7,
        "weight": 7
      },
      "item-2051": {
        "value": 8,
        "weight": 3
      },
      "item-2052": {
        "value": 1,
        "weight": 1
      },
      "item-2053": {
        "value": 3,
        "weight": 5
      },
      "item-2054": {
        "value": 2,
        "weight": 5
      },
      "item-2055": {
        "value": 2,
        "weight": 3
      },
      "item-2056": {
        "value": 2,
        "weight": 7
      },
      "item-2057": {
        "value": 4,
        "weight": 4
      },
      "item-2058": {
        "value": 1,
        "weight": 3
      },
      "item-2059": {
        "value": 6,
        "weight": 2
      },
      "item-2060": {
        "value": 8,
        "weight": 8
      },
      "item-2061": {
        "value": 4,
        "weight": 3
      },
      "item-2062": {
        "value": 1,
        "weight": 4
      },
      "item-2063": {
        "value": 8,
        "weight": 9
      },
      "item-2064": {
        "value": 8,
        "weight": 8
      },
      "item-2065": {
        "value": 5,
        "weight": 3
      },
      "item-2066": {
        "value": 1,
        "weight": 3
      },
      "item-2067": {
        "value": 7,
        "weight": 4
      },
      "item-2068": {
        "value": 8,
        "weight": 2
      },
      "item-2069": {
        "value": 5,
        "weight": 7
      },
      "item-2070": {
        "value": 1,
        "weight": 3
      },
      "item-2071": {
        "value": 6,
        "weight": 2
      },
      "item-2072": {
        "value": 7,
        "weight": 6
      },
      "item-2073": {
        "value": 8,
        "weight": 9
      },
      "item-2074": {
        "value": 4,
        "weight": 5
      },
      "item-2075": {
        "value": 3,
        "weight": 7
      },
      "item-2076": {
        "value": 1,
        "weight": 8
      },
      "item-2077": {
        "value": 1,
        "weight": 8
      },
      "item-2078": {
        "value": 6,
        "weight": 2
      },
      "item-2079": {
        "value": 1,
        "weight": 9
      },
      "item-2080": {
        "value": 7,
        "weight": 7
      },
      "item-2081": {
        "value": 6,
        "weight": 9
      },
      "item-2082": {
        "value": 2,
        "weight": 7
      },
      "item-2083": {
        "value": 4,
        "weight": 6
      },
      "item-2084": {
        "value": 3,
        "weight": 2
      },
      "item-2085": {
        "value": 5,
        "weight": 7
      },
      "item-2086": {
        "value": 2,
        "weight": 8
      },
      "item-2087": {
        "value": 9,
        "weight": 9
      },
      "item-2088": {
        "value": 3,
        "weight": 2
      },
      "item-2089": {
        "value": 1,
        "weight": 4
      },
      "item-2090": {
        "value": 8,
        "weight": 4
      },
      "item-2091": {
        "value": 4,
        "weight": 4
      },
      "item-2092": {
        "value": 2,
        "weight": 1
      },
      "item-2093": {
        "value": 5,
        "weight": 8
      },
      "item-2094": {
        "value": 6,
        "weight": 9
      },
      "item-2095": {
        "value": 2,
        "weight": 2
      },
      "item-2096": {
        "value": 6,
        "weight": 8
      },
      "item-2097": {
        "value": 9,
        "weight": 6
      },
      "item-2098": {
        "value": 6,
        "weight": 9
      },
      "item-2099": {
        "value": 3,
        "weight": 5
      },
      "item-2100": {
        "value": 1,
        "weight": 8
      },
      "item-2101": {
        "value": 8,
        "weight": 9
      },
      "item-2102": {
        "value": 6,
        "weight": 1
      },
      "item-2103": {
        "value": 3,
        "weight": 4
      },
      "item-2104": {
        "value": 6,
        "weight": 5
      },
      "item-2105": {
        "value": 1,
        "weight": 9
      },
      "item-2106": {
        "value": 1,
        "weight": 9
      },
      "item-2107": {
        "value": 4,
        "weight": 7
      },
      "item-2108": {
        "value": 1,
        "weight": 4
      },
      "item-2109": {
        "value": 4,
        "weight": 8
      },
      "item-2110": {
        "value": 2,
        "weight": 2
      },
      "item-2111": {
        "value": 4,
        "weight": 5
      },
      "item-2112": {
        "value": 7,
        "weight": 1
      },
      "item-2113": {
        "value": 8,
        "weight": 2
      },
      "item-2114": {
        "value": 7,
        "weight": 4
      },
      "item-2115": {
        "value": 1,
        "weight": 6
      },
      "item-2116": {
        "value": 7,
        "weight": 4
      },
      "item-2117": {
        "value": 6,
        "weight": 8
      },
      "item-2118": {
        "value": 5,
        "weight": 5
      },
      "item-2119": {
        "value": 1,
        "weight": 3
      },
      "item-2120": {
        "value": 7,
        "weight": 7
      },
      "item-2121": {
        "value": 6,
        "weight": 1
      },
      "item-2122": {
        "value": 5,
        "weight": 2
      },
      "item-2123": {
        "value": 9,
        "weight": 1
      },
      "item-2124": {
        "value": 1,
        "weight": 4
      },
      "item-2125": {
        "value": 9,
        "weight": 3
      },
      "item-2126": {
        "value": 7,
        "weight": 8
      },
      "item-2127": {
        "value": 5,
        "weight": 6
      },
      "item-2128": {
        "value": 3,
        "weight": 3
      },
      "item-2129": {
        "value": 6,
        "weight": 7
      },
      "item-2130": {
        "value": 5,
        "weight": 1
      },
      "item-2131": {
        "value": 4,
        "weight": 3
      },
      "item-2132": {
        "value": 6,
        "weight": 3
      },
      "item-2133": {
        "value": 2,
        "weight": 3
      },
      "item-2134": {
        "value": 1,
        "weight": 5
      },
      "item-2135": {
        "value": 3,
        "weight": 5
      },
      "item-2136": {
        "value": 5,
        "weight": 9
      },
      "item-2137": {
        "value": 2,
        "weight": 7
      },
      "item-2138": {
        "value": 9,
        "weight": 9
      },
      "item-2139": {
        "value": 7,
        "weight": 2
      },
      "item-2140": {
        "value": 8,
        "weight": 6
      },
      "item-2141": {
        "value": 1,
        "weight": 9
      },
      "item-2142": {
        "value": 1,
        "weight": 9
      },
      "item-2143": {
        "value": 5,
        "weight": 3
      },
      "item-2144": {
        "value": 5,
        "weight": 5
      },
      "item-2145": {
        "value": 5,
        "weight": 3
      },
      "item-2146": {
        "value": 2,
        "weight": 9
      },
      "item-2147": {
        "value": 8,
        "weight": 7
      },
      "item-2148": {
        "value": 4,
        "weight": 5
      },
      "item-2149": {
        "value": 5,
        "weight": 7
      },
      "item-2150": {
        "value": 6,
        "weight": 5
      },
      "item-2151": {
        "value": 5,
        "weight": 1
      },
      "item-2152": {
        "value": 9,
        "weight": 1
      },
      "item-2153": {
        "value": 4,
        "weight": 3
      },
      "item-2154": {
        "value": 2,
        "weight": 8
      },
      "item-2155": {
        "value": 7,
        "weight": 2
      },
      "item-2156": {
        "value": 5,
        "weight": 1
      },
      "item-2157": {
        "value": 9,
        "weight": 1
      },
      "item-2158": {
        "value": 8,
        "weight": 4
      },
      "item-2159": {
        "value": 6,
        "weight": 3
      },
      "item-2160": {
        "value": 4,
        "weight": 2
      },
      "item-2161": {
        "value": 2,
        "weight": 5
      },
      "item-2162": {
        "value": 9,
        "weight": 8
      },
      "item-2163": {
        "value": 8,
        "weight": 9
      },
      "item-2164": {
        "value": 3,
        "weight": 8
      },
      "item-2165": {
        "value": 6,
        "weight": 4
      },
      "item-2166": {
        "value": 4,
        "weight": 8
      },
      "item-2167": {
        "value": 2,
        "weight": 6
      },
      "item-2168": {
        "value": 6,
        "weight": 1
      },
      "item-2169": {
        "value": 4,
        "weight": 9
      },
      "item-2170": {
        "value": 4,
        "weight": 1
      },
      "item-2171": {
        "value": 8,
        "weight": 1
      },
      "item-2172": {
        "value": 7,
        "weight": 6
      },
      "item-2173": {
        "value": 2,
        "weight": 7
      },
      "item-2174": {
        "value": 9,
        "weight": 9
      },
      "item-2175": {
        "value": 5,
        "weight": 3
      },
      "item-2176": {
        "value": 1,
        "weight": 6
      },
      "item-2177": {
        "value": 4,
        "weight": 4
      },
      "item-2178": {
        "value": 3,
        "weight": 6
      },
      "item-2179": {
        "value": 9,
        "weight": 8
      },
      "item-2180": {
        "value": 7,
        "weight": 1
      },
      "item-2181": {
        "value": 5,
        "weight": 8
      },
      "item-2182": {
        "value": 4,
        "weight": 3
      },
      "item-2183": {
        "value": 2,
        "weight": 9
      },
      "item-2184": {
        "value": 2,
        "weight": 1
      },
      "item-2185": {
        "value": 4,
        "weight": 4
      },
      "item-2186": {
        "value": 7,
        "weight": 4
      },
      "item-2187": {
        "value": 2,
        "weight": 1
      },
      "item-2188": {
        "value": 9,
        "weight": 1
      },
      "item-2189": {
        "value": 3,
        "weight": 8
      },
      "item-2190": {
        "value": 3,
        "weight": 9
      },
      "item-2191": {
        "value": 4,
        "weight": 4
      },
      "item-2192": {
        "value": 6,
        "weight": 9
      },
      "item-2193": {
        "value": 7,
        "weight": 8
      },
      "item-2194": {
        "value": 5,
        "weight": 8
      },
      "item-2195": {
        "value": 7,
        "weight": 5
      },
      "item-2196": {
        "value": 3,
        "weight": 9
      },
      "item-2197": {
        "value": 4,
        "weight": 1
      },
      "item-2198": {
        "value": 9,
        "weight": 3
      },
      "item-2199": {
        "value": 6,
        "weight": 4
      },
      "item-2200": {
        "value": 1,
        "weight": 7
      },
      "item-2201": {
        "value": 3,
        "weight": 1
      },
      "item-2202": {
        "value": 7,
        "weight": 8
      },
      "item-2203": {
        "value": 9,
        "weight": 6
      },
      "item-2204": {
        "value": 5,
        "weight": 2
      },
      "item-2205": {
        "value": 8,
        "weight": 3
      },
      "item-2206": {
        "value": 8,
        "weight": 3
      },
      "item-2207": {
        "value": 6,
        "weight": 4
      },
      "item-2208": {
        "value": 8,
        "weight": 7
      },
      "item-2209": {
        "value": 4,
        "weight": 9
      },
      "item-2210": {
        "value": 6,
        "weight": 6
      },
      "item-2211": {
        "value": 4,
        "weight": 3
      },
      "item-2212": {
        "value": 1,
        "weight": 1
      },
      "item-2213": {
        "value": 2,
        "weight": 1
      },
      "item-2214": {
        "value": 1,
        "weight": 2
      },
      "item-2215": {
        "value": 5,
        "weight": 6
      },
      "item-2216": {
        "value": 2,
        "weight": 7
      },
      "item-2217": {
        "value": 6,
        "weight": 3
      },
      "item-2218": {
        "value": 4,
        "weight": 7
      },
      "item-2219": {
        "value": 6,
        "weight": 3
      },
      "item-2220": {
        "value": 6,
        "weight": 5
      },
      "item-2221": {
        "value": 6,
        "weight": 7
      },
      "item-2222": {
        "value": 2,
        "weight": 2
      },
      "item-2223": {
        "value": 8,
        "weight": 8
      },
      "item-2224": {
        "value": 4,
        "weight": 8
      },
      "item-2225": {
        "value": 9,
        "weight": 1
      },
      "item-2226": {
        "value": 8,
        "weight": 5
      },
      "item-2227": {
        "value": 7,
        "weight": 4
      },
      "item-2228": {
        "value": 1,
        "weight": 6
      },
      "item-2229": {
        "value": 6,
        "weight": 9
      },
      "item-2230": {
        "value": 4,
        "weight": 7
      },
      "item-2231": {
        "value": 7,
        "weight": 4
      },
      "item-2232": {
        "value": 2,
        "weight": 1
      },
      "item-2233": {
        "value": 2,
        "weight": 3
      },
      "item-2234": {
        "value": 4,
        "weight": 5
      },
      "item-2235": {
        "value": 6,
        "weight": 4
      },
      "item-2236": {
        "value": 7,
        "weight": 7
      },
      "item-2237": {
        "value": 8,
        "weight": 7
      },
      "item-2238": {
        "value": 2,
        "weight": 8
      },
      "item-2239": {
        "value": 7,
        "weight": 6
      },
      "item-2240": {
        "value": 2,
        "weight": 5
      },
      "item-2241": {
        "value": 3,
        "weight": 7
      },
      "item-2242": {
        "value": 8,
        "weight": 4
      },
      "item-2243": {
        "value": 4,
        "weight": 3
      },
      "item-2244": {
        "value": 9,
        "weight": 8
      },
      "item-2245": {
        "value": 5,
        "weight": 3
      },
      "item-2246": {
        "value": 8,
        "weight": 6
      },
      "item-2247": {
        "value": 9,
        "weight": 9
      },
      "item-2248": {
        "value": 4,
        "weight": 7
      },
      "item-2249": {
        "value": 6,
        "weight": 1
      },
      "item-2250": {
        "value": 9,
        "weight": 6
      },
      "item-2251": {
        "value": 5,
        "weight": 8
      },
      "item-2252": {
        "value": 4,
        "weight": 9
      },
      "item-2253": {
        "value": 3,
        "weight": 5
      },
      "item-2254": {
        "value": 9,
        "weight": 1
      },
      "item-2255": {
        "value": 6,
        "weight": 9
      },
      "item-2256": {
        "value": 2,
        "weight": 4
      },
      "item-2257": {
        "value": 4,
        "weight": 5
      },
      "item-2258": {
        "value": 3,
        "weight": 2
      },
      "item-2259": {
        "value": 2,
        "weight": 2
      },
      "item-2260": {
        "value": 4,
        "weight": 1
      },
      "item-2261": {
        "value": 8,
        "weight": 1
      },
      "item-2262": {
        "value": 3,
        "weight": 4
      },
      "item-2263": {
        "value": 7,
        "weight": 6
      },
      "item-2264": {
        "value": 6,
        "weight": 9
      },
      "item-2265": {
        "value": 1,
        "weight": 4
      },
      "item-2266": {
        "value": 4,
        "weight": 2
      },
      "item-2267": {
        "value": 2,
        "weight": 8
      },
      "item-2268": {
        "value": 2,
        "weight": 2
      },
      "item-2269": {
        "value": 3,
        "weight": 9
      },
      "item-2270": {
        "value": 5,
        "weight": 7
      },
      "item-2271": {
        "value": 6,
        "weight": 8
      },
      "item-2272": {
        "value": 6,
        "weight": 7
      },
      "item-2273": {
        "value": 7,
        "weight": 6
      },
      "item-2274": {
        "value": 3,
        "weight": 6
      },
      "item-2275": {
        "value": 8,
        "weight": 1
      },
      "item-2276": {
        "value": 2,
        "weight": 4
      },
      "item-2277": {
        "value": 5,
        "weight": 8
      },
      "item-2278": {
        "value": 3,
        "weight": 5
      },
      "item-2279": {
        "value": 1,
        "weight": 8
      },
      "item-2280": {
        "value": 8,
        "weight": 5
      },
      "item-2281": {
        "value": 9,
        "weight": 5
      },
      "item-2282": {
        "value": 7,
        "weight": 8
      },
      "item-2283": {
        "value": 1,
        "weight": 9
      },
      "item-2284": {
        "value": 2,
        "weight": 2
      },
      "item-2285": {
        "value": 8,
        "weight": 1
      },
      "item-2286": {
        "value": 9,
        "weight": 8
      },
      "item-2287": {
        "value": 2,
        "weight": 6
      },
      "item-2288": {
        "value": 6,
        "weight": 2
      },
      "item-2289": {
        "value": 1,
        "weight": 9
      },
      "item-2290": {
        "value": 2,
        "weight": 2
      },
      "item-2291": {
        "value": 7,
        "weight": 9
      },
      "item-2292": {
        "value": 4,
        "weight": 1
      },
      "item-2293": {
        "value": 8,
        "weight": 9
      },
      "item-2294": {
        "value": 7,
        "weight": 6
      },
      "item-2295": {
        "value": 4,
        "weight": 5
      },
      "item-2296": {
        "value": 4,
        "weight": 7
      },
      "item-2297": {
        "value": 2,
        "weight": 6
      },
      "item-2298": {
        "value": 8,
        "weight": 6
      },
      "item-2299": {
        "value": 3,
        "weight": 7
      },
      "item-2300": {
        "value": 9,
        "weight": 1
      },
      "item-2301": {
        "value": 4,
        "weight": 5
      },
      "item-2302": {
        "value": 1,
        "weight": 6
      },
      "item-2303": {
        "value": 8,
        "weight": 7
      },
      "item-2304": {
        "value": 9,
        "weight": 4
      },
      "item-2305": {
        "value": 1,
        "weight": 4
      },
      "item-2306": {
        "value": 4,
        "weight": 7
      },
      "item-2307": {
        "value": 8,
        "weight": 9
      },
      "item-2308": {
        "value": 7,
        "weight": 9
      },
      "item-2309": {
        "value": 5,
        "weight": 8
      },
      "item-2310": {
        "value": 8,
        "weight": 2
      },
      "item-2311": {
        "value": 9,
        "weight": 7
      },
      "item-2312": {
        "value": 9,
        "weight": 9
      },
      "item-2313": {
        "value": 2,
        "weight": 1
      },
      "item-2314": {
        "value": 3,
        "weight": 3
      },
      "item-2315": {
        "value": 8,
        "weight": 2
      },
      "item-2316": {
        "value": 8,
        "weight": 5
      },
      "item-2317": {
        "value": 3,
        "weight": 6
      },
      "item-2318": {
        "value": 6,
        "weight": 5
      },
      "item-2319": {
        "value": 1,
        "weight": 3
      },
      "item-2320": {
        "value": 1,
        "weight": 7
      },
      "item-2321": {
        "value": 9,
        "weight": 8
      },
      "item-2322": {
        "value": 3,
        "weight": 9
      },
      "item-2323": {
        "value": 3,
        "weight": 4
      },
      "item-2324": {
        "value": 1,
        "weight": 6
      },
      "item-2325": {
        "value": 6,
        "weight": 2
      },
      "item-2326": {
        "value": 7,
        "weight": 3
      },
      "item-2327": {
        "value": 5,
        "weight": 4
      },
      "item-2328": {
        "value": 3,
        "weight": 2
      },
      "item-2329": {
        "value": 8,
        "weight": 8
      },
      "item-2330": {
        "value": 5,
        "weight": 2
      },
      "item-2331": {
        "value": 2,
        "weight": 5
      },
      "item-2332": {
        "value": 6,
        "weight": 7
      },
      "item-2333": {
        "value": 9,
        "weight": 6
      },
      "item-2334": {
        "value": 9,
        "weight": 1
      },
      "item-2335": {
        "value": 4,
        "weight": 3
      },
      "item-2336": {
        "value": 9,
        "weight": 5
      },
      "item-2337": {
        "value": 6,
        "weight": 9
      },
      "item-2338": {
        "value": 6,
        "weight": 4
      },
      "item-2339": {
        "value": 4,
        "weight": 8
      },
      "item-2340": {
        "value": 3,
        "weight": 4
      },
      "item-2341": {
        "value": 7,
        "weight": 5
      },
      "item-2342": {
        "value": 4,
        "weight": 3
      },
      "item-2343": {
        "value": 2,
        "weight": 1
      },
      "item-2344": {
        "value": 2,
        "weight": 1
      },
      "item-2345": {
        "value": 8,
        "weight": 6
      },
      "item-2346": {
        "value": 7,
        "weight": 2
      },
      "item-2347": {
        "value": 2,
        "weight": 3
      },
      "item-2348": {
        "value": 7,
        "weight": 8
      },
      "item-2349": {
        "value": 7,
        "weight": 1
      },
      "item-2350": {
        "value": 9,
        "weight": 8
      },
      "item-2351": {
        "value": 6,
        "weight": 2
      },
      "item-2352": {
        "value": 3,
        "weight": 9
      },
      "item-2353": {
        "value": 3,
        "weight": 5
      },
      "item-2354": {
        "value": 3,
        "weight": 7
      },
      "item-2355": {
        "value": 1,
        "weight": 4
      },
      "item-2356": {
        "value": 9,
        "weight": 1
      },
      "item-2357": {
        "value": 2,
        "weight": 9
      },
      "item-2358": {
        "value": 3,
        "weight": 2
      },
      "item-2359": {
        "value": 7,
        "weight": 2
      },
      "item-2360": {
        "value": 8,
        "weight": 9
      },
      "item-2361": {
        "value": 6,
        "weight": 6
      },
      "item-2362": {
        "value": 3,
        "weight": 6
      },
      "item-2363": {
        "value": 1,
        "weight": 2
      },
      "item-2364": {
        "value": 6,
        "weight": 1
      },
      "item-2365": {
        "value": 6,
        "weight": 8
      },
      "item-2366": {
        "value": 1,
        "weight": 8
      },
      "item-2367": {
        "value": 2,
        "weight": 7
      },
      "item-2368": {
        "value": 6,
        "weight": 5
      },
      "item-2369": {
        "value": 8,
        "weight": 3
      },
      "item-2370": {
        "value": 6,
        "weight": 7
      },
      "item-2371": {
        "value": 1,
        "weight": 7
      },
      "item-2372": {
        "value": 4,
        "weight": 2
      },
      "item-2373": {
        "value": 2,
        "weight": 9
      },
      "item-2374": {
        "value": 8,
        "weight": 7
      },
      "item-2375": {
        "value": 6,
        "weight": 5
      },
      "item-2376": {
        "value": 1,
        "weight": 2
      },
      "item-2377": {
        "value": 7,
        "weight": 3
      },
      "item-2378": {
        "value": 9,
        "weight": 4
      },
      "item-2379": {
        "value": 3,
        "weight": 7
      },
      "item-2380": {
        "value": 5,
        "weight": 6
      },
      "item-2381": {
        "value": 5,
        "weight": 3
      },
      "item-2382": {
        "value": 6,
        "weight": 9
      },
      "item-2383": {
        "value": 2,
        "weight": 1
      },
      "item-2384": {
        "value": 9,
        "weight": 2
      },
      "item-2385": {
        "value": 1,
        "weight": 1
      },
      "item-2386": {
        "value": 6,
        "weight": 7
      },
      "item-2387": {
        "value": 9,
        "weight": 2
      },
      "item-2388": {
        "value": 9,
        "weight": 4
      },
      "item-2389": {
        "value": 5,
        "weight": 7
      },
      "item-2390": {
        "value": 9,
        "weight": 3
      },
      "item-2391": {
        "value": 5,
        "weight": 4
      },
      "item-2392": {
        "value": 5,
        "weight": 8
      },
      "item-2393": {
        "value": 1,
        "weight": 8
      },
      "item-2394": {
        "value": 7,
        "weight": 3
      },
      "item-2395": {
        "value": 3,
        "weight": 4
      },
      "item-2396": {
        "value": 5,
        "weight": 1
      },
      "item-2397": {
        "value": 8,
        "weight": 7
      },
      "item-2398": {
        "value": 2,
        "weight": 2
      },
      "item-2399": {
        "value": 3,
        "weight": 3
      },
      "item-2400": {
        "value": 6,
        "weight": 6
      },
      "item-2401": {
        "value": 4,
        "weight": 9
      },
      "item-2402": {
        "value": 4,
        "weight": 4
      },
      "item-2403": {
        "value": 1,
        "weight": 3
      },
      "item-2404": {
        "value": 1,
        "weight": 2
      },
      "item-2405": {
        "value": 4,
        "weight": 4
      },
      "item-2406": {
        "value": 4,
        "weight": 8
      },
      "item-2407": {
        "value": 2,
        "weight": 9
      },
      "item-2408": {
        "value": 5,
        "weight": 2
      },
      "item-2409": {
        "value": 5,
        "weight": 4
      },
      "item-2410": {
        "value": 7,
        "weight": 5
      },
      "item-2411": {
        "value": 1,
        "weight": 8
      },
      "item-2412": {
        "value": 8,
        "weight": 7
      },
      "item-2413": {
        "value": 5,
        "weight": 9
      },
      "item-2414": {
        "value": 6,
        "weight": 5
      },
      "item-2415": {
        "value": 8,
        "weight": 5
      },
      "item-2416": {
        "value": 3,
        "weight": 2
      },
      "item-2417": {
        "value": 6,
        "weight": 4
      },
      "item-2418": {
        "value": 2,
        "weight": 1
      },
      "item-2419": {
        "value": 5,
        "weight": 3
      },
      "item-2420": {
        "value": 8,
        "weight": 9
      },
      "item-2421": {
        "value": 9,
        "weight": 9
      },
      "item-2422": {
        "value": 7,
        "weight": 3
      },
      "item-2423": {
        "value": 9,
        "weight": 9
      },
      "item-2424": {
        "value": 9,
        "weight": 4
      },
      "item-2425": {
        "value": 1,
        "weight": 4
      },
      "item-2426": {
        "value": 6,
        "weight": 9
      },
      "item-2427": {
        "value": 4,
        "weight": 2
      },
      "item-2428": {
        "value": 6,
        "weight": 8
      },
      "item-2429": {
        "value": 9,
        "weight": 2
      },
      "item-2430": {
        "value": 4,
        "weight": 1
      },
      "item-2431": {
        "value": 6,
        "weight": 7
      },
      "item-2432": {
        "value": 6,
        "weight": 8
      },
      "item-2433": {
        "value": 1,
        "weight": 2
      },
      "item-2434": {
        "value": 8,
        "weight": 1
      },
      "item-2435": {
        "value": 9,
        "weight": 1
      },
      "item-2436": {
        "value": 8,
        "weight": 4
      },
      "item-2437": {
        "value": 7,
        "weight": 7
      },
      "item-2438": {
        "value": 1,
        "weight": 9
      },
      "item-2439": {
        "value": 4,
        "weight": 6
      },
      "item-2440": {
        "value": 3,
        "weight": 2
      },
      "item-2441": {
        "value": 6,
        "weight": 6
      },
      "item-2442": {
        "value": 1,
        "weight": 4
      },
      "item-2443": {
        "value": 4,
        "weight": 4
      },
      "item-2444": {
        "value": 4,
        "weight": 9
      },
      "item-2445": {
        "value": 8,
        "weight": 1
      },
      "item-2446": {
        "value": 1,
        "weight": 8
      },
      "item-2447": {
        "value": 8,
        "weight": 3
      },
      "item-2448": {
        "value": 7,
        "weight": 8
      },
      "item-2449": {
        "value": 7,
        "weight": 7
      },
      "item-2450": {
        "value": 3,
        "weight": 7
      },
      "item-2451": {
        "value": 5,
        "weight": 2
      },
      "item-2452": {
        "value": 2,
        "weight": 2
      },
      "item-2453": {
        "value": 9,
        "weight": 4
      },
      "item-2454": {
        "value": 1,
        "weight": 2
      },
      "item-2455": {
        "value": 6,
        "weight": 3
      },
      "item-2456": {
        "value": 6,
        "weight": 8
      },
      "item-2457": {
        "value": 5,
        "weight": 4
      },
      "item-2458": {
        "value": 4,
        "weight": 9
      },
      "item-2459": {
        "value": 4,
        "weight": 2
      },
      "item-2460": {
        "value": 9,
        "weight": 9
      },
      "item-2461": {
        "value": 9,
        "weight": 9
      },
      "item-2462": {
        "value": 7,
        "weight": 2
      },
      "item-2463": {
        "value": 2,
        "weight": 1
      },
      "item-2464": {
        "value": 7,
        "weight": 2
      },
      "item-2465": {
        "value": 3,
        "weight": 8
      },
      "item-2466": {
        "value": 6,
        "weight": 4
      },
      "item-2467": {
        "value": 8,
        "weight": 4
      },
      "item-2468": {
        "value": 7,
        "weight": 4
      },
      "item-2469": {
        "value": 3,
        "weight": 8
      },
      "item-2470": {
        "value": 1,
        "weight": 2
      },
      "item-2471": {
        "value": 4,
        "weight": 3
      },
      "item-2472": {
        "value": 4,
        "weight": 6
      },
      "item-2473": {
        "value": 2,
        "weight": 7
      },
      "item-2474": {
        "value": 3,
        "weight": 4
      },
      "item-2475": {
        "value": 9,
        "weight": 5
      },
      "item-2476": {
        "value": 5,
        "weight": 2
      },
      "item-2477": {
        "value": 6,
        "weight": 4
      },
      "item-2478": {
        "value": 7,
        "weight": 6
      },
      "item-2479": {
        "value": 1,
        "weight": 1
      },
      "item-2480": {
        "value": 6,
        "weight": 3
      },
      "item-2481": {
        "value": 5,
        "weight": 3
      },
      "item-2482": {
        "value": 6,
        "weight": 8
      },
      "item-2483": {
        "value": 4,
        "weight": 9
      },
      "item-2484": {
        "value": 2,
        "weight": 5
      },
      "item-2485": {
        "value": 5,
        "weight": 5
      },
      "item-2486": {
        "value": 7,
        "weight": 2
      },
      "item-2487": {
        "value": 8,
        "weight": 7
      },
      "item-2488": {
        "value": 3,
        "weight": 1
      },
      "item-2489": {
        "value": 2,
        "weight": 3
      },
      "item-2490": {
        "value": 4,
        "weight": 8
      },
      "item-2491": {
        "value": 6,
        "weight": 2
      },
      "item-2492": {
        "value": 7,
        "weight": 1
      },
      "item-2493": {
        "value": 3,
        "weight": 4
      },
      "item-2494": {
        "value": 4,
        "weight": 3
      },
      "item-2495": {
        "value": 3,
        "weight": 8
      },
      "item-2496": {
        "value": 5,
        "weight": 8
      },
      "item-2497": {
        "value": 3,
        "weight": 1
      },
      "item-2498": {
        "value": 7,
        "weight": 7
      },
      "item-2499": {
        "value": 5,
        "weight": 3
      },
      "item-2500": {
        "value": 6,
        "weight": 5
      },
      "item-2501": {
        "value": 9,
        "weight": 3
      },
      "item-2502": {
        "value": 8,
        "weight": 5
      },
      "item-2503": {
        "value": 3,
        "weight": 7
      },
      "item-2504": {
        "value": 6,
        "weight": 3
      },
      "item-2505": {
        "value": 1,
        "weight": 5
      },
      "item-2506": {
        "value": 2,
        "weight": 4
      },
      "item-2507": {
        "value": 5,
        "weight": 2
      },
      "item-2508": {
        "value": 3,
        "weight": 3
      },
      "item-2509": {
        "value": 7,
        "weight": 7
      },
      "item-2510": {
        "value": 2,
        "weight": 7
      },
      "item-2511": {
        "value": 5,
        "weight": 9
      },
      "item-2512": {
        "value": 3,
        "weight": 5
      },
      "item-2513": {
        "value": 9,
        "weight": 8
      },
      "item-2514": {
        "value": 8,
        "weight": 8
      },
      "item-2515": {
        "value": 9,
        "weight": 4
      },
      "item-2516": {
        "value": 8,
        "weight": 2
      },
      "item-2517": {
        "value": 7,
        "weight": 9
      },
      "item-2518": {
        "value": 7,
        "weight": 3
      },
      "item-2519": {
        "value": 3,
        "weight": 6
      },
      "item-2520": {
        "value": 4,
        "weight": 3
      },
      "item-2521": {
        "value": 6,
        "weight": 8
      },
      "item-2522": {
        "value": 8,
        "weight": 8
      },
      "item-2523": {
        "value": 8,
        "weight": 8
      },
      "item-2524": {
        "value": 5,
        "weight": 2
      },
      "item-2525": {
        "value": 6,
        "weight": 1
      },
      "item-2526": {
        "value": 7,
        "weight": 8
      },
      "item-2527": {
        "value": 1,
        "weight": 5
      },
      "item-2528": {
        "value": 5,
        "weight": 4
      },
      "item-2529": {
        "value": 6,
        "weight": 4
      },
      "item-2530": {
        "value": 3,
        "weight": 6
      },
      "item-2531": {
        "value": 3,
        "weight": 7
      },
      "item-2532": {
        "value": 3,
        "weight": 7
      },
      "item-2533": {
        "value": 2,
        "weight": 9
      },
      "item-2534": {
        "value": 1,
        "weight": 4
      },
      "item-2535": {
        "value": 7,
        "weight": 4
      },
      "item-2536": {
        "value": 1,
        "weight": 4
      },
      "item-2537": {
        "value": 2,
        "weight": 1
      },
      "item-2538": {
        "value": 2,
        "weight": 5
      },
      "item-2539": {
        "value": 6,
        "weight": 8
      },
      "item-2540": {
        "value": 2,
        "weight": 4
      },
      "item-2541": {
        "value": 9,
        "weight": 4
      },
      "item-2542": {
        "value": 5,
        "weight": 8
      },
      "item-2543": {
        "value": 6,
        "weight": 8
      },
      "item-2544": {
        "value": 4,
        "weight": 9
      },
      "item-2545": {
        "value": 3,
        "weight": 4
      },
      "item-2546": {
        "value": 4,
        "weight": 7
      },
      "item-2547": {
        "value": 2,
        "weight": 4
      },
      "item-2548": {
        "value": 3,
        "weight": 7
      },
      "item-2549": {
        "value": 5,
        "weight": 1
      },
      "item-2550": {
        "value": 6,
        "weight": 8
      },
      "item-2551": {
        "value": 9,
        "weight": 1
      },
      "item-2552": {
        "value": 1,
        "weight": 2
      },
      "item-2553": {
        "value": 6,
        "weight": 8
      },
      "item-2554": {
        "value": 8,
        "weight": 6
      },
      "item-2555": {
        "value": 2,
        "weight": 3
      },
      "item-2556": {
        "value": 1,
        "weight": 2
      },
      "item-2557": {
        "value": 9,
        "weight": 7
      },
      "item-2558": {
        "value": 9,
        "weight": 9
      },
      "item-2559": {
        "value": 1,
        "weight": 2
      },
      "item-2560": {
        "value": 1,
        "weight": 8
      },
      "item-2561": {
        "value": 2,
        "weight": 4
      },
      "item-2562": {
        "value": 3,
        "weight": 1
      },
      "item-2563": {
        "value": 5,
        "weight": 7
      },
      "item-2564": {
        "value": 5,
        "weight": 5
      },
      "item-2565": {
        "value": 2,
        "weight": 3
      },
      "item-2566": {
        "value": 1,
        "weight": 8
      },
      "item-2567": {
        "value": 5,
        "weight": 2
      },
      "item-2568": {
        "value": 4,
        "weight": 5
      },
      "item-2569": {
        "value": 7,
        "weight": 6
      },
      "item-2570": {
        "value": 7,
        "weight": 2
      },
      "item-2571": {
        "value": 2,
        "weight": 1
      },
      "item-2572": {
        "value": 8,
        "weight": 8
      },
      "item-2573": {
        "value": 9,
        "weight": 5
      },
      "item-2574": {
        "value": 7,
        "weight": 3
      },
      "item-2575": {
        "value": 4,
        "weight": 6
      },
      "item-2576": {
        "value": 2,
        "weight": 1
      },
      "item-2577": {
        "value": 8,
        "weight": 6
      },
      "item-2578": {
        "value": 9,
        "weight": 5
      },
      "item-2579": {
        "value": 2,
        "weight": 3
      },
      "item-2580": {
        "value": 4,
        "weight": 2
      },
      "item-2581": {
        "value": 7,
        "weight": 8
      },
      "item-2582": {
        "value": 8,
        "weight": 1
      },
      "item-2583": {
        "value": 7,
        "weight": 3
      },
      "item-2584": {
        "value": 1,
        "weight": 9
      },
      "item-2585": {
        "value": 9,
        "weight": 6
      },
      "item-2586": {
        "value": 9,
        "weight": 7
      },
      "item-2587": {
        "value": 7,
        "weight": 4
      },
      "item-2588": {
        "value": 4,
        "weight": 9
      },
      "item-2589": {
        "value": 9,
        "weight": 6
      },
      "item-2590": {
        "value": 5,
        "weight": 4
      },
      "item-2591": {
        "value": 3,
        "weight": 6
      },
      "item-2592": {
        "value": 3,
        "weight": 2
      },
      "item-2593": {
        "value": 9,
        "weight": 1
      },
      "item-2594": {
        "value": 6,
        "weight": 2
      },
      "item-2595": {
        "value": 2,
        "weight": 5
      },
      "item-2596": {
        "value": 3,
        "weight": 5
      },
      "item-2597": {
        "value": 3,
        "weight": 6
      },
      "item-2598": {
        "value": 7,
        "weight": 2
      },
      "item-2599": {
        "value": 9,
        "weight": 3
      },
      "item-2600": {
        "value": 9,
        "weight": 2
      },
      "item-2601": {
        "value": 8,
        "weight": 2
      },
      "item-2602": {
        "value": 5,
        "weight": 1
      },
      "item-2603": {
        "value": 7,
        "weight": 2
      },
      "item-2604": {
        "value": 5,
        "weight": 4
      },
      "item-2605": {
        "value": 2,
        "weight": 4
      },
      "item-2606": {
        "value": 9,
        "weight": 3
      },
      "item-2607": {
        "value": 3,
        "weight": 9
      },
      "item-2608": {
        "value": 2,
        "weight": 6
      },
      "item-2609": {
        "value": 4,
        "weight": 6
      },
      "item-2610": {
        "value": 8,
        "weight": 9
      },
      "item-2611": {
        "value": 5,
        "weight": 9
      },
      "item-2612": {
        "value": 5,
        "weight": 2
      },
      "item-2613": {
        "value": 1,
        "weight": 8
      },
      "item-2614": {
        "value": 9,
        "weight": 5
      },
      "item-2615": {
        "value": 5,
        "weight": 2
      },
      "item-2616": {
        "value": 1,
        "weight": 4
      },
      "item-2617": {
        "value": 7,
        "weight": 1
      },
      "item-2618": {
        "value": 9,
        "weight": 5
      },
      "item-2619": {
        "value": 6,
        "weight": 3
      },
      "item-2620": {
        "value": 5,
        "weight": 2
      },
      "item-2621": {
        "value": 2,
        "weight": 8
      },
      "item-2622": {
        "value": 8,
        "weight": 4
      },
      "item-2623": {
        "value": 9,
        "weight": 3
      },
      "item-2624": {
        "value": 6,
        "weight": 1
      },
      "item-2625": {
        "value": 9,
        "weight": 3
      },
      "item-2626": {
        "value": 2,
        "weight": 7
      },
      "item-2627": {
        "value": 6,
        "weight": 6
      },
      "item-2628": {
        "value": 5,
        "weight": 2
      },
      "item-2629": {
        "value": 3,
        "weight": 7
      },
      "item-2630": {
        "value": 8,
        "weight": 5
      },
      "item-2631": {
        "value": 8,
        "weight": 5
      },
      "item-2632": {
        "value": 6,
        "weight": 2
      },
      "item-2633": {
        "value": 9,
        "weight": 1
      },
      "item-2634": {
        "value": 7,
        "weight": 9
      },
      "item-2635": {
        "value": 1,
        "weight": 2
      },
      "item-2636": {
        "value": 1,
        "weight": 4
      },
      "item-2637": {
        "value": 3,
        "weight": 2
      },
      "item-2638": {
        "value": 6,
        "weight": 1
      },
      "item-2639": {
        "value": 7,
        "weight": 5
      },
      "item-2640": {
        "value": 3,
        "weight": 8
      },
      "item-2641": {
        "value": 3,
        "weight": 2
      },
      "item-2642": {
        "value": 3,
        "weight": 6
      },
      "item-2643": {
        "value": 4,
        "weight": 2
      },
      "item-2644": {
        "value": 2,
        "weight": 4
      },
      "item-2645": {
        "value": 9,
        "weight": 1
      },
      "item-2646": {
        "value": 9,
        "weight": 7
      },
      "item-2647": {
        "value": 5,
        "weight": 3
      },
      "item-2648": {
        "value": 9,
        "weight": 7
      },
      "item-2649": {
        "value": 5,
        "weight": 2
      },
      "item-2650": {
        "value": 6,
        "weight": 2
      },
      "item-2651": {
        "value": 3,
        "weight": 4
      },
      "item-2652": {
        "value": 4,
        "weight": 6
      },
      "item-2653": {
        "value": 4,
        "weight": 1
      },
      "item-2654": {
        "value": 2,
        "weight": 1
      },
      "item-2655": {
        "value": 4,
        "weight": 7
      },
      "item-2656": {
        "value": 9,
        "weight": 9
      },
      "item-2657": {
        "value": 1,
        "weight": 2
      },
      "item-2658": {
        "value": 6,
        "weight": 8
      },
      "item-2659": {
        "value": 7,
        "weight": 2
      },
      "item-2660": {
        "value": 3,
        "weight": 9
      },
      "item-2661": {
        "value": 6,
        "weight": 7
      },
      "item-2662": {
        "value": 3,
        "weight": 6
      },
      "item-2663": {
        "value": 5,
        "weight": 7
      },
      "item-2664": {
        "value": 4,
        "weight": 7
      },
      "item-2665": {
        "value": 7,
        "weight": 5
      },
      "item-2666": {
        "value": 2,
        "weight": 3
      },
      "item-2667": {
        "value": 3,
        "weight": 7
      },
      "item-2668": {
        "value": 8,
        "weight": 3
      },
      "item-2669": {
        "value": 3,
        "weight": 3
      },
      "item-2670": {
        "value": 5,
        "weight": 5
      },
      "item-2671": {
        "value": 4,
        "weight": 1
      },
      "item-2672": {
        "value": 1,
        "weight": 6
      },
      "item-2673": {
        "value": 3,
        "weight": 1
      },
      "item-2674": {
        "value": 4,
        "weight": 4
      },
      "item-2675": {
        "value": 5,
        "weight": 6
      },
      "item-2676": {
        "value": 7,
        "weight": 5
      },
      "item-2677": {
        "value": 6,
        "weight": 1
      },
      "item-2678": {
        "value": 3,
        "weight": 1
      },
      "item-2679": {
        "value": 7,
        "weight": 1
      },
      "item-2680": {
        "value": 9,
        "weight": 9
      },
      "item-2681": {
        "value": 5,
        "weight": 7
      },
      "item-2682": {
        "value": 6,
        "weight": 2
      },
      "item-2683": {
        "value": 4,
        "weight": 7
      },
      "item-2684": {
        "value": 4,
        "weight": 4
      },
      "item-2685": {
        "value": 8,
        "weight": 5
      },
      "item-2686": {
        "value": 3,
        "weight": 7
      },
      "item-2687": {
        "value": 5,
        "weight": 6
      },
      "item-2688": {
        "value": 1,
        "weight": 1
      },
      "item-2689": {
        "value": 7,
        "weight": 6
      },
      "item-2690": {
        "value": 3,
        "weight": 6
      },
      "item-2691": {
        "value": 3,
        "weight": 5
      },
      "item-2692": {
        "value": 5,
        "weight": 1
      },
      "item-2693": {
        "value": 5,
        "weight": 1
      },
      "item-2694": {
        "value": 8,
        "weight": 9
      },
      "item-2695": {
        "value": 4,
        "weight": 1
      },
      "item-2696": {
        "value": 3,
        "weight": 3
      },
      "item-2697": {
        "value": 1,
        "weight": 4
      },
      "item-2698": {
        "value": 8,
        "weight": 6
      },
      "item-2699": {
        "value": 9,
        "weight": 2
      },
      "item-2700": {
        "value": 3,
        "weight": 5
      },
      "item-2701": {
        "value": 1,
        "weight": 6
      },
      "item-2702": {
        "value": 2,
        "weight": 1
      },
      "item-2703": {
        "value": 8,
        "weight": 7
      },
      "item-2704": {
        "value": 6,
        "weight": 6
      },
      "item-2705": {
        "value": 9,
        "weight": 6
      },
      "item-2706": {
        "value": 3,
        "weight": 9
      },
      "item-2707": {
        "value": 8,
        "weight": 5
      },
      "item-2708": {
        "value": 1,
        "weight": 5
      },
      "item-2709": {
        "value": 2,
        "weight": 1
      },
      "item-2710": {
        "value": 8,
        "weight": 4
      },
      "item-2711": {
        "value": 9,
        "weight": 6
      },
      "item-2712": {
        "value": 8,
        "weight": 5
      },
      "item-2713": {
        "value": 4,
        "weight": 1
      },
      "item-2714": {
        "value": 3,
        "weight": 9
      },
      "item-2715": {
        "value": 7,
        "weight": 6
      },
      "item-2716": {
        "value": 7,
        "weight": 5
      },
      "item-2717": {
        "value": 1,
        "weight": 8
      },
      "item-2718": {
        "value": 3,
        "weight": 3
      },
      "item-2719": {
        "value": 7,
        "weight": 8
      },
      "item-2720": {
        "value": 8,
        "weight": 1
      },
      "item-2721": {
        "value": 4,
        "weight": 5
      },
      "item-2722": {
        "value": 7,
        "weight": 6
      },
      "item-2723": {
        "value": 9,
        "weight": 2
      },
      "item-2724": {
        "value": 9,
        "weight": 1
      },
      "item-2725": {
        "value": 4,
        "weight": 4
      },
      "item-2726": {
        "value": 2,
        "weight": 2
      },
      "item-2727": {
        "value": 6,
        "weight": 3
      },
      "item-2728": {
        "value": 9,
        "weight": 7
      },
      "item-2729": {
        "value": 9,
        "weight": 5
      },
      "item-2730": {
        "value": 1,
        "weight": 5
      },
      "item-2731": {
        "value": 4,
        "weight": 4
      },
      "item-2732": {
        "value": 3,
        "weight": 7
      },
      "item-2733": {
        "value": 8,
        "weight": 8
      },
      "item-2734": {
        "value": 9,
        "weight": 9
      },
      "item-2735": {
        "value": 2,
        "weight": 9
      },
      "item-2736": {
        "value": 6,
        "weight": 5
      },
      "item-2737": {
        "value": 4,
        "weight": 7
      },
      "item-2738": {
        "value": 2,
        "weight": 8
      },
      "item-2739": {
        "value": 1,
        "weight": 6
      },
      "item-2740": {
        "value": 3,
        "weight": 6
      },
      "item-2741": {
        "value": 3,
        "weight": 6
      },
      "item-2742": {
        "value": 5,
        "weight": 6
      },
      "item-2743": {
        "value": 9,
        "weight": 8
      },
      "item-2744": {
        "value": 2,
        "weight": 5
      },
      "item-2745": {
        "value": 4,
        "weight": 3
      },
      "item-2746": {
        "value": 3,
        "weight": 6
      },
      "item-2747": {
        "value": 8,
        "weight": 1
      },
      "item-2748": {
        "value": 8,
        "weight": 9
      },
      "item-2749": {
        "value": 6,
        "weight": 6
      },
      "item-2750": {
        "value": 9,
        "weight": 9
      },
      "item-2751": {
        "value": 7,
        "weight": 9
      },
      "item-2752": {
        "value": 8,
        "weight": 1
      },
      "item-2753": {
        "value": 5,
        "weight": 4
      },
      "item-2754": {
        "value": 1,
        "weight": 1
      },
      "item-2755": {
        "value": 6,
        "weight": 6
      },
      "item-2756": {
        "value": 5,
        "weight": 6
      },
      "item-2757": {
        "value": 1,
        "weight": 4
      },
      "item-2758": {
        "value": 3,
        "weight": 5
      },
      "item-2759": {
        "value": 2,
        "weight": 8
      },
      "item-2760": {
        "value": 3,
        "weight": 4
      },
      "item-2761": {
        "value": 5,
        "weight": 4
      },
      "item-2762": {
        "value": 5,
        "weight": 8
      },
      "item-2763": {
        "value": 3,
        "weight": 9
      },
      "item-2764": {
        "value": 8,
        "weight": 7
      },
      "item-2765": {
        "value": 2,
        "weight": 4
      },
      "item-2766": {
        "value": 3,
        "weight": 7
      },
      "item-2767": {
        "value": 2,
        "weight": 6
      },
      "item-2768": {
        "value": 9,
        "weight": 5
      },
      "item-2769": {
        "value": 8,
        "weight": 1
      },
      "item-2770": {
        "value": 1,
        "weight": 5
      },
      "item-2771": {
        "value": 3,
        "weight": 2
      },
      "item-2772": {
        "value": 4,
        "weight": 4
      },
      "item-2773": {
        "value": 8,
        "weight": 5
      },
      "item-2774": {
        "value": 6,
        "weight": 7
      },
      "item-2775": {
        "value": 1,
        "weight": 4
      },
      "item-2776": {
        "value": 8,
        "weight": 5
      },
      "item-2777": {
        "value": 6,
        "weight": 9
      },
      "item-2778": {
        "value": 4,
        "weight": 5
      },
      "item-2779": {
        "value": 1,
        "weight": 2
      },
      "item-2780": {
        "value": 9,
        "weight": 9
      },
      "item-2781": {
        "value": 9,
        "weight": 9
      },
      "item-2782": {
        "value": 6,
        "weight": 7
      },
      "item-2783": {
        "value": 1,
        "weight": 2
      },
      "item-2784": {
        "value": 9,
        "weight": 8
      },
      "item-2785": {
        "value": 7,
        "weight": 4
      },
      "item-2786": {
        "value": 6,
        "weight": 1
      },
      "item-2787": {
        "value": 5,
        "weight": 7
      },
      "item-2788": {
        "value": 9,
        "weight": 6
      },
      "item-2789": {
        "value": 6,
        "weight": 3
      },
      "item-2790": {
        "value": 1,
        "weight": 3
      },
      "item-2791": {
        "value": 5,
        "weight": 8
      },
      "item-2792": {
        "value": 7,
        "weight": 3
      },
      "item-2793": {
        "value": 9,
        "weight": 6
      },
      "item-2794": {
        "value": 4,
        "weight": 8
      },
      "item-2795": {
        "value": 3,
        "weight": 5
      },
      "item-2796": {
        "value": 4,
        "weight": 1
      },
      "item-2797": {
        "value": 1,
        "weight": 4
      },
      "item-2798": {
        "value": 4,
        "weight": 1
      },
      "item-2799": {
        "value": 3,
        "weight": 3
      },
      "item-2800": {
        "value": 3,
        "weight": 1
      },
      "item-2801": {
        "value": 5,
        "weight": 4
      },
      "item-2802": {
        "value": 4,
        "weight": 7
      },
      "item-2803": {
        "value": 4,
        "weight": 7
      },
      "item-2804": {
        "value": 7,
        "weight": 2
      },
      "item-2805": {
        "value": 6,
        "weight": 6
      },
      "item-2806": {
        "value": 5,
        "weight": 9
      },
      "item-2807": {
        "value": 3,
        "weight": 9
      },
      "item-2808": {
        "value": 9,
        "weight": 4
      },
      "item-2809": {
        "value": 5,
        "weight": 5
      },
      "item-2810": {
        "value": 5,
        "weight": 2
      },
      "item-2811": {
        "value": 5,
        "weight": 7
      },
      "item-2812": {
        "value": 3,
        "weight": 9
      },
      "item-2813": {
        "value": 9,
        "weight": 7
      },
      "item-2814": {
        "value": 6,
        "weight": 7
      },
      "item-2815": {
        "value": 9,
        "weight": 9
      },
      "item-2816": {
        "value": 8,
        "weight": 3
      },
      "item-2817": {
        "value": 8,
        "weight": 3
      },
      "item-2818": {
        "value": 1,
        "weight": 7
      },
      "item-2819": {
        "value": 5,
        "weight": 5
      },
      "item-2820": {
        "value": 6,
        "weight": 5
      },
      "item-2821": {
        "value": 2,
        "weight": 6
      },
      "item-2822": {
        "value": 7,
        "weight": 1
      },
      "item-2823": {
        "value": 8,
        "weight": 9
      },
      "item-2824": {
        "value": 3,
        "weight": 2
      },
      "item-2825": {
        "value": 4,
        "weight": 5
      },
      "item-2826": {
        "value": 3,
        "weight": 7
      },
      "item-2827": {
        "value": 5,
        "weight": 6
      },
      "item-2828": {
        "value": 7,
        "weight": 4
      },
      "item-2829": {
        "value": 4,
        "weight": 3
      },
      "item-2830": {
        "value": 9,
        "weight": 8
      },
      "item-2831": {
        "value": 2,
        "weight": 7
      },
      "item-2832": {
        "value": 4,
        "weight": 7
      },
      "item-2833": {
        "value": 4,
        "weight": 5
      },
      "item-2834": {
        "value": 2,
        "weight": 5
      },
      "item-2835": {
        "value": 4,
        "weight": 2
      },
      "item-2836": {
        "value": 2,
        "weight": 8
      },
      "item-2837": {
        "value": 1,
        "weight": 1
      },
      "item-2838": {
        "value": 4,
        "weight": 9
      },
      "item-2839": {
        "value": 9,
        "weight": 8
      },
      "item-2840": {
        "value": 2,
        "weight": 8
      },
      "item-2841": {
        "value": 8,
        "weight": 5
      },
      "item-2842": {
        "value": 4,
        "weight": 4
      },
      "item-2843": {
        "value": 1,
        "weight": 1
      },
      "item-2844": {
        "value": 3,
        "weight": 8
      },
      "item-2845": {
        "value": 9,
        "weight": 1
      },
      "item-2846": {
        "value": 3,
        "weight": 2
      },
      "item-2847": {
        "value": 6,
        "weight": 7
      },
      "item-2848": {
        "value": 1,
        "weight": 8
      },
      "item-2849": {
        "value": 4,
        "weight": 7
      },
      "item-2850": {
        "value": 5,
        "weight": 6
      },
      "item-2851": {
        "value": 8,
        "weight": 6
      },
      "item-2852": {
        "value": 7,
        "weight": 3
      },
      "item-2853": {
        "value": 6,
        "weight": 9
      },
      "item-2854": {
        "value": 4,
        "weight": 1
      },
      "item-2855": {
        "value": 8,
        "weight": 8
      },
      "item-2856": {
        "value": 2,
        "weight": 3
      },
      "item-2857": {
        "value": 1,
        "weight": 9
      },
      "item-2858": {
        "value": 8,
        "weight": 3
      },
      "item-2859": {
        "value": 5,
        "weight": 5
      },
      "item-2860": {
        "value": 1,
        "weight": 6
      },
      "item-2861": {
        "value": 4,
        "weight": 5
      },
      "item-2862": {
        "value": 3,
        "weight": 9
      },
      "item-2863": {
        "value": 6,
        "weight": 3
      },
      "item-2864": {
        "value": 3,
        "weight": 3
      },
      "item-2865": {
        "value": 7,
        "weight": 5
      },
      "item-2866": {
        "value": 6,
        "weight": 2
      },
      "item-2867": {
        "value": 3,
        "weight": 2
      },
      "item-2868": {
        "value": 3,
        "weight": 1
      },
      "item-2869": {
        "value": 7,
        "weight": 9
      },
      "item-2870": {
        "value": 6,
        "weight": 4
      },
      "item-2871": {
        "value": 1,
        "weight": 4
      },
      "item-2872": {
        "value": 2,
        "weight": 4
      },
      "item-2873": {
        "value": 7,
        "weight": 6
      },
      "item-2874": {
        "value": 7,
        "weight": 5
      },
      "item-2875": {
        "value": 5,
        "weight": 2
      },
      "item-2876": {
        "value": 3,
        "weight": 7
      },
      "item-2877": {
        "value": 9,
        "weight": 5
      },
      "item-2878": {
        "value": 2,
        "weight": 1
      },
      "item-2879": {
        "value": 8,
        "weight": 1
      },
      "item-2880": {
        "value": 9,
        "weight": 3
      },
      "item-2881": {
        "value": 4,
        "weight": 2
      },
      "item-2882": {
        "value": 2,
        "weight": 4
      },
      "item-2883": {
        "value": 8,
        "weight": 3
      },
      "item-2884": {
        "value": 7,
        "weight": 7
      },
      "item-2885": {
        "value": 8,
        "weight": 3
      },
      "item-2886": {
        "value": 7,
        "weight": 7
      },
      "item-2887": {
        "value": 2,
        "weight": 3
      },
      "item-2888": {
        "value": 1,
        "weight": 6
      },
      "item-2889": {
        "value": 1,
        "weight": 1
      },
      "item-2890": {
        "value": 1,
        "weight": 1
      },
      "item-2891": {
        "value": 9,
        "weight": 3
      },
      "item-2892": {
        "value": 3,
        "weight": 8
      },
      "item-2893": {
        "value": 2,
        "weight": 4
      },
      "item-2894": {
        "value": 8,
        "weight": 9
      },
      "item-2895": {
        "value": 5,
        "weight": 2
      },
      "item-2896": {
        "value": 1,
        "weight": 6
      },
      "item-2897": {
        "value": 9,
        "weight": 5
      },
      "item-2898": {
        "value": 8,
        "weight": 6
      },
      "item-2899": {
        "value": 5,
        "weight": 7
      },
      "item-2900": {
        "value": 1,
        "weight": 6
      },
      "item-2901": {
        "value": 1,
        "weight": 2
      },
      "item-2902": {
        "value": 1,
        "weight": 2
      },
      "item-2903": {
        "value": 6,
        "weight": 1
      },
      "item-2904": {
        "value": 5,
        "weight": 2
      },
      "item-2905": {
        "value": 6,
        "weight": 5
      },
      "item-2906": {
        "value": 3,
        "weight": 6
      },
      "item-2907": {
        "value": 3,
        "weight": 4
      },
      "item-2908": {
        "value": 4,
        "weight": 3
      },
      "item-2909": {
        "value": 7,
        "weight": 5
      },
      "item-2910": {
        "value": 9,
        "weight": 2
      },
      "item-2911": {
        "value": 9,
        "weight": 9
      },
      "item-2912": {
        "value": 4,
        "weight": 8
      },
      "item-2913": {
        "value": 2,
        "weight": 9
      },
      "item-2914": {
        "value": 8,
        "weight": 5
      },
      "item-2915": {
        "value": 6,
        "weight": 3
      },
      "item-2916": {
        "value": 9,
        "weight": 6
      },
      "item-2917": {
        "value": 7,
        "weight": 9
      },
      "item-2918": {
        "value": 8,
        "weight": 9
      },
      "item-2919": {
        "value": 4,
        "weight": 5
      },
      "item-2920": {
        "value": 2,
        "weight": 7
      },
      "item-2921": {
        "value": 4,
        "weight": 9
      },
      "item-2922": {
        "value": 4,
        "weight": 1
      },
      "item-2923": {
        "value": 2,
        "weight": 4
      },
      "item-2924": {
        "value": 9,
        "weight": 4
      },
      "item-2925": {
        "value": 4,
        "weight": 4
      },
      "item-2926": {
        "value": 4,
        "weight": 8
      },
      "item-2927": {
        "value": 4,
        "weight": 9
      },
      "item-2928": {
        "value": 6,
        "weight": 7
      },
      "item-2929": {
        "value": 4,
        "weight": 3
      },
      "item-2930": {
        "value": 9,
        "weight": 8
      },
      "item-2931": {
        "value": 8,
        "weight": 8
      },
      "item-2932": {
        "value": 4,
        "weight": 9
      },
      "item-2933": {
        "value": 7,
        "weight": 8
      },
      "item-2934": {
        "value": 9,
        "weight": 5
      },
      "item-2935": {
        "value": 3,
        "weight": 9
      },
      "item-2936": {
        "value": 7,
        "weight": 3
      },
      "item-2937": {
        "value": 8,
        "weight": 1
      },
      "item-2938": {
        "value": 7,
        "weight": 2
      },
      "item-2939": {
        "value": 5,
        "weight": 2
      },
      "item-2940": {
        "value": 4,
        "weight": 5
      },
      "item-2941": {
        "value": 4,
        "weight": 8
      },
      "item-2942": {
        "value": 6,
        "weight": 1
      },
      "item-2943": {
        "value": 2,
        "weight": 5
      },
      "item-2944": {
        "value": 2,
        "weight": 4
      },
      "item-2945": {
        "value": 7,
        "weight": 7
      },
      "item-2946": {
        "value": 3,
        "weight": 1
      },
      "item-2947": {
        "value": 5,
        "weight": 5
      },
      "item-2948": {
        "value": 7,
        "weight": 6
      },
      "item-2949": {
        "value": 3,
        "weight": 4
      },
      "item-2950": {
        "value": 9,
        "weight": 8
      },
      "item-2951": {
        "value": 8,
        "weight": 5
      },
      "item-2952": {
        "value": 5,
        "weight": 6
      },
      "item-2953": {
        "value": 6,
        "weight": 4
      },
      "item-2954": {
        "value": 2,
        "weight": 8
      },
      "item-2955": {
        "value": 1,
        "weight": 9
      },
      "item-2956": {
        "value": 3,
        "weight": 8
      },
      "item-2957": {
        "value": 8,
        "weight": 9
      },
      "item-2958": {
        "value": 5,
        "weight": 2
      },
      "item-2959": {
        "value": 6,
        "weight": 2
      },
      "item-2960": {
        "value": 3,
        "weight": 9
      },
      "item-2961": {
        "value": 8,
        "weight": 5
      },
      "item-2962": {
        "value": 2,
        "weight": 1
      },
      "item-2963": {
        "value": 6,
        "weight": 7
      },
      "item-2964": {
        "value": 7,
        "weight": 5
      },
      "item-2965": {
        "value": 4,
        "weight": 5
      },
      "item-2966": {
        "value": 6,
        "weight": 9
      },
      "item-2967": {
        "value": 4,
        "weight": 8
      },
      "item-2968": {
        "value": 9,
        "weight": 4
      },
      "item-2969": {
        "value": 8,
        "weight": 4
      },
      "item-2970": {
        "value": 3,
        "weight": 2
      },
      "item-2971": {
        "value": 2,
        "weight": 1
      },
      "item-2972": {
        "value": 1,
        "weight": 8
      },
      "item-2973": {
        "value": 2,
        "weight": 4
      },
      "item-2974": {
        "value": 9,
        "weight": 2
      },
      "item-2975": {
        "value": 1,
        "weight": 4
      },
      "item-2976": {
        "value": 4,
        "weight": 4
      },
      "item-2977": {
        "value": 6,
        "weight": 6
      },
      "item-2978": {
        "value": 2,
        "weight": 8
      },
      "item-2979": {
        "value": 4,
        "weight": 3
      },
      "item-2980": {
        "value": 1,
        "weight": 9
      },
      "item-2981": {
        "value": 3,
        "weight": 2
      },
      "item-2982": {
        "value": 5,
        "weight": 6
      },
      "item-2983": {
        "value": 1,
        "weight": 8
      },
      "item-2984": {
        "value": 7,
        "weight": 1
      },
      "item-2985": {
        "value": 2,
        "weight": 2
      },
      "item-2986": {
        "value": 9,
        "weight": 5
      },
      "item-2987": {
        "value": 1,
        "weight": 9
      },
      "item-2988": {
        "value": 5,
        "weight": 5
      },
      "item-2989": {
        "value": 3,
        "weight": 5
      },
      "item-2990": {
        "value": 6,
        "weight": 4
      },
      "item-2991": {
        "value": 1,
        "weight": 6
      },
      "item-2992": {
        "value": 8,
        "weight": 2
      },
      "item-2993": {
        "value": 8,
        "weight": 6
      },
      "item-2994": {
        "value": 7,
        "weight": 9
      },
      "item-2995": {
        "value": 6,
        "weight": 6
      },
      "item-2996": {
        "value": 7,
        "weight": 2
      },
      "item-2997": {
        "value": 4,
        "weight": 1
      },
      "item-2998": {
        "value": 9,
        "weight": 8
      },
      "item-2999": {
        "value": 7,
        "weight": 1
      },
      "item-3000": {
        "value": 7,
        "weight": 5
      },
      "item-3001": {
        "value": 2,
        "weight": 3
      },
      "item-3002": {
        "value": 2,
        "weight": 1
      },
      "item-3003": {
        "value": 5,
        "weight": 3
      },
      "item-3004": {
        "value": 5,
        "weight": 4
      },
      "item-3005": {
        "value": 6,
        "weight": 4
      },
      "item-3006": {
        "value": 8,
        "weight": 9
      },
      "item-3007": {
        "value": 7,
        "weight": 3
      },
      "item-3008": {
        "value": 4,
        "weight": 1
      },
      "item-3009": {
        "value": 6,
        "weight": 7
      },
      "item-3010": {
        "value": 8,
        "weight": 4
      },
      "item-3011": {
        "value": 7,
        "weight": 5
      },
      "item-3012": {
        "value": 7,
        "weight": 4
      },
      "item-3013": {
        "value": 3,
        "weight": 8
      },
      "item-3014": {
        "value": 5,
        "weight": 1
      },
      "item-3015": {
        "value": 8,
        "weight": 9
      },
      "item-3016": {
        "value": 9,
        "weight": 2
      },
      "item-3017": {
        "value": 3,
        "weight": 7
      },
      "item-3018": {
        "value": 2,
        "weight": 6
      },
      "item-3019": {
        "value": 4,
        "weight": 5
      },
      "item-3020": {
        "value": 5,
        "weight": 6
      },
      "item-3021": {
        "value": 3,
        "weight": 7
      },
      "item-3022": {
        "value": 2,
        "weight": 6
      },
      "item-3023": {
        "value": 4,
        "weight": 8
      },
      "item-3024": {
        "value": 4,
        "weight": 1
      },
      "item-3025": {
        "value": 9,
        "weight": 8
      },
      "item-3026": {
        "value": 1,
        "weight": 2
      },
      "item-3027": {
        "value": 2,
        "weight": 7
      },
      "item-3028": {
        "value": 8,
        "weight": 5
      },
      "item-3029": {
        "value": 2,
        "weight": 9
      },
      "item-3030": {
        "value": 8,
        "weight": 5
      },
      "item-3031": {
        "value": 3,
        "weight": 8
      },
      "item-3032": {
        "value": 8,
        "weight": 3
      },
      "item-3033": {
        "value": 5,
        "weight": 6
      },
      "item-3034": {
        "value": 8,
        "weight": 3
      },
      "item-3035": {
        "value": 7,
        "weight": 2
      },
      "item-3036": {
        "value": 6,
        "weight": 7
      },
      "item-3037": {
        "value": 1,
        "weight": 7
      },
      "item-3038": {
        "value": 3,
        "weight": 3
      },
      "item-3039": {
        "value": 5,
        "weight": 1
      },
      "item-3040": {
        "value": 5,
        "weight": 1
      },
      "item-3041": {
        "value": 5,
        "weight": 3
      },
      "item-3042": {
        "value": 3,
        "weight": 3
      },
      "item-3043": {
        "value": 2,
        "weight": 6
      },
      "item-3044": {
        "value": 5,
        "weight": 6
      },
      "item-3045": {
        "value": 7,
        "weight": 7
      },
      "item-3046": {
        "value": 8,
        "weight": 1
      },
      "item-3047": {
        "value": 3,
        "weight": 8
      },
      "item-3048": {
        "value": 4,
        "weight": 6
      },
      "item-3049": {
        "value": 1,
        "weight": 8
      },
      "item-3050": {
        "value": 4,
        "weight": 5
      },
      "item-3051": {
        "value": 9,
        "weight": 1
      },
      "item-3052": {
        "value": 7,
        "weight": 5
      },
      "item-3053": {
        "value": 7,
        "weight": 3
      },
      "item-3054": {
        "value": 2,
        "weight": 5
      },
      "item-3055": {
        "value": 9,
        "weight": 6
      },
      "item-3056": {
        "value": 1,
        "weight": 4
      },
      "item-3057": {
        "value": 6,
        "weight": 3
      },
      "item-3058": {
        "value": 6,
        "weight": 6
      },
      "item-3059": {
        "value": 4,
        "weight": 8
      },
      "item-3060": {
        "value": 8,
        "weight": 7
      },
      "item-3061": {
        "value": 3,
        "weight": 6
      },
      "item-3062": {
        "value": 2,
        "weight": 3
      },
      "item-3063": {
        "value": 8,
        "weight": 5
      },
      "item-3064": {
        "value": 5,
        "weight": 7
      },
      "item-3065": {
        "value": 1,
        "weight": 3
      },
      "item-3066": {
        "value": 6,
        "weight": 2
      },
      "item-3067": {
        "value": 1,
        "weight": 4
      },
      "item-3068": {
        "value": 9,
        "weight": 3
      },
      "item-3069": {
        "value": 3,
        "weight": 9
      },
      "item-3070": {
        "value": 5,
        "weight": 5
      },
      "item-3071": {
        "value": 5,
        "weight": 7
      },
      "item-3072": {
        "value": 6,
        "weight": 1
      },
      "item-3073": {
        "value": 4,
        "weight": 5
      },
      "item-3074": {
        "value": 8,
        "weight": 4
      },
      "item-3075": {
        "value": 1,
        "weight": 5
      },
      "item-3076": {
        "value": 9,
        "weight": 8
      },
      "item-3077": {
        "value": 9,
        "weight": 3
      },
      "item-3078": {
        "value": 5,
        "weight": 3
      },
      "item-3079": {
        "value": 7,
        "weight": 3
      },
      "item-3080": {
        "value": 2,
        "weight": 2
      },
      "item-3081": {
        "value": 3,
        "weight": 2
      },
      "item-3082": {
        "value": 8,
        "weight": 1
      },
      "item-3083": {
        "value": 6,
        "weight": 9
      },
      "item-3084": {
        "value": 8,
        "weight": 8
      },
      "item-3085": {
        "value": 7,
        "weight": 4
      },
      "item-3086": {
        "value": 2,
        "weight": 8
      },
      "item-3087": {
        "value": 2,
        "weight": 1
      },
      "item-3088": {
        "value": 3,
        "weight": 7
      },
      "item-3089": {
        "value": 8,
        "weight": 3
      },
      "item-3090": {
        "value": 7,
        "weight": 8
      },
      "item-3091": {
        "value": 5,
        "weight": 5
      },
      "item-3092": {
        "value": 9,
        "weight": 9
      },
      "item-3093": {
        "value": 1,
        "weight": 6
      },
      "item-3094": {
        "value": 2,
        "weight": 4
      },
      "item-3095": {
        "value": 5,
        "weight": 6
      },
      "item-3096": {
        "value": 8,
        "weight": 7
      },
      "item-3097": {
        "value": 9,
        "weight": 2
      },
      "item-3098": {
        "value": 1,
        "weight": 4
      },
      "item-3099": {
        "value": 3,
        "weight": 9
      },
      "item-3100": {
        "value": 7,
        "weight": 3
      },
      "item-3101": {
        "value": 9,
        "weight": 7
      },
      "item-3102": {
        "value": 4,
        "weight": 9
      },
      "item-3103": {
        "value": 9,
        "weight": 8
      },
      "item-3104": {
        "value": 1,
        "weight": 2
      },
      "item-3105": {
        "value": 3,
        "weight": 1
      },
      "item-3106": {
        "value": 2,
        "weight": 4
      },
      "item-3107": {
        "value": 5,
        "weight": 6
      },
      "item-3108": {
        "value": 7,
        "weight": 8
      },
      "item-3109": {
        "value": 5,
        "weight": 4
      },
      "item-3110": {
        "value": 7,
        "weight": 5
      },
      "item-3111": {
        "value": 9,
        "weight": 1
      },
      "item-3112": {
        "value": 2,
        "weight": 1
      },
      "item-3113": {
        "value": 7,
        "weight": 2
      },
      "item-3114": {
        "value": 6,
        "weight": 2
      },
      "item-3115": {
        "value": 3,
        "weight": 9
      },
      "item-3116": {
        "value": 8,
        "weight": 7
      },
      "item-3117": {
        "value": 8,
        "weight": 8
      },
      "item-3118": {
        "value": 5,
        "weight": 3
      },
      "item-3119": {
        "value": 7,
        "weight": 8
      },
      "item-3120": {
        "value": 9,
        "weight": 2
      },
      "item-3121": {
        "value": 6,
        "weight": 5
      },
      "item-3122": {
        "value": 4,
        "weight": 1
      },
      "item-3123": {
        "value": 3,
        "weight": 7
      },
      "item-3124": {
        "value": 2,
        "weight": 4
      },
      "item-3125": {
        "value": 4,
        "weight": 5
      },
      "item-3126": {
        "value": 3,
        "weight": 3
      },
      "item-3127": {
        "value": 9,
        "weight": 6
      },
      "item-3128": {
        "value": 3,
        "weight": 3
      },
      "item-3129": {
        "value": 6,
        "weight": 3
      },
      "item-3130": {
        "value": 4,
        "weight": 4
      },
      "item-3131": {
        "value": 5,
        "weight": 1
      },
      "item-3132": {
        "value": 5,
        "weight": 2
      },
      "item-3133": {
        "value": 6,
        "weight": 9
      },
      "item-3134": {
        "value": 9,
        "weight": 5
      },
      "item-3135": {
        "value": 9,
        "weight": 4
      },
      "item-3136": {
        "value": 9,
        "weight": 1
      },
      "item-3137": {
        "value": 7,
        "weight": 3
      },
      "item-3138": {
        "value": 6,
        "weight": 2
      },
      "item-3139": {
        "value": 1,
        "weight": 8
      },
      "item-3140": {
        "value": 7,
        "weight": 8
      },
      "item-3141": {
        "value": 2,
        "weight": 5
      },
      "item-3142": {
        "value": 4,
        "weight": 4
      },
      "item-3143": {
        "value": 1,
        "weight": 2
      },
      "item-3144": {
        "value": 7,
        "weight": 8
      },
      "item-3145": {
        "value": 8,
        "weight": 5
      },
      "item-3146": {
        "value": 6,
        "weight": 8
      },
      "item-3147": {
        "value": 6,
        "weight": 2
      },
      "item-3148": {
        "value": 9,
        "weight": 1
      },
      "item-3149": {
        "value": 3,
        "weight": 3
      },
      "item-3150": {
        "value": 5,
        "weight": 5
      },
      "item-3151": {
        "value": 9,
        "weight": 4
      },
      "item-3152": {
        "value": 6,
        "weight": 1
      },
      "item-3153": {
        "value": 4,
        "weight": 7
      },
      "item-3154": {
        "value": 5,
        "weight": 7
      },
      "item-3155": {
        "value": 2,
        "weight": 1
      },
      "item-3156": {
        "value": 5,
        "weight": 8
      },
      "item-3157": {
        "value": 3,
        "weight": 2
      },
      "item-3158": {
        "value": 1,
        "weight": 7
      },
      "item-3159": {
        "value": 4,
        "weight": 7
      },
      "item-3160": {
        "value": 2,
        "weight": 2
      },
      "item-3161": {
        "value": 6,
        "weight": 8
      },
      "item-3162": {
        "value": 1,
        "weight": 8
      },
      "item-3163": {
        "value": 6,
        "weight": 7
      },
      "item-3164": {
        "value": 9,
        "weight": 9
      },
      "item-3165": {
        "value": 5,
        "weight": 6
      },
      "item-3166": {
        "value": 3,
        "weight": 3
      },
      "item-3167": {
        "value": 5,
        "weight": 2
      },
      "item-3168": {
        "value": 6,
        "weight": 6
      },
      "item-3169": {
        "value": 9,
        "weight": 1
      },
      "item-3170": {
        "value": 6,
        "weight": 2
      },
      "item-3171": {
        "value": 7,
        "weight": 8
      },
      "item-3172": {
        "value": 9,
        "weight": 5
      },
      "item-3173": {
        "value": 9,
        "weight": 5
      },
      "item-3174": {
        "value": 5,
        "weight": 4
      },
      "item-3175": {
        "value": 7,
        "weight": 8
      },
      "item-3176": {
        "value": 3,
        "weight": 6
      },
      "item-3177": {
        "value": 8,
        "weight": 1
      },
      "item-3178": {
        "value": 2,
        "weight": 6
      },
      "item-3179": {
        "value": 3,
        "weight": 3
      },
      "item-3180": {
        "value": 3,
        "weight": 1
      },
      "item-3181": {
        "value": 2,
        "weight": 4
      },
      "item-3182": {
        "value": 1,
        "weight": 7
      },
      "item-3183": {
        "value": 5,
        "weight": 6
      },
      "item-3184": {
        "value": 6,
        "weight": 8
      },
      "item-3185": {
        "value": 9,
        "weight": 6
      },
      "item-3186": {
        "value": 7,
        "weight": 3
      },
      "item-3187": {
        "value": 6,
        "weight": 8
      },
      "item-3188": {
        "value": 8,
        "weight": 2
      },
      "item-3189": {
        "value": 2,
        "weight": 8
      },
      "item-3190": {
        "value": 1,
        "weight": 3
      },
      "item-3191": {
        "value": 5,
        "weight": 7
      },
      "item-3192": {
        "value": 5,
        "weight": 1
      },
      "item-3193": {
        "value": 9,
        "weight": 4
      },
      "item-3194": {
        "value": 7,
        "weight": 1
      },
      "item-3195": {
        "value": 5,
        "weight": 6
      },
      "item-3196": {
        "value": 9,
        "weight": 1
      },
      "item-3197": {
        "value": 9,
        "weight": 8
      },
      "item-3198": {
        "value": 6,
        "weight": 1
      },
      "item-3199": {
        "value": 1,
        "weight": 3
      },
      "item-3200": {
        "value": 3,
        "weight": 7
      },
      "item-3201": {
        "value": 9,
        "weight": 9
      },
      "item-3202": {
        "value": 5,
        "weight": 9
      },
      "item-3203": {
        "value": 9,
        "weight": 8
      },
      "item-3204": {
        "value": 7,
        "weight": 5
      },
      "item-3205": {
        "value": 7,
        "weight": 3
      },
      "item-3206": {
        "value": 1,
        "weight": 7
      },
      "item-3207": {
        "value": 2,
        "weight": 9
      },
      "item-3208": {
        "value": 1,
        "weight": 5
      },
      "item-3209": {
        "value": 8,
        "weight": 5
      },
      "item-3210": {
        "value": 8,
        "weight": 2
      },
      "item-3211": {
        "value": 6,
        "weight": 4
      },
      "item-3212": {
        "value": 8,
        "weight": 2
      },
      "item-3213": {
        "value": 2,
        "weight": 1
      },
      "item-3214": {
        "value": 9,
        "weight": 8
      },
      "item-3215": {
        "value": 1,
        "weight": 1
      },
      "item-3216": {
        "value": 2,
        "weight": 5
      },
      "item-3217": {
        "value": 4,
        "weight": 4
      },
      "item-3218": {
        "value": 8,
        "weight": 3
      },
      "item-3219": {
        "value": 9,
        "weight": 4
      },
      "item-3220": {
        "value": 2,
        "weight": 6
      },
      "item-3221": {
        "value": 2,
        "weight": 6
      },
      "item-3222": {
        "value": 2,
        "weight": 6
      },
      "item-3223": {
        "value": 5,
        "weight": 4
      },
      "item-3224": {
        "value": 7,
        "weight": 3
      },
      "item-3225": {
        "value": 6,
        "weight": 6
      },
      "item-3226": {
        "value": 2,
        "weight": 3
      },
      "item-3227": {
        "value": 2,
        "weight": 3
      },
      "item-3228": {
        "value": 6,
        "weight": 3
      },
      "item-3229": {
        "value": 2,
        "weight": 3
      },
      "item-3230": {
        "value": 4,
        "weight": 8
      },
      "item-3231": {
        "value": 6,
        "weight": 1
      },
      "item-3232": {
        "value": 2,
        "weight": 4
      },
      "item-3233": {
        "value": 2,
        "weight": 4
      },
      "item-3234": {
        "value": 4,
        "weight": 6
      },
      "item-3235": {
        "value": 1,
        "weight": 8
      },
      "item-3236": {
        "value": 7,
        "weight": 6
      },
      "item-3237": {
        "value": 7,
        "weight": 6
      },
      "item-3238": {
        "value": 6,
        "weight": 8
      },
      "item-3239": {
        "value": 3,
        "weight": 9
      },
      "item-3240": {
        "value": 4,
        "weight": 2
      },
      "item-3241": {
        "value": 8,
        "weight": 4
      },
      "item-3242": {
        "value": 9,
        "weight": 2
      },
      "item-3243": {
        "value": 2,
        "weight": 1
      },
      "item-3244": {
        "value": 3,
        "weight": 9
      },
      "item-3245": {
        "value": 5,
        "weight": 7
      },
      "item-3246": {
        "value": 8,
        "weight": 8
      },
      "item-3247": {
        "value": 5,
        "weight": 1
      },
      "item-3248": {
        "value": 4,
        "weight": 8
      },
      "item-3249": {
        "value": 2,
        "weight": 5
      },
      "item-3250": {
        "value": 7,
        "weight": 8
      },
      "item-3251": {
        "value": 8,
        "weight": 6
      },
      "item-3252": {
        "value": 4,
        "weight": 4
      },
      "item-3253": {
        "value": 9,
        "weight": 5
      },
      "item-3254": {
        "value": 3,
        "weight": 1
      },
      "item-3255": {
        "value": 2,
        "weight": 4
      },
      "item-3256": {
        "value": 1,
        "weight": 9
      },
      "item-3257": {
        "value": 2,
        "weight": 3
      },
      "item-3258": {
        "value": 4,
        "weight": 8
      },
      "item-3259": {
        "value": 7,
        "weight": 7
      },
      "item-3260": {
        "value": 9,
        "weight": 7
      },
      "item-3261": {
        "value": 8,
        "weight": 6
      },
      "item-3262": {
        "value": 1,
        "weight": 5
      },
      "item-3263": {
        "value": 6,
        "weight": 3
      },
      "item-3264": {
        "value": 1,
        "weight": 3
      },
      "item-3265": {
        "value": 6,
        "weight": 1
      },
      "item-3266": {
        "value": 3,
        "weight": 2
      },
      "item-3267": {
        "value": 2,
        "weight": 9
      },
      "item-3268": {
        "value": 2,
        "weight": 5
      },
      "item-3269": {
        "value": 3,
        "weight": 5
      },
      "item-3270": {
        "value": 8,
        "weight": 2
      },
      "item-3271": {
        "value": 7,
        "weight": 9
      },
      "item-3272": {
        "value": 7,
        "weight": 3
      },
      "item-3273": {
        "value": 9,
        "weight": 1
      },
      "item-3274": {
        "value": 1,
        "weight": 3
      },
      "item-3275": {
        "value": 2,
        "weight": 8
      },
      "item-3276": {
        "value": 6,
        "weight": 1
      },
      "item-3277": {
        "value": 8,
        "weight": 1
      },
      "item-3278": {
        "value": 3,
        "weight": 6
      },
      "item-3279": {
        "value": 9,
        "weight": 9
      },
      "item-3280": {
        "value": 7,
        "weight": 1
      },
      "item-3281": {
        "value": 7,
        "weight": 5
      },
      "item-3282": {
        "value": 6,
        "weight": 6
      },
      "item-3283": {
        "value": 5,
        "weight": 9
      },
      "item-3284": {
        "value": 4,
        "weight": 1
      },
      "item-3285": {
        "value": 1,
        "weight": 3
      },
      "item-3286": {
        "value": 5,
        "weight": 7
      },
      "item-3287": {
        "value": 8,
        "weight": 4
      },
      "item-3288": {
        "value": 4,
        "weight": 5
      },
      "item-3289": {
        "value": 9,
        "weight": 7
      },
      "item-3290": {
        "value": 8,
        "weight": 5
      },
      "item-3291": {
        "value": 5,
        "weight": 6
      },
      "item-3292": {
        "value": 8,
        "weight": 9
      },
      "item-3293": {
        "value": 1,
        "weight": 5
      },
      "item-3294": {
        "value": 3,
        "weight": 6
      },
      "item-3295": {
        "value": 7,
        "weight": 6
      },
      "item-3296": {
        "value": 7,
        "weight": 1
      },
      "item-3297": {
        "value": 8,
        "weight": 2
      },
      "item-3298": {
        "value": 9,
        "weight": 2
      },
      "item-3299": {
        "value": 2,
        "weight": 6
      },
      "item-3300": {
        "value": 8,
        "weight": 7
      },
      "item-3301": {
        "value": 1,
        "weight": 7
      },
      "item-3302": {
        "value": 4,
        "weight": 5
      },
      "item-3303": {
        "value": 1,
        "weight": 5
      },
      "item-3304": {
        "value": 5,
        "weight": 3
      },
      "item-3305": {
        "value": 2,
        "weight": 1
      },
      "item-3306": {
        "value": 1,
        "weight": 2
      },
      "item-3307": {
        "value": 3,
        "weight": 2
      },
      "item-3308": {
        "value": 3,
        "weight": 3
      },
      "item-3309": {
        "value": 9,
        "weight": 2
      },
      "item-3310": {
        "value": 5,
        "weight": 2
      },
      "item-3311": {
        "value": 6,
        "weight": 9
      },
      "item-3312": {
        "value": 4,
        "weight": 6
      },
      "item-3313": {
        "value": 2,
        "weight": 3
      },
      "item-3314": {
        "value": 5,
        "weight": 4
      },
      "item-3315": {
        "value": 4,
        "weight": 8
      },
      "item-3316": {
        "value": 1,
        "weight": 5
      },
      "item-3317": {
        "value": 6,
        "weight": 6
      },
      "item-3318": {
        "value": 1,
        "weight": 8
      },
      "item-3319": {
        "value": 7,
        "weight": 8
      },
      "item-3320": {
        "value": 3,
        "weight": 2
      },
      "item-3321": {
        "value": 1,
        "weight": 4
      },
      "item-3322": {
        "value": 6,
        "weight": 3
      },
      "item-3323": {
        "value": 6,
        "weight": 3
      },
      "item-3324": {
        "value": 1,
        "weight": 7
      },
      "item-3325": {
        "value": 6,
        "weight": 9
      },
      "item-3326": {
        "value": 4,
        "weight": 7
      },
      "item-3327": {
        "value": 7,
        "weight": 1
      },
      "item-3328": {
        "value": 6,
        "weight": 1
      },
      "item-3329": {
        "value": 1,
        "weight": 8
      },
      "item-3330": {
        "value": 8,
        "weight": 3
      },
      "item-3331": {
        "value": 5,
        "weight": 2
      },
      "item-3332": {
        "value": 1,
        "weight": 2
      },
      "item-3333": {
        "value": 7,
        "weight": 5
      },
      "item-3334": {
        "value": 2,
        "weight": 7
      },
      "item-3335": {
        "value": 9,
        "weight": 1
      },
      "item-3336": {
        "value": 5,
        "weight": 4
      },
      "item-3337": {
        "value": 8,
        "weight": 9
      },
      "item-3338": {
        "value": 3,
        "weight": 9
      },
      "item-3339": {
        "value": 1,
        "weight": 3
      },
      "item-3340": {
        "value": 5,
        "weight": 7
      },
      "item-3341": {
        "value": 9,
        "weight": 6
      },
      "item-3342": {
        "value": 5,
        "weight": 1
      },
      "item-3343": {
        "value": 4,
        "weight": 2
      },
      "item-3344": {
        "value": 6,
        "weight": 1
      },
      "item-3345": {
        "value": 3,
        "weight": 3
      },
      "item-3346": {
        "value": 5,
        "weight": 1
      },
      "item-3347": {
        "value": 4,
        "weight": 6
      },
      "item-3348": {
        "value": 4,
        "weight": 2
      },
      "item-3349": {
        "value": 2,
        "weight": 9
      },
      "item-3350": {
        "value": 6,
        "weight": 7
      },
      "item-3351": {
        "value": 9,
        "weight": 7
      },
      "item-3352": {
        "value": 5,
        "weight": 1
      },
      "item-3353": {
        "value": 7,
        "weight": 9
      },
      "item-3354": {
        "value": 8,
        "weight": 7
      },
      "item-3355": {
        "value": 3,
        "weight": 4
      },
      "item-3356": {
        "value": 6,
        "weight": 5
      },
      "item-3357": {
        "value": 8,
        "weight": 8
      },
      "item-3358": {
        "value": 9,
        "weight": 7
      },
      "item-3359": {
        "value": 4,
        "weight": 8
      },
      "item-3360": {
        "value": 7,
        "weight": 1
      },
      "item-3361": {
        "value": 8,
        "weight": 8
      },
      "item-3362": {
        "value": 7,
        "weight": 5
      },
      "item-3363": {
        "value": 7,
        "weight": 6
      },
      "item-3364": {
        "value": 8,
        "weight": 7
      },
      "item-3365": {
        "value": 2,
        "weight": 5
      },
      "item-3366": {
        "value": 8,
        "weight": 4
      },
      "item-3367": {
        "value": 8,
        "weight": 5
      },
      "item-3368": {
        "value": 8,
        "weight": 3
      },
      "item-3369": {
        "value": 8,
        "weight": 2
      },
      "item-3370": {
        "value": 9,
        "weight": 7
      },
      "item-3371": {
        "value": 5,
        "weight": 2
      },
      "item-3372": {
        "value": 4,
        "weight": 7
      },
      "item-3373": {
        "value": 8,
        "weight": 3
      },
      "item-3374": {
        "value": 3,
        "weight": 1
      },
      "item-3375": {
        "value": 8,
        "weight": 9
      },
      "item-3376": {
        "value": 5,
        "weight": 1
      },
      "item-3377": {
        "value": 6,
        "weight": 7
      },
      "item-3378": {
        "value": 6,
        "weight": 8
      },
      "item-3379": {
        "value": 4,
        "weight": 9
      },
      "item-3380": {
        "value": 2,
        "weight": 3
      },
      "item-3381": {
        "value": 2,
        "weight": 9
      },
      "item-3382": {
        "value": 1,
        "weight": 9
      },
      "item-3383": {
        "value": 1,
        "weight": 6
      },
      "item-3384": {
        "value": 3,
        "weight": 4
      },
      "item-3385": {
        "value": 9,
        "weight": 2
      },
      "item-3386": {
        "value": 4,
        "weight": 4
      },
      "item-3387": {
        "value": 8,
        "weight": 2
      },
      "item-3388": {
        "value": 8,
        "weight": 8
      },
      "item-3389": {
        "value": 8,
        "weight": 4
      },
      "item-3390": {
        "value": 9,
        "weight": 2
      },
      "item-3391": {
        "value": 1,
        "weight": 2
      },
      "item-3392": {
        "value": 9,
        "weight": 7
      },
      "item-3393": {
        "value": 5,
        "weight": 2
      },
      "item-3394": {
        "value": 5,
        "weight": 8
      },
      "item-3395": {
        "value": 9,
        "weight": 1
      },
      "item-3396": {
        "value": 7,
        "weight": 3
      },
      "item-3397": {
        "value": 8,
        "weight": 3
      },
      "item-3398": {
        "value": 9,
        "weight": 7
      },
      "item-3399": {
        "value": 6,
        "weight": 8
      },
      "item-3400": {
        "value": 4,
        "weight": 9
      },
      "item-3401": {
        "value": 1,
        "weight": 9
      },
      "item-3402": {
        "value": 7,
        "weight": 2
      },
      "item-3403": {
        "value": 9,
        "weight": 2
      },
      "item-3404": {
        "value": 6,
        "weight": 5
      },
      "item-3405": {
        "value": 4,
        "weight": 7
      },
      "item-3406": {
        "value": 2,
        "weight": 1
      },
      "item-3407": {
        "value": 4,
        "weight": 1
      },
      "item-3408": {
        "value": 9,
        "weight": 2
      },
      "item-3409": {
        "value": 5,
        "weight": 4
      },
      "item-3410": {
        "value": 8,
        "weight": 9
      },
      "item-3411": {
        "value": 2,
        "weight": 2
      },
      "item-3412": {
        "value": 1,
        "weight": 2
      },
      "item-3413": {
        "value": 1,
        "weight": 4
      },
      "item-3414": {
        "value": 3,
        "weight": 4
      },
      "item-3415": {
        "value": 9,
        "weight": 9
      },
      "item-3416": {
        "value": 2,
        "weight": 4
      },
      "item-3417": {
        "value": 4,
        "weight": 6
      },
      "item-3418": {
        "value": 5,
        "weight": 7
      },
      "item-3419": {
        "value": 7,
        "weight": 1
      },
      "item-3420": {
        "value": 9,
        "weight": 2
      },
      "item-3421": {
        "value": 2,
        "weight": 7
      },
      "item-3422": {
        "value": 3,
        "weight": 9
      },
      "item-3423": {
        "value": 4,
        "weight": 5
      },
      "item-3424": {
        "value": 2,
        "weight": 9
      },
      "item-3425": {
        "value": 8,
        "weight": 8
      },
      "item-3426": {
        "value": 9,
        "weight": 8
      },
      "item-3427": {
        "value": 4,
        "weight": 1
      },
      "item-3428": {
        "value": 5,
        "weight": 4
      },
      "item-3429": {
        "value": 1,
        "weight": 4
      },
      "item-3430": {
        "value": 5,
        "weight": 1
      },
      "item-3431": {
        "value": 7,
        "weight": 1
      },
      "item-3432": {
        "value": 7,
        "weight": 4
      },
      "item-3433": {
        "value": 3,
        "weight": 2
      },
      "item-3434": {
        "value": 9,
        "weight": 2
      },
      "item-3435": {
        "value": 1,
        "weight": 2
      },
      "item-3436": {
        "value": 2,
        "weight": 2
      },
      "item-3437": {
        "value": 7,
        "weight": 5
      },
      "item-3438": {
        "value": 8,
        "weight": 4
      },
      "item-3439": {
        "value": 1,
        "weight": 2
      },
      "item-3440": {
        "value": 5,
        "weight": 8
      },
      "item-3441": {
        "value": 1,
        "weight": 2
      },
      "item-3442": {
        "value": 2,
        "weight": 2
      },
      "item-3443": {
        "value": 1,
        "weight": 6
      },
      "item-3444": {
        "value": 8,
        "weight": 1
      },
      "item-3445": {
        "value": 6,
        "weight": 5
      },
      "item-3446": {
        "value": 3,
        "weight": 9
      },
      "item-3447": {
        "value": 4,
        "weight": 7
      },
      "item-3448": {
        "value": 8,
        "weight": 5
      },
      "item-3449": {
        "value": 1,
        "weight": 8
      },
      "item-3450": {
        "value": 1,
        "weight": 8
      },
      "item-3451": {
        "value": 7,
        "weight": 9
      },
      "item-3452": {
        "value": 6,
        "weight": 7
      },
      "item-3453": {
        "value": 7,
        "weight": 8
      },
      "item-3454": {
        "value": 9,
        "weight": 9
      },
      "item-3455": {
        "value": 7,
        "weight": 2
      },
      "item-3456": {
        "value": 8,
        "weight": 7
      },
      "item-3457": {
        "value": 6,
        "weight": 8
      },
      "item-3458": {
        "value": 3,
        "weight": 7
      },
      "item-3459": {
        "value": 4,
        "weight": 8
      },
      "item-3460": {
        "value": 2,
        "weight": 8
      },
      "item-3461": {
        "value": 8,
        "weight": 1
      },
      "item-3462": {
        "value": 4,
        "weight": 3
      },
      "item-3463": {
        "value": 2,
        "weight": 3
      },
      "item-3464": {
        "value": 6,
        "weight": 5
      },
      "item-3465": {
        "value": 6,
        "weight": 7
      },
      "item-3466": {
        "value": 8,
        "weight": 7
      },
      "item-3467": {
        "value": 2,
        "weight": 4
      },
      "item-3468": {
        "value": 7,
        "weight": 6
      },
      "item-3469": {
        "value": 7,
        "weight": 1
      },
      "item-3470": {
        "value": 2,
        "weight": 8
      },
      "item-3471": {
        "value": 7,
        "weight": 3
      },
      "item-3472": {
        "value": 2,
        "weight": 5
      },
      "item-3473": {
        "value": 2,
        "weight": 6
      },
      "item-3474": {
        "value": 3,
        "weight": 2
      },
      "item-3475": {
        "value": 4,
        "weight": 8
      },
      "item-3476": {
        "value": 7,
        "weight": 6
      },
      "item-3477": {
        "value": 3,
        "weight": 1
      },
      "item-3478": {
        "value": 5,
        "weight": 2
      },
      "item-3479": {
        "value": 4,
        "weight": 6
      },
      "item-3480": {
        "value": 2,
        "weight": 8
      },
      "item-3481": {
        "value": 6,
        "weight": 6
      },
      "item-3482": {
        "value": 4,
        "weight": 8
      },
      "item-3483": {
        "value": 7,
        "weight": 4
      },
      "item-3484": {
        "value": 2,
        "weight": 3
      },
      "item-3485": {
        "value": 9,
        "weight": 3
      },
      "item-3486": {
        "value": 4,
        "weight": 1
      },
      "item-3487": {
        "value": 2,
        "weight": 2
      },
      "item-3488": {
        "value": 5,
        "weight": 3
      },
      "item-3489": {
        "value": 3,
        "weight": 9
      },
      "item-3490": {
        "value": 8,
        "weight": 4
      },
      "item-3491": {
        "value": 1,
        "weight": 1
      },
      "item-3492": {
        "value": 4,
        "weight": 2
      },
      "item-3493": {
        "value": 9,
        "weight": 4
      },
      "item-3494": {
        "value": 7,
        "weight": 8
      },
      "item-3495": {
        "value": 2,
        "weight": 6
      },
      "item-3496": {
        "value": 8,
        "weight": 1
      },
      "item-3497": {
        "value": 4,
        "weight": 9
      },
      "item-3498": {
        "value": 7,
        "weight": 2
      },
      "item-3499": {
        "value": 5,
        "weight": 9
      },
      "item-3500": {
        "value": 1,
        "weight": 1
      },
      "item-3501": {
        "value": 3,
        "weight": 8
      },
      "item-3502": {
        "value": 9,
        "weight": 3
      },
      "item-3503": {
        "value": 6,
        "weight": 9
      },
      "item-3504": {
        "value": 4,
        "weight": 5
      },
      "item-3505": {
        "value": 4,
        "weight": 9
      },
      "item-3506": {
        "value": 3,
        "weight": 8
      },
      "item-3507": {
        "value": 8,
        "weight": 2
      },
      "item-3508": {
        "value": 4,
        "weight": 2
      },
      "item-3509": {
        "value": 5,
        "weight": 3
      },
      "item-3510": {
        "value": 5,
        "weight": 4
      },
      "item-3511": {
        "value": 9,
        "weight": 3
      },
      "item-3512": {
        "value": 6,
        "weight": 3
      },
      "item-3513": {
        "value": 3,
        "weight": 1
      },
      "item-3514": {
        "value": 7,
        "weight": 3
      },
      "item-3515": {
        "value": 9,
        "weight": 2
      },
      "item-3516": {
        "value": 6,
        "weight": 9
      },
      "item-3517": {
        "value": 9,
        "weight": 3
      },
      "item-3518": {
        "value": 5,
        "weight": 4
      },
      "item-3519": {
        "value": 9,
        "weight": 7
      },
      "item-3520": {
        "value": 3,
        "weight": 9
      },
      "item-3521": {
        "value": 5,
        "weight": 8
      },
      "item-3522": {
        "value": 7,
        "weight": 1
      },
      "item-3523": {
        "value": 7,
        "weight": 7
      },
      "item-3524": {
        "value": 8,
        "weight": 6
      },
      "item-3525": {
        "value": 2,
        "weight": 5
      },
      "item-3526": {
        "value": 6,
        "weight": 1
      },
      "item-3527": {
        "value": 3,
        "weight": 2
      },
      "item-3528": {
        "value": 3,
        "weight": 4
      },
      "item-3529": {
        "value": 5,
        "weight": 2
      },
      "item-3530": {
        "value": 6,
        "weight": 6
      },
      "item-3531": {
        "value": 7,
        "weight": 3
      },
      "item-3532": {
        "value": 5,
        "weight": 9
      },
      "item-3533": {
        "value": 3,
        "weight": 9
      },
      "item-3534": {
        "value": 6,
        "weight": 5
      },
      "item-3535": {
        "value": 4,
        "weight": 3
      },
      "item-3536": {
        "value": 8,
        "weight": 6
      },
      "item-3537": {
        "value": 4,
        "weight": 2
      },
      "item-3538": {
        "value": 6,
        "weight": 3
      },
      "item-3539": {
        "value": 6,
        "weight": 9
      },
      "item-3540": {
        "value": 9,
        "weight": 7
      },
      "item-3541": {
        "value": 3,
        "weight": 3
      },
      "item-3542": {
        "value": 4,
        "weight": 2
      },
      "item-3543": {
        "value": 1,
        "weight": 3
      },
      "item-3544": {
        "value": 2,
        "weight": 8
      },
      "item-3545": {
        "value": 7,
        "weight": 1
      },
      "item-3546": {
        "value": 4,
        "weight": 3
      },
      "item-3547": {
        "value": 1,
        "weight": 1
      },
      "item-3548": {
        "value": 1,
        "weight": 1
      },
      "item-3549": {
        "value": 2,
        "weight": 4
      },
      "item-3550": {
        "value": 4,
        "weight": 8
      },
      "item-3551": {
        "value": 5,
        "weight": 9
      },
      "item-3552": {
        "value": 3,
        "weight": 2
      },
      "item-3553": {
        "value": 8,
        "weight": 4
      },
      "item-3554": {
        "value": 4,
        "weight": 7
      },
      "item-3555": {
        "value": 3,
        "weight": 2
      },
      "item-3556": {
        "value": 2,
        "weight": 9
      },
      "item-3557": {
        "value": 3,
        "weight": 9
      },
      "item-3558": {
        "value": 4,
        "weight": 8
      },
      "item-3559": {
        "value": 7,
        "weight": 9
      },
      "item-3560": {
        "value": 8,
        "weight": 2
      },
      "item-3561": {
        "value": 1,
        "weight": 5
      },
      "item-3562": {
        "value": 4,
        "weight": 3
      },
      "item-3563": {
        "value": 1,
        "weight": 8
      },
      "item-3564": {
        "value": 9,
        "weight": 7
      },
      "item-3565": {
        "value": 1,
        "weight": 6
      },
      "item-3566": {
        "value": 7,
        "weight": 9
      },
      "item-3567": {
        "value": 3,
        "weight": 7
      },
      "item-3568": {
        "value": 7,
        "weight": 2
      },
      "item-3569": {
        "value": 3,
        "weight": 8
      },
      "item-3570": {
        "value": 7,
        "weight": 8
      },
      "item-3571": {
        "value": 6,
        "weight": 8
      },
      "item-3572": {
        "value": 5,
        "weight": 3
      },
      "item-3573": {
        "value": 2,
        "weight": 3
      },
      "item-3574": {
        "value": 2,
        "weight": 1
      },
      "item-3575": {
        "value": 4,
        "weight": 1
      },
      "item-3576": {
        "value": 6,
        "weight": 6
      },
      "item-3577": {
        "value": 1,
        "weight": 7
      },
      "item-3578": {
        "value": 7,
        "weight": 3
      },
      "item-3579": {
        "value": 8,
        "weight": 5
      },
      "item-3580": {
        "value": 5,
        "weight": 1
      },
      "item-3581": {
        "value": 3,
        "weight": 6
      },
      "item-3582": {
        "value": 9,
        "weight": 8
      },
      "item-3583": {
        "value": 9,
        "weight": 4
      },
      "item-3584": {
        "value": 1,
        "weight": 2
      },
      "item-3585": {
        "value": 5,
        "weight": 5
      },
      "item-3586": {
        "value": 9,
        "weight": 6
      },
      "item-3587": {
        "value": 4,
        "weight": 5
      },
      "item-3588": {
        "value": 6,
        "weight": 9
      },
      "item-3589": {
        "value": 6,
        "weight": 9
      },
      "item-3590": {
        "value": 6,
        "weight": 1
      },
      "item-3591": {
        "value": 2,
        "weight": 3
      },
      "item-3592": {
        "value": 7,
        "weight": 2
      },
      "item-3593": {
        "value": 2,
        "weight": 4
      },
      "item-3594": {
        "value": 1,
        "weight": 5
      },
      "item-3595": {
        "value": 2,
        "weight": 9
      },
      "item-3596": {
        "value": 7,
        "weight": 5
      },
      "item-3597": {
        "value": 1,
        "weight": 2
      },
      "item-3598": {
        "value": 7,
        "weight": 2
      },
      "item-3599": {
        "value": 7,
        "weight": 9
      },
      "item-3600": {
        "value": 9,
        "weight": 8
      },
      "item-3601": {
        "value": 2,
        "weight": 3
      },
      "item-3602": {
        "value": 8,
        "weight": 1
      },
      "item-3603": {
        "value": 6,
        "weight": 1
      },
      "item-3604": {
        "value": 3,
        "weight": 9
      },
      "item-3605": {
        "value": 4,
        "weight": 3
      },
      "item-3606": {
        "value": 8,
        "weight": 8
      },
      "item-3607": {
        "value": 8,
        "weight": 6
      },
      "item-3608": {
        "value": 5,
        "weight": 5
      },
      "item-3609": {
        "value": 9,
        "weight": 7
      },
      "item-3610": {
        "value": 9,
        "weight": 3
      },
      "item-3611": {
        "value": 8,
        "weight": 8
      },
      "item-3612": {
        "value": 6,
        "weight": 4
      },
      "item-3613": {
        "value": 6,
        "weight": 1
      },
      "item-3614": {
        "value": 3,
        "weight": 4
      },
      "item-3615": {
        "value": 5,
        "weight": 7
      },
      "item-3616": {
        "value": 1,
        "weight": 9
      },
      "item-3617": {
        "value": 4,
        "weight": 5
      },
      "item-3618": {
        "value": 4,
        "weight": 2
      },
      "item-3619": {
        "value": 7,
        "weight": 6
      },
      "item-3620": {
        "value": 1,
        "weight": 2
      },
      "item-3621": {
        "value": 9,
        "weight": 2
      },
      "item-3622": {
        "value": 9,
        "weight": 5
      },
      "item-3623": {
        "value": 4,
        "weight": 9
      },
      "item-3624": {
        "value": 8,
        "weight": 3
      },
      "item-3625": {
        "value": 4,
        "weight": 7
      },
      "item-3626": {
        "value": 6,
        "weight": 4
      },
      "item-3627": {
        "value": 7,
        "weight": 9
      },
      "item-3628": {
        "value": 5,
        "weight": 3
      },
      "item-3629": {
        "value": 4,
        "weight": 6
      },
      "item-3630": {
        "value": 2,
        "weight": 1
      },
      "item-3631": {
        "value": 6,
        "weight": 3
      },
      "item-3632": {
        "value": 6,
        "weight": 8
      },
      "item-3633": {
        "value": 1,
        "weight": 1
      },
      "item-3634": {
        "value": 4,
        "weight": 5
      },
      "item-3635": {
        "value": 4,
        "weight": 9
      },
      "item-3636": {
        "value": 1,
        "weight": 6
      },
      "item-3637": {
        "value": 9,
        "weight": 1
      },
      "item-3638": {
        "value": 6,
        "weight": 2
      },
      "item-3639": {
        "value": 1,
        "weight": 8
      },
      "item-3640": {
        "value": 2,
        "weight": 2
      },
      "item-3641": {
        "value": 4,
        "weight": 4
      },
      "item-3642": {
        "value": 4,
        "weight": 5
      },
      "item-3643": {
        "value": 6,
        "weight": 6
      },
      "item-3644": {
        "value": 3,
        "weight": 7
      },
      "item-3645": {
        "value": 1,
        "weight": 5
      },
      "item-3646": {
        "value": 6,
        "weight": 9
      },
      "item-3647": {
        "value": 2,
        "weight": 1
      },
      "item-3648": {
        "value": 9,
        "weight": 3
      },
      "item-3649": {
        "value": 2,
        "weight": 2
      },
      "item-3650": {
        "value": 9,
        "weight": 9
      },
      "item-3651": {
        "value": 4,
        "weight": 1
      },
      "item-3652": {
        "value": 3,
        "weight": 7
      },
      "item-3653": {
        "value": 8,
        "weight": 7
      },
      "item-3654": {
        "value": 9,
        "weight": 1
      },
      "item-3655": {
        "value": 5,
        "weight": 2
      },
      "item-3656": {
        "value": 7,
        "weight": 5
      },
      "item-3657": {
        "value": 1,
        "weight": 1
      },
      "item-3658": {
        "value": 8,
        "weight": 5
      },
      "item-3659": {
        "value": 1,
        "weight": 3
      },
      "item-3660": {
        "value": 8,
        "weight": 6
      },
      "item-3661": {
        "value": 3,
        "weight": 2
      },
      "item-3662": {
        "value": 4,
        "weight": 3
      },
      "item-3663": {
        "value": 7,
        "weight": 3
      },
      "item-3664": {
        "value": 5,
        "weight": 9
      },
      "item-3665": {
        "value": 9,
        "weight": 4
      },
      "item-3666": {
        "value": 1,
        "weight": 9
      },
      "item-3667": {
        "value": 9,
        "weight": 6
      },
      "item-3668": {
        "value": 4,
        "weight": 3
      },
      "item-3669": {
        "value": 4,
        "weight": 3
      },
      "item-3670": {
        "value": 4,
        "weight": 4
      },
      "item-3671": {
        "value": 4,
        "weight": 6
      },
      "item-3672": {
        "value": 4,
        "weight": 1
      },
      "item-3673": {
        "value": 7,
        "weight": 9
      },
      "item-3674": {
        "value": 2,
        "weight": 4
      },
      "item-3675": {
        "value": 6,
        "weight": 9
      },
      "item-3676": {
        "value": 3,
        "weight": 9
      },
      "item-3677": {
        "value": 2,
        "weight": 6
      },
      "item-3678": {
        "value": 2,
        "weight": 2
      },
      "item-3679": {
        "value": 6,
        "weight": 7
      },
      "item-3680": {
        "value": 9,
        "weight": 4
      },
      "item-3681": {
        "value": 7,
        "weight": 7
      },
      "item-3682": {
        "value": 6,
        "weight": 3
      },
      "item-3683": {
        "value": 8,
        "weight": 7
      },
      "item-3684": {
        "value": 8,
        "weight": 9
      },
      "item-3685": {
        "value": 8,
        "weight": 2
      },
      "item-3686": {
        "value": 2,
        "weight": 3
      },
      "item-3687": {
        "value": 3,
        "weight": 7
      },
      "item-3688": {
        "value": 8,
        "weight": 4
      },
      "item-3689": {
        "value": 7,
        "weight": 1
      },
      "item-3690": {
        "value": 7,
        "weight": 1
      },
      "item-3691": {
        "value": 3,
        "weight": 2
      },
      "item-3692": {
        "value": 1,
        "weight": 7
      },
      "item-3693": {
        "value": 1,
        "weight": 9
      },
      "item-3694": {
        "value": 7,
        "weight": 4
      },
      "item-3695": {
        "value": 1,
        "weight": 2
      },
      "item-3696": {
        "value": 1,
        "weight": 3
      },
      "item-3697": {
        "value": 6,
        "weight": 6
      },
      "item-3698": {
        "value": 6,
        "weight": 3
      },
      "item-3699": {
        "value": 2,
        "weight": 5
      },
      "item-3700": {
        "value": 6,
        "weight": 6
      },
      "item-3701": {
        "value": 3,
        "weight": 6
      },
      "item-3702": {
        "value": 9,
        "weight": 5
      },
      "item-3703": {
        "value": 7,
        "weight": 5
      },
      "item-3704": {
        "value": 9,
        "weight": 1
      },
      "item-3705": {
        "value": 7,
        "weight": 6
      },
      "item-3706": {
        "value": 6,
        "weight": 9
      },
      "item-3707": {
        "value": 1,
        "weight": 7
      },
      "item-3708": {
        "value": 3,
        "weight": 2
      },
      "item-3709": {
        "value": 6,
        "weight": 8
      },
      "item-3710": {
        "value": 8,
        "weight": 5
      },
      "item-3711": {
        "value": 1,
        "weight": 5
      },
      "item-3712": {
        "value": 8,
        "weight": 6
      },
      "item-3713": {
        "value": 9,
        "weight": 1
      },
      "item-3714": {
        "value": 2,
        "weight": 7
      },
      "item-3715": {
        "value": 3,
        "weight": 5
      },
      "item-3716": {
        "value": 2,
        "weight": 9
      },
      "item-3717": {
        "value": 5,
        "weight": 2
      },
      "item-3718": {
        "value": 9,
        "weight": 3
      },
      "item-3719": {
        "value": 3,
        "weight": 5
      },
      "item-3720": {
        "value": 4,
        "weight": 8
      },
      "item-3721": {
        "value": 4,
        "weight": 5
      },
      "item-3722": {
        "value": 4,
        "weight": 2
      },
      "item-3723": {
        "value": 4,
        "weight": 8
      },
      "item-3724": {
        "value": 4,
        "weight": 4
      },
      "item-3725": {
        "value": 6,
        "weight": 4
      },
      "item-3726": {
        "value": 3,
        "weight": 6
      },
      "item-3727": {
        "value": 6,
        "weight": 5
      },
      "item-3728": {
        "value": 5,
        "weight": 5
      },
      "item-3729": {
        "value": 4,
        "weight": 5
      },
      "item-3730": {
        "value": 6,
        "weight": 3
      },
      "item-3731": {
        "value": 8,
        "weight": 8
      },
      "item-3732": {
        "value": 7,
        "weight": 7
      },
      "item-3733": {
        "value": 7,
        "weight": 5
      },
      "item-3734": {
        "value": 9,
        "weight": 3
      },
      "item-3735": {
        "value": 8,
        "weight": 9
      },
      "item-3736": {
        "value": 3,
        "weight": 6
      },
      "item-3737": {
        "value": 1,
        "weight": 2
      },
      "item-3738": {
        "value": 5,
        "weight": 3
      },
      "item-3739": {
        "value": 5,
        "weight": 7
      },
      "item-3740": {
        "value": 8,
        "weight": 1
      },
      "item-3741": {
        "value": 5,
        "weight": 8
      },
      "item-3742": {
        "value": 4,
        "weight": 8
      },
      "item-3743": {
        "value": 5,
        "weight": 4
      },
      "item-3744": {
        "value": 7,
        "weight": 6
      },
      "item-3745": {
        "value": 4,
        "weight": 5
      },
      "item-3746": {
        "value": 8,
        "weight": 3
      },
      "item-3747": {
        "value": 1,
        "weight": 3
      },
      "item-3748": {
        "value": 7,
        "weight": 1
      },
      "item-3749": {
        "value": 3,
        "weight": 6
      },
      "item-3750": {
        "value": 7,
        "weight": 8
      },
      "item-3751": {
        "value": 1,
        "weight": 7
      },
      "item-3752": {
        "value": 1,
        "weight": 2
      },
      "item-3753": {
        "value": 4,
        "weight": 7
      },
      "item-3754": {
        "value": 5,
        "weight": 3
      },
      "item-3755": {
        "value": 9,
        "weight": 7
      },
      "item-3756": {
        "value": 5,
        "weight": 4
      },
      "item-3757": {
        "value": 8,
        "weight": 9
      },
      "item-3758": {
        "value": 9,
        "weight": 4
      },
      "item-3759": {
        "value": 2,
        "weight": 1
      },
      "item-3760": {
        "value": 1,
        "weight": 5
      },
      "item-3761": {
        "value": 6,
        "weight": 2
      },
      "item-3762": {
        "value": 4,
        "weight": 4
      },
      "item-3763": {
        "value": 3,
        "weight": 6
      },
      "item-3764": {
        "value": 4,
        "weight": 1
      },
      "item-3765": {
        "value": 6,
        "weight": 6
      },
      "item-3766": {
        "value": 8,
        "weight": 3
      },
      "item-3767": {
        "value": 3,
        "weight": 6
      },
      "item-3768": {
        "value": 4,
        "weight": 9
      },
      "item-3769": {
        "value": 6,
        "weight": 1
      },
      "item-3770": {
        "value": 3,
        "weight": 1
      },
      "item-3771": {
        "value": 6,
        "weight": 9
      },
      "item-3772": {
        "value": 4,
        "weight": 7
      },
      "item-3773": {
        "value": 5,
        "weight": 7
      },
      "item-3774": {
        "value": 2,
        "weight": 9
      },
      "item-3775": {
        "value": 2,
        "weight": 3
      },
      "item-3776": {
        "value": 9,
        "weight": 2
      },
      "item-3777": {
        "value": 1,
        "weight": 6
      },
      "item-3778": {
        "value": 8,
        "weight": 9
      },
      "item-3779": {
        "value": 3,
        "weight": 3
      },
      "item-3780": {
        "value": 6,
        "weight": 1
      },
      "item-3781": {
        "value": 8,
        "weight": 6
      },
      "item-3782": {
        "value": 4,
        "weight": 5
      },
      "item-3783": {
        "value": 2,
        "weight": 1
      },
      "item-3784": {
        "value": 6,
        "weight": 5
      },
      "item-3785": {
        "value": 2,
        "weight": 7
      },
      "item-3786": {
        "value": 8,
        "weight": 7
      },
      "item-3787": {
        "value": 6,
        "weight": 6
      },
      "item-3788": {
        "value": 8,
        "weight": 2
      },
      "item-3789": {
        "value": 5,
        "weight": 2
      },
      "item-3790": {
        "value": 5,
        "weight": 8
      },
      "item-3791": {
        "value": 8,
        "weight": 2
      },
      "item-3792": {
        "value": 3,
        "weight": 3
      },
      "item-3793": {
        "value": 5,
        "weight": 1
      },
      "item-3794": {
        "value": 7,
        "weight": 8
      },
      "item-3795": {
        "value": 3,
        "weight": 4
      },
      "item-3796": {
        "value": 2,
        "weight": 7
      },
      "item-3797": {
        "value": 4,
        "weight": 1
      },
      "item-3798": {
        "value": 2,
        "weight": 3
      },
      "item-3799": {
        "value": 4,
        "weight": 8
      },
      "item-3800": {
        "value": 5,
        "weight": 6
      },
      "item-3801": {
        "value": 9,
        "weight": 9
      },
      "item-3802": {
        "value": 8,
        "weight": 5
      },
      "item-3803": {
        "value": 9,
        "weight": 3
      },
      "item-3804": {
        "value": 7,
        "weight": 2
      },
      "item-3805": {
        "value": 4,
        "weight": 4
      },
      "item-3806": {
        "value": 2,
        "weight": 7
      },
      "item-3807": {
        "value": 5,
        "weight": 9
      },
      "item-3808": {
        "value": 1,
        "weight": 6
      },
      "item-3809": {
        "value": 8,
        "weight": 5
      },
      "item-3810": {
        "value": 5,
        "weight": 4
      },
      "item-3811": {
        "value": 8,
        "weight": 2
      },
      "item-3812": {
        "value": 6,
        "weight": 3
      },
      "item-3813": {
        "value": 2,
        "weight": 2
      },
      "item-3814": {
        "value": 6,
        "weight": 7
      },
      "item-3815": {
        "value": 5,
        "weight": 7
      },
      "item-3816": {
        "value": 1,
        "weight": 6
      },
      "item-3817": {
        "value": 3,
        "weight": 1
      },
      "item-3818": {
        "value": 9,
        "weight": 9
      },
      "item-3819": {
        "value": 6,
        "weight": 1
      },
      "item-3820": {
        "value": 4,
        "weight": 1
      },
      "item-3821": {
        "value": 8,
        "weight": 3
      },
      "item-3822": {
        "value": 8,
        "weight": 3
      },
      "item-3823": {
        "value": 8,
        "weight": 7
      },
      "item-3824": {
        "value": 5,
        "weight": 6
      },
      "item-3825": {
        "value": 3,
        "weight": 8
      },
      "item-3826": {
        "value": 5,
        "weight": 1
      },
      "item-3827": {
        "value": 1,
        "weight": 7
      },
      "item-3828": {
        "value": 1,
        "weight": 4
      },
      "item-3829": {
        "value": 4,
        "weight": 6
      },
      "item-3830": {
        "value": 1,
        "weight": 5
      },
      "item-3831": {
        "value": 7,
        "weight": 2
      },
      "item-3832": {
        "value": 2,
        "weight": 7
      },
      "item-3833": {
        "value": 4,
        "weight": 6
      },
      "item-3834": {
        "value": 2,
        "weight": 9
      },
      "item-3835": {
        "value": 5,
        "weight": 4
      },
      "item-3836": {
        "value": 5,
        "weight": 2
      },
      "item-3837": {
        "value": 9,
        "weight": 3
      },
      "item-3838": {
        "value": 5,
        "weight": 7
      },
      "item-3839": {
        "value": 7,
        "weight": 1
      },
      "item-3840": {
        "value": 9,
        "weight": 6
      },
      "item-3841": {
        "value": 5,
        "weight": 4
      },
      "item-3842": {
        "value": 1,
        "weight": 8
      },
      "item-3843": {
        "value": 5,
        "weight": 9
      },
      "item-3844": {
        "value": 2,
        "weight": 4
      },
      "item-3845": {
        "value": 2,
        "weight": 7
      },
      "item-3846": {
        "value": 4,
        "weight": 8
      },
      "item-3847": {
        "value": 7,
        "weight": 6
      },
      "item-3848": {
        "value": 8,
        "weight": 2
      },
      "item-3849": {
        "value": 4,
        "weight": 9
      },
      "item-3850": {
        "value": 3,
        "weight": 8
      },
      "item-3851": {
        "value": 6,
        "weight": 8
      },
      "item-3852": {
        "value": 4,
        "weight": 1
      },
      "item-3853": {
        "value": 7,
        "weight": 6
      },
      "item-3854": {
        "value": 2,
        "weight": 6
      },
      "item-3855": {
        "value": 4,
        "weight": 3
      },
      "item-3856": {
        "value": 5,
        "weight": 3
      },
      "item-3857": {
        "value": 1,
        "weight": 4
      },
      "item-3858": {
        "value": 1,
        "weight": 8
      },
      "item-3859": {
        "value": 9,
        "weight": 6
      },
      "item-3860": {
        "value": 8,
        "weight": 7
      },
      "item-3861": {
        "value": 4,
        "weight": 7
      },
      "item-3862": {
        "value": 4,
        "weight": 3
      },
      "item-3863": {
        "value": 4,
        "weight": 9
      },
      "item-3864": {
        "value": 9,
        "weight": 9
      },
      "item-3865": {
        "value": 1,
        "weight": 4
      },
      "item-3866": {
        "value": 6,
        "weight": 6
      },
      "item-3867": {
        "value": 6,
        "weight": 3
      },
      "item-3868": {
        "value": 6,
        "weight": 5
      },
      "item-3869": {
        "value": 2,
        "weight": 9
      },
      "item-3870": {
        "value": 7,
        "weight": 2
      },
      "item-3871": {
        "value": 4,
        "weight": 8
      },
      "item-3872": {
        "value": 5,
        "weight": 3
      },
      "item-3873": {
        "value": 4,
        "weight": 6
      },
      "item-3874": {
        "value": 3,
        "weight": 3
      },
      "item-3875": {
        "value": 4,
        "weight": 3
      },
      "item-3876": {
        "value": 6,
        "weight": 7
      },
      "item-3877": {
        "value": 9,
        "weight": 9
      },
      "item-3878": {
        "value": 1,
        "weight": 2
      },
      "item-3879": {
        "value": 8,
        "weight": 4
      },
      "item-3880": {
        "value": 1,
        "weight": 3
      },
      "item-3881": {
        "value": 8,
        "weight": 9
      },
      "item-3882": {
        "value": 9,
        "weight": 3
      },
      "item-3883": {
        "value": 8,
        "weight": 1
      },
      "item-3884": {
        "value": 1,
        "weight": 7
      },
      "item-3885": {
        "value": 4,
        "weight": 8
      },
      "item-3886": {
        "value": 3,
        "weight": 2
      },
      "item-3887": {
        "value": 8,
        "weight": 5
      },
      "item-3888": {
        "value": 6,
        "weight": 5
      },
      "item-3889": {
        "value": 8,
        "weight": 6
      },
      "item-3890": {
        "value": 4,
        "weight": 1
      },
      "item-3891": {
        "value": 7,
        "weight": 2
      },
      "item-3892": {
        "value": 8,
        "weight": 1
      },
      "item-3893": {
        "value": 2,
        "weight": 1
      },
      "item-3894": {
        "value": 2,
        "weight": 1
      },
      "item-3895": {
        "value": 6,
        "weight": 7
      },
      "item-3896": {
        "value": 2,
        "weight": 3
      },
      "item-3897": {
        "value": 6,
        "weight": 5
      },
      "item-3898": {
        "value": 8,
        "weight": 2
      },
      "item-3899": {
        "value": 7,
        "weight": 4
      },
      "item-3900": {
        "value": 1,
        "weight": 3
      },
      "item-3901": {
        "value": 3,
        "weight": 5
      },
      "item-3902": {
        "value": 7,
        "weight": 5
      },
      "item-3903": {
        "value": 7,
        "weight": 8
      },
      "item-3904": {
        "value": 9,
        "weight": 5
      },
      "item-3905": {
        "value": 1,
        "weight": 3
      },
      "item-3906": {
        "value": 2,
        "weight": 4
      },
      "item-3907": {
        "value": 4,
        "weight": 4
      },
      "item-3908": {
        "value": 8,
        "weight": 6
      },
      "item-3909": {
        "value": 3,
        "weight": 4
      },
      "item-3910": {
        "value": 2,
        "weight": 1
      },
      "item-3911": {
        "value": 8,
        "weight": 3
      },
      "item-3912": {
        "value": 4,
        "weight": 9
      },
      "item-3913": {
        "value": 6,
        "weight": 8
      },
      "item-3914": {
        "value": 3,
        "weight": 9
      },
      "item-3915": {
        "value": 2,
        "weight": 2
      },
      "item-3916": {
        "value": 4,
        "weight": 4
      },
      "item-3917": {
        "value": 8,
        "weight": 8
      },
      "item-3918": {
        "value": 4,
        "weight": 9
      },
      "item-3919": {
        "value": 6,
        "weight": 8
      },
      "item-3920": {
        "value": 2,
        "weight": 4
      },
      "item-3921": {
        "value": 3,
        "weight": 1
      },
      "item-3922": {
        "value": 4,
        "weight": 3
      },
      "item-3923": {
        "value": 5,
        "weight": 8
      },
      "item-3924": {
        "value": 5,
        "weight": 5
      },
      "item-3925": {
        "value": 6,
        "weight": 5
      },
      "item-3926": {
        "value": 2,
        "weight": 6
      },
      "item-3927": {
        "value": 4,
        "weight": 4
      },
      "item-3928": {
        "value": 9,
        "weight": 6
      },
      "item-3929": {
        "value": 2,
        "weight": 7
      },
      "item-3930": {
        "value": 5,
        "weight": 1
      },
      "item-3931": {
        "value": 6,
        "weight": 5
      },
      "item-3932": {
        "value": 6,
        "weight": 5
      },
      "item-3933": {
        "value": 5,
        "weight": 3
      },
      "item-3934": {
        "value": 8,
        "weight": 5
      },
      "item-3935": {
        "value": 6,
        "weight": 7
      },
      "item-3936": {
        "value": 1,
        "weight": 6
      },
      "item-3937": {
        "value": 6,
        "weight": 9
      },
      "item-3938": {
        "value": 6,
        "weight": 4
      },
      "item-3939": {
        "value": 5,
        "weight": 3
      },
      "item-3940": {
        "value": 9,
        "weight": 6
      },
      "item-3941": {
        "value": 1,
        "weight": 4
      },
      "item-3942": {
        "value": 1,
        "weight": 7
      },
      "item-3943": {
        "value": 5,
        "weight": 6
      },
      "item-3944": {
        "value": 7,
        "weight": 4
      },
      "item-3945": {
        "value": 7,
        "weight": 2
      },
      "item-3946": {
        "value": 7,
        "weight": 7
      },
      "item-3947": {
        "value": 6,
        "weight": 8
      },
      "item-3948": {
        "value": 6,
        "weight": 2
      },
      "item-3949": {
        "value": 7,
        "weight": 2
      },
      "item-3950": {
        "value": 5,
        "weight": 8
      },
      "item-3951": {
        "value": 6,
        "weight": 5
      },
      "item-3952": {
        "value": 7,
        "weight": 8
      },
      "item-3953": {
        "value": 6,
        "weight": 5
      },
      "item-3954": {
        "value": 5,
        "weight": 9
      },
      "item-3955": {
        "value": 5,
        "weight": 8
      },
      "item-3956": {
        "value": 8,
        "weight": 3
      },
      "item-3957": {
        "value": 4,
        "weight": 4
      },
      "item-3958": {
        "value": 6,
        "weight": 9
      },
      "item-3959": {
        "value": 1,
        "weight": 5
      },
      "item-3960": {
        "value": 3,
        "weight": 4
      },
      "item-3961": {
        "value": 1,
        "weight": 2
      },
      "item-3962": {
        "value": 7,
        "weight": 4
      },
      "item-3963": {
        "value": 2,
        "weight": 1
      },
      "item-3964": {
        "value": 4,
        "weight": 9
      },
      "item-3965": {
        "value": 8,
        "weight": 4
      },
      "item-3966": {
        "value": 5,
        "weight": 7
      },
      "item-3967": {
        "value": 8,
        "weight": 8
      },
      "item-3968": {
        "value": 3,
        "weight": 5
      },
      "item-3969": {
        "value": 2,
        "weight": 4
      },
      "item-3970": {
        "value": 4,
        "weight": 8
      },
      "item-3971": {
        "value": 9,
        "weight": 2
      },
      "item-3972": {
        "value": 4,
        "weight": 8
      },
      "item-3973": {
        "value": 2,
        "weight": 7
      },
      "item-3974": {
        "value": 2,
        "weight": 7
      },
      "item-3975": {
        "value": 8,
        "weight": 9
      },
      "item-3976": {
        "value": 9,
        "weight": 2
      },
      "item-3977": {
        "value": 4,
        "weight": 1
      },
      "item-3978": {
        "value": 1,
        "weight": 7
      },
      "item-3979": {
        "value": 3,
        "weight": 9
      },
      "item-3980": {
        "value": 3,
        "weight": 7
      },
      "item-3981": {
        "value": 6,
        "weight": 8
      },
      "item-3982": {
        "value": 7,
        "weight": 2
      },
      "item-3983": {
        "value": 4,
        "weight": 3
      },
      "item-3984": {
        "value": 1,
        "weight": 7
      },
      "item-3985": {
        "value": 6,
        "weight": 4
      },
      "item-3986": {
        "value": 5,
        "weight": 4
      },
      "item-3987": {
        "value": 3,
        "weight": 2
      },
      "item-3988": {
        "value": 4,
        "weight": 9
      },
      "item-3989": {
        "value": 4,
        "weight": 7
      },
      "item-3990": {
        "value": 8,
        "weight": 1
      },
      "item-3991": {
        "value": 8,
        "weight": 5
      },
      "item-3992": {
        "value": 5,
        "weight": 8
      },
      "item-3993": {
        "value": 9,
        "weight": 1
      },
      "item-3994": {
        "value": 9,
        "weight": 3
      },
      "item-3995": {
        "value": 3,
        "weight": 9
      },
      "item-3996": {
        "value": 4,
        "weight": 4
      },
      "item-3997": {
        "value": 3,
        "weight": 8
      },
      "item-3998": {
        "value": 3,
        "weight": 3
      },
      "item-3999": {
        "value": 1,
        "weight": 1
      },
      "item-4000": {
        "value": 7,
        "weight": 9
      },
      "item-4001": {
        "value": 8,
        "weight": 5
      },
      "item-4002": {
        "value": 4,
        "weight": 9
      },
      "item-4003": {
        "value": 6,
        "weight": 2
      },
      "item-4004": {
        "value": 3,
        "weight": 6
      },
      "item-4005": {
        "value": 8,
        "weight": 7
      },
      "item-4006": {
        "value": 8,
        "weight": 9
      },
      "item-4007": {
        "value": 9,
        "weight": 1
      },
      "item-4008": {
        "value": 5,
        "weight": 7
      },
      "item-4009": {
        "value": 6,
        "weight": 5
      },
      "item-4010": {
        "value": 1,
        "weight": 5
      },
      "item-4011": {
        "value": 9,
        "weight": 3
      },
      "item-4012": {
        "value": 2,
        "weight": 8
      },
      "item-4013": {
        "value": 7,
        "weight": 4
      },
      "item-4014": {
        "value": 8,
        "weight": 2
      },
      "item-4015": {
        "value": 1,
        "weight": 7
      },
      "item-4016": {
        "value": 6,
        "weight": 6
      },
      "item-4017": {
        "value": 7,
        "weight": 3
      },
      "item-4018": {
        "value": 8,
        "weight": 4
      },
      "item-4019": {
        "value": 5,
        "weight": 8
      },
      "item-4020": {
        "value": 3,
        "weight": 8
      },
      "item-4021": {
        "value": 9,
        "weight": 6
      },
      "item-4022": {
        "value": 6,
        "weight": 2
      },
      "item-4023": {
        "value": 4,
        "weight": 6
      },
      "item-4024": {
        "value": 3,
        "weight": 1
      },
      "item-4025": {
        "value": 1,
        "weight": 6
      },
      "item-4026": {
        "value": 8,
        "weight": 7
      },
      "item-4027": {
        "value": 2,
        "weight": 8
      },
      "item-4028": {
        "value": 5,
        "weight": 6
      },
      "item-4029": {
        "value": 6,
        "weight": 2
      },
      "item-4030": {
        "value": 8,
        "weight": 2
      },
      "item-4031": {
        "value": 7,
        "weight": 3
      },
      "item-4032": {
        "value": 8,
        "weight": 8
      },
      "item-4033": {
        "value": 3,
        "weight": 3
      },
      "item-4034": {
        "value": 4,
        "weight": 1
      },
      "item-4035": {
        "value": 1,
        "weight": 7
      },
      "item-4036": {
        "value": 1,
        "weight": 3
      },
      "item-4037": {
        "value": 9,
        "weight": 2
      },
      "item-4038": {
        "value": 6,
        "weight": 1
      },
      "item-4039": {
        "value": 4,
        "weight": 8
      },
      "item-4040": {
        "value": 1,
        "weight": 5
      },
      "item-4041": {
        "value": 5,
        "weight": 6
      },
      "item-4042": {
        "value": 3,
        "weight": 1
      },
      "item-4043": {
        "value": 3,
        "weight": 2
      },
      "item-4044": {
        "value": 4,
        "weight": 5
      },
      "item-4045": {
        "value": 4,
        "weight": 3
      },
      "item-4046": {
        "value": 4,
        "weight": 5
      },
      "item-4047": {
        "value": 7,
        "weight": 6
      },
      "item-4048": {
        "value": 9,
        "weight": 1
      },
      "item-4049": {
        "value": 8,
        "weight": 8
      },
      "item-4050": {
        "value": 4,
        "weight": 8
      },
      "item-4051": {
        "value": 6,
        "weight": 2
      },
      "item-4052": {
        "value": 8,
        "weight": 1
      },
      "item-4053": {
        "value": 1,
        "weight": 9
      },
      "item-4054": {
        "value": 6,
        "weight": 8
      },
      "item-4055": {
        "value": 8,
        "weight": 6
      },
      "item-4056": {
        "value": 4,
        "weight": 1
      },
      "item-4057": {
        "value": 7,
        "weight": 7
      },
      "item-4058": {
        "value": 7,
        "weight": 1
      },
      "item-4059": {
        "value": 8,
        "weight": 8
      },
      "item-4060": {
        "value": 4,
        "weight": 4
      },
      "item-4061": {
        "value": 5,
        "weight": 3
      },
      "item-4062": {
        "value": 9,
        "weight": 3
      },
      "item-4063": {
        "value": 1,
        "weight": 4
      },
      "item-4064": {
        "value": 5,
        "weight": 5
      },
      "item-4065": {
        "value": 9,
        "weight": 4
      },
      "item-4066": {
        "value": 3,
        "weight": 4
      },
      "item-4067": {
        "value": 6,
        "weight": 2
      },
      "item-4068": {
        "value": 7,
        "weight": 4
      },
      "item-4069": {
        "value": 9,
        "weight": 8
      },
      "item-4070": {
        "value": 3,
        "weight": 5
      },
      "item-4071": {
        "value": 6,
        "weight": 1
      },
      "item-4072": {
        "value": 3,
        "weight": 3
      },
      "item-4073": {
        "value": 7,
        "weight": 9
      },
      "item-4074": {
        "value": 4,
        "weight": 6
      },
      "item-4075": {
        "value": 3,
        "weight": 7
      },
      "item-4076": {
        "value": 6,
        "weight": 6
      },
      "item-4077": {
        "value": 3,
        "weight": 4
      },
      "item-4078": {
        "value": 6,
        "weight": 1
      },
      "item-4079": {
        "value": 4,
        "weight": 8
      },
      "item-4080": {
        "value": 7,
        "weight": 7
      },
      "item-4081": {
        "value": 7,
        "weight": 3
      },
      "item-4082": {
        "value": 9,
        "weight": 1
      },
      "item-4083": {
        "value": 9,
        "weight": 5
      },
      "item-4084": {
        "value": 8,
        "weight": 9
      },
      "item-4085": {
        "value": 5,
        "weight": 8
      },
      "item-4086": {
        "value": 8,
        "weight": 7
      },
      "item-4087": {
        "value": 5,
        "weight": 7
      },
      "item-4088": {
        "value": 8,
        "weight": 2
      },
      "item-4089": {
        "value": 1,
        "weight": 6
      },
      "item-4090": {
        "value": 8,
        "weight": 2
      },
      "item-4091": {
        "value": 1,
        "weight": 3
      },
      "item-4092": {
        "value": 2,
        "weight": 2
      },
      "item-4093": {
        "value": 2,
        "weight": 4
      },
      "item-4094": {
        "value": 2,
        "weight": 1
      },
      "item-4095": {
        "value": 7,
        "weight": 6
      },
      "item-4096": {
        "value": 6,
        "weight": 8
      },
      "item-4097": {
        "value": 8,
        "weight": 8
      },
      "item-4098": {
        "value": 5,
        "weight": 1
      },
      "item-4099": {
        "value": 8,
        "weight": 4
      },
      "item-4100": {
        "value": 8,
        "weight": 6
      },
      "item-4101": {
        "value": 8,
        "weight": 1
      },
      "item-4102": {
        "value": 3,
        "weight": 3
      },
      "item-4103": {
        "value": 8,
        "weight": 1
      },
      "item-4104": {
        "value": 7,
        "weight": 4
      },
      "item-4105": {
        "value": 1,
        "weight": 6
      },
      "item-4106": {
        "value": 2,
        "weight": 4
      },
      "item-4107": {
        "value": 1,
        "weight": 3
      },
      "item-4108": {
        "value": 2,
        "weight": 6
      },
      "item-4109": {
        "value": 1,
        "weight": 7
      },
      "item-4110": {
        "value": 2,
        "weight": 7
      },
      "item-4111": {
        "value": 6,
        "weight": 2
      },
      "item-4112": {
        "value": 9,
        "weight": 2
      },
      "item-4113": {
        "value": 4,
        "weight": 3
      },
      "item-4114": {
        "value": 8,
        "weight": 1
      },
      "item-4115": {
        "value": 3,
        "weight": 9
      },
      "item-4116": {
        "value": 1,
        "weight": 3
      },
      "item-4117": {
        "value": 7,
        "weight": 2
      },
      "item-4118": {
        "value": 7,
        "weight": 4
      },
      "item-4119": {
        "value": 2,
        "weight": 8
      },
      "item-4120": {
        "value": 8,
        "weight": 5
      },
      "item-4121": {
        "value": 3,
        "weight": 5
      },
      "item-4122": {
        "value": 1,
        "weight": 3
      },
      "item-4123": {
        "value": 6,
        "weight": 6
      },
      "item-4124": {
        "value": 6,
        "weight": 4
      },
      "item-4125": {
        "value": 8,
        "weight": 5
      },
      "item-4126": {
        "value": 2,
        "weight": 1
      },
      "item-4127": {
        "value": 7,
        "weight": 4
      },
      "item-4128": {
        "value": 8,
        "weight": 9
      },
      "item-4129": {
        "value": 6,
        "weight": 1
      },
      "item-4130": {
        "value": 9,
        "weight": 4
      },
      "item-4131": {
        "value": 7,
        "weight": 3
      },
      "item-4132": {
        "value": 2,
        "weight": 1
      },
      "item-4133": {
        "value": 5,
        "weight": 4
      },
      "item-4134": {
        "value": 9,
        "weight": 4
      },
      "item-4135": {
        "value": 6,
        "weight": 2
      },
      "item-4136": {
        "value": 2,
        "weight": 8
      },
      "item-4137": {
        "value": 1,
        "weight": 1
      },
      "item-4138": {
        "value": 2,
        "weight": 2
      },
      "item-4139": {
        "value": 1,
        "weight": 2
      },
      "item-4140": {
        "value": 4,
        "weight": 9
      },
      "item-4141": {
        "value": 3,
        "weight": 3
      },
      "item-4142": {
        "value": 1,
        "weight": 2
      },
      "item-4143": {
        "value": 9,
        "weight": 4
      },
      "item-4144": {
        "value": 6,
        "weight": 8
      },
      "item-4145": {
        "value": 7,
        "weight": 8
      },
      "item-4146": {
        "value": 7,
        "weight": 3
      },
      "item-4147": {
        "value": 5,
        "weight": 1
      },
      "item-4148": {
        "value": 6,
        "weight": 3
      },
      "item-4149": {
        "value": 8,
        "weight": 4
      },
      "item-4150": {
        "value": 8,
        "weight": 9
      },
      "item-4151": {
        "value": 9,
        "weight": 4
      },
      "item-4152": {
        "value": 8,
        "weight": 7
      },
      "item-4153": {
        "value": 9,
        "weight": 8
      },
      "item-4154": {
        "value": 3,
        "weight": 3
      },
      "item-4155": {
        "value": 7,
        "weight": 7
      },
      "item-4156": {
        "value": 9,
        "weight": 7
      },
      "item-4157": {
        "value": 4,
        "weight": 3
      },
      "item-4158": {
        "value": 6,
        "weight": 9
      },
      "item-4159": {
        "value": 3,
        "weight": 3
      },
      "item-4160": {
        "value": 5,
        "weight": 9
      },
      "item-4161": {
        "value": 6,
        "weight": 3
      },
      "item-4162": {
        "value": 3,
        "weight": 7
      },
      "item-4163": {
        "value": 1,
        "weight": 2
      },
      "item-4164": {
        "value": 2,
        "weight": 8
      },
      "item-4165": {
        "value": 5,
        "weight": 8
      },
      "item-4166": {
        "value": 5,
        "weight": 6
      },
      "item-4167": {
        "value": 7,
        "weight": 8
      },
      "item-4168": {
        "value": 2,
        "weight": 4
      },
      "item-4169": {
        "value": 4,
        "weight": 4
      },
      "item-4170": {
        "value": 4,
        "weight": 5
      },
      "item-4171": {
        "value": 5,
        "weight": 5
      },
      "item-4172": {
        "value": 7,
        "weight": 4
      },
      "item-4173": {
        "value": 5,
        "weight": 6
      },
      "item-4174": {
        "value": 9,
        "weight": 1
      },
      "item-4175": {
        "value": 2,
        "weight": 9
      },
      "item-4176": {
        "value": 3,
        "weight": 1
      },
      "item-4177": {
        "value": 1,
        "weight": 3
      },
      "item-4178": {
        "value": 2,
        "weight": 1
      },
      "item-4179": {
        "value": 6,
        "weight": 7
      },
      "item-4180": {
        "value": 1,
        "weight": 6
      },
      "item-4181": {
        "value": 8,
        "weight": 8
      },
      "item-4182": {
        "value": 3,
        "weight": 1
      },
      "item-4183": {
        "value": 6,
        "weight": 8
      },
      "item-4184": {
        "value": 2,
        "weight": 1
      },
      "item-4185": {
        "value": 4,
        "weight": 5
      },
      "item-4186": {
        "value": 6,
        "weight": 8
      },
      "item-4187": {
        "value": 7,
        "weight": 9
      },
      "item-4188": {
        "value": 3,
        "weight": 2
      },
      "item-4189": {
        "value": 3,
        "weight": 1
      },
      "item-4190": {
        "value": 3,
        "weight": 9
      },
      "item-4191": {
        "value": 2,
        "weight": 5
      },
      "item-4192": {
        "value": 2,
        "weight": 8
      },
      "item-4193": {
        "value": 2,
        "weight": 8
      },
      "item-4194": {
        "value": 7,
        "weight": 4
      },
      "item-4195": {
        "value": 6,
        "weight": 9
      },
      "item-4196": {
        "value": 7,
        "weight": 5
      },
      "item-4197": {
        "value": 1,
        "weight": 9
      },
      "item-4198": {
        "value": 9,
        "weight": 2
      },
      "item-4199": {
        "value": 1,
        "weight": 2
      },
      "item-4200": {
        "value": 5,
        "weight": 2
      },
      "item-4201": {
        "value": 6,
        "weight": 9
      },
      "item-4202": {
        "value": 9,
        "weight": 2
      },
      "item-4203": {
        "value": 5,
        "weight": 5
      },
      "item-4204": {
        "value": 5,
        "weight": 4
      },
      "item-4205": {
        "value": 9,
        "weight": 9
      },
      "item-4206": {
        "value": 8,
        "weight": 1
      },
      "item-4207": {
        "value": 7,
        "weight": 5
      },
      "item-4208": {
        "value": 5,
        "weight": 8
      },
      "item-4209": {
        "value": 7,
        "weight": 4
      },
      "item-4210": {
        "value": 5,
        "weight": 6
      },
      "item-4211": {
        "value": 2,
        "weight": 6
      },
      "item-4212": {
        "value": 6,
        "weight": 8
      },
      "item-4213": {
        "value": 5,
        "weight": 9
      },
      "item-4214": {
        "value": 1,
        "weight": 1
      },
      "item-4215": {
        "value": 9,
        "weight": 4
      },
      "item-4216": {
        "value": 1,
        "weight": 1
      },
      "item-4217": {
        "value": 4,
        "weight": 9
      },
      "item-4218": {
        "value": 6,
        "weight": 8
      },
      "item-4219": {
        "value": 2,
        "weight": 7
      },
      "item-4220": {
        "value": 9,
        "weight": 4
      },
      "item-4221": {
        "value": 9,
        "weight": 9
      },
      "item-4222": {
        "value": 8,
        "weight": 1
      },
      "item-4223": {
        "value": 3,
        "weight": 9
      },
      "item-4224": {
        "value": 8,
        "weight": 1
      },
      "item-4225": {
        "value": 8,
        "weight": 8
      },
      "item-4226": {
        "value": 5,
        "weight": 3
      },
      "item-4227": {
        "value": 7,
        "weight": 4
      },
      "item-4228": {
        "value": 5,
        "weight": 9
      },
      "item-4229": {
        "value": 4,
        "weight": 8
      },
      "item-4230": {
        "value": 8,
        "weight": 1
      },
      "item-4231": {
        "value": 2,
        "weight": 5
      },
      "item-4232": {
        "value": 3,
        "weight": 9
      },
      "item-4233": {
        "value": 4,
        "weight": 7
      },
      "item-4234": {
        "value": 3,
        "weight": 5
      },
      "item-4235": {
        "value": 9,
        "weight": 1
      },
      "item-4236": {
        "value": 9,
        "weight": 1
      },
      "item-4237": {
        "value": 3,
        "weight": 6
      },
      "item-4238": {
        "value": 6,
        "weight": 5
      },
      "item-4239": {
        "value": 5,
        "weight": 9
      },
      "item-4240": {
        "value": 6,
        "weight": 7
      },
      "item-4241": {
        "value": 8,
        "weight": 1
      },
      "item-4242": {
        "value": 9,
        "weight": 5
      },
      "item-4243": {
        "value": 7,
        "weight": 9
      },
      "item-4244": {
        "value": 6,
        "weight": 9
      },
      "item-4245": {
        "value": 2,
        "weight": 6
      },
      "item-4246": {
        "value": 2,
        "weight": 7
      },
      "item-4247": {
        "value": 7,
        "weight": 9
      },
      "item-4248": {
        "value": 8,
        "weight": 5
      },
      "item-4249": {
        "value": 3,
        "weight": 1
      },
      "item-4250": {
        "value": 3,
        "weight": 7
      },
      "item-4251": {
        "value": 9,
        "weight": 4
      },
      "item-4252": {
        "value": 2,
        "weight": 8
      },
      "item-4253": {
        "value": 4,
        "weight": 3
      },
      "item-4254": {
        "value": 9,
        "weight": 5
      },
      "item-4255": {
        "value": 9,
        "weight": 5
      },
      "item-4256": {
        "value": 8,
        "weight": 1
      },
      "item-4257": {
        "value": 6,
        "weight": 5
      },
      "item-4258": {
        "value": 5,
        "weight": 9
      },
      "item-4259": {
        "value": 8,
        "weight": 5
      },
      "item-4260": {
        "value": 6,
        "weight": 2
      },
      "item-4261": {
        "value": 1,
        "weight": 8
      },
      "item-4262": {
        "value": 5,
        "weight": 5
      },
      "item-4263": {
        "value": 2,
        "weight": 9
      },
      "item-4264": {
        "value": 3,
        "weight": 4
      },
      "item-4265": {
        "value": 5,
        "weight": 2
      },
      "item-4266": {
        "value": 7,
        "weight": 8
      },
      "item-4267": {
        "value": 8,
        "weight": 5
      },
      "item-4268": {
        "value": 4,
        "weight": 7
      },
      "item-4269": {
        "value": 3,
        "weight": 5
      },
      "item-4270": {
        "value": 5,
        "weight": 1
      },
      "item-4271": {
        "value": 5,
        "weight": 7
      },
      "item-4272": {
        "value": 4,
        "weight": 3
      },
      "item-4273": {
        "value": 1,
        "weight": 1
      },
      "item-4274": {
        "value": 8,
        "weight": 5
      },
      "item-4275": {
        "value": 1,
        "weight": 5
      },
      "item-4276": {
        "value": 9,
        "weight": 9
      },
      "item-4277": {
        "value": 8,
        "weight": 3
      },
      "item-4278": {
        "value": 8,
        "weight": 6
      },
      "item-4279": {
        "value": 3,
        "weight": 1
      },
      "item-4280": {
        "value": 6,
        "weight": 1
      },
      "item-4281": {
        "value": 4,
        "weight": 6
      },
      "item-4282": {
        "value": 2,
        "weight": 2
      },
      "item-4283": {
        "value": 7,
        "weight": 6
      },
      "item-4284": {
        "value": 4,
        "weight": 4
      },
      "item-4285": {
        "value": 3,
        "weight": 4
      },
      "item-4286": {
        "value": 3,
        "weight": 4
      },
      "item-4287": {
        "value": 3,
        "weight": 1
      },
      "item-4288": {
        "value": 2,
        "weight": 8
      },
      "item-4289": {
        "value": 9,
        "weight": 2
      },
      "item-4290": {
        "value": 4,
        "weight": 8
      },
      "item-4291": {
        "value": 5,
        "weight": 5
      },
      "item-4292": {
        "value": 3,
        "weight": 6
      },
      "item-4293": {
        "value": 4,
        "weight": 6
      },
      "item-4294": {
        "value": 1,
        "weight": 8
      },
      "item-4295": {
        "value": 8,
        "weight": 6
      },
      "item-4296": {
        "value": 4,
        "weight": 1
      },
      "item-4297": {
        "value": 4,
        "weight": 6
      },
      "item-4298": {
        "value": 3,
        "weight": 3
      },
      "item-4299": {
        "value": 8,
        "weight": 9
      },
      "item-4300": {
        "value": 9,
        "weight": 9
      },
      "item-4301": {
        "value": 4,
        "weight": 1
      },
      "item-4302": {
        "value": 5,
        "weight": 5
      },
      "item-4303": {
        "value": 3,
        "weight": 8
      },
      "item-4304": {
        "value": 7,
        "weight": 5
      },
      "item-4305": {
        "value": 9,
        "weight": 4
      },
      "item-4306": {
        "value": 5,
        "weight": 4
      },
      "item-4307": {
        "value": 7,
        "weight": 1
      },
      "item-4308": {
        "value": 8,
        "weight": 8
      },
      "item-4309": {
        "value": 4,
        "weight": 3
      },
      "item-4310": {
        "value": 7,
        "weight": 1
      },
      "item-4311": {
        "value": 1,
        "weight": 3
      },
      "item-4312": {
        "value": 8,
        "weight": 1
      },
      "item-4313": {
        "value": 5,
        "weight": 1
      },
      "item-4314": {
        "value": 6,
        "weight": 9
      },
      "item-4315": {
        "value": 3,
        "weight": 3
      },
      "item-4316": {
        "value": 3,
        "weight": 8
      },
      "item-4317": {
        "value": 1,
        "weight": 1
      },
      "item-4318": {
        "value": 6,
        "weight": 6
      },
      "item-4319": {
        "value": 8,
        "weight": 8
      },
      "item-4320": {
        "value": 6,
        "weight": 2
      },
      "item-4321": {
        "value": 1,
        "weight": 4
      },
      "item-4322": {
        "value": 8,
        "weight": 1
      },
      "item-4323": {
        "value": 6,
        "weight": 7
      },
      "item-4324": {
        "value": 5,
        "weight": 8
      },
      "item-4325": {
        "value": 5,
        "weight": 2
      },
      "item-4326": {
        "value": 9,
        "weight": 6
      },
      "item-4327": {
        "value": 5,
        "weight": 9
      },
      "item-4328": {
        "value": 5,
        "weight": 3
      },
      "item-4329": {
        "value": 2,
        "weight": 5
      },
      "item-4330": {
        "value": 6,
        "weight": 4
      },
      "item-4331": {
        "value": 8,
        "weight": 2
      },
      "item-4332": {
        "value": 6,
        "weight": 5
      },
      "item-4333": {
        "value": 2,
        "weight": 3
      },
      "item-4334": {
        "value": 7,
        "weight": 4
      },
      "item-4335": {
        "value": 2,
        "weight": 3
      },
      "item-4336": {
        "value": 6,
        "weight": 5
      },
      "item-4337": {
        "value": 3,
        "weight": 2
      },
      "item-4338": {
        "value": 8,
        "weight": 4
      },
      "item-4339": {
        "value": 4,
        "weight": 1
      },
      "item-4340": {
        "value": 7,
        "weight": 2
      },
      "item-4341": {
        "value": 6,
        "weight": 4
      },
      "item-4342": {
        "value": 3,
        "weight": 4
      },
      "item-4343": {
        "value": 9,
        "weight": 4
      },
      "item-4344": {
        "value": 1,
        "weight": 3
      },
      "item-4345": {
        "value": 2,
        "weight": 4
      },
      "item-4346": {
        "value": 4,
        "weight": 1
      },
      "item-4347": {
        "value": 9,
        "weight": 5
      },
      "item-4348": {
        "value": 6,
        "weight": 7
      },
      "item-4349": {
        "value": 8,
        "weight": 5
      },
      "item-4350": {
        "value": 5,
        "weight": 4
      },
      "item-4351": {
        "value": 8,
        "weight": 1
      },
      "item-4352": {
        "value": 1,
        "weight": 4
      },
      "item-4353": {
        "value": 2,
        "weight": 3
      },
      "item-4354": {
        "value": 6,
        "weight": 4
      },
      "item-4355": {
        "value": 4,
        "weight": 6
      },
      "item-4356": {
        "value": 5,
        "weight": 1
      },
      "item-4357": {
        "value": 9,
        "weight": 8
      },
      "item-4358": {
        "value": 3,
        "weight": 5
      },
      "item-4359": {
        "value": 1,
        "weight": 3
      },
      "item-4360": {
        "value": 6,
        "weight": 3
      },
      "item-4361": {
        "value": 9,
        "weight": 8
      },
      "item-4362": {
        "value": 2,
        "weight": 8
      },
      "item-4363": {
        "value": 2,
        "weight": 4
      },
      "item-4364": {
        "value": 1,
        "weight": 5
      },
      "item-4365": {
        "value": 2,
        "weight": 4
      },
      "item-4366": {
        "value": 9,
        "weight": 9
      },
      "item-4367": {
        "value": 7,
        "weight": 6
      },
      "item-4368": {
        "value": 7,
        "weight": 6
      },
      "item-4369": {
        "value": 7,
        "weight": 6
      },
      "item-4370": {
        "value": 2,
        "weight": 9
      },
      "item-4371": {
        "value": 2,
        "weight": 3
      },
      "item-4372": {
        "value": 2,
        "weight": 8
      },
      "item-4373": {
        "value": 3,
        "weight": 2
      },
      "item-4374": {
        "value": 1,
        "weight": 8
      },
      "item-4375": {
        "value": 3,
        "weight": 1
      },
      "item-4376": {
        "value": 7,
        "weight": 3
      },
      "item-4377": {
        "value": 8,
        "weight": 4
      },
      "item-4378": {
        "value": 1,
        "weight": 7
      },
      "item-4379": {
        "value": 2,
        "weight": 9
      },
      "item-4380": {
        "value": 5,
        "weight": 5
      },
      "item-4381": {
        "value": 7,
        "weight": 2
      },
      "item-4382": {
        "value": 7,
        "weight": 9
      },
      "item-4383": {
        "value": 4,
        "weight": 6
      },
      "item-4384": {
        "value": 6,
        "weight": 7
      },
      "item-4385": {
        "value": 2,
        "weight": 2
      },
      "item-4386": {
        "value": 9,
        "weight": 4
      },
      "item-4387": {
        "value": 5,
        "weight": 6
      },
      "item-4388": {
        "value": 2,
        "weight": 1
      },
      "item-4389": {
        "value": 9,
        "weight": 3
      },
      "item-4390": {
        "value": 6,
        "weight": 7
      },
      "item-4391": {
        "value": 6,
        "weight": 5
      },
      "item-4392": {
        "value": 2,
        "weight": 5
      },
      "item-4393": {
        "value": 8,
        "weight": 6
      },
      "item-4394": {
        "value": 6,
        "weight": 7
      },
      "item-4395": {
        "value": 7,
        "weight": 9
      },
      "item-4396": {
        "value": 3,
        "weight": 5
      },
      "item-4397": {
        "value": 7,
        "weight": 7
      },
      "item-4398": {
        "value": 8,
        "weight": 9
      },
      "item-4399": {
        "value": 5,
        "weight": 9
      },
      "item-4400": {
        "value": 4,
        "weight": 5
      },
      "item-4401": {
        "value": 8,
        "weight": 4
      },
      "item-4402": {
        "value": 6,
        "weight": 6
      },
      "item-4403": {
        "value": 2,
        "weight": 1
      },
      "item-4404": {
        "value": 7,
        "weight": 8
      },
      "item-4405": {
        "value": 7,
        "weight": 3
      },
      "item-4406": {
        "value": 8,
        "weight": 5
      },
      "item-4407": {
        "value": 2,
        "weight": 6
      },
      "item-4408": {
        "value": 9,
        "weight": 6
      },
      "item-4409": {
        "value": 8,
        "weight": 9
      },
      "item-4410": {
        "value": 1,
        "weight": 8
      },
      "item-4411": {
        "value": 1,
        "weight": 2
      },
      "item-4412": {
        "value": 9,
        "weight": 4
      },
      "item-4413": {
        "value": 4,
        "weight": 3
      },
      "item-4414": {
        "value": 7,
        "weight": 4
      },
      "item-4415": {
        "value": 9,
        "weight": 8
      },
      "item-4416": {
        "value": 5,
        "weight": 9
      },
      "item-4417": {
        "value": 5,
        "weight": 8
      },
      "item-4418": {
        "value": 3,
        "weight": 9
      },
      "item-4419": {
        "value": 8,
        "weight": 7
      },
      "item-4420": {
        "value": 7,
        "weight": 7
      },
      "item-4421": {
        "value": 2,
        "weight": 8
      },
      "item-4422": {
        "value": 6,
        "weight": 7
      },
      "item-4423": {
        "value": 9,
        "weight": 3
      },
      "item-4424": {
        "value": 9,
        "weight": 5
      },
      "item-4425": {
        "value": 9,
        "weight": 4
      },
      "item-4426": {
        "value": 8,
        "weight": 6
      },
      "item-4427": {
        "value": 5,
        "weight": 6
      },
      "item-4428": {
        "value": 8,
        "weight": 2
      },
      "item-4429": {
        "value": 5,
        "weight": 8
      },
      "item-4430": {
        "value": 4,
        "weight": 6
      },
      "item-4431": {
        "value": 2,
        "weight": 6
      },
      "item-4432": {
        "value": 9,
        "weight": 1
      },
      "item-4433": {
        "value": 6,
        "weight": 5
      },
      "item-4434": {
        "value": 5,
        "weight": 1
      },
      "item-4435": {
        "value": 8,
        "weight": 2
      },
      "item-4436": {
        "value": 9,
        "weight": 1
      },
      "item-4437": {
        "value": 4,
        "weight": 5
      },
      "item-4438": {
        "value": 5,
        "weight": 2
      },
      "item-4439": {
        "value": 4,
        "weight": 1
      },
      "item-4440": {
        "value": 4,
        "weight": 3
      },
      "item-4441": {
        "value": 8,
        "weight": 7
      },
      "item-4442": {
        "value": 2,
        "weight": 3
      },
      "item-4443": {
        "value": 5,
        "weight": 8
      },
      "item-4444": {
        "value": 3,
        "weight": 4
      },
      "item-4445": {
        "value": 5,
        "weight": 4
      },
      "item-4446": {
        "value": 4,
        "weight": 4
      },
      "item-4447": {
        "value": 2,
        "weight": 9
      },
      "item-4448": {
        "value": 3,
        "weight": 5
      },
      "item-4449": {
        "value": 4,
        "weight": 9
      },
      "item-4450": {
        "value": 3,
        "weight": 8
      },
      "item-4451": {
        "value": 6,
        "weight": 3
      },
      "item-4452": {
        "value": 4,
        "weight": 8
      },
      "item-4453": {
        "value": 5,
        "weight": 9
      },
      "item-4454": {
        "value": 7,
        "weight": 7
      },
      "item-4455": {
        "value": 7,
        "weight": 2
      },
      "item-4456": {
        "value": 3,
        "weight": 8
      },
      "item-4457": {
        "value": 5,
        "weight": 1
      },
      "item-4458": {
        "value": 6,
        "weight": 9
      },
      "item-4459": {
        "value": 9,
        "weight": 5
      },
      "item-4460": {
        "value": 8,
        "weight": 4
      },
      "item-4461": {
        "value": 7,
        "weight": 4
      },
      "item-4462": {
        "value": 9,
        "weight": 9
      },
      "item-4463": {
        "value": 2,
        "weight": 2
      },
      "item-4464": {
        "value": 4,
        "weight": 2
      },
      "item-4465": {
        "value": 6,
        "weight": 1
      },
      "item-4466": {
        "value": 2,
        "weight": 3
      },
      "item-4467": {
        "value": 4,
        "weight": 9
      },
      "item-4468": {
        "value": 8,
        "weight": 2
      },
      "item-4469": {
        "value": 7,
        "weight": 3
      },
      "item-4470": {
        "value": 9,
        "weight": 5
      },
      "item-4471": {
        "value": 3,
        "weight": 8
      },
      "item-4472": {
        "value": 7,
        "weight": 7
      },
      "item-4473": {
        "value": 3,
        "weight": 4
      },
      "item-4474": {
        "value": 3,
        "weight": 9
      },
      "item-4475": {
        "value": 1,
        "weight": 8
      },
      "item-4476": {
        "value": 5,
        "weight": 5
      },
      "item-4477": {
        "value": 4,
        "weight": 2
      },
      "item-4478": {
        "value": 7,
        "weight": 6
      },
      "item-4479": {
        "value": 7,
        "weight": 2
      },
      "item-4480": {
        "value": 7,
        "weight": 1
      },
      "item-4481": {
        "value": 4,
        "weight": 1
      },
      "item-4482": {
        "value": 9,
        "weight": 3
      },
      "item-4483": {
        "value": 4,
        "weight": 4
      },
      "item-4484": {
        "value": 6,
        "weight": 4
      },
      "item-4485": {
        "value": 7,
        "weight": 6
      },
      "item-4486": {
        "value": 9,
        "weight": 7
      },
      "item-4487": {
        "value": 7,
        "weight": 5
      },
      "item-4488": {
        "value": 7,
        "weight": 3
      },
      "item-4489": {
        "value": 3,
        "weight": 1
      },
      "item-4490": {
        "value": 8,
        "weight": 1
      },
      "item-4491": {
        "value": 3,
        "weight": 6
      },
      "item-4492": {
        "value": 5,
        "weight": 1
      },
      "item-4493": {
        "value": 1,
        "weight": 4
      },
      "item-4494": {
        "value": 4,
        "weight": 8
      },
      "item-4495": {
        "value": 4,
        "weight": 3
      },
      "item-4496": {
        "value": 5,
        "weight": 2
      },
      "item-4497": {
        "value": 9,
        "weight": 4
      },
      "item-4498": {
        "value": 4,
        "weight": 8
      },
      "item-4499": {
        "value": 6,
        "weight": 5
      },
      "item-4500": {
        "value": 9,
        "weight": 7
      },
      "item-4501": {
        "value": 3,
        "weight": 1
      },
      "item-4502": {
        "value": 3,
        "weight": 3
      },
      "item-4503": {
        "value": 1,
        "weight": 3
      },
      "item-4504": {
        "value": 6,
        "weight": 7
      },
      "item-4505": {
        "value": 1,
        "weight": 9
      },
      "item-4506": {
        "value": 8,
        "weight": 5
      },
      "item-4507": {
        "value": 9,
        "weight": 4
      },
      "item-4508": {
        "value": 4,
        "weight": 7
      },
      "item-4509": {
        "value": 1,
        "weight": 1
      },
      "item-4510": {
        "value": 9,
        "weight": 2
      },
      "item-4511": {
        "value": 3,
        "weight": 5
      },
      "item-4512": {
        "value": 6,
        "weight": 7
      },
      "item-4513": {
        "value": 8,
        "weight": 8
      },
      "item-4514": {
        "value": 3,
        "weight": 7
      },
      "item-4515": {
        "value": 4,
        "weight": 5
      },
      "item-4516": {
        "value": 6,
        "weight": 1
      },
      "item-4517": {
        "value": 1,
        "weight": 7
      },
      "item-4518": {
        "value": 8,
        "weight": 3
      },
      "item-4519": {
        "value": 1,
        "weight": 6
      },
      "item-4520": {
        "value": 1,
        "weight": 3
      },
      "item-4521": {
        "value": 3,
        "weight": 9
      },
      "item-4522": {
        "value": 4,
        "weight": 4
      },
      "item-4523": {
        "value": 7,
        "weight": 5
      },
      "item-4524": {
        "value": 4,
        "weight": 1
      },
      "item-4525": {
        "value": 3,
        "weight": 5
      },
      "item-4526": {
        "value": 9,
        "weight": 6
      },
      "item-4527": {
        "value": 3,
        "weight": 2
      },
      "item-4528": {
        "value": 2,
        "weight": 3
      },
      "item-4529": {
        "value": 1,
        "weight": 8
      },
      "item-4530": {
        "value": 8,
        "weight": 6
      },
      "item-4531": {
        "value": 9,
        "weight": 6
      },
      "item-4532": {
        "value": 7,
        "weight": 4
      },
      "item-4533": {
        "value": 9,
        "weight": 4
      },
      "item-4534": {
        "value": 1,
        "weight": 5
      },
      "item-4535": {
        "value": 8,
        "weight": 4
      },
      "item-4536": {
        "value": 7,
        "weight": 5
      },
      "item-4537": {
        "value": 7,
        "weight": 9
      },
      "item-4538": {
        "value": 9,
        "weight": 2
      },
      "item-4539": {
        "value": 2,
        "weight": 7
      },
      "item-4540": {
        "value": 8,
        "weight": 4
      },
      "item-4541": {
        "value": 1,
        "weight": 7
      },
      "item-4542": {
        "value": 1,
        "weight": 3
      },
      "item-4543": {
        "value": 6,
        "weight": 8
      },
      "item-4544": {
        "value": 2,
        "weight": 8
      },
      "item-4545": {
        "value": 7,
        "weight": 1
      },
      "item-4546": {
        "value": 6,
        "weight": 5
      },
      "item-4547": {
        "value": 7,
        "weight": 4
      },
      "item-4548": {
        "value": 6,
        "weight": 8
      },
      "item-4549": {
        "value": 9,
        "weight": 1
      },
      "item-4550": {
        "value": 6,
        "weight": 9
      },
      "item-4551": {
        "value": 7,
        "weight": 1
      },
      "item-4552": {
        "value": 8,
        "weight": 7
      },
      "item-4553": {
        "value": 2,
        "weight": 4
      },
      "item-4554": {
        "value": 7,
        "weight": 1
      },
      "item-4555": {
        "value": 8,
        "weight": 3
      },
      "item-4556": {
        "value": 7,
        "weight": 3
      },
      "item-4557": {
        "value": 2,
        "weight": 5
      },
      "item-4558": {
        "value": 1,
        "weight": 3
      },
      "item-4559": {
        "value": 6,
        "weight": 3
      },
      "item-4560": {
        "value": 4,
        "weight": 5
      },
      "item-4561": {
        "value": 9,
        "weight": 2
      },
      "item-4562": {
        "value": 5,
        "weight": 1
      },
      "item-4563": {
        "value": 8,
        "weight": 6
      },
      "item-4564": {
        "value": 7,
        "weight": 1
      },
      "item-4565": {
        "value": 1,
        "weight": 3
      },
      "item-4566": {
        "value": 1,
        "weight": 9
      },
      "item-4567": {
        "value": 5,
        "weight": 7
      },
      "item-4568": {
        "value": 7,
        "weight": 2
      },
      "item-4569": {
        "value": 8,
        "weight": 8
      },
      "item-4570": {
        "value": 1,
        "weight": 4
      },
      "item-4571": {
        "value": 3,
        "weight": 5
      },
      "item-4572": {
        "value": 6,
        "weight": 1
      },
      "item-4573": {
        "value": 9,
        "weight": 5
      },
      "item-4574": {
        "value": 8,
        "weight": 7
      },
      "item-4575": {
        "value": 3,
        "weight": 9
      },
      "item-4576": {
        "value": 4,
        "weight": 2
      },
      "item-4577": {
        "value": 6,
        "weight": 1
      },
      "item-4578": {
        "value": 8,
        "weight": 8
      },
      "item-4579": {
        "value": 4,
        "weight": 7
      },
      "item-4580": {
        "value": 6,
        "weight": 9
      },
      "item-4581": {
        "value": 3,
        "weight": 9
      },
      "item-4582": {
        "value": 6,
        "weight": 6
      },
      "item-4583": {
        "value": 2,
        "weight": 2
      },
      "item-4584": {
        "value": 8,
        "weight": 6
      },
      "item-4585": {
        "value": 7,
        "weight": 8
      },
      "item-4586": {
        "value": 7,
        "weight": 4
      },
      "item-4587": {
        "value": 7,
        "weight": 8
      },
      "item-4588": {
        "value": 4,
        "weight": 3
      },
      "item-4589": {
        "value": 5,
        "weight": 7
      },
      "item-4590": {
        "value": 7,
        "weight": 5
      },
      "item-4591": {
        "value": 9,
        "weight": 1
      },
      "item-4592": {
        "value": 1,
        "weight": 8
      },
      "item-4593": {
        "value": 2,
        "weight": 9
      },
      "item-4594": {
        "value": 5,
        "weight": 5
      },
      "item-4595": {
        "value": 5,
        "weight": 8
      },
      "item-4596": {
        "value": 8,
        "weight": 7
      },
      "item-4597": {
        "value": 7,
        "weight": 1
      },
      "item-4598": {
        "value": 6,
        "weight": 9
      },
      "item-4599": {
        "value": 7,
        "weight": 9
      },
      "item-4600": {
        "value": 6,
        "weight": 1
      },
      "item-4601": {
        "value": 2,
        "weight": 7
      },
      "item-4602": {
        "value": 9,
        "weight": 2
      },
      "item-4603": {
        "value": 9,
        "weight": 7
      },
      "item-4604": {
        "value": 9,
        "weight": 3
      },
      "item-4605": {
        "value": 1,
        "weight": 4
      },
      "item-4606": {
        "value": 7,
        "weight": 7
      },
      "item-4607": {
        "value": 5,
        "weight": 5
      },
      "item-4608": {
        "value": 9,
        "weight": 1
      },
      "item-4609": {
        "value": 8,
        "weight": 3
      },
      "item-4610": {
        "value": 9,
        "weight": 6
      },
      "item-4611": {
        "value": 2,
        "weight": 9
      },
      "item-4612": {
        "value": 9,
        "weight": 7
      },
      "item-4613": {
        "value": 6,
        "weight": 6
      },
      "item-4614": {
        "value": 3,
        "weight": 5
      },
      "item-4615": {
        "value": 2,
        "weight": 8
      },
      "item-4616": {
        "value": 7,
        "weight": 6
      },
      "item-4617": {
        "value": 8,
        "weight": 3
      },
      "item-4618": {
        "value": 4,
        "weight": 7
      },
      "item-4619": {
        "value": 3,
        "weight": 2
      },
      "item-4620": {
        "value": 3,
        "weight": 5
      },
      "item-4621": {
        "value": 6,
        "weight": 3
      },
      "item-4622": {
        "value": 6,
        "weight": 7
      },
      "item-4623": {
        "value": 5,
        "weight": 3
      },
      "item-4624": {
        "value": 9,
        "weight": 4
      },
      "item-4625": {
        "value": 8,
        "weight": 4
      },
      "item-4626": {
        "value": 1,
        "weight": 4
      },
      "item-4627": {
        "value": 7,
        "weight": 3
      },
      "item-4628": {
        "value": 4,
        "weight": 3
      },
      "item-4629": {
        "value": 1,
        "weight": 6
      },
      "item-4630": {
        "value": 2,
        "weight": 1
      },
      "item-4631": {
        "value": 9,
        "weight": 6
      },
      "item-4632": {
        "value": 6,
        "weight": 1
      },
      "item-4633": {
        "value": 8,
        "weight": 4
      },
      "item-4634": {
        "value": 5,
        "weight": 5
      },
      "item-4635": {
        "value": 2,
        "weight": 7
      },
      "item-4636": {
        "value": 1,
        "weight": 7
      },
      "item-4637": {
        "value": 5,
        "weight": 3
      },
      "item-4638": {
        "value": 8,
        "weight": 4
      },
      "item-4639": {
        "value": 1,
        "weight": 6
      },
      "item-4640": {
        "value": 7,
        "weight": 1
      },
      "item-4641": {
        "value": 6,
        "weight": 8
      },
      "item-4642": {
        "value": 7,
        "weight": 6
      },
      "item-4643": {
        "value": 6,
        "weight": 7
      },
      "item-4644": {
        "value": 9,
        "weight": 7
      },
      "item-4645": {
        "value": 9,
        "weight": 2
      },
      "item-4646": {
        "value": 9,
        "weight": 3
      },
      "item-4647": {
        "value": 3,
        "weight": 1
      },
      "item-4648": {
        "value": 1,
        "weight": 6
      },
      "item-4649": {
        "value": 1,
        "weight": 9
      },
      "item-4650": {
        "value": 7,
        "weight": 3
      },
      "item-4651": {
        "value": 2,
        "weight": 4
      },
      "item-4652": {
        "value": 4,
        "weight": 2
      },
      "item-4653": {
        "value": 3,
        "weight": 4
      },
      "item-4654": {
        "value": 6,
        "weight": 3
      },
      "item-4655": {
        "value": 6,
        "weight": 2
      },
      "item-4656": {
        "value": 9,
        "weight": 2
      },
      "item-4657": {
        "value": 9,
        "weight": 2
      },
      "item-4658": {
        "value": 3,
        "weight": 1
      },
      "item-4659": {
        "value": 6,
        "weight": 9
      },
      "item-4660": {
        "value": 5,
        "weight": 1
      },
      "item-4661": {
        "value": 2,
        "weight": 3
      },
      "item-4662": {
        "value": 4,
        "weight": 1
      },
      "item-4663": {
        "value": 9,
        "weight": 6
      },
      "item-4664": {
        "value": 1,
        "weight": 9
      },
      "item-4665": {
        "value": 9,
        "weight": 6
      },
      "item-4666": {
        "value": 9,
        "weight": 1
      },
      "item-4667": {
        "value": 5,
        "weight": 8
      },
      "item-4668": {
        "value": 7,
        "weight": 3
      },
      "item-4669": {
        "value": 3,
        "weight": 2
      },
      "item-4670": {
        "value": 8,
        "weight": 1
      },
      "item-4671": {
        "value": 9,
        "weight": 5
      },
      "item-4672": {
        "value": 1,
        "weight": 8
      },
      "item-4673": {
        "value": 8,
        "weight": 9
      },
      "item-4674": {
        "value": 7,
        "weight": 9
      },
      "item-4675": {
        "value": 1,
        "weight": 6
      },
      "item-4676": {
        "value": 2,
        "weight": 2
      },
      "item-4677": {
        "value": 2,
        "weight": 1
      },
      "item-4678": {
        "value": 1,
        "weight": 4
      },
      "item-4679": {
        "value": 9,
        "weight": 3
      },
      "item-4680": {
        "value": 8,
        "weight": 2
      },
      "item-4681": {
        "value": 5,
        "weight": 7
      },
      "item-4682": {
        "value": 6,
        "weight": 1
      },
      "item-4683": {
        "value": 2,
        "weight": 8
      },
      "item-4684": {
        "value": 3,
        "weight": 7
      },
      "item-4685": {
        "value": 5,
        "weight": 3
      },
      "item-4686": {
        "value": 8,
        "weight": 6
      },
      "item-4687": {
        "value": 7,
        "weight": 3
      },
      "item-4688": {
        "value": 6,
        "weight": 3
      },
      "item-4689": {
        "value": 6,
        "weight": 3
      },
      "item-4690": {
        "value": 7,
        "weight": 9
      },
      "item-4691": {
        "value": 8,
        "weight": 4
      },
      "item-4692": {
        "value": 3,
        "weight": 3
      },
      "item-4693": {
        "value": 2,
        "weight": 3
      },
      "item-4694": {
        "value": 5,
        "weight": 5
      },
      "item-4695": {
        "value": 3,
        "weight": 9
      },
      "item-4696": {
        "value": 5,
        "weight": 9
      },
      "item-4697": {
        "value": 8,
        "weight": 1
      },
      "item-4698": {
        "value": 6,
        "weight": 2
      },
      "item-4699": {
        "value": 2,
        "weight": 9
      },
      "item-4700": {
        "value": 5,
        "weight": 5
      },
      "item-4701": {
        "value": 3,
        "weight": 6
      },
      "item-4702": {
        "value": 1,
        "weight": 4
      },
      "item-4703": {
        "value": 3,
        "weight": 9
      },
      "item-4704": {
        "value": 5,
        "weight": 4
      },
      "item-4705": {
        "value": 3,
        "weight": 9
      },
      "item-4706": {
        "value": 7,
        "weight": 1
      },
      "item-4707": {
        "value": 8,
        "weight": 1
      },
      "item-4708": {
        "value": 4,
        "weight": 9
      },
      "item-4709": {
        "value": 6,
        "weight": 3
      },
      "item-4710": {
        "value": 6,
        "weight": 9
      },
      "item-4711": {
        "value": 8,
        "weight": 1
      },
      "item-4712": {
        "value": 3,
        "weight": 2
      },
      "item-4713": {
        "value": 8,
        "weight": 4
      },
      "item-4714": {
        "value": 4,
        "weight": 8
      },
      "item-4715": {
        "value": 1,
        "weight": 1
      },
      "item-4716": {
        "value": 2,
        "weight": 1
      },
      "item-4717": {
        "value": 7,
        "weight": 3
      },
      "item-4718": {
        "value": 4,
        "weight": 5
      },
      "item-4719": {
        "value": 6,
        "weight": 6
      },
      "item-4720": {
        "value": 2,
        "weight": 3
      },
      "item-4721": {
        "value": 2,
        "weight": 2
      },
      "item-4722": {
        "value": 4,
        "weight": 3
      },
      "item-4723": {
        "value": 5,
        "weight": 7
      },
      "item-4724": {
        "value": 3,
        "weight": 1
      },
      "item-4725": {
        "value": 3,
        "weight": 3
      },
      "item-4726": {
        "value": 6,
        "weight": 4
      },
      "item-4727": {
        "value": 9,
        "weight": 7
      },
      "item-4728": {
        "value": 1,
        "weight": 9
      },
      "item-4729": {
        "value": 1,
        "weight": 8
      },
      "item-4730": {
        "value": 7,
        "weight": 8
      },
      "item-4731": {
        "value": 9,
        "weight": 8
      },
      "item-4732": {
        "value": 8,
        "weight": 8
      },
      "item-4733": {
        "value": 9,
        "weight": 2
      },
      "item-4734": {
        "value": 1,
        "weight": 4
      },
      "item-4735": {
        "value": 9,
        "weight": 9
      },
      "item-4736": {
        "value": 2,
        "weight": 8
      },
      "item-4737": {
        "value": 2,
        "weight": 2
      },
      "item-4738": {
        "value": 7,
        "weight": 3
      },
      "item-4739": {
        "value": 9,
        "weight": 6
      },
      "item-4740": {
        "value": 2,
        "weight": 2
      },
      "item-4741": {
        "value": 5,
        "weight": 6
      },
      "item-4742": {
        "value": 3,
        "weight": 2
      },
      "item-4743": {
        "value": 5,
        "weight": 4
      },
      "item-4744": {
        "value": 7,
        "weight": 2
      },
      "item-4745": {
        "value": 8,
        "weight": 2
      },
      "item-4746": {
        "value": 8,
        "weight": 3
      },
      "item-4747": {
        "value": 9,
        "weight": 5
      },
      "item-4748": {
        "value": 8,
        "weight": 7
      },
      "item-4749": {
        "value": 3,
        "weight": 6
      },
      "item-4750": {
        "value": 1,
        "weight": 3
      },
      "item-4751": {
        "value": 2,
        "weight": 8
      },
      "item-4752": {
        "value": 8,
        "weight": 4
      },
      "item-4753": {
        "value": 3,
        "weight": 2
      },
      "item-4754": {
        "value": 2,
        "weight": 6
      },
      "item-4755": {
        "value": 9,
        "weight": 3
      },
      "item-4756": {
        "value": 3,
        "weight": 6
      },
      "item-4757": {
        "value": 7,
        "weight": 5
      },
      "item-4758": {
        "value": 8,
        "weight": 6
      },
      "item-4759": {
        "value": 2,
        "weight": 6
      },
      "item-4760": {
        "value": 5,
        "weight": 9
      },
      "item-4761": {
        "value": 5,
        "weight": 1
      },
      "item-4762": {
        "value": 2,
        "weight": 1
      },
      "item-4763": {
        "value": 1,
        "weight": 4
      },
      "item-4764": {
        "value": 7,
        "weight": 7
      },
      "item-4765": {
        "value": 8,
        "weight": 9
      },
      "item-4766": {
        "value": 3,
        "weight": 5
      },
      "item-4767": {
        "value": 2,
        "weight": 9
      },
      "item-4768": {
        "value": 6,
        "weight": 7
      },
      "item-4769": {
        "value": 9,
        "weight": 5
      },
      "item-4770": {
        "value": 8,
        "weight": 1
      },
      "item-4771": {
        "value": 5,
        "weight": 2
      },
      "item-4772": {
        "value": 8,
        "weight": 2
      },
      "item-4773": {
        "value": 9,
        "weight": 8
      },
      "item-4774": {
        "value": 9,
        "weight": 5
      },
      "item-4775": {
        "value": 3,
        "weight": 8
      },
      "item-4776": {
        "value": 1,
        "weight": 1
      },
      "item-4777": {
        "value": 1,
        "weight": 8
      },
      "item-4778": {
        "value": 6,
        "weight": 2
      },
      "item-4779": {
        "value": 5,
        "weight": 6
      },
      "item-4780": {
        "value": 5,
        "weight": 8
      },
      "item-4781": {
        "value": 9,
        "weight": 5
      },
      "item-4782": {
        "value": 6,
        "weight": 7
      },
      "item-4783": {
        "value": 5,
        "weight": 7
      },
      "item-4784": {
        "value": 7,
        "weight": 9
      },
      "item-4785": {
        "value": 6,
        "weight": 6
      },
      "item-4786": {
        "value": 4,
        "weight": 7
      },
      "item-4787": {
        "value": 5,
        "weight": 5
      },
      "item-4788": {
        "value": 4,
        "weight": 7
      },
      "item-4789": {
        "value": 4,
        "weight": 8
      },
      "item-4790": {
        "value": 4,
        "weight": 5
      },
      "item-4791": {
        "value": 9,
        "weight": 7
      },
      "item-4792": {
        "value": 7,
        "weight": 3
      },
      "item-4793": {
        "value": 9,
        "weight": 1
      },
      "item-4794": {
        "value": 5,
        "weight": 5
      },
      "item-4795": {
        "value": 9,
        "weight": 2
      },
      "item-4796": {
        "value": 9,
        "weight": 7
      },
      "item-4797": {
        "value": 8,
        "weight": 3
      },
      "item-4798": {
        "value": 5,
        "weight": 3
      },
      "item-4799": {
        "value": 3,
        "weight": 7
      },
      "item-4800": {
        "value": 2,
        "weight": 2
      },
      "item-4801": {
        "value": 3,
        "weight": 1
      },
      "item-4802": {
        "value": 5,
        "weight": 6
      },
      "item-4803": {
        "value": 4,
        "weight": 7
      },
      "item-4804": {
        "value": 8,
        "weight": 9
      },
      "item-4805": {
        "value": 5,
        "weight": 3
      },
      "item-4806": {
        "value": 6,
        "weight": 4
      },
      "item-4807": {
        "value": 4,
        "weight": 3
      },
      "item-4808": {
        "value": 2,
        "weight": 1
      },
      "item-4809": {
        "value": 7,
        "weight": 8
      },
      "item-4810": {
        "value": 2,
        "weight": 1
      },
      "item-4811": {
        "value": 6,
        "weight": 4
      },
      "item-4812": {
        "value": 4,
        "weight": 8
      },
      "item-4813": {
        "value": 9,
        "weight": 8
      },
      "item-4814": {
        "value": 5,
        "weight": 6
      },
      "item-4815": {
        "value": 7,
        "weight": 6
      },
      "item-4816": {
        "value": 9,
        "weight": 3
      },
      "item-4817": {
        "value": 8,
        "weight": 6
      },
      "item-4818": {
        "value": 4,
        "weight": 7
      },
      "item-4819": {
        "value": 8,
        "weight": 2
      },
      "item-4820": {
        "value": 2,
        "weight": 8
      },
      "item-4821": {
        "value": 4,
        "weight": 9
      },
      "item-4822": {
        "value": 3,
        "weight": 1
      },
      "item-4823": {
        "value": 6,
        "weight": 7
      },
      "item-4824": {
        "value": 6,
        "weight": 5
      },
      "item-4825": {
        "value": 3,
        "weight": 1
      },
      "item-4826": {
        "value": 3,
        "weight": 4
      },
      "item-4827": {
        "value": 6,
        "weight": 8
      },
      "item-4828": {
        "value": 7,
        "weight": 8
      },
      "item-4829": {
        "value": 3,
        "weight": 3
      },
      "item-4830": {
        "value": 8,
        "weight": 7
      },
      "item-4831": {
        "value": 5,
        "weight": 8
      },
      "item-4832": {
        "value": 7,
        "weight": 3
      },
      "item-4833": {
        "value": 1,
        "weight": 9
      },
      "item-4834": {
        "value": 5,
        "weight": 3
      },
      "item-4835": {
        "value": 5,
        "weight": 6
      },
      "item-4836": {
        "value": 2,
        "weight": 9
      },
      "item-4837": {
        "value": 9,
        "weight": 6
      },
      "item-4838": {
        "value": 6,
        "weight": 7
      },
      "item-4839": {
        "value": 8,
        "weight": 1
      },
      "item-4840": {
        "value": 4,
        "weight": 7
      },
      "item-4841": {
        "value": 1,
        "weight": 9
      },
      "item-4842": {
        "value": 7,
        "weight": 5
      },
      "item-4843": {
        "value": 8,
        "weight": 8
      },
      "item-4844": {
        "value": 3,
        "weight": 6
      },
      "item-4845": {
        "value": 8,
        "weight": 3
      },
      "item-4846": {
        "value": 2,
        "weight": 2
      },
      "item-4847": {
        "value": 7,
        "weight": 8
      },
      "item-4848": {
        "value": 6,
        "weight": 6
      },
      "item-4849": {
        "value": 2,
        "weight": 7
      },
      "item-4850": {
        "value": 9,
        "weight": 9
      },
      "item-4851": {
        "value": 8,
        "weight": 6
      },
      "item-4852": {
        "value": 6,
        "weight": 5
      },
      "item-4853": {
        "value": 5,
        "weight": 2
      },
      "item-4854": {
        "value": 8,
        "weight": 5
      },
      "item-4855": {
        "value": 2,
        "weight": 4
      },
      "item-4856": {
        "value": 3,
        "weight": 8
      },
      "item-4857": {
        "value": 1,
        "weight": 7
      },
      "item-4858": {
        "value": 2,
        "weight": 3
      },
      "item-4859": {
        "value": 2,
        "weight": 3
      },
      "item-4860": {
        "value": 4,
        "weight": 2
      },
      "item-4861": {
        "value": 4,
        "weight": 1
      },
      "item-4862": {
        "value": 4,
        "weight": 5
      },
      "item-4863": {
        "value": 7,
        "weight": 8
      },
      "item-4864": {
        "value": 6,
        "weight": 4
      },
      "item-4865": {
        "value": 2,
        "weight": 6
      },
      "item-4866": {
        "value": 4,
        "weight": 9
      },
      "item-4867": {
        "value": 6,
        "weight": 7
      },
      "item-4868": {
        "value": 3,
        "weight": 4
      },
      "item-4869": {
        "value": 3,
        "weight": 9
      },
      "item-4870": {
        "value": 8,
        "weight": 3
      },
      "item-4871": {
        "value": 4,
        "weight": 9
      },
      "item-4872": {
        "value": 6,
        "weight": 9
      },
      "item-4873": {
        "value": 6,
        "weight": 5
      },
      "item-4874": {
        "value": 3,
        "weight": 2
      },
      "item-4875": {
        "value": 4,
        "weight": 5
      },
      "item-4876": {
        "value": 6,
        "weight": 8
      },
      "item-4877": {
        "value": 7,
        "weight": 8
      },
      "item-4878": {
        "value": 1,
        "weight": 2
      },
      "item-4879": {
        "value": 8,
        "weight": 5
      },
      "item-4880": {
        "value": 2,
        "weight": 3
      },
      "item-4881": {
        "value": 8,
        "weight": 6
      },
      "item-4882": {
        "value": 2,
        "weight": 2
      },
      "item-4883": {
        "value": 2,
        "weight": 5
      },
      "item-4884": {
        "value": 4,
        "weight": 4
      },
      "item-4885": {
        "value": 9,
        "weight": 1
      },
      "item-4886": {
        "value": 4,
        "weight": 6
      },
      "item-4887": {
        "value": 4,
        "weight": 1
      },
      "item-4888": {
        "value": 2,
        "weight": 3
      },
      "item-4889": {
        "value": 1,
        "weight": 2
      },
      "item-4890": {
        "value": 1,
        "weight": 3
      },
      "item-4891": {
        "value": 3,
        "weight": 9
      },
      "item-4892": {
        "value": 6,
        "weight": 9
      },
      "item-4893": {
        "value": 5,
        "weight": 5
      },
      "item-4894": {
        "value": 3,
        "weight": 4
      },
      "item-4895": {
        "value": 9,
        "weight": 1
      },
      "item-4896": {
        "value": 6,
        "weight": 3
      },
      "item-4897": {
        "value": 1,
        "weight": 4
      },
      "item-4898": {
        "value": 2,
        "weight": 3
      },
      "item-4899": {
        "value": 4,
        "weight": 8
      },
      "item-4900": {
        "value": 8,
        "weight": 6
      },
      "item-4901": {
        "value": 1,
        "weight": 7
      },
      "item-4902": {
        "value": 1,
        "weight": 9
      },
      "item-4903": {
        "value": 2,
        "weight": 7
      },
      "item-4904": {
        "value": 3,
        "weight": 4
      },
      "item-4905": {
        "value": 7,
        "weight": 2
      },
      "item-4906": {
        "value": 8,
        "weight": 2
      },
      "item-4907": {
        "value": 5,
        "weight": 8
      },
      "item-4908": {
        "value": 9,
        "weight": 2
      },
      "item-4909": {
        "value": 7,
        "weight": 7
      },
      "item-4910": {
        "value": 1,
        "weight": 5
      },
      "item-4911": {
        "value": 9,
        "weight": 3
      },
      "item-4912": {
        "value": 1,
        "weight": 4
      },
      "item-4913": {
        "value": 8,
        "weight": 9
      },
      "item-4914": {
        "value": 1,
        "weight": 9
      },
      "item-4915": {
        "value": 6,
        "weight": 1
      },
      "item-4916": {
        "value": 5,
        "weight": 2
      },
      "item-4917": {
        "value": 7,
        "weight": 4
      },
      "item-4918": {
        "value": 7,
        "weight": 7
      },
      "item-4919": {
        "value": 8,
        "weight": 2
      },
      "item-4920": {
        "value": 1,
        "weight": 9
      },
      "item-4921": {
        "value": 2,
        "weight": 7
      },
      "item-4922": {
        "value": 8,
        "weight": 6
      },
      "item-4923": {
        "value": 5,
        "weight": 8
      },
      "item-4924": {
        "value": 5,
        "weight": 4
      },
      "item-4925": {
        "value": 6,
        "weight": 1
      },
      "item-4926": {
        "value": 3,
        "weight": 2
      },
      "item-4927": {
        "value": 4,
        "weight": 7
      },
      "item-4928": {
        "value": 9,
        "weight": 7
      },
      "item-4929": {
        "value": 1,
        "weight": 4
      },
      "item-4930": {
        "value": 4,
        "weight": 6
      },
      "item-4931": {
        "value": 2,
        "weight": 8
      },
      "item-4932": {
        "value": 3,
        "weight": 7
      },
      "item-4933": {
        "value": 4,
        "weight": 5
      },
      "item-4934": {
        "value": 1,
        "weight": 8
      },
      "item-4935": {
        "value": 7,
        "weight": 4
      },
      "item-4936": {
        "value": 2,
        "weight": 8
      },
      "item-4937": {
        "value": 2,
        "weight": 7
      },
      "item-4938": {
        "value": 9,
        "weight": 5
      },
      "item-4939": {
        "value": 1,
        "weight": 6
      },
      "item-4940": {
        "value": 6,
        "weight": 7
      },
      "item-4941": {
        "value": 2,
        "weight": 3
      },
      "item-4942": {
        "value": 4,
        "weight": 5
      },
      "item-4943": {
        "value": 7,
        "weight": 3
      },
      "item-4944": {
        "value": 5,
        "weight": 8
      },
      "item-4945": {
        "value": 2,
        "weight": 5
      },
      "item-4946": {
        "value": 7,
        "weight": 5
      },
      "item-4947": {
        "value": 9,
        "weight": 5
      },
      "item-4948": {
        "value": 7,
        "weight": 4
      },
      "item-4949": {
        "value": 5,
        "weight": 2
      },
      "item-4950": {
        "value": 8,
        "weight": 2
      },
      "item-4951": {
        "value": 5,
        "weight": 5
      },
      "item-4952": {
        "value": 7,
        "weight": 6
      },
      "item-4953": {
        "value": 9,
        "weight": 5
      },
      "item-4954": {
        "value": 8,
        "weight": 5
      },
      "item-4955": {
        "value": 4,
        "weight": 8
      },
      "item-4956": {
        "value": 3,
        "weight": 4
      },
      "item-4957": {
        "value": 8,
        "weight": 4
      },
      "item-4958": {
        "value": 2,
        "weight": 9
      },
      "item-4959": {
        "value": 7,
        "weight": 4
      },
      "item-4960": {
        "value": 1,
        "weight": 3
      },
      "item-4961": {
        "value": 7,
        "weight": 4
      },
      "item-4962": {
        "value": 2,
        "weight": 9
      },
      "item-4963": {
        "value": 5,
        "weight": 9
      },
      "item-4964": {
        "value": 8,
        "weight": 2
      },
      "item-4965": {
        "value": 7,
        "weight": 3
      },
      "item-4966": {
        "value": 9,
        "weight": 4
      },
      "item-4967": {
        "value": 5,
        "weight": 1
      },
      "item-4968": {
        "value": 4,
        "weight": 2
      },
      "item-4969": {
        "value": 8,
        "weight": 4
      },
      "item-4970": {
        "value": 8,
        "weight": 8
      },
      "item-4971": {
        "value": 7,
        "weight": 5
      },
      "item-4972": {
        "value": 8,
        "weight": 5
      },
      "item-4973": {
        "value": 1,
        "weight": 2
      },
      "item-4974": {
        "value": 2,
        "weight": 4
      },
      "item-4975": {
        "value": 3,
        "weight": 2
      },
      "item-4976": {
        "value": 4,
        "weight": 4
      },
      "item-4977": {
        "value": 5,
        "weight": 6
      },
      "item-4978": {
        "value": 2,
        "weight": 8
      },
      "item-4979": {
        "value": 8,
        "weight": 2
      },
      "item-4980": {
        "value": 1,
        "weight": 6
      },
      "item-4981": {
        "value": 8,
        "weight": 1
      },
      "item-4982": {
        "value": 2,
        "weight": 4
      },
      "item-4983": {
        "value": 1,
        "weight": 5
      },
      "item-4984": {
        "value": 6,
        "weight": 3
      },
      "item-4985": {
        "value": 5,
        "weight": 9
      },
      "item-4986": {
        "value": 5,
        "weight": 2
      },
      "item-4987": {
        "value": 2,
        "weight": 3
      },
      "item-4988": {
        "value": 4,
        "weight": 5
      },
      "item-4989": {
        "value": 4,
        "weight": 3
      },
      "item-4990": {
        "value": 9,
        "weight": 1
      },
      "item-4991": {
        "value": 4,
        "weight": 4
      },
      "item-4992": {
        "value": 5,
        "weight": 3
      },
      "item-4993": {
        "value": 3,
        "weight": 1
      },
      "item-4994": {
        "value": 3,
        "weight": 8
      },
      "item-4995": {
        "value": 4,
        "weight": 8
      },
      "item-4996": {
        "value": 6,
        "weight": 8
      },
      "item-4997": {
        "value": 4,
        "weight": 6
      },
      "item-4998": {
        "value": 7,
        "weight": 8
      },
      "item-4999": {
        "value": 9,
        "weight": 3
      },
      "item-5000": {
        "value": 9,
        "weight": 4
      },
      "item-5001": {
        "value": 6,
        "weight": 8
      },
      "item-5002": {
        "value": 3,
        "weight": 8
      },
      "item-5003": {
        "value": 9,
        "weight": 2
      },
      "item-5004": {
        "value": 8,
        "weight": 9
      },
      "item-5005": {
        "value": 7,
        "weight": 8
      },
      "item-5006": {
        "value": 1,
        "weight": 7
      },
      "item-5007": {
        "value": 7,
        "weight": 3
      },
      "item-5008": {
        "value": 6,
        "weight": 2
      },
      "item-5009": {
        "value": 6,
        "weight": 3
      },
      "item-5010": {
        "value": 5,
        "weight": 6
      },
      "item-5011": {
        "value": 6,
        "weight": 2
      },
      "item-5012": {
        "value": 2,
        "weight": 7
      },
      "item-5013": {
        "value": 7,
        "weight": 3
      },
      "item-5014": {
        "value": 5,
        "weight": 8
      },
      "item-5015": {
        "value": 8,
        "weight": 1
      },
      "item-5016": {
        "value": 5,
        "weight": 9
      },
      "item-5017": {
        "value": 9,
        "weight": 2
      },
      "item-5018": {
        "value": 9,
        "weight": 2
      },
      "item-5019": {
        "value": 8,
        "weight": 8
      },
      "item-5020": {
        "value": 3,
        "weight": 6
      },
      "item-5021": {
        "value": 7,
        "weight": 3
      },
      "item-5022": {
        "value": 4,
        "weight": 2
      },
      "item-5023": {
        "value": 6,
        "weight": 3
      },
      "item-5024": {
        "value": 9,
        "weight": 3
      },
      "item-5025": {
        "value": 7,
        "weight": 1
      },
      "item-5026": {
        "value": 1,
        "weight": 9
      },
      "item-5027": {
        "value": 9,
        "weight": 2
      },
      "item-5028": {
        "value": 5,
        "weight": 3
      },
      "item-5029": {
        "value": 2,
        "weight": 2
      },
      "item-5030": {
        "value": 8,
        "weight": 5
      },
      "item-5031": {
        "value": 8,
        "weight": 5
      },
      "item-5032": {
        "value": 9,
        "weight": 8
      },
      "item-5033": {
        "value": 3,
        "weight": 1
      },
      "item-5034": {
        "value": 7,
        "weight": 8
      },
      "item-5035": {
        "value": 5,
        "weight": 9
      },
      "item-5036": {
        "value": 9,
        "weight": 3
      },
      "item-5037": {
        "value": 9,
        "weight": 4
      },
      "item-5038": {
        "value": 5,
        "weight": 5
      },
      "item-5039": {
        "value": 6,
        "weight": 6
      },
      "item-5040": {
        "value": 3,
        "weight": 4
      },
      "item-5041": {
        "value": 4,
        "weight": 8
      },
      "item-5042": {
        "value": 2,
        "weight": 9
      },
      "item-5043": {
        "value": 5,
        "weight": 9
      },
      "item-5044": {
        "value": 5,
        "weight": 5
      },
      "item-5045": {
        "value": 1,
        "weight": 8
      },
      "item-5046": {
        "value": 8,
        "weight": 1
      },
      "item-5047": {
        "value": 8,
        "weight": 7
      },
      "item-5048": {
        "value": 8,
        "weight": 4
      },
      "item-5049": {
        "value": 6,
        "weight": 1
      },
      "item-5050": {
        "value": 9,
        "weight": 6
      },
      "item-5051": {
        "value": 9,
        "weight": 1
      },
      "item-5052": {
        "value": 8,
        "weight": 9
      },
      "item-5053": {
        "value": 4,
        "weight": 3
      },
      "item-5054": {
        "value": 1,
        "weight": 8
      },
      "item-5055": {
        "value": 2,
        "weight": 4
      },
      "item-5056": {
        "value": 3,
        "weight": 7
      },
      "item-5057": {
        "value": 4,
        "weight": 2
      },
      "item-5058": {
        "value": 3,
        "weight": 3
      },
      "item-5059": {
        "value": 5,
        "weight": 1
      },
      "item-5060": {
        "value": 3,
        "weight": 6
      },
      "item-5061": {
        "value": 7,
        "weight": 8
      },
      "item-5062": {
        "value": 9,
        "weight": 7
      },
      "item-5063": {
        "value": 1,
        "weight": 5
      },
      "item-5064": {
        "value": 3,
        "weight": 2
      },
      "item-5065": {
        "value": 8,
        "weight": 5
      },
      "item-5066": {
        "value": 7,
        "weight": 2
      },
      "item-5067": {
        "value": 9,
        "weight": 4
      },
      "item-5068": {
        "value": 5,
        "weight": 2
      },
      "item-5069": {
        "value": 3,
        "weight": 6
      },
      "item-5070": {
        "value": 5,
        "weight": 7
      },
      "item-5071": {
        "value": 9,
        "weight": 3
      },
      "item-5072": {
        "value": 7,
        "weight": 8
      },
      "item-5073": {
        "value": 4,
        "weight": 7
      },
      "item-5074": {
        "value": 6,
        "weight": 6
      },
      "item-5075": {
        "value": 6,
        "weight": 1
      },
      "item-5076": {
        "value": 6,
        "weight": 8
      },
      "item-5077": {
        "value": 8,
        "weight": 9
      },
      "item-5078": {
        "value": 1,
        "weight": 5
      },
      "item-5079": {
        "value": 5,
        "weight": 2
      },
      "item-5080": {
        "value": 7,
        "weight": 1
      },
      "item-5081": {
        "value": 2,
        "weight": 1
      },
      "item-5082": {
        "value": 4,
        "weight": 4
      },
      "item-5083": {
        "value": 3,
        "weight": 4
      },
      "item-5084": {
        "value": 3,
        "weight": 2
      },
      "item-5085": {
        "value": 5,
        "weight": 7
      },
      "item-5086": {
        "value": 4,
        "weight": 9
      },
      "item-5087": {
        "value": 6,
        "weight": 3
      },
      "item-5088": {
        "value": 9,
        "weight": 7
      },
      "item-5089": {
        "value": 9,
        "weight": 8
      },
      "item-5090": {
        "value": 7,
        "weight": 4
      },
      "item-5091": {
        "value": 5,
        "weight": 8
      },
      "item-5092": {
        "value": 7,
        "weight": 2
      },
      "item-5093": {
        "value": 1,
        "weight": 5
      },
      "item-5094": {
        "value": 9,
        "weight": 1
      },
      "item-5095": {
        "value": 8,
        "weight": 8
      },
      "item-5096": {
        "value": 5,
        "weight": 1
      },
      "item-5097": {
        "value": 9,
        "weight": 6
      },
      "item-5098": {
        "value": 7,
        "weight": 2
      },
      "item-5099": {
        "value": 7,
        "weight": 5
      },
      "item-5100": {
        "value": 4,
        "weight": 1
      },
      "item-5101": {
        "value": 7,
        "weight": 6
      },
      "item-5102": {
        "value": 7,
        "weight": 1
      },
      "item-5103": {
        "value": 9,
        "weight": 4
      },
      "item-5104": {
        "value": 7,
        "weight": 4
      },
      "item-5105": {
        "value": 5,
        "weight": 6
      },
      "item-5106": {
        "value": 7,
        "weight": 2
      },
      "item-5107": {
        "value": 4,
        "weight": 8
      },
      "item-5108": {
        "value": 1,
        "weight": 3
      },
      "item-5109": {
        "value": 5,
        "weight": 7
      },
      "item-5110": {
        "value": 9,
        "weight": 2
      },
      "item-5111": {
        "value": 6,
        "weight": 9
      },
      "item-5112": {
        "value": 1,
        "weight": 2
      },
      "item-5113": {
        "value": 7,
        "weight": 5
      },
      "item-5114": {
        "value": 4,
        "weight": 8
      },
      "item-5115": {
        "value": 6,
        "weight": 3
      },
      "item-5116": {
        "value": 7,
        "weight": 7
      },
      "item-5117": {
        "value": 1,
        "weight": 5
      },
      "item-5118": {
        "value": 8,
        "weight": 3
      },
      "item-5119": {
        "value": 1,
        "weight": 7
      },
      "item-5120": {
        "value": 4,
        "weight": 3
      },
      "item-5121": {
        "value": 4,
        "weight": 7
      },
      "item-5122": {
        "value": 4,
        "weight": 4
      },
      "item-5123": {
        "value": 8,
        "weight": 5
      },
      "item-5124": {
        "value": 9,
        "weight": 9
      },
      "item-5125": {
        "value": 8,
        "weight": 2
      },
      "item-5126": {
        "value": 3,
        "weight": 2
      },
      "item-5127": {
        "value": 6,
        "weight": 2
      },
      "item-5128": {
        "value": 3,
        "weight": 5
      },
      "item-5129": {
        "value": 3,
        "weight": 6
      },
      "item-5130": {
        "value": 4,
        "weight": 8
      },
      "item-5131": {
        "value": 1,
        "weight": 1
      },
      "item-5132": {
        "value": 9,
        "weight": 3
      },
      "item-5133": {
        "value": 1,
        "weight": 7
      },
      "item-5134": {
        "value": 2,
        "weight": 1
      },
      "item-5135": {
        "value": 1,
        "weight": 1
      },
      "item-5136": {
        "value": 2,
        "weight": 2
      },
      "item-5137": {
        "value": 7,
        "weight": 2
      },
      "item-5138": {
        "value": 4,
        "weight": 8
      },
      "item-5139": {
        "value": 2,
        "weight": 9
      },
      "item-5140": {
        "value": 9,
        "weight": 8
      },
      "item-5141": {
        "value": 9,
        "weight": 1
      },
      "item-5142": {
        "value": 2,
        "weight": 1
      },
      "item-5143": {
        "value": 6,
        "weight": 2
      },
      "item-5144": {
        "value": 8,
        "weight": 2
      },
      "item-5145": {
        "value": 6,
        "weight": 3
      },
      "item-5146": {
        "value": 3,
        "weight": 1
      },
      "item-5147": {
        "value": 3,
        "weight": 8
      },
      "item-5148": {
        "value": 4,
        "weight": 4
      },
      "item-5149": {
        "value": 5,
        "weight": 8
      },
      "item-5150": {
        "value": 5,
        "weight": 8
      },
      "item-5151": {
        "value": 2,
        "weight": 8
      },
      "item-5152": {
        "value": 8,
        "weight": 6
      },
      "item-5153": {
        "value": 9,
        "weight": 3
      },
      "item-5154": {
        "value": 4,
        "weight": 2
      },
      "item-5155": {
        "value": 2,
        "weight": 3
      },
      "item-5156": {
        "value": 6,
        "weight": 1
      },
      "item-5157": {
        "value": 9,
        "weight": 4
      },
      "item-5158": {
        "value": 7,
        "weight": 1
      },
      "item-5159": {
        "value": 4,
        "weight": 9
      },
      "item-5160": {
        "value": 5,
        "weight": 3
      },
      "item-5161": {
        "value": 7,
        "weight": 8
      },
      "item-5162": {
        "value": 9,
        "weight": 7
      },
      "item-5163": {
        "value": 8,
        "weight": 8
      },
      "item-5164": {
        "value": 4,
        "weight": 8
      },
      "item-5165": {
        "value": 2,
        "weight": 9
      },
      "item-5166": {
        "value": 1,
        "weight": 7
      },
      "item-5167": {
        "value": 6,
        "weight": 9
      },
      "item-5168": {
        "value": 4,
        "weight": 3
      },
      "item-5169": {
        "value": 7,
        "weight": 7
      },
      "item-5170": {
        "value": 6,
        "weight": 7
      },
      "item-5171": {
        "value": 3,
        "weight": 9
      },
      "item-5172": {
        "value": 4,
        "weight": 7
      },
      "item-5173": {
        "value": 3,
        "weight": 6
      },
      "item-5174": {
        "value": 4,
        "weight": 7
      },
      "item-5175": {
        "value": 3,
        "weight": 4
      },
      "item-5176": {
        "value": 5,
        "weight": 5
      },
      "item-5177": {
        "value": 7,
        "weight": 7
      },
      "item-5178": {
        "value": 2,
        "weight": 7
      },
      "item-5179": {
        "value": 4,
        "weight": 6
      },
      "item-5180": {
        "value": 4,
        "weight": 4
      },
      "item-5181": {
        "value": 7,
        "weight": 4
      },
      "item-5182": {
        "value": 1,
        "weight": 4
      },
      "item-5183": {
        "value": 1,
        "weight": 7
      },
      "item-5184": {
        "value": 6,
        "weight": 8
      },
      "item-5185": {
        "value": 2,
        "weight": 6
      },
      "item-5186": {
        "value": 6,
        "weight": 2
      },
      "item-5187": {
        "value": 3,
        "weight": 7
      },
      "item-5188": {
        "value": 2,
        "weight": 2
      },
      "item-5189": {
        "value": 4,
        "weight": 4
      },
      "item-5190": {
        "value": 6,
        "weight": 6
      },
      "item-5191": {
        "value": 4,
        "weight": 8
      },
      "item-5192": {
        "value": 6,
        "weight": 7
      },
      "item-5193": {
        "value": 6,
        "weight": 2
      },
      "item-5194": {
        "value": 1,
        "weight": 6
      },
      "item-5195": {
        "value": 1,
        "weight": 5
      },
      "item-5196": {
        "value": 8,
        "weight": 8
      },
      "item-5197": {
        "value": 2,
        "weight": 7
      },
      "item-5198": {
        "value": 2,
        "weight": 8
      },
      "item-5199": {
        "value": 2,
        "weight": 4
      },
      "item-5200": {
        "value": 5,
        "weight": 7
      },
      "item-5201": {
        "value": 6,
        "weight": 9
      },
      "item-5202": {
        "value": 7,
        "weight": 2
      },
      "item-5203": {
        "value": 3,
        "weight": 7
      },
      "item-5204": {
        "value": 1,
        "weight": 4
      },
      "item-5205": {
        "value": 6,
        "weight": 8
      },
      "item-5206": {
        "value": 2,
        "weight": 4
      },
      "item-5207": {
        "value": 3,
        "weight": 8
      },
      "item-5208": {
        "value": 9,
        "weight": 1
      },
      "item-5209": {
        "value": 7,
        "weight": 6
      },
      "item-5210": {
        "value": 2,
        "weight": 9
      },
      "item-5211": {
        "value": 9,
        "weight": 7
      },
      "item-5212": {
        "value": 3,
        "weight": 5
      },
      "item-5213": {
        "value": 1,
        "weight": 1
      },
      "item-5214": {
        "value": 4,
        "weight": 2
      },
      "item-5215": {
        "value": 3,
        "weight": 9
      },
      "item-5216": {
        "value": 4,
        "weight": 2
      },
      "item-5217": {
        "value": 8,
        "weight": 7
      },
      "item-5218": {
        "value": 6,
        "weight": 7
      },
      "item-5219": {
        "value": 4,
        "weight": 4
      },
      "item-5220": {
        "value": 4,
        "weight": 3
      },
      "item-5221": {
        "value": 3,
        "weight": 7
      },
      "item-5222": {
        "value": 3,
        "weight": 9
      },
      "item-5223": {
        "value": 8,
        "weight": 8
      },
      "item-5224": {
        "value": 4,
        "weight": 4
      },
      "item-5225": {
        "value": 7,
        "weight": 9
      },
      "item-5226": {
        "value": 9,
        "weight": 5
      },
      "item-5227": {
        "value": 9,
        "weight": 3
      },
      "item-5228": {
        "value": 4,
        "weight": 6
      },
      "item-5229": {
        "value": 4,
        "weight": 3
      },
      "item-5230": {
        "value": 1,
        "weight": 3
      },
      "item-5231": {
        "value": 7,
        "weight": 5
      },
      "item-5232": {
        "value": 5,
        "weight": 3
      },
      "item-5233": {
        "value": 9,
        "weight": 2
      },
      "item-5234": {
        "value": 6,
        "weight": 5
      },
      "item-5235": {
        "value": 7,
        "weight": 6
      },
      "item-5236": {
        "value": 1,
        "weight": 7
      },
      "item-5237": {
        "value": 3,
        "weight": 8
      },
      "item-5238": {
        "value": 4,
        "weight": 6
      },
      "item-5239": {
        "value": 9,
        "weight": 5
      },
      "item-5240": {
        "value": 4,
        "weight": 3
      },
      "item-5241": {
        "value": 8,
        "weight": 8
      },
      "item-5242": {
        "value": 1,
        "weight": 3
      },
      "item-5243": {
        "value": 9,
        "weight": 8
      },
      "item-5244": {
        "value": 2,
        "weight": 4
      },
      "item-5245": {
        "value": 1,
        "weight": 9
      },
      "item-5246": {
        "value": 1,
        "weight": 8
      },
      "item-5247": {
        "value": 1,
        "weight": 4
      },
      "item-5248": {
        "value": 2,
        "weight": 3
      },
      "item-5249": {
        "value": 7,
        "weight": 1
      },
      "item-5250": {
        "value": 1,
        "weight": 3
      },
      "item-5251": {
        "value": 8,
        "weight": 5
      },
      "item-5252": {
        "value": 7,
        "weight": 7
      },
      "item-5253": {
        "value": 8,
        "weight": 2
      },
      "item-5254": {
        "value": 5,
        "weight": 7
      },
      "item-5255": {
        "value": 1,
        "weight": 5
      },
      "item-5256": {
        "value": 5,
        "weight": 9
      },
      "item-5257": {
        "value": 2,
        "weight": 2
      },
      "item-5258": {
        "value": 7,
        "weight": 7
      },
      "item-5259": {
        "value": 8,
        "weight": 8
      },
      "item-5260": {
        "value": 1,
        "weight": 9
      },
      "item-5261": {
        "value": 5,
        "weight": 5
      },
      "item-5262": {
        "value": 6,
        "weight": 7
      },
      "item-5263": {
        "value": 6,
        "weight": 8
      },
      "item-5264": {
        "value": 3,
        "weight": 4
      },
      "item-5265": {
        "value": 6,
        "weight": 7
      },
      "item-5266": {
        "value": 5,
        "weight": 8
      },
      "item-5267": {
        "value": 1,
        "weight": 5
      },
      "item-5268": {
        "value": 1,
        "weight": 3
      },
      "item-5269": {
        "value": 5,
        "weight": 6
      },
      "item-5270": {
        "value": 3,
        "weight": 1
      },
      "item-5271": {
        "value": 3,
        "weight": 9
      },
      "item-5272": {
        "value": 5,
        "weight": 5
      },
      "item-5273": {
        "value": 3,
        "weight": 9
      },
      "item-5274": {
        "value": 3,
        "weight": 6
      },
      "item-5275": {
        "value": 4,
        "weight": 9
      },
      "item-5276": {
        "value": 5,
        "weight": 9
      },
      "item-5277": {
        "value": 9,
        "weight": 8
      },
      "item-5278": {
        "value": 3,
        "weight": 2
      },
      "item-5279": {
        "value": 2,
        "weight": 4
      },
      "item-5280": {
        "value": 4,
        "weight": 2
      },
      "item-5281": {
        "value": 5,
        "weight": 3
      },
      "item-5282": {
        "value": 2,
        "weight": 1
      },
      "item-5283": {
        "value": 8,
        "weight": 1
      },
      "item-5284": {
        "value": 9,
        "weight": 6
      },
      "item-5285": {
        "value": 1,
        "weight": 5
      },
      "item-5286": {
        "value": 7,
        "weight": 6
      },
      "item-5287": {
        "value": 3,
        "weight": 8
      },
      "item-5288": {
        "value": 4,
        "weight": 1
      },
      "item-5289": {
        "value": 1,
        "weight": 5
      },
      "item-5290": {
        "value": 6,
        "weight": 7
      },
      "item-5291": {
        "value": 4,
        "weight": 1
      },
      "item-5292": {
        "value": 4,
        "weight": 6
      },
      "item-5293": {
        "value": 8,
        "weight": 4
      },
      "item-5294": {
        "value": 2,
        "weight": 7
      },
      "item-5295": {
        "value": 1,
        "weight": 5
      },
      "item-5296": {
        "value": 6,
        "weight": 4
      },
      "item-5297": {
        "value": 5,
        "weight": 9
      },
      "item-5298": {
        "value": 5,
        "weight": 2
      },
      "item-5299": {
        "value": 5,
        "weight": 7
      },
      "item-5300": {
        "value": 3,
        "weight": 9
      },
      "item-5301": {
        "value": 4,
        "weight": 5
      },
      "item-5302": {
        "value": 1,
        "weight": 6
      },
      "item-5303": {
        "value": 8,
        "weight": 8
      },
      "item-5304": {
        "value": 6,
        "weight": 8
      },
      "item-5305": {
        "value": 7,
        "weight": 1
      },
      "item-5306": {
        "value": 9,
        "weight": 3
      },
      "item-5307": {
        "value": 7,
        "weight": 8
      },
      "item-5308": {
        "value": 5,
        "weight": 1
      },
      "item-5309": {
        "value": 4,
        "weight": 4
      },
      "item-5310": {
        "value": 2,
        "weight": 9
      },
      "item-5311": {
        "value": 7,
        "weight": 2
      },
      "item-5312": {
        "value": 1,
        "weight": 4
      },
      "item-5313": {
        "value": 2,
        "weight": 4
      },
      "item-5314": {
        "value": 7,
        "weight": 9
      },
      "item-5315": {
        "value": 4,
        "weight": 6
      },
      "item-5316": {
        "value": 7,
        "weight": 4
      },
      "item-5317": {
        "value": 5,
        "weight": 5
      },
      "item-5318": {
        "value": 3,
        "weight": 7
      },
      "item-5319": {
        "value": 9,
        "weight": 7
      },
      "item-5320": {
        "value": 4,
        "weight": 5
      },
      "item-5321": {
        "value": 9,
        "weight": 5
      },
      "item-5322": {
        "value": 9,
        "weight": 1
      },
      "item-5323": {
        "value": 4,
        "weight": 4
      },
      "item-5324": {
        "value": 3,
        "weight": 1
      },
      "item-5325": {
        "value": 1,
        "weight": 2
      },
      "item-5326": {
        "value": 6,
        "weight": 2
      },
      "item-5327": {
        "value": 6,
        "weight": 9
      },
      "item-5328": {
        "value": 7,
        "weight": 7
      },
      "item-5329": {
        "value": 8,
        "weight": 6
      },
      "item-5330": {
        "value": 9,
        "weight": 7
      },
      "item-5331": {
        "value": 5,
        "weight": 4
      },
      "item-5332": {
        "value": 5,
        "weight": 6
      },
      "item-5333": {
        "value": 4,
        "weight": 3
      },
      "item-5334": {
        "value": 6,
        "weight": 1
      },
      "item-5335": {
        "value": 2,
        "weight": 1
      },
      "item-5336": {
        "value": 9,
        "weight": 7
      },
      "item-5337": {
        "value": 8,
        "weight": 2
      },
      "item-5338": {
        "value": 3,
        "weight": 3
      },
      "item-5339": {
        "value": 8,
        "weight": 9
      },
      "item-5340": {
        "value": 6,
        "weight": 1
      },
      "item-5341": {
        "value": 8,
        "weight": 4
      },
      "item-5342": {
        "value": 7,
        "weight": 7
      },
      "item-5343": {
        "value": 2,
        "weight": 3
      },
      "item-5344": {
        "value": 7,
        "weight": 5
      },
      "item-5345": {
        "value": 7,
        "weight": 6
      },
      "item-5346": {
        "value": 7,
        "weight": 9
      },
      "item-5347": {
        "value": 1,
        "weight": 8
      },
      "item-5348": {
        "value": 2,
        "weight": 3
      },
      "item-5349": {
        "value": 4,
        "weight": 4
      },
      "item-5350": {
        "value": 5,
        "weight": 1
      },
      "item-5351": {
        "value": 2,
        "weight": 2
      },
      "item-5352": {
        "value": 3,
        "weight": 6
      },
      "item-5353": {
        "value": 4,
        "weight": 5
      },
      "item-5354": {
        "value": 2,
        "weight": 1
      },
      "item-5355": {
        "value": 7,
        "weight": 9
      },
      "item-5356": {
        "value": 4,
        "weight": 7
      },
      "item-5357": {
        "value": 2,
        "weight": 7
      },
      "item-5358": {
        "value": 4,
        "weight": 1
      },
      "item-5359": {
        "value": 7,
        "weight": 3
      },
      "item-5360": {
        "value": 2,
        "weight": 3
      },
      "item-5361": {
        "value": 1,
        "weight": 7
      },
      "item-5362": {
        "value": 1,
        "weight": 4
      },
      "item-5363": {
        "value": 9,
        "weight": 1
      },
      "item-5364": {
        "value": 6,
        "weight": 8
      },
      "item-5365": {
        "value": 8,
        "weight": 7
      },
      "item-5366": {
        "value": 6,
        "weight": 2
      },
      "item-5367": {
        "value": 5,
        "weight": 1
      },
      "item-5368": {
        "value": 3,
        "weight": 5
      },
      "item-5369": {
        "value": 8,
        "weight": 8
      },
      "item-5370": {
        "value": 1,
        "weight": 4
      },
      "item-5371": {
        "value": 9,
        "weight": 8
      },
      "item-5372": {
        "value": 5,
        "weight": 2
      },
      "item-5373": {
        "value": 8,
        "weight": 8
      },
      "item-5374": {
        "value": 3,
        "weight": 7
      },
      "item-5375": {
        "value": 3,
        "weight": 7
      },
      "item-5376": {
        "value": 7,
        "weight": 6
      },
      "item-5377": {
        "value": 3,
        "weight": 9
      },
      "item-5378": {
        "value": 7,
        "weight": 5
      },
      "item-5379": {
        "value": 8,
        "weight": 7
      },
      "item-5380": {
        "value": 3,
        "weight": 1
      },
      "item-5381": {
        "value": 8,
        "weight": 7
      },
      "item-5382": {
        "value": 7,
        "weight": 1
      },
      "item-5383": {
        "value": 8,
        "weight": 5
      },
      "item-5384": {
        "value": 9,
        "weight": 6
      },
      "item-5385": {
        "value": 7,
        "weight": 5
      },
      "item-5386": {
        "value": 7,
        "weight": 9
      },
      "item-5387": {
        "value": 3,
        "weight": 7
      },
      "item-5388": {
        "value": 8,
        "weight": 9
      },
      "item-5389": {
        "value": 1,
        "weight": 7
      },
      "item-5390": {
        "value": 8,
        "weight": 2
      },
      "item-5391": {
        "value": 3,
        "weight": 4
      },
      "item-5392": {
        "value": 4,
        "weight": 2
      },
      "item-5393": {
        "value": 1,
        "weight": 4
      },
      "item-5394": {
        "value": 6,
        "weight": 9
      },
      "item-5395": {
        "value": 2,
        "weight": 3
      },
      "item-5396": {
        "value": 8,
        "weight": 1
      },
      "item-5397": {
        "value": 7,
        "weight": 6
      },
      "item-5398": {
        "value": 2,
        "weight": 5
      },
      "item-5399": {
        "value": 1,
        "weight": 7
      },
      "item-5400": {
        "value": 4,
        "weight": 5
      },
      "item-5401": {
        "value": 9,
        "weight": 5
      },
      "item-5402": {
        "value": 8,
        "weight": 5
      },
      "item-5403": {
        "value": 3,
        "weight": 2
      },
      "item-5404": {
        "value": 2,
        "weight": 1
      },
      "item-5405": {
        "value": 7,
        "weight": 6
      },
      "item-5406": {
        "value": 8,
        "weight": 9
      },
      "item-5407": {
        "value": 2,
        "weight": 3
      },
      "item-5408": {
        "value": 1,
        "weight": 6
      },
      "item-5409": {
        "value": 4,
        "weight": 8
      },
      "item-5410": {
        "value": 8,
        "weight": 9
      },
      "item-5411": {
        "value": 9,
        "weight": 9
      },
      "item-5412": {
        "value": 6,
        "weight": 9
      },
      "item-5413": {
        "value": 8,
        "weight": 1
      },
      "item-5414": {
        "value": 9,
        "weight": 7
      },
      "item-5415": {
        "value": 2,
        "weight": 8
      },
      "item-5416": {
        "value": 4,
        "weight": 6
      },
      "item-5417": {
        "value": 6,
        "weight": 1
      },
      "item-5418": {
        "value": 8,
        "weight": 9
      },
      "item-5419": {
        "value": 1,
        "weight": 4
      },
      "item-5420": {
        "value": 6,
        "weight": 5
      },
      "item-5421": {
        "value": 8,
        "weight": 7
      },
      "item-5422": {
        "value": 9,
        "weight": 5
      },
      "item-5423": {
        "value": 6,
        "weight": 3
      },
      "item-5424": {
        "value": 7,
        "weight": 6
      },
      "item-5425": {
        "value": 8,
        "weight": 8
      },
      "item-5426": {
        "value": 9,
        "weight": 9
      },
      "item-5427": {
        "value": 4,
        "weight": 9
      },
      "item-5428": {
        "value": 4,
        "weight": 7
      },
      "item-5429": {
        "value": 6,
        "weight": 7
      },
      "item-5430": {
        "value": 6,
        "weight": 9
      },
      "item-5431": {
        "value": 4,
        "weight": 4
      },
      "item-5432": {
        "value": 4,
        "weight": 9
      },
      "item-5433": {
        "value": 5,
        "weight": 2
      },
      "item-5434": {
        "value": 3,
        "weight": 2
      },
      "item-5435": {
        "value": 5,
        "weight": 9
      },
      "item-5436": {
        "value": 9,
        "weight": 1
      },
      "item-5437": {
        "value": 6,
        "weight": 3
      },
      "item-5438": {
        "value": 7,
        "weight": 6
      },
      "item-5439": {
        "value": 8,
        "weight": 9
      },
      "item-5440": {
        "value": 5,
        "weight": 8
      },
      "item-5441": {
        "value": 6,
        "weight": 9
      },
      "item-5442": {
        "value": 3,
        "weight": 5
      },
      "item-5443": {
        "value": 1,
        "weight": 4
      },
      "item-5444": {
        "value": 1,
        "weight": 9
      },
      "item-5445": {
        "value": 6,
        "weight": 2
      },
      "item-5446": {
        "value": 1,
        "weight": 5
      },
      "item-5447": {
        "value": 2,
        "weight": 6
      },
      "item-5448": {
        "value": 4,
        "weight": 9
      },
      "item-5449": {
        "value": 2,
        "weight": 5
      },
      "item-5450": {
        "value": 7,
        "weight": 7
      },
      "item-5451": {
        "value": 3,
        "weight": 9
      },
      "item-5452": {
        "value": 3,
        "weight": 6
      },
      "item-5453": {
        "value": 2,
        "weight": 7
      },
      "item-5454": {
        "value": 1,
        "weight": 7
      },
      "item-5455": {
        "value": 8,
        "weight": 6
      },
      "item-5456": {
        "value": 9,
        "weight": 9
      },
      "item-5457": {
        "value": 4,
        "weight": 1
      },
      "item-5458": {
        "value": 8,
        "weight": 6
      },
      "item-5459": {
        "value": 3,
        "weight": 5
      },
      "item-5460": {
        "value": 3,
        "weight": 5
      },
      "item-5461": {
        "value": 7,
        "weight": 5
      },
      "item-5462": {
        "value": 1,
        "weight": 6
      },
      "item-5463": {
        "value": 6,
        "weight": 9
      },
      "item-5464": {
        "value": 8,
        "weight": 9
      },
      "item-5465": {
        "value": 3,
        "weight": 1
      },
      "item-5466": {
        "value": 4,
        "weight": 3
      },
      "item-5467": {
        "value": 8,
        "weight": 5
      },
      "item-5468": {
        "value": 6,
        "weight": 4
      },
      "item-5469": {
        "value": 4,
        "weight": 7
      },
      "item-5470": {
        "value": 3,
        "weight": 3
      },
      "item-5471": {
        "value": 4,
        "weight": 8
      },
      "item-5472": {
        "value": 9,
        "weight": 6
      },
      "item-5473": {
        "value": 3,
        "weight": 4
      },
      "item-5474": {
        "value": 4,
        "weight": 2
      },
      "item-5475": {
        "value": 6,
        "weight": 8
      },
      "item-5476": {
        "value": 8,
        "weight": 2
      },
      "item-5477": {
        "value": 8,
        "weight": 8
      },
      "item-5478": {
        "value": 7,
        "weight": 5
      },
      "item-5479": {
        "value": 4,
        "weight": 8
      },
      "item-5480": {
        "value": 4,
        "weight": 5
      },
      "item-5481": {
        "value": 2,
        "weight": 1
      },
      "item-5482": {
        "value": 9,
        "weight": 3
      },
      "item-5483": {
        "value": 6,
        "weight": 2
      },
      "item-5484": {
        "value": 6,
        "weight": 9
      },
      "item-5485": {
        "value": 8,
        "weight": 4
      },
      "item-5486": {
        "value": 6,
        "weight": 4
      },
      "item-5487": {
        "value": 2,
        "weight": 8
      },
      "item-5488": {
        "value": 3,
        "weight": 8
      },
      "item-5489": {
        "value": 5,
        "weight": 5
      },
      "item-5490": {
        "value": 3,
        "weight": 4
      },
      "item-5491": {
        "value": 5,
        "weight": 2
      },
      "item-5492": {
        "value": 7,
        "weight": 9
      },
      "item-5493": {
        "value": 5,
        "weight": 5
      },
      "item-5494": {
        "value": 6,
        "weight": 7
      },
      "item-5495": {
        "value": 1,
        "weight": 2
      },
      "item-5496": {
        "value": 5,
        "weight": 6
      },
      "item-5497": {
        "value": 3,
        "weight": 1
      },
      "item-5498": {
        "value": 5,
        "weight": 9
      },
      "item-5499": {
        "value": 7,
        "weight": 1
      },
      "item-5500": {
        "value": 3,
        "weight": 5
      },
      "item-5501": {
        "value": 7,
        "weight": 6
      },
      "item-5502": {
        "value": 8,
        "weight": 5
      },
      "item-5503": {
        "value": 1,
        "weight": 3
      },
      "item-5504": {
        "value": 3,
        "weight": 9
      },
      "item-5505": {
        "value": 9,
        "weight": 1
      },
      "item-5506": {
        "value": 5,
        "weight": 3
      },
      "item-5507": {
        "value": 4,
        "weight": 5
      },
      "item-5508": {
        "value": 2,
        "weight": 7
      },
      "item-5509": {
        "value": 5,
        "weight": 5
      },
      "item-5510": {
        "value": 5,
        "weight": 8
      },
      "item-5511": {
        "value": 9,
        "weight": 9
      },
      "item-5512": {
        "value": 5,
        "weight": 6
      },
      "item-5513": {
        "value": 8,
        "weight": 9
      },
      "item-5514": {
        "value": 3,
        "weight": 9
      },
      "item-5515": {
        "value": 9,
        "weight": 3
      },
      "item-5516": {
        "value": 4,
        "weight": 2
      },
      "item-5517": {
        "value": 2,
        "weight": 4
      },
      "item-5518": {
        "value": 5,
        "weight": 5
      },
      "item-5519": {
        "value": 9,
        "weight": 6
      },
      "item-5520": {
        "value": 9,
        "weight": 2
      },
      "item-5521": {
        "value": 8,
        "weight": 4
      },
      "item-5522": {
        "value": 5,
        "weight": 1
      },
      "item-5523": {
        "value": 6,
        "weight": 6
      },
      "item-5524": {
        "value": 6,
        "weight": 1
      },
      "item-5525": {
        "value": 3,
        "weight": 9
      },
      "item-5526": {
        "value": 9,
        "weight": 7
      },
      "item-5527": {
        "value": 1,
        "weight": 8
      },
      "item-5528": {
        "value": 3,
        "weight": 2
      },
      "item-5529": {
        "value": 3,
        "weight": 6
      },
      "item-5530": {
        "value": 2,
        "weight": 1
      },
      "item-5531": {
        "value": 8,
        "weight": 5
      },
      "item-5532": {
        "value": 5,
        "weight": 4
      },
      "item-5533": {
        "value": 9,
        "weight": 8
      },
      "item-5534": {
        "value": 5,
        "weight": 9
      },
      "item-5535": {
        "value": 9,
        "weight": 8
      },
      "item-5536": {
        "value": 3,
        "weight": 4
      },
      "item-5537": {
        "value": 1,
        "weight": 7
      },
      "item-5538": {
        "value": 7,
        "weight": 4
      },
      "item-5539": {
        "value": 9,
        "weight": 5
      },
      "item-5540": {
        "value": 4,
        "weight": 5
      },
      "item-5541": {
        "value": 4,
        "weight": 1
      },
      "item-5542": {
        "value": 9,
        "weight": 2
      },
      "item-5543": {
        "value": 4,
        "weight": 6
      },
      "item-5544": {
        "value": 8,
        "weight": 6
      },
      "item-5545": {
        "value": 2,
        "weight": 7
      },
      "item-5546": {
        "value": 6,
        "weight": 4
      },
      "item-5547": {
        "value": 9,
        "weight": 5
      },
      "item-5548": {
        "value": 6,
        "weight": 4
      },
      "item-5549": {
        "value": 6,
        "weight": 9
      },
      "item-5550": {
        "value": 4,
        "weight": 2
      },
      "item-5551": {
        "value": 5,
        "weight": 6
      },
      "item-5552": {
        "value": 6,
        "weight": 8
      },
      "item-5553": {
        "value": 9,
        "weight": 6
      },
      "item-5554": {
        "value": 6,
        "weight": 1
      },
      "item-5555": {
        "value": 6,
        "weight": 1
      },
      "item-5556": {
        "value": 2,
        "weight": 2
      },
      "item-5557": {
        "value": 5,
        "weight": 5
      },
      "item-5558": {
        "value": 5,
        "weight": 8
      },
      "item-5559": {
        "value": 4,
        "weight": 6
      },
      "item-5560": {
        "value": 4,
        "weight": 6
      },
      "item-5561": {
        "value": 2,
        "weight": 1
      },
      "item-5562": {
        "value": 5,
        "weight": 4
      },
      "item-5563": {
        "value": 4,
        "weight": 9
      },
      "item-5564": {
        "value": 6,
        "weight": 9
      },
      "item-5565": {
        "value": 3,
        "weight": 1
      },
      "item-5566": {
        "value": 3,
        "weight": 7
      },
      "item-5567": {
        "value": 1,
        "weight": 8
      },
      "item-5568": {
        "value": 7,
        "weight": 5
      },
      "item-5569": {
        "value": 1,
        "weight": 6
      },
      "item-5570": {
        "value": 3,
        "weight": 1
      },
      "item-5571": {
        "value": 7,
        "weight": 1
      },
      "item-5572": {
        "value": 6,
        "weight": 3
      },
      "item-5573": {
        "value": 2,
        "weight": 5
      },
      "item-5574": {
        "value": 2,
        "weight": 8
      },
      "item-5575": {
        "value": 5,
        "weight": 5
      },
      "item-5576": {
        "value": 4,
        "weight": 8
      },
      "item-5577": {
        "value": 1,
        "weight": 4
      },
      "item-5578": {
        "value": 8,
        "weight": 9
      },
      "item-5579": {
        "value": 2,
        "weight": 3
      },
      "item-5580": {
        "value": 6,
        "weight": 4
      },
      "item-5581": {
        "value": 2,
        "weight": 1
      },
      "item-5582": {
        "value": 1,
        "weight": 4
      },
      "item-5583": {
        "value": 6,
        "weight": 8
      },
      "item-5584": {
        "value": 1,
        "weight": 8
      },
      "item-5585": {
        "value": 5,
        "weight": 7
      },
      "item-5586": {
        "value": 8,
        "weight": 5
      },
      "item-5587": {
        "value": 1,
        "weight": 4
      },
      "item-5588": {
        "value": 3,
        "weight": 6
      },
      "item-5589": {
        "value": 9,
        "weight": 7
      },
      "item-5590": {
        "value": 2,
        "weight": 3
      },
      "item-5591": {
        "value": 2,
        "weight": 1
      },
      "item-5592": {
        "value": 8,
        "weight": 7
      },
      "item-5593": {
        "value": 5,
        "weight": 8
      },
      "item-5594": {
        "value": 2,
        "weight": 6
      },
      "item-5595": {
        "value": 9,
        "weight": 8
      },
      "item-5596": {
        "value": 6,
        "weight": 6
      },
      "item-5597": {
        "value": 2,
        "weight": 2
      },
      "item-5598": {
        "value": 5,
        "weight": 1
      },
      "item-5599": {
        "value": 7,
        "weight": 9
      },
      "item-5600": {
        "value": 7,
        "weight": 7
      },
      "item-5601": {
        "value": 3,
        "weight": 8
      },
      "item-5602": {
        "value": 8,
        "weight": 9
      },
      "item-5603": {
        "value": 5,
        "weight": 5
      },
      "item-5604": {
        "value": 3,
        "weight": 8
      },
      "item-5605": {
        "value": 5,
        "weight": 4
      },
      "item-5606": {
        "value": 6,
        "weight": 5
      },
      "item-5607": {
        "value": 4,
        "weight": 3
      },
      "item-5608": {
        "value": 9,
        "weight": 4
      },
      "item-5609": {
        "value": 7,
        "weight": 8
      },
      "item-5610": {
        "value": 8,
        "weight": 6
      },
      "item-5611": {
        "value": 7,
        "weight": 3
      },
      "item-5612": {
        "value": 6,
        "weight": 2
      },
      "item-5613": {
        "value": 8,
        "weight": 9
      },
      "item-5614": {
        "value": 7,
        "weight": 8
      },
      "item-5615": {
        "value": 4,
        "weight": 4
      },
      "item-5616": {
        "value": 1,
        "weight": 6
      },
      "item-5617": {
        "value": 4,
        "weight": 5
      },
      "item-5618": {
        "value": 1,
        "weight": 4
      },
      "item-5619": {
        "value": 9,
        "weight": 3
      },
      "item-5620": {
        "value": 9,
        "weight": 6
      },
      "item-5621": {
        "value": 4,
        "weight": 8
      },
      "item-5622": {
        "value": 5,
        "weight": 5
      },
      "item-5623": {
        "value": 8,
        "weight": 5
      },
      "item-5624": {
        "value": 1,
        "weight": 8
      },
      "item-5625": {
        "value": 8,
        "weight": 6
      },
      "item-5626": {
        "value": 8,
        "weight": 2
      },
      "item-5627": {
        "value": 4,
        "weight": 1
      },
      "item-5628": {
        "value": 6,
        "weight": 9
      },
      "item-5629": {
        "value": 6,
        "weight": 4
      },
      "item-5630": {
        "value": 5,
        "weight": 6
      },
      "item-5631": {
        "value": 5,
        "weight": 5
      },
      "item-5632": {
        "value": 6,
        "weight": 3
      },
      "item-5633": {
        "value": 9,
        "weight": 9
      },
      "item-5634": {
        "value": 3,
        "weight": 8
      },
      "item-5635": {
        "value": 9,
        "weight": 7
      },
      "item-5636": {
        "value": 2,
        "weight": 7
      },
      "item-5637": {
        "value": 1,
        "weight": 1
      },
      "item-5638": {
        "value": 9,
        "weight": 7
      },
      "item-5639": {
        "value": 9,
        "weight": 8
      },
      "item-5640": {
        "value": 6,
        "weight": 7
      },
      "item-5641": {
        "value": 9,
        "weight": 7
      },
      "item-5642": {
        "value": 1,
        "weight": 9
      },
      "item-5643": {
        "value": 4,
        "weight": 1
      },
      "item-5644": {
        "value": 7,
        "weight": 4
      },
      "item-5645": {
        "value": 6,
        "weight": 8
      },
      "item-5646": {
        "value": 7,
        "weight": 6
      },
      "item-5647": {
        "value": 2,
        "weight": 8
      },
      "item-5648": {
        "value": 2,
        "weight": 4
      },
      "item-5649": {
        "value": 7,
        "weight": 6
      },
      "item-5650": {
        "value": 7,
        "weight": 5
      },
      "item-5651": {
        "value": 9,
        "weight": 6
      },
      "item-5652": {
        "value": 7,
        "weight": 9
      },
      "item-5653": {
        "value": 8,
        "weight": 1
      },
      "item-5654": {
        "value": 1,
        "weight": 4
      },
      "item-5655": {
        "value": 1,
        "weight": 1
      },
      "item-5656": {
        "value": 8,
        "weight": 3
      },
      "item-5657": {
        "value": 3,
        "weight": 5
      },
      "item-5658": {
        "value": 4,
        "weight": 6
      },
      "item-5659": {
        "value": 2,
        "weight": 8
      },
      "item-5660": {
        "value": 9,
        "weight": 5
      },
      "item-5661": {
        "value": 9,
        "weight": 8
      },
      "item-5662": {
        "value": 4,
        "weight": 7
      },
      "item-5663": {
        "value": 1,
        "weight": 4
      },
      "item-5664": {
        "value": 1,
        "weight": 3
      },
      "item-5665": {
        "value": 6,
        "weight": 9
      },
      "item-5666": {
        "value": 9,
        "weight": 4
      },
      "item-5667": {
        "value": 4,
        "weight": 6
      },
      "item-5668": {
        "value": 2,
        "weight": 3
      },
      "item-5669": {
        "value": 2,
        "weight": 6
      },
      "item-5670": {
        "value": 8,
        "weight": 1
      },
      "item-5671": {
        "value": 7,
        "weight": 8
      },
      "item-5672": {
        "value": 3,
        "weight": 6
      },
      "item-5673": {
        "value": 1,
        "weight": 1
      },
      "item-5674": {
        "value": 2,
        "weight": 9
      },
      "item-5675": {
        "value": 4,
        "weight": 9
      },
      "item-5676": {
        "value": 7,
        "weight": 9
      },
      "item-5677": {
        "value": 7,
        "weight": 7
      },
      "item-5678": {
        "value": 1,
        "weight": 9
      },
      "item-5679": {
        "value": 2,
        "weight": 8
      },
      "item-5680": {
        "value": 5,
        "weight": 3
      },
      "item-5681": {
        "value": 9,
        "weight": 1
      },
      "item-5682": {
        "value": 9,
        "weight": 9
      },
      "item-5683": {
        "value": 9,
        "weight": 9
      },
      "item-5684": {
        "value": 9,
        "weight": 4
      },
      "item-5685": {
        "value": 9,
        "weight": 2
      },
      "item-5686": {
        "value": 3,
        "weight": 5
      },
      "item-5687": {
        "value": 7,
        "weight": 4
      },
      "item-5688": {
        "value": 1,
        "weight": 3
      },
      "item-5689": {
        "value": 6,
        "weight": 9
      },
      "item-5690": {
        "value": 2,
        "weight": 3
      },
      "item-5691": {
        "value": 1,
        "weight": 4
      },
      "item-5692": {
        "value": 1,
        "weight": 8
      },
      "item-5693": {
        "value": 8,
        "weight": 3
      },
      "item-5694": {
        "value": 7,
        "weight": 9
      },
      "item-5695": {
        "value": 3,
        "weight": 1
      },
      "item-5696": {
        "value": 2,
        "weight": 3
      },
      "item-5697": {
        "value": 3,
        "weight": 9
      },
      "item-5698": {
        "value": 7,
        "weight": 1
      },
      "item-5699": {
        "value": 1,
        "weight": 4
      },
      "item-5700": {
        "value": 6,
        "weight": 3
      },
      "item-5701": {
        "value": 1,
        "weight": 8
      },
      "item-5702": {
        "value": 1,
        "weight": 6
      },
      "item-5703": {
        "value": 3,
        "weight": 7
      },
      "item-5704": {
        "value": 8,
        "weight": 6
      },
      "item-5705": {
        "value": 6,
        "weight": 1
      },
      "item-5706": {
        "value": 6,
        "weight": 2
      },
      "item-5707": {
        "value": 9,
        "weight": 8
      },
      "item-5708": {
        "value": 4,
        "weight": 6
      },
      "item-5709": {
        "value": 4,
        "weight": 2
      },
      "item-5710": {
        "value": 7,
        "weight": 9
      },
      "item-5711": {
        "value": 1,
        "weight": 7
      },
      "item-5712": {
        "value": 5,
        "weight": 4
      },
      "item-5713": {
        "value": 5,
        "weight": 5
      },
      "item-5714": {
        "value": 9,
        "weight": 7
      },
      "item-5715": {
        "value": 4,
        "weight": 4
      },
      "item-5716": {
        "value": 5,
        "weight": 7
      },
      "item-5717": {
        "value": 5,
        "weight": 2
      },
      "item-5718": {
        "value": 2,
        "weight": 8
      },
      "item-5719": {
        "value": 9,
        "weight": 5
      },
      "item-5720": {
        "value": 4,
        "weight": 1
      },
      "item-5721": {
        "value": 4,
        "weight": 2
      },
      "item-5722": {
        "value": 2,
        "weight": 9
      },
      "item-5723": {
        "value": 3,
        "weight": 1
      },
      "item-5724": {
        "value": 2,
        "weight": 2
      },
      "item-5725": {
        "value": 8,
        "weight": 7
      },
      "item-5726": {
        "value": 4,
        "weight": 8
      },
      "item-5727": {
        "value": 6,
        "weight": 5
      },
      "item-5728": {
        "value": 7,
        "weight": 5
      },
      "item-5729": {
        "value": 8,
        "weight": 2
      },
      "item-5730": {
        "value": 8,
        "weight": 3
      },
      "item-5731": {
        "value": 4,
        "weight": 4
      },
      "item-5732": {
        "value": 5,
        "weight": 3
      },
      "item-5733": {
        "value": 1,
        "weight": 5
      },
      "item-5734": {
        "value": 1,
        "weight": 1
      },
      "item-5735": {
        "value": 4,
        "weight": 6
      },
      "item-5736": {
        "value": 5,
        "weight": 7
      },
      "item-5737": {
        "value": 6,
        "weight": 6
      },
      "item-5738": {
        "value": 9,
        "weight": 5
      },
      "item-5739": {
        "value": 4,
        "weight": 4
      },
      "item-5740": {
        "value": 9,
        "weight": 3
      },
      "item-5741": {
        "value": 7,
        "weight": 6
      },
      "item-5742": {
        "value": 5,
        "weight": 9
      },
      "item-5743": {
        "value": 4,
        "weight": 5
      },
      "item-5744": {
        "value": 5,
        "weight": 5
      },
      "item-5745": {
        "value": 6,
        "weight": 2
      },
      "item-5746": {
        "value": 4,
        "weight": 3
      },
      "item-5747": {
        "value": 7,
        "weight": 2
      },
      "item-5748": {
        "value": 1,
        "weight": 2
      },
      "item-5749": {
        "value": 9,
        "weight": 8
      },
      "item-5750": {
        "value": 1,
        "weight": 4
      },
      "item-5751": {
        "value": 2,
        "weight": 6
      },
      "item-5752": {
        "value": 6,
        "weight": 5
      },
      "item-5753": {
        "value": 2,
        "weight": 7
      },
      "item-5754": {
        "value": 6,
        "weight": 2
      },
      "item-5755": {
        "value": 7,
        "weight": 9
      },
      "item-5756": {
        "value": 2,
        "weight": 6
      },
      "item-5757": {
        "value": 1,
        "weight": 7
      },
      "item-5758": {
        "value": 5,
        "weight": 2
      },
      "item-5759": {
        "value": 3,
        "weight": 9
      },
      "item-5760": {
        "value": 4,
        "weight": 6
      },
      "item-5761": {
        "value": 2,
        "weight": 4
      },
      "item-5762": {
        "value": 5,
        "weight": 1
      },
      "item-5763": {
        "value": 7,
        "weight": 9
      },
      "item-5764": {
        "value": 1,
        "weight": 4
      },
      "item-5765": {
        "value": 4,
        "weight": 9
      },
      "item-5766": {
        "value": 7,
        "weight": 2
      },
      "item-5767": {
        "value": 2,
        "weight": 5
      },
      "item-5768": {
        "value": 4,
        "weight": 8
      },
      "item-5769": {
        "value": 8,
        "weight": 5
      },
      "item-5770": {
        "value": 5,
        "weight": 8
      },
      "item-5771": {
        "value": 9,
        "weight": 1
      },
      "item-5772": {
        "value": 6,
        "weight": 6
      },
      "item-5773": {
        "value": 9,
        "weight": 2
      },
      "item-5774": {
        "value": 5,
        "weight": 9
      },
      "item-5775": {
        "value": 7,
        "weight": 7
      },
      "item-5776": {
        "value": 9,
        "weight": 6
      },
      "item-5777": {
        "value": 9,
        "weight": 7
      },
      "item-5778": {
        "value": 6,
        "weight": 4
      },
      "item-5779": {
        "value": 4,
        "weight": 7
      },
      "item-5780": {
        "value": 4,
        "weight": 5
      },
      "item-5781": {
        "value": 6,
        "weight": 1
      },
      "item-5782": {
        "value": 1,
        "weight": 8
      },
      "item-5783": {
        "value": 2,
        "weight": 8
      },
      "item-5784": {
        "value": 1,
        "weight": 5
      },
      "item-5785": {
        "value": 1,
        "weight": 8
      },
      "item-5786": {
        "value": 7,
        "weight": 3
      },
      "item-5787": {
        "value": 3,
        "weight": 3
      },
      "item-5788": {
        "value": 6,
        "weight": 3
      },
      "item-5789": {
        "value": 1,
        "weight": 2
      },
      "item-5790": {
        "value": 1,
        "weight": 7
      },
      "item-5791": {
        "value": 1,
        "weight": 7
      },
      "item-5792": {
        "value": 3,
        "weight": 9
      },
      "item-5793": {
        "value": 8,
        "weight": 3
      },
      "item-5794": {
        "value": 5,
        "weight": 3
      },
      "item-5795": {
        "value": 8,
        "weight": 2
      },
      "item-5796": {
        "value": 5,
        "weight": 8
      },
      "item-5797": {
        "value": 8,
        "weight": 8
      },
      "item-5798": {
        "value": 6,
        "weight": 9
      },
      "item-5799": {
        "value": 1,
        "weight": 7
      },
      "item-5800": {
        "value": 6,
        "weight": 7
      },
      "item-5801": {
        "value": 1,
        "weight": 1
      },
      "item-5802": {
        "value": 6,
        "weight": 9
      },
      "item-5803": {
        "value": 2,
        "weight": 3
      },
      "item-5804": {
        "value": 6,
        "weight": 8
      },
      "item-5805": {
        "value": 9,
        "weight": 2
      },
      "item-5806": {
        "value": 5,
        "weight": 1
      },
      "item-5807": {
        "value": 5,
        "weight": 3
      },
      "item-5808": {
        "value": 4,
        "weight": 8
      },
      "item-5809": {
        "value": 2,
        "weight": 2
      },
      "item-5810": {
        "value": 8,
        "weight": 3
      },
      "item-5811": {
        "value": 1,
        "weight": 8
      },
      "item-5812": {
        "value": 1,
        "weight": 8
      },
      "item-5813": {
        "value": 8,
        "weight": 7
      },
      "item-5814": {
        "value": 6,
        "weight": 6
      },
      "item-5815": {
        "value": 6,
        "weight": 2
      },
      "item-5816": {
        "value": 4,
        "weight": 3
      },
      "item-5817": {
        "value": 5,
        "weight": 5
      },
      "item-5818": {
        "value": 6,
        "weight": 3
      },
      "item-5819": {
        "value": 7,
        "weight": 2
      },
      "item-5820": {
        "value": 2,
        "weight": 3
      },
      "item-5821": {
        "value": 2,
        "weight": 5
      },
      "item-5822": {
        "value": 3,
        "weight": 2
      },
      "item-5823": {
        "value": 7,
        "weight": 2
      },
      "item-5824": {
        "value": 2,
        "weight": 8
      },
      "item-5825": {
        "value": 5,
        "weight": 1
      },
      "item-5826": {
        "value": 4,
        "weight": 5
      },
      "item-5827": {
        "value": 2,
        "weight": 4
      },
      "item-5828": {
        "value": 6,
        "weight": 7
      },
      "item-5829": {
        "value": 9,
        "weight": 4
      },
      "item-5830": {
        "value": 4,
        "weight": 4
      },
      "item-5831": {
        "value": 8,
        "weight": 5
      },
      "item-5832": {
        "value": 8,
        "weight": 5
      },
      "item-5833": {
        "value": 6,
        "weight": 1
      },
      "item-5834": {
        "value": 5,
        "weight": 1
      },
      "item-5835": {
        "value": 7,
        "weight": 7
      },
      "item-5836": {
        "value": 6,
        "weight": 7
      },
      "item-5837": {
        "value": 3,
        "weight": 2
      },
      "item-5838": {
        "value": 5,
        "weight": 9
      },
      "item-5839": {
        "value": 6,
        "weight": 4
      },
      "item-5840": {
        "value": 3,
        "weight": 3
      },
      "item-5841": {
        "value": 2,
        "weight": 7
      },
      "item-5842": {
        "value": 9,
        "weight": 4
      },
      "item-5843": {
        "value": 3,
        "weight": 7
      },
      "item-5844": {
        "value": 2,
        "weight": 4
      },
      "item-5845": {
        "value": 2,
        "weight": 8
      },
      "item-5846": {
        "value": 7,
        "weight": 9
      },
      "item-5847": {
        "value": 8,
        "weight": 2
      },
      "item-5848": {
        "value": 5,
        "weight": 8
      },
      "item-5849": {
        "value": 2,
        "weight": 8
      },
      "item-5850": {
        "value": 8,
        "weight": 6
      },
      "item-5851": {
        "value": 5,
        "weight": 3
      },
      "item-5852": {
        "value": 3,
        "weight": 3
      },
      "item-5853": {
        "value": 6,
        "weight": 2
      },
      "item-5854": {
        "value": 4,
        "weight": 7
      },
      "item-5855": {
        "value": 8,
        "weight": 8
      },
      "item-5856": {
        "value": 3,
        "weight": 2
      },
      "item-5857": {
        "value": 3,
        "weight": 7
      },
      "item-5858": {
        "value": 6,
        "weight": 7
      },
      "item-5859": {
        "value": 4,
        "weight": 6
      },
      "item-5860": {
        "value": 5,
        "weight": 2
      },
      "item-5861": {
        "value": 4,
        "weight": 3
      },
      "item-5862": {
        "value": 1,
        "weight": 4
      },
      "item-5863": {
        "value": 1,
        "weight": 6
      },
      "item-5864": {
        "value": 5,
        "weight": 6
      },
      "item-5865": {
        "value": 9,
        "weight": 3
      },
      "item-5866": {
        "value": 4,
        "weight": 2
      },
      "item-5867": {
        "value": 7,
        "weight": 9
      },
      "item-5868": {
        "value": 1,
        "weight": 8
      },
      "item-5869": {
        "value": 8,
        "weight": 5
      },
      "item-5870": {
        "value": 9,
        "weight": 5
      },
      "item-5871": {
        "value": 1,
        "weight": 2
      },
      "item-5872": {
        "value": 3,
        "weight": 5
      },
      "item-5873": {
        "value": 2,
        "weight": 3
      },
      "item-5874": {
        "value": 9,
        "weight": 5
      },
      "item-5875": {
        "value": 7,
        "weight": 6
      },
      "item-5876": {
        "value": 5,
        "weight": 5
      },
      "item-5877": {
        "value": 5,
        "weight": 4
      },
      "item-5878": {
        "value": 4,
        "weight": 1
      },
      "item-5879": {
        "value": 9,
        "weight": 8
      },
      "item-5880": {
        "value": 7,
        "weight": 9
      },
      "item-5881": {
        "value": 5,
        "weight": 6
      },
      "item-5882": {
        "value": 6,
        "weight": 9
      },
      "item-5883": {
        "value": 2,
        "weight": 9
      },
      "item-5884": {
        "value": 6,
        "weight": 2
      },
      "item-5885": {
        "value": 4,
        "weight": 9
      },
      "item-5886": {
        "value": 5,
        "weight": 2
      },
      "item-5887": {
        "value": 8,
        "weight": 2
      },
      "item-5888": {
        "value": 1,
        "weight": 6
      },
      "item-5889": {
        "value": 9,
        "weight": 6
      },
      "item-5890": {
        "value": 7,
        "weight": 2
      },
      "item-5891": {
        "value": 2,
        "weight": 8
      },
      "item-5892": {
        "value": 7,
        "weight": 6
      },
      "item-5893": {
        "value": 9,
        "weight": 1
      },
      "item-5894": {
        "value": 9,
        "weight": 4
      },
      "item-5895": {
        "value": 7,
        "weight": 3
      },
      "item-5896": {
        "value": 3,
        "weight": 8
      },
      "item-5897": {
        "value": 3,
        "weight": 9
      },
      "item-5898": {
        "value": 6,
        "weight": 4
      },
      "item-5899": {
        "value": 5,
        "weight": 1
      },
      "item-5900": {
        "value": 2,
        "weight": 2
      },
      "item-5901": {
        "value": 1,
        "weight": 5
      },
      "item-5902": {
        "value": 3,
        "weight": 5
      },
      "item-5903": {
        "value": 8,
        "weight": 8
      },
      "item-5904": {
        "value": 3,
        "weight": 2
      },
      "item-5905": {
        "value": 4,
        "weight": 7
      },
      "item-5906": {
        "value": 8,
        "weight": 7
      },
      "item-5907": {
        "value": 3,
        "weight": 3
      },
      "item-5908": {
        "value": 1,
        "weight": 5
      },
      "item-5909": {
        "value": 3,
        "weight": 4
      },
      "item-5910": {
        "value": 1,
        "weight": 9
      },
      "item-5911": {
        "value": 1,
        "weight": 8
      },
      "item-5912": {
        "value": 7,
        "weight": 7
      },
      "item-5913": {
        "value": 5,
        "weight": 5
      },
      "item-5914": {
        "value": 6,
        "weight": 3
      },
      "item-5915": {
        "value": 8,
        "weight": 4
      },
      "item-5916": {
        "value": 6,
        "weight": 7
      },
      "item-5917": {
        "value": 5,
        "weight": 1
      },
      "item-5918": {
        "value": 8,
        "weight": 7
      },
      "item-5919": {
        "value": 1,
        "weight": 2
      },
      "item-5920": {
        "value": 2,
        "weight": 6
      },
      "item-5921": {
        "value": 9,
        "weight": 8
      },
      "item-5922": {
        "value": 8,
        "weight": 1
      },
      "item-5923": {
        "value": 2,
        "weight": 2
      },
      "item-5924": {
        "value": 6,
        "weight": 7
      },
      "item-5925": {
        "value": 4,
        "weight": 8
      },
      "item-5926": {
        "value": 1,
        "weight": 8
      },
      "item-5927": {
        "value": 8,
        "weight": 5
      },
      "item-5928": {
        "value": 4,
        "weight": 6
      },
      "item-5929": {
        "value": 2,
        "weight": 4
      },
      "item-5930": {
        "value": 5,
        "weight": 2
      },
      "item-5931": {
        "value": 1,
        "weight": 2
      },
      "item-5932": {
        "value": 6,
        "weight": 2
      },
      "item-5933": {
        "value": 9,
        "weight": 2
      },
      "item-5934": {
        "value": 1,
        "weight": 1
      },
      "item-5935": {
        "value": 1,
        "weight": 3
      },
      "item-5936": {
        "value": 2,
        "weight": 8
      },
      "item-5937": {
        "value": 7,
        "weight": 3
      },
      "item-5938": {
        "value": 1,
        "weight": 8
      },
      "item-5939": {
        "value": 4,
        "weight": 3
      },
      "item-5940": {
        "value": 9,
        "weight": 3
      },
      "item-5941": {
        "value": 9,
        "weight": 7
      },
      "item-5942": {
        "value": 9,
        "weight": 9
      },
      "item-5943": {
        "value": 3,
        "weight": 7
      },
      "item-5944": {
        "value": 5,
        "weight": 3
      },
      "item-5945": {
        "value": 2,
        "weight": 2
      },
      "item-5946": {
        "value": 2,
        "weight": 5
      },
      "item-5947": {
        "value": 7,
        "weight": 2
      },
      "item-5948": {
        "value": 1,
        "weight": 1
      },
      "item-5949": {
        "value": 9,
        "weight": 5
      },
      "item-5950": {
        "value": 1,
        "weight": 4
      },
      "item-5951": {
        "value": 6,
        "weight": 1
      },
      "item-5952": {
        "value": 3,
        "weight": 8
      },
      "item-5953": {
        "value": 5,
        "weight": 8
      },
      "item-5954": {
        "value": 1,
        "weight": 4
      },
      "item-5955": {
        "value": 3,
        "weight": 5
      },
      "item-5956": {
        "value": 3,
        "weight": 2
      },
      "item-5957": {
        "value": 6,
        "weight": 1
      },
      "item-5958": {
        "value": 4,
        "weight": 9
      },
      "item-5959": {
        "value": 2,
        "weight": 8
      },
      "item-5960": {
        "value": 1,
        "weight": 7
      },
      "item-5961": {
        "value": 4,
        "weight": 7
      },
      "item-5962": {
        "value": 2,
        "weight": 6
      },
      "item-5963": {
        "value": 2,
        "weight": 4
      },
      "item-5964": {
        "value": 9,
        "weight": 6
      },
      "item-5965": {
        "value": 3,
        "weight": 7
      },
      "item-5966": {
        "value": 3,
        "weight": 8
      },
      "item-5967": {
        "value": 4,
        "weight": 4
      },
      "item-5968": {
        "value": 7,
        "weight": 3
      },
      "item-5969": {
        "value": 7,
        "weight": 4
      },
      "item-5970": {
        "value": 8,
        "weight": 9
      },
      "item-5971": {
        "value": 1,
        "weight": 7
      },
      "item-5972": {
        "value": 8,
        "weight": 6
      },
      "item-5973": {
        "value": 2,
        "weight": 4
      },
      "item-5974": {
        "value": 2,
        "weight": 7
      },
      "item-5975": {
        "value": 1,
        "weight": 2
      },
      "item-5976": {
        "value": 1,
        "weight": 5
      },
      "item-5977": {
        "value": 4,
        "weight": 7
      },
      "item-5978": {
        "value": 4,
        "weight": 4
      },
      "item-5979": {
        "value": 4,
        "weight": 6
      },
      "item-5980": {
        "value": 1,
        "weight": 9
      },
      "item-5981": {
        "value": 2,
        "weight": 4
      },
      "item-5982": {
        "value": 2,
        "weight": 1
      },
      "item-5983": {
        "value": 7,
        "weight": 5
      },
      "item-5984": {
        "value": 6,
        "weight": 9
      },
      "item-5985": {
        "value": 1,
        "weight": 5
      },
      "item-5986": {
        "value": 1,
        "weight": 8
      },
      "item-5987": {
        "value": 9,
        "weight": 3
      },
      "item-5988": {
        "value": 4,
        "weight": 4
      },
      "item-5989": {
        "value": 8,
        "weight": 7
      },
      "item-5990": {
        "value": 4,
        "weight": 1
      },
      "item-5991": {
        "value": 7,
        "weight": 1
      },
      "item-5992": {
        "value": 4,
        "weight": 7
      },
      "item-5993": {
        "value": 1,
        "weight": 9
      },
      "item-5994": {
        "value": 9,
        "weight": 8
      },
      "item-5995": {
        "value": 1,
        "weight": 7
      },
      "item-5996": {
        "value": 9,
        "weight": 6
      },
      "item-5997": {
        "value": 7,
        "weight": 1
      },
      "item-5998": {
        "value": 6,
        "weight": 9
      },
      "item-5999": {
        "value": 6,
        "weight": 3
      },
      "item-6000": {
        "value": 7,
        "weight": 4
      },
      "item-6001": {
        "value": 6,
        "weight": 5
      },
      "item-6002": {
        "value": 5,
        "weight": 3
      },
      "item-6003": {
        "value": 4,
        "weight": 5
      },
      "item-6004": {
        "value": 4,
        "weight": 2
      },
      "item-6005": {
        "value": 5,
        "weight": 1
      },
      "item-6006": {
        "value": 3,
        "weight": 4
      },
      "item-6007": {
        "value": 6,
        "weight": 3
      },
      "item-6008": {
        "value": 5,
        "weight": 8
      },
      "item-6009": {
        "value": 6,
        "weight": 3
      },
      "item-6010": {
        "value": 6,
        "weight": 2
      },
      "item-6011": {
        "value": 6,
        "weight": 9
      },
      "item-6012": {
        "value": 9,
        "weight": 1
      },
      "item-6013": {
        "value": 5,
        "weight": 8
      },
      "item-6014": {
        "value": 4,
        "weight": 4
      },
      "item-6015": {
        "value": 6,
        "weight": 2
      },
      "item-6016": {
        "value": 4,
        "weight": 1
      },
      "item-6017": {
        "value": 3,
        "weight": 9
      },
      "item-6018": {
        "value": 8,
        "weight": 9
      },
      "item-6019": {
        "value": 5,
        "weight": 9
      },
      "item-6020": {
        "value": 1,
        "weight": 7
      },
      "item-6021": {
        "value": 1,
        "weight": 5
      },
      "item-6022": {
        "value": 1,
        "weight": 4
      },
      "item-6023": {
        "value": 2,
        "weight": 2
      },
      "item-6024": {
        "value": 9,
        "weight": 4
      },
      "item-6025": {
        "value": 9,
        "weight": 8
      },
      "item-6026": {
        "value": 6,
        "weight": 9
      },
      "item-6027": {
        "value": 4,
        "weight": 9
      },
      "item-6028": {
        "value": 8,
        "weight": 3
      },
      "item-6029": {
        "value": 9,
        "weight": 9
      },
      "item-6030": {
        "value": 1,
        "weight": 4
      },
      "item-6031": {
        "value": 9,
        "weight": 1
      },
      "item-6032": {
        "value": 2,
        "weight": 6
      },
      "item-6033": {
        "value": 3,
        "weight": 4
      },
      "item-6034": {
        "value": 6,
        "weight": 2
      },
      "item-6035": {
        "value": 4,
        "weight": 1
      },
      "item-6036": {
        "value": 1,
        "weight": 4
      },
      "item-6037": {
        "value": 7,
        "weight": 2
      },
      "item-6038": {
        "value": 3,
        "weight": 6
      },
      "item-6039": {
        "value": 2,
        "weight": 8
      },
      "item-6040": {
        "value": 9,
        "weight": 8
      },
      "item-6041": {
        "value": 5,
        "weight": 9
      },
      "item-6042": {
        "value": 9,
        "weight": 6
      },
      "item-6043": {
        "value": 1,
        "weight": 6
      },
      "item-6044": {
        "value": 6,
        "weight": 2
      },
      "item-6045": {
        "value": 5,
        "weight": 3
      },
      "item-6046": {
        "value": 7,
        "weight": 4
      },
      "item-6047": {
        "value": 7,
        "weight": 5
      },
      "item-6048": {
        "value": 3,
        "weight": 4
      },
      "item-6049": {
        "value": 7,
        "weight": 7
      },
      "item-6050": {
        "value": 1,
        "weight": 7
      },
      "item-6051": {
        "value": 1,
        "weight": 3
      },
      "item-6052": {
        "value": 6,
        "weight": 5
      },
      "item-6053": {
        "value": 3,
        "weight": 9
      },
      "item-6054": {
        "value": 6,
        "weight": 5
      },
      "item-6055": {
        "value": 7,
        "weight": 6
      },
      "item-6056": {
        "value": 3,
        "weight": 2
      },
      "item-6057": {
        "value": 7,
        "weight": 2
      },
      "item-6058": {
        "value": 4,
        "weight": 6
      },
      "item-6059": {
        "value": 8,
        "weight": 5
      },
      "item-6060": {
        "value": 3,
        "weight": 5
      },
      "item-6061": {
        "value": 4,
        "weight": 3
      },
      "item-6062": {
        "value": 3,
        "weight": 6
      },
      "item-6063": {
        "value": 6,
        "weight": 3
      },
      "item-6064": {
        "value": 4,
        "weight": 1
      },
      "item-6065": {
        "value": 5,
        "weight": 2
      },
      "item-6066": {
        "value": 7,
        "weight": 8
      },
      "item-6067": {
        "value": 9,
        "weight": 3
      },
      "item-6068": {
        "value": 7,
        "weight": 8
      },
      "item-6069": {
        "value": 9,
        "weight": 1
      },
      "item-6070": {
        "value": 1,
        "weight": 5
      },
      "item-6071": {
        "value": 5,
        "weight": 1
      },
      "item-6072": {
        "value": 3,
        "weight": 9
      },
      "item-6073": {
        "value": 1,
        "weight": 2
      },
      "item-6074": {
        "value": 7,
        "weight": 7
      },
      "item-6075": {
        "value": 7,
        "weight": 2
      },
      "item-6076": {
        "value": 8,
        "weight": 4
      },
      "item-6077": {
        "value": 5,
        "weight": 8
      },
      "item-6078": {
        "value": 7,
        "weight": 1
      },
      "item-6079": {
        "value": 2,
        "weight": 4
      },
      "item-6080": {
        "value": 9,
        "weight": 8
      },
      "item-6081": {
        "value": 3,
        "weight": 8
      },
      "item-6082": {
        "value": 7,
        "weight": 7
      },
      "item-6083": {
        "value": 3,
        "weight": 9
      },
      "item-6084": {
        "value": 4,
        "weight": 1
      },
      "item-6085": {
        "value": 6,
        "weight": 3
      },
      "item-6086": {
        "value": 9,
        "weight": 3
      },
      "item-6087": {
        "value": 5,
        "weight": 1
      },
      "item-6088": {
        "value": 6,
        "weight": 1
      },
      "item-6089": {
        "value": 5,
        "weight": 8
      },
      "item-6090": {
        "value": 1,
        "weight": 2
      },
      "item-6091": {
        "value": 3,
        "weight": 5
      },
      "item-6092": {
        "value": 7,
        "weight": 6
      },
      "item-6093": {
        "value": 7,
        "weight": 8
      },
      "item-6094": {
        "value": 1,
        "weight": 7
      },
      "item-6095": {
        "value": 4,
        "weight": 8
      },
      "item-6096": {
        "value": 7,
        "weight": 8
      },
      "item-6097": {
        "value": 2,
        "weight": 4
      },
      "item-6098": {
        "value": 7,
        "weight": 9
      },
      "item-6099": {
        "value": 6,
        "weight": 6
      },
      "item-6100": {
        "value": 4,
        "weight": 5
      },
      "item-6101": {
        "value": 7,
        "weight": 6
      },
      "item-6102": {
        "value": 3,
        "weight": 5
      },
      "item-6103": {
        "value": 1,
        "weight": 9
      },
      "item-6104": {
        "value": 2,
        "weight": 2
      },
      "item-6105": {
        "value": 8,
        "weight": 9
      },
      "item-6106": {
        "value": 8,
        "weight": 6
      },
      "item-6107": {
        "value": 4,
        "weight": 8
      },
      "item-6108": {
        "value": 7,
        "weight": 1
      },
      "item-6109": {
        "value": 2,
        "weight": 9
      },
      "item-6110": {
        "value": 5,
        "weight": 3
      },
      "item-6111": {
        "value": 8,
        "weight": 3
      },
      "item-6112": {
        "value": 5,
        "weight": 3
      },
      "item-6113": {
        "value": 6,
        "weight": 1
      },
      "item-6114": {
        "value": 8,
        "weight": 8
      },
      "item-6115": {
        "value": 7,
        "weight": 1
      },
      "item-6116": {
        "value": 3,
        "weight": 6
      },
      "item-6117": {
        "value": 7,
        "weight": 3
      },
      "item-6118": {
        "value": 6,
        "weight": 6
      },
      "item-6119": {
        "value": 4,
        "weight": 3
      },
      "item-6120": {
        "value": 7,
        "weight": 6
      },
      "item-6121": {
        "value": 8,
        "weight": 3
      },
      "item-6122": {
        "value": 4,
        "weight": 7
      },
      "item-6123": {
        "value": 7,
        "weight": 3
      },
      "item-6124": {
        "value": 6,
        "weight": 7
      },
      "item-6125": {
        "value": 1,
        "weight": 1
      },
      "item-6126": {
        "value": 1,
        "weight": 4
      },
      "item-6127": {
        "value": 2,
        "weight": 7
      },
      "item-6128": {
        "value": 4,
        "weight": 9
      },
      "item-6129": {
        "value": 5,
        "weight": 1
      },
      "item-6130": {
        "value": 5,
        "weight": 1
      },
      "item-6131": {
        "value": 1,
        "weight": 1
      },
      "item-6132": {
        "value": 6,
        "weight": 3
      },
      "item-6133": {
        "value": 3,
        "weight": 1
      },
      "item-6134": {
        "value": 1,
        "weight": 4
      },
      "item-6135": {
        "value": 2,
        "weight": 2
      },
      "item-6136": {
        "value": 9,
        "weight": 3
      },
      "item-6137": {
        "value": 8,
        "weight": 7
      },
      "item-6138": {
        "value": 1,
        "weight": 3
      },
      "item-6139": {
        "value": 7,
        "weight": 2
      },
      "item-6140": {
        "value": 5,
        "weight": 7
      },
      "item-6141": {
        "value": 3,
        "weight": 5
      },
      "item-6142": {
        "value": 5,
        "weight": 2
      },
      "item-6143": {
        "value": 8,
        "weight": 8
      },
      "item-6144": {
        "value": 4,
        "weight": 8
      },
      "item-6145": {
        "value": 2,
        "weight": 7
      },
      "item-6146": {
        "value": 8,
        "weight": 1
      },
      "item-6147": {
        "value": 8,
        "weight": 8
      },
      "item-6148": {
        "value": 1,
        "weight": 8
      },
      "item-6149": {
        "value": 7,
        "weight": 7
      },
      "item-6150": {
        "value": 2,
        "weight": 6
      },
      "item-6151": {
        "value": 5,
        "weight": 2
      },
      "item-6152": {
        "value": 2,
        "weight": 3
      },
      "item-6153": {
        "value": 8,
        "weight": 8
      },
      "item-6154": {
        "value": 5,
        "weight": 3
      },
      "item-6155": {
        "value": 3,
        "weight": 2
      },
      "item-6156": {
        "value": 4,
        "weight": 5
      },
      "item-6157": {
        "value": 8,
        "weight": 8
      },
      "item-6158": {
        "value": 9,
        "weight": 6
      },
      "item-6159": {
        "value": 5,
        "weight": 6
      },
      "item-6160": {
        "value": 7,
        "weight": 2
      },
      "item-6161": {
        "value": 3,
        "weight": 3
      },
      "item-6162": {
        "value": 2,
        "weight": 9
      },
      "item-6163": {
        "value": 2,
        "weight": 1
      },
      "item-6164": {
        "value": 7,
        "weight": 5
      },
      "item-6165": {
        "value": 4,
        "weight": 2
      },
      "item-6166": {
        "value": 6,
        "weight": 6
      },
      "item-6167": {
        "value": 9,
        "weight": 7
      },
      "item-6168": {
        "value": 1,
        "weight": 4
      },
      "item-6169": {
        "value": 4,
        "weight": 1
      },
      "item-6170": {
        "value": 2,
        "weight": 6
      },
      "item-6171": {
        "value": 8,
        "weight": 6
      },
      "item-6172": {
        "value": 3,
        "weight": 6
      },
      "item-6173": {
        "value": 6,
        "weight": 9
      },
      "item-6174": {
        "value": 3,
        "weight": 2
      },
      "item-6175": {
        "value": 6,
        "weight": 9
      },
      "item-6176": {
        "value": 2,
        "weight": 3
      },
      "item-6177": {
        "value": 5,
        "weight": 3
      },
      "item-6178": {
        "value": 3,
        "weight": 7
      },
      "item-6179": {
        "value": 8,
        "weight": 5
      },
      "item-6180": {
        "value": 7,
        "weight": 8
      },
      "item-6181": {
        "value": 4,
        "weight": 7
      },
      "item-6182": {
        "value": 2,
        "weight": 5
      },
      "item-6183": {
        "value": 1,
        "weight": 7
      },
      "item-6184": {
        "value": 6,
        "weight": 3
      },
      "item-6185": {
        "value": 3,
        "weight": 6
      },
      "item-6186": {
        "value": 9,
        "weight": 3
      },
      "item-6187": {
        "value": 5,
        "weight": 6
      },
      "item-6188": {
        "value": 2,
        "weight": 1
      },
      "item-6189": {
        "value": 6,
        "weight": 2
      },
      "item-6190": {
        "value": 9,
        "weight": 1
      },
      "item-6191": {
        "value": 9,
        "weight": 2
      },
      "item-6192": {
        "value": 7,
        "weight": 2
      },
      "item-6193": {
        "value": 7,
        "weight": 6
      },
      "item-6194": {
        "value": 8,
        "weight": 5
      },
      "item-6195": {
        "value": 5,
        "weight": 7
      },
      "item-6196": {
        "value": 7,
        "weight": 2
      },
      "item-6197": {
        "value": 1,
        "weight": 7
      },
      "item-6198": {
        "value": 6,
        "weight": 3
      },
      "item-6199": {
        "value": 6,
        "weight": 7
      },
      "item-6200": {
        "value": 2,
        "weight": 9
      },
      "item-6201": {
        "value": 6,
        "weight": 9
      },
      "item-6202": {
        "value": 8,
        "weight": 5
      },
      "item-6203": {
        "value": 3,
        "weight": 5
      },
      "item-6204": {
        "value": 3,
        "weight": 7
      },
      "item-6205": {
        "value": 9,
        "weight": 5
      },
      "item-6206": {
        "value": 2,
        "weight": 7
      },
      "item-6207": {
        "value": 9,
        "weight": 2
      },
      "item-6208": {
        "value": 7,
        "weight": 8
      },
      "item-6209": {
        "value": 7,
        "weight": 6
      },
      "item-6210": {
        "value": 3,
        "weight": 9
      },
      "item-6211": {
        "value": 2,
        "weight": 6
      },
      "item-6212": {
        "value": 3,
        "weight": 6
      },
      "item-6213": {
        "value": 4,
        "weight": 8
      },
      "item-6214": {
        "value": 7,
        "weight": 5
      },
      "item-6215": {
        "value": 5,
        "weight": 7
      },
      "item-6216": {
        "value": 1,
        "weight": 2
      },
      "item-6217": {
        "value": 8,
        "weight": 4
      },
      "item-6218": {
        "value": 5,
        "weight": 7
      },
      "item-6219": {
        "value": 8,
        "weight": 2
      },
      "item-6220": {
        "value": 7,
        "weight": 8
      },
      "item-6221": {
        "value": 7,
        "weight": 5
      },
      "item-6222": {
        "value": 8,
        "weight": 5
      },
      "item-6223": {
        "value": 1,
        "weight": 2
      },
      "item-6224": {
        "value": 9,
        "weight": 3
      },
      "item-6225": {
        "value": 7,
        "weight": 8
      },
      "item-6226": {
        "value": 5,
        "weight": 9
      },
      "item-6227": {
        "value": 7,
        "weight": 9
      },
      "item-6228": {
        "value": 7,
        "weight": 9
      },
      "item-6229": {
        "value": 8,
        "weight": 7
      },
      "item-6230": {
        "value": 3,
        "weight": 9
      },
      "item-6231": {
        "value": 7,
        "weight": 5
      },
      "item-6232": {
        "value": 2,
        "weight": 5
      },
      "item-6233": {
        "value": 8,
        "weight": 2
      },
      "item-6234": {
        "value": 8,
        "weight": 5
      },
      "item-6235": {
        "value": 2,
        "weight": 3
      },
      "item-6236": {
        "value": 6,
        "weight": 2
      },
      "item-6237": {
        "value": 2,
        "weight": 6
      },
      "item-6238": {
        "value": 1,
        "weight": 7
      },
      "item-6239": {
        "value": 8,
        "weight": 8
      },
      "item-6240": {
        "value": 4,
        "weight": 3
      },
      "item-6241": {
        "value": 7,
        "weight": 5
      },
      "item-6242": {
        "value": 5,
        "weight": 1
      },
      "item-6243": {
        "value": 3,
        "weight": 8
      },
      "item-6244": {
        "value": 7,
        "weight": 4
      },
      "item-6245": {
        "value": 1,
        "weight": 5
      },
      "item-6246": {
        "value": 8,
        "weight": 9
      },
      "item-6247": {
        "value": 8,
        "weight": 7
      },
      "item-6248": {
        "value": 2,
        "weight": 8
      },
      "item-6249": {
        "value": 3,
        "weight": 1
      },
      "item-6250": {
        "value": 3,
        "weight": 1
      },
      "item-6251": {
        "value": 3,
        "weight": 3
      },
      "item-6252": {
        "value": 4,
        "weight": 3
      },
      "item-6253": {
        "value": 3,
        "weight": 4
      },
      "item-6254": {
        "value": 1,
        "weight": 1
      },
      "item-6255": {
        "value": 3,
        "weight": 7
      },
      "item-6256": {
        "value": 6,
        "weight": 3
      },
      "item-6257": {
        "value": 3,
        "weight": 3
      },
      "item-6258": {
        "value": 5,
        "weight": 3
      },
      "item-6259": {
        "value": 6,
        "weight": 1
      },
      "item-6260": {
        "value": 5,
        "weight": 9
      },
      "item-6261": {
        "value": 7,
        "weight": 9
      },
      "item-6262": {
        "value": 5,
        "weight": 3
      },
      "item-6263": {
        "value": 9,
        "weight": 5
      },
      "item-6264": {
        "value": 2,
        "weight": 2
      },
      "item-6265": {
        "value": 7,
        "weight": 2
      },
      "item-6266": {
        "value": 2,
        "weight": 1
      },
      "item-6267": {
        "value": 6,
        "weight": 3
      },
      "item-6268": {
        "value": 2,
        "weight": 5
      },
      "item-6269": {
        "value": 3,
        "weight": 5
      },
      "item-6270": {
        "value": 7,
        "weight": 2
      },
      "item-6271": {
        "value": 7,
        "weight": 9
      },
      "item-6272": {
        "value": 9,
        "weight": 2
      },
      "item-6273": {
        "value": 3,
        "weight": 6
      },
      "item-6274": {
        "value": 4,
        "weight": 6
      },
      "item-6275": {
        "value": 6,
        "weight": 9
      },
      "item-6276": {
        "value": 8,
        "weight": 4
      },
      "item-6277": {
        "value": 6,
        "weight": 4
      },
      "item-6278": {
        "value": 7,
        "weight": 4
      },
      "item-6279": {
        "value": 2,
        "weight": 2
      },
      "item-6280": {
        "value": 7,
        "weight": 2
      },
      "item-6281": {
        "value": 5,
        "weight": 4
      },
      "item-6282": {
        "value": 1,
        "weight": 8
      },
      "item-6283": {
        "value": 5,
        "weight": 8
      },
      "item-6284": {
        "value": 6,
        "weight": 3
      },
      "item-6285": {
        "value": 1,
        "weight": 1
      },
      "item-6286": {
        "value": 4,
        "weight": 8
      },
      "item-6287": {
        "value": 5,
        "weight": 2
      },
      "item-6288": {
        "value": 2,
        "weight": 6
      },
      "item-6289": {
        "value": 9,
        "weight": 8
      },
      "item-6290": {
        "value": 4,
        "weight": 4
      },
      "item-6291": {
        "value": 7,
        "weight": 2
      },
      "item-6292": {
        "value": 9,
        "weight": 8
      },
      "item-6293": {
        "value": 3,
        "weight": 8
      },
      "item-6294": {
        "value": 6,
        "weight": 8
      },
      "item-6295": {
        "value": 9,
        "weight": 6
      },
      "item-6296": {
        "value": 3,
        "weight": 9
      },
      "item-6297": {
        "value": 4,
        "weight": 1
      },
      "item-6298": {
        "value": 6,
        "weight": 2
      },
      "item-6299": {
        "value": 4,
        "weight": 6
      },
      "item-6300": {
        "value": 5,
        "weight": 6
      },
      "item-6301": {
        "value": 6,
        "weight": 9
      },
      "item-6302": {
        "value": 5,
        "weight": 3
      },
      "item-6303": {
        "value": 6,
        "weight": 9
      },
      "item-6304": {
        "value": 3,
        "weight": 7
      },
      "item-6305": {
        "value": 9,
        "weight": 2
      },
      "item-6306": {
        "value": 8,
        "weight": 2
      },
      "item-6307": {
        "value": 1,
        "weight": 2
      },
      "item-6308": {
        "value": 5,
        "weight": 4
      },
      "item-6309": {
        "value": 7,
        "weight": 7
      },
      "item-6310": {
        "value": 1,
        "weight": 9
      },
      "item-6311": {
        "value": 5,
        "weight": 1
      },
      "item-6312": {
        "value": 3,
        "weight": 2
      },
      "item-6313": {
        "value": 9,
        "weight": 7
      },
      "item-6314": {
        "value": 9,
        "weight": 6
      },
      "item-6315": {
        "value": 6,
        "weight": 3
      },
      "item-6316": {
        "value": 4,
        "weight": 6
      },
      "item-6317": {
        "value": 8,
        "weight": 5
      },
      "item-6318": {
        "value": 3,
        "weight": 1
      },
      "item-6319": {
        "value": 4,
        "weight": 4
      },
      "item-6320": {
        "value": 7,
        "weight": 9
      },
      "item-6321": {
        "value": 4,
        "weight": 6
      },
      "item-6322": {
        "value": 8,
        "weight": 8
      },
      "item-6323": {
        "value": 6,
        "weight": 7
      },
      "item-6324": {
        "value": 6,
        "weight": 1
      },
      "item-6325": {
        "value": 9,
        "weight": 5
      },
      "item-6326": {
        "value": 3,
        "weight": 3
      },
      "item-6327": {
        "value": 1,
        "weight": 4
      },
      "item-6328": {
        "value": 4,
        "weight": 4
      },
      "item-6329": {
        "value": 2,
        "weight": 9
      },
      "item-6330": {
        "value": 1,
        "weight": 7
      },
      "item-6331": {
        "value": 5,
        "weight": 9
      },
      "item-6332": {
        "value": 1,
        "weight": 8
      },
      "item-6333": {
        "value": 2,
        "weight": 9
      },
      "item-6334": {
        "value": 2,
        "weight": 9
      },
      "item-6335": {
        "value": 3,
        "weight": 8
      },
      "item-6336": {
        "value": 9,
        "weight": 3
      },
      "item-6337": {
        "value": 5,
        "weight": 3
      },
      "item-6338": {
        "value": 2,
        "weight": 1
      },
      "item-6339": {
        "value": 6,
        "weight": 4
      },
      "item-6340": {
        "value": 2,
        "weight": 2
      },
      "item-6341": {
        "value": 1,
        "weight": 9
      },
      "item-6342": {
        "value": 3,
        "weight": 7
      },
      "item-6343": {
        "value": 9,
        "weight": 9
      },
      "item-6344": {
        "value": 3,
        "weight": 2
      },
      "item-6345": {
        "value": 3,
        "weight": 4
      },
      "item-6346": {
        "value": 9,
        "weight": 3
      },
      "item-6347": {
        "value": 3,
        "weight": 4
      },
      "item-6348": {
        "value": 7,
        "weight": 3
      },
      "item-6349": {
        "value": 3,
        "weight": 5
      },
      "item-6350": {
        "value": 5,
        "weight": 3
      },
      "item-6351": {
        "value": 6,
        "weight": 1
      },
      "item-6352": {
        "value": 4,
        "weight": 9
      },
      "item-6353": {
        "value": 8,
        "weight": 9
      },
      "item-6354": {
        "value": 8,
        "weight": 2
      },
      "item-6355": {
        "value": 3,
        "weight": 4
      },
      "item-6356": {
        "value": 4,
        "weight": 8
      },
      "item-6357": {
        "value": 6,
        "weight": 6
      },
      "item-6358": {
        "value": 8,
        "weight": 4
      },
      "item-6359": {
        "value": 7,
        "weight": 6
      },
      "item-6360": {
        "value": 6,
        "weight": 8
      },
      "item-6361": {
        "value": 8,
        "weight": 2
      },
      "item-6362": {
        "value": 7,
        "weight": 5
      },
      "item-6363": {
        "value": 6,
        "weight": 3
      },
      "item-6364": {
        "value": 4,
        "weight": 1
      },
      "item-6365": {
        "value": 8,
        "weight": 3
      },
      "item-6366": {
        "value": 4,
        "weight": 2
      },
      "item-6367": {
        "value": 9,
        "weight": 5
      },
      "item-6368": {
        "value": 8,
        "weight": 7
      },
      "item-6369": {
        "value": 7,
        "weight": 4
      },
      "item-6370": {
        "value": 2,
        "weight": 3
      },
      "item-6371": {
        "value": 1,
        "weight": 4
      },
      "item-6372": {
        "value": 8,
        "weight": 4
      },
      "item-6373": {
        "value": 7,
        "weight": 8
      },
      "item-6374": {
        "value": 5,
        "weight": 5
      },
      "item-6375": {
        "value": 9,
        "weight": 8
      },
      "item-6376": {
        "value": 3,
        "weight": 9
      },
      "item-6377": {
        "value": 1,
        "weight": 1
      },
      "item-6378": {
        "value": 9,
        "weight": 1
      },
      "item-6379": {
        "value": 4,
        "weight": 7
      },
      "item-6380": {
        "value": 9,
        "weight": 5
      },
      "item-6381": {
        "value": 5,
        "weight": 7
      },
      "item-6382": {
        "value": 4,
        "weight": 1
      },
      "item-6383": {
        "value": 4,
        "weight": 9
      },
      "item-6384": {
        "value": 4,
        "weight": 5
      },
      "item-6385": {
        "value": 8,
        "weight": 5
      },
      "item-6386": {
        "value": 4,
        "weight": 7
      },
      "item-6387": {
        "value": 1,
        "weight": 4
      },
      "item-6388": {
        "value": 5,
        "weight": 3
      },
      "item-6389": {
        "value": 8,
        "weight": 6
      },
      "item-6390": {
        "value": 7,
        "weight": 8
      },
      "item-6391": {
        "value": 8,
        "weight": 9
      },
      "item-6392": {
        "value": 7,
        "weight": 7
      },
      "item-6393": {
        "value": 6,
        "weight": 9
      },
      "item-6394": {
        "value": 6,
        "weight": 4
      },
      "item-6395": {
        "value": 5,
        "weight": 6
      },
      "item-6396": {
        "value": 5,
        "weight": 8
      },
      "item-6397": {
        "value": 8,
        "weight": 2
      },
      "item-6398": {
        "value": 8,
        "weight": 6
      },
      "item-6399": {
        "value": 7,
        "weight": 4
      },
      "item-6400": {
        "value": 1,
        "weight": 8
      },
      "item-6401": {
        "value": 8,
        "weight": 8
      },
      "item-6402": {
        "value": 9,
        "weight": 6
      },
      "item-6403": {
        "value": 6,
        "weight": 9
      },
      "item-6404": {
        "value": 5,
        "weight": 3
      },
      "item-6405": {
        "value": 3,
        "weight": 2
      },
      "item-6406": {
        "value": 2,
        "weight": 3
      },
      "item-6407": {
        "value": 9,
        "weight": 5
      },
      "item-6408": {
        "value": 9,
        "weight": 5
      },
      "item-6409": {
        "value": 9,
        "weight": 6
      },
      "item-6410": {
        "value": 3,
        "weight": 8
      },
      "item-6411": {
        "value": 7,
        "weight": 9
      },
      "item-6412": {
        "value": 7,
        "weight": 1
      },
      "item-6413": {
        "value": 1,
        "weight": 6
      },
      "item-6414": {
        "value": 8,
        "weight": 7
      },
      "item-6415": {
        "value": 9,
        "weight": 9
      },
      "item-6416": {
        "value": 1,
        "weight": 1
      },
      "item-6417": {
        "value": 1,
        "weight": 8
      },
      "item-6418": {
        "value": 1,
        "weight": 4
      },
      "item-6419": {
        "value": 7,
        "weight": 5
      },
      "item-6420": {
        "value": 9,
        "weight": 9
      },
      "item-6421": {
        "value": 4,
        "weight": 8
      },
      "item-6422": {
        "value": 3,
        "weight": 5
      },
      "item-6423": {
        "value": 4,
        "weight": 5
      },
      "item-6424": {
        "value": 2,
        "weight": 6
      },
      "item-6425": {
        "value": 3,
        "weight": 4
      },
      "item-6426": {
        "value": 6,
        "weight": 3
      },
      "item-6427": {
        "value": 7,
        "weight": 4
      },
      "item-6428": {
        "value": 6,
        "weight": 8
      },
      "item-6429": {
        "value": 6,
        "weight": 1
      },
      "item-6430": {
        "value": 7,
        "weight": 8
      },
      "item-6431": {
        "value": 6,
        "weight": 4
      },
      "item-6432": {
        "value": 7,
        "weight": 6
      },
      "item-6433": {
        "value": 3,
        "weight": 3
      },
      "item-6434": {
        "value": 4,
        "weight": 6
      },
      "item-6435": {
        "value": 5,
        "weight": 6
      },
      "item-6436": {
        "value": 6,
        "weight": 5
      },
      "item-6437": {
        "value": 6,
        "weight": 9
      },
      "item-6438": {
        "value": 3,
        "weight": 2
      },
      "item-6439": {
        "value": 6,
        "weight": 1
      },
      "item-6440": {
        "value": 5,
        "weight": 9
      },
      "item-6441": {
        "value": 5,
        "weight": 8
      },
      "item-6442": {
        "value": 8,
        "weight": 5
      },
      "item-6443": {
        "value": 4,
        "weight": 3
      },
      "item-6444": {
        "value": 6,
        "weight": 7
      },
      "item-6445": {
        "value": 4,
        "weight": 9
      },
      "item-6446": {
        "value": 1,
        "weight": 9
      },
      "item-6447": {
        "value": 1,
        "weight": 8
      },
      "item-6448": {
        "value": 4,
        "weight": 8
      },
      "item-6449": {
        "value": 1,
        "weight": 4
      },
      "item-6450": {
        "value": 5,
        "weight": 6
      },
      "item-6451": {
        "value": 7,
        "weight": 7
      },
      "item-6452": {
        "value": 1,
        "weight": 9
      },
      "item-6453": {
        "value": 8,
        "weight": 4
      },
      "item-6454": {
        "value": 1,
        "weight": 7
      },
      "item-6455": {
        "value": 9,
        "weight": 8
      },
      "item-6456": {
        "value": 7,
        "weight": 3
      },
      "item-6457": {
        "value": 9,
        "weight": 7
      },
      "item-6458": {
        "value": 1,
        "weight": 2
      },
      "item-6459": {
        "value": 3,
        "weight": 6
      },
      "item-6460": {
        "value": 1,
        "weight": 8
      },
      "item-6461": {
        "value": 6,
        "weight": 7
      },
      "item-6462": {
        "value": 1,
        "weight": 7
      },
      "item-6463": {
        "value": 4,
        "weight": 8
      },
      "item-6464": {
        "value": 1,
        "weight": 6
      },
      "item-6465": {
        "value": 6,
        "weight": 3
      },
      "item-6466": {
        "value": 4,
        "weight": 7
      },
      "item-6467": {
        "value": 2,
        "weight": 9
      },
      "item-6468": {
        "value": 3,
        "weight": 9
      },
      "item-6469": {
        "value": 1,
        "weight": 7
      },
      "item-6470": {
        "value": 4,
        "weight": 8
      },
      "item-6471": {
        "value": 5,
        "weight": 8
      },
      "item-6472": {
        "value": 6,
        "weight": 5
      },
      "item-6473": {
        "value": 1,
        "weight": 9
      },
      "item-6474": {
        "value": 5,
        "weight": 2
      },
      "item-6475": {
        "value": 6,
        "weight": 4
      },
      "item-6476": {
        "value": 1,
        "weight": 8
      },
      "item-6477": {
        "value": 2,
        "weight": 4
      },
      "item-6478": {
        "value": 1,
        "weight": 5
      },
      "item-6479": {
        "value": 8,
        "weight": 7
      },
      "item-6480": {
        "value": 9,
        "weight": 4
      },
      "item-6481": {
        "value": 6,
        "weight": 7
      },
      "item-6482": {
        "value": 8,
        "weight": 5
      },
      "item-6483": {
        "value": 4,
        "weight": 1
      },
      "item-6484": {
        "value": 2,
        "weight": 1
      },
      "item-6485": {
        "value": 6,
        "weight": 3
      },
      "item-6486": {
        "value": 4,
        "weight": 1
      },
      "item-6487": {
        "value": 2,
        "weight": 2
      },
      "item-6488": {
        "value": 1,
        "weight": 7
      },
      "item-6489": {
        "value": 6,
        "weight": 3
      },
      "item-6490": {
        "value": 3,
        "weight": 8
      },
      "item-6491": {
        "value": 9,
        "weight": 8
      },
      "item-6492": {
        "value": 5,
        "weight": 1
      },
      "item-6493": {
        "value": 6,
        "weight": 5
      },
      "item-6494": {
        "value": 6,
        "weight": 5
      },
      "item-6495": {
        "value": 5,
        "weight": 9
      },
      "item-6496": {
        "value": 4,
        "weight": 3
      },
      "item-6497": {
        "value": 7,
        "weight": 8
      },
      "item-6498": {
        "value": 1,
        "weight": 2
      },
      "item-6499": {
        "value": 5,
        "weight": 5
      },
      "item-6500": {
        "value": 3,
        "weight": 7
      },
      "item-6501": {
        "value": 3,
        "weight": 7
      },
      "item-6502": {
        "value": 8,
        "weight": 5
      },
      "item-6503": {
        "value": 5,
        "weight": 7
      },
      "item-6504": {
        "value": 3,
        "weight": 4
      },
      "item-6505": {
        "value": 7,
        "weight": 2
      },
      "item-6506": {
        "value": 1,
        "weight": 6
      },
      "item-6507": {
        "value": 1,
        "weight": 9
      },
      "item-6508": {
        "value": 9,
        "weight": 4
      },
      "item-6509": {
        "value": 6,
        "weight": 1
      },
      "item-6510": {
        "value": 2,
        "weight": 6
      },
      "item-6511": {
        "value": 8,
        "weight": 8
      },
      "item-6512": {
        "value": 3,
        "weight": 7
      },
      "item-6513": {
        "value": 6,
        "weight": 1
      },
      "item-6514": {
        "value": 6,
        "weight": 2
      },
      "item-6515": {
        "value": 3,
        "weight": 7
      },
      "item-6516": {
        "value": 4,
        "weight": 9
      },
      "item-6517": {
        "value": 6,
        "weight": 3
      },
      "item-6518": {
        "value": 7,
        "weight": 2
      },
      "item-6519": {
        "value": 9,
        "weight": 2
      },
      "item-6520": {
        "value": 1,
        "weight": 3
      },
      "item-6521": {
        "value": 9,
        "weight": 4
      },
      "item-6522": {
        "value": 3,
        "weight": 6
      },
      "item-6523": {
        "value": 2,
        "weight": 4
      },
      "item-6524": {
        "value": 7,
        "weight": 4
      },
      "item-6525": {
        "value": 3,
        "weight": 7
      },
      "item-6526": {
        "value": 2,
        "weight": 3
      },
      "item-6527": {
        "value": 2,
        "weight": 3
      },
      "item-6528": {
        "value": 3,
        "weight": 1
      },
      "item-6529": {
        "value": 1,
        "weight": 3
      },
      "item-6530": {
        "value": 5,
        "weight": 9
      },
      "item-6531": {
        "value": 2,
        "weight": 2
      },
      "item-6532": {
        "value": 5,
        "weight": 6
      },
      "item-6533": {
        "value": 7,
        "weight": 6
      },
      "item-6534": {
        "value": 5,
        "weight": 1
      },
      "item-6535": {
        "value": 1,
        "weight": 5
      },
      "item-6536": {
        "value": 9,
        "weight": 2
      },
      "item-6537": {
        "value": 2,
        "weight": 9
      },
      "item-6538": {
        "value": 4,
        "weight": 2
      },
      "item-6539": {
        "value": 3,
        "weight": 8
      },
      "item-6540": {
        "value": 4,
        "weight": 9
      },
      "item-6541": {
        "value": 4,
        "weight": 3
      },
      "item-6542": {
        "value": 6,
        "weight": 6
      },
      "item-6543": {
        "value": 2,
        "weight": 6
      },
      "item-6544": {
        "value": 9,
        "weight": 9
      },
      "item-6545": {
        "value": 6,
        "weight": 8
      },
      "item-6546": {
        "value": 8,
        "weight": 3
      },
      "item-6547": {
        "value": 9,
        "weight": 6
      },
      "item-6548": {
        "value": 5,
        "weight": 5
      },
      "item-6549": {
        "value": 4,
        "weight": 5
      },
      "item-6550": {
        "value": 1,
        "weight": 1
      },
      "item-6551": {
        "value": 3,
        "weight": 3
      },
      "item-6552": {
        "value": 2,
        "weight": 3
      },
      "item-6553": {
        "value": 5,
        "weight": 8
      },
      "item-6554": {
        "value": 2,
        "weight": 8
      },
      "item-6555": {
        "value": 2,
        "weight": 6
      },
      "item-6556": {
        "value": 4,
        "weight": 4
      },
      "item-6557": {
        "value": 4,
        "weight": 3
      },
      "item-6558": {
        "value": 3,
        "weight": 1
      },
      "item-6559": {
        "value": 4,
        "weight": 7
      },
      "item-6560": {
        "value": 8,
        "weight": 1
      },
      "item-6561": {
        "value": 7,
        "weight": 2
      },
      "item-6562": {
        "value": 3,
        "weight": 6
      },
      "item-6563": {
        "value": 2,
        "weight": 6
      },
      "item-6564": {
        "value": 9,
        "weight": 1
      },
      "item-6565": {
        "value": 9,
        "weight": 6
      },
      "item-6566": {
        "value": 1,
        "weight": 7
      },
      "item-6567": {
        "value": 2,
        "weight": 9
      },
      "item-6568": {
        "value": 8,
        "weight": 6
      },
      "item-6569": {
        "value": 1,
        "weight": 4
      },
      "item-6570": {
        "value": 5,
        "weight": 2
      },
      "item-6571": {
        "value": 2,
        "weight": 4
      },
      "item-6572": {
        "value": 5,
        "weight": 9
      },
      "item-6573": {
        "value": 8,
        "weight": 5
      },
      "item-6574": {
        "value": 3,
        "weight": 5
      },
      "item-6575": {
        "value": 9,
        "weight": 6
      },
      "item-6576": {
        "value": 3,
        "weight": 6
      },
      "item-6577": {
        "value": 3,
        "weight": 8
      },
      "item-6578": {
        "value": 6,
        "weight": 3
      },
      "item-6579": {
        "value": 2,
        "weight": 6
      },
      "item-6580": {
        "value": 7,
        "weight": 7
      },
      "item-6581": {
        "value": 9,
        "weight": 7
      },
      "item-6582": {
        "value": 2,
        "weight": 9
      },
      "item-6583": {
        "value": 8,
        "weight": 1
      },
      "item-6584": {
        "value": 1,
        "weight": 8
      },
      "item-6585": {
        "value": 4,
        "weight": 1
      },
      "item-6586": {
        "value": 4,
        "weight": 6
      },
      "item-6587": {
        "value": 1,
        "weight": 9
      },
      "item-6588": {
        "value": 5,
        "weight": 5
      },
      "item-6589": {
        "value": 2,
        "weight": 2
      },
      "item-6590": {
        "value": 7,
        "weight": 3
      },
      "item-6591": {
        "value": 5,
        "weight": 3
      },
      "item-6592": {
        "value": 6,
        "weight": 8
      },
      "item-6593": {
        "value": 7,
        "weight": 7
      },
      "item-6594": {
        "value": 3,
        "weight": 3
      },
      "item-6595": {
        "value": 1,
        "weight": 7
      },
      "item-6596": {
        "value": 5,
        "weight": 6
      },
      "item-6597": {
        "value": 1,
        "weight": 6
      },
      "item-6598": {
        "value": 5,
        "weight": 4
      },
      "item-6599": {
        "value": 6,
        "weight": 9
      },
      "item-6600": {
        "value": 7,
        "weight": 5
      },
      "item-6601": {
        "value": 2,
        "weight": 5
      },
      "item-6602": {
        "value": 9,
        "weight": 7
      },
      "item-6603": {
        "value": 9,
        "weight": 5
      },
      "item-6604": {
        "value": 8,
        "weight": 5
      },
      "item-6605": {
        "value": 6,
        "weight": 9
      },
      "item-6606": {
        "value": 4,
        "weight": 5
      },
      "item-6607": {
        "value": 8,
        "weight": 4
      },
      "item-6608": {
        "value": 2,
        "weight": 8
      },
      "item-6609": {
        "value": 9,
        "weight": 4
      },
      "item-6610": {
        "value": 3,
        "weight": 2
      },
      "item-6611": {
        "value": 8,
        "weight": 3
      },
      "item-6612": {
        "value": 4,
        "weight": 6
      },
      "item-6613": {
        "value": 2,
        "weight": 2
      },
      "item-6614": {
        "value": 8,
        "weight": 9
      },
      "item-6615": {
        "value": 5,
        "weight": 1
      },
      "item-6616": {
        "value": 5,
        "weight": 2
      },
      "item-6617": {
        "value": 1,
        "weight": 1
      },
      "item-6618": {
        "value": 2,
        "weight": 1
      },
      "item-6619": {
        "value": 6,
        "weight": 3
      },
      "item-6620": {
        "value": 4,
        "weight": 9
      },
      "item-6621": {
        "value": 7,
        "weight": 4
      },
      "item-6622": {
        "value": 2,
        "weight": 1
      },
      "item-6623": {
        "value": 7,
        "weight": 2
      },
      "item-6624": {
        "value": 1,
        "weight": 5
      },
      "item-6625": {
        "value": 1,
        "weight": 8
      },
      "item-6626": {
        "value": 9,
        "weight": 7
      },
      "item-6627": {
        "value": 5,
        "weight": 1
      },
      "item-6628": {
        "value": 5,
        "weight": 6
      },
      "item-6629": {
        "value": 5,
        "weight": 2
      },
      "item-6630": {
        "value": 1,
        "weight": 4
      },
      "item-6631": {
        "value": 3,
        "weight": 7
      },
      "item-6632": {
        "value": 1,
        "weight": 7
      },
      "item-6633": {
        "value": 2,
        "weight": 4
      },
      "item-6634": {
        "value": 8,
        "weight": 5
      },
      "item-6635": {
        "value": 5,
        "weight": 4
      },
      "item-6636": {
        "value": 5,
        "weight": 3
      },
      "item-6637": {
        "value": 1,
        "weight": 1
      },
      "item-6638": {
        "value": 8,
        "weight": 8
      },
      "item-6639": {
        "value": 2,
        "weight": 5
      },
      "item-6640": {
        "value": 8,
        "weight": 5
      },
      "item-6641": {
        "value": 8,
        "weight": 1
      },
      "item-6642": {
        "value": 7,
        "weight": 9
      },
      "item-6643": {
        "value": 6,
        "weight": 4
      },
      "item-6644": {
        "value": 6,
        "weight": 8
      },
      "item-6645": {
        "value": 7,
        "weight": 4
      },
      "item-6646": {
        "value": 7,
        "weight": 1
      },
      "item-6647": {
        "value": 7,
        "weight": 9
      },
      "item-6648": {
        "value": 8,
        "weight": 2
      },
      "item-6649": {
        "value": 8,
        "weight": 3
      },
      "item-6650": {
        "value": 9,
        "weight": 3
      },
      "item-6651": {
        "value": 4,
        "weight": 4
      },
      "item-6652": {
        "value": 5,
        "weight": 6
      },
      "item-6653": {
        "value": 2,
        "weight": 7
      },
      "item-6654": {
        "value": 2,
        "weight": 6
      },
      "item-6655": {
        "value": 8,
        "weight": 1
      },
      "item-6656": {
        "value": 6,
        "weight": 5
      },
      "item-6657": {
        "value": 7,
        "weight": 7
      },
      "item-6658": {
        "value": 8,
        "weight": 5
      },
      "item-6659": {
        "value": 1,
        "weight": 9
      },
      "item-6660": {
        "value": 1,
        "weight": 6
      },
      "item-6661": {
        "value": 3,
        "weight": 8
      },
      "item-6662": {
        "value": 7,
        "weight": 7
      },
      "item-6663": {
        "value": 2,
        "weight": 7
      },
      "item-6664": {
        "value": 4,
        "weight": 8
      },
      "item-6665": {
        "value": 6,
        "weight": 2
      },
      "item-6666": {
        "value": 6,
        "weight": 2
      },
      "item-6667": {
        "value": 5,
        "weight": 5
      },
      "item-6668": {
        "value": 1,
        "weight": 6
      },
      "item-6669": {
        "value": 2,
        "weight": 4
      },
      "item-6670": {
        "value": 2,
        "weight": 6
      },
      "item-6671": {
        "value": 4,
        "weight": 6
      },
      "item-6672": {
        "value": 6,
        "weight": 1
      },
      "item-6673": {
        "value": 8,
        "weight": 4
      },
      "item-6674": {
        "value": 1,
        "weight": 2
      },
      "item-6675": {
        "value": 5,
        "weight": 2
      },
      "item-6676": {
        "value": 1,
        "weight": 5
      },
      "item-6677": {
        "value": 4,
        "weight": 9
      },
      "item-6678": {
        "value": 3,
        "weight": 5
      },
      "item-6679": {
        "value": 3,
        "weight": 6
      },
      "item-6680": {
        "value": 7,
        "weight": 2
      },
      "item-6681": {
        "value": 8,
        "weight": 1
      },
      "item-6682": {
        "value": 2,
        "weight": 3
      },
      "item-6683": {
        "value": 4,
        "weight": 9
      },
      "item-6684": {
        "value": 1,
        "weight": 4
      },
      "item-6685": {
        "value": 1,
        "weight": 9
      },
      "item-6686": {
        "value": 5,
        "weight": 9
      },
      "item-6687": {
        "value": 6,
        "weight": 3
      },
      "item-6688": {
        "value": 5,
        "weight": 8
      },
      "item-6689": {
        "value": 4,
        "weight": 9
      },
      "item-6690": {
        "value": 5,
        "weight": 1
      },
      "item-6691": {
        "value": 2,
        "weight": 2
      },
      "item-6692": {
        "value": 8,
        "weight": 2
      },
      "item-6693": {
        "value": 4,
        "weight": 7
      },
      "item-6694": {
        "value": 2,
        "weight": 2
      },
      "item-6695": {
        "value": 7,
        "weight": 3
      },
      "item-6696": {
        "value": 8,
        "weight": 1
      },
      "item-6697": {
        "value": 6,
        "weight": 3
      },
      "item-6698": {
        "value": 5,
        "weight": 8
      },
      "item-6699": {
        "value": 8,
        "weight": 5
      },
      "item-6700": {
        "value": 9,
        "weight": 9
      },
      "item-6701": {
        "value": 8,
        "weight": 7
      },
      "item-6702": {
        "value": 1,
        "weight": 8
      },
      "item-6703": {
        "value": 1,
        "weight": 6
      },
      "item-6704": {
        "value": 5,
        "weight": 1
      },
      "item-6705": {
        "value": 4,
        "weight": 6
      },
      "item-6706": {
        "value": 3,
        "weight": 2
      },
      "item-6707": {
        "value": 2,
        "weight": 4
      },
      "item-6708": {
        "value": 6,
        "weight": 1
      },
      "item-6709": {
        "value": 4,
        "weight": 2
      },
      "item-6710": {
        "value": 2,
        "weight": 1
      },
      "item-6711": {
        "value": 9,
        "weight": 8
      },
      "item-6712": {
        "value": 8,
        "weight": 6
      },
      "item-6713": {
        "value": 1,
        "weight": 7
      },
      "item-6714": {
        "value": 7,
        "weight": 3
      },
      "item-6715": {
        "value": 8,
        "weight": 2
      },
      "item-6716": {
        "value": 2,
        "weight": 4
      },
      "item-6717": {
        "value": 7,
        "weight": 7
      },
      "item-6718": {
        "value": 7,
        "weight": 9
      },
      "item-6719": {
        "value": 4,
        "weight": 5
      },
      "item-6720": {
        "value": 9,
        "weight": 8
      },
      "item-6721": {
        "value": 2,
        "weight": 5
      },
      "item-6722": {
        "value": 9,
        "weight": 1
      },
      "item-6723": {
        "value": 8,
        "weight": 3
      },
      "item-6724": {
        "value": 7,
        "weight": 6
      },
      "item-6725": {
        "value": 4,
        "weight": 6
      },
      "item-6726": {
        "value": 8,
        "weight": 8
      },
      "item-6727": {
        "value": 6,
        "weight": 1
      },
      "item-6728": {
        "value": 9,
        "weight": 1
      },
      "item-6729": {
        "value": 5,
        "weight": 6
      },
      "item-6730": {
        "value": 6,
        "weight": 4
      },
      "item-6731": {
        "value": 7,
        "weight": 5
      },
      "item-6732": {
        "value": 4,
        "weight": 1
      },
      "item-6733": {
        "value": 8,
        "weight": 8
      },
      "item-6734": {
        "value": 6,
        "weight": 5
      },
      "item-6735": {
        "value": 8,
        "weight": 6
      },
      "item-6736": {
        "value": 4,
        "weight": 3
      },
      "item-6737": {
        "value": 7,
        "weight": 9
      },
      "item-6738": {
        "value": 5,
        "weight": 3
      },
      "item-6739": {
        "value": 2,
        "weight": 5
      },
      "item-6740": {
        "value": 3,
        "weight": 8
      },
      "item-6741": {
        "value": 1,
        "weight": 3
      },
      "item-6742": {
        "value": 3,
        "weight": 9
      },
      "item-6743": {
        "value": 6,
        "weight": 4
      },
      "item-6744": {
        "value": 8,
        "weight": 6
      },
      "item-6745": {
        "value": 3,
        "weight": 3
      },
      "item-6746": {
        "value": 6,
        "weight": 7
      },
      "item-6747": {
        "value": 6,
        "weight": 5
      },
      "item-6748": {
        "value": 7,
        "weight": 6
      },
      "item-6749": {
        "value": 4,
        "weight": 5
      },
      "item-6750": {
        "value": 2,
        "weight": 3
      },
      "item-6751": {
        "value": 1,
        "weight": 5
      },
      "item-6752": {
        "value": 9,
        "weight": 6
      },
      "item-6753": {
        "value": 2,
        "weight": 3
      },
      "item-6754": {
        "value": 1,
        "weight": 5
      },
      "item-6755": {
        "value": 2,
        "weight": 4
      },
      "item-6756": {
        "value": 5,
        "weight": 8
      },
      "item-6757": {
        "value": 4,
        "weight": 5
      },
      "item-6758": {
        "value": 8,
        "weight": 5
      },
      "item-6759": {
        "value": 5,
        "weight": 8
      },
      "item-6760": {
        "value": 6,
        "weight": 3
      },
      "item-6761": {
        "value": 9,
        "weight": 2
      },
      "item-6762": {
        "value": 6,
        "weight": 9
      },
      "item-6763": {
        "value": 6,
        "weight": 9
      },
      "item-6764": {
        "value": 7,
        "weight": 5
      },
      "item-6765": {
        "value": 6,
        "weight": 2
      },
      "item-6766": {
        "value": 1,
        "weight": 4
      },
      "item-6767": {
        "value": 3,
        "weight": 7
      },
      "item-6768": {
        "value": 7,
        "weight": 4
      },
      "item-6769": {
        "value": 1,
        "weight": 1
      },
      "item-6770": {
        "value": 6,
        "weight": 6
      },
      "item-6771": {
        "value": 6,
        "weight": 7
      },
      "item-6772": {
        "value": 1,
        "weight": 7
      },
      "item-6773": {
        "value": 4,
        "weight": 4
      },
      "item-6774": {
        "value": 8,
        "weight": 2
      },
      "item-6775": {
        "value": 3,
        "weight": 8
      },
      "item-6776": {
        "value": 1,
        "weight": 6
      },
      "item-6777": {
        "value": 6,
        "weight": 9
      },
      "item-6778": {
        "value": 2,
        "weight": 4
      },
      "item-6779": {
        "value": 8,
        "weight": 9
      },
      "item-6780": {
        "value": 5,
        "weight": 6
      },
      "item-6781": {
        "value": 8,
        "weight": 1
      },
      "item-6782": {
        "value": 3,
        "weight": 7
      },
      "item-6783": {
        "value": 5,
        "weight": 1
      },
      "item-6784": {
        "value": 8,
        "weight": 4
      },
      "item-6785": {
        "value": 8,
        "weight": 8
      },
      "item-6786": {
        "value": 6,
        "weight": 2
      },
      "item-6787": {
        "value": 1,
        "weight": 9
      },
      "item-6788": {
        "value": 2,
        "weight": 8
      },
      "item-6789": {
        "value": 7,
        "weight": 4
      },
      "item-6790": {
        "value": 2,
        "weight": 1
      },
      "item-6791": {
        "value": 2,
        "weight": 7
      },
      "item-6792": {
        "value": 6,
        "weight": 9
      },
      "item-6793": {
        "value": 9,
        "weight": 2
      },
      "item-6794": {
        "value": 3,
        "weight": 6
      },
      "item-6795": {
        "value": 6,
        "weight": 8
      },
      "item-6796": {
        "value": 9,
        "weight": 8
      },
      "item-6797": {
        "value": 2,
        "weight": 5
      },
      "item-6798": {
        "value": 2,
        "weight": 4
      },
      "item-6799": {
        "value": 7,
        "weight": 1
      },
      "item-6800": {
        "value": 1,
        "weight": 6
      },
      "item-6801": {
        "value": 9,
        "weight": 5
      },
      "item-6802": {
        "value": 3,
        "weight": 1
      },
      "item-6803": {
        "value": 8,
        "weight": 2
      },
      "item-6804": {
        "value": 7,
        "weight": 5
      },
      "item-6805": {
        "value": 6,
        "weight": 2
      },
      "item-6806": {
        "value": 3,
        "weight": 7
      },
      "item-6807": {
        "value": 8,
        "weight": 9
      },
      "item-6808": {
        "value": 3,
        "weight": 3
      },
      "item-6809": {
        "value": 1,
        "weight": 7
      },
      "item-6810": {
        "value": 4,
        "weight": 8
      },
      "item-6811": {
        "value": 8,
        "weight": 3
      },
      "item-6812": {
        "value": 7,
        "weight": 9
      },
      "item-6813": {
        "value": 8,
        "weight": 1
      },
      "item-6814": {
        "value": 6,
        "weight": 2
      },
      "item-6815": {
        "value": 3,
        "weight": 9
      },
      "item-6816": {
        "value": 1,
        "weight": 1
      },
      "item-6817": {
        "value": 7,
        "weight": 9
      },
      "item-6818": {
        "value": 1,
        "weight": 4
      },
      "item-6819": {
        "value": 4,
        "weight": 9
      },
      "item-6820": {
        "value": 5,
        "weight": 6
      },
      "item-6821": {
        "value": 3,
        "weight": 5
      },
      "item-6822": {
        "value": 8,
        "weight": 9
      },
      "item-6823": {
        "value": 8,
        "weight": 3
      },
      "item-6824": {
        "value": 1,
        "weight": 9
      },
      "item-6825": {
        "value": 8,
        "weight": 5
      },
      "item-6826": {
        "value": 7,
        "weight": 5
      },
      "item-6827": {
        "value": 6,
        "weight": 6
      },
      "item-6828": {
        "value": 4,
        "weight": 9
      },
      "item-6829": {
        "value": 1,
        "weight": 1
      },
      "item-6830": {
        "value": 5,
        "weight": 6
      },
      "item-6831": {
        "value": 3,
        "weight": 8
      },
      "item-6832": {
        "value": 6,
        "weight": 5
      },
      "item-6833": {
        "value": 5,
        "weight": 8
      },
      "item-6834": {
        "value": 9,
        "weight": 4
      },
      "item-6835": {
        "value": 1,
        "weight": 4
      },
      "item-6836": {
        "value": 6,
        "weight": 9
      },
      "item-6837": {
        "value": 2,
        "weight": 9
      },
      "item-6838": {
        "value": 3,
        "weight": 2
      },
      "item-6839": {
        "value": 8,
        "weight": 9
      },
      "item-6840": {
        "value": 7,
        "weight": 4
      },
      "item-6841": {
        "value": 6,
        "weight": 7
      },
      "item-6842": {
        "value": 1,
        "weight": 6
      },
      "item-6843": {
        "value": 5,
        "weight": 7
      },
      "item-6844": {
        "value": 9,
        "weight": 8
      },
      "item-6845": {
        "value": 5,
        "weight": 3
      },
      "item-6846": {
        "value": 9,
        "weight": 2
      },
      "item-6847": {
        "value": 8,
        "weight": 1
      },
      "item-6848": {
        "value": 7,
        "weight": 6
      },
      "item-6849": {
        "value": 2,
        "weight": 9
      },
      "item-6850": {
        "value": 2,
        "weight": 5
      },
      "item-6851": {
        "value": 4,
        "weight": 1
      },
      "item-6852": {
        "value": 9,
        "weight": 5
      },
      "item-6853": {
        "value": 7,
        "weight": 2
      },
      "item-6854": {
        "value": 7,
        "weight": 8
      },
      "item-6855": {
        "value": 4,
        "weight": 6
      },
      "item-6856": {
        "value": 7,
        "weight": 4
      },
      "item-6857": {
        "value": 8,
        "weight": 6
      },
      "item-6858": {
        "value": 8,
        "weight": 5
      },
      "item-6859": {
        "value": 2,
        "weight": 2
      },
      "item-6860": {
        "value": 9,
        "weight": 3
      },
      "item-6861": {
        "value": 3,
        "weight": 8
      },
      "item-6862": {
        "value": 3,
        "weight": 9
      },
      "item-6863": {
        "value": 5,
        "weight": 4
      },
      "item-6864": {
        "value": 3,
        "weight": 1
      },
      "item-6865": {
        "value": 9,
        "weight": 8
      },
      "item-6866": {
        "value": 3,
        "weight": 2
      },
      "item-6867": {
        "value": 4,
        "weight": 4
      },
      "item-6868": {
        "value": 1,
        "weight": 1
      },
      "item-6869": {
        "value": 9,
        "weight": 8
      },
      "item-6870": {
        "value": 8,
        "weight": 9
      },
      "item-6871": {
        "value": 5,
        "weight": 7
      },
      "item-6872": {
        "value": 4,
        "weight": 1
      },
      "item-6873": {
        "value": 6,
        "weight": 6
      },
      "item-6874": {
        "value": 1,
        "weight": 7
      },
      "item-6875": {
        "value": 5,
        "weight": 7
      },
      "item-6876": {
        "value": 9,
        "weight": 8
      },
      "item-6877": {
        "value": 2,
        "weight": 8
      },
      "item-6878": {
        "value": 6,
        "weight": 5
      },
      "item-6879": {
        "value": 8,
        "weight": 9
      },
      "item-6880": {
        "value": 8,
        "weight": 9
      },
      "item-6881": {
        "value": 9,
        "weight": 8
      },
      "item-6882": {
        "value": 4,
        "weight": 3
      },
      "item-6883": {
        "value": 8,
        "weight": 1
      },
      "item-6884": {
        "value": 5,
        "weight": 6
      },
      "item-6885": {
        "value": 1,
        "weight": 9
      },
      "item-6886": {
        "value": 5,
        "weight": 2
      },
      "item-6887": {
        "value": 8,
        "weight": 7
      },
      "item-6888": {
        "value": 7,
        "weight": 7
      },
      "item-6889": {
        "value": 3,
        "weight": 5
      },
      "item-6890": {
        "value": 4,
        "weight": 4
      },
      "item-6891": {
        "value": 7,
        "weight": 3
      },
      "item-6892": {
        "value": 3,
        "weight": 9
      },
      "item-6893": {
        "value": 3,
        "weight": 4
      },
      "item-6894": {
        "value": 7,
        "weight": 9
      },
      "item-6895": {
        "value": 3,
        "weight": 6
      },
      "item-6896": {
        "value": 6,
        "weight": 9
      },
      "item-6897": {
        "value": 4,
        "weight": 8
      },
      "item-6898": {
        "value": 4,
        "weight": 6
      },
      "item-6899": {
        "value": 5,
        "weight": 3
      },
      "item-6900": {
        "value": 2,
        "weight": 1
      },
      "item-6901": {
        "value": 1,
        "weight": 4
      },
      "item-6902": {
        "value": 3,
        "weight": 1
      },
      "item-6903": {
        "value": 4,
        "weight": 3
      },
      "item-6904": {
        "value": 8,
        "weight": 2
      },
      "item-6905": {
        "value": 4,
        "weight": 1
      },
      "item-6906": {
        "value": 1,
        "weight": 3
      },
      "item-6907": {
        "value": 7,
        "weight": 5
      },
      "item-6908": {
        "value": 8,
        "weight": 4
      },
      "item-6909": {
        "value": 3,
        "weight": 9
      },
      "item-6910": {
        "value": 4,
        "weight": 8
      },
      "item-6911": {
        "value": 7,
        "weight": 4
      },
      "item-6912": {
        "value": 6,
        "weight": 9
      },
      "item-6913": {
        "value": 1,
        "weight": 7
      },
      "item-6914": {
        "value": 6,
        "weight": 6
      },
      "item-6915": {
        "value": 1,
        "weight": 2
      },
      "item-6916": {
        "value": 2,
        "weight": 1
      },
      "item-6917": {
        "value": 3,
        "weight": 9
      },
      "item-6918": {
        "value": 9,
        "weight": 4
      },
      "item-6919": {
        "value": 5,
        "weight": 5
      },
      "item-6920": {
        "value": 2,
        "weight": 4
      },
      "item-6921": {
        "value": 2,
        "weight": 1
      },
      "item-6922": {
        "value": 2,
        "weight": 4
      },
      "item-6923": {
        "value": 2,
        "weight": 9
      },
      "item-6924": {
        "value": 7,
        "weight": 2
      },
      "item-6925": {
        "value": 1,
        "weight": 2
      },
      "item-6926": {
        "value": 5,
        "weight": 5
      },
      "item-6927": {
        "value": 3,
        "weight": 9
      },
      "item-6928": {
        "value": 3,
        "weight": 5
      },
      "item-6929": {
        "value": 5,
        "weight": 9
      },
      "item-6930": {
        "value": 7,
        "weight": 4
      },
      "item-6931": {
        "value": 2,
        "weight": 9
      },
      "item-6932": {
        "value": 6,
        "weight": 4
      },
      "item-6933": {
        "value": 5,
        "weight": 1
      },
      "item-6934": {
        "value": 2,
        "weight": 4
      },
      "item-6935": {
        "value": 6,
        "weight": 3
      },
      "item-6936": {
        "value": 3,
        "weight": 1
      },
      "item-6937": {
        "value": 8,
        "weight": 2
      },
      "item-6938": {
        "value": 7,
        "weight": 1
      },
      "item-6939": {
        "value": 7,
        "weight": 6
      },
      "item-6940": {
        "value": 9,
        "weight": 8
      },
      "item-6941": {
        "value": 2,
        "weight": 3
      },
      "item-6942": {
        "value": 4,
        "weight": 9
      },
      "item-6943": {
        "value": 9,
        "weight": 6
      },
      "item-6944": {
        "value": 7,
        "weight": 5
      },
      "item-6945": {
        "value": 5,
        "weight": 9
      },
      "item-6946": {
        "value": 4,
        "weight": 7
      },
      "item-6947": {
        "value": 8,
        "weight": 2
      },
      "item-6948": {
        "value": 3,
        "weight": 2
      },
      "item-6949": {
        "value": 9,
        "weight": 6
      },
      "item-6950": {
        "value": 5,
        "weight": 7
      },
      "item-6951": {
        "value": 5,
        "weight": 1
      },
      "item-6952": {
        "value": 3,
        "weight": 6
      },
      "item-6953": {
        "value": 8,
        "weight": 3
      },
      "item-6954": {
        "value": 1,
        "weight": 8
      },
      "item-6955": {
        "value": 1,
        "weight": 4
      },
      "item-6956": {
        "value": 8,
        "weight": 9
      },
      "item-6957": {
        "value": 8,
        "weight": 9
      },
      "item-6958": {
        "value": 7,
        "weight": 7
      },
      "item-6959": {
        "value": 9,
        "weight": 7
      },
      "item-6960": {
        "value": 3,
        "weight": 9
      },
      "item-6961": {
        "value": 8,
        "weight": 4
      },
      "item-6962": {
        "value": 7,
        "weight": 3
      },
      "item-6963": {
        "value": 2,
        "weight": 9
      },
      "item-6964": {
        "value": 3,
        "weight": 3
      },
      "item-6965": {
        "value": 5,
        "weight": 7
      },
      "item-6966": {
        "value": 8,
        "weight": 7
      },
      "item-6967": {
        "value": 2,
        "weight": 2
      },
      "item-6968": {
        "value": 4,
        "weight": 4
      },
      "item-6969": {
        "value": 3,
        "weight": 2
      },
      "item-6970": {
        "value": 6,
        "weight": 9
      },
      "item-6971": {
        "value": 3,
        "weight": 5
      },
      "item-6972": {
        "value": 1,
        "weight": 2
      },
      "item-6973": {
        "value": 8,
        "weight": 5
      },
      "item-6974": {
        "value": 6,
        "weight": 8
      },
      "item-6975": {
        "value": 1,
        "weight": 8
      },
      "item-6976": {
        "value": 9,
        "weight": 9
      },
      "item-6977": {
        "value": 6,
        "weight": 4
      },
      "item-6978": {
        "value": 1,
        "weight": 2
      },
      "item-6979": {
        "value": 8,
        "weight": 8
      },
      "item-6980": {
        "value": 4,
        "weight": 1
      },
      "item-6981": {
        "value": 8,
        "weight": 6
      },
      "item-6982": {
        "value": 2,
        "weight": 8
      },
      "item-6983": {
        "value": 7,
        "weight": 7
      },
      "item-6984": {
        "value": 7,
        "weight": 8
      },
      "item-6985": {
        "value": 5,
        "weight": 2
      },
      "item-6986": {
        "value": 2,
        "weight": 9
      },
      "item-6987": {
        "value": 2,
        "weight": 2
      },
      "item-6988": {
        "value": 2,
        "weight": 9
      },
      "item-6989": {
        "value": 1,
        "weight": 7
      },
      "item-6990": {
        "value": 3,
        "weight": 4
      },
      "item-6991": {
        "value": 2,
        "weight": 2
      },
      "item-6992": {
        "value": 1,
        "weight": 3
      },
      "item-6993": {
        "value": 6,
        "weight": 7
      },
      "item-6994": {
        "value": 2,
        "weight": 2
      },
      "item-6995": {
        "value": 7,
        "weight": 4
      },
      "item-6996": {
        "value": 8,
        "weight": 3
      },
      "item-6997": {
        "value": 8,
        "weight": 6
      },
      "item-6998": {
        "value": 8,
        "weight": 5
      },
      "item-6999": {
        "value": 1,
        "weight": 2
      },
      "item-7000": {
        "value": 1,
        "weight": 7
      },
      "item-7001": {
        "value": 5,
        "weight": 4
      },
      "item-7002": {
        "value": 4,
        "weight": 6
      },
      "item-7003": {
        "value": 1,
        "weight": 3
      },
      "item-7004": {
        "value": 3,
        "weight": 5
      },
      "item-7005": {
        "value": 6,
        "weight": 6
      },
      "item-7006": {
        "value": 8,
        "weight": 7
      },
      "item-7007": {
        "value": 4,
        "weight": 9
      },
      "item-7008": {
        "value": 9,
        "weight": 5
      },
      "item-7009": {
        "value": 2,
        "weight": 9
      },
      "item-7010": {
        "value": 9,
        "weight": 2
      },
      "item-7011": {
        "value": 4,
        "weight": 4
      },
      "item-7012": {
        "value": 6,
        "weight": 4
      },
      "item-7013": {
        "value": 3,
        "weight": 7
      },
      "item-7014": {
        "value": 5,
        "weight": 8
      },
      "item-7015": {
        "value": 6,
        "weight": 3
      },
      "item-7016": {
        "value": 7,
        "weight": 7
      },
      "item-7017": {
        "value": 7,
        "weight": 9
      },
      "item-7018": {
        "value": 9,
        "weight": 9
      },
      "item-7019": {
        "value": 8,
        "weight": 6
      },
      "item-7020": {
        "value": 8,
        "weight": 9
      },
      "item-7021": {
        "value": 2,
        "weight": 2
      },
      "item-7022": {
        "value": 2,
        "weight": 2
      },
      "item-7023": {
        "value": 4,
        "weight": 7
      },
      "item-7024": {
        "value": 5,
        "weight": 2
      },
      "item-7025": {
        "value": 9,
        "weight": 1
      },
      "item-7026": {
        "value": 9,
        "weight": 1
      },
      "item-7027": {
        "value": 2,
        "weight": 5
      },
      "item-7028": {
        "value": 9,
        "weight": 3
      },
      "item-7029": {
        "value": 6,
        "weight": 1
      },
      "item-7030": {
        "value": 1,
        "weight": 3
      },
      "item-7031": {
        "value": 1,
        "weight": 2
      },
      "item-7032": {
        "value": 3,
        "weight": 6
      },
      "item-7033": {
        "value": 4,
        "weight": 6
      },
      "item-7034": {
        "value": 4,
        "weight": 4
      },
      "item-7035": {
        "value": 4,
        "weight": 3
      },
      "item-7036": {
        "value": 1,
        "weight": 4
      },
      "item-7037": {
        "value": 7,
        "weight": 2
      },
      "item-7038": {
        "value": 2,
        "weight": 4
      },
      "item-7039": {
        "value": 6,
        "weight": 1
      },
      "item-7040": {
        "value": 5,
        "weight": 9
      },
      "item-7041": {
        "value": 2,
        "weight": 4
      },
      "item-7042": {
        "value": 1,
        "weight": 9
      },
      "item-7043": {
        "value": 1,
        "weight": 8
      },
      "item-7044": {
        "value": 3,
        "weight": 3
      },
      "item-7045": {
        "value": 9,
        "weight": 7
      },
      "item-7046": {
        "value": 1,
        "weight": 4
      },
      "item-7047": {
        "value": 3,
        "weight": 5
      },
      "item-7048": {
        "value": 7,
        "weight": 1
      },
      "item-7049": {
        "value": 7,
        "weight": 6
      },
      "item-7050": {
        "value": 7,
        "weight": 9
      },
      "item-7051": {
        "value": 7,
        "weight": 6
      },
      "item-7052": {
        "value": 7,
        "weight": 9
      },
      "item-7053": {
        "value": 1,
        "weight": 4
      },
      "item-7054": {
        "value": 2,
        "weight": 3
      },
      "item-7055": {
        "value": 1,
        "weight": 4
      },
      "item-7056": {
        "value": 6,
        "weight": 5
      },
      "item-7057": {
        "value": 2,
        "weight": 8
      },
      "item-7058": {
        "value": 6,
        "weight": 3
      },
      "item-7059": {
        "value": 3,
        "weight": 2
      },
      "item-7060": {
        "value": 4,
        "weight": 9
      },
      "item-7061": {
        "value": 7,
        "weight": 1
      },
      "item-7062": {
        "value": 2,
        "weight": 7
      },
      "item-7063": {
        "value": 9,
        "weight": 7
      },
      "item-7064": {
        "value": 3,
        "weight": 3
      },
      "item-7065": {
        "value": 9,
        "weight": 8
      },
      "item-7066": {
        "value": 4,
        "weight": 7
      },
      "item-7067": {
        "value": 1,
        "weight": 1
      },
      "item-7068": {
        "value": 7,
        "weight": 7
      },
      "item-7069": {
        "value": 4,
        "weight": 9
      },
      "item-7070": {
        "value": 8,
        "weight": 4
      },
      "item-7071": {
        "value": 7,
        "weight": 4
      },
      "item-7072": {
        "value": 1,
        "weight": 1
      },
      "item-7073": {
        "value": 2,
        "weight": 4
      },
      "item-7074": {
        "value": 7,
        "weight": 3
      },
      "item-7075": {
        "value": 2,
        "weight": 7
      },
      "item-7076": {
        "value": 6,
        "weight": 4
      },
      "item-7077": {
        "value": 3,
        "weight": 2
      },
      "item-7078": {
        "value": 3,
        "weight": 5
      },
      "item-7079": {
        "value": 9,
        "weight": 3
      },
      "item-7080": {
        "value": 5,
        "weight": 9
      },
      "item-7081": {
        "value": 2,
        "weight": 4
      },
      "item-7082": {
        "value": 2,
        "weight": 4
      },
      "item-7083": {
        "value": 5,
        "weight": 7
      },
      "item-7084": {
        "value": 3,
        "weight": 2
      },
      "item-7085": {
        "value": 4,
        "weight": 7
      },
      "item-7086": {
        "value": 4,
        "weight": 8
      },
      "item-7087": {
        "value": 7,
        "weight": 4
      },
      "item-7088": {
        "value": 9,
        "weight": 4
      },
      "item-7089": {
        "value": 4,
        "weight": 6
      },
      "item-7090": {
        "value": 6,
        "weight": 2
      },
      "item-7091": {
        "value": 6,
        "weight": 8
      },
      "item-7092": {
        "value": 6,
        "weight": 3
      },
      "item-7093": {
        "value": 9,
        "weight": 3
      },
      "item-7094": {
        "value": 8,
        "weight": 3
      },
      "item-7095": {
        "value": 9,
        "weight": 1
      },
      "item-7096": {
        "value": 4,
        "weight": 4
      },
      "item-7097": {
        "value": 9,
        "weight": 7
      },
      "item-7098": {
        "value": 5,
        "weight": 6
      },
      "item-7099": {
        "value": 5,
        "weight": 5
      },
      "item-7100": {
        "value": 3,
        "weight": 4
      },
      "item-7101": {
        "value": 4,
        "weight": 4
      },
      "item-7102": {
        "value": 9,
        "weight": 9
      },
      "item-7103": {
        "value": 3,
        "weight": 5
      },
      "item-7104": {
        "value": 8,
        "weight": 3
      },
      "item-7105": {
        "value": 3,
        "weight": 9
      },
      "item-7106": {
        "value": 8,
        "weight": 4
      },
      "item-7107": {
        "value": 2,
        "weight": 4
      },
      "item-7108": {
        "value": 9,
        "weight": 6
      },
      "item-7109": {
        "value": 3,
        "weight": 4
      },
      "item-7110": {
        "value": 6,
        "weight": 9
      },
      "item-7111": {
        "value": 1,
        "weight": 8
      },
      "item-7112": {
        "value": 3,
        "weight": 2
      },
      "item-7113": {
        "value": 5,
        "weight": 8
      },
      "item-7114": {
        "value": 6,
        "weight": 1
      },
      "item-7115": {
        "value": 3,
        "weight": 1
      },
      "item-7116": {
        "value": 9,
        "weight": 4
      },
      "item-7117": {
        "value": 5,
        "weight": 1
      },
      "item-7118": {
        "value": 2,
        "weight": 6
      },
      "item-7119": {
        "value": 9,
        "weight": 2
      },
      "item-7120": {
        "value": 2,
        "weight": 9
      },
      "item-7121": {
        "value": 5,
        "weight": 3
      },
      "item-7122": {
        "value": 2,
        "weight": 1
      },
      "item-7123": {
        "value": 5,
        "weight": 6
      },
      "item-7124": {
        "value": 9,
        "weight": 3
      },
      "item-7125": {
        "value": 8,
        "weight": 9
      },
      "item-7126": {
        "value": 6,
        "weight": 9
      },
      "item-7127": {
        "value": 3,
        "weight": 3
      },
      "item-7128": {
        "value": 4,
        "weight": 1
      },
      "item-7129": {
        "value": 1,
        "weight": 2
      },
      "item-7130": {
        "value": 3,
        "weight": 6
      },
      "item-7131": {
        "value": 2,
        "weight": 2
      },
      "item-7132": {
        "value": 4,
        "weight": 9
      },
      "item-7133": {
        "value": 9,
        "weight": 1
      },
      "item-7134": {
        "value": 4,
        "weight": 7
      },
      "item-7135": {
        "value": 8,
        "weight": 5
      },
      "item-7136": {
        "value": 5,
        "weight": 4
      },
      "item-7137": {
        "value": 9,
        "weight": 5
      },
      "item-7138": {
        "value": 4,
        "weight": 6
      },
      "item-7139": {
        "value": 9,
        "weight": 9
      },
      "item-7140": {
        "value": 2,
        "weight": 4
      },
      "item-7141": {
        "value": 1,
        "weight": 5
      },
      "item-7142": {
        "value": 5,
        "weight": 6
      },
      "item-7143": {
        "value": 7,
        "weight": 4
      },
      "item-7144": {
        "value": 4,
        "weight": 2
      },
      "item-7145": {
        "value": 8,
        "weight": 3
      },
      "item-7146": {
        "value": 4,
        "weight": 6
      },
      "item-7147": {
        "value": 2,
        "weight": 9
      },
      "item-7148": {
        "value": 3,
        "weight": 3
      },
      "item-7149": {
        "value": 9,
        "weight": 1
      },
      "item-7150": {
        "value": 1,
        "weight": 5
      },
      "item-7151": {
        "value": 4,
        "weight": 9
      },
      "item-7152": {
        "value": 5,
        "weight": 4
      },
      "item-7153": {
        "value": 4,
        "weight": 3
      },
      "item-7154": {
        "value": 5,
        "weight": 5
      },
      "item-7155": {
        "value": 1,
        "weight": 1
      },
      "item-7156": {
        "value": 5,
        "weight": 7
      },
      "item-7157": {
        "value": 1,
        "weight": 8
      },
      "item-7158": {
        "value": 3,
        "weight": 7
      },
      "item-7159": {
        "value": 8,
        "weight": 1
      },
      "item-7160": {
        "value": 5,
        "weight": 2
      },
      "item-7161": {
        "value": 8,
        "weight": 9
      },
      "item-7162": {
        "value": 6,
        "weight": 9
      },
      "item-7163": {
        "value": 6,
        "weight": 2
      },
      "item-7164": {
        "value": 7,
        "weight": 2
      },
      "item-7165": {
        "value": 9,
        "weight": 7
      },
      "item-7166": {
        "value": 4,
        "weight": 4
      },
      "item-7167": {
        "value": 2,
        "weight": 8
      },
      "item-7168": {
        "value": 7,
        "weight": 7
      },
      "item-7169": {
        "value": 2,
        "weight": 4
      },
      "item-7170": {
        "value": 2,
        "weight": 4
      },
      "item-7171": {
        "value": 2,
        "weight": 8
      },
      "item-7172": {
        "value": 9,
        "weight": 7
      },
      "item-7173": {
        "value": 7,
        "weight": 5
      },
      "item-7174": {
        "value": 7,
        "weight": 6
      },
      "item-7175": {
        "value": 8,
        "weight": 4
      },
      "item-7176": {
        "value": 4,
        "weight": 6
      },
      "item-7177": {
        "value": 2,
        "weight": 4
      },
      "item-7178": {
        "value": 9,
        "weight": 1
      },
      "item-7179": {
        "value": 7,
        "weight": 4
      },
      "item-7180": {
        "value": 5,
        "weight": 9
      },
      "item-7181": {
        "value": 3,
        "weight": 1
      },
      "item-7182": {
        "value": 1,
        "weight": 6
      },
      "item-7183": {
        "value": 6,
        "weight": 4
      },
      "item-7184": {
        "value": 6,
        "weight": 1
      },
      "item-7185": {
        "value": 2,
        "weight": 9
      },
      "item-7186": {
        "value": 5,
        "weight": 5
      },
      "item-7187": {
        "value": 7,
        "weight": 1
      },
      "item-7188": {
        "value": 1,
        "weight": 2
      },
      "item-7189": {
        "value": 5,
        "weight": 6
      },
      "item-7190": {
        "value": 3,
        "weight": 1
      },
      "item-7191": {
        "value": 9,
        "weight": 6
      },
      "item-7192": {
        "value": 4,
        "weight": 4
      },
      "item-7193": {
        "value": 3,
        "weight": 4
      },
      "item-7194": {
        "value": 4,
        "weight": 4
      },
      "item-7195": {
        "value": 4,
        "weight": 2
      },
      "item-7196": {
        "value": 2,
        "weight": 6
      },
      "item-7197": {
        "value": 9,
        "weight": 5
      },
      "item-7198": {
        "value": 4,
        "weight": 3
      },
      "item-7199": {
        "value": 9,
        "weight": 9
      },
      "item-7200": {
        "value": 8,
        "weight": 9
      },
      "item-7201": {
        "value": 5,
        "weight": 4
      },
      "item-7202": {
        "value": 4,
        "weight": 9
      },
      "item-7203": {
        "value": 7,
        "weight": 6
      },
      "item-7204": {
        "value": 9,
        "weight": 7
      },
      "item-7205": {
        "value": 8,
        "weight": 4
      },
      "item-7206": {
        "value": 8,
        "weight": 1
      },
      "item-7207": {
        "value": 2,
        "weight": 2
      },
      "item-7208": {
        "value": 5,
        "weight": 4
      },
      "item-7209": {
        "value": 7,
        "weight": 6
      },
      "item-7210": {
        "value": 7,
        "weight": 8
      },
      "item-7211": {
        "value": 3,
        "weight": 7
      },
      "item-7212": {
        "value": 3,
        "weight": 6
      },
      "item-7213": {
        "value": 5,
        "weight": 8
      },
      "item-7214": {
        "value": 6,
        "weight": 5
      },
      "item-7215": {
        "value": 3,
        "weight": 9
      },
      "item-7216": {
        "value": 3,
        "weight": 8
      },
      "item-7217": {
        "value": 3,
        "weight": 4
      },
      "item-7218": {
        "value": 6,
        "weight": 7
      },
      "item-7219": {
        "value": 8,
        "weight": 6
      },
      "item-7220": {
        "value": 1,
        "weight": 9
      },
      "item-7221": {
        "value": 8,
        "weight": 6
      },
      "item-7222": {
        "value": 8,
        "weight": 7
      },
      "item-7223": {
        "value": 5,
        "weight": 9
      },
      "item-7224": {
        "value": 6,
        "weight": 9
      },
      "item-7225": {
        "value": 9,
        "weight": 6
      },
      "item-7226": {
        "value": 1,
        "weight": 4
      },
      "item-7227": {
        "value": 7,
        "weight": 2
      },
      "item-7228": {
        "value": 2,
        "weight": 2
      },
      "item-7229": {
        "value": 7,
        "weight": 2
      },
      "item-7230": {
        "value": 7,
        "weight": 6
      },
      "item-7231": {
        "value": 6,
        "weight": 9
      },
      "item-7232": {
        "value": 2,
        "weight": 7
      },
      "item-7233": {
        "value": 1,
        "weight": 7
      },
      "item-7234": {
        "value": 9,
        "weight": 9
      },
      "item-7235": {
        "value": 2,
        "weight": 7
      },
      "item-7236": {
        "value": 6,
        "weight": 9
      },
      "item-7237": {
        "value": 5,
        "weight": 9
      },
      "item-7238": {
        "value": 2,
        "weight": 3
      },
      "item-7239": {
        "value": 2,
        "weight": 8
      },
      "item-7240": {
        "value": 3,
        "weight": 3
      },
      "item-7241": {
        "value": 7,
        "weight": 2
      },
      "item-7242": {
        "value": 5,
        "weight": 4
      },
      "item-7243": {
        "value": 1,
        "weight": 5
      },
      "item-7244": {
        "value": 3,
        "weight": 9
      },
      "item-7245": {
        "value": 6,
        "weight": 4
      },
      "item-7246": {
        "value": 2,
        "weight": 1
      },
      "item-7247": {
        "value": 1,
        "weight": 4
      },
      "item-7248": {
        "value": 4,
        "weight": 6
      },
      "item-7249": {
        "value": 7,
        "weight": 4
      },
      "item-7250": {
        "value": 5,
        "weight": 1
      },
      "item-7251": {
        "value": 7,
        "weight": 2
      },
      "item-7252": {
        "value": 9,
        "weight": 6
      },
      "item-7253": {
        "value": 4,
        "weight": 6
      },
      "item-7254": {
        "value": 5,
        "weight": 4
      },
      "item-7255": {
        "value": 4,
        "weight": 2
      },
      "item-7256": {
        "value": 5,
        "weight": 6
      },
      "item-7257": {
        "value": 6,
        "weight": 9
      },
      "item-7258": {
        "value": 4,
        "weight": 5
      },
      "item-7259": {
        "value": 1,
        "weight": 7
      },
      "item-7260": {
        "value": 7,
        "weight": 7
      },
      "item-7261": {
        "value": 9,
        "weight": 7
      },
      "item-7262": {
        "value": 2,
        "weight": 8
      },
      "item-7263": {
        "value": 3,
        "weight": 2
      },
      "item-7264": {
        "value": 9,
        "weight": 4
      },
      "item-7265": {
        "value": 5,
        "weight": 9
      },
      "item-7266": {
        "value": 4,
        "weight": 2
      },
      "item-7267": {
        "value": 3,
        "weight": 6
      },
      "item-7268": {
        "value": 1,
        "weight": 8
      },
      "item-7269": {
        "value": 6,
        "weight": 1
      },
      "item-7270": {
        "value": 1,
        "weight": 1
      },
      "item-7271": {
        "value": 7,
        "weight": 6
      },
      "item-7272": {
        "value": 9,
        "weight": 7
      },
      "item-7273": {
        "value": 7,
        "weight": 4
      },
      "item-7274": {
        "value": 1,
        "weight": 9
      },
      "item-7275": {
        "value": 2,
        "weight": 2
      },
      "item-7276": {
        "value": 7,
        "weight": 9
      },
      "item-7277": {
        "value": 3,
        "weight": 5
      },
      "item-7278": {
        "value": 3,
        "weight": 1
      },
      "item-7279": {
        "value": 8,
        "weight": 8
      },
      "item-7280": {
        "value": 8,
        "weight": 3
      },
      "item-7281": {
        "value": 9,
        "weight": 2
      },
      "item-7282": {
        "value": 7,
        "weight": 5
      },
      "item-7283": {
        "value": 6,
        "weight": 3
      },
      "item-7284": {
        "value": 5,
        "weight": 8
      },
      "item-7285": {
        "value": 1,
        "weight": 2
      },
      "item-7286": {
        "value": 9,
        "weight": 7
      },
      "item-7287": {
        "value": 8,
        "weight": 1
      },
      "item-7288": {
        "value": 9,
        "weight": 9
      },
      "item-7289": {
        "value": 2,
        "weight": 5
      },
      "item-7290": {
        "value": 3,
        "weight": 6
      },
      "item-7291": {
        "value": 4,
        "weight": 5
      },
      "item-7292": {
        "value": 4,
        "weight": 6
      },
      "item-7293": {
        "value": 9,
        "weight": 7
      },
      "item-7294": {
        "value": 6,
        "weight": 7
      },
      "item-7295": {
        "value": 9,
        "weight": 2
      },
      "item-7296": {
        "value": 6,
        "weight": 3
      },
      "item-7297": {
        "value": 9,
        "weight": 3
      },
      "item-7298": {
        "value": 3,
        "weight": 2
      },
      "item-7299": {
        "value": 1,
        "weight": 5
      },
      "item-7300": {
        "value": 5,
        "weight": 5
      },
      "item-7301": {
        "value": 6,
        "weight": 6
      },
      "item-7302": {
        "value": 2,
        "weight": 8
      },
      "item-7303": {
        "value": 5,
        "weight": 5
      },
      "item-7304": {
        "value": 9,
        "weight": 1
      },
      "item-7305": {
        "value": 9,
        "weight": 2
      },
      "item-7306": {
        "value": 4,
        "weight": 6
      },
      "item-7307": {
        "value": 8,
        "weight": 8
      },
      "item-7308": {
        "value": 9,
        "weight": 3
      },
      "item-7309": {
        "value": 9,
        "weight": 7
      },
      "item-7310": {
        "value": 5,
        "weight": 4
      },
      "item-7311": {
        "value": 6,
        "weight": 2
      },
      "item-7312": {
        "value": 5,
        "weight": 8
      },
      "item-7313": {
        "value": 3,
        "weight": 8
      },
      "item-7314": {
        "value": 7,
        "weight": 3
      },
      "item-7315": {
        "value": 5,
        "weight": 1
      },
      "item-7316": {
        "value": 7,
        "weight": 2
      },
      "item-7317": {
        "value": 9,
        "weight": 8
      },
      "item-7318": {
        "value": 1,
        "weight": 1
      },
      "item-7319": {
        "value": 1,
        "weight": 5
      },
      "item-7320": {
        "value": 9,
        "weight": 3
      },
      "item-7321": {
        "value": 8,
        "weight": 9
      },
      "item-7322": {
        "value": 9,
        "weight": 7
      },
      "item-7323": {
        "value": 7,
        "weight": 8
      },
      "item-7324": {
        "value": 5,
        "weight": 9
      },
      "item-7325": {
        "value": 4,
        "weight": 1
      },
      "item-7326": {
        "value": 8,
        "weight": 3
      },
      "item-7327": {
        "value": 2,
        "weight": 5
      },
      "item-7328": {
        "value": 5,
        "weight": 4
      },
      "item-7329": {
        "value": 9,
        "weight": 3
      },
      "item-7330": {
        "value": 7,
        "weight": 3
      },
      "item-7331": {
        "value": 3,
        "weight": 9
      },
      "item-7332": {
        "value": 6,
        "weight": 2
      },
      "item-7333": {
        "value": 7,
        "weight": 9
      },
      "item-7334": {
        "value": 4,
        "weight": 2
      },
      "item-7335": {
        "value": 8,
        "weight": 7
      },
      "item-7336": {
        "value": 7,
        "weight": 4
      },
      "item-7337": {
        "value": 6,
        "weight": 9
      },
      "item-7338": {
        "value": 8,
        "weight": 4
      },
      "item-7339": {
        "value": 3,
        "weight": 4
      },
      "item-7340": {
        "value": 4,
        "weight": 5
      },
      "item-7341": {
        "value": 7,
        "weight": 5
      },
      "item-7342": {
        "value": 2,
        "weight": 9
      },
      "item-7343": {
        "value": 1,
        "weight": 3
      },
      "item-7344": {
        "value": 6,
        "weight": 9
      },
      "item-7345": {
        "value": 1,
        "weight": 8
      },
      "item-7346": {
        "value": 1,
        "weight": 5
      },
      "item-7347": {
        "value": 1,
        "weight": 2
      },
      "item-7348": {
        "value": 1,
        "weight": 5
      },
      "item-7349": {
        "value": 5,
        "weight": 5
      },
      "item-7350": {
        "value": 9,
        "weight": 6
      },
      "item-7351": {
        "value": 1,
        "weight": 6
      },
      "item-7352": {
        "value": 6,
        "weight": 1
      },
      "item-7353": {
        "value": 9,
        "weight": 9
      },
      "item-7354": {
        "value": 5,
        "weight": 3
      },
      "item-7355": {
        "value": 6,
        "weight": 7
      },
      "item-7356": {
        "value": 9,
        "weight": 7
      },
      "item-7357": {
        "value": 6,
        "weight": 4
      },
      "item-7358": {
        "value": 3,
        "weight": 5
      },
      "item-7359": {
        "value": 3,
        "weight": 8
      },
      "item-7360": {
        "value": 8,
        "weight": 4
      },
      "item-7361": {
        "value": 6,
        "weight": 8
      },
      "item-7362": {
        "value": 1,
        "weight": 4
      },
      "item-7363": {
        "value": 3,
        "weight": 5
      },
      "item-7364": {
        "value": 2,
        "weight": 8
      },
      "item-7365": {
        "value": 5,
        "weight": 6
      },
      "item-7366": {
        "value": 7,
        "weight": 7
      },
      "item-7367": {
        "value": 1,
        "weight": 9
      },
      "item-7368": {
        "value": 8,
        "weight": 7
      },
      "item-7369": {
        "value": 7,
        "weight": 9
      },
      "item-7370": {
        "value": 2,
        "weight": 2
      },
      "item-7371": {
        "value": 5,
        "weight": 3
      },
      "item-7372": {
        "value": 9,
        "weight": 4
      },
      "item-7373": {
        "value": 6,
        "weight": 9
      },
      "item-7374": {
        "value": 3,
        "weight": 2
      },
      "item-7375": {
        "value": 8,
        "weight": 8
      },
      "item-7376": {
        "value": 6,
        "weight": 2
      },
      "item-7377": {
        "value": 2,
        "weight": 7
      },
      "item-7378": {
        "value": 4,
        "weight": 4
      },
      "item-7379": {
        "value": 7,
        "weight": 1
      },
      "item-7380": {
        "value": 8,
        "weight": 5
      },
      "item-7381": {
        "value": 4,
        "weight": 8
      },
      "item-7382": {
        "value": 9,
        "weight": 2
      },
      "item-7383": {
        "value": 9,
        "weight": 9
      },
      "item-7384": {
        "value": 3,
        "weight": 6
      },
      "item-7385": {
        "value": 4,
        "weight": 3
      },
      "item-7386": {
        "value": 4,
        "weight": 6
      },
      "item-7387": {
        "value": 3,
        "weight": 7
      },
      "item-7388": {
        "value": 3,
        "weight": 7
      },
      "item-7389": {
        "value": 3,
        "weight": 2
      },
      "item-7390": {
        "value": 1,
        "weight": 7
      },
      "item-7391": {
        "value": 5,
        "weight": 2
      },
      "item-7392": {
        "value": 7,
        "weight": 1
      },
      "item-7393": {
        "value": 1,
        "weight": 6
      },
      "item-7394": {
        "value": 3,
        "weight": 1
      },
      "item-7395": {
        "value": 1,
        "weight": 3
      },
      "item-7396": {
        "value": 5,
        "weight": 2
      },
      "item-7397": {
        "value": 8,
        "weight": 4
      },
      "item-7398": {
        "value": 9,
        "weight": 1
      },
      "item-7399": {
        "value": 1,
        "weight": 7
      },
      "item-7400": {
        "value": 5,
        "weight": 8
      },
      "item-7401": {
        "value": 3,
        "weight": 6
      },
      "item-7402": {
        "value": 3,
        "weight": 4
      },
      "item-7403": {
        "value": 4,
        "weight": 9
      },
      "item-7404": {
        "value": 7,
        "weight": 2
      },
      "item-7405": {
        "value": 3,
        "weight": 8
      },
      "item-7406": {
        "value": 5,
        "weight": 7
      },
      "item-7407": {
        "value": 9,
        "weight": 2
      },
      "item-7408": {
        "value": 3,
        "weight": 5
      },
      "item-7409": {
        "value": 6,
        "weight": 8
      },
      "item-7410": {
        "value": 1,
        "weight": 1
      },
      "item-7411": {
        "value": 4,
        "weight": 2
      },
      "item-7412": {
        "value": 5,
        "weight": 8
      },
      "item-7413": {
        "value": 7,
        "weight": 1
      },
      "item-7414": {
        "value": 1,
        "weight": 8
      },
      "item-7415": {
        "value": 4,
        "weight": 4
      },
      "item-7416": {
        "value": 6,
        "weight": 6
      },
      "item-7417": {
        "value": 3,
        "weight": 5
      },
      "item-7418": {
        "value": 3,
        "weight": 9
      },
      "item-7419": {
        "value": 9,
        "weight": 9
      },
      "item-7420": {
        "value": 3,
        "weight": 5
      },
      "item-7421": {
        "value": 7,
        "weight": 3
      },
      "item-7422": {
        "value": 2,
        "weight": 3
      },
      "item-7423": {
        "value": 7,
        "weight": 8
      },
      "item-7424": {
        "value": 1,
        "weight": 9
      },
      "item-7425": {
        "value": 9,
        "weight": 3
      },
      "item-7426": {
        "value": 9,
        "weight": 1
      },
      "item-7427": {
        "value": 7,
        "weight": 4
      },
      "item-7428": {
        "value": 2,
        "weight": 1
      },
      "item-7429": {
        "value": 1,
        "weight": 5
      },
      "item-7430": {
        "value": 8,
        "weight": 7
      },
      "item-7431": {
        "value": 1,
        "weight": 1
      },
      "item-7432": {
        "value": 7,
        "weight": 6
      },
      "item-7433": {
        "value": 7,
        "weight": 2
      },
      "item-7434": {
        "value": 6,
        "weight": 4
      },
      "item-7435": {
        "value": 8,
        "weight": 7
      },
      "item-7436": {
        "value": 9,
        "weight": 6
      },
      "item-7437": {
        "value": 7,
        "weight": 1
      },
      "item-7438": {
        "value": 5,
        "weight": 5
      },
      "item-7439": {
        "value": 2,
        "weight": 9
      },
      "item-7440": {
        "value": 5,
        "weight": 9
      },
      "item-7441": {
        "value": 9,
        "weight": 2
      },
      "item-7442": {
        "value": 5,
        "weight": 2
      },
      "item-7443": {
        "value": 4,
        "weight": 6
      },
      "item-7444": {
        "value": 9,
        "weight": 9
      },
      "item-7445": {
        "value": 8,
        "weight": 8
      },
      "item-7446": {
        "value": 4,
        "weight": 3
      },
      "item-7447": {
        "value": 7,
        "weight": 3
      },
      "item-7448": {
        "value": 3,
        "weight": 2
      },
      "item-7449": {
        "value": 4,
        "weight": 9
      },
      "item-7450": {
        "value": 6,
        "weight": 2
      },
      "item-7451": {
        "value": 7,
        "weight": 5
      },
      "item-7452": {
        "value": 6,
        "weight": 5
      },
      "item-7453": {
        "value": 9,
        "weight": 6
      },
      "item-7454": {
        "value": 8,
        "weight": 2
      },
      "item-7455": {
        "value": 8,
        "weight": 1
      },
      "item-7456": {
        "value": 7,
        "weight": 2
      },
      "item-7457": {
        "value": 6,
        "weight": 9
      },
      "item-7458": {
        "value": 8,
        "weight": 4
      },
      "item-7459": {
        "value": 7,
        "weight": 5
      },
      "item-7460": {
        "value": 9,
        "weight": 7
      },
      "item-7461": {
        "value": 3,
        "weight": 3
      },
      "item-7462": {
        "value": 7,
        "weight": 6
      },
      "item-7463": {
        "value": 6,
        "weight": 2
      },
      "item-7464": {
        "value": 6,
        "weight": 4
      },
      "item-7465": {
        "value": 5,
        "weight": 1
      },
      "item-7466": {
        "value": 8,
        "weight": 7
      },
      "item-7467": {
        "value": 4,
        "weight": 1
      },
      "item-7468": {
        "value": 6,
        "weight": 6
      },
      "item-7469": {
        "value": 2,
        "weight": 1
      },
      "item-7470": {
        "value": 2,
        "weight": 3
      },
      "item-7471": {
        "value": 6,
        "weight": 1
      },
      "item-7472": {
        "value": 6,
        "weight": 5
      },
      "item-7473": {
        "value": 4,
        "weight": 2
      },
      "item-7474": {
        "value": 7,
        "weight": 2
      },
      "item-7475": {
        "value": 7,
        "weight": 8
      },
      "item-7476": {
        "value": 3,
        "weight": 2
      },
      "item-7477": {
        "value": 6,
        "weight": 6
      },
      "item-7478": {
        "value": 3,
        "weight": 4
      },
      "item-7479": {
        "value": 1,
        "weight": 6
      },
      "item-7480": {
        "value": 7,
        "weight": 4
      },
      "item-7481": {
        "value": 5,
        "weight": 2
      },
      "item-7482": {
        "value": 4,
        "weight": 4
      },
      "item-7483": {
        "value": 6,
        "weight": 4
      },
      "item-7484": {
        "value": 4,
        "weight": 2
      },
      "item-7485": {
        "value": 5,
        "weight": 1
      },
      "item-7486": {
        "value": 1,
        "weight": 2
      },
      "item-7487": {
        "value": 3,
        "weight": 5
      },
      "item-7488": {
        "value": 4,
        "weight": 5
      },
      "item-7489": {
        "value": 8,
        "weight": 9
      },
      "item-7490": {
        "value": 2,
        "weight": 8
      },
      "item-7491": {
        "value": 9,
        "weight": 2
      },
      "item-7492": {
        "value": 7,
        "weight": 6
      },
      "item-7493": {
        "value": 5,
        "weight": 5
      },
      "item-7494": {
        "value": 3,
        "weight": 8
      },
      "item-7495": {
        "value": 1,
        "weight": 5
      },
      "item-7496": {
        "value": 7,
        "weight": 8
      },
      "item-7497": {
        "value": 6,
        "weight": 1
      },
      "item-7498": {
        "value": 8,
        "weight": 1
      },
      "item-7499": {
        "value": 2,
        "weight": 9
      },
      "item-7500": {
        "value": 1,
        "weight": 7
      },
      "item-7501": {
        "value": 7,
        "weight": 5
      },
      "item-7502": {
        "value": 8,
        "weight": 8
      },
      "item-7503": {
        "value": 8,
        "weight": 2
      },
      "item-7504": {
        "value": 2,
        "weight": 9
      },
      "item-7505": {
        "value": 8,
        "weight": 6
      },
      "item-7506": {
        "value": 7,
        "weight": 8
      },
      "item-7507": {
        "value": 9,
        "weight": 4
      },
      "item-7508": {
        "value": 8,
        "weight": 3
      },
      "item-7509": {
        "value": 1,
        "weight": 6
      },
      "item-7510": {
        "value": 3,
        "weight": 5
      },
      "item-7511": {
        "value": 2,
        "weight": 9
      },
      "item-7512": {
        "value": 9,
        "weight": 1
      },
      "item-7513": {
        "value": 9,
        "weight": 3
      },
      "item-7514": {
        "value": 1,
        "weight": 8
      },
      "item-7515": {
        "value": 4,
        "weight": 6
      },
      "item-7516": {
        "value": 4,
        "weight": 6
      },
      "item-7517": {
        "value": 6,
        "weight": 4
      },
      "item-7518": {
        "value": 1,
        "weight": 3
      },
      "item-7519": {
        "value": 6,
        "weight": 4
      },
      "item-7520": {
        "value": 4,
        "weight": 7
      },
      "item-7521": {
        "value": 9,
        "weight": 2
      },
      "item-7522": {
        "value": 4,
        "weight": 5
      },
      "item-7523": {
        "value": 7,
        "weight": 2
      },
      "item-7524": {
        "value": 3,
        "weight": 4
      },
      "item-7525": {
        "value": 2,
        "weight": 1
      },
      "item-7526": {
        "value": 5,
        "weight": 5
      },
      "item-7527": {
        "value": 4,
        "weight": 4
      },
      "item-7528": {
        "value": 6,
        "weight": 7
      },
      "item-7529": {
        "value": 2,
        "weight": 2
      },
      "item-7530": {
        "value": 5,
        "weight": 4
      },
      "item-7531": {
        "value": 7,
        "weight": 5
      },
      "item-7532": {
        "value": 9,
        "weight": 3
      },
      "item-7533": {
        "value": 3,
        "weight": 6
      },
      "item-7534": {
        "value": 1,
        "weight": 5
      },
      "item-7535": {
        "value": 5,
        "weight": 6
      },
      "item-7536": {
        "value": 5,
        "weight": 8
      },
      "item-7537": {
        "value": 5,
        "weight": 2
      },
      "item-7538": {
        "value": 6,
        "weight": 4
      },
      "item-7539": {
        "value": 9,
        "weight": 5
      },
      "item-7540": {
        "value": 5,
        "weight": 5
      },
      "item-7541": {
        "value": 7,
        "weight": 8
      },
      "item-7542": {
        "value": 4,
        "weight": 8
      },
      "item-7543": {
        "value": 1,
        "weight": 7
      },
      "item-7544": {
        "value": 2,
        "weight": 2
      },
      "item-7545": {
        "value": 9,
        "weight": 7
      },
      "item-7546": {
        "value": 4,
        "weight": 7
      },
      "item-7547": {
        "value": 6,
        "weight": 8
      },
      "item-7548": {
        "value": 7,
        "weight": 2
      },
      "item-7549": {
        "value": 3,
        "weight": 8
      },
      "item-7550": {
        "value": 3,
        "weight": 3
      },
      "item-7551": {
        "value": 5,
        "weight": 6
      },
      "item-7552": {
        "value": 6,
        "weight": 5
      },
      "item-7553": {
        "value": 4,
        "weight": 6
      },
      "item-7554": {
        "value": 4,
        "weight": 7
      },
      "item-7555": {
        "value": 2,
        "weight": 6
      },
      "item-7556": {
        "value": 4,
        "weight": 1
      },
      "item-7557": {
        "value": 7,
        "weight": 8
      },
      "item-7558": {
        "value": 7,
        "weight": 8
      },
      "item-7559": {
        "value": 9,
        "weight": 6
      },
      "item-7560": {
        "value": 5,
        "weight": 8
      },
      "item-7561": {
        "value": 4,
        "weight": 6
      },
      "item-7562": {
        "value": 8,
        "weight": 4
      },
      "item-7563": {
        "value": 4,
        "weight": 6
      },
      "item-7564": {
        "value": 6,
        "weight": 4
      },
      "item-7565": {
        "value": 4,
        "weight": 3
      },
      "item-7566": {
        "value": 4,
        "weight": 3
      },
      "item-7567": {
        "value": 2,
        "weight": 7
      },
      "item-7568": {
        "value": 8,
        "weight": 5
      },
      "item-7569": {
        "value": 2,
        "weight": 8
      },
      "item-7570": {
        "value": 4,
        "weight": 9
      },
      "item-7571": {
        "value": 8,
        "weight": 3
      },
      "item-7572": {
        "value": 7,
        "weight": 1
      },
      "item-7573": {
        "value": 5,
        "weight": 1
      },
      "item-7574": {
        "value": 3,
        "weight": 7
      },
      "item-7575": {
        "value": 6,
        "weight": 8
      },
      "item-7576": {
        "value": 5,
        "weight": 8
      },
      "item-7577": {
        "value": 9,
        "weight": 5
      },
      "item-7578": {
        "value": 6,
        "weight": 3
      },
      "item-7579": {
        "value": 8,
        "weight": 8
      },
      "item-7580": {
        "value": 8,
        "weight": 6
      },
      "item-7581": {
        "value": 4,
        "weight": 5
      },
      "item-7582": {
        "value": 9,
        "weight": 4
      },
      "item-7583": {
        "value": 3,
        "weight": 1
      },
      "item-7584": {
        "value": 1,
        "weight": 1
      },
      "item-7585": {
        "value": 8,
        "weight": 1
      },
      "item-7586": {
        "value": 9,
        "weight": 5
      },
      "item-7587": {
        "value": 3,
        "weight": 8
      },
      "item-7588": {
        "value": 3,
        "weight": 7
      },
      "item-7589": {
        "value": 1,
        "weight": 9
      },
      "item-7590": {
        "value": 1,
        "weight": 6
      },
      "item-7591": {
        "value": 4,
        "weight": 1
      },
      "item-7592": {
        "value": 4,
        "weight": 5
      },
      "item-7593": {
        "value": 4,
        "weight": 5
      },
      "item-7594": {
        "value": 2,
        "weight": 8
      },
      "item-7595": {
        "value": 9,
        "weight": 2
      },
      "item-7596": {
        "value": 1,
        "weight": 1
      },
      "item-7597": {
        "value": 5,
        "weight": 7
      },
      "item-7598": {
        "value": 4,
        "weight": 9
      },
      "item-7599": {
        "value": 5,
        "weight": 2
      },
      "item-7600": {
        "value": 2,
        "weight": 9
      },
      "item-7601": {
        "value": 1,
        "weight": 2
      },
      "item-7602": {
        "value": 3,
        "weight": 1
      },
      "item-7603": {
        "value": 7,
        "weight": 4
      },
      "item-7604": {
        "value": 2,
        "weight": 6
      },
      "item-7605": {
        "value": 2,
        "weight": 2
      },
      "item-7606": {
        "value": 5,
        "weight": 8
      },
      "item-7607": {
        "value": 4,
        "weight": 8
      },
      "item-7608": {
        "value": 6,
        "weight": 6
      },
      "item-7609": {
        "value": 2,
        "weight": 9
      },
      "item-7610": {
        "value": 8,
        "weight": 6
      },
      "item-7611": {
        "value": 9,
        "weight": 9
      },
      "item-7612": {
        "value": 4,
        "weight": 6
      },
      "item-7613": {
        "value": 4,
        "weight": 5
      },
      "item-7614": {
        "value": 1,
        "weight": 1
      },
      "item-7615": {
        "value": 8,
        "weight": 5
      },
      "item-7616": {
        "value": 2,
        "weight": 6
      },
      "item-7617": {
        "value": 8,
        "weight": 1
      },
      "item-7618": {
        "value": 5,
        "weight": 2
      },
      "item-7619": {
        "value": 7,
        "weight": 4
      },
      "item-7620": {
        "value": 4,
        "weight": 1
      },
      "item-7621": {
        "value": 6,
        "weight": 2
      },
      "item-7622": {
        "value": 4,
        "weight": 3
      },
      "item-7623": {
        "value": 6,
        "weight": 5
      },
      "item-7624": {
        "value": 9,
        "weight": 9
      },
      "item-7625": {
        "value": 3,
        "weight": 8
      },
      "item-7626": {
        "value": 3,
        "weight": 6
      },
      "item-7627": {
        "value": 6,
        "weight": 3
      },
      "item-7628": {
        "value": 1,
        "weight": 3
      },
      "item-7629": {
        "value": 9,
        "weight": 4
      },
      "item-7630": {
        "value": 7,
        "weight": 9
      },
      "item-7631": {
        "value": 2,
        "weight": 5
      },
      "item-7632": {
        "value": 5,
        "weight": 6
      },
      "item-7633": {
        "value": 6,
        "weight": 5
      },
      "item-7634": {
        "value": 8,
        "weight": 2
      },
      "item-7635": {
        "value": 3,
        "weight": 7
      },
      "item-7636": {
        "value": 1,
        "weight": 3
      },
      "item-7637": {
        "value": 4,
        "weight": 3
      },
      "item-7638": {
        "value": 8,
        "weight": 2
      },
      "item-7639": {
        "value": 7,
        "weight": 6
      },
      "item-7640": {
        "value": 8,
        "weight": 1
      },
      "item-7641": {
        "value": 3,
        "weight": 3
      },
      "item-7642": {
        "value": 1,
        "weight": 3
      },
      "item-7643": {
        "value": 6,
        "weight": 8
      },
      "item-7644": {
        "value": 7,
        "weight": 2
      },
      "item-7645": {
        "value": 6,
        "weight": 8
      },
      "item-7646": {
        "value": 8,
        "weight": 7
      },
      "item-7647": {
        "value": 9,
        "weight": 3
      },
      "item-7648": {
        "value": 5,
        "weight": 2
      },
      "item-7649": {
        "value": 9,
        "weight": 7
      },
      "item-7650": {
        "value": 1,
        "weight": 8
      },
      "item-7651": {
        "value": 6,
        "weight": 6
      },
      "item-7652": {
        "value": 8,
        "weight": 4
      },
      "item-7653": {
        "value": 5,
        "weight": 1
      },
      "item-7654": {
        "value": 8,
        "weight": 7
      },
      "item-7655": {
        "value": 3,
        "weight": 4
      },
      "item-7656": {
        "value": 6,
        "weight": 6
      },
      "item-7657": {
        "value": 9,
        "weight": 6
      },
      "item-7658": {
        "value": 8,
        "weight": 6
      },
      "item-7659": {
        "value": 8,
        "weight": 5
      },
      "item-7660": {
        "value": 7,
        "weight": 9
      },
      "item-7661": {
        "value": 6,
        "weight": 8
      },
      "item-7662": {
        "value": 4,
        "weight": 8
      },
      "item-7663": {
        "value": 2,
        "weight": 5
      },
      "item-7664": {
        "value": 8,
        "weight": 4
      },
      "item-7665": {
        "value": 1,
        "weight": 4
      },
      "item-7666": {
        "value": 7,
        "weight": 2
      },
      "item-7667": {
        "value": 6,
        "weight": 2
      },
      "item-7668": {
        "value": 7,
        "weight": 1
      },
      "item-7669": {
        "value": 1,
        "weight": 3
      },
      "item-7670": {
        "value": 8,
        "weight": 4
      },
      "item-7671": {
        "value": 6,
        "weight": 4
      },
      "item-7672": {
        "value": 2,
        "weight": 6
      },
      "item-7673": {
        "value": 3,
        "weight": 4
      },
      "item-7674": {
        "value": 1,
        "weight": 6
      },
      "item-7675": {
        "value": 3,
        "weight": 3
      },
      "item-7676": {
        "value": 6,
        "weight": 6
      },
      "item-7677": {
        "value": 8,
        "weight": 4
      },
      "item-7678": {
        "value": 1,
        "weight": 5
      },
      "item-7679": {
        "value": 9,
        "weight": 2
      },
      "item-7680": {
        "value": 4,
        "weight": 7
      },
      "item-7681": {
        "value": 7,
        "weight": 7
      },
      "item-7682": {
        "value": 3,
        "weight": 3
      },
      "item-7683": {
        "value": 1,
        "weight": 5
      },
      "item-7684": {
        "value": 7,
        "weight": 1
      },
      "item-7685": {
        "value": 7,
        "weight": 4
      },
      "item-7686": {
        "value": 3,
        "weight": 4
      },
      "item-7687": {
        "value": 9,
        "weight": 3
      },
      "item-7688": {
        "value": 7,
        "weight": 9
      },
      "item-7689": {
        "value": 8,
        "weight": 6
      },
      "item-7690": {
        "value": 9,
        "weight": 7
      },
      "item-7691": {
        "value": 2,
        "weight": 3
      },
      "item-7692": {
        "value": 5,
        "weight": 3
      },
      "item-7693": {
        "value": 8,
        "weight": 9
      },
      "item-7694": {
        "value": 4,
        "weight": 1
      },
      "item-7695": {
        "value": 2,
        "weight": 3
      },
      "item-7696": {
        "value": 8,
        "weight": 5
      },
      "item-7697": {
        "value": 4,
        "weight": 7
      },
      "item-7698": {
        "value": 3,
        "weight": 8
      },
      "item-7699": {
        "value": 3,
        "weight": 8
      },
      "item-7700": {
        "value": 3,
        "weight": 4
      },
      "item-7701": {
        "value": 4,
        "weight": 7
      },
      "item-7702": {
        "value": 7,
        "weight": 1
      },
      "item-7703": {
        "value": 1,
        "weight": 1
      },
      "item-7704": {
        "value": 2,
        "weight": 9
      },
      "item-7705": {
        "value": 1,
        "weight": 9
      },
      "item-7706": {
        "value": 5,
        "weight": 7
      },
      "item-7707": {
        "value": 6,
        "weight": 5
      },
      "item-7708": {
        "value": 7,
        "weight": 6
      },
      "item-7709": {
        "value": 4,
        "weight": 9
      },
      "item-7710": {
        "value": 4,
        "weight": 7
      },
      "item-7711": {
        "value": 5,
        "weight": 6
      },
      "item-7712": {
        "value": 9,
        "weight": 2
      },
      "item-7713": {
        "value": 1,
        "weight": 4
      },
      "item-7714": {
        "value": 5,
        "weight": 4
      },
      "item-7715": {
        "value": 3,
        "weight": 2
      },
      "item-7716": {
        "value": 4,
        "weight": 8
      },
      "item-7717": {
        "value": 4,
        "weight": 1
      },
      "item-7718": {
        "value": 4,
        "weight": 8
      },
      "item-7719": {
        "value": 6,
        "weight": 3
      },
      "item-7720": {
        "value": 7,
        "weight": 7
      },
      "item-7721": {
        "value": 1,
        "weight": 3
      },
      "item-7722": {
        "value": 3,
        "weight": 9
      },
      "item-7723": {
        "value": 5,
        "weight": 8
      },
      "item-7724": {
        "value": 3,
        "weight": 6
      },
      "item-7725": {
        "value": 2,
        "weight": 4
      },
      "item-7726": {
        "value": 9,
        "weight": 8
      },
      "item-7727": {
        "value": 7,
        "weight": 2
      },
      "item-7728": {
        "value": 3,
        "weight": 9
      },
      "item-7729": {
        "value": 6,
        "weight": 1
      },
      "item-7730": {
        "value": 1,
        "weight": 1
      },
      "item-7731": {
        "value": 9,
        "weight": 6
      },
      "item-7732": {
        "value": 8,
        "weight": 9
      },
      "item-7733": {
        "value": 9,
        "weight": 5
      },
      "item-7734": {
        "value": 1,
        "weight": 9
      },
      "item-7735": {
        "value": 5,
        "weight": 8
      },
      "item-7736": {
        "value": 5,
        "weight": 9
      },
      "item-7737": {
        "value": 4,
        "weight": 2
      },
      "item-7738": {
        "value": 5,
        "weight": 4
      },
      "item-7739": {
        "value": 2,
        "weight": 8
      },
      "item-7740": {
        "value": 4,
        "weight": 7
      },
      "item-7741": {
        "value": 5,
        "weight": 6
      },
      "item-7742": {
        "value": 7,
        "weight": 7
      },
      "item-7743": {
        "value": 9,
        "weight": 3
      },
      "item-7744": {
        "value": 6,
        "weight": 2
      },
      "item-7745": {
        "value": 5,
        "weight": 3
      },
      "item-7746": {
        "value": 5,
        "weight": 8
      },
      "item-7747": {
        "value": 2,
        "weight": 6
      },
      "item-7748": {
        "value": 1,
        "weight": 9
      },
      "item-7749": {
        "value": 7,
        "weight": 1
      },
      "item-7750": {
        "value": 6,
        "weight": 1
      },
      "item-7751": {
        "value": 9,
        "weight": 4
      },
      "item-7752": {
        "value": 8,
        "weight": 9
      },
      "item-7753": {
        "value": 4,
        "weight": 4
      },
      "item-7754": {
        "value": 1,
        "weight": 3
      },
      "item-7755": {
        "value": 1,
        "weight": 1
      },
      "item-7756": {
        "value": 7,
        "weight": 4
      },
      "item-7757": {
        "value": 1,
        "weight": 2
      },
      "item-7758": {
        "value": 5,
        "weight": 6
      },
      "item-7759": {
        "value": 2,
        "weight": 1
      },
      "item-7760": {
        "value": 5,
        "weight": 4
      },
      "item-7761": {
        "value": 9,
        "weight": 7
      },
      "item-7762": {
        "value": 6,
        "weight": 6
      },
      "item-7763": {
        "value": 4,
        "weight": 2
      },
      "item-7764": {
        "value": 7,
        "weight": 7
      },
      "item-7765": {
        "value": 8,
        "weight": 5
      },
      "item-7766": {
        "value": 5,
        "weight": 7
      },
      "item-7767": {
        "value": 1,
        "weight": 6
      },
      "item-7768": {
        "value": 8,
        "weight": 1
      },
      "item-7769": {
        "value": 3,
        "weight": 3
      },
      "item-7770": {
        "value": 3,
        "weight": 3
      },
      "item-7771": {
        "value": 3,
        "weight": 5
      },
      "item-7772": {
        "value": 4,
        "weight": 2
      },
      "item-7773": {
        "value": 9,
        "weight": 8
      },
      "item-7774": {
        "value": 4,
        "weight": 5
      },
      "item-7775": {
        "value": 5,
        "weight": 8
      },
      "item-7776": {
        "value": 2,
        "weight": 1
      },
      "item-7777": {
        "value": 4,
        "weight": 7
      },
      "item-7778": {
        "value": 4,
        "weight": 8
      },
      "item-7779": {
        "value": 4,
        "weight": 4
      },
      "item-7780": {
        "value": 1,
        "weight": 8
      },
      "item-7781": {
        "value": 7,
        "weight": 7
      },
      "item-7782": {
        "value": 2,
        "weight": 9
      },
      "item-7783": {
        "value": 2,
        "weight": 4
      },
      "item-7784": {
        "value": 1,
        "weight": 2
      },
      "item-7785": {
        "value": 5,
        "weight": 9
      },
      "item-7786": {
        "value": 2,
        "weight": 7
      },
      "item-7787": {
        "value": 1,
        "weight": 2
      },
      "item-7788": {
        "value": 9,
        "weight": 2
      },
      "item-7789": {
        "value": 9,
        "weight": 6
      },
      "item-7790": {
        "value": 7,
        "weight": 4
      },
      "item-7791": {
        "value": 6,
        "weight": 2
      },
      "item-7792": {
        "value": 1,
        "weight": 7
      },
      "item-7793": {
        "value": 3,
        "weight": 2
      },
      "item-7794": {
        "value": 4,
        "weight": 8
      },
      "item-7795": {
        "value": 9,
        "weight": 2
      },
      "item-7796": {
        "value": 1,
        "weight": 3
      },
      "item-7797": {
        "value": 2,
        "weight": 9
      },
      "item-7798": {
        "value": 3,
        "weight": 7
      },
      "item-7799": {
        "value": 4,
        "weight": 8
      },
      "item-7800": {
        "value": 1,
        "weight": 5
      },
      "item-7801": {
        "value": 6,
        "weight": 6
      },
      "item-7802": {
        "value": 2,
        "weight": 5
      },
      "item-7803": {
        "value": 7,
        "weight": 3
      },
      "item-7804": {
        "value": 5,
        "weight": 7
      },
      "item-7805": {
        "value": 6,
        "weight": 5
      },
      "item-7806": {
        "value": 9,
        "weight": 8
      },
      "item-7807": {
        "value": 2,
        "weight": 4
      },
      "item-7808": {
        "value": 2,
        "weight": 6
      },
      "item-7809": {
        "value": 4,
        "weight": 4
      },
      "item-7810": {
        "value": 4,
        "weight": 8
      },
      "item-7811": {
        "value": 8,
        "weight": 2
      },
      "item-7812": {
        "value": 5,
        "weight": 9
      },
      "item-7813": {
        "value": 1,
        "weight": 6
      },
      "item-7814": {
        "value": 8,
        "weight": 8
      },
      "item-7815": {
        "value": 3,
        "weight": 4
      },
      "item-7816": {
        "value": 4,
        "weight": 5
      },
      "item-7817": {
        "value": 9,
        "weight": 6
      },
      "item-7818": {
        "value": 4,
        "weight": 8
      },
      "item-7819": {
        "value": 3,
        "weight": 4
      },
      "item-7820": {
        "value": 5,
        "weight": 1
      },
      "item-7821": {
        "value": 1,
        "weight": 4
      },
      "item-7822": {
        "value": 4,
        "weight": 4
      },
      "item-7823": {
        "value": 7,
        "weight": 7
      },
      "item-7824": {
        "value": 6,
        "weight": 2
      },
      "item-7825": {
        "value": 2,
        "weight": 6
      },
      "item-7826": {
        "value": 1,
        "weight": 5
      },
      "item-7827": {
        "value": 6,
        "weight": 6
      },
      "item-7828": {
        "value": 5,
        "weight": 4
      },
      "item-7829": {
        "value": 8,
        "weight": 3
      },
      "item-7830": {
        "value": 4,
        "weight": 4
      },
      "item-7831": {
        "value": 5,
        "weight": 5
      },
      "item-7832": {
        "value": 9,
        "weight": 9
      },
      "item-7833": {
        "value": 8,
        "weight": 7
      },
      "item-7834": {
        "value": 7,
        "weight": 7
      },
      "item-7835": {
        "value": 2,
        "weight": 3
      },
      "item-7836": {
        "value": 8,
        "weight": 8
      },
      "item-7837": {
        "value": 2,
        "weight": 3
      },
      "item-7838": {
        "value": 1,
        "weight": 9
      },
      "item-7839": {
        "value": 7,
        "weight": 3
      },
      "item-7840": {
        "value": 3,
        "weight": 3
      },
      "item-7841": {
        "value": 3,
        "weight": 3
      },
      "item-7842": {
        "value": 1,
        "weight": 7
      },
      "item-7843": {
        "value": 5,
        "weight": 9
      },
      "item-7844": {
        "value": 3,
        "weight": 1
      },
      "item-7845": {
        "value": 9,
        "weight": 9
      },
      "item-7846": {
        "value": 6,
        "weight": 2
      },
      "item-7847": {
        "value": 6,
        "weight": 8
      },
      "item-7848": {
        "value": 9,
        "weight": 3
      },
      "item-7849": {
        "value": 5,
        "weight": 7
      },
      "item-7850": {
        "value": 5,
        "weight": 8
      },
      "item-7851": {
        "value": 6,
        "weight": 3
      },
      "item-7852": {
        "value": 8,
        "weight": 7
      },
      "item-7853": {
        "value": 2,
        "weight": 3
      },
      "item-7854": {
        "value": 3,
        "weight": 1
      },
      "item-7855": {
        "value": 1,
        "weight": 4
      },
      "item-7856": {
        "value": 2,
        "weight": 5
      },
      "item-7857": {
        "value": 6,
        "weight": 8
      },
      "item-7858": {
        "value": 4,
        "weight": 2
      },
      "item-7859": {
        "value": 8,
        "weight": 1
      },
      "item-7860": {
        "value": 3,
        "weight": 8
      },
      "item-7861": {
        "value": 9,
        "weight": 8
      },
      "item-7862": {
        "value": 2,
        "weight": 3
      },
      "item-7863": {
        "value": 4,
        "weight": 8
      },
      "item-7864": {
        "value": 9,
        "weight": 1
      },
      "item-7865": {
        "value": 2,
        "weight": 1
      },
      "item-7866": {
        "value": 7,
        "weight": 3
      },
      "item-7867": {
        "value": 7,
        "weight": 4
      },
      "item-7868": {
        "value": 8,
        "weight": 9
      },
      "item-7869": {
        "value": 2,
        "weight": 3
      },
      "item-7870": {
        "value": 5,
        "weight": 8
      },
      "item-7871": {
        "value": 9,
        "weight": 4
      },
      "item-7872": {
        "value": 8,
        "weight": 3
      },
      "item-7873": {
        "value": 7,
        "weight": 7
      },
      "item-7874": {
        "value": 5,
        "weight": 8
      },
      "item-7875": {
        "value": 8,
        "weight": 7
      },
      "item-7876": {
        "value": 9,
        "weight": 4
      },
      "item-7877": {
        "value": 3,
        "weight": 1
      },
      "item-7878": {
        "value": 7,
        "weight": 5
      },
      "item-7879": {
        "value": 6,
        "weight": 4
      },
      "item-7880": {
        "value": 3,
        "weight": 6
      },
      "item-7881": {
        "value": 8,
        "weight": 6
      },
      "item-7882": {
        "value": 3,
        "weight": 8
      },
      "item-7883": {
        "value": 8,
        "weight": 6
      },
      "item-7884": {
        "value": 6,
        "weight": 4
      },
      "item-7885": {
        "value": 6,
        "weight": 7
      },
      "item-7886": {
        "value": 9,
        "weight": 5
      },
      "item-7887": {
        "value": 8,
        "weight": 7
      },
      "item-7888": {
        "value": 4,
        "weight": 5
      },
      "item-7889": {
        "value": 1,
        "weight": 5
      },
      "item-7890": {
        "value": 2,
        "weight": 2
      },
      "item-7891": {
        "value": 9,
        "weight": 8
      },
      "item-7892": {
        "value": 4,
        "weight": 6
      },
      "item-7893": {
        "value": 7,
        "weight": 4
      },
      "item-7894": {
        "value": 9,
        "weight": 6
      },
      "item-7895": {
        "value": 1,
        "weight": 2
      },
      "item-7896": {
        "value": 9,
        "weight": 6
      },
      "item-7897": {
        "value": 6,
        "weight": 4
      },
      "item-7898": {
        "value": 3,
        "weight": 5
      },
      "item-7899": {
        "value": 2,
        "weight": 8
      },
      "item-7900": {
        "value": 5,
        "weight": 2
      },
      "item-7901": {
        "value": 6,
        "weight": 7
      },
      "item-7902": {
        "value": 4,
        "weight": 4
      },
      "item-7903": {
        "value": 3,
        "weight": 2
      },
      "item-7904": {
        "value": 8,
        "weight": 4
      },
      "item-7905": {
        "value": 4,
        "weight": 7
      },
      "item-7906": {
        "value": 5,
        "weight": 1
      },
      "item-7907": {
        "value": 3,
        "weight": 9
      },
      "item-7908": {
        "value": 1,
        "weight": 2
      },
      "item-7909": {
        "value": 8,
        "weight": 8
      },
      "item-7910": {
        "value": 2,
        "weight": 3
      },
      "item-7911": {
        "value": 5,
        "weight": 5
      },
      "item-7912": {
        "value": 4,
        "weight": 6
      },
      "item-7913": {
        "value": 5,
        "weight": 9
      },
      "item-7914": {
        "value": 6,
        "weight": 4
      },
      "item-7915": {
        "value": 8,
        "weight": 5
      },
      "item-7916": {
        "value": 5,
        "weight": 7
      },
      "item-7917": {
        "value": 9,
        "weight": 9
      },
      "item-7918": {
        "value": 1,
        "weight": 5
      },
      "item-7919": {
        "value": 1,
        "weight": 3
      },
      "item-7920": {
        "value": 5,
        "weight": 5
      },
      "item-7921": {
        "value": 4,
        "weight": 9
      },
      "item-7922": {
        "value": 8,
        "weight": 1
      },
      "item-7923": {
        "value": 1,
        "weight": 9
      },
      "item-7924": {
        "value": 6,
        "weight": 3
      },
      "item-7925": {
        "value": 6,
        "weight": 5
      },
      "item-7926": {
        "value": 8,
        "weight": 4
      },
      "item-7927": {
        "value": 1,
        "weight": 3
      },
      "item-7928": {
        "value": 1,
        "weight": 1
      },
      "item-7929": {
        "value": 6,
        "weight": 9
      },
      "item-7930": {
        "value": 7,
        "weight": 7
      },
      "item-7931": {
        "value": 9,
        "weight": 5
      },
      "item-7932": {
        "value": 9,
        "weight": 4
      },
      "item-7933": {
        "value": 5,
        "weight": 9
      },
      "item-7934": {
        "value": 3,
        "weight": 4
      },
      "item-7935": {
        "value": 8,
        "weight": 2
      },
      "item-7936": {
        "value": 4,
        "weight": 6
      },
      "item-7937": {
        "value": 1,
        "weight": 8
      },
      "item-7938": {
        "value": 7,
        "weight": 8
      },
      "item-7939": {
        "value": 3,
        "weight": 6
      },
      "item-7940": {
        "value": 9,
        "weight": 2
      },
      "item-7941": {
        "value": 6,
        "weight": 7
      },
      "item-7942": {
        "value": 7,
        "weight": 1
      },
      "item-7943": {
        "value": 8,
        "weight": 7
      },
      "item-7944": {
        "value": 1,
        "weight": 6
      },
      "item-7945": {
        "value": 2,
        "weight": 6
      },
      "item-7946": {
        "value": 5,
        "weight": 8
      },
      "item-7947": {
        "value": 4,
        "weight": 9
      },
      "item-7948": {
        "value": 8,
        "weight": 3
      },
      "item-7949": {
        "value": 3,
        "weight": 7
      },
      "item-7950": {
        "value": 5,
        "weight": 5
      },
      "item-7951": {
        "value": 6,
        "weight": 5
      },
      "item-7952": {
        "value": 3,
        "weight": 1
      },
      "item-7953": {
        "value": 5,
        "weight": 7
      },
      "item-7954": {
        "value": 3,
        "weight": 8
      },
      "item-7955": {
        "value": 7,
        "weight": 1
      },
      "item-7956": {
        "value": 9,
        "weight": 4
      },
      "item-7957": {
        "value": 8,
        "weight": 1
      },
      "item-7958": {
        "value": 6,
        "weight": 6
      },
      "item-7959": {
        "value": 6,
        "weight": 2
      },
      "item-7960": {
        "value": 6,
        "weight": 2
      },
      "item-7961": {
        "value": 5,
        "weight": 8
      },
      "item-7962": {
        "value": 6,
        "weight": 2
      },
      "item-7963": {
        "value": 7,
        "weight": 7
      },
      "item-7964": {
        "value": 3,
        "weight": 4
      },
      "item-7965": {
        "value": 7,
        "weight": 7
      },
      "item-7966": {
        "value": 6,
        "weight": 4
      },
      "item-7967": {
        "value": 3,
        "weight": 4
      },
      "item-7968": {
        "value": 9,
        "weight": 3
      },
      "item-7969": {
        "value": 2,
        "weight": 1
      },
      "item-7970": {
        "value": 1,
        "weight": 9
      },
      "item-7971": {
        "value": 6,
        "weight": 2
      },
      "item-7972": {
        "value": 2,
        "weight": 4
      },
      "item-7973": {
        "value": 9,
        "weight": 8
      },
      "item-7974": {
        "value": 7,
        "weight": 9
      },
      "item-7975": {
        "value": 4,
        "weight": 5
      },
      "item-7976": {
        "value": 9,
        "weight": 9
      },
      "item-7977": {
        "value": 4,
        "weight": 8
      },
      "item-7978": {
        "value": 1,
        "weight": 4
      },
      "item-7979": {
        "value": 7,
        "weight": 5
      },
      "item-7980": {
        "value": 9,
        "weight": 4
      },
      "item-7981": {
        "value": 5,
        "weight": 2
      },
      "item-7982": {
        "value": 7,
        "weight": 2
      },
      "item-7983": {
        "value": 9,
        "weight": 4
      },
      "item-7984": {
        "value": 6,
        "weight": 3
      },
      "item-7985": {
        "value": 5,
        "weight": 5
      },
      "item-7986": {
        "value": 1,
        "weight": 7
      },
      "item-7987": {
        "value": 5,
        "weight": 1
      },
      "item-7988": {
        "value": 4,
        "weight": 1
      },
      "item-7989": {
        "value": 1,
        "weight": 8
      },
      "item-7990": {
        "value": 1,
        "weight": 3
      },
      "item-7991": {
        "value": 7,
        "weight": 3
      },
      "item-7992": {
        "value": 1,
        "weight": 6
      },
      "item-7993": {
        "value": 8,
        "weight": 3
      },
      "item-7994": {
        "value": 1,
        "weight": 5
      },
      "item-7995": {
        "value": 2,
        "weight": 4
      },
      "item-7996": {
        "value": 8,
        "weight": 8
      },
      "item-7997": {
        "value": 6,
        "weight": 1
      },
      "item-7998": {
        "value": 9,
        "weight": 4
      },
      "item-7999": {
        "value": 9,
        "weight": 6
      },
      "item-8000": {
        "value": 3,
        "weight": 3
      },
      "item-8001": {
        "value": 3,
        "weight": 6
      },
      "item-8002": {
        "value": 3,
        "weight": 7
      },
      "item-8003": {
        "value": 8,
        "weight": 5
      },
      "item-8004": {
        "value": 5,
        "weight": 8
      },
      "item-8005": {
        "value": 3,
        "weight": 3
      },
      "item-8006": {
        "value": 5,
        "weight": 8
      },
      "item-8007": {
        "value": 7,
        "weight": 4
      },
      "item-8008": {
        "value": 3,
        "weight": 1
      },
      "item-8009": {
        "value": 3,
        "weight": 3
      },
      "item-8010": {
        "value": 5,
        "weight": 2
      },
      "item-8011": {
        "value": 1,
        "weight": 7
      },
      "item-8012": {
        "value": 9,
        "weight": 8
      },
      "item-8013": {
        "value": 2,
        "weight": 6
      },
      "item-8014": {
        "value": 5,
        "weight": 3
      },
      "item-8015": {
        "value": 1,
        "weight": 6
      },
      "item-8016": {
        "value": 1,
        "weight": 3
      },
      "item-8017": {
        "value": 8,
        "weight": 4
      },
      "item-8018": {
        "value": 3,
        "weight": 5
      },
      "item-8019": {
        "value": 9,
        "weight": 9
      },
      "item-8020": {
        "value": 8,
        "weight": 1
      },
      "item-8021": {
        "value": 8,
        "weight": 9
      },
      "item-8022": {
        "value": 7,
        "weight": 4
      },
      "item-8023": {
        "value": 8,
        "weight": 3
      },
      "item-8024": {
        "value": 8,
        "weight": 3
      },
      "item-8025": {
        "value": 5,
        "weight": 2
      },
      "item-8026": {
        "value": 3,
        "weight": 1
      },
      "item-8027": {
        "value": 1,
        "weight": 9
      },
      "item-8028": {
        "value": 3,
        "weight": 9
      },
      "item-8029": {
        "value": 4,
        "weight": 1
      },
      "item-8030": {
        "value": 7,
        "weight": 6
      },
      "item-8031": {
        "value": 5,
        "weight": 5
      },
      "item-8032": {
        "value": 4,
        "weight": 6
      },
      "item-8033": {
        "value": 7,
        "weight": 2
      },
      "item-8034": {
        "value": 7,
        "weight": 6
      },
      "item-8035": {
        "value": 5,
        "weight": 9
      },
      "item-8036": {
        "value": 3,
        "weight": 7
      },
      "item-8037": {
        "value": 1,
        "weight": 7
      },
      "item-8038": {
        "value": 6,
        "weight": 7
      },
      "item-8039": {
        "value": 7,
        "weight": 5
      },
      "item-8040": {
        "value": 4,
        "weight": 8
      },
      "item-8041": {
        "value": 4,
        "weight": 2
      },
      "item-8042": {
        "value": 5,
        "weight": 4
      },
      "item-8043": {
        "value": 1,
        "weight": 3
      },
      "item-8044": {
        "value": 5,
        "weight": 9
      },
      "item-8045": {
        "value": 7,
        "weight": 4
      },
      "item-8046": {
        "value": 1,
        "weight": 9
      },
      "item-8047": {
        "value": 7,
        "weight": 9
      },
      "item-8048": {
        "value": 4,
        "weight": 2
      },
      "item-8049": {
        "value": 6,
        "weight": 4
      },
      "item-8050": {
        "value": 7,
        "weight": 1
      },
      "item-8051": {
        "value": 4,
        "weight": 2
      },
      "item-8052": {
        "value": 6,
        "weight": 7
      },
      "item-8053": {
        "value": 4,
        "weight": 4
      },
      "item-8054": {
        "value": 6,
        "weight": 8
      },
      "item-8055": {
        "value": 3,
        "weight": 4
      },
      "item-8056": {
        "value": 5,
        "weight": 5
      },
      "item-8057": {
        "value": 2,
        "weight": 2
      },
      "item-8058": {
        "value": 9,
        "weight": 7
      },
      "item-8059": {
        "value": 2,
        "weight": 4
      },
      "item-8060": {
        "value": 8,
        "weight": 2
      },
      "item-8061": {
        "value": 1,
        "weight": 7
      },
      "item-8062": {
        "value": 8,
        "weight": 2
      },
      "item-8063": {
        "value": 1,
        "weight": 6
      },
      "item-8064": {
        "value": 7,
        "weight": 3
      },
      "item-8065": {
        "value": 2,
        "weight": 4
      },
      "item-8066": {
        "value": 3,
        "weight": 1
      },
      "item-8067": {
        "value": 1,
        "weight": 3
      },
      "item-8068": {
        "value": 8,
        "weight": 3
      },
      "item-8069": {
        "value": 5,
        "weight": 3
      },
      "item-8070": {
        "value": 5,
        "weight": 7
      },
      "item-8071": {
        "value": 2,
        "weight": 7
      },
      "item-8072": {
        "value": 1,
        "weight": 3
      },
      "item-8073": {
        "value": 9,
        "weight": 9
      },
      "item-8074": {
        "value": 3,
        "weight": 5
      },
      "item-8075": {
        "value": 6,
        "weight": 6
      },
      "item-8076": {
        "value": 6,
        "weight": 5
      },
      "item-8077": {
        "value": 4,
        "weight": 3
      },
      "item-8078": {
        "value": 8,
        "weight": 9
      },
      "item-8079": {
        "value": 6,
        "weight": 9
      },
      "item-8080": {
        "value": 4,
        "weight": 2
      },
      "item-8081": {
        "value": 8,
        "weight": 5
      },
      "item-8082": {
        "value": 8,
        "weight": 5
      },
      "item-8083": {
        "value": 1,
        "weight": 3
      },
      "item-8084": {
        "value": 7,
        "weight": 8
      },
      "item-8085": {
        "value": 6,
        "weight": 7
      },
      "item-8086": {
        "value": 5,
        "weight": 9
      },
      "item-8087": {
        "value": 9,
        "weight": 5
      },
      "item-8088": {
        "value": 4,
        "weight": 5
      },
      "item-8089": {
        "value": 6,
        "weight": 4
      },
      "item-8090": {
        "value": 8,
        "weight": 8
      },
      "item-8091": {
        "value": 8,
        "weight": 2
      },
      "item-8092": {
        "value": 7,
        "weight": 8
      },
      "item-8093": {
        "value": 8,
        "weight": 3
      },
      "item-8094": {
        "value": 2,
        "weight": 1
      },
      "item-8095": {
        "value": 8,
        "weight": 9
      },
      "item-8096": {
        "value": 7,
        "weight": 8
      },
      "item-8097": {
        "value": 5,
        "weight": 1
      },
      "item-8098": {
        "value": 2,
        "weight": 9
      },
      "item-8099": {
        "value": 5,
        "weight": 9
      },
      "item-8100": {
        "value": 1,
        "weight": 6
      },
      "item-8101": {
        "value": 6,
        "weight": 3
      },
      "item-8102": {
        "value": 7,
        "weight": 9
      },
      "item-8103": {
        "value": 5,
        "weight": 6
      },
      "item-8104": {
        "value": 4,
        "weight": 6
      },
      "item-8105": {
        "value": 8,
        "weight": 8
      },
      "item-8106": {
        "value": 9,
        "weight": 1
      },
      "item-8107": {
        "value": 8,
        "weight": 6
      },
      "item-8108": {
        "value": 6,
        "weight": 2
      },
      "item-8109": {
        "value": 1,
        "weight": 2
      },
      "item-8110": {
        "value": 5,
        "weight": 4
      },
      "item-8111": {
        "value": 9,
        "weight": 6
      },
      "item-8112": {
        "value": 4,
        "weight": 2
      },
      "item-8113": {
        "value": 7,
        "weight": 9
      },
      "item-8114": {
        "value": 6,
        "weight": 1
      },
      "item-8115": {
        "value": 8,
        "weight": 8
      },
      "item-8116": {
        "value": 2,
        "weight": 9
      },
      "item-8117": {
        "value": 8,
        "weight": 9
      },
      "item-8118": {
        "value": 3,
        "weight": 3
      },
      "item-8119": {
        "value": 3,
        "weight": 8
      },
      "item-8120": {
        "value": 1,
        "weight": 5
      },
      "item-8121": {
        "value": 6,
        "weight": 8
      },
      "item-8122": {
        "value": 1,
        "weight": 5
      },
      "item-8123": {
        "value": 4,
        "weight": 1
      },
      "item-8124": {
        "value": 1,
        "weight": 4
      },
      "item-8125": {
        "value": 2,
        "weight": 6
      },
      "item-8126": {
        "value": 9,
        "weight": 1
      },
      "item-8127": {
        "value": 9,
        "weight": 5
      },
      "item-8128": {
        "value": 6,
        "weight": 2
      },
      "item-8129": {
        "value": 1,
        "weight": 7
      },
      "item-8130": {
        "value": 3,
        "weight": 8
      },
      "item-8131": {
        "value": 5,
        "weight": 6
      },
      "item-8132": {
        "value": 6,
        "weight": 1
      },
      "item-8133": {
        "value": 9,
        "weight": 3
      },
      "item-8134": {
        "value": 3,
        "weight": 2
      },
      "item-8135": {
        "value": 4,
        "weight": 2
      },
      "item-8136": {
        "value": 1,
        "weight": 5
      },
      "item-8137": {
        "value": 8,
        "weight": 9
      },
      "item-8138": {
        "value": 2,
        "weight": 2
      },
      "item-8139": {
        "value": 3,
        "weight": 9
      },
      "item-8140": {
        "value": 2,
        "weight": 2
      },
      "item-8141": {
        "value": 2,
        "weight": 2
      },
      "item-8142": {
        "value": 5,
        "weight": 2
      },
      "item-8143": {
        "value": 9,
        "weight": 2
      },
      "item-8144": {
        "value": 8,
        "weight": 1
      },
      "item-8145": {
        "value": 8,
        "weight": 1
      },
      "item-8146": {
        "value": 5,
        "weight": 3
      },
      "item-8147": {
        "value": 2,
        "weight": 1
      },
      "item-8148": {
        "value": 3,
        "weight": 2
      },
      "item-8149": {
        "value": 9,
        "weight": 1
      },
      "item-8150": {
        "value": 1,
        "weight": 9
      },
      "item-8151": {
        "value": 1,
        "weight": 7
      },
      "item-8152": {
        "value": 3,
        "weight": 6
      },
      "item-8153": {
        "value": 1,
        "weight": 7
      },
      "item-8154": {
        "value": 6,
        "weight": 9
      },
      "item-8155": {
        "value": 8,
        "weight": 8
      },
      "item-8156": {
        "value": 7,
        "weight": 9
      },
      "item-8157": {
        "value": 1,
        "weight": 8
      },
      "item-8158": {
        "value": 3,
        "weight": 7
      },
      "item-8159": {
        "value": 3,
        "weight": 7
      },
      "item-8160": {
        "value": 3,
        "weight": 4
      },
      "item-8161": {
        "value": 9,
        "weight": 8
      },
      "item-8162": {
        "value": 3,
        "weight": 7
      },
      "item-8163": {
        "value": 7,
        "weight": 9
      },
      "item-8164": {
        "value": 5,
        "weight": 3
      },
      "item-8165": {
        "value": 1,
        "weight": 4
      },
      "item-8166": {
        "value": 1,
        "weight": 2
      },
      "item-8167": {
        "value": 9,
        "weight": 1
      },
      "item-8168": {
        "value": 3,
        "weight": 4
      },
      "item-8169": {
        "value": 3,
        "weight": 8
      },
      "item-8170": {
        "value": 5,
        "weight": 2
      },
      "item-8171": {
        "value": 9,
        "weight": 3
      },
      "item-8172": {
        "value": 8,
        "weight": 3
      },
      "item-8173": {
        "value": 5,
        "weight": 2
      },
      "item-8174": {
        "value": 7,
        "weight": 2
      },
      "item-8175": {
        "value": 2,
        "weight": 8
      },
      "item-8176": {
        "value": 3,
        "weight": 7
      },
      "item-8177": {
        "value": 2,
        "weight": 4
      },
      "item-8178": {
        "value": 1,
        "weight": 5
      },
      "item-8179": {
        "value": 8,
        "weight": 8
      },
      "item-8180": {
        "value": 7,
        "weight": 5
      },
      "item-8181": {
        "value": 6,
        "weight": 8
      },
      "item-8182": {
        "value": 6,
        "weight": 9
      },
      "item-8183": {
        "value": 7,
        "weight": 8
      },
      "item-8184": {
        "value": 1,
        "weight": 1
      },
      "item-8185": {
        "value": 9,
        "weight": 5
      },
      "item-8186": {
        "value": 7,
        "weight": 2
      },
      "item-8187": {
        "value": 8,
        "weight": 4
      },
      "item-8188": {
        "value": 7,
        "weight": 8
      },
      "item-8189": {
        "value": 9,
        "weight": 9
      },
      "item-8190": {
        "value": 2,
        "weight": 7
      },
      "item-8191": {
        "value": 3,
        "weight": 1
      },
      "item-8192": {
        "value": 5,
        "weight": 9
      },
      "item-8193": {
        "value": 5,
        "weight": 9
      },
      "item-8194": {
        "value": 7,
        "weight": 4
      },
      "item-8195": {
        "value": 6,
        "weight": 4
      },
      "item-8196": {
        "value": 4,
        "weight": 3
      },
      "item-8197": {
        "value": 6,
        "weight": 2
      },
      "item-8198": {
        "value": 4,
        "weight": 2
      },
      "item-8199": {
        "value": 7,
        "weight": 3
      },
      "item-8200": {
        "value": 6,
        "weight": 8
      },
      "item-8201": {
        "value": 6,
        "weight": 4
      },
      "item-8202": {
        "value": 3,
        "weight": 5
      },
      "item-8203": {
        "value": 1,
        "weight": 7
      },
      "item-8204": {
        "value": 1,
        "weight": 6
      },
      "item-8205": {
        "value": 8,
        "weight": 9
      },
      "item-8206": {
        "value": 4,
        "weight": 9
      },
      "item-8207": {
        "value": 7,
        "weight": 7
      },
      "item-8208": {
        "value": 2,
        "weight": 8
      },
      "item-8209": {
        "value": 2,
        "weight": 2
      },
      "item-8210": {
        "value": 6,
        "weight": 3
      },
      "item-8211": {
        "value": 2,
        "weight": 7
      },
      "item-8212": {
        "value": 2,
        "weight": 2
      },
      "item-8213": {
        "value": 5,
        "weight": 2
      },
      "item-8214": {
        "value": 7,
        "weight": 3
      },
      "item-8215": {
        "value": 1,
        "weight": 3
      },
      "item-8216": {
        "value": 1,
        "weight": 7
      },
      "item-8217": {
        "value": 9,
        "weight": 6
      },
      "item-8218": {
        "value": 1,
        "weight": 6
      },
      "item-8219": {
        "value": 2,
        "weight": 9
      },
      "item-8220": {
        "value": 3,
        "weight": 4
      },
      "item-8221": {
        "value": 9,
        "weight": 5
      },
      "item-8222": {
        "value": 9,
        "weight": 7
      },
      "item-8223": {
        "value": 5,
        "weight": 9
      },
      "item-8224": {
        "value": 8,
        "weight": 1
      },
      "item-8225": {
        "value": 1,
        "weight": 2
      },
      "item-8226": {
        "value": 6,
        "weight": 5
      },
      "item-8227": {
        "value": 1,
        "weight": 3
      },
      "item-8228": {
        "value": 2,
        "weight": 8
      },
      "item-8229": {
        "value": 1,
        "weight": 4
      },
      "item-8230": {
        "value": 9,
        "weight": 5
      },
      "item-8231": {
        "value": 3,
        "weight": 4
      },
      "item-8232": {
        "value": 1,
        "weight": 5
      },
      "item-8233": {
        "value": 5,
        "weight": 6
      },
      "item-8234": {
        "value": 2,
        "weight": 8
      },
      "item-8235": {
        "value": 9,
        "weight": 3
      },
      "item-8236": {
        "value": 7,
        "weight": 3
      },
      "item-8237": {
        "value": 8,
        "weight": 8
      },
      "item-8238": {
        "value": 4,
        "weight": 2
      },
      "item-8239": {
        "value": 2,
        "weight": 8
      },
      "item-8240": {
        "value": 6,
        "weight": 4
      },
      "item-8241": {
        "value": 9,
        "weight": 4
      },
      "item-8242": {
        "value": 1,
        "weight": 2
      },
      "item-8243": {
        "value": 1,
        "weight": 2
      },
      "item-8244": {
        "value": 4,
        "weight": 8
      },
      "item-8245": {
        "value": 3,
        "weight": 2
      },
      "item-8246": {
        "value": 1,
        "weight": 8
      },
      "item-8247": {
        "value": 2,
        "weight": 6
      },
      "item-8248": {
        "value": 7,
        "weight": 2
      },
      "item-8249": {
        "value": 9,
        "weight": 7
      },
      "item-8250": {
        "value": 3,
        "weight": 8
      },
      "item-8251": {
        "value": 9,
        "weight": 2
      },
      "item-8252": {
        "value": 2,
        "weight": 5
      },
      "item-8253": {
        "value": 1,
        "weight": 8
      },
      "item-8254": {
        "value": 9,
        "weight": 3
      },
      "item-8255": {
        "value": 5,
        "weight": 1
      },
      "item-8256": {
        "value": 6,
        "weight": 2
      },
      "item-8257": {
        "value": 9,
        "weight": 1
      },
      "item-8258": {
        "value": 1,
        "weight": 1
      },
      "item-8259": {
        "value": 2,
        "weight": 5
      },
      "item-8260": {
        "value": 7,
        "weight": 3
      },
      "item-8261": {
        "value": 9,
        "weight": 9
      },
      "item-8262": {
        "value": 9,
        "weight": 3
      },
      "item-8263": {
        "value": 5,
        "weight": 8
      },
      "item-8264": {
        "value": 5,
        "weight": 3
      },
      "item-8265": {
        "value": 3,
        "weight": 7
      },
      "item-8266": {
        "value": 8,
        "weight": 7
      },
      "item-8267": {
        "value": 3,
        "weight": 2
      },
      "item-8268": {
        "value": 2,
        "weight": 8
      },
      "item-8269": {
        "value": 2,
        "weight": 2
      },
      "item-8270": {
        "value": 1,
        "weight": 3
      },
      "item-8271": {
        "value": 7,
        "weight": 2
      },
      "item-8272": {
        "value": 1,
        "weight": 8
      },
      "item-8273": {
        "value": 3,
        "weight": 2
      },
      "item-8274": {
        "value": 8,
        "weight": 9
      },
      "item-8275": {
        "value": 6,
        "weight": 9
      },
      "item-8276": {
        "value": 6,
        "weight": 1
      },
      "item-8277": {
        "value": 1,
        "weight": 3
      },
      "item-8278": {
        "value": 2,
        "weight": 2
      },
      "item-8279": {
        "value": 1,
        "weight": 5
      },
      "item-8280": {
        "value": 1,
        "weight": 2
      },
      "item-8281": {
        "value": 1,
        "weight": 3
      },
      "item-8282": {
        "value": 6,
        "weight": 9
      },
      "item-8283": {
        "value": 7,
        "weight": 8
      },
      "item-8284": {
        "value": 7,
        "weight": 3
      },
      "item-8285": {
        "value": 8,
        "weight": 2
      },
      "item-8286": {
        "value": 8,
        "weight": 7
      },
      "item-8287": {
        "value": 5,
        "weight": 2
      },
      "item-8288": {
        "value": 7,
        "weight": 1
      },
      "item-8289": {
        "value": 8,
        "weight": 5
      },
      "item-8290": {
        "value": 2,
        "weight": 9
      },
      "item-8291": {
        "value": 4,
        "weight": 5
      },
      "item-8292": {
        "value": 6,
        "weight": 5
      },
      "item-8293": {
        "value": 5,
        "weight": 6
      },
      "item-8294": {
        "value": 2,
        "weight": 3
      },
      "item-8295": {
        "value": 4,
        "weight": 9
      },
      "item-8296": {
        "value": 6,
        "weight": 4
      },
      "item-8297": {
        "value": 2,
        "weight": 8
      },
      "item-8298": {
        "value": 7,
        "weight": 6
      },
      "item-8299": {
        "value": 4,
        "weight": 1
      },
      "item-8300": {
        "value": 7,
        "weight": 3
      },
      "item-8301": {
        "value": 9,
        "weight": 7
      },
      "item-8302": {
        "value": 7,
        "weight": 6
      },
      "item-8303": {
        "value": 2,
        "weight": 1
      },
      "item-8304": {
        "value": 4,
        "weight": 5
      },
      "item-8305": {
        "value": 4,
        "weight": 2
      },
      "item-8306": {
        "value": 5,
        "weight": 3
      },
      "item-8307": {
        "value": 7,
        "weight": 1
      },
      "item-8308": {
        "value": 7,
        "weight": 4
      },
      "item-8309": {
        "value": 1,
        "weight": 3
      },
      "item-8310": {
        "value": 4,
        "weight": 9
      },
      "item-8311": {
        "value": 6,
        "weight": 3
      },
      "item-8312": {
        "value": 2,
        "weight": 4
      },
      "item-8313": {
        "value": 1,
        "weight": 5
      },
      "item-8314": {
        "value": 4,
        "weight": 6
      },
      "item-8315": {
        "value": 7,
        "weight": 4
      },
      "item-8316": {
        "value": 5,
        "weight": 9
      },
      "item-8317": {
        "value": 1,
        "weight": 7
      },
      "item-8318": {
        "value": 1,
        "weight": 5
      },
      "item-8319": {
        "value": 8,
        "weight": 8
      },
      "item-8320": {
        "value": 3,
        "weight": 3
      },
      "item-8321": {
        "value": 6,
        "weight": 7
      },
      "item-8322": {
        "value": 4,
        "weight": 1
      },
      "item-8323": {
        "value": 3,
        "weight": 9
      },
      "item-8324": {
        "value": 7,
        "weight": 6
      },
      "item-8325": {
        "value": 5,
        "weight": 7
      },
      "item-8326": {
        "value": 7,
        "weight": 6
      },
      "item-8327": {
        "value": 6,
        "weight": 8
      },
      "item-8328": {
        "value": 2,
        "weight": 5
      },
      "item-8329": {
        "value": 1,
        "weight": 2
      },
      "item-8330": {
        "value": 1,
        "weight": 1
      },
      "item-8331": {
        "value": 8,
        "weight": 4
      },
      "item-8332": {
        "value": 4,
        "weight": 7
      },
      "item-8333": {
        "value": 7,
        "weight": 5
      },
      "item-8334": {
        "value": 5,
        "weight": 6
      },
      "item-8335": {
        "value": 4,
        "weight": 2
      },
      "item-8336": {
        "value": 8,
        "weight": 2
      },
      "item-8337": {
        "value": 2,
        "weight": 9
      },
      "item-8338": {
        "value": 5,
        "weight": 6
      },
      "item-8339": {
        "value": 7,
        "weight": 1
      },
      "item-8340": {
        "value": 4,
        "weight": 8
      },
      "item-8341": {
        "value": 5,
        "weight": 8
      },
      "item-8342": {
        "value": 5,
        "weight": 8
      },
      "item-8343": {
        "value": 8,
        "weight": 6
      },
      "item-8344": {
        "value": 5,
        "weight": 5
      },
      "item-8345": {
        "value": 4,
        "weight": 1
      },
      "item-8346": {
        "value": 9,
        "weight": 9
      },
      "item-8347": {
        "value": 2,
        "weight": 6
      },
      "item-8348": {
        "value": 9,
        "weight": 5
      },
      "item-8349": {
        "value": 1,
        "weight": 4
      },
      "item-8350": {
        "value": 8,
        "weight": 8
      },
      "item-8351": {
        "value": 3,
        "weight": 6
      },
      "item-8352": {
        "value": 5,
        "weight": 8
      },
      "item-8353": {
        "value": 9,
        "weight": 4
      },
      "item-8354": {
        "value": 8,
        "weight": 6
      },
      "item-8355": {
        "value": 3,
        "weight": 6
      },
      "item-8356": {
        "value": 9,
        "weight": 5
      },
      "item-8357": {
        "value": 7,
        "weight": 4
      },
      "item-8358": {
        "value": 7,
        "weight": 9
      },
      "item-8359": {
        "value": 7,
        "weight": 6
      },
      "item-8360": {
        "value": 8,
        "weight": 6
      },
      "item-8361": {
        "value": 3,
        "weight": 7
      },
      "item-8362": {
        "value": 6,
        "weight": 9
      },
      "item-8363": {
        "value": 7,
        "weight": 1
      },
      "item-8364": {
        "value": 3,
        "weight": 9
      },
      "item-8365": {
        "value": 8,
        "weight": 3
      },
      "item-8366": {
        "value": 2,
        "weight": 2
      },
      "item-8367": {
        "value": 9,
        "weight": 9
      },
      "item-8368": {
        "value": 2,
        "weight": 6
      },
      "item-8369": {
        "value": 7,
        "weight": 7
      },
      "item-8370": {
        "value": 2,
        "weight": 8
      },
      "item-8371": {
        "value": 4,
        "weight": 1
      },
      "item-8372": {
        "value": 6,
        "weight": 4
      },
      "item-8373": {
        "value": 9,
        "weight": 2
      },
      "item-8374": {
        "value": 8,
        "weight": 4
      },
      "item-8375": {
        "value": 6,
        "weight": 5
      },
      "item-8376": {
        "value": 7,
        "weight": 1
      },
      "item-8377": {
        "value": 4,
        "weight": 3
      },
      "item-8378": {
        "value": 9,
        "weight": 4
      },
      "item-8379": {
        "value": 4,
        "weight": 7
      },
      "item-8380": {
        "value": 2,
        "weight": 1
      },
      "item-8381": {
        "value": 6,
        "weight": 5
      },
      "item-8382": {
        "value": 2,
        "weight": 7
      },
      "item-8383": {
        "value": 6,
        "weight": 3
      },
      "item-8384": {
        "value": 8,
        "weight": 1
      },
      "item-8385": {
        "value": 6,
        "weight": 9
      },
      "item-8386": {
        "value": 2,
        "weight": 2
      },
      "item-8387": {
        "value": 9,
        "weight": 1
      },
      "item-8388": {
        "value": 5,
        "weight": 1
      },
      "item-8389": {
        "value": 2,
        "weight": 8
      },
      "item-8390": {
        "value": 6,
        "weight": 9
      },
      "item-8391": {
        "value": 1,
        "weight": 9
      },
      "item-8392": {
        "value": 3,
        "weight": 8
      },
      "item-8393": {
        "value": 4,
        "weight": 3
      },
      "item-8394": {
        "value": 4,
        "weight": 2
      },
      "item-8395": {
        "value": 3,
        "weight": 8
      },
      "item-8396": {
        "value": 4,
        "weight": 8
      },
      "item-8397": {
        "value": 9,
        "weight": 7
      },
      "item-8398": {
        "value": 8,
        "weight": 3
      },
      "item-8399": {
        "value": 5,
        "weight": 4
      },
      "item-8400": {
        "value": 2,
        "weight": 4
      },
      "item-8401": {
        "value": 8,
        "weight": 9
      },
      "item-8402": {
        "value": 5,
        "weight": 2
      },
      "item-8403": {
        "value": 5,
        "weight": 5
      },
      "item-8404": {
        "value": 8,
        "weight": 1
      },
      "item-8405": {
        "value": 2,
        "weight": 5
      },
      "item-8406": {
        "value": 3,
        "weight": 4
      },
      "item-8407": {
        "value": 9,
        "weight": 2
      },
      "item-8408": {
        "value": 3,
        "weight": 5
      },
      "item-8409": {
        "value": 2,
        "weight": 9
      },
      "item-8410": {
        "value": 7,
        "weight": 1
      },
      "item-8411": {
        "value": 5,
        "weight": 5
      },
      "item-8412": {
        "value": 2,
        "weight": 8
      },
      "item-8413": {
        "value": 7,
        "weight": 4
      },
      "item-8414": {
        "value": 4,
        "weight": 6
      },
      "item-8415": {
        "value": 8,
        "weight": 5
      },
      "item-8416": {
        "value": 7,
        "weight": 5
      },
      "item-8417": {
        "value": 7,
        "weight": 6
      },
      "item-8418": {
        "value": 3,
        "weight": 3
      },
      "item-8419": {
        "value": 1,
        "weight": 6
      },
      "item-8420": {
        "value": 3,
        "weight": 1
      },
      "item-8421": {
        "value": 8,
        "weight": 6
      },
      "item-8422": {
        "value": 4,
        "weight": 8
      },
      "item-8423": {
        "value": 6,
        "weight": 7
      },
      "item-8424": {
        "value": 3,
        "weight": 9
      },
      "item-8425": {
        "value": 9,
        "weight": 3
      },
      "item-8426": {
        "value": 7,
        "weight": 9
      },
      "item-8427": {
        "value": 7,
        "weight": 5
      },
      "item-8428": {
        "value": 3,
        "weight": 2
      },
      "item-8429": {
        "value": 9,
        "weight": 4
      },
      "item-8430": {
        "value": 4,
        "weight": 3
      },
      "item-8431": {
        "value": 1,
        "weight": 3
      },
      "item-8432": {
        "value": 3,
        "weight": 6
      },
      "item-8433": {
        "value": 2,
        "weight": 3
      },
      "item-8434": {
        "value": 4,
        "weight": 2
      },
      "item-8435": {
        "value": 4,
        "weight": 4
      },
      "item-8436": {
        "value": 9,
        "weight": 7
      },
      "item-8437": {
        "value": 4,
        "weight": 6
      },
      "item-8438": {
        "value": 8,
        "weight": 6
      },
      "item-8439": {
        "value": 3,
        "weight": 9
      },
      "item-8440": {
        "value": 7,
        "weight": 4
      },
      "item-8441": {
        "value": 3,
        "weight": 6
      },
      "item-8442": {
        "value": 5,
        "weight": 4
      },
      "item-8443": {
        "value": 5,
        "weight": 4
      },
      "item-8444": {
        "value": 5,
        "weight": 7
      },
      "item-8445": {
        "value": 2,
        "weight": 5
      },
      "item-8446": {
        "value": 2,
        "weight": 8
      },
      "item-8447": {
        "value": 7,
        "weight": 8
      },
      "item-8448": {
        "value": 8,
        "weight": 5
      },
      "item-8449": {
        "value": 4,
        "weight": 7
      },
      "item-8450": {
        "value": 8,
        "weight": 9
      },
      "item-8451": {
        "value": 1,
        "weight": 9
      },
      "item-8452": {
        "value": 3,
        "weight": 8
      },
      "item-8453": {
        "value": 6,
        "weight": 4
      },
      "item-8454": {
        "value": 5,
        "weight": 1
      },
      "item-8455": {
        "value": 3,
        "weight": 4
      },
      "item-8456": {
        "value": 1,
        "weight": 5
      },
      "item-8457": {
        "value": 4,
        "weight": 2
      },
      "item-8458": {
        "value": 2,
        "weight": 4
      },
      "item-8459": {
        "value": 2,
        "weight": 4
      },
      "item-8460": {
        "value": 7,
        "weight": 3
      },
      "item-8461": {
        "value": 3,
        "weight": 2
      },
      "item-8462": {
        "value": 3,
        "weight": 4
      },
      "item-8463": {
        "value": 2,
        "weight": 6
      },
      "item-8464": {
        "value": 9,
        "weight": 1
      },
      "item-8465": {
        "value": 6,
        "weight": 8
      },
      "item-8466": {
        "value": 3,
        "weight": 5
      },
      "item-8467": {
        "value": 5,
        "weight": 4
      },
      "item-8468": {
        "value": 8,
        "weight": 9
      },
      "item-8469": {
        "value": 3,
        "weight": 5
      },
      "item-8470": {
        "value": 9,
        "weight": 4
      },
      "item-8471": {
        "value": 2,
        "weight": 3
      },
      "item-8472": {
        "value": 7,
        "weight": 9
      },
      "item-8473": {
        "value": 5,
        "weight": 2
      },
      "item-8474": {
        "value": 3,
        "weight": 9
      },
      "item-8475": {
        "value": 7,
        "weight": 3
      },
      "item-8476": {
        "value": 9,
        "weight": 8
      },
      "item-8477": {
        "value": 1,
        "weight": 3
      },
      "item-8478": {
        "value": 7,
        "weight": 9
      },
      "item-8479": {
        "value": 2,
        "weight": 5
      },
      "item-8480": {
        "value": 1,
        "weight": 8
      },
      "item-8481": {
        "value": 3,
        "weight": 6
      },
      "item-8482": {
        "value": 7,
        "weight": 4
      },
      "item-8483": {
        "value": 8,
        "weight": 9
      },
      "item-8484": {
        "value": 5,
        "weight": 2
      },
      "item-8485": {
        "value": 9,
        "weight": 9
      },
      "item-8486": {
        "value": 1,
        "weight": 5
      },
      "item-8487": {
        "value": 2,
        "weight": 3
      },
      "item-8488": {
        "value": 9,
        "weight": 4
      },
      "item-8489": {
        "value": 2,
        "weight": 3
      },
      "item-8490": {
        "value": 2,
        "weight": 4
      },
      "item-8491": {
        "value": 3,
        "weight": 7
      },
      "item-8492": {
        "value": 1,
        "weight": 4
      },
      "item-8493": {
        "value": 2,
        "weight": 1
      },
      "item-8494": {
        "value": 1,
        "weight": 3
      },
      "item-8495": {
        "value": 2,
        "weight": 2
      },
      "item-8496": {
        "value": 9,
        "weight": 7
      },
      "item-8497": {
        "value": 2,
        "weight": 5
      },
      "item-8498": {
        "value": 8,
        "weight": 4
      },
      "item-8499": {
        "value": 1,
        "weight": 4
      },
      "item-8500": {
        "value": 1,
        "weight": 1
      },
      "item-8501": {
        "value": 1,
        "weight": 4
      },
      "item-8502": {
        "value": 5,
        "weight": 8
      },
      "item-8503": {
        "value": 4,
        "weight": 6
      },
      "item-8504": {
        "value": 6,
        "weight": 3
      },
      "item-8505": {
        "value": 4,
        "weight": 1
      },
      "item-8506": {
        "value": 8,
        "weight": 8
      },
      "item-8507": {
        "value": 3,
        "weight": 3
      },
      "item-8508": {
        "value": 2,
        "weight": 8
      },
      "item-8509": {
        "value": 1,
        "weight": 4
      },
      "item-8510": {
        "value": 6,
        "weight": 6
      },
      "item-8511": {
        "value": 1,
        "weight": 9
      },
      "item-8512": {
        "value": 8,
        "weight": 8
      },
      "item-8513": {
        "value": 8,
        "weight": 3
      },
      "item-8514": {
        "value": 6,
        "weight": 6
      },
      "item-8515": {
        "value": 4,
        "weight": 7
      },
      "item-8516": {
        "value": 7,
        "weight": 2
      },
      "item-8517": {
        "value": 7,
        "weight": 7
      },
      "item-8518": {
        "value": 6,
        "weight": 7
      },
      "item-8519": {
        "value": 3,
        "weight": 7
      },
      "item-8520": {
        "value": 4,
        "weight": 4
      },
      "item-8521": {
        "value": 6,
        "weight": 9
      },
      "item-8522": {
        "value": 4,
        "weight": 5
      },
      "item-8523": {
        "value": 4,
        "weight": 8
      },
      "item-8524": {
        "value": 3,
        "weight": 7
      },
      "item-8525": {
        "value": 6,
        "weight": 2
      },
      "item-8526": {
        "value": 2,
        "weight": 4
      },
      "item-8527": {
        "value": 1,
        "weight": 3
      },
      "item-8528": {
        "value": 9,
        "weight": 8
      },
      "item-8529": {
        "value": 6,
        "weight": 2
      },
      "item-8530": {
        "value": 6,
        "weight": 8
      },
      "item-8531": {
        "value": 9,
        "weight": 3
      },
      "item-8532": {
        "value": 3,
        "weight": 5
      },
      "item-8533": {
        "value": 5,
        "weight": 6
      },
      "item-8534": {
        "value": 9,
        "weight": 4
      },
      "item-8535": {
        "value": 5,
        "weight": 6
      },
      "item-8536": {
        "value": 1,
        "weight": 4
      },
      "item-8537": {
        "value": 1,
        "weight": 2
      },
      "item-8538": {
        "value": 3,
        "weight": 8
      },
      "item-8539": {
        "value": 6,
        "weight": 5
      },
      "item-8540": {
        "value": 7,
        "weight": 5
      },
      "item-8541": {
        "value": 4,
        "weight": 5
      },
      "item-8542": {
        "value": 2,
        "weight": 3
      },
      "item-8543": {
        "value": 8,
        "weight": 8
      },
      "item-8544": {
        "value": 2,
        "weight": 5
      },
      "item-8545": {
        "value": 4,
        "weight": 3
      },
      "item-8546": {
        "value": 4,
        "weight": 9
      },
      "item-8547": {
        "value": 8,
        "weight": 3
      },
      "item-8548": {
        "value": 8,
        "weight": 8
      },
      "item-8549": {
        "value": 6,
        "weight": 7
      },
      "item-8550": {
        "value": 6,
        "weight": 6
      },
      "item-8551": {
        "value": 3,
        "weight": 3
      },
      "item-8552": {
        "value": 4,
        "weight": 4
      },
      "item-8553": {
        "value": 6,
        "weight": 3
      },
      "item-8554": {
        "value": 4,
        "weight": 2
      },
      "item-8555": {
        "value": 1,
        "weight": 8
      },
      "item-8556": {
        "value": 3,
        "weight": 7
      },
      "item-8557": {
        "value": 6,
        "weight": 4
      },
      "item-8558": {
        "value": 6,
        "weight": 3
      },
      "item-8559": {
        "value": 4,
        "weight": 8
      },
      "item-8560": {
        "value": 4,
        "weight": 5
      },
      "item-8561": {
        "value": 7,
        "weight": 3
      },
      "item-8562": {
        "value": 9,
        "weight": 9
      },
      "item-8563": {
        "value": 7,
        "weight": 7
      },
      "item-8564": {
        "value": 3,
        "weight": 2
      },
      "item-8565": {
        "value": 6,
        "weight": 3
      },
      "item-8566": {
        "value": 8,
        "weight": 9
      },
      "item-8567": {
        "value": 3,
        "weight": 5
      },
      "item-8568": {
        "value": 7,
        "weight": 7
      },
      "item-8569": {
        "value": 7,
        "weight": 9
      },
      "item-8570": {
        "value": 1,
        "weight": 2
      },
      "item-8571": {
        "value": 6,
        "weight": 2
      },
      "item-8572": {
        "value": 6,
        "weight": 9
      },
      "item-8573": {
        "value": 3,
        "weight": 5
      },
      "item-8574": {
        "value": 7,
        "weight": 2
      },
      "item-8575": {
        "value": 9,
        "weight": 8
      },
      "item-8576": {
        "value": 1,
        "weight": 6
      },
      "item-8577": {
        "value": 3,
        "weight": 8
      },
      "item-8578": {
        "value": 6,
        "weight": 5
      },
      "item-8579": {
        "value": 6,
        "weight": 1
      },
      "item-8580": {
        "value": 8,
        "weight": 5
      },
      "item-8581": {
        "value": 2,
        "weight": 8
      },
      "item-8582": {
        "value": 5,
        "weight": 1
      },
      "item-8583": {
        "value": 2,
        "weight": 7
      },
      "item-8584": {
        "value": 4,
        "weight": 8
      },
      "item-8585": {
        "value": 7,
        "weight": 7
      },
      "item-8586": {
        "value": 4,
        "weight": 7
      },
      "item-8587": {
        "value": 3,
        "weight": 2
      },
      "item-8588": {
        "value": 4,
        "weight": 2
      },
      "item-8589": {
        "value": 1,
        "weight": 7
      },
      "item-8590": {
        "value": 3,
        "weight": 2
      },
      "item-8591": {
        "value": 8,
        "weight": 5
      },
      "item-8592": {
        "value": 9,
        "weight": 2
      },
      "item-8593": {
        "value": 8,
        "weight": 3
      },
      "item-8594": {
        "value": 5,
        "weight": 7
      },
      "item-8595": {
        "value": 4,
        "weight": 4
      },
      "item-8596": {
        "value": 3,
        "weight": 1
      },
      "item-8597": {
        "value": 7,
        "weight": 7
      },
      "item-8598": {
        "value": 4,
        "weight": 7
      },
      "item-8599": {
        "value": 4,
        "weight": 6
      },
      "item-8600": {
        "value": 6,
        "weight": 1
      },
      "item-8601": {
        "value": 7,
        "weight": 9
      },
      "item-8602": {
        "value": 4,
        "weight": 1
      },
      "item-8603": {
        "value": 9,
        "weight": 6
      },
      "item-8604": {
        "value": 8,
        "weight": 2
      },
      "item-8605": {
        "value": 6,
        "weight": 5
      },
      "item-8606": {
        "value": 3,
        "weight": 2
      },
      "item-8607": {
        "value": 1,
        "weight": 7
      },
      "item-8608": {
        "value": 5,
        "weight": 6
      },
      "item-8609": {
        "value": 8,
        "weight": 1
      },
      "item-8610": {
        "value": 8,
        "weight": 1
      },
      "item-8611": {
        "value": 2,
        "weight": 2
      },
      "item-8612": {
        "value": 6,
        "weight": 2
      },
      "item-8613": {
        "value": 7,
        "weight": 3
      },
      "item-8614": {
        "value": 7,
        "weight": 6
      },
      "item-8615": {
        "value": 6,
        "weight": 5
      },
      "item-8616": {
        "value": 6,
        "weight": 2
      },
      "item-8617": {
        "value": 1,
        "weight": 1
      },
      "item-8618": {
        "value": 2,
        "weight": 1
      },
      "item-8619": {
        "value": 6,
        "weight": 9
      },
      "item-8620": {
        "value": 2,
        "weight": 1
      },
      "item-8621": {
        "value": 6,
        "weight": 6
      },
      "item-8622": {
        "value": 4,
        "weight": 5
      },
      "item-8623": {
        "value": 5,
        "weight": 4
      },
      "item-8624": {
        "value": 1,
        "weight": 4
      },
      "item-8625": {
        "value": 2,
        "weight": 2
      },
      "item-8626": {
        "value": 1,
        "weight": 9
      },
      "item-8627": {
        "value": 9,
        "weight": 5
      },
      "item-8628": {
        "value": 1,
        "weight": 4
      },
      "item-8629": {
        "value": 8,
        "weight": 2
      },
      "item-8630": {
        "value": 5,
        "weight": 6
      },
      "item-8631": {
        "value": 8,
        "weight": 4
      },
      "item-8632": {
        "value": 8,
        "weight": 1
      },
      "item-8633": {
        "value": 1,
        "weight": 8
      },
      "item-8634": {
        "value": 4,
        "weight": 1
      },
      "item-8635": {
        "value": 8,
        "weight": 1
      },
      "item-8636": {
        "value": 9,
        "weight": 7
      },
      "item-8637": {
        "value": 4,
        "weight": 2
      },
      "item-8638": {
        "value": 4,
        "weight": 1
      },
      "item-8639": {
        "value": 8,
        "weight": 7
      },
      "item-8640": {
        "value": 7,
        "weight": 8
      },
      "item-8641": {
        "value": 4,
        "weight": 2
      },
      "item-8642": {
        "value": 4,
        "weight": 3
      },
      "item-8643": {
        "value": 7,
        "weight": 6
      },
      "item-8644": {
        "value": 9,
        "weight": 8
      },
      "item-8645": {
        "value": 9,
        "weight": 7
      },
      "item-8646": {
        "value": 5,
        "weight": 7
      },
      "item-8647": {
        "value": 4,
        "weight": 7
      },
      "item-8648": {
        "value": 7,
        "weight": 4
      },
      "item-8649": {
        "value": 9,
        "weight": 6
      },
      "item-8650": {
        "value": 9,
        "weight": 8
      },
      "item-8651": {
        "value": 6,
        "weight": 8
      },
      "item-8652": {
        "value": 2,
        "weight": 6
      },
      "item-8653": {
        "value": 7,
        "weight": 8
      },
      "item-8654": {
        "value": 9,
        "weight": 6
      },
      "item-8655": {
        "value": 9,
        "weight": 9
      },
      "item-8656": {
        "value": 3,
        "weight": 2
      },
      "item-8657": {
        "value": 5,
        "weight": 8
      },
      "item-8658": {
        "value": 1,
        "weight": 7
      },
      "item-8659": {
        "value": 4,
        "weight": 7
      },
      "item-8660": {
        "value": 5,
        "weight": 8
      },
      "item-8661": {
        "value": 1,
        "weight": 8
      },
      "item-8662": {
        "value": 7,
        "weight": 6
      },
      "item-8663": {
        "value": 7,
        "weight": 1
      },
      "item-8664": {
        "value": 6,
        "weight": 3
      },
      "item-8665": {
        "value": 1,
        "weight": 2
      },
      "item-8666": {
        "value": 3,
        "weight": 9
      },
      "item-8667": {
        "value": 6,
        "weight": 1
      },
      "item-8668": {
        "value": 2,
        "weight": 4
      },
      "item-8669": {
        "value": 1,
        "weight": 6
      },
      "item-8670": {
        "value": 2,
        "weight": 6
      },
      "item-8671": {
        "value": 4,
        "weight": 9
      },
      "item-8672": {
        "value": 5,
        "weight": 2
      },
      "item-8673": {
        "value": 5,
        "weight": 2
      },
      "item-8674": {
        "value": 2,
        "weight": 1
      },
      "item-8675": {
        "value": 1,
        "weight": 6
      },
      "item-8676": {
        "value": 7,
        "weight": 7
      },
      "item-8677": {
        "value": 2,
        "weight": 6
      },
      "item-8678": {
        "value": 6,
        "weight": 4
      },
      "item-8679": {
        "value": 6,
        "weight": 7
      },
      "item-8680": {
        "value": 2,
        "weight": 3
      },
      "item-8681": {
        "value": 3,
        "weight": 3
      },
      "item-8682": {
        "value": 2,
        "weight": 4
      },
      "item-8683": {
        "value": 6,
        "weight": 8
      },
      "item-8684": {
        "value": 3,
        "weight": 7
      },
      "item-8685": {
        "value": 3,
        "weight": 7
      },
      "item-8686": {
        "value": 4,
        "weight": 4
      },
      "item-8687": {
        "value": 4,
        "weight": 6
      },
      "item-8688": {
        "value": 4,
        "weight": 4
      },
      "item-8689": {
        "value": 9,
        "weight": 7
      },
      "item-8690": {
        "value": 6,
        "weight": 6
      },
      "item-8691": {
        "value": 1,
        "weight": 9
      },
      "item-8692": {
        "value": 3,
        "weight": 7
      },
      "item-8693": {
        "value": 6,
        "weight": 6
      },
      "item-8694": {
        "value": 1,
        "weight": 8
      },
      "item-8695": {
        "value": 3,
        "weight": 6
      },
      "item-8696": {
        "value": 1,
        "weight": 2
      },
      "item-8697": {
        "value": 6,
        "weight": 6
      },
      "item-8698": {
        "value": 9,
        "weight": 9
      },
      "item-8699": {
        "value": 2,
        "weight": 2
      },
      "item-8700": {
        "value": 4,
        "weight": 2
      },
      "item-8701": {
        "value": 5,
        "weight": 3
      },
      "item-8702": {
        "value": 3,
        "weight": 9
      },
      "item-8703": {
        "value": 6,
        "weight": 3
      },
      "item-8704": {
        "value": 6,
        "weight": 2
      },
      "item-8705": {
        "value": 2,
        "weight": 2
      },
      "item-8706": {
        "value": 7,
        "weight": 3
      },
      "item-8707": {
        "value": 6,
        "weight": 4
      },
      "item-8708": {
        "value": 9,
        "weight": 5
      },
      "item-8709": {
        "value": 9,
        "weight": 5
      },
      "item-8710": {
        "value": 7,
        "weight": 1
      },
      "item-8711": {
        "value": 5,
        "weight": 6
      },
      "item-8712": {
        "value": 2,
        "weight": 5
      },
      "item-8713": {
        "value": 8,
        "weight": 3
      },
      "item-8714": {
        "value": 8,
        "weight": 9
      },
      "item-8715": {
        "value": 1,
        "weight": 9
      },
      "item-8716": {
        "value": 7,
        "weight": 1
      },
      "item-8717": {
        "value": 2,
        "weight": 6
      },
      "item-8718": {
        "value": 1,
        "weight": 2
      },
      "item-8719": {
        "value": 3,
        "weight": 5
      },
      "item-8720": {
        "value": 4,
        "weight": 4
      },
      "item-8721": {
        "value": 3,
        "weight": 6
      },
      "item-8722": {
        "value": 8,
        "weight": 6
      },
      "item-8723": {
        "value": 3,
        "weight": 2
      },
      "item-8724": {
        "value": 1,
        "weight": 5
      },
      "item-8725": {
        "value": 3,
        "weight": 8
      },
      "item-8726": {
        "value": 4,
        "weight": 6
      },
      "item-8727": {
        "value": 7,
        "weight": 1
      },
      "item-8728": {
        "value": 3,
        "weight": 8
      },
      "item-8729": {
        "value": 8,
        "weight": 9
      },
      "item-8730": {
        "value": 6,
        "weight": 3
      },
      "item-8731": {
        "value": 6,
        "weight": 9
      },
      "item-8732": {
        "value": 3,
        "weight": 6
      },
      "item-8733": {
        "value": 5,
        "weight": 9
      },
      "item-8734": {
        "value": 9,
        "weight": 9
      },
      "item-8735": {
        "value": 2,
        "weight": 1
      },
      "item-8736": {
        "value": 7,
        "weight": 9
      },
      "item-8737": {
        "value": 3,
        "weight": 9
      },
      "item-8738": {
        "value": 2,
        "weight": 2
      },
      "item-8739": {
        "value": 9,
        "weight": 6
      },
      "item-8740": {
        "value": 9,
        "weight": 4
      },
      "item-8741": {
        "value": 2,
        "weight": 7
      },
      "item-8742": {
        "value": 3,
        "weight": 9
      },
      "item-8743": {
        "value": 3,
        "weight": 4
      },
      "item-8744": {
        "value": 8,
        "weight": 2
      },
      "item-8745": {
        "value": 6,
        "weight": 6
      },
      "item-8746": {
        "value": 9,
        "weight": 8
      },
      "item-8747": {
        "value": 7,
        "weight": 2
      },
      "item-8748": {
        "value": 7,
        "weight": 1
      },
      "item-8749": {
        "value": 8,
        "weight": 5
      },
      "item-8750": {
        "value": 4,
        "weight": 2
      },
      "item-8751": {
        "value": 7,
        "weight": 3
      },
      "item-8752": {
        "value": 2,
        "weight": 8
      },
      "item-8753": {
        "value": 6,
        "weight": 4
      },
      "item-8754": {
        "value": 1,
        "weight": 3
      },
      "item-8755": {
        "value": 1,
        "weight": 6
      },
      "item-8756": {
        "value": 4,
        "weight": 9
      },
      "item-8757": {
        "value": 5,
        "weight": 9
      },
      "item-8758": {
        "value": 3,
        "weight": 8
      },
      "item-8759": {
        "value": 5,
        "weight": 9
      },
      "item-8760": {
        "value": 9,
        "weight": 9
      },
      "item-8761": {
        "value": 2,
        "weight": 2
      },
      "item-8762": {
        "value": 8,
        "weight": 4
      },
      "item-8763": {
        "value": 6,
        "weight": 5
      },
      "item-8764": {
        "value": 5,
        "weight": 9
      },
      "item-8765": {
        "value": 9,
        "weight": 7
      },
      "item-8766": {
        "value": 4,
        "weight": 4
      },
      "item-8767": {
        "value": 3,
        "weight": 5
      },
      "item-8768": {
        "value": 6,
        "weight": 3
      },
      "item-8769": {
        "value": 8,
        "weight": 3
      },
      "item-8770": {
        "value": 8,
        "weight": 5
      },
      "item-8771": {
        "value": 8,
        "weight": 1
      },
      "item-8772": {
        "value": 8,
        "weight": 4
      },
      "item-8773": {
        "value": 7,
        "weight": 6
      },
      "item-8774": {
        "value": 7,
        "weight": 2
      },
      "item-8775": {
        "value": 5,
        "weight": 5
      },
      "item-8776": {
        "value": 7,
        "weight": 6
      },
      "item-8777": {
        "value": 2,
        "weight": 1
      },
      "item-8778": {
        "value": 5,
        "weight": 2
      },
      "item-8779": {
        "value": 1,
        "weight": 3
      },
      "item-8780": {
        "value": 1,
        "weight": 6
      },
      "item-8781": {
        "value": 2,
        "weight": 3
      },
      "item-8782": {
        "value": 2,
        "weight": 7
      },
      "item-8783": {
        "value": 4,
        "weight": 8
      },
      "item-8784": {
        "value": 5,
        "weight": 8
      },
      "item-8785": {
        "value": 2,
        "weight": 4
      },
      "item-8786": {
        "value": 1,
        "weight": 1
      },
      "item-8787": {
        "value": 8,
        "weight": 5
      },
      "item-8788": {
        "value": 5,
        "weight": 4
      },
      "item-8789": {
        "value": 3,
        "weight": 2
      },
      "item-8790": {
        "value": 9,
        "weight": 2
      },
      "item-8791": {
        "value": 8,
        "weight": 2
      },
      "item-8792": {
        "value": 9,
        "weight": 3
      },
      "item-8793": {
        "value": 7,
        "weight": 3
      },
      "item-8794": {
        "value": 1,
        "weight": 5
      },
      "item-8795": {
        "value": 3,
        "weight": 9
      },
      "item-8796": {
        "value": 3,
        "weight": 6
      },
      "item-8797": {
        "value": 2,
        "weight": 7
      },
      "item-8798": {
        "value": 9,
        "weight": 7
      },
      "item-8799": {
        "value": 2,
        "weight": 1
      },
      "item-8800": {
        "value": 2,
        "weight": 3
      },
      "item-8801": {
        "value": 2,
        "weight": 8
      },
      "item-8802": {
        "value": 6,
        "weight": 7
      },
      "item-8803": {
        "value": 7,
        "weight": 6
      },
      "item-8804": {
        "value": 6,
        "weight": 2
      },
      "item-8805": {
        "value": 4,
        "weight": 6
      },
      "item-8806": {
        "value": 5,
        "weight": 2
      },
      "item-8807": {
        "value": 3,
        "weight": 9
      },
      "item-8808": {
        "value": 7,
        "weight": 9
      },
      "item-8809": {
        "value": 1,
        "weight": 9
      },
      "item-8810": {
        "value": 9,
        "weight": 8
      },
      "item-8811": {
        "value": 6,
        "weight": 9
      },
      "item-8812": {
        "value": 3,
        "weight": 4
      },
      "item-8813": {
        "value": 3,
        "weight": 9
      },
      "item-8814": {
        "value": 4,
        "weight": 1
      },
      "item-8815": {
        "value": 2,
        "weight": 7
      },
      "item-8816": {
        "value": 1,
        "weight": 3
      },
      "item-8817": {
        "value": 6,
        "weight": 5
      },
      "item-8818": {
        "value": 7,
        "weight": 9
      },
      "item-8819": {
        "value": 8,
        "weight": 9
      },
      "item-8820": {
        "value": 3,
        "weight": 6
      },
      "item-8821": {
        "value": 2,
        "weight": 3
      },
      "item-8822": {
        "value": 7,
        "weight": 6
      },
      "item-8823": {
        "value": 6,
        "weight": 9
      },
      "item-8824": {
        "value": 9,
        "weight": 4
      },
      "item-8825": {
        "value": 2,
        "weight": 1
      },
      "item-8826": {
        "value": 3,
        "weight": 8
      },
      "item-8827": {
        "value": 7,
        "weight": 4
      },
      "item-8828": {
        "value": 7,
        "weight": 7
      },
      "item-8829": {
        "value": 8,
        "weight": 1
      },
      "item-8830": {
        "value": 3,
        "weight": 7
      },
      "item-8831": {
        "value": 4,
        "weight": 8
      },
      "item-8832": {
        "value": 1,
        "weight": 7
      },
      "item-8833": {
        "value": 4,
        "weight": 3
      },
      "item-8834": {
        "value": 4,
        "weight": 1
      },
      "item-8835": {
        "value": 5,
        "weight": 5
      },
      "item-8836": {
        "value": 9,
        "weight": 6
      },
      "item-8837": {
        "value": 1,
        "weight": 2
      },
      "item-8838": {
        "value": 6,
        "weight": 3
      },
      "item-8839": {
        "value": 1,
        "weight": 5
      },
      "item-8840": {
        "value": 2,
        "weight": 9
      },
      "item-8841": {
        "value": 1,
        "weight": 5
      },
      "item-8842": {
        "value": 1,
        "weight": 4
      },
      "item-8843": {
        "value": 8,
        "weight": 1
      },
      "item-8844": {
        "value": 2,
        "weight": 2
      },
      "item-8845": {
        "value": 2,
        "weight": 8
      },
      "item-8846": {
        "value": 9,
        "weight": 8
      },
      "item-8847": {
        "value": 6,
        "weight": 3
      },
      "item-8848": {
        "value": 8,
        "weight": 5
      },
      "item-8849": {
        "value": 6,
        "weight": 6
      },
      "item-8850": {
        "value": 2,
        "weight": 9
      },
      "item-8851": {
        "value": 9,
        "weight": 9
      },
      "item-8852": {
        "value": 3,
        "weight": 4
      },
      "item-8853": {
        "value": 2,
        "weight": 1
      },
      "item-8854": {
        "value": 3,
        "weight": 4
      },
      "item-8855": {
        "value": 5,
        "weight": 6
      },
      "item-8856": {
        "value": 6,
        "weight": 2
      },
      "item-8857": {
        "value": 3,
        "weight": 3
      },
      "item-8858": {
        "value": 1,
        "weight": 9
      },
      "item-8859": {
        "value": 9,
        "weight": 6
      },
      "item-8860": {
        "value": 9,
        "weight": 7
      },
      "item-8861": {
        "value": 2,
        "weight": 6
      },
      "item-8862": {
        "value": 1,
        "weight": 3
      },
      "item-8863": {
        "value": 7,
        "weight": 6
      },
      "item-8864": {
        "value": 1,
        "weight": 6
      },
      "item-8865": {
        "value": 4,
        "weight": 3
      },
      "item-8866": {
        "value": 3,
        "weight": 1
      },
      "item-8867": {
        "value": 4,
        "weight": 3
      },
      "item-8868": {
        "value": 6,
        "weight": 4
      },
      "item-8869": {
        "value": 1,
        "weight": 6
      },
      "item-8870": {
        "value": 6,
        "weight": 3
      },
      "item-8871": {
        "value": 7,
        "weight": 5
      },
      "item-8872": {
        "value": 5,
        "weight": 7
      },
      "item-8873": {
        "value": 7,
        "weight": 5
      },
      "item-8874": {
        "value": 7,
        "weight": 5
      },
      "item-8875": {
        "value": 8,
        "weight": 9
      },
      "item-8876": {
        "value": 6,
        "weight": 4
      },
      "item-8877": {
        "value": 7,
        "weight": 4
      },
      "item-8878": {
        "value": 3,
        "weight": 3
      },
      "item-8879": {
        "value": 1,
        "weight": 7
      },
      "item-8880": {
        "value": 9,
        "weight": 2
      },
      "item-8881": {
        "value": 4,
        "weight": 1
      },
      "item-8882": {
        "value": 7,
        "weight": 7
      },
      "item-8883": {
        "value": 2,
        "weight": 3
      },
      "item-8884": {
        "value": 6,
        "weight": 9
      },
      "item-8885": {
        "value": 5,
        "weight": 9
      },
      "item-8886": {
        "value": 3,
        "weight": 5
      },
      "item-8887": {
        "value": 8,
        "weight": 1
      },
      "item-8888": {
        "value": 7,
        "weight": 9
      },
      "item-8889": {
        "value": 9,
        "weight": 4
      },
      "item-8890": {
        "value": 6,
        "weight": 8
      },
      "item-8891": {
        "value": 7,
        "weight": 2
      },
      "item-8892": {
        "value": 5,
        "weight": 1
      },
      "item-8893": {
        "value": 7,
        "weight": 8
      },
      "item-8894": {
        "value": 4,
        "weight": 7
      },
      "item-8895": {
        "value": 8,
        "weight": 2
      },
      "item-8896": {
        "value": 9,
        "weight": 7
      },
      "item-8897": {
        "value": 9,
        "weight": 3
      },
      "item-8898": {
        "value": 8,
        "weight": 9
      },
      "item-8899": {
        "value": 1,
        "weight": 6
      },
      "item-8900": {
        "value": 5,
        "weight": 7
      },
      "item-8901": {
        "value": 8,
        "weight": 5
      },
      "item-8902": {
        "value": 6,
        "weight": 8
      },
      "item-8903": {
        "value": 2,
        "weight": 4
      },
      "item-8904": {
        "value": 7,
        "weight": 5
      },
      "item-8905": {
        "value": 7,
        "weight": 3
      },
      "item-8906": {
        "value": 8,
        "weight": 2
      },
      "item-8907": {
        "value": 7,
        "weight": 7
      },
      "item-8908": {
        "value": 9,
        "weight": 3
      },
      "item-8909": {
        "value": 1,
        "weight": 6
      },
      "item-8910": {
        "value": 5,
        "weight": 5
      },
      "item-8911": {
        "value": 1,
        "weight": 4
      },
      "item-8912": {
        "value": 5,
        "weight": 2
      },
      "item-8913": {
        "value": 1,
        "weight": 9
      },
      "item-8914": {
        "value": 9,
        "weight": 1
      },
      "item-8915": {
        "value": 1,
        "weight": 7
      },
      "item-8916": {
        "value": 8,
        "weight": 9
      },
      "item-8917": {
        "value": 8,
        "weight": 5
      },
      "item-8918": {
        "value": 1,
        "weight": 1
      },
      "item-8919": {
        "value": 6,
        "weight": 9
      },
      "item-8920": {
        "value": 5,
        "weight": 3
      },
      "item-8921": {
        "value": 5,
        "weight": 6
      },
      "item-8922": {
        "value": 6,
        "weight": 1
      },
      "item-8923": {
        "value": 4,
        "weight": 9
      },
      "item-8924": {
        "value": 7,
        "weight": 2
      },
      "item-8925": {
        "value": 8,
        "weight": 4
      },
      "item-8926": {
        "value": 5,
        "weight": 3
      },
      "item-8927": {
        "value": 5,
        "weight": 7
      },
      "item-8928": {
        "value": 1,
        "weight": 6
      },
      "item-8929": {
        "value": 9,
        "weight": 1
      },
      "item-8930": {
        "value": 1,
        "weight": 9
      },
      "item-8931": {
        "value": 3,
        "weight": 2
      },
      "item-8932": {
        "value": 9,
        "weight": 1
      },
      "item-8933": {
        "value": 7,
        "weight": 3
      },
      "item-8934": {
        "value": 6,
        "weight": 9
      },
      "item-8935": {
        "value": 9,
        "weight": 1
      },
      "item-8936": {
        "value": 9,
        "weight": 3
      },
      "item-8937": {
        "value": 6,
        "weight": 2
      },
      "item-8938": {
        "value": 9,
        "weight": 7
      },
      "item-8939": {
        "value": 2,
        "weight": 7
      },
      "item-8940": {
        "value": 5,
        "weight": 6
      },
      "item-8941": {
        "value": 4,
        "weight": 9
      },
      "item-8942": {
        "value": 8,
        "weight": 4
      },
      "item-8943": {
        "value": 2,
        "weight": 2
      },
      "item-8944": {
        "value": 6,
        "weight": 1
      },
      "item-8945": {
        "value": 8,
        "weight": 5
      },
      "item-8946": {
        "value": 3,
        "weight": 7
      },
      "item-8947": {
        "value": 3,
        "weight": 8
      },
      "item-8948": {
        "value": 4,
        "weight": 9
      },
      "item-8949": {
        "value": 4,
        "weight": 4
      },
      "item-8950": {
        "value": 4,
        "weight": 2
      },
      "item-8951": {
        "value": 7,
        "weight": 3
      },
      "item-8952": {
        "value": 6,
        "weight": 7
      },
      "item-8953": {
        "value": 8,
        "weight": 9
      },
      "item-8954": {
        "value": 6,
        "weight": 5
      },
      "item-8955": {
        "value": 1,
        "weight": 8
      },
      "item-8956": {
        "value": 4,
        "weight": 3
      },
      "item-8957": {
        "value": 6,
        "weight": 6
      },
      "item-8958": {
        "value": 6,
        "weight": 9
      },
      "item-8959": {
        "value": 8,
        "weight": 3
      },
      "item-8960": {
        "value": 9,
        "weight": 9
      },
      "item-8961": {
        "value": 3,
        "weight": 2
      },
      "item-8962": {
        "value": 7,
        "weight": 2
      },
      "item-8963": {
        "value": 4,
        "weight": 3
      },
      "item-8964": {
        "value": 4,
        "weight": 4
      },
      "item-8965": {
        "value": 1,
        "weight": 8
      },
      "item-8966": {
        "value": 1,
        "weight": 7
      },
      "item-8967": {
        "value": 1,
        "weight": 4
      },
      "item-8968": {
        "value": 8,
        "weight": 8
      },
      "item-8969": {
        "value": 7,
        "weight": 5
      },
      "item-8970": {
        "value": 9,
        "weight": 4
      },
      "item-8971": {
        "value": 3,
        "weight": 4
      },
      "item-8972": {
        "value": 5,
        "weight": 8
      },
      "item-8973": {
        "value": 8,
        "weight": 1
      },
      "item-8974": {
        "value": 1,
        "weight": 7
      },
      "item-8975": {
        "value": 3,
        "weight": 3
      },
      "item-8976": {
        "value": 3,
        "weight": 7
      },
      "item-8977": {
        "value": 9,
        "weight": 2
      },
      "item-8978": {
        "value": 4,
        "weight": 9
      },
      "item-8979": {
        "value": 2,
        "weight": 9
      },
      "item-8980": {
        "value": 6,
        "weight": 7
      },
      "item-8981": {
        "value": 2,
        "weight": 7
      },
      "item-8982": {
        "value": 4,
        "weight": 4
      },
      "item-8983": {
        "value": 4,
        "weight": 4
      },
      "item-8984": {
        "value": 5,
        "weight": 9
      },
      "item-8985": {
        "value": 3,
        "weight": 7
      },
      "item-8986": {
        "value": 1,
        "weight": 1
      },
      "item-8987": {
        "value": 3,
        "weight": 2
      },
      "item-8988": {
        "value": 5,
        "weight": 6
      },
      "item-8989": {
        "value": 6,
        "weight": 6
      },
      "item-8990": {
        "value": 5,
        "weight": 5
      },
      "item-8991": {
        "value": 8,
        "weight": 2
      },
      "item-8992": {
        "value": 9,
        "weight": 3
      },
      "item-8993": {
        "value": 4,
        "weight": 7
      },
      "item-8994": {
        "value": 9,
        "weight": 7
      },
      "item-8995": {
        "value": 5,
        "weight": 2
      },
      "item-8996": {
        "value": 8,
        "weight": 1
      },
      "item-8997": {
        "value": 7,
        "weight": 9
      },
      "item-8998": {
        "value": 5,
        "weight": 6
      },
      "item-8999": {
        "value": 6,
        "weight": 3
      },
      "item-9000": {
        "value": 7,
        "weight": 8
      },
      "item-9001": {
        "value": 9,
        "weight": 2
      },
      "item-9002": {
        "value": 8,
        "weight": 7
      },
      "item-9003": {
        "value": 3,
        "weight": 2
      },
      "item-9004": {
        "value": 2,
        "weight": 8
      },
      "item-9005": {
        "value": 3,
        "weight": 3
      },
      "item-9006": {
        "value": 4,
        "weight": 1
      },
      "item-9007": {
        "value": 8,
        "weight": 3
      },
      "item-9008": {
        "value": 3,
        "weight": 5
      },
      "item-9009": {
        "value": 6,
        "weight": 8
      },
      "item-9010": {
        "value": 2,
        "weight": 6
      },
      "item-9011": {
        "value": 8,
        "weight": 3
      },
      "item-9012": {
        "value": 7,
        "weight": 2
      },
      "item-9013": {
        "value": 3,
        "weight": 9
      },
      "item-9014": {
        "value": 1,
        "weight": 6
      },
      "item-9015": {
        "value": 1,
        "weight": 8
      },
      "item-9016": {
        "value": 9,
        "weight": 8
      },
      "item-9017": {
        "value": 4,
        "weight": 7
      },
      "item-9018": {
        "value": 4,
        "weight": 3
      },
      "item-9019": {
        "value": 7,
        "weight": 6
      },
      "item-9020": {
        "value": 5,
        "weight": 5
      },
      "item-9021": {
        "value": 4,
        "weight": 4
      },
      "item-9022": {
        "value": 1,
        "weight": 1
      },
      "item-9023": {
        "value": 2,
        "weight": 6
      },
      "item-9024": {
        "value": 6,
        "weight": 5
      },
      "item-9025": {
        "value": 7,
        "weight": 7
      },
      "item-9026": {
        "value": 3,
        "weight": 8
      },
      "item-9027": {
        "value": 5,
        "weight": 4
      },
      "item-9028": {
        "value": 3,
        "weight": 6
      },
      "item-9029": {
        "value": 8,
        "weight": 5
      },
      "item-9030": {
        "value": 2,
        "weight": 4
      },
      "item-9031": {
        "value": 4,
        "weight": 2
      },
      "item-9032": {
        "value": 4,
        "weight": 8
      },
      "item-9033": {
        "value": 3,
        "weight": 5
      },
      "item-9034": {
        "value": 9,
        "weight": 9
      },
      "item-9035": {
        "value": 6,
        "weight": 6
      },
      "item-9036": {
        "value": 9,
        "weight": 1
      },
      "item-9037": {
        "value": 4,
        "weight": 1
      },
      "item-9038": {
        "value": 5,
        "weight": 6
      },
      "item-9039": {
        "value": 2,
        "weight": 3
      },
      "item-9040": {
        "value": 3,
        "weight": 8
      },
      "item-9041": {
        "value": 7,
        "weight": 4
      },
      "item-9042": {
        "value": 9,
        "weight": 8
      },
      "item-9043": {
        "value": 4,
        "weight": 1
      },
      "item-9044": {
        "value": 1,
        "weight": 8
      },
      "item-9045": {
        "value": 2,
        "weight": 3
      },
      "item-9046": {
        "value": 6,
        "weight": 9
      },
      "item-9047": {
        "value": 1,
        "weight": 3
      },
      "item-9048": {
        "value": 7,
        "weight": 8
      },
      "item-9049": {
        "value": 1,
        "weight": 4
      },
      "item-9050": {
        "value": 2,
        "weight": 1
      },
      "item-9051": {
        "value": 5,
        "weight": 3
      },
      "item-9052": {
        "value": 8,
        "weight": 4
      },
      "item-9053": {
        "value": 8,
        "weight": 2
      },
      "item-9054": {
        "value": 6,
        "weight": 9
      },
      "item-9055": {
        "value": 3,
        "weight": 2
      },
      "item-9056": {
        "value": 5,
        "weight": 8
      },
      "item-9057": {
        "value": 5,
        "weight": 4
      },
      "item-9058": {
        "value": 8,
        "weight": 4
      },
      "item-9059": {
        "value": 7,
        "weight": 9
      },
      "item-9060": {
        "value": 4,
        "weight": 7
      },
      "item-9061": {
        "value": 9,
        "weight": 6
      },
      "item-9062": {
        "value": 6,
        "weight": 9
      },
      "item-9063": {
        "value": 2,
        "weight": 3
      },
      "item-9064": {
        "value": 9,
        "weight": 9
      },
      "item-9065": {
        "value": 9,
        "weight": 7
      },
      "item-9066": {
        "value": 9,
        "weight": 7
      },
      "item-9067": {
        "value": 6,
        "weight": 1
      },
      "item-9068": {
        "value": 2,
        "weight": 2
      },
      "item-9069": {
        "value": 9,
        "weight": 5
      },
      "item-9070": {
        "value": 7,
        "weight": 1
      },
      "item-9071": {
        "value": 3,
        "weight": 6
      },
      "item-9072": {
        "value": 2,
        "weight": 9
      },
      "item-9073": {
        "value": 8,
        "weight": 3
      },
      "item-9074": {
        "value": 5,
        "weight": 7
      },
      "item-9075": {
        "value": 1,
        "weight": 2
      },
      "item-9076": {
        "value": 3,
        "weight": 1
      },
      "item-9077": {
        "value": 9,
        "weight": 9
      },
      "item-9078": {
        "value": 1,
        "weight": 9
      },
      "item-9079": {
        "value": 1,
        "weight": 3
      },
      "item-9080": {
        "value": 1,
        "weight": 8
      },
      "item-9081": {
        "value": 5,
        "weight": 1
      },
      "item-9082": {
        "value": 1,
        "weight": 3
      },
      "item-9083": {
        "value": 6,
        "weight": 1
      },
      "item-9084": {
        "value": 6,
        "weight": 8
      },
      "item-9085": {
        "value": 5,
        "weight": 4
      },
      "item-9086": {
        "value": 7,
        "weight": 7
      },
      "item-9087": {
        "value": 3,
        "weight": 5
      },
      "item-9088": {
        "value": 6,
        "weight": 8
      },
      "item-9089": {
        "value": 6,
        "weight": 1
      },
      "item-9090": {
        "value": 3,
        "weight": 2
      },
      "item-9091": {
        "value": 3,
        "weight": 6
      },
      "item-9092": {
        "value": 8,
        "weight": 4
      },
      "item-9093": {
        "value": 3,
        "weight": 9
      },
      "item-9094": {
        "value": 1,
        "weight": 1
      },
      "item-9095": {
        "value": 6,
        "weight": 7
      },
      "item-9096": {
        "value": 3,
        "weight": 8
      },
      "item-9097": {
        "value": 9,
        "weight": 1
      },
      "item-9098": {
        "value": 9,
        "weight": 9
      },
      "item-9099": {
        "value": 4,
        "weight": 9
      },
      "item-9100": {
        "value": 1,
        "weight": 4
      },
      "item-9101": {
        "value": 9,
        "weight": 3
      },
      "item-9102": {
        "value": 5,
        "weight": 5
      },
      "item-9103": {
        "value": 2,
        "weight": 4
      },
      "item-9104": {
        "value": 6,
        "weight": 5
      },
      "item-9105": {
        "value": 8,
        "weight": 9
      },
      "item-9106": {
        "value": 4,
        "weight": 8
      },
      "item-9107": {
        "value": 7,
        "weight": 8
      },
      "item-9108": {
        "value": 6,
        "weight": 1
      },
      "item-9109": {
        "value": 9,
        "weight": 4
      },
      "item-9110": {
        "value": 6,
        "weight": 8
      },
      "item-9111": {
        "value": 1,
        "weight": 2
      },
      "item-9112": {
        "value": 6,
        "weight": 6
      },
      "item-9113": {
        "value": 3,
        "weight": 8
      },
      "item-9114": {
        "value": 3,
        "weight": 7
      },
      "item-9115": {
        "value": 2,
        "weight": 6
      },
      "item-9116": {
        "value": 1,
        "weight": 5
      },
      "item-9117": {
        "value": 2,
        "weight": 8
      },
      "item-9118": {
        "value": 1,
        "weight": 7
      },
      "item-9119": {
        "value": 2,
        "weight": 9
      },
      "item-9120": {
        "value": 2,
        "weight": 6
      },
      "item-9121": {
        "value": 5,
        "weight": 2
      },
      "item-9122": {
        "value": 1,
        "weight": 9
      },
      "item-9123": {
        "value": 5,
        "weight": 8
      },
      "item-9124": {
        "value": 4,
        "weight": 1
      },
      "item-9125": {
        "value": 2,
        "weight": 2
      },
      "item-9126": {
        "value": 7,
        "weight": 6
      },
      "item-9127": {
        "value": 4,
        "weight": 9
      },
      "item-9128": {
        "value": 3,
        "weight": 1
      },
      "item-9129": {
        "value": 3,
        "weight": 5
      },
      "item-9130": {
        "value": 1,
        "weight": 3
      },
      "item-9131": {
        "value": 8,
        "weight": 8
      },
      "item-9132": {
        "value": 9,
        "weight": 2
      },
      "item-9133": {
        "value": 3,
        "weight": 2
      },
      "item-9134": {
        "value": 3,
        "weight": 8
      },
      "item-9135": {
        "value": 6,
        "weight": 9
      },
      "item-9136": {
        "value": 1,
        "weight": 5
      },
      "item-9137": {
        "value": 1,
        "weight": 1
      },
      "item-9138": {
        "value": 8,
        "weight": 5
      },
      "item-9139": {
        "value": 9,
        "weight": 5
      },
      "item-9140": {
        "value": 1,
        "weight": 3
      },
      "item-9141": {
        "value": 4,
        "weight": 2
      },
      "item-9142": {
        "value": 8,
        "weight": 2
      },
      "item-9143": {
        "value": 7,
        "weight": 5
      },
      "item-9144": {
        "value": 4,
        "weight": 2
      },
      "item-9145": {
        "value": 9,
        "weight": 3
      },
      "item-9146": {
        "value": 6,
        "weight": 2
      },
      "item-9147": {
        "value": 7,
        "weight": 7
      },
      "item-9148": {
        "value": 9,
        "weight": 1
      },
      "item-9149": {
        "value": 9,
        "weight": 9
      },
      "item-9150": {
        "value": 3,
        "weight": 6
      },
      "item-9151": {
        "value": 6,
        "weight": 8
      },
      "item-9152": {
        "value": 3,
        "weight": 4
      },
      "item-9153": {
        "value": 8,
        "weight": 6
      },
      "item-9154": {
        "value": 5,
        "weight": 3
      },
      "item-9155": {
        "value": 1,
        "weight": 3
      },
      "item-9156": {
        "value": 7,
        "weight": 7
      },
      "item-9157": {
        "value": 8,
        "weight": 7
      },
      "item-9158": {
        "value": 5,
        "weight": 3
      },
      "item-9159": {
        "value": 2,
        "weight": 8
      },
      "item-9160": {
        "value": 9,
        "weight": 3
      },
      "item-9161": {
        "value": 8,
        "weight": 7
      },
      "item-9162": {
        "value": 3,
        "weight": 6
      },
      "item-9163": {
        "value": 4,
        "weight": 5
      },
      "item-9164": {
        "value": 5,
        "weight": 3
      },
      "item-9165": {
        "value": 4,
        "weight": 7
      },
      "item-9166": {
        "value": 7,
        "weight": 5
      },
      "item-9167": {
        "value": 9,
        "weight": 1
      },
      "item-9168": {
        "value": 2,
        "weight": 9
      },
      "item-9169": {
        "value": 4,
        "weight": 8
      },
      "item-9170": {
        "value": 9,
        "weight": 3
      },
      "item-9171": {
        "value": 9,
        "weight": 1
      },
      "item-9172": {
        "value": 2,
        "weight": 7
      },
      "item-9173": {
        "value": 9,
        "weight": 1
      },
      "item-9174": {
        "value": 2,
        "weight": 3
      },
      "item-9175": {
        "value": 7,
        "weight": 2
      },
      "item-9176": {
        "value": 3,
        "weight": 7
      },
      "item-9177": {
        "value": 9,
        "weight": 4
      },
      "item-9178": {
        "value": 1,
        "weight": 7
      },
      "item-9179": {
        "value": 1,
        "weight": 1
      },
      "item-9180": {
        "value": 9,
        "weight": 5
      },
      "item-9181": {
        "value": 6,
        "weight": 5
      },
      "item-9182": {
        "value": 8,
        "weight": 7
      },
      "item-9183": {
        "value": 5,
        "weight": 3
      },
      "item-9184": {
        "value": 2,
        "weight": 3
      },
      "item-9185": {
        "value": 9,
        "weight": 9
      },
      "item-9186": {
        "value": 6,
        "weight": 8
      },
      "item-9187": {
        "value": 4,
        "weight": 8
      },
      "item-9188": {
        "value": 6,
        "weight": 7
      },
      "item-9189": {
        "value": 5,
        "weight": 7
      },
      "item-9190": {
        "value": 9,
        "weight": 3
      },
      "item-9191": {
        "value": 3,
        "weight": 7
      },
      "item-9192": {
        "value": 5,
        "weight": 2
      },
      "item-9193": {
        "value": 2,
        "weight": 9
      },
      "item-9194": {
        "value": 1,
        "weight": 9
      },
      "item-9195": {
        "value": 1,
        "weight": 5
      },
      "item-9196": {
        "value": 9,
        "weight": 7
      },
      "item-9197": {
        "value": 4,
        "weight": 8
      },
      "item-9198": {
        "value": 1,
        "weight": 4
      },
      "item-9199": {
        "value": 9,
        "weight": 6
      },
      "item-9200": {
        "value": 4,
        "weight": 6
      },
      "item-9201": {
        "value": 1,
        "weight": 9
      },
      "item-9202": {
        "value": 1,
        "weight": 8
      },
      "item-9203": {
        "value": 8,
        "weight": 1
      },
      "item-9204": {
        "value": 2,
        "weight": 8
      },
      "item-9205": {
        "value": 3,
        "weight": 8
      },
      "item-9206": {
        "value": 3,
        "weight": 6
      },
      "item-9207": {
        "value": 1,
        "weight": 7
      },
      "item-9208": {
        "value": 8,
        "weight": 2
      },
      "item-9209": {
        "value": 4,
        "weight": 2
      },
      "item-9210": {
        "value": 1,
        "weight": 3
      },
      "item-9211": {
        "value": 3,
        "weight": 2
      },
      "item-9212": {
        "value": 9,
        "weight": 7
      },
      "item-9213": {
        "value": 5,
        "weight": 8
      },
      "item-9214": {
        "value": 6,
        "weight": 9
      },
      "item-9215": {
        "value": 8,
        "weight": 5
      },
      "item-9216": {
        "value": 1,
        "weight": 1
      },
      "item-9217": {
        "value": 8,
        "weight": 1
      },
      "item-9218": {
        "value": 7,
        "weight": 7
      },
      "item-9219": {
        "value": 1,
        "weight": 9
      },
      "item-9220": {
        "value": 1,
        "weight": 8
      },
      "item-9221": {
        "value": 3,
        "weight": 5
      },
      "item-9222": {
        "value": 1,
        "weight": 2
      },
      "item-9223": {
        "value": 2,
        "weight": 4
      },
      "item-9224": {
        "value": 8,
        "weight": 7
      },
      "item-9225": {
        "value": 9,
        "weight": 1
      },
      "item-9226": {
        "value": 1,
        "weight": 5
      },
      "item-9227": {
        "value": 4,
        "weight": 3
      },
      "item-9228": {
        "value": 6,
        "weight": 7
      },
      "item-9229": {
        "value": 3,
        "weight": 9
      },
      "item-9230": {
        "value": 6,
        "weight": 3
      },
      "item-9231": {
        "value": 4,
        "weight": 6
      },
      "item-9232": {
        "value": 4,
        "weight": 1
      },
      "item-9233": {
        "value": 1,
        "weight": 3
      },
      "item-9234": {
        "value": 5,
        "weight": 9
      },
      "item-9235": {
        "value": 8,
        "weight": 7
      },
      "item-9236": {
        "value": 2,
        "weight": 7
      },
      "item-9237": {
        "value": 6,
        "weight": 4
      },
      "item-9238": {
        "value": 8,
        "weight": 3
      },
      "item-9239": {
        "value": 1,
        "weight": 1
      },
      "item-9240": {
        "value": 6,
        "weight": 3
      },
      "item-9241": {
        "value": 1,
        "weight": 6
      },
      "item-9242": {
        "value": 5,
        "weight": 7
      },
      "item-9243": {
        "value": 9,
        "weight": 2
      },
      "item-9244": {
        "value": 2,
        "weight": 3
      },
      "item-9245": {
        "value": 4,
        "weight": 4
      },
      "item-9246": {
        "value": 3,
        "weight": 1
      },
      "item-9247": {
        "value": 2,
        "weight": 9
      },
      "item-9248": {
        "value": 9,
        "weight": 4
      },
      "item-9249": {
        "value": 2,
        "weight": 5
      },
      "item-9250": {
        "value": 5,
        "weight": 2
      },
      "item-9251": {
        "value": 3,
        "weight": 2
      },
      "item-9252": {
        "value": 2,
        "weight": 9
      },
      "item-9253": {
        "value": 5,
        "weight": 4
      },
      "item-9254": {
        "value": 5,
        "weight": 7
      },
      "item-9255": {
        "value": 5,
        "weight": 6
      },
      "item-9256": {
        "value": 6,
        "weight": 7
      },
      "item-9257": {
        "value": 1,
        "weight": 4
      },
      "item-9258": {
        "value": 4,
        "weight": 1
      },
      "item-9259": {
        "value": 2,
        "weight": 8
      },
      "item-9260": {
        "value": 2,
        "weight": 5
      },
      "item-9261": {
        "value": 7,
        "weight": 9
      },
      "item-9262": {
        "value": 9,
        "weight": 1
      },
      "item-9263": {
        "value": 1,
        "weight": 7
      },
      "item-9264": {
        "value": 9,
        "weight": 8
      },
      "item-9265": {
        "value": 3,
        "weight": 9
      },
      "item-9266": {
        "value": 4,
        "weight": 2
      },
      "item-9267": {
        "value": 7,
        "weight": 7
      },
      "item-9268": {
        "value": 1,
        "weight": 5
      },
      "item-9269": {
        "value": 9,
        "weight": 8
      },
      "item-9270": {
        "value": 4,
        "weight": 1
      },
      "item-9271": {
        "value": 6,
        "weight": 2
      },
      "item-9272": {
        "value": 5,
        "weight": 4
      },
      "item-9273": {
        "value": 3,
        "weight": 3
      },
      "item-9274": {
        "value": 7,
        "weight": 1
      },
      "item-9275": {
        "value": 6,
        "weight": 7
      },
      "item-9276": {
        "value": 4,
        "weight": 3
      },
      "item-9277": {
        "value": 3,
        "weight": 4
      },
      "item-9278": {
        "value": 4,
        "weight": 3
      },
      "item-9279": {
        "value": 7,
        "weight": 2
      },
      "item-9280": {
        "value": 2,
        "weight": 2
      },
      "item-9281": {
        "value": 1,
        "weight": 6
      },
      "item-9282": {
        "value": 9,
        "weight": 5
      },
      "item-9283": {
        "value": 3,
        "weight": 8
      },
      "item-9284": {
        "value": 5,
        "weight": 9
      },
      "item-9285": {
        "value": 2,
        "weight": 5
      },
      "item-9286": {
        "value": 1,
        "weight": 4
      },
      "item-9287": {
        "value": 9,
        "weight": 1
      },
      "item-9288": {
        "value": 3,
        "weight": 2
      },
      "item-9289": {
        "value": 6,
        "weight": 6
      },
      "item-9290": {
        "value": 2,
        "weight": 9
      },
      "item-9291": {
        "value": 5,
        "weight": 9
      },
      "item-9292": {
        "value": 8,
        "weight": 7
      },
      "item-9293": {
        "value": 4,
        "weight": 6
      },
      "item-9294": {
        "value": 9,
        "weight": 7
      },
      "item-9295": {
        "value": 2,
        "weight": 4
      },
      "item-9296": {
        "value": 3,
        "weight": 2
      },
      "item-9297": {
        "value": 6,
        "weight": 3
      },
      "item-9298": {
        "value": 4,
        "weight": 3
      },
      "item-9299": {
        "value": 9,
        "weight": 7
      },
      "item-9300": {
        "value": 9,
        "weight": 9
      },
      "item-9301": {
        "value": 3,
        "weight": 5
      },
      "item-9302": {
        "value": 1,
        "weight": 5
      },
      "item-9303": {
        "value": 5,
        "weight": 4
      },
      "item-9304": {
        "value": 9,
        "weight": 4
      },
      "item-9305": {
        "value": 5,
        "weight": 3
      },
      "item-9306": {
        "value": 5,
        "weight": 5
      },
      "item-9307": {
        "value": 4,
        "weight": 2
      },
      "item-9308": {
        "value": 4,
        "weight": 4
      },
      "item-9309": {
        "value": 1,
        "weight": 4
      },
      "item-9310": {
        "value": 6,
        "weight": 7
      },
      "item-9311": {
        "value": 3,
        "weight": 4
      },
      "item-9312": {
        "value": 1,
        "weight": 9
      },
      "item-9313": {
        "value": 8,
        "weight": 8
      },
      "item-9314": {
        "value": 4,
        "weight": 4
      },
      "item-9315": {
        "value": 3,
        "weight": 1
      },
      "item-9316": {
        "value": 6,
        "weight": 9
      },
      "item-9317": {
        "value": 4,
        "weight": 9
      },
      "item-9318": {
        "value": 3,
        "weight": 2
      },
      "item-9319": {
        "value": 9,
        "weight": 3
      },
      "item-9320": {
        "value": 6,
        "weight": 2
      },
      "item-9321": {
        "value": 5,
        "weight": 8
      },
      "item-9322": {
        "value": 1,
        "weight": 1
      },
      "item-9323": {
        "value": 3,
        "weight": 8
      },
      "item-9324": {
        "value": 6,
        "weight": 2
      },
      "item-9325": {
        "value": 5,
        "weight": 7
      },
      "item-9326": {
        "value": 4,
        "weight": 1
      },
      "item-9327": {
        "value": 8,
        "weight": 1
      },
      "item-9328": {
        "value": 8,
        "weight": 9
      },
      "item-9329": {
        "value": 5,
        "weight": 7
      },
      "item-9330": {
        "value": 2,
        "weight": 5
      },
      "item-9331": {
        "value": 6,
        "weight": 4
      },
      "item-9332": {
        "value": 2,
        "weight": 3
      },
      "item-9333": {
        "value": 9,
        "weight": 8
      },
      "item-9334": {
        "value": 7,
        "weight": 2
      },
      "item-9335": {
        "value": 7,
        "weight": 1
      },
      "item-9336": {
        "value": 5,
        "weight": 3
      },
      "item-9337": {
        "value": 5,
        "weight": 6
      },
      "item-9338": {
        "value": 8,
        "weight": 6
      },
      "item-9339": {
        "value": 3,
        "weight": 6
      },
      "item-9340": {
        "value": 5,
        "weight": 4
      },
      "item-9341": {
        "value": 6,
        "weight": 1
      },
      "item-9342": {
        "value": 7,
        "weight": 1
      },
      "item-9343": {
        "value": 5,
        "weight": 8
      },
      "item-9344": {
        "value": 6,
        "weight": 5
      },
      "item-9345": {
        "value": 1,
        "weight": 9
      },
      "item-9346": {
        "value": 9,
        "weight": 1
      },
      "item-9347": {
        "value": 7,
        "weight": 8
      },
      "item-9348": {
        "value": 4,
        "weight": 2
      },
      "item-9349": {
        "value": 3,
        "weight": 5
      },
      "item-9350": {
        "value": 2,
        "weight": 2
      },
      "item-9351": {
        "value": 6,
        "weight": 8
      },
      "item-9352": {
        "value": 1,
        "weight": 6
      },
      "item-9353": {
        "value": 2,
        "weight": 4
      },
      "item-9354": {
        "value": 4,
        "weight": 6
      },
      "item-9355": {
        "value": 7,
        "weight": 7
      },
      "item-9356": {
        "value": 3,
        "weight": 4
      },
      "item-9357": {
        "value": 6,
        "weight": 5
      },
      "item-9358": {
        "value": 6,
        "weight": 1
      },
      "item-9359": {
        "value": 5,
        "weight": 6
      },
      "item-9360": {
        "value": 4,
        "weight": 1
      },
      "item-9361": {
        "value": 7,
        "weight": 7
      },
      "item-9362": {
        "value": 6,
        "weight": 7
      },
      "item-9363": {
        "value": 4,
        "weight": 2
      },
      "item-9364": {
        "value": 7,
        "weight": 5
      },
      "item-9365": {
        "value": 3,
        "weight": 4
      },
      "item-9366": {
        "value": 7,
        "weight": 5
      },
      "item-9367": {
        "value": 7,
        "weight": 3
      },
      "item-9368": {
        "value": 7,
        "weight": 8
      },
      "item-9369": {
        "value": 7,
        "weight": 4
      },
      "item-9370": {
        "value": 1,
        "weight": 6
      },
      "item-9371": {
        "value": 9,
        "weight": 1
      },
      "item-9372": {
        "value": 5,
        "weight": 7
      },
      "item-9373": {
        "value": 7,
        "weight": 1
      },
      "item-9374": {
        "value": 9,
        "weight": 9
      },
      "item-9375": {
        "value": 2,
        "weight": 8
      },
      "item-9376": {
        "value": 7,
        "weight": 9
      },
      "item-9377": {
        "value": 9,
        "weight": 9
      },
      "item-9378": {
        "value": 6,
        "weight": 7
      },
      "item-9379": {
        "value": 5,
        "weight": 6
      },
      "item-9380": {
        "value": 7,
        "weight": 9
      },
      "item-9381": {
        "value": 3,
        "weight": 4
      },
      "item-9382": {
        "value": 3,
        "weight": 4
      },
      "item-9383": {
        "value": 3,
        "weight": 8
      },
      "item-9384": {
        "value": 9,
        "weight": 7
      },
      "item-9385": {
        "value": 1,
        "weight": 9
      },
      "item-9386": {
        "value": 5,
        "weight": 6
      },
      "item-9387": {
        "value": 1,
        "weight": 4
      },
      "item-9388": {
        "value": 1,
        "weight": 5
      },
      "item-9389": {
        "value": 4,
        "weight": 9
      },
      "item-9390": {
        "value": 2,
        "weight": 2
      },
      "item-9391": {
        "value": 8,
        "weight": 4
      },
      "item-9392": {
        "value": 6,
        "weight": 7
      },
      "item-9393": {
        "value": 8,
        "weight": 7
      },
      "item-9394": {
        "value": 4,
        "weight": 4
      },
      "item-9395": {
        "value": 1,
        "weight": 9
      },
      "item-9396": {
        "value": 2,
        "weight": 5
      },
      "item-9397": {
        "value": 6,
        "weight": 2
      },
      "item-9398": {
        "value": 7,
        "weight": 6
      },
      "item-9399": {
        "value": 4,
        "weight": 2
      },
      "item-9400": {
        "value": 4,
        "weight": 4
      },
      "item-9401": {
        "value": 1,
        "weight": 3
      },
      "item-9402": {
        "value": 1,
        "weight": 5
      },
      "item-9403": {
        "value": 8,
        "weight": 8
      },
      "item-9404": {
        "value": 6,
        "weight": 8
      },
      "item-9405": {
        "value": 6,
        "weight": 2
      },
      "item-9406": {
        "value": 1,
        "weight": 2
      },
      "item-9407": {
        "value": 2,
        "weight": 4
      },
      "item-9408": {
        "value": 9,
        "weight": 1
      },
      "item-9409": {
        "value": 8,
        "weight": 1
      },
      "item-9410": {
        "value": 2,
        "weight": 6
      },
      "item-9411": {
        "value": 7,
        "weight": 1
      },
      "item-9412": {
        "value": 5,
        "weight": 7
      },
      "item-9413": {
        "value": 9,
        "weight": 4
      },
      "item-9414": {
        "value": 7,
        "weight": 5
      },
      "item-9415": {
        "value": 5,
        "weight": 9
      },
      "item-9416": {
        "value": 9,
        "weight": 2
      },
      "item-9417": {
        "value": 2,
        "weight": 4
      },
      "item-9418": {
        "value": 1,
        "weight": 9
      },
      "item-9419": {
        "value": 8,
        "weight": 8
      },
      "item-9420": {
        "value": 1,
        "weight": 3
      },
      "item-9421": {
        "value": 3,
        "weight": 9
      },
      "item-9422": {
        "value": 1,
        "weight": 5
      },
      "item-9423": {
        "value": 9,
        "weight": 5
      },
      "item-9424": {
        "value": 4,
        "weight": 5
      },
      "item-9425": {
        "value": 7,
        "weight": 1
      },
      "item-9426": {
        "value": 3,
        "weight": 3
      },
      "item-9427": {
        "value": 6,
        "weight": 2
      },
      "item-9428": {
        "value": 3,
        "weight": 8
      },
      "item-9429": {
        "value": 6,
        "weight": 1
      },
      "item-9430": {
        "value": 9,
        "weight": 9
      },
      "item-9431": {
        "value": 2,
        "weight": 7
      },
      "item-9432": {
        "value": 6,
        "weight": 9
      },
      "item-9433": {
        "value": 1,
        "weight": 6
      },
      "item-9434": {
        "value": 1,
        "weight": 9
      },
      "item-9435": {
        "value": 7,
        "weight": 6
      },
      "item-9436": {
        "value": 3,
        "weight": 7
      },
      "item-9437": {
        "value": 9,
        "weight": 1
      },
      "item-9438": {
        "value": 9,
        "weight": 6
      },
      "item-9439": {
        "value": 9,
        "weight": 4
      },
      "item-9440": {
        "value": 4,
        "weight": 6
      },
      "item-9441": {
        "value": 4,
        "weight": 2
      },
      "item-9442": {
        "value": 2,
        "weight": 7
      },
      "item-9443": {
        "value": 3,
        "weight": 4
      },
      "item-9444": {
        "value": 3,
        "weight": 5
      },
      "item-9445": {
        "value": 1,
        "weight": 5
      },
      "item-9446": {
        "value": 2,
        "weight": 2
      },
      "item-9447": {
        "value": 9,
        "weight": 1
      },
      "item-9448": {
        "value": 6,
        "weight": 8
      },
      "item-9449": {
        "value": 4,
        "weight": 4
      },
      "item-9450": {
        "value": 6,
        "weight": 1
      },
      "item-9451": {
        "value": 1,
        "weight": 9
      },
      "item-9452": {
        "value": 1,
        "weight": 2
      },
      "item-9453": {
        "value": 9,
        "weight": 9
      },
      "item-9454": {
        "value": 6,
        "weight": 6
      },
      "item-9455": {
        "value": 8,
        "weight": 2
      },
      "item-9456": {
        "value": 5,
        "weight": 6
      },
      "item-9457": {
        "value": 4,
        "weight": 6
      },
      "item-9458": {
        "value": 4,
        "weight": 1
      },
      "item-9459": {
        "value": 8,
        "weight": 3
      },
      "item-9460": {
        "value": 7,
        "weight": 7
      },
      "item-9461": {
        "value": 6,
        "weight": 8
      },
      "item-9462": {
        "value": 5,
        "weight": 1
      },
      "item-9463": {
        "value": 9,
        "weight": 4
      },
      "item-9464": {
        "value": 5,
        "weight": 1
      },
      "item-9465": {
        "value": 8,
        "weight": 4
      },
      "item-9466": {
        "value": 9,
        "weight": 2
      },
      "item-9467": {
        "value": 6,
        "weight": 5
      },
      "item-9468": {
        "value": 5,
        "weight": 5
      },
      "item-9469": {
        "value": 6,
        "weight": 6
      },
      "item-9470": {
        "value": 1,
        "weight": 8
      },
      "item-9471": {
        "value": 6,
        "weight": 3
      },
      "item-9472": {
        "value": 3,
        "weight": 3
      },
      "item-9473": {
        "value": 1,
        "weight": 3
      },
      "item-9474": {
        "value": 2,
        "weight": 5
      },
      "item-9475": {
        "value": 2,
        "weight": 6
      },
      "item-9476": {
        "value": 7,
        "weight": 2
      },
      "item-9477": {
        "value": 4,
        "weight": 1
      },
      "item-9478": {
        "value": 3,
        "weight": 6
      },
      "item-9479": {
        "value": 6,
        "weight": 4
      },
      "item-9480": {
        "value": 9,
        "weight": 7
      },
      "item-9481": {
        "value": 7,
        "weight": 5
      },
      "item-9482": {
        "value": 3,
        "weight": 1
      },
      "item-9483": {
        "value": 5,
        "weight": 5
      },
      "item-9484": {
        "value": 1,
        "weight": 2
      },
      "item-9485": {
        "value": 6,
        "weight": 1
      },
      "item-9486": {
        "value": 7,
        "weight": 2
      },
      "item-9487": {
        "value": 5,
        "weight": 5
      },
      "item-9488": {
        "value": 4,
        "weight": 5
      },
      "item-9489": {
        "value": 2,
        "weight": 6
      },
      "item-9490": {
        "value": 5,
        "weight": 9
      },
      "item-9491": {
        "value": 5,
        "weight": 6
      },
      "item-9492": {
        "value": 2,
        "weight": 6
      },
      "item-9493": {
        "value": 6,
        "weight": 2
      },
      "item-9494": {
        "value": 3,
        "weight": 9
      },
      "item-9495": {
        "value": 7,
        "weight": 4
      },
      "item-9496": {
        "value": 5,
        "weight": 8
      },
      "item-9497": {
        "value": 4,
        "weight": 6
      },
      "item-9498": {
        "value": 2,
        "weight": 7
      },
      "item-9499": {
        "value": 9,
        "weight": 2
      },
      "item-9500": {
        "value": 4,
        "weight": 5
      },
      "item-9501": {
        "value": 9,
        "weight": 3
      },
      "item-9502": {
        "value": 1,
        "weight": 1
      },
      "item-9503": {
        "value": 3,
        "weight": 8
      },
      "item-9504": {
        "value": 3,
        "weight": 8
      },
      "item-9505": {
        "value": 9,
        "weight": 7
      },
      "item-9506": {
        "value": 3,
        "weight": 1
      },
      "item-9507": {
        "value": 6,
        "weight": 8
      },
      "item-9508": {
        "value": 9,
        "weight": 6
      },
      "item-9509": {
        "value": 3,
        "weight": 1
      },
      "item-9510": {
        "value": 5,
        "weight": 5
      },
      "item-9511": {
        "value": 8,
        "weight": 2
      },
      "item-9512": {
        "value": 6,
        "weight": 1
      },
      "item-9513": {
        "value": 6,
        "weight": 8
      },
      "item-9514": {
        "value": 5,
        "weight": 8
      },
      "item-9515": {
        "value": 4,
        "weight": 1
      },
      "item-9516": {
        "value": 1,
        "weight": 1
      },
      "item-9517": {
        "value": 8,
        "weight": 4
      },
      "item-9518": {
        "value": 7,
        "weight": 4
      },
      "item-9519": {
        "value": 5,
        "weight": 8
      },
      "item-9520": {
        "value": 4,
        "weight": 7
      },
      "item-9521": {
        "value": 2,
        "weight": 1
      },
      "item-9522": {
        "value": 9,
        "weight": 3
      },
      "item-9523": {
        "value": 7,
        "weight": 2
      },
      "item-9524": {
        "value": 8,
        "weight": 3
      },
      "item-9525": {
        "value": 1,
        "weight": 4
      },
      "item-9526": {
        "value": 7,
        "weight": 4
      },
      "item-9527": {
        "value": 5,
        "weight": 1
      },
      "item-9528": {
        "value": 5,
        "weight": 9
      },
      "item-9529": {
        "value": 3,
        "weight": 9
      },
      "item-9530": {
        "value": 2,
        "weight": 2
      },
      "item-9531": {
        "value": 8,
        "weight": 7
      },
      "item-9532": {
        "value": 9,
        "weight": 7
      },
      "item-9533": {
        "value": 8,
        "weight": 1
      },
      "item-9534": {
        "value": 1,
        "weight": 8
      },
      "item-9535": {
        "value": 2,
        "weight": 4
      },
      "item-9536": {
        "value": 2,
        "weight": 5
      },
      "item-9537": {
        "value": 4,
        "weight": 7
      },
      "item-9538": {
        "value": 2,
        "weight": 2
      },
      "item-9539": {
        "value": 9,
        "weight": 8
      },
      "item-9540": {
        "value": 3,
        "weight": 3
      },
      "item-9541": {
        "value": 5,
        "weight": 1
      },
      "item-9542": {
        "value": 4,
        "weight": 4
      },
      "item-9543": {
        "value": 6,
        "weight": 4
      },
      "item-9544": {
        "value": 5,
        "weight": 6
      },
      "item-9545": {
        "value": 2,
        "weight": 5
      },
      "item-9546": {
        "value": 7,
        "weight": 7
      },
      "item-9547": {
        "value": 6,
        "weight": 6
      },
      "item-9548": {
        "value": 2,
        "weight": 1
      },
      "item-9549": {
        "value": 2,
        "weight": 9
      },
      "item-9550": {
        "value": 3,
        "weight": 5
      },
      "item-9551": {
        "value": 7,
        "weight": 8
      },
      "item-9552": {
        "value": 9,
        "weight": 2
      },
      "item-9553": {
        "value": 5,
        "weight": 4
      },
      "item-9554": {
        "value": 2,
        "weight": 1
      },
      "item-9555": {
        "value": 5,
        "weight": 5
      },
      "item-9556": {
        "value": 4,
        "weight": 4
      },
      "item-9557": {
        "value": 2,
        "weight": 3
      },
      "item-9558": {
        "value": 2,
        "weight": 6
      },
      "item-9559": {
        "value": 7,
        "weight": 9
      },
      "item-9560": {
        "value": 2,
        "weight": 5
      },
      "item-9561": {
        "value": 1,
        "weight": 5
      },
      "item-9562": {
        "value": 4,
        "weight": 6
      },
      "item-9563": {
        "value": 3,
        "weight": 2
      },
      "item-9564": {
        "value": 2,
        "weight": 9
      },
      "item-9565": {
        "value": 8,
        "weight": 9
      },
      "item-9566": {
        "value": 1,
        "weight": 8
      },
      "item-9567": {
        "value": 5,
        "weight": 5
      },
      "item-9568": {
        "value": 1,
        "weight": 1
      },
      "item-9569": {
        "value": 5,
        "weight": 8
      },
      "item-9570": {
        "value": 3,
        "weight": 5
      },
      "item-9571": {
        "value": 3,
        "weight": 5
      },
      "item-9572": {
        "value": 4,
        "weight": 7
      },
      "item-9573": {
        "value": 4,
        "weight": 9
      },
      "item-9574": {
        "value": 7,
        "weight": 9
      },
      "item-9575": {
        "value": 7,
        "weight": 5
      },
      "item-9576": {
        "value": 7,
        "weight": 8
      },
      "item-9577": {
        "value": 5,
        "weight": 6
      },
      "item-9578": {
        "value": 9,
        "weight": 3
      },
      "item-9579": {
        "value": 3,
        "weight": 3
      },
      "item-9580": {
        "value": 2,
        "weight": 8
      },
      "item-9581": {
        "value": 8,
        "weight": 7
      },
      "item-9582": {
        "value": 5,
        "weight": 5
      },
      "item-9583": {
        "value": 6,
        "weight": 7
      },
      "item-9584": {
        "value": 4,
        "weight": 8
      },
      "item-9585": {
        "value": 7,
        "weight": 8
      },
      "item-9586": {
        "value": 9,
        "weight": 4
      },
      "item-9587": {
        "value": 1,
        "weight": 1
      },
      "item-9588": {
        "value": 4,
        "weight": 4
      },
      "item-9589": {
        "value": 2,
        "weight": 6
      },
      "item-9590": {
        "value": 1,
        "weight": 2
      },
      "item-9591": {
        "value": 8,
        "weight": 4
      },
      "item-9592": {
        "value": 6,
        "weight": 2
      },
      "item-9593": {
        "value": 9,
        "weight": 1
      },
      "item-9594": {
        "value": 7,
        "weight": 6
      },
      "item-9595": {
        "value": 8,
        "weight": 8
      },
      "item-9596": {
        "value": 5,
        "weight": 4
      },
      "item-9597": {
        "value": 2,
        "weight": 3
      },
      "item-9598": {
        "value": 8,
        "weight": 1
      },
      "item-9599": {
        "value": 7,
        "weight": 8
      },
      "item-9600": {
        "value": 7,
        "weight": 7
      },
      "item-9601": {
        "value": 3,
        "weight": 5
      },
      "item-9602": {
        "value": 5,
        "weight": 3
      },
      "item-9603": {
        "value": 7,
        "weight": 9
      },
      "item-9604": {
        "value": 2,
        "weight": 9
      },
      "item-9605": {
        "value": 4,
        "weight": 9
      },
      "item-9606": {
        "value": 1,
        "weight": 2
      },
      "item-9607": {
        "value": 5,
        "weight": 8
      },
      "item-9608": {
        "value": 8,
        "weight": 2
      },
      "item-9609": {
        "value": 9,
        "weight": 5
      },
      "item-9610": {
        "value": 4,
        "weight": 9
      },
      "item-9611": {
        "value": 5,
        "weight": 4
      },
      "item-9612": {
        "value": 2,
        "weight": 6
      },
      "item-9613": {
        "value": 6,
        "weight": 8
      },
      "item-9614": {
        "value": 9,
        "weight": 8
      },
      "item-9615": {
        "value": 6,
        "weight": 1
      },
      "item-9616": {
        "value": 5,
        "weight": 9
      },
      "item-9617": {
        "value": 8,
        "weight": 2
      },
      "item-9618": {
        "value": 9,
        "weight": 9
      },
      "item-9619": {
        "value": 8,
        "weight": 6
      },
      "item-9620": {
        "value": 4,
        "weight": 2
      },
      "item-9621": {
        "value": 1,
        "weight": 6
      },
      "item-9622": {
        "value": 1,
        "weight": 6
      },
      "item-9623": {
        "value": 9,
        "weight": 1
      },
      "item-9624": {
        "value": 1,
        "weight": 3
      },
      "item-9625": {
        "value": 9,
        "weight": 8
      },
      "item-9626": {
        "value": 9,
        "weight": 6
      },
      "item-9627": {
        "value": 6,
        "weight": 6
      },
      "item-9628": {
        "value": 4,
        "weight": 8
      },
      "item-9629": {
        "value": 9,
        "weight": 1
      },
      "item-9630": {
        "value": 5,
        "weight": 8
      },
      "item-9631": {
        "value": 3,
        "weight": 2
      },
      "item-9632": {
        "value": 5,
        "weight": 4
      },
      "item-9633": {
        "value": 5,
        "weight": 6
      },
      "item-9634": {
        "value": 3,
        "weight": 2
      },
      "item-9635": {
        "value": 7,
        "weight": 7
      },
      "item-9636": {
        "value": 5,
        "weight": 7
      },
      "item-9637": {
        "value": 7,
        "weight": 1
      },
      "item-9638": {
        "value": 6,
        "weight": 4
      },
      "item-9639": {
        "value": 6,
        "weight": 5
      },
      "item-9640": {
        "value": 9,
        "weight": 9
      },
      "item-9641": {
        "value": 9,
        "weight": 1
      },
      "item-9642": {
        "value": 5,
        "weight": 1
      },
      "item-9643": {
        "value": 2,
        "weight": 2
      },
      "item-9644": {
        "value": 4,
        "weight": 1
      },
      "item-9645": {
        "value": 5,
        "weight": 5
      },
      "item-9646": {
        "value": 3,
        "weight": 1
      },
      "item-9647": {
        "value": 1,
        "weight": 6
      },
      "item-9648": {
        "value": 5,
        "weight": 8
      },
      "item-9649": {
        "value": 8,
        "weight": 3
      },
      "item-9650": {
        "value": 2,
        "weight": 7
      },
      "item-9651": {
        "value": 3,
        "weight": 1
      },
      "item-9652": {
        "value": 9,
        "weight": 3
      },
      "item-9653": {
        "value": 3,
        "weight": 3
      },
      "item-9654": {
        "value": 9,
        "weight": 6
      },
      "item-9655": {
        "value": 7,
        "weight": 8
      },
      "item-9656": {
        "value": 1,
        "weight": 6
      },
      "item-9657": {
        "value": 9,
        "weight": 7
      },
      "item-9658": {
        "value": 9,
        "weight": 6
      },
      "item-9659": {
        "value": 8,
        "weight": 4
      },
      "item-9660": {
        "value": 9,
        "weight": 4
      },
      "item-9661": {
        "value": 4,
        "weight": 7
      },
      "item-9662": {
        "value": 4,
        "weight": 9
      },
      "item-9663": {
        "value": 6,
        "weight": 8
      },
      "item-9664": {
        "value": 3,
        "weight": 1
      },
      "item-9665": {
        "value": 1,
        "weight": 3
      },
      "item-9666": {
        "value": 5,
        "weight": 5
      },
      "item-9667": {
        "value": 4,
        "weight": 6
      },
      "item-9668": {
        "value": 3,
        "weight": 7
      },
      "item-9669": {
        "value": 2,
        "weight": 1
      },
      "item-9670": {
        "value": 6,
        "weight": 8
      },
      "item-9671": {
        "value": 7,
        "weight": 2
      },
      "item-9672": {
        "value": 3,
        "weight": 7
      },
      "item-9673": {
        "value": 3,
        "weight": 8
      },
      "item-9674": {
        "value": 4,
        "weight": 8
      },
      "item-9675": {
        "value": 6,
        "weight": 6
      },
      "item-9676": {
        "value": 3,
        "weight": 6
      },
      "item-9677": {
        "value": 8,
        "weight": 1
      },
      "item-9678": {
        "value": 3,
        "weight": 7
      },
      "item-9679": {
        "value": 3,
        "weight": 2
      },
      "item-9680": {
        "value": 1,
        "weight": 4
      },
      "item-9681": {
        "value": 3,
        "weight": 5
      },
      "item-9682": {
        "value": 2,
        "weight": 6
      },
      "item-9683": {
        "value": 3,
        "weight": 8
      },
      "item-9684": {
        "value": 3,
        "weight": 7
      },
      "item-9685": {
        "value": 1,
        "weight": 4
      },
      "item-9686": {
        "value": 9,
        "weight": 8
      },
      "item-9687": {
        "value": 2,
        "weight": 6
      },
      "item-9688": {
        "value": 3,
        "weight": 5
      },
      "item-9689": {
        "value": 9,
        "weight": 2
      },
      "item-9690": {
        "value": 3,
        "weight": 7
      },
      "item-9691": {
        "value": 1,
        "weight": 1
      },
      "item-9692": {
        "value": 9,
        "weight": 2
      },
      "item-9693": {
        "value": 9,
        "weight": 7
      },
      "item-9694": {
        "value": 6,
        "weight": 6
      },
      "item-9695": {
        "value": 6,
        "weight": 2
      },
      "item-9696": {
        "value": 3,
        "weight": 1
      },
      "item-9697": {
        "value": 8,
        "weight": 9
      },
      "item-9698": {
        "value": 1,
        "weight": 7
      },
      "item-9699": {
        "value": 1,
        "weight": 4
      },
      "item-9700": {
        "value": 4,
        "weight": 3
      },
      "item-9701": {
        "value": 5,
        "weight": 6
      },
      "item-9702": {
        "value": 9,
        "weight": 9
      },
      "item-9703": {
        "value": 5,
        "weight": 2
      },
      "item-9704": {
        "value": 2,
        "weight": 2
      },
      "item-9705": {
        "value": 7,
        "weight": 9
      },
      "item-9706": {
        "value": 9,
        "weight": 5
      },
      "item-9707": {
        "value": 6,
        "weight": 6
      },
      "item-9708": {
        "value": 8,
        "weight": 8
      },
      "item-9709": {
        "value": 9,
        "weight": 1
      },
      "item-9710": {
        "value": 9,
        "weight": 3
      },
      "item-9711": {
        "value": 7,
        "weight": 1
      },
      "item-9712": {
        "value": 5,
        "weight": 4
      },
      "item-9713": {
        "value": 7,
        "weight": 5
      },
      "item-9714": {
        "value": 2,
        "weight": 8
      },
      "item-9715": {
        "value": 2,
        "weight": 4
      },
      "item-9716": {
        "value": 4,
        "weight": 7
      },
      "item-9717": {
        "value": 9,
        "weight": 4
      },
      "item-9718": {
        "value": 2,
        "weight": 3
      },
      "item-9719": {
        "value": 8,
        "weight": 1
      },
      "item-9720": {
        "value": 4,
        "weight": 8
      },
      "item-9721": {
        "value": 7,
        "weight": 6
      },
      "item-9722": {
        "value": 3,
        "weight": 5
      },
      "item-9723": {
        "value": 6,
        "weight": 3
      },
      "item-9724": {
        "value": 1,
        "weight": 6
      },
      "item-9725": {
        "value": 7,
        "weight": 6
      },
      "item-9726": {
        "value": 3,
        "weight": 5
      },
      "item-9727": {
        "value": 3,
        "weight": 3
      },
      "item-9728": {
        "value": 3,
        "weight": 6
      },
      "item-9729": {
        "value": 7,
        "weight": 5
      },
      "item-9730": {
        "value": 1,
        "weight": 1
      },
      "item-9731": {
        "value": 7,
        "weight": 3
      },
      "item-9732": {
        "value": 2,
        "weight": 1
      },
      "item-9733": {
        "value": 8,
        "weight": 1
      },
      "item-9734": {
        "value": 6,
        "weight": 2
      },
      "item-9735": {
        "value": 8,
        "weight": 5
      },
      "item-9736": {
        "value": 3,
        "weight": 8
      },
      "item-9737": {
        "value": 6,
        "weight": 3
      },
      "item-9738": {
        "value": 8,
        "weight": 2
      },
      "item-9739": {
        "value": 1,
        "weight": 6
      },
      "item-9740": {
        "value": 7,
        "weight": 4
      },
      "item-9741": {
        "value": 5,
        "weight": 6
      },
      "item-9742": {
        "value": 9,
        "weight": 6
      },
      "item-9743": {
        "value": 5,
        "weight": 9
      },
      "item-9744": {
        "value": 9,
        "weight": 2
      },
      "item-9745": {
        "value": 1,
        "weight": 3
      },
      "item-9746": {
        "value": 1,
        "weight": 8
      },
      "item-9747": {
        "value": 1,
        "weight": 2
      },
      "item-9748": {
        "value": 4,
        "weight": 9
      },
      "item-9749": {
        "value": 4,
        "weight": 6
      },
      "item-9750": {
        "value": 8,
        "weight": 7
      },
      "item-9751": {
        "value": 4,
        "weight": 6
      },
      "item-9752": {
        "value": 8,
        "weight": 2
      },
      "item-9753": {
        "value": 9,
        "weight": 9
      },
      "item-9754": {
        "value": 5,
        "weight": 7
      },
      "item-9755": {
        "value": 6,
        "weight": 6
      },
      "item-9756": {
        "value": 6,
        "weight": 8
      },
      "item-9757": {
        "value": 9,
        "weight": 8
      },
      "item-9758": {
        "value": 7,
        "weight": 9
      },
      "item-9759": {
        "value": 4,
        "weight": 1
      },
      "item-9760": {
        "value": 2,
        "weight": 1
      },
      "item-9761": {
        "value": 1,
        "weight": 9
      },
      "item-9762": {
        "value": 1,
        "weight": 4
      },
      "item-9763": {
        "value": 6,
        "weight": 6
      },
      "item-9764": {
        "value": 1,
        "weight": 1
      },
      "item-9765": {
        "value": 3,
        "weight": 5
      },
      "item-9766": {
        "value": 1,
        "weight": 1
      },
      "item-9767": {
        "value": 7,
        "weight": 8
      },
      "item-9768": {
        "value": 9,
        "weight": 4
      },
      "item-9769": {
        "value": 8,
        "weight": 7
      },
      "item-9770": {
        "value": 3,
        "weight": 3
      },
      "item-9771": {
        "value": 1,
        "weight": 1
      },
      "item-9772": {
        "value": 3,
        "weight": 2
      },
      "item-9773": {
        "value": 4,
        "weight": 3
      },
      "item-9774": {
        "value": 9,
        "weight": 5
      },
      "item-9775": {
        "value": 4,
        "weight": 9
      },
      "item-9776": {
        "value": 7,
        "weight": 4
      },
      "item-9777": {
        "value": 3,
        "weight": 1
      },
      "item-9778": {
        "value": 9,
        "weight": 2
      },
      "item-9779": {
        "value": 7,
        "weight": 2
      },
      "item-9780": {
        "value": 1,
        "weight": 2
      },
      "item-9781": {
        "value": 4,
        "weight": 4
      },
      "item-9782": {
        "value": 2,
        "weight": 1
      },
      "item-9783": {
        "value": 4,
        "weight": 1
      },
      "item-9784": {
        "value": 9,
        "weight": 7
      },
      "item-9785": {
        "value": 7,
        "weight": 4
      },
      "item-9786": {
        "value": 9,
        "weight": 1
      },
      "item-9787": {
        "value": 3,
        "weight": 8
      },
      "item-9788": {
        "value": 9,
        "weight": 1
      },
      "item-9789": {
        "value": 6,
        "weight": 8
      },
      "item-9790": {
        "value": 8,
        "weight": 2
      },
      "item-9791": {
        "value": 4,
        "weight": 6
      },
      "item-9792": {
        "value": 6,
        "weight": 1
      },
      "item-9793": {
        "value": 8,
        "weight": 3
      },
      "item-9794": {
        "value": 9,
        "weight": 2
      },
      "item-9795": {
        "value": 3,
        "weight": 5
      },
      "item-9796": {
        "value": 3,
        "weight": 4
      },
      "item-9797": {
        "value": 3,
        "weight": 2
      },
      "item-9798": {
        "value": 3,
        "weight": 7
      },
      "item-9799": {
        "value": 8,
        "weight": 1
      },
      "item-9800": {
        "value": 7,
        "weight": 6
      },
      "item-9801": {
        "value": 2,
        "weight": 8
      },
      "item-9802": {
        "value": 7,
        "weight": 6
      },
      "item-9803": {
        "value": 9,
        "weight": 8
      },
      "item-9804": {
        "value": 5,
        "weight": 3
      },
      "item-9805": {
        "value": 2,
        "weight": 1
      },
      "item-9806": {
        "value": 4,
        "weight": 4
      },
      "item-9807": {
        "value": 9,
        "weight": 5
      },
      "item-9808": {
        "value": 5,
        "weight": 8
      },
      "item-9809": {
        "value": 7,
        "weight": 3
      },
      "item-9810": {
        "value": 7,
        "weight": 5
      },
      "item-9811": {
        "value": 8,
        "weight": 3
      },
      "item-9812": {
        "value": 5,
        "weight": 9
      },
      "item-9813": {
        "value": 2,
        "weight": 2
      },
      "item-9814": {
        "value": 3,
        "weight": 9
      },
      "item-9815": {
        "value": 1,
        "weight": 5
      },
      "item-9816": {
        "value": 1,
        "weight": 7
      },
      "item-9817": {
        "value": 4,
        "weight": 6
      },
      "item-9818": {
        "value": 6,
        "weight": 6
      },
      "item-9819": {
        "value": 1,
        "weight": 2
      },
      "item-9820": {
        "value": 2,
        "weight": 3
      },
      "item-9821": {
        "value": 6,
        "weight": 9
      },
      "item-9822": {
        "value": 8,
        "weight": 3
      },
      "item-9823": {
        "value": 7,
        "weight": 2
      },
      "item-9824": {
        "value": 6,
        "weight": 7
      },
      "item-9825": {
        "value": 4,
        "weight": 1
      },
      "item-9826": {
        "value": 6,
        "weight": 2
      },
      "item-9827": {
        "value": 1,
        "weight": 9
      },
      "item-9828": {
        "value": 8,
        "weight": 3
      },
      "item-9829": {
        "value": 7,
        "weight": 7
      },
      "item-9830": {
        "value": 7,
        "weight": 8
      },
      "item-9831": {
        "value": 7,
        "weight": 8
      },
      "item-9832": {
        "value": 6,
        "weight": 6
      },
      "item-9833": {
        "value": 7,
        "weight": 6
      },
      "item-9834": {
        "value": 8,
        "weight": 4
      },
      "item-9835": {
        "value": 5,
        "weight": 4
      },
      "item-9836": {
        "value": 8,
        "weight": 2
      },
      "item-9837": {
        "value": 9,
        "weight": 1
      },
      "item-9838": {
        "value": 8,
        "weight": 3
      },
      "item-9839": {
        "value": 5,
        "weight": 5
      },
      "item-9840": {
        "value": 6,
        "weight": 7
      },
      "item-9841": {
        "value": 8,
        "weight": 7
      },
      "item-9842": {
        "value": 7,
        "weight": 7
      },
      "item-9843": {
        "value": 8,
        "weight": 2
      },
      "item-9844": {
        "value": 4,
        "weight": 5
      },
      "item-9845": {
        "value": 6,
        "weight": 6
      },
      "item-9846": {
        "value": 3,
        "weight": 2
      },
      "item-9847": {
        "value": 6,
        "weight": 4
      },
      "item-9848": {
        "value": 9,
        "weight": 3
      },
      "item-9849": {
        "value": 5,
        "weight": 9
      },
      "item-9850": {
        "value": 9,
        "weight": 6
      },
      "item-9851": {
        "value": 6,
        "weight": 2
      },
      "item-9852": {
        "value": 6,
        "weight": 1
      },
      "item-9853": {
        "value": 2,
        "weight": 4
      },
      "item-9854": {
        "value": 1,
        "weight": 7
      },
      "item-9855": {
        "value": 2,
        "weight": 2
      },
      "item-9856": {
        "value": 4,
        "weight": 3
      },
      "item-9857": {
        "value": 9,
        "weight": 8
      },
      "item-9858": {
        "value": 4,
        "weight": 4
      },
      "item-9859": {
        "value": 3,
        "weight": 3
      },
      "item-9860": {
        "value": 9,
        "weight": 7
      },
      "item-9861": {
        "value": 8,
        "weight": 7
      },
      "item-9862": {
        "value": 6,
        "weight": 4
      },
      "item-9863": {
        "value": 5,
        "weight": 6
      },
      "item-9864": {
        "value": 7,
        "weight": 4
      },
      "item-9865": {
        "value": 3,
        "weight": 4
      },
      "item-9866": {
        "value": 8,
        "weight": 3
      },
      "item-9867": {
        "value": 8,
        "weight": 9
      },
      "item-9868": {
        "value": 1,
        "weight": 1
      },
      "item-9869": {
        "value": 2,
        "weight": 7
      },
      "item-9870": {
        "value": 2,
        "weight": 2
      },
      "item-9871": {
        "value": 1,
        "weight": 1
      },
      "item-9872": {
        "value": 9,
        "weight": 5
      },
      "item-9873": {
        "value": 9,
        "weight": 4
      },
      "item-9874": {
        "value": 9,
        "weight": 8
      },
      "item-9875": {
        "value": 4,
        "weight": 7
      },
      "item-9876": {
        "value": 5,
        "weight": 3
      },
      "item-9877": {
        "value": 7,
        "weight": 8
      },
      "item-9878": {
        "value": 5,
        "weight": 5
      },
      "item-9879": {
        "value": 3,
        "weight": 4
      },
      "item-9880": {
        "value": 8,
        "weight": 8
      },
      "item-9881": {
        "value": 9,
        "weight": 2
      },
      "item-9882": {
        "value": 3,
        "weight": 2
      },
      "item-9883": {
        "value": 2,
        "weight": 2
      },
      "item-9884": {
        "value": 4,
        "weight": 8
      },
      "item-9885": {
        "value": 3,
        "weight": 8
      },
      "item-9886": {
        "value": 8,
        "weight": 8
      },
      "item-9887": {
        "value": 9,
        "weight": 3
      },
      "item-9888": {
        "value": 5,
        "weight": 4
      },
      "item-9889": {
        "value": 6,
        "weight": 1
      },
      "item-9890": {
        "value": 8,
        "weight": 5
      },
      "item-9891": {
        "value": 5,
        "weight": 7
      },
      "item-9892": {
        "value": 1,
        "weight": 9
      },
      "item-9893": {
        "value": 6,
        "weight": 3
      },
      "item-9894": {
        "value": 3,
        "weight": 1
      },
      "item-9895": {
        "value": 6,
        "weight": 6
      },
      "item-9896": {
        "value": 3,
        "weight": 4
      },
      "item-9897": {
        "value": 9,
        "weight": 4
      },
      "item-9898": {
        "value": 9,
        "weight": 7
      },
      "item-9899": {
        "value": 5,
        "weight": 2
      },
      "item-9900": {
        "value": 4,
        "weight": 3
      },
      "item-9901": {
        "value": 6,
        "weight": 2
      },
      "item-9902": {
        "value": 6,
        "weight": 8
      },
      "item-9903": {
        "value": 2,
        "weight": 4
      },
      "item-9904": {
        "value": 1,
        "weight": 1
      },
      "item-9905": {
        "value": 8,
        "weight": 2
      },
      "item-9906": {
        "value": 5,
        "weight": 6
      },
      "item-9907": {
        "value": 3,
        "weight": 7
      },
      "item-9908": {
        "value": 1,
        "weight": 6
      },
      "item-9909": {
        "value": 4,
        "weight": 9
      },
      "item-9910": {
        "value": 6,
        "weight": 9
      },
      "item-9911": {
        "value": 2,
        "weight": 1
      },
      "item-9912": {
        "value": 3,
        "weight": 4
      },
      "item-9913": {
        "value": 8,
        "weight": 6
      },
      "item-9914": {
        "value": 8,
        "weight": 5
      },
      "item-9915": {
        "value": 3,
        "weight": 6
      },
      "item-9916": {
        "value": 2,
        "weight": 2
      },
      "item-9917": {
        "value": 9,
        "weight": 4
      },
      "item-9918": {
        "value": 3,
        "weight": 6
      },
      "item-9919": {
        "value": 4,
        "weight": 3
      },
      "item-9920": {
        "value": 5,
        "weight": 2
      },
      "item-9921": {
        "value": 1,
        "weight": 5
      },
      "item-9922": {
        "value": 6,
        "weight": 5
      },
      "item-9923": {
        "value": 9,
        "weight": 2
      },
      "item-9924": {
        "value": 2,
        "weight": 1
      },
      "item-9925": {
        "value": 4,
        "weight": 3
      },
      "item-9926": {
        "value": 9,
        "weight": 7
      },
      "item-9927": {
        "value": 3,
        "weight": 4
      },
      "item-9928": {
        "value": 3,
        "weight": 3
      },
      "item-9929": {
        "value": 5,
        "weight": 4
      },
      "item-9930": {
        "value": 4,
        "weight": 1
      },
      "item-9931": {
        "value": 9,
        "weight": 1
      },
      "item-9932": {
        "value": 5,
        "weight": 6
      },
      "item-9933": {
        "value": 8,
        "weight": 9
      },
      "item-9934": {
        "value": 7,
        "weight": 9
      },
      "item-9935": {
        "value": 5,
        "weight": 3
      },
      "item-9936": {
        "value": 8,
        "weight": 8
      },
      "item-9937": {
        "value": 8,
        "weight": 6
      },
      "item-9938": {
        "value": 2,
        "weight": 3
      },
      "item-9939": {
        "value": 1,
        "weight": 7
      },
      "item-9940": {
        "value": 3,
        "weight": 4
      },
      "item-9941": {
        "value": 8,
        "weight": 9
      },
      "item-9942": {
        "value": 9,
        "weight": 4
      },
      "item-9943": {
        "value": 8,
        "weight": 8
      },
      "item-9944": {
        "value": 5,
        "weight": 6
      },
      "item-9945": {
        "value": 1,
        "weight": 3
      },
      "item-9946": {
        "value": 6,
        "weight": 4
      },
      "item-9947": {
        "value": 2,
        "weight": 6
      },
      "item-9948": {
        "value": 8,
        "weight": 3
      },
      "item-9949": {
        "value": 5,
        "weight": 5
      },
      "item-9950": {
        "value": 2,
        "weight": 4
      },
      "item-9951": {
        "value": 1,
        "weight": 7
      },
      "item-9952": {
        "value": 4,
        "weight": 2
      },
      "item-9953": {
        "value": 9,
        "weight": 5
      },
      "item-9954": {
        "value": 7,
        "weight": 9
      },
      "item-9955": {
        "value": 6,
        "weight": 8
      },
      "item-9956": {
        "value": 8,
        "weight": 5
      },
      "item-9957": {
        "value": 4,
        "weight": 3
      },
      "item-9958": {
        "value": 9,
        "weight": 2
      },
      "item-9959": {
        "value": 2,
        "weight": 7
      },
      "item-9960": {
        "value": 6,
        "weight": 1
      },
      "item-9961": {
        "value": 2,
        "weight": 3
      },
      "item-9962": {
        "value": 6,
        "weight": 4
      },
      "item-9963": {
        "value": 4,
        "weight": 2
      },
      "item-9964": {
        "value": 7,
        "weight": 3
      },
      "item-9965": {
        "value": 3,
        "weight": 3
      },
      "item-9966": {
        "value": 9,
        "weight": 3
      },
      "item-9967": {
        "value": 7,
        "weight": 6
      },
      "item-9968": {
        "value": 6,
        "weight": 8
      },
      "item-9969": {
        "value": 1,
        "weight": 5
      },
      "item-9970": {
        "value": 4,
        "weight": 3
      },
      "item-9971": {
        "value": 7,
        "weight": 2
      },
      "item-9972": {
        "value": 1,
        "weight": 6
      },
      "item-9973": {
        "value": 7,
        "weight": 8
      },
      "item-9974": {
        "value": 9,
        "weight": 6
      },
      "item-9975": {
        "value": 9,
        "weight": 1
      },
      "item-9976": {
        "value": 8,
        "weight": 1
      },
      "item-9977": {
        "value": 7,
        "weight": 3
      },
      "item-9978": {
        "value": 8,
        "weight": 4
      },
      "item-9979": {
        "value": 5,
        "weight": 7
      },
      "item-9980": {
        "value": 9,
        "weight": 6
      },
      "item-9981": {
        "value": 3,
        "weight": 3
      },
      "item-9982": {
        "value": 7,
        "weight": 7
      },
      "item-9983": {
        "value": 9,
        "weight": 9
      },
      "item-9984": {
        "value": 6,
        "weight": 9
      },
      "item-9985": {
        "value": 3,
        "weight": 1
      },
      "item-9986": {
        "value": 8,
        "weight": 8
      },
      "item-9987": {
        "value": 6,
        "weight": 9
      },
      "item-9988": {
        "value": 4,
        "weight": 7
      },
      "item-9989": {
        "value": 2,
        "weight": 3
      },
      "item-9990": {
        "value": 2,
        "weight": 3
      },
      "item-9991": {
        "value": 4,
        "weight": 1
      },
      "item-9992": {
        "value": 4,
        "weight": 4
      },
      "item-9993": {
        "value": 9,
        "weight": 4
      },
      "item-9994": {
        "value": 5,
        "weight": 8
      },
      "item-9995": {
        "value": 2,
        "weight": 9
      },
      "item-9996": {
        "value": 3,
        "weight": 2
      },
      "item-9997": {
        "value": 6,
        "weight": 7
      },
      "item-9998": {
        "value": 7,
        "weight": 2
      },
      "item-9999": {
        "value": 5,
        "weight": 3
      },
      "item-10000": {
        "value": 1,
        "weight": 9
      },
      "item-10001": {
        "value": 3,
        "weight": 9
      },
      "item-10002": {
        "value": 5,
        "weight": 4
      },
      "item-10003": {
        "value": 1,
        "weight": 4
      },
      "item-10004": {
        "value": 8,
        "weight": 1
      },
      "item-10005": {
        "value": 1,
        "weight": 1
      },
      "item-10006": {
        "value": 8,
        "weight": 1
      },
      "item-10007": {
        "value": 4,
        "weight": 9
      },
      "item-10008": {
        "value": 5,
        "weight": 5
      },
      "item-10009": {
        "value": 5,
        "weight": 3
      },
      "item-10010": {
        "value": 6,
        "weight": 9
      },
      "item-10011": {
        "value": 4,
        "weight": 7
      },
      "item-10012": {
        "value": 1,
        "weight": 3
      },
      "item-10013": {
        "value": 6,
        "weight": 7
      },
      "item-10014": {
        "value": 4,
        "weight": 4
      },
      "item-10015": {
        "value": 2,
        "weight": 2
      },
      "item-10016": {
        "value": 5,
        "weight": 4
      },
      "item-10017": {
        "value": 6,
        "weight": 3
      },
      "item-10018": {
        "value": 5,
        "weight": 9
      },
      "item-10019": {
        "value": 7,
        "weight": 5
      },
      "item-10020": {
        "value": 5,
        "weight": 1
      },
      "item-10021": {
        "value": 4,
        "weight": 3
      },
      "item-10022": {
        "value": 6,
        "weight": 6
      },
      "item-10023": {
        "value": 3,
        "weight": 3
      },
      "item-10024": {
        "value": 6,
        "weight": 7
      },
      "item-10025": {
        "value": 4,
        "weight": 3
      },
      "item-10026": {
        "value": 7,
        "weight": 5
      },
      "item-10027": {
        "value": 7,
        "weight": 9
      },
      "item-10028": {
        "value": 5,
        "weight": 8
      },
      "item-10029": {
        "value": 5,
        "weight": 3
      },
      "item-10030": {
        "value": 3,
        "weight": 6
      },
      "item-10031": {
        "value": 2,
        "weight": 1
      },
      "item-10032": {
        "value": 3,
        "weight": 8
      },
      "item-10033": {
        "value": 8,
        "weight": 5
      },
      "item-10034": {
        "value": 2,
        "weight": 8
      },
      "item-10035": {
        "value": 1,
        "weight": 2
      },
      "item-10036": {
        "value": 8,
        "weight": 9
      },
      "item-10037": {
        "value": 3,
        "weight": 1
      },
      "item-10038": {
        "value": 7,
        "weight": 3
      },
      "item-10039": {
        "value": 4,
        "weight": 9
      },
      "item-10040": {
        "value": 3,
        "weight": 6
      },
      "item-10041": {
        "value": 6,
        "weight": 9
      },
      "item-10042": {
        "value": 3,
        "weight": 7
      },
      "item-10043": {
        "value": 5,
        "weight": 5
      },
      "item-10044": {
        "value": 7,
        "weight": 9
      },
      "item-10045": {
        "value": 9,
        "weight": 5
      },
      "item-10046": {
        "value": 2,
        "weight": 8
      },
      "item-10047": {
        "value": 4,
        "weight": 1
      },
      "item-10048": {
        "value": 5,
        "weight": 4
      },
      "item-10049": {
        "value": 4,
        "weight": 3
      },
      "item-10050": {
        "value": 2,
        "weight": 5
      },
      "item-10051": {
        "value": 3,
        "weight": 5
      },
      "item-10052": {
        "value": 9,
        "weight": 9
      },
      "item-10053": {
        "value": 5,
        "weight": 9
      },
      "item-10054": {
        "value": 6,
        "weight": 4
      },
      "item-10055": {
        "value": 9,
        "weight": 5
      },
      "item-10056": {
        "value": 1,
        "weight": 6
      },
      "item-10057": {
        "value": 1,
        "weight": 6
      },
      "item-10058": {
        "value": 4,
        "weight": 6
      },
      "item-10059": {
        "value": 5,
        "weight": 6
      },
      "item-10060": {
        "value": 9,
        "weight": 1
      },
      "item-10061": {
        "value": 2,
        "weight": 9
      },
      "item-10062": {
        "value": 7,
        "weight": 7
      },
      "item-10063": {
        "value": 8,
        "weight": 3
      },
      "item-10064": {
        "value": 9,
        "weight": 1
      },
      "item-10065": {
        "value": 9,
        "weight": 5
      },
      "item-10066": {
        "value": 9,
        "weight": 5
      },
      "item-10067": {
        "value": 8,
        "weight": 7
      },
      "item-10068": {
        "value": 6,
        "weight": 4
      },
      "item-10069": {
        "value": 4,
        "weight": 3
      },
      "item-10070": {
        "value": 5,
        "weight": 5
      },
      "item-10071": {
        "value": 6,
        "weight": 8
      },
      "item-10072": {
        "value": 6,
        "weight": 5
      },
      "item-10073": {
        "value": 7,
        "weight": 8
      },
      "item-10074": {
        "value": 2,
        "weight": 3
      },
      "item-10075": {
        "value": 8,
        "weight": 2
      },
      "item-10076": {
        "value": 4,
        "weight": 9
      },
      "item-10077": {
        "value": 8,
        "weight": 3
      },
      "item-10078": {
        "value": 8,
        "weight": 9
      },
      "item-10079": {
        "value": 5,
        "weight": 8
      },
      "item-10080": {
        "value": 8,
        "weight": 1
      },
      "item-10081": {
        "value": 9,
        "weight": 9
      },
      "item-10082": {
        "value": 1,
        "weight": 4
      },
      "item-10083": {
        "value": 4,
        "weight": 2
      },
      "item-10084": {
        "value": 9,
        "weight": 3
      },
      "item-10085": {
        "value": 8,
        "weight": 4
      },
      "item-10086": {
        "value": 9,
        "weight": 5
      },
      "item-10087": {
        "value": 2,
        "weight": 2
      },
      "item-10088": {
        "value": 9,
        "weight": 6
      },
      "item-10089": {
        "value": 2,
        "weight": 8
      },
      "item-10090": {
        "value": 8,
        "weight": 6
      },
      "item-10091": {
        "value": 7,
        "weight": 3
      },
      "item-10092": {
        "value": 3,
        "weight": 7
      },
      "item-10093": {
        "value": 8,
        "weight": 5
      },
      "item-10094": {
        "value": 4,
        "weight": 8
      },
      "item-10095": {
        "value": 3,
        "weight": 4
      },
      "item-10096": {
        "value": 2,
        "weight": 7
      },
      "item-10097": {
        "value": 5,
        "weight": 2
      },
      "item-10098": {
        "value": 5,
        "weight": 9
      },
      "item-10099": {
        "value": 8,
        "weight": 4
      },
      "item-10100": {
        "value": 6,
        "weight": 7
      },
      "item-10101": {
        "value": 8,
        "weight": 2
      },
      "item-10102": {
        "value": 7,
        "weight": 5
      },
      "item-10103": {
        "value": 1,
        "weight": 4
      },
      "item-10104": {
        "value": 9,
        "weight": 8
      },
      "item-10105": {
        "value": 9,
        "weight": 3
      },
      "item-10106": {
        "value": 9,
        "weight": 8
      },
      "item-10107": {
        "value": 7,
        "weight": 7
      },
      "item-10108": {
        "value": 8,
        "weight": 4
      },
      "item-10109": {
        "value": 7,
        "weight": 3
      },
      "item-10110": {
        "value": 3,
        "weight": 3
      },
      "item-10111": {
        "value": 6,
        "weight": 6
      },
      "item-10112": {
        "value": 9,
        "weight": 8
      },
      "item-10113": {
        "value": 8,
        "weight": 9
      },
      "item-10114": {
        "value": 5,
        "weight": 8
      },
      "item-10115": {
        "value": 3,
        "weight": 6
      },
      "item-10116": {
        "value": 2,
        "weight": 6
      },
      "item-10117": {
        "value": 1,
        "weight": 4
      },
      "item-10118": {
        "value": 7,
        "weight": 4
      },
      "item-10119": {
        "value": 7,
        "weight": 1
      },
      "item-10120": {
        "value": 6,
        "weight": 3
      },
      "item-10121": {
        "value": 1,
        "weight": 9
      },
      "item-10122": {
        "value": 8,
        "weight": 6
      },
      "item-10123": {
        "value": 8,
        "weight": 8
      },
      "item-10124": {
        "value": 7,
        "weight": 3
      },
      "item-10125": {
        "value": 5,
        "weight": 1
      },
      "item-10126": {
        "value": 2,
        "weight": 8
      },
      "item-10127": {
        "value": 3,
        "weight": 1
      },
      "item-10128": {
        "value": 6,
        "weight": 5
      },
      "item-10129": {
        "value": 6,
        "weight": 5
      },
      "item-10130": {
        "value": 8,
        "weight": 3
      },
      "item-10131": {
        "value": 6,
        "weight": 1
      },
      "item-10132": {
        "value": 4,
        "weight": 3
      },
      "item-10133": {
        "value": 3,
        "weight": 4
      },
      "item-10134": {
        "value": 4,
        "weight": 2
      },
      "item-10135": {
        "value": 9,
        "weight": 3
      },
      "item-10136": {
        "value": 4,
        "weight": 5
      },
      "item-10137": {
        "value": 5,
        "weight": 8
      },
      "item-10138": {
        "value": 9,
        "weight": 8
      },
      "item-10139": {
        "value": 4,
        "weight": 1
      },
      "item-10140": {
        "value": 7,
        "weight": 3
      },
      "item-10141": {
        "value": 9,
        "weight": 4
      },
      "item-10142": {
        "value": 9,
        "weight": 1
      },
      "item-10143": {
        "value": 9,
        "weight": 3
      },
      "item-10144": {
        "value": 8,
        "weight": 9
      },
      "item-10145": {
        "value": 8,
        "weight": 1
      },
      "item-10146": {
        "value": 2,
        "weight": 3
      },
      "item-10147": {
        "value": 6,
        "weight": 1
      },
      "item-10148": {
        "value": 5,
        "weight": 7
      },
      "item-10149": {
        "value": 5,
        "weight": 9
      },
      "item-10150": {
        "value": 1,
        "weight": 3
      },
      "item-10151": {
        "value": 5,
        "weight": 9
      },
      "item-10152": {
        "value": 6,
        "weight": 6
      },
      "item-10153": {
        "value": 6,
        "weight": 4
      },
      "item-10154": {
        "value": 5,
        "weight": 6
      },
      "item-10155": {
        "value": 8,
        "weight": 6
      },
      "item-10156": {
        "value": 2,
        "weight": 6
      },
      "item-10157": {
        "value": 1,
        "weight": 4
      },
      "item-10158": {
        "value": 2,
        "weight": 7
      },
      "item-10159": {
        "value": 3,
        "weight": 5
      },
      "item-10160": {
        "value": 6,
        "weight": 4
      },
      "item-10161": {
        "value": 1,
        "weight": 9
      },
      "item-10162": {
        "value": 8,
        "weight": 3
      },
      "item-10163": {
        "value": 4,
        "weight": 9
      },
      "item-10164": {
        "value": 5,
        "weight": 3
      },
      "item-10165": {
        "value": 1,
        "weight": 6
      },
      "item-10166": {
        "value": 4,
        "weight": 3
      },
      "item-10167": {
        "value": 9,
        "weight": 8
      },
      "item-10168": {
        "value": 9,
        "weight": 8
      },
      "item-10169": {
        "value": 2,
        "weight": 6
      },
      "item-10170": {
        "value": 8,
        "weight": 1
      },
      "item-10171": {
        "value": 3,
        "weight": 3
      },
      "item-10172": {
        "value": 7,
        "weight": 4
      },
      "item-10173": {
        "value": 9,
        "weight": 9
      },
      "item-10174": {
        "value": 7,
        "weight": 1
      },
      "item-10175": {
        "value": 2,
        "weight": 1
      },
      "item-10176": {
        "value": 7,
        "weight": 7
      },
      "item-10177": {
        "value": 4,
        "weight": 3
      },
      "item-10178": {
        "value": 9,
        "weight": 1
      },
      "item-10179": {
        "value": 7,
        "weight": 9
      },
      "item-10180": {
        "value": 5,
        "weight": 3
      },
      "item-10181": {
        "value": 6,
        "weight": 2
      },
      "item-10182": {
        "value": 1,
        "weight": 1
      },
      "item-10183": {
        "value": 6,
        "weight": 6
      },
      "item-10184": {
        "value": 5,
        "weight": 9
      },
      "item-10185": {
        "value": 5,
        "weight": 9
      },
      "item-10186": {
        "value": 2,
        "weight": 6
      },
      "item-10187": {
        "value": 9,
        "weight": 6
      },
      "item-10188": {
        "value": 3,
        "weight": 9
      },
      "item-10189": {
        "value": 8,
        "weight": 8
      },
      "item-10190": {
        "value": 1,
        "weight": 4
      },
      "item-10191": {
        "value": 9,
        "weight": 2
      },
      "item-10192": {
        "value": 8,
        "weight": 5
      },
      "item-10193": {
        "value": 6,
        "weight": 8
      },
      "item-10194": {
        "value": 8,
        "weight": 3
      },
      "item-10195": {
        "value": 8,
        "weight": 5
      },
      "item-10196": {
        "value": 4,
        "weight": 1
      },
      "item-10197": {
        "value": 3,
        "weight": 3
      },
      "item-10198": {
        "value": 7,
        "weight": 9
      },
      "item-10199": {
        "value": 7,
        "weight": 6
      },
      "item-10200": {
        "value": 9,
        "weight": 2
      },
      "item-10201": {
        "value": 1,
        "weight": 2
      },
      "item-10202": {
        "value": 9,
        "weight": 2
      },
      "item-10203": {
        "value": 8,
        "weight": 3
      },
      "item-10204": {
        "value": 6,
        "weight": 7
      },
      "item-10205": {
        "value": 8,
        "weight": 2
      },
      "item-10206": {
        "value": 1,
        "weight": 2
      },
      "item-10207": {
        "value": 1,
        "weight": 4
      },
      "item-10208": {
        "value": 2,
        "weight": 6
      },
      "item-10209": {
        "value": 2,
        "weight": 7
      },
      "item-10210": {
        "value": 3,
        "weight": 7
      },
      "item-10211": {
        "value": 1,
        "weight": 1
      },
      "item-10212": {
        "value": 2,
        "weight": 2
      },
      "item-10213": {
        "value": 1,
        "weight": 5
      },
      "item-10214": {
        "value": 9,
        "weight": 8
      },
      "item-10215": {
        "value": 7,
        "weight": 6
      },
      "item-10216": {
        "value": 5,
        "weight": 1
      },
      "item-10217": {
        "value": 1,
        "weight": 2
      },
      "item-10218": {
        "value": 1,
        "weight": 9
      },
      "item-10219": {
        "value": 3,
        "weight": 7
      },
      "item-10220": {
        "value": 5,
        "weight": 8
      },
      "item-10221": {
        "value": 6,
        "weight": 1
      },
      "item-10222": {
        "value": 8,
        "weight": 4
      },
      "item-10223": {
        "value": 8,
        "weight": 6
      },
      "item-10224": {
        "value": 8,
        "weight": 1
      },
      "item-10225": {
        "value": 3,
        "weight": 3
      },
      "item-10226": {
        "value": 8,
        "weight": 6
      },
      "item-10227": {
        "value": 1,
        "weight": 1
      },
      "item-10228": {
        "value": 7,
        "weight": 6
      },
      "item-10229": {
        "value": 6,
        "weight": 2
      },
      "item-10230": {
        "value": 3,
        "weight": 7
      },
      "item-10231": {
        "value": 9,
        "weight": 9
      },
      "item-10232": {
        "value": 5,
        "weight": 9
      },
      "item-10233": {
        "value": 1,
        "weight": 5
      },
      "item-10234": {
        "value": 6,
        "weight": 7
      },
      "item-10235": {
        "value": 4,
        "weight": 5
      },
      "item-10236": {
        "value": 3,
        "weight": 1
      },
      "item-10237": {
        "value": 2,
        "weight": 1
      },
      "item-10238": {
        "value": 7,
        "weight": 7
      },
      "item-10239": {
        "value": 2,
        "weight": 9
      },
      "item-10240": {
        "value": 1,
        "weight": 8
      },
      "item-10241": {
        "value": 9,
        "weight": 5
      },
      "item-10242": {
        "value": 9,
        "weight": 7
      },
      "item-10243": {
        "value": 3,
        "weight": 1
      },
      "item-10244": {
        "value": 2,
        "weight": 9
      },
      "item-10245": {
        "value": 8,
        "weight": 7
      },
      "item-10246": {
        "value": 4,
        "weight": 3
      },
      "item-10247": {
        "value": 7,
        "weight": 3
      },
      "item-10248": {
        "value": 6,
        "weight": 3
      },
      "item-10249": {
        "value": 4,
        "weight": 3
      },
      "item-10250": {
        "value": 9,
        "weight": 6
      },
      "item-10251": {
        "value": 5,
        "weight": 7
      },
      "item-10252": {
        "value": 6,
        "weight": 7
      },
      "item-10253": {
        "value": 7,
        "weight": 4
      },
      "item-10254": {
        "value": 5,
        "weight": 2
      },
      "item-10255": {
        "value": 1,
        "weight": 4
      },
      "item-10256": {
        "value": 1,
        "weight": 3
      },
      "item-10257": {
        "value": 2,
        "weight": 4
      },
      "item-10258": {
        "value": 7,
        "weight": 9
      },
      "item-10259": {
        "value": 2,
        "weight": 9
      },
      "item-10260": {
        "value": 6,
        "weight": 1
      },
      "item-10261": {
        "value": 1,
        "weight": 5
      },
      "item-10262": {
        "value": 8,
        "weight": 9
      },
      "item-10263": {
        "value": 7,
        "weight": 6
      },
      "item-10264": {
        "value": 7,
        "weight": 5
      },
      "item-10265": {
        "value": 9,
        "weight": 4
      },
      "item-10266": {
        "value": 3,
        "weight": 7
      },
      "item-10267": {
        "value": 6,
        "weight": 6
      },
      "item-10268": {
        "value": 6,
        "weight": 8
      },
      "item-10269": {
        "value": 2,
        "weight": 9
      },
      "item-10270": {
        "value": 1,
        "weight": 2
      },
      "item-10271": {
        "value": 7,
        "weight": 7
      },
      "item-10272": {
        "value": 4,
        "weight": 3
      },
      "item-10273": {
        "value": 5,
        "weight": 6
      },
      "item-10274": {
        "value": 3,
        "weight": 2
      },
      "item-10275": {
        "value": 4,
        "weight": 5
      },
      "item-10276": {
        "value": 6,
        "weight": 4
      },
      "item-10277": {
        "value": 5,
        "weight": 1
      },
      "item-10278": {
        "value": 8,
        "weight": 3
      },
      "item-10279": {
        "value": 3,
        "weight": 4
      },
      "item-10280": {
        "value": 6,
        "weight": 4
      },
      "item-10281": {
        "value": 2,
        "weight": 7
      },
      "item-10282": {
        "value": 7,
        "weight": 9
      },
      "item-10283": {
        "value": 8,
        "weight": 1
      },
      "item-10284": {
        "value": 1,
        "weight": 6
      },
      "item-10285": {
        "value": 8,
        "weight": 4
      },
      "item-10286": {
        "value": 6,
        "weight": 7
      },
      "item-10287": {
        "value": 1,
        "weight": 3
      },
      "item-10288": {
        "value": 1,
        "weight": 5
      },
      "item-10289": {
        "value": 5,
        "weight": 2
      },
      "item-10290": {
        "value": 4,
        "weight": 5
      },
      "item-10291": {
        "value": 8,
        "weight": 4
      },
      "item-10292": {
        "value": 8,
        "weight": 6
      },
      "item-10293": {
        "value": 8,
        "weight": 7
      },
      "item-10294": {
        "value": 3,
        "weight": 4
      },
      "item-10295": {
        "value": 5,
        "weight": 5
      },
      "item-10296": {
        "value": 9,
        "weight": 1
      },
      "item-10297": {
        "value": 1,
        "weight": 7
      },
      "item-10298": {
        "value": 5,
        "weight": 8
      },
      "item-10299": {
        "value": 1,
        "weight": 5
      },
      "item-10300": {
        "value": 3,
        "weight": 4
      },
      "item-10301": {
        "value": 3,
        "weight": 2
      },
      "item-10302": {
        "value": 6,
        "weight": 6
      },
      "item-10303": {
        "value": 5,
        "weight": 3
      },
      "item-10304": {
        "value": 6,
        "weight": 5
      },
      "item-10305": {
        "value": 7,
        "weight": 5
      },
      "item-10306": {
        "value": 7,
        "weight": 4
      },
      "item-10307": {
        "value": 8,
        "weight": 4
      },
      "item-10308": {
        "value": 6,
        "weight": 3
      },
      "item-10309": {
        "value": 1,
        "weight": 7
      },
      "item-10310": {
        "value": 6,
        "weight": 7
      },
      "item-10311": {
        "value": 3,
        "weight": 3
      },
      "item-10312": {
        "value": 3,
        "weight": 5
      },
      "item-10313": {
        "value": 2,
        "weight": 6
      },
      "item-10314": {
        "value": 3,
        "weight": 6
      },
      "item-10315": {
        "value": 8,
        "weight": 3
      },
      "item-10316": {
        "value": 6,
        "weight": 9
      },
      "item-10317": {
        "value": 5,
        "weight": 5
      },
      "item-10318": {
        "value": 8,
        "weight": 1
      },
      "item-10319": {
        "value": 9,
        "weight": 2
      },
      "item-10320": {
        "value": 8,
        "weight": 6
      },
      "item-10321": {
        "value": 8,
        "weight": 7
      },
      "item-10322": {
        "value": 8,
        "weight": 6
      },
      "item-10323": {
        "value": 7,
        "weight": 3
      },
      "item-10324": {
        "value": 1,
        "weight": 2
      },
      "item-10325": {
        "value": 7,
        "weight": 2
      },
      "item-10326": {
        "value": 6,
        "weight": 6
      },
      "item-10327": {
        "value": 9,
        "weight": 5
      },
      "item-10328": {
        "value": 6,
        "weight": 7
      },
      "item-10329": {
        "value": 8,
        "weight": 1
      },
      "item-10330": {
        "value": 9,
        "weight": 9
      },
      "item-10331": {
        "value": 9,
        "weight": 4
      },
      "item-10332": {
        "value": 8,
        "weight": 3
      },
      "item-10333": {
        "value": 4,
        "weight": 4
      },
      "item-10334": {
        "value": 4,
        "weight": 9
      },
      "item-10335": {
        "value": 6,
        "weight": 5
      },
      "item-10336": {
        "value": 7,
        "weight": 3
      },
      "item-10337": {
        "value": 7,
        "weight": 8
      },
      "item-10338": {
        "value": 2,
        "weight": 5
      },
      "item-10339": {
        "value": 7,
        "weight": 6
      },
      "item-10340": {
        "value": 7,
        "weight": 2
      },
      "item-10341": {
        "value": 2,
        "weight": 8
      },
      "item-10342": {
        "value": 6,
        "weight": 4
      },
      "item-10343": {
        "value": 8,
        "weight": 8
      },
      "item-10344": {
        "value": 6,
        "weight": 7
      },
      "item-10345": {
        "value": 8,
        "weight": 7
      },
      "item-10346": {
        "value": 4,
        "weight": 8
      },
      "item-10347": {
        "value": 2,
        "weight": 3
      },
      "item-10348": {
        "value": 2,
        "weight": 4
      },
      "item-10349": {
        "value": 8,
        "weight": 4
      },
      "item-10350": {
        "value": 3,
        "weight": 5
      },
      "item-10351": {
        "value": 3,
        "weight": 3
      },
      "item-10352": {
        "value": 8,
        "weight": 4
      },
      "item-10353": {
        "value": 1,
        "weight": 8
      },
      "item-10354": {
        "value": 9,
        "weight": 9
      },
      "item-10355": {
        "value": 9,
        "weight": 6
      },
      "item-10356": {
        "value": 1,
        "weight": 8
      },
      "item-10357": {
        "value": 9,
        "weight": 7
      },
      "item-10358": {
        "value": 5,
        "weight": 5
      },
      "item-10359": {
        "value": 5,
        "weight": 3
      },
      "item-10360": {
        "value": 3,
        "weight": 7
      },
      "item-10361": {
        "value": 4,
        "weight": 8
      },
      "item-10362": {
        "value": 6,
        "weight": 5
      },
      "item-10363": {
        "value": 2,
        "weight": 5
      },
      "item-10364": {
        "value": 2,
        "weight": 4
      },
      "item-10365": {
        "value": 8,
        "weight": 7
      },
      "item-10366": {
        "value": 3,
        "weight": 6
      },
      "item-10367": {
        "value": 3,
        "weight": 6
      },
      "item-10368": {
        "value": 6,
        "weight": 9
      },
      "item-10369": {
        "value": 8,
        "weight": 7
      },
      "item-10370": {
        "value": 8,
        "weight": 1
      },
      "item-10371": {
        "value": 9,
        "weight": 6
      },
      "item-10372": {
        "value": 2,
        "weight": 3
      },
      "item-10373": {
        "value": 3,
        "weight": 3
      },
      "item-10374": {
        "value": 7,
        "weight": 7
      },
      "item-10375": {
        "value": 2,
        "weight": 8
      },
      "item-10376": {
        "value": 4,
        "weight": 8
      },
      "item-10377": {
        "value": 2,
        "weight": 7
      },
      "item-10378": {
        "value": 6,
        "weight": 1
      },
      "item-10379": {
        "value": 7,
        "weight": 5
      },
      "item-10380": {
        "value": 1,
        "weight": 1
      },
      "item-10381": {
        "value": 5,
        "weight": 2
      },
      "item-10382": {
        "value": 3,
        "weight": 8
      },
      "item-10383": {
        "value": 6,
        "weight": 4
      },
      "item-10384": {
        "value": 6,
        "weight": 8
      },
      "item-10385": {
        "value": 7,
        "weight": 7
      },
      "item-10386": {
        "value": 7,
        "weight": 1
      },
      "item-10387": {
        "value": 9,
        "weight": 3
      },
      "item-10388": {
        "value": 5,
        "weight": 9
      },
      "item-10389": {
        "value": 1,
        "weight": 8
      },
      "item-10390": {
        "value": 3,
        "weight": 7
      },
      "item-10391": {
        "value": 3,
        "weight": 4
      },
      "item-10392": {
        "value": 9,
        "weight": 4
      },
      "item-10393": {
        "value": 5,
        "weight": 3
      },
      "item-10394": {
        "value": 2,
        "weight": 1
      },
      "item-10395": {
        "value": 4,
        "weight": 3
      },
      "item-10396": {
        "value": 9,
        "weight": 2
      },
      "item-10397": {
        "value": 3,
        "weight": 2
      },
      "item-10398": {
        "value": 2,
        "weight": 1
      },
      "item-10399": {
        "value": 1,
        "weight": 2
      },
      "item-10400": {
        "value": 5,
        "weight": 3
      },
      "item-10401": {
        "value": 7,
        "weight": 7
      },
      "item-10402": {
        "value": 2,
        "weight": 9
      },
      "item-10403": {
        "value": 9,
        "weight": 4
      },
      "item-10404": {
        "value": 4,
        "weight": 4
      },
      "item-10405": {
        "value": 7,
        "weight": 5
      },
      "item-10406": {
        "value": 9,
        "weight": 4
      },
      "item-10407": {
        "value": 3,
        "weight": 1
      },
      "item-10408": {
        "value": 9,
        "weight": 6
      },
      "item-10409": {
        "value": 5,
        "weight": 3
      },
      "item-10410": {
        "value": 3,
        "weight": 1
      },
      "item-10411": {
        "value": 2,
        "weight": 2
      },
      "item-10412": {
        "value": 9,
        "weight": 6
      },
      "item-10413": {
        "value": 8,
        "weight": 4
      },
      "item-10414": {
        "value": 1,
        "weight": 6
      },
      "item-10415": {
        "value": 9,
        "weight": 5
      },
      "item-10416": {
        "value": 2,
        "weight": 1
      },
      "item-10417": {
        "value": 2,
        "weight": 3
      },
      "item-10418": {
        "value": 3,
        "weight": 2
      },
      "item-10419": {
        "value": 5,
        "weight": 3
      },
      "item-10420": {
        "value": 6,
        "weight": 4
      },
      "item-10421": {
        "value": 7,
        "weight": 2
      },
      "item-10422": {
        "value": 7,
        "weight": 7
      },
      "item-10423": {
        "value": 6,
        "weight": 9
      },
      "item-10424": {
        "value": 1,
        "weight": 4
      },
      "item-10425": {
        "value": 5,
        "weight": 5
      },
      "item-10426": {
        "value": 5,
        "weight": 9
      },
      "item-10427": {
        "value": 9,
        "weight": 4
      },
      "item-10428": {
        "value": 5,
        "weight": 9
      },
      "item-10429": {
        "value": 9,
        "weight": 4
      },
      "item-10430": {
        "value": 4,
        "weight": 3
      },
      "item-10431": {
        "value": 6,
        "weight": 1
      },
      "item-10432": {
        "value": 1,
        "weight": 9
      },
      "item-10433": {
        "value": 7,
        "weight": 2
      },
      "item-10434": {
        "value": 1,
        "weight": 2
      },
      "item-10435": {
        "value": 4,
        "weight": 6
      },
      "item-10436": {
        "value": 1,
        "weight": 2
      },
      "item-10437": {
        "value": 9,
        "weight": 4
      },
      "item-10438": {
        "value": 3,
        "weight": 9
      },
      "item-10439": {
        "value": 8,
        "weight": 2
      },
      "item-10440": {
        "value": 9,
        "weight": 3
      },
      "item-10441": {
        "value": 8,
        "weight": 4
      },
      "item-10442": {
        "value": 6,
        "weight": 9
      },
      "item-10443": {
        "value": 6,
        "weight": 2
      },
      "item-10444": {
        "value": 1,
        "weight": 4
      },
      "item-10445": {
        "value": 7,
        "weight": 2
      },
      "item-10446": {
        "value": 9,
        "weight": 8
      },
      "item-10447": {
        "value": 1,
        "weight": 7
      },
      "item-10448": {
        "value": 4,
        "weight": 9
      },
      "item-10449": {
        "value": 1,
        "weight": 5
      },
      "item-10450": {
        "value": 9,
        "weight": 8
      },
      "item-10451": {
        "value": 6,
        "weight": 7
      },
      "item-10452": {
        "value": 7,
        "weight": 1
      },
      "item-10453": {
        "value": 1,
        "weight": 2
      },
      "item-10454": {
        "value": 2,
        "weight": 9
      },
      "item-10455": {
        "value": 5,
        "weight": 7
      },
      "item-10456": {
        "value": 1,
        "weight": 5
      },
      "item-10457": {
        "value": 4,
        "weight": 3
      },
      "item-10458": {
        "value": 7,
        "weight": 5
      },
      "item-10459": {
        "value": 4,
        "weight": 5
      },
      "item-10460": {
        "value": 1,
        "weight": 6
      },
      "item-10461": {
        "value": 2,
        "weight": 1
      },
      "item-10462": {
        "value": 7,
        "weight": 4
      },
      "item-10463": {
        "value": 2,
        "weight": 6
      },
      "item-10464": {
        "value": 3,
        "weight": 1
      },
      "item-10465": {
        "value": 8,
        "weight": 4
      },
      "item-10466": {
        "value": 2,
        "weight": 6
      },
      "item-10467": {
        "value": 8,
        "weight": 3
      },
      "item-10468": {
        "value": 1,
        "weight": 8
      },
      "item-10469": {
        "value": 5,
        "weight": 5
      },
      "item-10470": {
        "value": 1,
        "weight": 1
      },
      "item-10471": {
        "value": 5,
        "weight": 9
      },
      "item-10472": {
        "value": 7,
        "weight": 5
      },
      "item-10473": {
        "value": 8,
        "weight": 8
      },
      "item-10474": {
        "value": 1,
        "weight": 2
      },
      "item-10475": {
        "value": 4,
        "weight": 6
      },
      "item-10476": {
        "value": 4,
        "weight": 1
      },
      "item-10477": {
        "value": 9,
        "weight": 4
      },
      "item-10478": {
        "value": 9,
        "weight": 3
      },
      "item-10479": {
        "value": 3,
        "weight": 9
      },
      "item-10480": {
        "value": 8,
        "weight": 7
      },
      "item-10481": {
        "value": 4,
        "weight": 6
      },
      "item-10482": {
        "value": 7,
        "weight": 9
      },
      "item-10483": {
        "value": 1,
        "weight": 6
      },
      "item-10484": {
        "value": 6,
        "weight": 7
      },
      "item-10485": {
        "value": 6,
        "weight": 4
      },
      "item-10486": {
        "value": 3,
        "weight": 1
      },
      "item-10487": {
        "value": 7,
        "weight": 5
      },
      "item-10488": {
        "value": 5,
        "weight": 5
      },
      "item-10489": {
        "value": 1,
        "weight": 4
      },
      "item-10490": {
        "value": 9,
        "weight": 6
      },
      "item-10491": {
        "value": 8,
        "weight": 5
      },
      "item-10492": {
        "value": 9,
        "weight": 9
      },
      "item-10493": {
        "value": 1,
        "weight": 5
      },
      "item-10494": {
        "value": 3,
        "weight": 6
      },
      "item-10495": {
        "value": 3,
        "weight": 2
      },
      "item-10496": {
        "value": 8,
        "weight": 5
      },
      "item-10497": {
        "value": 3,
        "weight": 7
      },
      "item-10498": {
        "value": 3,
        "weight": 9
      },
      "item-10499": {
        "value": 9,
        "weight": 6
      },
      "item-10500": {
        "value": 4,
        "weight": 5
      },
      "item-10501": {
        "value": 8,
        "weight": 5
      },
      "item-10502": {
        "value": 2,
        "weight": 3
      },
      "item-10503": {
        "value": 2,
        "weight": 6
      },
      "item-10504": {
        "value": 7,
        "weight": 9
      },
      "item-10505": {
        "value": 6,
        "weight": 1
      },
      "item-10506": {
        "value": 8,
        "weight": 7
      },
      "item-10507": {
        "value": 8,
        "weight": 9
      },
      "item-10508": {
        "value": 1,
        "weight": 1
      },
      "item-10509": {
        "value": 9,
        "weight": 9
      },
      "item-10510": {
        "value": 9,
        "weight": 7
      },
      "item-10511": {
        "value": 7,
        "weight": 1
      },
      "item-10512": {
        "value": 7,
        "weight": 4
      },
      "item-10513": {
        "value": 5,
        "weight": 5
      },
      "item-10514": {
        "value": 3,
        "weight": 4
      },
      "item-10515": {
        "value": 6,
        "weight": 1
      },
      "item-10516": {
        "value": 6,
        "weight": 6
      },
      "item-10517": {
        "value": 2,
        "weight": 2
      },
      "item-10518": {
        "value": 9,
        "weight": 3
      },
      "item-10519": {
        "value": 1,
        "weight": 3
      },
      "item-10520": {
        "value": 6,
        "weight": 2
      },
      "item-10521": {
        "value": 2,
        "weight": 8
      },
      "item-10522": {
        "value": 7,
        "weight": 5
      },
      "item-10523": {
        "value": 4,
        "weight": 2
      },
      "item-10524": {
        "value": 7,
        "weight": 3
      },
      "item-10525": {
        "value": 6,
        "weight": 1
      },
      "item-10526": {
        "value": 7,
        "weight": 5
      },
      "item-10527": {
        "value": 6,
        "weight": 1
      },
      "item-10528": {
        "value": 1,
        "weight": 5
      },
      "item-10529": {
        "value": 1,
        "weight": 5
      },
      "item-10530": {
        "value": 9,
        "weight": 1
      },
      "item-10531": {
        "value": 8,
        "weight": 6
      },
      "item-10532": {
        "value": 9,
        "weight": 7
      },
      "item-10533": {
        "value": 3,
        "weight": 4
      },
      "item-10534": {
        "value": 3,
        "weight": 3
      },
      "item-10535": {
        "value": 8,
        "weight": 6
      },
      "item-10536": {
        "value": 9,
        "weight": 6
      },
      "item-10537": {
        "value": 2,
        "weight": 4
      },
      "item-10538": {
        "value": 4,
        "weight": 6
      },
      "item-10539": {
        "value": 9,
        "weight": 9
      },
      "item-10540": {
        "value": 3,
        "weight": 6
      },
      "item-10541": {
        "value": 8,
        "weight": 9
      },
      "item-10542": {
        "value": 1,
        "weight": 8
      },
      "item-10543": {
        "value": 1,
        "weight": 7
      },
      "item-10544": {
        "value": 3,
        "weight": 5
      },
      "item-10545": {
        "value": 1,
        "weight": 7
      },
      "item-10546": {
        "value": 3,
        "weight": 9
      },
      "item-10547": {
        "value": 3,
        "weight": 8
      },
      "item-10548": {
        "value": 7,
        "weight": 4
      },
      "item-10549": {
        "value": 5,
        "weight": 4
      },
      "item-10550": {
        "value": 3,
        "weight": 6
      },
      "item-10551": {
        "value": 4,
        "weight": 4
      },
      "item-10552": {
        "value": 1,
        "weight": 4
      },
      "item-10553": {
        "value": 4,
        "weight": 2
      },
      "item-10554": {
        "value": 3,
        "weight": 5
      },
      "item-10555": {
        "value": 1,
        "weight": 9
      },
      "item-10556": {
        "value": 7,
        "weight": 3
      },
      "item-10557": {
        "value": 3,
        "weight": 7
      },
      "item-10558": {
        "value": 7,
        "weight": 8
      },
      "item-10559": {
        "value": 8,
        "weight": 8
      },
      "item-10560": {
        "value": 6,
        "weight": 4
      },
      "item-10561": {
        "value": 7,
        "weight": 4
      },
      "item-10562": {
        "value": 1,
        "weight": 3
      },
      "item-10563": {
        "value": 8,
        "weight": 9
      },
      "item-10564": {
        "value": 7,
        "weight": 6
      },
      "item-10565": {
        "value": 1,
        "weight": 7
      },
      "item-10566": {
        "value": 4,
        "weight": 5
      },
      "item-10567": {
        "value": 1,
        "weight": 6
      },
      "item-10568": {
        "value": 9,
        "weight": 4
      },
      "item-10569": {
        "value": 2,
        "weight": 2
      },
      "item-10570": {
        "value": 4,
        "weight": 8
      },
      "item-10571": {
        "value": 8,
        "weight": 3
      },
      "item-10572": {
        "value": 9,
        "weight": 5
      },
      "item-10573": {
        "value": 1,
        "weight": 7
      },
      "item-10574": {
        "value": 8,
        "weight": 1
      },
      "item-10575": {
        "value": 7,
        "weight": 6
      },
      "item-10576": {
        "value": 3,
        "weight": 2
      },
      "item-10577": {
        "value": 1,
        "weight": 1
      },
      "item-10578": {
        "value": 2,
        "weight": 9
      },
      "item-10579": {
        "value": 9,
        "weight": 9
      },
      "item-10580": {
        "value": 3,
        "weight": 1
      },
      "item-10581": {
        "value": 2,
        "weight": 3
      },
      "item-10582": {
        "value": 9,
        "weight": 8
      },
      "item-10583": {
        "value": 8,
        "weight": 4
      },
      "item-10584": {
        "value": 5,
        "weight": 9
      },
      "item-10585": {
        "value": 9,
        "weight": 3
      },
      "item-10586": {
        "value": 5,
        "weight": 3
      },
      "item-10587": {
        "value": 9,
        "weight": 8
      },
      "item-10588": {
        "value": 4,
        "weight": 3
      },
      "item-10589": {
        "value": 9,
        "weight": 1
      },
      "item-10590": {
        "value": 5,
        "weight": 3
      },
      "item-10591": {
        "value": 6,
        "weight": 6
      },
      "item-10592": {
        "value": 3,
        "weight": 1
      },
      "item-10593": {
        "value": 2,
        "weight": 1
      },
      "item-10594": {
        "value": 7,
        "weight": 1
      },
      "item-10595": {
        "value": 2,
        "weight": 4
      },
      "item-10596": {
        "value": 3,
        "weight": 5
      },
      "item-10597": {
        "value": 2,
        "weight": 1
      },
      "item-10598": {
        "value": 3,
        "weight": 4
      },
      "item-10599": {
        "value": 5,
        "weight": 8
      },
      "item-10600": {
        "value": 4,
        "weight": 8
      },
      "item-10601": {
        "value": 3,
        "weight": 9
      },
      "item-10602": {
        "value": 6,
        "weight": 5
      },
      "item-10603": {
        "value": 1,
        "weight": 7
      },
      "item-10604": {
        "value": 2,
        "weight": 2
      },
      "item-10605": {
        "value": 9,
        "weight": 6
      },
      "item-10606": {
        "value": 4,
        "weight": 4
      },
      "item-10607": {
        "value": 7,
        "weight": 7
      },
      "item-10608": {
        "value": 5,
        "weight": 7
      },
      "item-10609": {
        "value": 9,
        "weight": 5
      },
      "item-10610": {
        "value": 9,
        "weight": 1
      },
      "item-10611": {
        "value": 8,
        "weight": 1
      },
      "item-10612": {
        "value": 7,
        "weight": 9
      },
      "item-10613": {
        "value": 8,
        "weight": 3
      },
      "item-10614": {
        "value": 8,
        "weight": 1
      },
      "item-10615": {
        "value": 5,
        "weight": 7
      },
      "item-10616": {
        "value": 3,
        "weight": 1
      },
      "item-10617": {
        "value": 4,
        "weight": 6
      },
      "item-10618": {
        "value": 4,
        "weight": 2
      },
      "item-10619": {
        "value": 4,
        "weight": 8
      },
      "item-10620": {
        "value": 2,
        "weight": 2
      },
      "item-10621": {
        "value": 6,
        "weight": 4
      },
      "item-10622": {
        "value": 9,
        "weight": 6
      },
      "item-10623": {
        "value": 8,
        "weight": 7
      },
      "item-10624": {
        "value": 3,
        "weight": 8
      },
      "item-10625": {
        "value": 6,
        "weight": 3
      },
      "item-10626": {
        "value": 6,
        "weight": 3
      },
      "item-10627": {
        "value": 7,
        "weight": 5
      },
      "item-10628": {
        "value": 2,
        "weight": 4
      },
      "item-10629": {
        "value": 6,
        "weight": 7
      },
      "item-10630": {
        "value": 9,
        "weight": 9
      },
      "item-10631": {
        "value": 3,
        "weight": 4
      },
      "item-10632": {
        "value": 9,
        "weight": 3
      },
      "item-10633": {
        "value": 8,
        "weight": 3
      },
      "item-10634": {
        "value": 9,
        "weight": 9
      },
      "item-10635": {
        "value": 1,
        "weight": 9
      },
      "item-10636": {
        "value": 2,
        "weight": 2
      },
      "item-10637": {
        "value": 4,
        "weight": 1
      },
      "item-10638": {
        "value": 4,
        "weight": 1
      },
      "item-10639": {
        "value": 2,
        "weight": 9
      },
      "item-10640": {
        "value": 8,
        "weight": 1
      },
      "item-10641": {
        "value": 6,
        "weight": 5
      },
      "item-10642": {
        "value": 9,
        "weight": 4
      },
      "item-10643": {
        "value": 8,
        "weight": 6
      },
      "item-10644": {
        "value": 4,
        "weight": 4
      },
      "item-10645": {
        "value": 9,
        "weight": 3
      },
      "item-10646": {
        "value": 1,
        "weight": 8
      },
      "item-10647": {
        "value": 5,
        "weight": 1
      },
      "item-10648": {
        "value": 2,
        "weight": 3
      },
      "item-10649": {
        "value": 1,
        "weight": 4
      },
      "item-10650": {
        "value": 9,
        "weight": 7
      },
      "item-10651": {
        "value": 4,
        "weight": 5
      },
      "item-10652": {
        "value": 9,
        "weight": 2
      },
      "item-10653": {
        "value": 3,
        "weight": 1
      },
      "item-10654": {
        "value": 2,
        "weight": 9
      },
      "item-10655": {
        "value": 7,
        "weight": 6
      },
      "item-10656": {
        "value": 5,
        "weight": 9
      },
      "item-10657": {
        "value": 9,
        "weight": 4
      },
      "item-10658": {
        "value": 5,
        "weight": 5
      },
      "item-10659": {
        "value": 8,
        "weight": 9
      },
      "item-10660": {
        "value": 3,
        "weight": 1
      },
      "item-10661": {
        "value": 5,
        "weight": 3
      },
      "item-10662": {
        "value": 6,
        "weight": 3
      },
      "item-10663": {
        "value": 2,
        "weight": 9
      },
      "item-10664": {
        "value": 4,
        "weight": 2
      },
      "item-10665": {
        "value": 2,
        "weight": 4
      },
      "item-10666": {
        "value": 2,
        "weight": 7
      },
      "item-10667": {
        "value": 4,
        "weight": 4
      },
      "item-10668": {
        "value": 9,
        "weight": 4
      },
      "item-10669": {
        "value": 8,
        "weight": 7
      },
      "item-10670": {
        "value": 3,
        "weight": 2
      },
      "item-10671": {
        "value": 5,
        "weight": 8
      },
      "item-10672": {
        "value": 2,
        "weight": 8
      },
      "item-10673": {
        "value": 1,
        "weight": 5
      },
      "item-10674": {
        "value": 6,
        "weight": 9
      },
      "item-10675": {
        "value": 2,
        "weight": 8
      },
      "item-10676": {
        "value": 3,
        "weight": 4
      },
      "item-10677": {
        "value": 3,
        "weight": 8
      },
      "item-10678": {
        "value": 4,
        "weight": 8
      },
      "item-10679": {
        "value": 1,
        "weight": 5
      },
      "item-10680": {
        "value": 6,
        "weight": 3
      },
      "item-10681": {
        "value": 4,
        "weight": 6
      },
      "item-10682": {
        "value": 9,
        "weight": 7
      },
      "item-10683": {
        "value": 2,
        "weight": 5
      },
      "item-10684": {
        "value": 3,
        "weight": 1
      },
      "item-10685": {
        "value": 2,
        "weight": 1
      },
      "item-10686": {
        "value": 7,
        "weight": 1
      },
      "item-10687": {
        "value": 6,
        "weight": 3
      },
      "item-10688": {
        "value": 2,
        "weight": 1
      },
      "item-10689": {
        "value": 3,
        "weight": 5
      },
      "item-10690": {
        "value": 6,
        "weight": 4
      },
      "item-10691": {
        "value": 6,
        "weight": 5
      },
      "item-10692": {
        "value": 6,
        "weight": 6
      },
      "item-10693": {
        "value": 8,
        "weight": 6
      },
      "item-10694": {
        "value": 7,
        "weight": 6
      },
      "item-10695": {
        "value": 1,
        "weight": 3
      },
      "item-10696": {
        "value": 9,
        "weight": 7
      },
      "item-10697": {
        "value": 1,
        "weight": 5
      },
      "item-10698": {
        "value": 8,
        "weight": 5
      },
      "item-10699": {
        "value": 2,
        "weight": 3
      },
      "item-10700": {
        "value": 9,
        "weight": 9
      },
      "item-10701": {
        "value": 6,
        "weight": 8
      },
      "item-10702": {
        "value": 4,
        "weight": 3
      },
      "item-10703": {
        "value": 1,
        "weight": 9
      },
      "item-10704": {
        "value": 6,
        "weight": 2
      },
      "item-10705": {
        "value": 8,
        "weight": 9
      },
      "item-10706": {
        "value": 7,
        "weight": 6
      },
      "item-10707": {
        "value": 8,
        "weight": 4
      },
      "item-10708": {
        "value": 3,
        "weight": 4
      },
      "item-10709": {
        "value": 5,
        "weight": 9
      },
      "item-10710": {
        "value": 5,
        "weight": 6
      },
      "item-10711": {
        "value": 9,
        "weight": 5
      },
      "item-10712": {
        "value": 1,
        "weight": 9
      },
      "item-10713": {
        "value": 7,
        "weight": 8
      },
      "item-10714": {
        "value": 9,
        "weight": 1
      },
      "item-10715": {
        "value": 4,
        "weight": 2
      },
      "item-10716": {
        "value": 7,
        "weight": 6
      },
      "item-10717": {
        "value": 6,
        "weight": 4
      },
      "item-10718": {
        "value": 7,
        "weight": 7
      },
      "item-10719": {
        "value": 1,
        "weight": 7
      },
      "item-10720": {
        "value": 5,
        "weight": 2
      },
      "item-10721": {
        "value": 9,
        "weight": 3
      },
      "item-10722": {
        "value": 1,
        "weight": 2
      },
      "item-10723": {
        "value": 8,
        "weight": 7
      },
      "item-10724": {
        "value": 5,
        "weight": 3
      },
      "item-10725": {
        "value": 2,
        "weight": 1
      },
      "item-10726": {
        "value": 4,
        "weight": 4
      },
      "item-10727": {
        "value": 8,
        "weight": 4
      },
      "item-10728": {
        "value": 9,
        "weight": 4
      },
      "item-10729": {
        "value": 1,
        "weight": 4
      },
      "item-10730": {
        "value": 7,
        "weight": 5
      },
      "item-10731": {
        "value": 7,
        "weight": 5
      },
      "item-10732": {
        "value": 3,
        "weight": 8
      },
      "item-10733": {
        "value": 3,
        "weight": 2
      },
      "item-10734": {
        "value": 9,
        "weight": 1
      },
      "item-10735": {
        "value": 2,
        "weight": 6
      },
      "item-10736": {
        "value": 2,
        "weight": 9
      },
      "item-10737": {
        "value": 6,
        "weight": 6
      },
      "item-10738": {
        "value": 4,
        "weight": 6
      },
      "item-10739": {
        "value": 1,
        "weight": 5
      },
      "item-10740": {
        "value": 7,
        "weight": 6
      },
      "item-10741": {
        "value": 2,
        "weight": 7
      },
      "item-10742": {
        "value": 2,
        "weight": 7
      },
      "item-10743": {
        "value": 4,
        "weight": 1
      },
      "item-10744": {
        "value": 8,
        "weight": 8
      },
      "item-10745": {
        "value": 2,
        "weight": 3
      },
      "item-10746": {
        "value": 7,
        "weight": 9
      },
      "item-10747": {
        "value": 9,
        "weight": 9
      },
      "item-10748": {
        "value": 8,
        "weight": 1
      },
      "item-10749": {
        "value": 3,
        "weight": 9
      },
      "item-10750": {
        "value": 1,
        "weight": 2
      },
      "item-10751": {
        "value": 8,
        "weight": 5
      },
      "item-10752": {
        "value": 2,
        "weight": 5
      },
      "item-10753": {
        "value": 4,
        "weight": 4
      },
      "item-10754": {
        "value": 2,
        "weight": 5
      },
      "item-10755": {
        "value": 8,
        "weight": 4
      },
      "item-10756": {
        "value": 6,
        "weight": 5
      },
      "item-10757": {
        "value": 8,
        "weight": 5
      },
      "item-10758": {
        "value": 1,
        "weight": 3
      },
      "item-10759": {
        "value": 5,
        "weight": 7
      },
      "item-10760": {
        "value": 5,
        "weight": 9
      },
      "item-10761": {
        "value": 3,
        "weight": 3
      },
      "item-10762": {
        "value": 4,
        "weight": 7
      },
      "item-10763": {
        "value": 7,
        "weight": 5
      },
      "item-10764": {
        "value": 9,
        "weight": 8
      },
      "item-10765": {
        "value": 7,
        "weight": 4
      },
      "item-10766": {
        "value": 8,
        "weight": 9
      },
      "item-10767": {
        "value": 8,
        "weight": 6
      },
      "item-10768": {
        "value": 3,
        "weight": 3
      },
      "item-10769": {
        "value": 7,
        "weight": 1
      },
      "item-10770": {
        "value": 5,
        "weight": 1
      },
      "item-10771": {
        "value": 8,
        "weight": 7
      },
      "item-10772": {
        "value": 9,
        "weight": 1
      },
      "item-10773": {
        "value": 8,
        "weight": 7
      },
      "item-10774": {
        "value": 7,
        "weight": 8
      },
      "item-10775": {
        "value": 7,
        "weight": 7
      },
      "item-10776": {
        "value": 4,
        "weight": 9
      },
      "item-10777": {
        "value": 5,
        "weight": 3
      },
      "item-10778": {
        "value": 1,
        "weight": 4
      },
      "item-10779": {
        "value": 7,
        "weight": 5
      },
      "item-10780": {
        "value": 4,
        "weight": 8
      },
      "item-10781": {
        "value": 8,
        "weight": 1
      },
      "item-10782": {
        "value": 1,
        "weight": 7
      },
      "item-10783": {
        "value": 4,
        "weight": 7
      },
      "item-10784": {
        "value": 6,
        "weight": 8
      },
      "item-10785": {
        "value": 4,
        "weight": 2
      },
      "item-10786": {
        "value": 9,
        "weight": 7
      },
      "item-10787": {
        "value": 7,
        "weight": 5
      },
      "item-10788": {
        "value": 7,
        "weight": 1
      },
      "item-10789": {
        "value": 8,
        "weight": 3
      },
      "item-10790": {
        "value": 2,
        "weight": 9
      },
      "item-10791": {
        "value": 8,
        "weight": 7
      },
      "item-10792": {
        "value": 9,
        "weight": 5
      },
      "item-10793": {
        "value": 7,
        "weight": 1
      },
      "item-10794": {
        "value": 2,
        "weight": 7
      },
      "item-10795": {
        "value": 1,
        "weight": 1
      },
      "item-10796": {
        "value": 9,
        "weight": 8
      },
      "item-10797": {
        "value": 7,
        "weight": 7
      },
      "item-10798": {
        "value": 1,
        "weight": 1
      },
      "item-10799": {
        "value": 8,
        "weight": 8
      },
      "item-10800": {
        "value": 1,
        "weight": 6
      },
      "item-10801": {
        "value": 2,
        "weight": 5
      },
      "item-10802": {
        "value": 4,
        "weight": 5
      },
      "item-10803": {
        "value": 8,
        "weight": 4
      },
      "item-10804": {
        "value": 4,
        "weight": 2
      },
      "item-10805": {
        "value": 5,
        "weight": 2
      },
      "item-10806": {
        "value": 3,
        "weight": 9
      },
      "item-10807": {
        "value": 3,
        "weight": 6
      },
      "item-10808": {
        "value": 6,
        "weight": 1
      },
      "item-10809": {
        "value": 5,
        "weight": 2
      },
      "item-10810": {
        "value": 5,
        "weight": 6
      },
      "item-10811": {
        "value": 2,
        "weight": 2
      },
      "item-10812": {
        "value": 1,
        "weight": 3
      },
      "item-10813": {
        "value": 4,
        "weight": 3
      },
      "item-10814": {
        "value": 6,
        "weight": 8
      },
      "item-10815": {
        "value": 8,
        "weight": 5
      },
      "item-10816": {
        "value": 1,
        "weight": 2
      },
      "item-10817": {
        "value": 8,
        "weight": 5
      },
      "item-10818": {
        "value": 7,
        "weight": 9
      },
      "item-10819": {
        "value": 6,
        "weight": 2
      },
      "item-10820": {
        "value": 5,
        "weight": 8
      },
      "item-10821": {
        "value": 5,
        "weight": 4
      },
      "item-10822": {
        "value": 3,
        "weight": 8
      },
      "item-10823": {
        "value": 1,
        "weight": 1
      },
      "item-10824": {
        "value": 8,
        "weight": 2
      },
      "item-10825": {
        "value": 8,
        "weight": 6
      },
      "item-10826": {
        "value": 3,
        "weight": 1
      },
      "item-10827": {
        "value": 3,
        "weight": 5
      },
      "item-10828": {
        "value": 3,
        "weight": 3
      },
      "item-10829": {
        "value": 9,
        "weight": 3
      },
      "item-10830": {
        "value": 3,
        "weight": 8
      },
      "item-10831": {
        "value": 1,
        "weight": 2
      },
      "item-10832": {
        "value": 2,
        "weight": 5
      },
      "item-10833": {
        "value": 1,
        "weight": 2
      },
      "item-10834": {
        "value": 8,
        "weight": 6
      },
      "item-10835": {
        "value": 2,
        "weight": 5
      },
      "item-10836": {
        "value": 1,
        "weight": 9
      },
      "item-10837": {
        "value": 3,
        "weight": 4
      },
      "item-10838": {
        "value": 1,
        "weight": 2
      },
      "item-10839": {
        "value": 4,
        "weight": 5
      },
      "item-10840": {
        "value": 6,
        "weight": 9
      },
      "item-10841": {
        "value": 3,
        "weight": 4
      },
      "item-10842": {
        "value": 4,
        "weight": 4
      },
      "item-10843": {
        "value": 8,
        "weight": 5
      },
      "item-10844": {
        "value": 1,
        "weight": 2
      },
      "item-10845": {
        "value": 6,
        "weight": 8
      },
      "item-10846": {
        "value": 9,
        "weight": 9
      },
      "item-10847": {
        "value": 8,
        "weight": 5
      },
      "item-10848": {
        "value": 5,
        "weight": 6
      },
      "item-10849": {
        "value": 6,
        "weight": 8
      },
      "item-10850": {
        "value": 5,
        "weight": 3
      },
      "item-10851": {
        "value": 7,
        "weight": 8
      },
      "item-10852": {
        "value": 4,
        "weight": 7
      },
      "item-10853": {
        "value": 8,
        "weight": 1
      },
      "item-10854": {
        "value": 7,
        "weight": 4
      },
      "item-10855": {
        "value": 3,
        "weight": 1
      },
      "item-10856": {
        "value": 7,
        "weight": 3
      },
      "item-10857": {
        "value": 1,
        "weight": 3
      },
      "item-10858": {
        "value": 6,
        "weight": 2
      },
      "item-10859": {
        "value": 2,
        "weight": 4
      },
      "item-10860": {
        "value": 4,
        "weight": 3
      },
      "item-10861": {
        "value": 7,
        "weight": 1
      },
      "item-10862": {
        "value": 3,
        "weight": 3
      },
      "item-10863": {
        "value": 2,
        "weight": 9
      },
      "item-10864": {
        "value": 1,
        "weight": 9
      },
      "item-10865": {
        "value": 4,
        "weight": 1
      },
      "item-10866": {
        "value": 4,
        "weight": 5
      },
      "item-10867": {
        "value": 9,
        "weight": 7
      },
      "item-10868": {
        "value": 8,
        "weight": 7
      },
      "item-10869": {
        "value": 6,
        "weight": 1
      },
      "item-10870": {
        "value": 9,
        "weight": 1
      },
      "item-10871": {
        "value": 6,
        "weight": 2
      },
      "item-10872": {
        "value": 7,
        "weight": 5
      },
      "item-10873": {
        "value": 6,
        "weight": 2
      },
      "item-10874": {
        "value": 1,
        "weight": 9
      },
      "item-10875": {
        "value": 7,
        "weight": 6
      },
      "item-10876": {
        "value": 7,
        "weight": 3
      },
      "item-10877": {
        "value": 1,
        "weight": 9
      },
      "item-10878": {
        "value": 1,
        "weight": 2
      },
      "item-10879": {
        "value": 8,
        "weight": 6
      },
      "item-10880": {
        "value": 3,
        "weight": 1
      },
      "item-10881": {
        "value": 3,
        "weight": 7
      },
      "item-10882": {
        "value": 8,
        "weight": 3
      },
      "item-10883": {
        "value": 7,
        "weight": 5
      },
      "item-10884": {
        "value": 4,
        "weight": 8
      },
      "item-10885": {
        "value": 2,
        "weight": 7
      },
      "item-10886": {
        "value": 2,
        "weight": 3
      },
      "item-10887": {
        "value": 8,
        "weight": 5
      },
      "item-10888": {
        "value": 4,
        "weight": 6
      },
      "item-10889": {
        "value": 1,
        "weight": 1
      },
      "item-10890": {
        "value": 2,
        "weight": 2
      },
      "item-10891": {
        "value": 3,
        "weight": 8
      },
      "item-10892": {
        "value": 8,
        "weight": 2
      },
      "item-10893": {
        "value": 1,
        "weight": 9
      },
      "item-10894": {
        "value": 4,
        "weight": 9
      },
      "item-10895": {
        "value": 5,
        "weight": 9
      },
      "item-10896": {
        "value": 7,
        "weight": 9
      },
      "item-10897": {
        "value": 9,
        "weight": 7
      },
      "item-10898": {
        "value": 7,
        "weight": 2
      },
      "item-10899": {
        "value": 1,
        "weight": 9
      },
      "item-10900": {
        "value": 7,
        "weight": 6
      },
      "item-10901": {
        "value": 1,
        "weight": 7
      },
      "item-10902": {
        "value": 2,
        "weight": 8
      },
      "item-10903": {
        "value": 3,
        "weight": 6
      },
      "item-10904": {
        "value": 4,
        "weight": 6
      },
      "item-10905": {
        "value": 1,
        "weight": 4
      },
      "item-10906": {
        "value": 9,
        "weight": 5
      },
      "item-10907": {
        "value": 5,
        "weight": 8
      },
      "item-10908": {
        "value": 6,
        "weight": 8
      },
      "item-10909": {
        "value": 8,
        "weight": 3
      },
      "item-10910": {
        "value": 2,
        "weight": 3
      },
      "item-10911": {
        "value": 7,
        "weight": 6
      },
      "item-10912": {
        "value": 8,
        "weight": 8
      },
      "item-10913": {
        "value": 5,
        "weight": 9
      },
      "item-10914": {
        "value": 5,
        "weight": 4
      },
      "item-10915": {
        "value": 2,
        "weight": 3
      },
      "item-10916": {
        "value": 6,
        "weight": 6
      },
      "item-10917": {
        "value": 8,
        "weight": 3
      },
      "item-10918": {
        "value": 3,
        "weight": 5
      },
      "item-10919": {
        "value": 8,
        "weight": 8
      },
      "item-10920": {
        "value": 8,
        "weight": 9
      },
      "item-10921": {
        "value": 2,
        "weight": 5
      },
      "item-10922": {
        "value": 9,
        "weight": 9
      },
      "item-10923": {
        "value": 2,
        "weight": 8
      },
      "item-10924": {
        "value": 5,
        "weight": 1
      },
      "item-10925": {
        "value": 6,
        "weight": 3
      },
      "item-10926": {
        "value": 1,
        "weight": 2
      },
      "item-10927": {
        "value": 7,
        "weight": 6
      },
      "item-10928": {
        "value": 3,
        "weight": 9
      },
      "item-10929": {
        "value": 1,
        "weight": 8
      },
      "item-10930": {
        "value": 8,
        "weight": 2
      },
      "item-10931": {
        "value": 7,
        "weight": 4
      },
      "item-10932": {
        "value": 6,
        "weight": 1
      },
      "item-10933": {
        "value": 4,
        "weight": 2
      },
      "item-10934": {
        "value": 5,
        "weight": 9
      },
      "item-10935": {
        "value": 4,
        "weight": 6
      },
      "item-10936": {
        "value": 7,
        "weight": 3
      },
      "item-10937": {
        "value": 3,
        "weight": 7
      },
      "item-10938": {
        "value": 6,
        "weight": 7
      },
      "item-10939": {
        "value": 2,
        "weight": 4
      },
      "item-10940": {
        "value": 5,
        "weight": 3
      },
      "item-10941": {
        "value": 8,
        "weight": 4
      },
      "item-10942": {
        "value": 1,
        "weight": 3
      },
      "item-10943": {
        "value": 8,
        "weight": 3
      },
      "item-10944": {
        "value": 3,
        "weight": 8
      },
      "item-10945": {
        "value": 9,
        "weight": 9
      },
      "item-10946": {
        "value": 9,
        "weight": 9
      },
      "item-10947": {
        "value": 2,
        "weight": 7
      },
      "item-10948": {
        "value": 8,
        "weight": 7
      },
      "item-10949": {
        "value": 7,
        "weight": 8
      },
      "item-10950": {
        "value": 6,
        "weight": 2
      },
      "item-10951": {
        "value": 4,
        "weight": 7
      },
      "item-10952": {
        "value": 4,
        "weight": 2
      },
      "item-10953": {
        "value": 1,
        "weight": 4
      },
      "item-10954": {
        "value": 3,
        "weight": 2
      },
      "item-10955": {
        "value": 5,
        "weight": 8
      },
      "item-10956": {
        "value": 7,
        "weight": 3
      },
      "item-10957": {
        "value": 1,
        "weight": 3
      },
      "item-10958": {
        "value": 5,
        "weight": 4
      },
      "item-10959": {
        "value": 4,
        "weight": 1
      },
      "item-10960": {
        "value": 6,
        "weight": 2
      },
      "item-10961": {
        "value": 7,
        "weight": 7
      },
      "item-10962": {
        "value": 6,
        "weight": 8
      },
      "item-10963": {
        "value": 6,
        "weight": 1
      },
      "item-10964": {
        "value": 4,
        "weight": 8
      },
      "item-10965": {
        "value": 2,
        "weight": 2
      },
      "item-10966": {
        "value": 5,
        "weight": 7
      },
      "item-10967": {
        "value": 5,
        "weight": 3
      },
      "item-10968": {
        "value": 4,
        "weight": 8
      },
      "item-10969": {
        "value": 3,
        "weight": 1
      },
      "item-10970": {
        "value": 1,
        "weight": 9
      },
      "item-10971": {
        "value": 6,
        "weight": 9
      },
      "item-10972": {
        "value": 2,
        "weight": 6
      },
      "item-10973": {
        "value": 7,
        "weight": 1
      },
      "item-10974": {
        "value": 6,
        "weight": 3
      },
      "item-10975": {
        "value": 8,
        "weight": 8
      },
      "item-10976": {
        "value": 7,
        "weight": 7
      },
      "item-10977": {
        "value": 4,
        "weight": 2
      },
      "item-10978": {
        "value": 3,
        "weight": 4
      },
      "item-10979": {
        "value": 5,
        "weight": 1
      },
      "item-10980": {
        "value": 9,
        "weight": 7
      },
      "item-10981": {
        "value": 8,
        "weight": 1
      },
      "item-10982": {
        "value": 1,
        "weight": 6
      },
      "item-10983": {
        "value": 4,
        "weight": 4
      },
      "item-10984": {
        "value": 6,
        "weight": 9
      },
      "item-10985": {
        "value": 9,
        "weight": 8
      },
      "item-10986": {
        "value": 9,
        "weight": 6
      },
      "item-10987": {
        "value": 5,
        "weight": 1
      },
      "item-10988": {
        "value": 9,
        "weight": 3
      },
      "item-10989": {
        "value": 2,
        "weight": 9
      },
      "item-10990": {
        "value": 4,
        "weight": 7
      },
      "item-10991": {
        "value": 7,
        "weight": 4
      },
      "item-10992": {
        "value": 8,
        "weight": 2
      },
      "item-10993": {
        "value": 8,
        "weight": 1
      },
      "item-10994": {
        "value": 8,
        "weight": 4
      },
      "item-10995": {
        "value": 9,
        "weight": 6
      },
      "item-10996": {
        "value": 2,
        "weight": 8
      },
      "item-10997": {
        "value": 3,
        "weight": 3
      },
      "item-10998": {
        "value": 6,
        "weight": 4
      },
      "item-10999": {
        "value": 2,
        "weight": 4
      },
      "item-11000": {
        "value": 5,
        "weight": 1
      },
      "item-11001": {
        "value": 7,
        "weight": 2
      },
      "item-11002": {
        "value": 8,
        "weight": 2
      },
      "item-11003": {
        "value": 1,
        "weight": 7
      },
      "item-11004": {
        "value": 8,
        "weight": 1
      },
      "item-11005": {
        "value": 4,
        "weight": 1
      },
      "item-11006": {
        "value": 8,
        "weight": 1
      },
      "item-11007": {
        "value": 4,
        "weight": 9
      },
      "item-11008": {
        "value": 2,
        "weight": 2
      },
      "item-11009": {
        "value": 7,
        "weight": 5
      },
      "item-11010": {
        "value": 6,
        "weight": 1
      },
      "item-11011": {
        "value": 5,
        "weight": 8
      },
      "item-11012": {
        "value": 6,
        "weight": 3
      },
      "item-11013": {
        "value": 2,
        "weight": 9
      },
      "item-11014": {
        "value": 6,
        "weight": 1
      },
      "item-11015": {
        "value": 7,
        "weight": 3
      },
      "item-11016": {
        "value": 8,
        "weight": 2
      },
      "item-11017": {
        "value": 5,
        "weight": 8
      },
      "item-11018": {
        "value": 5,
        "weight": 7
      },
      "item-11019": {
        "value": 6,
        "weight": 1
      },
      "item-11020": {
        "value": 8,
        "weight": 4
      },
      "item-11021": {
        "value": 8,
        "weight": 5
      },
      "item-11022": {
        "value": 1,
        "weight": 9
      },
      "item-11023": {
        "value": 5,
        "weight": 3
      },
      "item-11024": {
        "value": 9,
        "weight": 3
      },
      "item-11025": {
        "value": 8,
        "weight": 5
      },
      "item-11026": {
        "value": 1,
        "weight": 5
      },
      "item-11027": {
        "value": 7,
        "weight": 4
      },
      "item-11028": {
        "value": 6,
        "weight": 7
      },
      "item-11029": {
        "value": 6,
        "weight": 1
      },
      "item-11030": {
        "value": 7,
        "weight": 7
      },
      "item-11031": {
        "value": 9,
        "weight": 1
      },
      "item-11032": {
        "value": 6,
        "weight": 6
      },
      "item-11033": {
        "value": 6,
        "weight": 1
      },
      "item-11034": {
        "value": 7,
        "weight": 6
      },
      "item-11035": {
        "value": 7,
        "weight": 8
      },
      "item-11036": {
        "value": 9,
        "weight": 4
      },
      "item-11037": {
        "value": 4,
        "weight": 2
      },
      "item-11038": {
        "value": 8,
        "weight": 7
      },
      "item-11039": {
        "value": 7,
        "weight": 2
      },
      "item-11040": {
        "value": 3,
        "weight": 6
      },
      "item-11041": {
        "value": 6,
        "weight": 2
      },
      "item-11042": {
        "value": 7,
        "weight": 3
      },
      "item-11043": {
        "value": 9,
        "weight": 7
      },
      "item-11044": {
        "value": 8,
        "weight": 7
      },
      "item-11045": {
        "value": 8,
        "weight": 2
      },
      "item-11046": {
        "value": 8,
        "weight": 8
      },
      "item-11047": {
        "value": 3,
        "weight": 1
      },
      "item-11048": {
        "value": 7,
        "weight": 7
      },
      "item-11049": {
        "value": 8,
        "weight": 3
      },
      "item-11050": {
        "value": 2,
        "weight": 5
      },
      "item-11051": {
        "value": 7,
        "weight": 7
      },
      "item-11052": {
        "value": 1,
        "weight": 2
      },
      "item-11053": {
        "value": 2,
        "weight": 6
      },
      "item-11054": {
        "value": 4,
        "weight": 7
      },
      "item-11055": {
        "value": 8,
        "weight": 5
      },
      "item-11056": {
        "value": 2,
        "weight": 4
      },
      "item-11057": {
        "value": 6,
        "weight": 3
      },
      "item-11058": {
        "value": 1,
        "weight": 7
      },
      "item-11059": {
        "value": 5,
        "weight": 4
      },
      "item-11060": {
        "value": 3,
        "weight": 3
      },
      "item-11061": {
        "value": 7,
        "weight": 4
      },
      "item-11062": {
        "value": 3,
        "weight": 8
      },
      "item-11063": {
        "value": 9,
        "weight": 4
      },
      "item-11064": {
        "value": 3,
        "weight": 7
      },
      "item-11065": {
        "value": 9,
        "weight": 1
      },
      "item-11066": {
        "value": 3,
        "weight": 8
      },
      "item-11067": {
        "value": 7,
        "weight": 2
      },
      "item-11068": {
        "value": 3,
        "weight": 5
      },
      "item-11069": {
        "value": 9,
        "weight": 4
      },
      "item-11070": {
        "value": 3,
        "weight": 1
      },
      "item-11071": {
        "value": 5,
        "weight": 6
      },
      "item-11072": {
        "value": 4,
        "weight": 5
      },
      "item-11073": {
        "value": 3,
        "weight": 4
      },
      "item-11074": {
        "value": 9,
        "weight": 8
      },
      "item-11075": {
        "value": 2,
        "weight": 2
      },
      "item-11076": {
        "value": 7,
        "weight": 5
      },
      "item-11077": {
        "value": 6,
        "weight": 6
      },
      "item-11078": {
        "value": 4,
        "weight": 4
      },
      "item-11079": {
        "value": 4,
        "weight": 7
      },
      "item-11080": {
        "value": 7,
        "weight": 6
      },
      "item-11081": {
        "value": 2,
        "weight": 7
      },
      "item-11082": {
        "value": 6,
        "weight": 4
      },
      "item-11083": {
        "value": 8,
        "weight": 2
      },
      "item-11084": {
        "value": 3,
        "weight": 1
      },
      "item-11085": {
        "value": 2,
        "weight": 1
      },
      "item-11086": {
        "value": 7,
        "weight": 1
      },
      "item-11087": {
        "value": 4,
        "weight": 9
      },
      "item-11088": {
        "value": 9,
        "weight": 3
      },
      "item-11089": {
        "value": 2,
        "weight": 3
      },
      "item-11090": {
        "value": 2,
        "weight": 9
      },
      "item-11091": {
        "value": 4,
        "weight": 1
      },
      "item-11092": {
        "value": 3,
        "weight": 8
      },
      "item-11093": {
        "value": 8,
        "weight": 2
      },
      "item-11094": {
        "value": 6,
        "weight": 3
      },
      "item-11095": {
        "value": 3,
        "weight": 2
      },
      "item-11096": {
        "value": 3,
        "weight": 1
      },
      "item-11097": {
        "value": 2,
        "weight": 9
      },
      "item-11098": {
        "value": 9,
        "weight": 4
      },
      "item-11099": {
        "value": 2,
        "weight": 7
      },
      "item-11100": {
        "value": 9,
        "weight": 2
      },
      "item-11101": {
        "value": 1,
        "weight": 5
      },
      "item-11102": {
        "value": 9,
        "weight": 5
      },
      "item-11103": {
        "value": 8,
        "weight": 1
      },
      "item-11104": {
        "value": 3,
        "weight": 8
      },
      "item-11105": {
        "value": 8,
        "weight": 3
      },
      "item-11106": {
        "value": 7,
        "weight": 9
      },
      "item-11107": {
        "value": 1,
        "weight": 6
      },
      "item-11108": {
        "value": 2,
        "weight": 1
      },
      "item-11109": {
        "value": 7,
        "weight": 6
      },
      "item-11110": {
        "value": 5,
        "weight": 8
      },
      "item-11111": {
        "value": 3,
        "weight": 4
      },
      "item-11112": {
        "value": 8,
        "weight": 7
      },
      "item-11113": {
        "value": 9,
        "weight": 2
      },
      "item-11114": {
        "value": 5,
        "weight": 3
      },
      "item-11115": {
        "value": 4,
        "weight": 4
      },
      "item-11116": {
        "value": 3,
        "weight": 1
      },
      "item-11117": {
        "value": 3,
        "weight": 3
      },
      "item-11118": {
        "value": 5,
        "weight": 1
      },
      "item-11119": {
        "value": 2,
        "weight": 1
      },
      "item-11120": {
        "value": 5,
        "weight": 3
      },
      "item-11121": {
        "value": 1,
        "weight": 4
      },
      "item-11122": {
        "value": 4,
        "weight": 2
      },
      "item-11123": {
        "value": 8,
        "weight": 6
      },
      "item-11124": {
        "value": 5,
        "weight": 8
      },
      "item-11125": {
        "value": 3,
        "weight": 4
      },
      "item-11126": {
        "value": 1,
        "weight": 2
      },
      "item-11127": {
        "value": 5,
        "weight": 4
      },
      "item-11128": {
        "value": 9,
        "weight": 1
      },
      "item-11129": {
        "value": 9,
        "weight": 3
      },
      "item-11130": {
        "value": 1,
        "weight": 5
      },
      "item-11131": {
        "value": 3,
        "weight": 9
      },
      "item-11132": {
        "value": 7,
        "weight": 2
      },
      "item-11133": {
        "value": 1,
        "weight": 1
      },
      "item-11134": {
        "value": 5,
        "weight": 9
      },
      "item-11135": {
        "value": 9,
        "weight": 2
      },
      "item-11136": {
        "value": 2,
        "weight": 2
      },
      "item-11137": {
        "value": 7,
        "weight": 8
      },
      "item-11138": {
        "value": 6,
        "weight": 5
      },
      "item-11139": {
        "value": 8,
        "weight": 7
      },
      "item-11140": {
        "value": 8,
        "weight": 4
      },
      "item-11141": {
        "value": 3,
        "weight": 4
      },
      "item-11142": {
        "value": 8,
        "weight": 3
      },
      "item-11143": {
        "value": 8,
        "weight": 3
      },
      "item-11144": {
        "value": 8,
        "weight": 4
      },
      "item-11145": {
        "value": 6,
        "weight": 6
      },
      "item-11146": {
        "value": 4,
        "weight": 9
      },
      "item-11147": {
        "value": 6,
        "weight": 1
      },
      "item-11148": {
        "value": 5,
        "weight": 7
      },
      "item-11149": {
        "value": 8,
        "weight": 9
      },
      "item-11150": {
        "value": 4,
        "weight": 2
      },
      "item-11151": {
        "value": 7,
        "weight": 8
      },
      "item-11152": {
        "value": 3,
        "weight": 5
      },
      "item-11153": {
        "value": 3,
        "weight": 4
      },
      "item-11154": {
        "value": 2,
        "weight": 7
      },
      "item-11155": {
        "value": 4,
        "weight": 3
      },
      "item-11156": {
        "value": 3,
        "weight": 5
      },
      "item-11157": {
        "value": 9,
        "weight": 9
      },
      "item-11158": {
        "value": 2,
        "weight": 4
      },
      "item-11159": {
        "value": 5,
        "weight": 5
      },
      "item-11160": {
        "value": 4,
        "weight": 2
      },
      "item-11161": {
        "value": 5,
        "weight": 9
      },
      "item-11162": {
        "value": 5,
        "weight": 7
      },
      "item-11163": {
        "value": 3,
        "weight": 4
      },
      "item-11164": {
        "value": 9,
        "weight": 8
      },
      "item-11165": {
        "value": 5,
        "weight": 6
      },
      "item-11166": {
        "value": 9,
        "weight": 6
      },
      "item-11167": {
        "value": 7,
        "weight": 9
      },
      "item-11168": {
        "value": 4,
        "weight": 8
      },
      "item-11169": {
        "value": 9,
        "weight": 9
      },
      "item-11170": {
        "value": 3,
        "weight": 6
      },
      "item-11171": {
        "value": 3,
        "weight": 6
      },
      "item-11172": {
        "value": 6,
        "weight": 6
      },
      "item-11173": {
        "value": 5,
        "weight": 3
      },
      "item-11174": {
        "value": 1,
        "weight": 1
      },
      "item-11175": {
        "value": 5,
        "weight": 9
      },
      "item-11176": {
        "value": 5,
        "weight": 5
      },
      "item-11177": {
        "value": 5,
        "weight": 1
      },
      "item-11178": {
        "value": 9,
        "weight": 2
      },
      "item-11179": {
        "value": 1,
        "weight": 6
      },
      "item-11180": {
        "value": 3,
        "weight": 2
      },
      "item-11181": {
        "value": 3,
        "weight": 8
      },
      "item-11182": {
        "value": 4,
        "weight": 9
      },
      "item-11183": {
        "value": 3,
        "weight": 9
      },
      "item-11184": {
        "value": 9,
        "weight": 1
      },
      "item-11185": {
        "value": 5,
        "weight": 9
      },
      "item-11186": {
        "value": 4,
        "weight": 6
      },
      "item-11187": {
        "value": 4,
        "weight": 9
      },
      "item-11188": {
        "value": 5,
        "weight": 8
      },
      "item-11189": {
        "value": 3,
        "weight": 1
      },
      "item-11190": {
        "value": 6,
        "weight": 7
      },
      "item-11191": {
        "value": 7,
        "weight": 6
      },
      "item-11192": {
        "value": 9,
        "weight": 6
      },
      "item-11193": {
        "value": 7,
        "weight": 2
      },
      "item-11194": {
        "value": 9,
        "weight": 7
      },
      "item-11195": {
        "value": 9,
        "weight": 1
      },
      "item-11196": {
        "value": 4,
        "weight": 1
      },
      "item-11197": {
        "value": 2,
        "weight": 6
      },
      "item-11198": {
        "value": 4,
        "weight": 4
      },
      "item-11199": {
        "value": 8,
        "weight": 8
      },
      "item-11200": {
        "value": 2,
        "weight": 2
      },
      "item-11201": {
        "value": 6,
        "weight": 7
      },
      "item-11202": {
        "value": 6,
        "weight": 7
      },
      "item-11203": {
        "value": 7,
        "weight": 4
      },
      "item-11204": {
        "value": 7,
        "weight": 8
      },
      "item-11205": {
        "value": 5,
        "weight": 2
      },
      "item-11206": {
        "value": 5,
        "weight": 6
      },
      "item-11207": {
        "value": 3,
        "weight": 3
      },
      "item-11208": {
        "value": 4,
        "weight": 1
      },
      "item-11209": {
        "value": 4,
        "weight": 6
      },
      "item-11210": {
        "value": 6,
        "weight": 3
      },
      "item-11211": {
        "value": 9,
        "weight": 2
      },
      "item-11212": {
        "value": 8,
        "weight": 6
      },
      "item-11213": {
        "value": 8,
        "weight": 7
      },
      "item-11214": {
        "value": 6,
        "weight": 2
      },
      "item-11215": {
        "value": 6,
        "weight": 9
      },
      "item-11216": {
        "value": 7,
        "weight": 3
      },
      "item-11217": {
        "value": 5,
        "weight": 3
      },
      "item-11218": {
        "value": 6,
        "weight": 3
      },
      "item-11219": {
        "value": 4,
        "weight": 8
      },
      "item-11220": {
        "value": 8,
        "weight": 4
      },
      "item-11221": {
        "value": 7,
        "weight": 8
      },
      "item-11222": {
        "value": 2,
        "weight": 6
      },
      "item-11223": {
        "value": 2,
        "weight": 8
      },
      "item-11224": {
        "value": 7,
        "weight": 9
      },
      "item-11225": {
        "value": 3,
        "weight": 1
      },
      "item-11226": {
        "value": 7,
        "weight": 8
      },
      "item-11227": {
        "value": 8,
        "weight": 7
      },
      "item-11228": {
        "value": 8,
        "weight": 8
      },
      "item-11229": {
        "value": 6,
        "weight": 2
      },
      "item-11230": {
        "value": 8,
        "weight": 1
      },
      "item-11231": {
        "value": 9,
        "weight": 7
      },
      "item-11232": {
        "value": 4,
        "weight": 8
      },
      "item-11233": {
        "value": 5,
        "weight": 9
      },
      "item-11234": {
        "value": 6,
        "weight": 1
      },
      "item-11235": {
        "value": 5,
        "weight": 5
      },
      "item-11236": {
        "value": 6,
        "weight": 6
      },
      "item-11237": {
        "value": 6,
        "weight": 6
      },
      "item-11238": {
        "value": 2,
        "weight": 6
      },
      "item-11239": {
        "value": 6,
        "weight": 2
      },
      "item-11240": {
        "value": 5,
        "weight": 5
      },
      "item-11241": {
        "value": 2,
        "weight": 9
      },
      "item-11242": {
        "value": 9,
        "weight": 9
      },
      "item-11243": {
        "value": 9,
        "weight": 9
      },
      "item-11244": {
        "value": 3,
        "weight": 5
      },
      "item-11245": {
        "value": 4,
        "weight": 6
      },
      "item-11246": {
        "value": 3,
        "weight": 6
      },
      "item-11247": {
        "value": 1,
        "weight": 9
      },
      "item-11248": {
        "value": 1,
        "weight": 7
      },
      "item-11249": {
        "value": 5,
        "weight": 6
      },
      "item-11250": {
        "value": 3,
        "weight": 7
      },
      "item-11251": {
        "value": 7,
        "weight": 8
      },
      "item-11252": {
        "value": 6,
        "weight": 9
      },
      "item-11253": {
        "value": 8,
        "weight": 4
      },
      "item-11254": {
        "value": 9,
        "weight": 9
      },
      "item-11255": {
        "value": 8,
        "weight": 2
      },
      "item-11256": {
        "value": 6,
        "weight": 2
      },
      "item-11257": {
        "value": 6,
        "weight": 1
      },
      "item-11258": {
        "value": 3,
        "weight": 9
      },
      "item-11259": {
        "value": 5,
        "weight": 9
      },
      "item-11260": {
        "value": 3,
        "weight": 9
      },
      "item-11261": {
        "value": 7,
        "weight": 7
      },
      "item-11262": {
        "value": 1,
        "weight": 4
      },
      "item-11263": {
        "value": 8,
        "weight": 1
      },
      "item-11264": {
        "value": 9,
        "weight": 7
      },
      "item-11265": {
        "value": 4,
        "weight": 7
      },
      "item-11266": {
        "value": 6,
        "weight": 6
      },
      "item-11267": {
        "value": 1,
        "weight": 8
      },
      "item-11268": {
        "value": 2,
        "weight": 8
      },
      "item-11269": {
        "value": 1,
        "weight": 2
      },
      "item-11270": {
        "value": 6,
        "weight": 6
      },
      "item-11271": {
        "value": 3,
        "weight": 6
      },
      "item-11272": {
        "value": 9,
        "weight": 7
      },
      "item-11273": {
        "value": 2,
        "weight": 2
      },
      "item-11274": {
        "value": 9,
        "weight": 2
      },
      "item-11275": {
        "value": 1,
        "weight": 7
      },
      "item-11276": {
        "value": 1,
        "weight": 4
      },
      "item-11277": {
        "value": 3,
        "weight": 6
      },
      "item-11278": {
        "value": 9,
        "weight": 7
      },
      "item-11279": {
        "value": 4,
        "weight": 8
      },
      "item-11280": {
        "value": 7,
        "weight": 2
      },
      "item-11281": {
        "value": 6,
        "weight": 1
      },
      "item-11282": {
        "value": 6,
        "weight": 8
      },
      "item-11283": {
        "value": 4,
        "weight": 9
      },
      "item-11284": {
        "value": 8,
        "weight": 2
      },
      "item-11285": {
        "value": 2,
        "weight": 7
      },
      "item-11286": {
        "value": 1,
        "weight": 3
      },
      "item-11287": {
        "value": 4,
        "weight": 2
      },
      "item-11288": {
        "value": 4,
        "weight": 5
      },
      "item-11289": {
        "value": 6,
        "weight": 9
      },
      "item-11290": {
        "value": 6,
        "weight": 5
      },
      "item-11291": {
        "value": 2,
        "weight": 1
      },
      "item-11292": {
        "value": 3,
        "weight": 4
      },
      "item-11293": {
        "value": 4,
        "weight": 9
      },
      "item-11294": {
        "value": 7,
        "weight": 5
      },
      "item-11295": {
        "value": 7,
        "weight": 3
      },
      "item-11296": {
        "value": 2,
        "weight": 8
      },
      "item-11297": {
        "value": 2,
        "weight": 4
      },
      "item-11298": {
        "value": 3,
        "weight": 8
      },
      "item-11299": {
        "value": 6,
        "weight": 4
      },
      "item-11300": {
        "value": 7,
        "weight": 7
      },
      "item-11301": {
        "value": 1,
        "weight": 6
      },
      "item-11302": {
        "value": 9,
        "weight": 5
      },
      "item-11303": {
        "value": 8,
        "weight": 3
      },
      "item-11304": {
        "value": 5,
        "weight": 9
      },
      "item-11305": {
        "value": 8,
        "weight": 7
      },
      "item-11306": {
        "value": 3,
        "weight": 9
      },
      "item-11307": {
        "value": 7,
        "weight": 2
      },
      "item-11308": {
        "value": 9,
        "weight": 4
      },
      "item-11309": {
        "value": 9,
        "weight": 4
      },
      "item-11310": {
        "value": 1,
        "weight": 5
      },
      "item-11311": {
        "value": 2,
        "weight": 1
      },
      "item-11312": {
        "value": 9,
        "weight": 2
      },
      "item-11313": {
        "value": 4,
        "weight": 8
      },
      "item-11314": {
        "value": 6,
        "weight": 8
      },
      "item-11315": {
        "value": 1,
        "weight": 2
      },
      "item-11316": {
        "value": 4,
        "weight": 6
      },
      "item-11317": {
        "value": 2,
        "weight": 2
      },
      "item-11318": {
        "value": 8,
        "weight": 7
      },
      "item-11319": {
        "value": 3,
        "weight": 4
      },
      "item-11320": {
        "value": 4,
        "weight": 6
      },
      "item-11321": {
        "value": 6,
        "weight": 4
      },
      "item-11322": {
        "value": 5,
        "weight": 9
      },
      "item-11323": {
        "value": 4,
        "weight": 5
      },
      "item-11324": {
        "value": 2,
        "weight": 6
      },
      "item-11325": {
        "value": 7,
        "weight": 9
      },
      "item-11326": {
        "value": 5,
        "weight": 4
      },
      "item-11327": {
        "value": 5,
        "weight": 5
      },
      "item-11328": {
        "value": 6,
        "weight": 7
      },
      "item-11329": {
        "value": 9,
        "weight": 8
      },
      "item-11330": {
        "value": 9,
        "weight": 1
      },
      "item-11331": {
        "value": 8,
        "weight": 3
      },
      "item-11332": {
        "value": 5,
        "weight": 5
      },
      "item-11333": {
        "value": 8,
        "weight": 1
      },
      "item-11334": {
        "value": 7,
        "weight": 3
      },
      "item-11335": {
        "value": 3,
        "weight": 6
      },
      "item-11336": {
        "value": 3,
        "weight": 6
      },
      "item-11337": {
        "value": 8,
        "weight": 6
      },
      "item-11338": {
        "value": 2,
        "weight": 8
      },
      "item-11339": {
        "value": 4,
        "weight": 3
      },
      "item-11340": {
        "value": 5,
        "weight": 6
      },
      "item-11341": {
        "value": 4,
        "weight": 4
      },
      "item-11342": {
        "value": 3,
        "weight": 3
      },
      "item-11343": {
        "value": 2,
        "weight": 6
      },
      "item-11344": {
        "value": 3,
        "weight": 5
      },
      "item-11345": {
        "value": 7,
        "weight": 5
      },
      "item-11346": {
        "value": 4,
        "weight": 4
      },
      "item-11347": {
        "value": 4,
        "weight": 7
      },
      "item-11348": {
        "value": 4,
        "weight": 7
      },
      "item-11349": {
        "value": 7,
        "weight": 1
      },
      "item-11350": {
        "value": 7,
        "weight": 5
      },
      "item-11351": {
        "value": 4,
        "weight": 1
      },
      "item-11352": {
        "value": 4,
        "weight": 5
      },
      "item-11353": {
        "value": 4,
        "weight": 1
      },
      "item-11354": {
        "value": 3,
        "weight": 8
      },
      "item-11355": {
        "value": 2,
        "weight": 9
      },
      "item-11356": {
        "value": 2,
        "weight": 8
      },
      "item-11357": {
        "value": 1,
        "weight": 6
      },
      "item-11358": {
        "value": 1,
        "weight": 3
      },
      "item-11359": {
        "value": 9,
        "weight": 7
      },
      "item-11360": {
        "value": 6,
        "weight": 8
      },
      "item-11361": {
        "value": 1,
        "weight": 5
      },
      "item-11362": {
        "value": 9,
        "weight": 5
      },
      "item-11363": {
        "value": 1,
        "weight": 2
      },
      "item-11364": {
        "value": 4,
        "weight": 2
      },
      "item-11365": {
        "value": 3,
        "weight": 6
      },
      "item-11366": {
        "value": 9,
        "weight": 8
      },
      "item-11367": {
        "value": 6,
        "weight": 8
      },
      "item-11368": {
        "value": 9,
        "weight": 7
      },
      "item-11369": {
        "value": 4,
        "weight": 3
      },
      "item-11370": {
        "value": 3,
        "weight": 7
      },
      "item-11371": {
        "value": 9,
        "weight": 3
      },
      "item-11372": {
        "value": 2,
        "weight": 5
      },
      "item-11373": {
        "value": 3,
        "weight": 3
      },
      "item-11374": {
        "value": 4,
        "weight": 5
      },
      "item-11375": {
        "value": 5,
        "weight": 8
      },
      "item-11376": {
        "value": 9,
        "weight": 8
      },
      "item-11377": {
        "value": 5,
        "weight": 7
      },
      "item-11378": {
        "value": 4,
        "weight": 6
      },
      "item-11379": {
        "value": 3,
        "weight": 8
      },
      "item-11380": {
        "value": 3,
        "weight": 3
      },
      "item-11381": {
        "value": 1,
        "weight": 1
      },
      "item-11382": {
        "value": 6,
        "weight": 2
      },
      "item-11383": {
        "value": 7,
        "weight": 6
      },
      "item-11384": {
        "value": 2,
        "weight": 2
      },
      "item-11385": {
        "value": 9,
        "weight": 8
      },
      "item-11386": {
        "value": 9,
        "weight": 8
      },
      "item-11387": {
        "value": 4,
        "weight": 9
      },
      "item-11388": {
        "value": 1,
        "weight": 5
      },
      "item-11389": {
        "value": 1,
        "weight": 9
      },
      "item-11390": {
        "value": 4,
        "weight": 8
      },
      "item-11391": {
        "value": 8,
        "weight": 9
      },
      "item-11392": {
        "value": 4,
        "weight": 2
      },
      "item-11393": {
        "value": 1,
        "weight": 3
      },
      "item-11394": {
        "value": 2,
        "weight": 4
      },
      "item-11395": {
        "value": 8,
        "weight": 4
      },
      "item-11396": {
        "value": 1,
        "weight": 7
      },
      "item-11397": {
        "value": 9,
        "weight": 9
      },
      "item-11398": {
        "value": 2,
        "weight": 5
      },
      "item-11399": {
        "value": 5,
        "weight": 5
      },
      "item-11400": {
        "value": 4,
        "weight": 4
      },
      "item-11401": {
        "value": 9,
        "weight": 5
      },
      "item-11402": {
        "value": 6,
        "weight": 7
      },
      "item-11403": {
        "value": 5,
        "weight": 2
      },
      "item-11404": {
        "value": 9,
        "weight": 6
      },
      "item-11405": {
        "value": 5,
        "weight": 3
      },
      "item-11406": {
        "value": 1,
        "weight": 4
      },
      "item-11407": {
        "value": 1,
        "weight": 9
      },
      "item-11408": {
        "value": 2,
        "weight": 6
      },
      "item-11409": {
        "value": 6,
        "weight": 9
      },
      "item-11410": {
        "value": 3,
        "weight": 6
      },
      "item-11411": {
        "value": 2,
        "weight": 7
      },
      "item-11412": {
        "value": 4,
        "weight": 8
      },
      "item-11413": {
        "value": 8,
        "weight": 7
      },
      "item-11414": {
        "value": 2,
        "weight": 7
      },
      "item-11415": {
        "value": 1,
        "weight": 7
      },
      "item-11416": {
        "value": 4,
        "weight": 3
      },
      "item-11417": {
        "value": 5,
        "weight": 6
      },
      "item-11418": {
        "value": 8,
        "weight": 9
      },
      "item-11419": {
        "value": 6,
        "weight": 1
      },
      "item-11420": {
        "value": 9,
        "weight": 7
      },
      "item-11421": {
        "value": 3,
        "weight": 7
      },
      "item-11422": {
        "value": 7,
        "weight": 2
      },
      "item-11423": {
        "value": 7,
        "weight": 9
      },
      "item-11424": {
        "value": 9,
        "weight": 2
      },
      "item-11425": {
        "value": 7,
        "weight": 1
      },
      "item-11426": {
        "value": 9,
        "weight": 7
      },
      "item-11427": {
        "value": 9,
        "weight": 2
      },
      "item-11428": {
        "value": 2,
        "weight": 8
      },
      "item-11429": {
        "value": 1,
        "weight": 5
      },
      "item-11430": {
        "value": 5,
        "weight": 6
      },
      "item-11431": {
        "value": 8,
        "weight": 5
      },
      "item-11432": {
        "value": 8,
        "weight": 6
      },
      "item-11433": {
        "value": 9,
        "weight": 9
      },
      "item-11434": {
        "value": 8,
        "weight": 7
      },
      "item-11435": {
        "value": 8,
        "weight": 2
      },
      "item-11436": {
        "value": 1,
        "weight": 5
      },
      "item-11437": {
        "value": 8,
        "weight": 5
      },
      "item-11438": {
        "value": 8,
        "weight": 2
      },
      "item-11439": {
        "value": 5,
        "weight": 8
      },
      "item-11440": {
        "value": 5,
        "weight": 2
      },
      "item-11441": {
        "value": 2,
        "weight": 5
      },
      "item-11442": {
        "value": 8,
        "weight": 7
      },
      "item-11443": {
        "value": 6,
        "weight": 6
      },
      "item-11444": {
        "value": 3,
        "weight": 1
      },
      "item-11445": {
        "value": 8,
        "weight": 1
      },
      "item-11446": {
        "value": 3,
        "weight": 5
      },
      "item-11447": {
        "value": 3,
        "weight": 3
      },
      "item-11448": {
        "value": 1,
        "weight": 3
      },
      "item-11449": {
        "value": 7,
        "weight": 4
      },
      "item-11450": {
        "value": 8,
        "weight": 8
      },
      "item-11451": {
        "value": 4,
        "weight": 9
      },
      "item-11452": {
        "value": 5,
        "weight": 9
      },
      "item-11453": {
        "value": 6,
        "weight": 5
      },
      "item-11454": {
        "value": 4,
        "weight": 1
      },
      "item-11455": {
        "value": 9,
        "weight": 3
      },
      "item-11456": {
        "value": 8,
        "weight": 5
      },
      "item-11457": {
        "value": 4,
        "weight": 4
      },
      "item-11458": {
        "value": 3,
        "weight": 8
      },
      "item-11459": {
        "value": 2,
        "weight": 6
      },
      "item-11460": {
        "value": 7,
        "weight": 5
      },
      "item-11461": {
        "value": 7,
        "weight": 7
      },
      "item-11462": {
        "value": 5,
        "weight": 6
      },
      "item-11463": {
        "value": 6,
        "weight": 8
      },
      "item-11464": {
        "value": 3,
        "weight": 3
      },
      "item-11465": {
        "value": 2,
        "weight": 7
      },
      "item-11466": {
        "value": 2,
        "weight": 8
      },
      "item-11467": {
        "value": 4,
        "weight": 7
      },
      "item-11468": {
        "value": 7,
        "weight": 2
      },
      "item-11469": {
        "value": 8,
        "weight": 2
      },
      "item-11470": {
        "value": 3,
        "weight": 2
      },
      "item-11471": {
        "value": 3,
        "weight": 5
      },
      "item-11472": {
        "value": 5,
        "weight": 9
      },
      "item-11473": {
        "value": 4,
        "weight": 5
      },
      "item-11474": {
        "value": 8,
        "weight": 6
      },
      "item-11475": {
        "value": 6,
        "weight": 2
      },
      "item-11476": {
        "value": 5,
        "weight": 8
      },
      "item-11477": {
        "value": 9,
        "weight": 9
      },
      "item-11478": {
        "value": 6,
        "weight": 5
      },
      "item-11479": {
        "value": 8,
        "weight": 5
      },
      "item-11480": {
        "value": 5,
        "weight": 8
      },
      "item-11481": {
        "value": 8,
        "weight": 9
      },
      "item-11482": {
        "value": 9,
        "weight": 1
      },
      "item-11483": {
        "value": 3,
        "weight": 2
      },
      "item-11484": {
        "value": 7,
        "weight": 4
      },
      "item-11485": {
        "value": 5,
        "weight": 2
      },
      "item-11486": {
        "value": 3,
        "weight": 1
      },
      "item-11487": {
        "value": 2,
        "weight": 3
      },
      "item-11488": {
        "value": 9,
        "weight": 6
      },
      "item-11489": {
        "value": 3,
        "weight": 8
      },
      "item-11490": {
        "value": 2,
        "weight": 5
      },
      "item-11491": {
        "value": 9,
        "weight": 9
      },
      "item-11492": {
        "value": 7,
        "weight": 4
      },
      "item-11493": {
        "value": 7,
        "weight": 6
      },
      "item-11494": {
        "value": 2,
        "weight": 1
      },
      "item-11495": {
        "value": 7,
        "weight": 2
      },
      "item-11496": {
        "value": 1,
        "weight": 1
      },
      "item-11497": {
        "value": 4,
        "weight": 7
      },
      "item-11498": {
        "value": 3,
        "weight": 7
      },
      "item-11499": {
        "value": 5,
        "weight": 5
      },
      "item-11500": {
        "value": 2,
        "weight": 6
      },
      "item-11501": {
        "value": 3,
        "weight": 3
      },
      "item-11502": {
        "value": 9,
        "weight": 8
      },
      "item-11503": {
        "value": 4,
        "weight": 1
      },
      "item-11504": {
        "value": 1,
        "weight": 7
      },
      "item-11505": {
        "value": 4,
        "weight": 9
      },
      "item-11506": {
        "value": 9,
        "weight": 6
      },
      "item-11507": {
        "value": 5,
        "weight": 3
      },
      "item-11508": {
        "value": 7,
        "weight": 7
      },
      "item-11509": {
        "value": 6,
        "weight": 3
      },
      "item-11510": {
        "value": 1,
        "weight": 6
      },
      "item-11511": {
        "value": 5,
        "weight": 9
      },
      "item-11512": {
        "value": 5,
        "weight": 9
      },
      "item-11513": {
        "value": 7,
        "weight": 6
      },
      "item-11514": {
        "value": 6,
        "weight": 3
      },
      "item-11515": {
        "value": 2,
        "weight": 8
      },
      "item-11516": {
        "value": 1,
        "weight": 3
      },
      "item-11517": {
        "value": 3,
        "weight": 5
      },
      "item-11518": {
        "value": 8,
        "weight": 4
      },
      "item-11519": {
        "value": 5,
        "weight": 2
      },
      "item-11520": {
        "value": 2,
        "weight": 2
      },
      "item-11521": {
        "value": 8,
        "weight": 7
      },
      "item-11522": {
        "value": 3,
        "weight": 9
      },
      "item-11523": {
        "value": 1,
        "weight": 3
      },
      "item-11524": {
        "value": 8,
        "weight": 4
      },
      "item-11525": {
        "value": 9,
        "weight": 7
      },
      "item-11526": {
        "value": 7,
        "weight": 2
      },
      "item-11527": {
        "value": 9,
        "weight": 1
      },
      "item-11528": {
        "value": 5,
        "weight": 8
      },
      "item-11529": {
        "value": 6,
        "weight": 8
      },
      "item-11530": {
        "value": 7,
        "weight": 4
      },
      "item-11531": {
        "value": 4,
        "weight": 2
      },
      "item-11532": {
        "value": 8,
        "weight": 5
      },
      "item-11533": {
        "value": 5,
        "weight": 4
      },
      "item-11534": {
        "value": 8,
        "weight": 5
      },
      "item-11535": {
        "value": 9,
        "weight": 7
      },
      "item-11536": {
        "value": 2,
        "weight": 9
      },
      "item-11537": {
        "value": 7,
        "weight": 8
      },
      "item-11538": {
        "value": 3,
        "weight": 3
      },
      "item-11539": {
        "value": 2,
        "weight": 4
      },
      "item-11540": {
        "value": 2,
        "weight": 5
      },
      "item-11541": {
        "value": 9,
        "weight": 2
      },
      "item-11542": {
        "value": 6,
        "weight": 6
      },
      "item-11543": {
        "value": 4,
        "weight": 6
      },
      "item-11544": {
        "value": 4,
        "weight": 1
      },
      "item-11545": {
        "value": 8,
        "weight": 7
      },
      "item-11546": {
        "value": 3,
        "weight": 2
      },
      "item-11547": {
        "value": 2,
        "weight": 1
      },
      "item-11548": {
        "value": 3,
        "weight": 2
      },
      "item-11549": {
        "value": 6,
        "weight": 3
      },
      "item-11550": {
        "value": 6,
        "weight": 3
      },
      "item-11551": {
        "value": 6,
        "weight": 6
      },
      "item-11552": {
        "value": 4,
        "weight": 4
      },
      "item-11553": {
        "value": 7,
        "weight": 4
      },
      "item-11554": {
        "value": 3,
        "weight": 9
      },
      "item-11555": {
        "value": 4,
        "weight": 7
      },
      "item-11556": {
        "value": 7,
        "weight": 8
      },
      "item-11557": {
        "value": 7,
        "weight": 8
      },
      "item-11558": {
        "value": 2,
        "weight": 4
      },
      "item-11559": {
        "value": 5,
        "weight": 3
      },
      "item-11560": {
        "value": 4,
        "weight": 9
      },
      "item-11561": {
        "value": 1,
        "weight": 5
      },
      "item-11562": {
        "value": 6,
        "weight": 9
      },
      "item-11563": {
        "value": 5,
        "weight": 8
      },
      "item-11564": {
        "value": 9,
        "weight": 1
      },
      "item-11565": {
        "value": 2,
        "weight": 6
      },
      "item-11566": {
        "value": 4,
        "weight": 4
      },
      "item-11567": {
        "value": 9,
        "weight": 4
      },
      "item-11568": {
        "value": 7,
        "weight": 1
      },
      "item-11569": {
        "value": 9,
        "weight": 7
      },
      "item-11570": {
        "value": 3,
        "weight": 1
      },
      "item-11571": {
        "value": 1,
        "weight": 4
      },
      "item-11572": {
        "value": 1,
        "weight": 6
      },
      "item-11573": {
        "value": 6,
        "weight": 1
      },
      "item-11574": {
        "value": 7,
        "weight": 6
      },
      "item-11575": {
        "value": 4,
        "weight": 2
      },
      "item-11576": {
        "value": 8,
        "weight": 2
      },
      "item-11577": {
        "value": 4,
        "weight": 8
      },
      "item-11578": {
        "value": 4,
        "weight": 6
      },
      "item-11579": {
        "value": 8,
        "weight": 3
      },
      "item-11580": {
        "value": 9,
        "weight": 9
      },
      "item-11581": {
        "value": 6,
        "weight": 1
      },
      "item-11582": {
        "value": 7,
        "weight": 3
      },
      "item-11583": {
        "value": 2,
        "weight": 9
      },
      "item-11584": {
        "value": 7,
        "weight": 9
      },
      "item-11585": {
        "value": 2,
        "weight": 9
      },
      "item-11586": {
        "value": 9,
        "weight": 9
      },
      "item-11587": {
        "value": 5,
        "weight": 4
      },
      "item-11588": {
        "value": 2,
        "weight": 8
      },
      "item-11589": {
        "value": 4,
        "weight": 5
      },
      "item-11590": {
        "value": 4,
        "weight": 6
      },
      "item-11591": {
        "value": 3,
        "weight": 1
      },
      "item-11592": {
        "value": 3,
        "weight": 4
      },
      "item-11593": {
        "value": 2,
        "weight": 9
      },
      "item-11594": {
        "value": 1,
        "weight": 8
      },
      "item-11595": {
        "value": 5,
        "weight": 7
      },
      "item-11596": {
        "value": 7,
        "weight": 8
      },
      "item-11597": {
        "value": 3,
        "weight": 1
      },
      "item-11598": {
        "value": 7,
        "weight": 2
      },
      "item-11599": {
        "value": 6,
        "weight": 4
      },
      "item-11600": {
        "value": 4,
        "weight": 8
      },
      "item-11601": {
        "value": 5,
        "weight": 1
      },
      "item-11602": {
        "value": 5,
        "weight": 6
      },
      "item-11603": {
        "value": 7,
        "weight": 6
      },
      "item-11604": {
        "value": 6,
        "weight": 6
      },
      "item-11605": {
        "value": 9,
        "weight": 4
      },
      "item-11606": {
        "value": 1,
        "weight": 5
      },
      "item-11607": {
        "value": 5,
        "weight": 1
      },
      "item-11608": {
        "value": 2,
        "weight": 1
      },
      "item-11609": {
        "value": 7,
        "weight": 5
      },
      "item-11610": {
        "value": 1,
        "weight": 3
      },
      "item-11611": {
        "value": 2,
        "weight": 6
      },
      "item-11612": {
        "value": 3,
        "weight": 3
      },
      "item-11613": {
        "value": 6,
        "weight": 9
      },
      "item-11614": {
        "value": 8,
        "weight": 4
      },
      "item-11615": {
        "value": 5,
        "weight": 6
      },
      "item-11616": {
        "value": 4,
        "weight": 3
      },
      "item-11617": {
        "value": 2,
        "weight": 4
      },
      "item-11618": {
        "value": 5,
        "weight": 6
      },
      "item-11619": {
        "value": 4,
        "weight": 5
      },
      "item-11620": {
        "value": 5,
        "weight": 2
      },
      "item-11621": {
        "value": 4,
        "weight": 6
      },
      "item-11622": {
        "value": 4,
        "weight": 2
      },
      "item-11623": {
        "value": 1,
        "weight": 3
      },
      "item-11624": {
        "value": 8,
        "weight": 7
      },
      "item-11625": {
        "value": 3,
        "weight": 1
      },
      "item-11626": {
        "value": 7,
        "weight": 1
      },
      "item-11627": {
        "value": 8,
        "weight": 9
      },
      "item-11628": {
        "value": 2,
        "weight": 5
      },
      "item-11629": {
        "value": 7,
        "weight": 3
      },
      "item-11630": {
        "value": 2,
        "weight": 9
      },
      "item-11631": {
        "value": 2,
        "weight": 5
      },
      "item-11632": {
        "value": 2,
        "weight": 6
      },
      "item-11633": {
        "value": 4,
        "weight": 4
      },
      "item-11634": {
        "value": 9,
        "weight": 5
      },
      "item-11635": {
        "value": 1,
        "weight": 1
      },
      "item-11636": {
        "value": 8,
        "weight": 7
      },
      "item-11637": {
        "value": 9,
        "weight": 8
      },
      "item-11638": {
        "value": 1,
        "weight": 9
      },
      "item-11639": {
        "value": 1,
        "weight": 1
      },
      "item-11640": {
        "value": 9,
        "weight": 2
      },
      "item-11641": {
        "value": 9,
        "weight": 7
      },
      "item-11642": {
        "value": 8,
        "weight": 8
      },
      "item-11643": {
        "value": 1,
        "weight": 3
      },
      "item-11644": {
        "value": 6,
        "weight": 7
      },
      "item-11645": {
        "value": 9,
        "weight": 4
      },
      "item-11646": {
        "value": 3,
        "weight": 3
      },
      "item-11647": {
        "value": 4,
        "weight": 6
      },
      "item-11648": {
        "value": 4,
        "weight": 4
      },
      "item-11649": {
        "value": 5,
        "weight": 1
      },
      "item-11650": {
        "value": 8,
        "weight": 4
      },
      "item-11651": {
        "value": 2,
        "weight": 8
      },
      "item-11652": {
        "value": 3,
        "weight": 7
      },
      "item-11653": {
        "value": 2,
        "weight": 1
      },
      "item-11654": {
        "value": 7,
        "weight": 1
      },
      "item-11655": {
        "value": 9,
        "weight": 3
      },
      "item-11656": {
        "value": 3,
        "weight": 4
      },
      "item-11657": {
        "value": 6,
        "weight": 7
      },
      "item-11658": {
        "value": 8,
        "weight": 4
      },
      "item-11659": {
        "value": 3,
        "weight": 3
      },
      "item-11660": {
        "value": 2,
        "weight": 5
      },
      "item-11661": {
        "value": 8,
        "weight": 8
      },
      "item-11662": {
        "value": 2,
        "weight": 1
      },
      "item-11663": {
        "value": 7,
        "weight": 7
      },
      "item-11664": {
        "value": 3,
        "weight": 6
      },
      "item-11665": {
        "value": 8,
        "weight": 7
      },
      "item-11666": {
        "value": 2,
        "weight": 6
      },
      "item-11667": {
        "value": 4,
        "weight": 8
      },
      "item-11668": {
        "value": 3,
        "weight": 7
      },
      "item-11669": {
        "value": 4,
        "weight": 2
      },
      "item-11670": {
        "value": 2,
        "weight": 8
      },
      "item-11671": {
        "value": 6,
        "weight": 5
      },
      "item-11672": {
        "value": 1,
        "weight": 2
      },
      "item-11673": {
        "value": 5,
        "weight": 9
      },
      "item-11674": {
        "value": 2,
        "weight": 5
      },
      "item-11675": {
        "value": 2,
        "weight": 7
      },
      "item-11676": {
        "value": 1,
        "weight": 1
      },
      "item-11677": {
        "value": 9,
        "weight": 1
      },
      "item-11678": {
        "value": 8,
        "weight": 5
      },
      "item-11679": {
        "value": 1,
        "weight": 5
      },
      "item-11680": {
        "value": 8,
        "weight": 7
      },
      "item-11681": {
        "value": 7,
        "weight": 2
      },
      "item-11682": {
        "value": 7,
        "weight": 8
      },
      "item-11683": {
        "value": 4,
        "weight": 1
      },
      "item-11684": {
        "value": 2,
        "weight": 3
      },
      "item-11685": {
        "value": 8,
        "weight": 2
      },
      "item-11686": {
        "value": 7,
        "weight": 5
      },
      "item-11687": {
        "value": 2,
        "weight": 7
      },
      "item-11688": {
        "value": 3,
        "weight": 4
      },
      "item-11689": {
        "value": 7,
        "weight": 7
      },
      "item-11690": {
        "value": 3,
        "weight": 4
      },
      "item-11691": {
        "value": 2,
        "weight": 6
      },
      "item-11692": {
        "value": 7,
        "weight": 1
      },
      "item-11693": {
        "value": 2,
        "weight": 5
      },
      "item-11694": {
        "value": 3,
        "weight": 6
      },
      "item-11695": {
        "value": 7,
        "weight": 1
      },
      "item-11696": {
        "value": 3,
        "weight": 1
      },
      "item-11697": {
        "value": 7,
        "weight": 2
      },
      "item-11698": {
        "value": 4,
        "weight": 5
      },
      "item-11699": {
        "value": 5,
        "weight": 3
      },
      "item-11700": {
        "value": 6,
        "weight": 2
      },
      "item-11701": {
        "value": 3,
        "weight": 4
      },
      "item-11702": {
        "value": 2,
        "weight": 4
      },
      "item-11703": {
        "value": 5,
        "weight": 3
      },
      "item-11704": {
        "value": 3,
        "weight": 4
      },
      "item-11705": {
        "value": 4,
        "weight": 9
      },
      "item-11706": {
        "value": 1,
        "weight": 7
      },
      "item-11707": {
        "value": 8,
        "weight": 5
      },
      "item-11708": {
        "value": 9,
        "weight": 6
      },
      "item-11709": {
        "value": 2,
        "weight": 4
      },
      "item-11710": {
        "value": 4,
        "weight": 7
      },
      "item-11711": {
        "value": 2,
        "weight": 4
      },
      "item-11712": {
        "value": 6,
        "weight": 2
      },
      "item-11713": {
        "value": 1,
        "weight": 7
      },
      "item-11714": {
        "value": 9,
        "weight": 3
      },
      "item-11715": {
        "value": 4,
        "weight": 4
      },
      "item-11716": {
        "value": 2,
        "weight": 7
      },
      "item-11717": {
        "value": 2,
        "weight": 8
      },
      "item-11718": {
        "value": 5,
        "weight": 5
      },
      "item-11719": {
        "value": 8,
        "weight": 9
      },
      "item-11720": {
        "value": 5,
        "weight": 6
      },
      "item-11721": {
        "value": 6,
        "weight": 5
      },
      "item-11722": {
        "value": 2,
        "weight": 9
      },
      "item-11723": {
        "value": 8,
        "weight": 9
      },
      "item-11724": {
        "value": 3,
        "weight": 2
      },
      "item-11725": {
        "value": 1,
        "weight": 9
      },
      "item-11726": {
        "value": 3,
        "weight": 6
      },
      "item-11727": {
        "value": 2,
        "weight": 1
      },
      "item-11728": {
        "value": 6,
        "weight": 9
      },
      "item-11729": {
        "value": 1,
        "weight": 8
      },
      "item-11730": {
        "value": 4,
        "weight": 9
      },
      "item-11731": {
        "value": 1,
        "weight": 3
      },
      "item-11732": {
        "value": 8,
        "weight": 7
      },
      "item-11733": {
        "value": 5,
        "weight": 5
      },
      "item-11734": {
        "value": 9,
        "weight": 9
      },
      "item-11735": {
        "value": 5,
        "weight": 3
      },
      "item-11736": {
        "value": 1,
        "weight": 1
      },
      "item-11737": {
        "value": 1,
        "weight": 2
      },
      "item-11738": {
        "value": 6,
        "weight": 3
      },
      "item-11739": {
        "value": 2,
        "weight": 3
      },
      "item-11740": {
        "value": 7,
        "weight": 5
      },
      "item-11741": {
        "value": 3,
        "weight": 9
      },
      "item-11742": {
        "value": 5,
        "weight": 7
      },
      "item-11743": {
        "value": 2,
        "weight": 4
      },
      "item-11744": {
        "value": 6,
        "weight": 3
      },
      "item-11745": {
        "value": 9,
        "weight": 6
      },
      "item-11746": {
        "value": 4,
        "weight": 1
      },
      "item-11747": {
        "value": 7,
        "weight": 7
      },
      "item-11748": {
        "value": 3,
        "weight": 1
      },
      "item-11749": {
        "value": 2,
        "weight": 6
      },
      "item-11750": {
        "value": 5,
        "weight": 1
      },
      "item-11751": {
        "value": 2,
        "weight": 1
      },
      "item-11752": {
        "value": 6,
        "weight": 4
      },
      "item-11753": {
        "value": 5,
        "weight": 9
      },
      "item-11754": {
        "value": 7,
        "weight": 7
      },
      "item-11755": {
        "value": 1,
        "weight": 3
      },
      "item-11756": {
        "value": 5,
        "weight": 2
      },
      "item-11757": {
        "value": 4,
        "weight": 6
      },
      "item-11758": {
        "value": 2,
        "weight": 7
      },
      "item-11759": {
        "value": 1,
        "weight": 1
      },
      "item-11760": {
        "value": 1,
        "weight": 7
      },
      "item-11761": {
        "value": 9,
        "weight": 1
      },
      "item-11762": {
        "value": 4,
        "weight": 7
      },
      "item-11763": {
        "value": 2,
        "weight": 5
      },
      "item-11764": {
        "value": 5,
        "weight": 5
      },
      "item-11765": {
        "value": 2,
        "weight": 3
      },
      "item-11766": {
        "value": 9,
        "weight": 5
      },
      "item-11767": {
        "value": 6,
        "weight": 5
      },
      "item-11768": {
        "value": 1,
        "weight": 8
      },
      "item-11769": {
        "value": 6,
        "weight": 2
      },
      "item-11770": {
        "value": 2,
        "weight": 6
      },
      "item-11771": {
        "value": 7,
        "weight": 5
      },
      "item-11772": {
        "value": 8,
        "weight": 1
      },
      "item-11773": {
        "value": 4,
        "weight": 2
      },
      "item-11774": {
        "value": 7,
        "weight": 9
      },
      "item-11775": {
        "value": 9,
        "weight": 7
      },
      "item-11776": {
        "value": 1,
        "weight": 1
      },
      "item-11777": {
        "value": 6,
        "weight": 2
      },
      "item-11778": {
        "value": 3,
        "weight": 4
      },
      "item-11779": {
        "value": 2,
        "weight": 5
      },
      "item-11780": {
        "value": 1,
        "weight": 2
      },
      "item-11781": {
        "value": 5,
        "weight": 8
      },
      "item-11782": {
        "value": 6,
        "weight": 7
      },
      "item-11783": {
        "value": 7,
        "weight": 2
      },
      "item-11784": {
        "value": 4,
        "weight": 3
      },
      "item-11785": {
        "value": 4,
        "weight": 1
      },
      "item-11786": {
        "value": 8,
        "weight": 3
      },
      "item-11787": {
        "value": 6,
        "weight": 9
      },
      "item-11788": {
        "value": 9,
        "weight": 8
      },
      "item-11789": {
        "value": 1,
        "weight": 7
      },
      "item-11790": {
        "value": 6,
        "weight": 5
      },
      "item-11791": {
        "value": 6,
        "weight": 1
      },
      "item-11792": {
        "value": 8,
        "weight": 7
      },
      "item-11793": {
        "value": 1,
        "weight": 9
      },
      "item-11794": {
        "value": 6,
        "weight": 2
      },
      "item-11795": {
        "value": 7,
        "weight": 4
      },
      "item-11796": {
        "value": 2,
        "weight": 1
      },
      "item-11797": {
        "value": 5,
        "weight": 1
      },
      "item-11798": {
        "value": 8,
        "weight": 2
      },
      "item-11799": {
        "value": 3,
        "weight": 5
      },
      "item-11800": {
        "value": 2,
        "weight": 1
      },
      "item-11801": {
        "value": 8,
        "weight": 1
      },
      "item-11802": {
        "value": 6,
        "weight": 8
      },
      "item-11803": {
        "value": 4,
        "weight": 2
      },
      "item-11804": {
        "value": 5,
        "weight": 7
      },
      "item-11805": {
        "value": 8,
        "weight": 7
      },
      "item-11806": {
        "value": 7,
        "weight": 3
      },
      "item-11807": {
        "value": 7,
        "weight": 7
      },
      "item-11808": {
        "value": 6,
        "weight": 9
      },
      "item-11809": {
        "value": 8,
        "weight": 1
      },
      "item-11810": {
        "value": 7,
        "weight": 1
      },
      "item-11811": {
        "value": 8,
        "weight": 6
      },
      "item-11812": {
        "value": 2,
        "weight": 2
      },
      "item-11813": {
        "value": 4,
        "weight": 3
      },
      "item-11814": {
        "value": 9,
        "weight": 2
      },
      "item-11815": {
        "value": 5,
        "weight": 4
      },
      "item-11816": {
        "value": 3,
        "weight": 3
      },
      "item-11817": {
        "value": 8,
        "weight": 8
      },
      "item-11818": {
        "value": 1,
        "weight": 4
      },
      "item-11819": {
        "value": 3,
        "weight": 7
      },
      "item-11820": {
        "value": 8,
        "weight": 6
      },
      "item-11821": {
        "value": 2,
        "weight": 1
      },
      "item-11822": {
        "value": 8,
        "weight": 4
      },
      "item-11823": {
        "value": 9,
        "weight": 2
      },
      "item-11824": {
        "value": 8,
        "weight": 3
      },
      "item-11825": {
        "value": 2,
        "weight": 5
      },
      "item-11826": {
        "value": 7,
        "weight": 9
      },
      "item-11827": {
        "value": 6,
        "weight": 6
      },
      "item-11828": {
        "value": 5,
        "weight": 1
      },
      "item-11829": {
        "value": 6,
        "weight": 8
      },
      "item-11830": {
        "value": 4,
        "weight": 7
      },
      "item-11831": {
        "value": 9,
        "weight": 1
      },
      "item-11832": {
        "value": 5,
        "weight": 5
      },
      "item-11833": {
        "value": 2,
        "weight": 4
      },
      "item-11834": {
        "value": 8,
        "weight": 9
      },
      "item-11835": {
        "value": 6,
        "weight": 1
      },
      "item-11836": {
        "value": 7,
        "weight": 2
      },
      "item-11837": {
        "value": 6,
        "weight": 3
      },
      "item-11838": {
        "value": 1,
        "weight": 6
      },
      "item-11839": {
        "value": 8,
        "weight": 9
      },
      "item-11840": {
        "value": 7,
        "weight": 9
      },
      "item-11841": {
        "value": 2,
        "weight": 5
      },
      "item-11842": {
        "value": 8,
        "weight": 1
      },
      "item-11843": {
        "value": 5,
        "weight": 2
      },
      "item-11844": {
        "value": 5,
        "weight": 6
      },
      "item-11845": {
        "value": 7,
        "weight": 4
      },
      "item-11846": {
        "value": 1,
        "weight": 7
      },
      "item-11847": {
        "value": 3,
        "weight": 3
      },
      "item-11848": {
        "value": 8,
        "weight": 5
      },
      "item-11849": {
        "value": 6,
        "weight": 6
      },
      "item-11850": {
        "value": 9,
        "weight": 7
      },
      "item-11851": {
        "value": 1,
        "weight": 9
      },
      "item-11852": {
        "value": 2,
        "weight": 4
      },
      "item-11853": {
        "value": 6,
        "weight": 1
      },
      "item-11854": {
        "value": 6,
        "weight": 6
      },
      "item-11855": {
        "value": 2,
        "weight": 8
      },
      "item-11856": {
        "value": 3,
        "weight": 2
      },
      "item-11857": {
        "value": 4,
        "weight": 6
      },
      "item-11858": {
        "value": 6,
        "weight": 3
      },
      "item-11859": {
        "value": 4,
        "weight": 4
      },
      "item-11860": {
        "value": 2,
        "weight": 3
      },
      "item-11861": {
        "value": 8,
        "weight": 1
      },
      "item-11862": {
        "value": 5,
        "weight": 2
      },
      "item-11863": {
        "value": 4,
        "weight": 2
      },
      "item-11864": {
        "value": 3,
        "weight": 5
      },
      "item-11865": {
        "value": 1,
        "weight": 3
      },
      "item-11866": {
        "value": 2,
        "weight": 4
      },
      "item-11867": {
        "value": 3,
        "weight": 2
      },
      "item-11868": {
        "value": 3,
        "weight": 6
      },
      "item-11869": {
        "value": 8,
        "weight": 5
      },
      "item-11870": {
        "value": 8,
        "weight": 4
      },
      "item-11871": {
        "value": 1,
        "weight": 9
      },
      "item-11872": {
        "value": 9,
        "weight": 2
      },
      "item-11873": {
        "value": 6,
        "weight": 4
      },
      "item-11874": {
        "value": 3,
        "weight": 8
      },
      "item-11875": {
        "value": 6,
        "weight": 1
      },
      "item-11876": {
        "value": 3,
        "weight": 2
      },
      "item-11877": {
        "value": 7,
        "weight": 9
      },
      "item-11878": {
        "value": 4,
        "weight": 7
      },
      "item-11879": {
        "value": 5,
        "weight": 1
      },
      "item-11880": {
        "value": 3,
        "weight": 9
      },
      "item-11881": {
        "value": 7,
        "weight": 4
      },
      "item-11882": {
        "value": 2,
        "weight": 5
      },
      "item-11883": {
        "value": 9,
        "weight": 5
      },
      "item-11884": {
        "value": 7,
        "weight": 7
      },
      "item-11885": {
        "value": 6,
        "weight": 7
      },
      "item-11886": {
        "value": 9,
        "weight": 7
      },
      "item-11887": {
        "value": 9,
        "weight": 9
      },
      "item-11888": {
        "value": 2,
        "weight": 8
      },
      "item-11889": {
        "value": 6,
        "weight": 5
      },
      "item-11890": {
        "value": 3,
        "weight": 3
      },
      "item-11891": {
        "value": 5,
        "weight": 9
      },
      "item-11892": {
        "value": 5,
        "weight": 2
      },
      "item-11893": {
        "value": 9,
        "weight": 6
      },
      "item-11894": {
        "value": 4,
        "weight": 3
      },
      "item-11895": {
        "value": 8,
        "weight": 9
      },
      "item-11896": {
        "value": 1,
        "weight": 4
      },
      "item-11897": {
        "value": 5,
        "weight": 5
      },
      "item-11898": {
        "value": 6,
        "weight": 1
      },
      "item-11899": {
        "value": 6,
        "weight": 5
      },
      "item-11900": {
        "value": 9,
        "weight": 6
      },
      "item-11901": {
        "value": 6,
        "weight": 2
      },
      "item-11902": {
        "value": 5,
        "weight": 3
      },
      "item-11903": {
        "value": 1,
        "weight": 9
      },
      "item-11904": {
        "value": 6,
        "weight": 8
      },
      "item-11905": {
        "value": 7,
        "weight": 4
      },
      "item-11906": {
        "value": 1,
        "weight": 3
      },
      "item-11907": {
        "value": 5,
        "weight": 9
      },
      "item-11908": {
        "value": 6,
        "weight": 6
      },
      "item-11909": {
        "value": 9,
        "weight": 8
      },
      "item-11910": {
        "value": 2,
        "weight": 9
      },
      "item-11911": {
        "value": 5,
        "weight": 6
      },
      "item-11912": {
        "value": 3,
        "weight": 4
      },
      "item-11913": {
        "value": 8,
        "weight": 2
      },
      "item-11914": {
        "value": 1,
        "weight": 3
      },
      "item-11915": {
        "value": 2,
        "weight": 8
      },
      "item-11916": {
        "value": 6,
        "weight": 5
      },
      "item-11917": {
        "value": 7,
        "weight": 1
      },
      "item-11918": {
        "value": 9,
        "weight": 9
      },
      "item-11919": {
        "value": 3,
        "weight": 7
      },
      "item-11920": {
        "value": 9,
        "weight": 6
      },
      "item-11921": {
        "value": 6,
        "weight": 3
      },
      "item-11922": {
        "value": 9,
        "weight": 7
      },
      "item-11923": {
        "value": 4,
        "weight": 8
      },
      "item-11924": {
        "value": 7,
        "weight": 4
      },
      "item-11925": {
        "value": 6,
        "weight": 9
      },
      "item-11926": {
        "value": 7,
        "weight": 3
      },
      "item-11927": {
        "value": 6,
        "weight": 9
      },
      "item-11928": {
        "value": 3,
        "weight": 8
      },
      "item-11929": {
        "value": 3,
        "weight": 8
      },
      "item-11930": {
        "value": 9,
        "weight": 8
      },
      "item-11931": {
        "value": 3,
        "weight": 7
      },
      "item-11932": {
        "value": 7,
        "weight": 7
      },
      "item-11933": {
        "value": 8,
        "weight": 1
      },
      "item-11934": {
        "value": 7,
        "weight": 4
      },
      "item-11935": {
        "value": 9,
        "weight": 7
      },
      "item-11936": {
        "value": 5,
        "weight": 4
      },
      "item-11937": {
        "value": 9,
        "weight": 8
      },
      "item-11938": {
        "value": 3,
        "weight": 6
      },
      "item-11939": {
        "value": 1,
        "weight": 8
      },
      "item-11940": {
        "value": 3,
        "weight": 6
      },
      "item-11941": {
        "value": 8,
        "weight": 5
      },
      "item-11942": {
        "value": 6,
        "weight": 7
      },
      "item-11943": {
        "value": 3,
        "weight": 7
      },
      "item-11944": {
        "value": 9,
        "weight": 9
      },
      "item-11945": {
        "value": 6,
        "weight": 6
      },
      "item-11946": {
        "value": 9,
        "weight": 4
      },
      "item-11947": {
        "value": 7,
        "weight": 9
      },
      "item-11948": {
        "value": 7,
        "weight": 7
      },
      "item-11949": {
        "value": 5,
        "weight": 9
      },
      "item-11950": {
        "value": 5,
        "weight": 7
      },
      "item-11951": {
        "value": 7,
        "weight": 9
      },
      "item-11952": {
        "value": 2,
        "weight": 3
      },
      "item-11953": {
        "value": 9,
        "weight": 3
      },
      "item-11954": {
        "value": 6,
        "weight": 4
      },
      "item-11955": {
        "value": 8,
        "weight": 7
      },
      "item-11956": {
        "value": 4,
        "weight": 6
      },
      "item-11957": {
        "value": 2,
        "weight": 1
      },
      "item-11958": {
        "value": 7,
        "weight": 9
      },
      "item-11959": {
        "value": 4,
        "weight": 5
      },
      "item-11960": {
        "value": 8,
        "weight": 3
      },
      "item-11961": {
        "value": 6,
        "weight": 6
      },
      "item-11962": {
        "value": 3,
        "weight": 5
      },
      "item-11963": {
        "value": 3,
        "weight": 8
      },
      "item-11964": {
        "value": 2,
        "weight": 6
      },
      "item-11965": {
        "value": 7,
        "weight": 7
      },
      "item-11966": {
        "value": 4,
        "weight": 2
      },
      "item-11967": {
        "value": 1,
        "weight": 3
      },
      "item-11968": {
        "value": 1,
        "weight": 6
      },
      "item-11969": {
        "value": 4,
        "weight": 6
      },
      "item-11970": {
        "value": 8,
        "weight": 9
      },
      "item-11971": {
        "value": 9,
        "weight": 2
      },
      "item-11972": {
        "value": 8,
        "weight": 7
      },
      "item-11973": {
        "value": 6,
        "weight": 6
      },
      "item-11974": {
        "value": 5,
        "weight": 1
      },
      "item-11975": {
        "value": 3,
        "weight": 8
      },
      "item-11976": {
        "value": 4,
        "weight": 4
      },
      "item-11977": {
        "value": 1,
        "weight": 8
      },
      "item-11978": {
        "value": 3,
        "weight": 3
      },
      "item-11979": {
        "value": 4,
        "weight": 5
      },
      "item-11980": {
        "value": 8,
        "weight": 7
      },
      "item-11981": {
        "value": 2,
        "weight": 5
      },
      "item-11982": {
        "value": 7,
        "weight": 5
      },
      "item-11983": {
        "value": 1,
        "weight": 3
      },
      "item-11984": {
        "value": 4,
        "weight": 5
      },
      "item-11985": {
        "value": 3,
        "weight": 8
      },
      "item-11986": {
        "value": 6,
        "weight": 6
      },
      "item-11987": {
        "value": 9,
        "weight": 6
      },
      "item-11988": {
        "value": 1,
        "weight": 6
      },
      "item-11989": {
        "value": 3,
        "weight": 8
      },
      "item-11990": {
        "value": 6,
        "weight": 8
      },
      "item-11991": {
        "value": 7,
        "weight": 8
      },
      "item-11992": {
        "value": 7,
        "weight": 8
      },
      "item-11993": {
        "value": 1,
        "weight": 9
      },
      "item-11994": {
        "value": 9,
        "weight": 3
      },
      "item-11995": {
        "value": 8,
        "weight": 9
      },
      "item-11996": {
        "value": 3,
        "weight": 7
      },
      "item-11997": {
        "value": 5,
        "weight": 7
      },
      "item-11998": {
        "value": 7,
        "weight": 5
      },
      "item-11999": {
        "value": 7,
        "weight": 2
      },
      "item-12000": {
        "value": 9,
        "weight": 6
      },
      "item-12001": {
        "value": 4,
        "weight": 9
      },
      "item-12002": {
        "value": 6,
        "weight": 4
      },
      "item-12003": {
        "value": 6,
        "weight": 5
      },
      "item-12004": {
        "value": 2,
        "weight": 9
      },
      "item-12005": {
        "value": 4,
        "weight": 4
      },
      "item-12006": {
        "value": 3,
        "weight": 2
      },
      "item-12007": {
        "value": 3,
        "weight": 7
      },
      "item-12008": {
        "value": 6,
        "weight": 3
      },
      "item-12009": {
        "value": 1,
        "weight": 2
      },
      "item-12010": {
        "value": 6,
        "weight": 7
      },
      "item-12011": {
        "value": 9,
        "weight": 2
      },
      "item-12012": {
        "value": 3,
        "weight": 5
      },
      "item-12013": {
        "value": 7,
        "weight": 3
      },
      "item-12014": {
        "value": 5,
        "weight": 6
      },
      "item-12015": {
        "value": 4,
        "weight": 5
      },
      "item-12016": {
        "value": 3,
        "weight": 5
      },
      "item-12017": {
        "value": 7,
        "weight": 3
      },
      "item-12018": {
        "value": 6,
        "weight": 3
      },
      "item-12019": {
        "value": 3,
        "weight": 6
      },
      "item-12020": {
        "value": 6,
        "weight": 5
      },
      "item-12021": {
        "value": 2,
        "weight": 1
      },
      "item-12022": {
        "value": 4,
        "weight": 6
      },
      "item-12023": {
        "value": 7,
        "weight": 2
      },
      "item-12024": {
        "value": 8,
        "weight": 1
      },
      "item-12025": {
        "value": 1,
        "weight": 8
      },
      "item-12026": {
        "value": 7,
        "weight": 1
      },
      "item-12027": {
        "value": 8,
        "weight": 6
      },
      "item-12028": {
        "value": 6,
        "weight": 5
      },
      "item-12029": {
        "value": 8,
        "weight": 5
      },
      "item-12030": {
        "value": 4,
        "weight": 6
      },
      "item-12031": {
        "value": 4,
        "weight": 3
      },
      "item-12032": {
        "value": 5,
        "weight": 9
      },
      "item-12033": {
        "value": 9,
        "weight": 5
      },
      "item-12034": {
        "value": 4,
        "weight": 9
      },
      "item-12035": {
        "value": 6,
        "weight": 1
      },
      "item-12036": {
        "value": 5,
        "weight": 9
      },
      "item-12037": {
        "value": 4,
        "weight": 2
      },
      "item-12038": {
        "value": 4,
        "weight": 6
      },
      "item-12039": {
        "value": 9,
        "weight": 4
      },
      "item-12040": {
        "value": 7,
        "weight": 7
      },
      "item-12041": {
        "value": 4,
        "weight": 5
      },
      "item-12042": {
        "value": 1,
        "weight": 4
      },
      "item-12043": {
        "value": 4,
        "weight": 5
      },
      "item-12044": {
        "value": 8,
        "weight": 8
      },
      "item-12045": {
        "value": 2,
        "weight": 9
      },
      "item-12046": {
        "value": 7,
        "weight": 2
      },
      "item-12047": {
        "value": 2,
        "weight": 7
      },
      "item-12048": {
        "value": 4,
        "weight": 2
      },
      "item-12049": {
        "value": 5,
        "weight": 9
      },
      "item-12050": {
        "value": 8,
        "weight": 4
      },
      "item-12051": {
        "value": 9,
        "weight": 7
      },
      "item-12052": {
        "value": 8,
        "weight": 8
      },
      "item-12053": {
        "value": 4,
        "weight": 1
      },
      "item-12054": {
        "value": 9,
        "weight": 3
      },
      "item-12055": {
        "value": 4,
        "weight": 7
      },
      "item-12056": {
        "value": 9,
        "weight": 5
      },
      "item-12057": {
        "value": 2,
        "weight": 2
      },
      "item-12058": {
        "value": 6,
        "weight": 4
      },
      "item-12059": {
        "value": 5,
        "weight": 1
      },
      "item-12060": {
        "value": 3,
        "weight": 6
      },
      "item-12061": {
        "value": 2,
        "weight": 1
      },
      "item-12062": {
        "value": 6,
        "weight": 6
      },
      "item-12063": {
        "value": 8,
        "weight": 9
      },
      "item-12064": {
        "value": 7,
        "weight": 3
      },
      "item-12065": {
        "value": 5,
        "weight": 7
      },
      "item-12066": {
        "value": 7,
        "weight": 1
      },
      "item-12067": {
        "value": 9,
        "weight": 4
      },
      "item-12068": {
        "value": 3,
        "weight": 8
      },
      "item-12069": {
        "value": 1,
        "weight": 9
      },
      "item-12070": {
        "value": 5,
        "weight": 6
      },
      "item-12071": {
        "value": 9,
        "weight": 5
      },
      "item-12072": {
        "value": 4,
        "weight": 6
      },
      "item-12073": {
        "value": 7,
        "weight": 7
      },
      "item-12074": {
        "value": 3,
        "weight": 5
      },
      "item-12075": {
        "value": 4,
        "weight": 7
      },
      "item-12076": {
        "value": 6,
        "weight": 4
      },
      "item-12077": {
        "value": 8,
        "weight": 8
      },
      "item-12078": {
        "value": 2,
        "weight": 9
      },
      "item-12079": {
        "value": 5,
        "weight": 7
      },
      "item-12080": {
        "value": 4,
        "weight": 7
      },
      "item-12081": {
        "value": 9,
        "weight": 9
      },
      "item-12082": {
        "value": 9,
        "weight": 7
      },
      "item-12083": {
        "value": 2,
        "weight": 5
      },
      "item-12084": {
        "value": 6,
        "weight": 7
      },
      "item-12085": {
        "value": 2,
        "weight": 1
      },
      "item-12086": {
        "value": 1,
        "weight": 6
      },
      "item-12087": {
        "value": 9,
        "weight": 6
      },
      "item-12088": {
        "value": 6,
        "weight": 8
      },
      "item-12089": {
        "value": 3,
        "weight": 6
      },
      "item-12090": {
        "value": 7,
        "weight": 5
      },
      "item-12091": {
        "value": 1,
        "weight": 2
      },
      "item-12092": {
        "value": 2,
        "weight": 3
      },
      "item-12093": {
        "value": 9,
        "weight": 8
      },
      "item-12094": {
        "value": 7,
        "weight": 9
      },
      "item-12095": {
        "value": 3,
        "weight": 5
      },
      "item-12096": {
        "value": 3,
        "weight": 5
      },
      "item-12097": {
        "value": 7,
        "weight": 8
      },
      "item-12098": {
        "value": 6,
        "weight": 4
      },
      "item-12099": {
        "value": 2,
        "weight": 1
      },
      "item-12100": {
        "value": 4,
        "weight": 2
      },
      "item-12101": {
        "value": 6,
        "weight": 4
      },
      "item-12102": {
        "value": 5,
        "weight": 8
      },
      "item-12103": {
        "value": 8,
        "weight": 7
      },
      "item-12104": {
        "value": 3,
        "weight": 6
      },
      "item-12105": {
        "value": 2,
        "weight": 9
      },
      "item-12106": {
        "value": 2,
        "weight": 3
      },
      "item-12107": {
        "value": 8,
        "weight": 3
      },
      "item-12108": {
        "value": 8,
        "weight": 6
      },
      "item-12109": {
        "value": 8,
        "weight": 9
      },
      "item-12110": {
        "value": 3,
        "weight": 4
      },
      "item-12111": {
        "value": 8,
        "weight": 9
      },
      "item-12112": {
        "value": 2,
        "weight": 8
      },
      "item-12113": {
        "value": 1,
        "weight": 1
      },
      "item-12114": {
        "value": 2,
        "weight": 6
      },
      "item-12115": {
        "value": 6,
        "weight": 6
      },
      "item-12116": {
        "value": 7,
        "weight": 8
      },
      "item-12117": {
        "value": 8,
        "weight": 5
      },
      "item-12118": {
        "value": 7,
        "weight": 2
      },
      "item-12119": {
        "value": 8,
        "weight": 3
      },
      "item-12120": {
        "value": 2,
        "weight": 4
      },
      "item-12121": {
        "value": 4,
        "weight": 4
      },
      "item-12122": {
        "value": 9,
        "weight": 9
      },
      "item-12123": {
        "value": 7,
        "weight": 9
      },
      "item-12124": {
        "value": 7,
        "weight": 1
      },
      "item-12125": {
        "value": 9,
        "weight": 5
      },
      "item-12126": {
        "value": 9,
        "weight": 9
      },
      "item-12127": {
        "value": 2,
        "weight": 7
      },
      "item-12128": {
        "value": 5,
        "weight": 6
      },
      "item-12129": {
        "value": 9,
        "weight": 9
      },
      "item-12130": {
        "value": 3,
        "weight": 4
      },
      "item-12131": {
        "value": 2,
        "weight": 4
      },
      "item-12132": {
        "value": 8,
        "weight": 9
      },
      "item-12133": {
        "value": 3,
        "weight": 6
      },
      "item-12134": {
        "value": 8,
        "weight": 1
      },
      "item-12135": {
        "value": 8,
        "weight": 7
      },
      "item-12136": {
        "value": 8,
        "weight": 1
      },
      "item-12137": {
        "value": 2,
        "weight": 5
      },
      "item-12138": {
        "value": 9,
        "weight": 8
      },
      "item-12139": {
        "value": 3,
        "weight": 2
      },
      "item-12140": {
        "value": 2,
        "weight": 4
      },
      "item-12141": {
        "value": 9,
        "weight": 4
      },
      "item-12142": {
        "value": 1,
        "weight": 8
      },
      "item-12143": {
        "value": 5,
        "weight": 4
      },
      "item-12144": {
        "value": 4,
        "weight": 3
      },
      "item-12145": {
        "value": 5,
        "weight": 9
      },
      "item-12146": {
        "value": 7,
        "weight": 4
      },
      "item-12147": {
        "value": 3,
        "weight": 1
      },
      "item-12148": {
        "value": 2,
        "weight": 8
      },
      "item-12149": {
        "value": 7,
        "weight": 6
      },
      "item-12150": {
        "value": 8,
        "weight": 9
      },
      "item-12151": {
        "value": 4,
        "weight": 7
      },
      "item-12152": {
        "value": 9,
        "weight": 7
      },
      "item-12153": {
        "value": 9,
        "weight": 5
      },
      "item-12154": {
        "value": 6,
        "weight": 9
      },
      "item-12155": {
        "value": 8,
        "weight": 6
      },
      "item-12156": {
        "value": 4,
        "weight": 5
      },
      "item-12157": {
        "value": 3,
        "weight": 3
      },
      "item-12158": {
        "value": 5,
        "weight": 3
      },
      "item-12159": {
        "value": 8,
        "weight": 7
      },
      "item-12160": {
        "value": 7,
        "weight": 3
      },
      "item-12161": {
        "value": 8,
        "weight": 4
      },
      "item-12162": {
        "value": 5,
        "weight": 6
      },
      "item-12163": {
        "value": 6,
        "weight": 6
      },
      "item-12164": {
        "value": 7,
        "weight": 1
      },
      "item-12165": {
        "value": 6,
        "weight": 8
      },
      "item-12166": {
        "value": 7,
        "weight": 4
      },
      "item-12167": {
        "value": 3,
        "weight": 7
      },
      "item-12168": {
        "value": 2,
        "weight": 2
      },
      "item-12169": {
        "value": 2,
        "weight": 4
      },
      "item-12170": {
        "value": 7,
        "weight": 6
      },
      "item-12171": {
        "value": 7,
        "weight": 6
      },
      "item-12172": {
        "value": 7,
        "weight": 3
      },
      "item-12173": {
        "value": 8,
        "weight": 5
      },
      "item-12174": {
        "value": 4,
        "weight": 3
      },
      "item-12175": {
        "value": 7,
        "weight": 4
      },
      "item-12176": {
        "value": 8,
        "weight": 9
      },
      "item-12177": {
        "value": 5,
        "weight": 3
      },
      "item-12178": {
        "value": 1,
        "weight": 9
      },
      "item-12179": {
        "value": 9,
        "weight": 2
      },
      "item-12180": {
        "value": 6,
        "weight": 7
      },
      "item-12181": {
        "value": 6,
        "weight": 4
      },
      "item-12182": {
        "value": 2,
        "weight": 8
      },
      "item-12183": {
        "value": 5,
        "weight": 4
      },
      "item-12184": {
        "value": 4,
        "weight": 8
      },
      "item-12185": {
        "value": 3,
        "weight": 3
      },
      "item-12186": {
        "value": 7,
        "weight": 5
      },
      "item-12187": {
        "value": 8,
        "weight": 9
      },
      "item-12188": {
        "value": 5,
        "weight": 5
      },
      "item-12189": {
        "value": 8,
        "weight": 1
      },
      "item-12190": {
        "value": 9,
        "weight": 8
      },
      "item-12191": {
        "value": 2,
        "weight": 3
      },
      "item-12192": {
        "value": 2,
        "weight": 9
      },
      "item-12193": {
        "value": 1,
        "weight": 1
      },
      "item-12194": {
        "value": 5,
        "weight": 9
      },
      "item-12195": {
        "value": 7,
        "weight": 3
      },
      "item-12196": {
        "value": 7,
        "weight": 8
      },
      "item-12197": {
        "value": 9,
        "weight": 8
      },
      "item-12198": {
        "value": 6,
        "weight": 6
      },
      "item-12199": {
        "value": 8,
        "weight": 4
      },
      "item-12200": {
        "value": 3,
        "weight": 1
      },
      "item-12201": {
        "value": 1,
        "weight": 7
      },
      "item-12202": {
        "value": 3,
        "weight": 9
      },
      "item-12203": {
        "value": 4,
        "weight": 3
      },
      "item-12204": {
        "value": 7,
        "weight": 1
      },
      "item-12205": {
        "value": 3,
        "weight": 1
      },
      "item-12206": {
        "value": 6,
        "weight": 5
      },
      "item-12207": {
        "value": 2,
        "weight": 5
      },
      "item-12208": {
        "value": 3,
        "weight": 5
      },
      "item-12209": {
        "value": 3,
        "weight": 2
      },
      "item-12210": {
        "value": 2,
        "weight": 8
      },
      "item-12211": {
        "value": 9,
        "weight": 2
      },
      "item-12212": {
        "value": 3,
        "weight": 7
      },
      "item-12213": {
        "value": 3,
        "weight": 6
      },
      "item-12214": {
        "value": 6,
        "weight": 9
      },
      "item-12215": {
        "value": 3,
        "weight": 6
      },
      "item-12216": {
        "value": 1,
        "weight": 7
      },
      "item-12217": {
        "value": 9,
        "weight": 4
      },
      "item-12218": {
        "value": 8,
        "weight": 7
      },
      "item-12219": {
        "value": 8,
        "weight": 6
      },
      "item-12220": {
        "value": 9,
        "weight": 5
      },
      "item-12221": {
        "value": 8,
        "weight": 8
      },
      "item-12222": {
        "value": 8,
        "weight": 2
      },
      "item-12223": {
        "value": 4,
        "weight": 3
      },
      "item-12224": {
        "value": 2,
        "weight": 5
      },
      "item-12225": {
        "value": 3,
        "weight": 4
      },
      "item-12226": {
        "value": 4,
        "weight": 2
      },
      "item-12227": {
        "value": 7,
        "weight": 3
      },
      "item-12228": {
        "value": 1,
        "weight": 7
      },
      "item-12229": {
        "value": 4,
        "weight": 8
      },
      "item-12230": {
        "value": 2,
        "weight": 8
      },
      "item-12231": {
        "value": 8,
        "weight": 1
      },
      "item-12232": {
        "value": 8,
        "weight": 1
      },
      "item-12233": {
        "value": 2,
        "weight": 2
      },
      "item-12234": {
        "value": 5,
        "weight": 5
      },
      "item-12235": {
        "value": 9,
        "weight": 9
      },
      "item-12236": {
        "value": 9,
        "weight": 4
      },
      "item-12237": {
        "value": 6,
        "weight": 1
      },
      "item-12238": {
        "value": 2,
        "weight": 3
      },
      "item-12239": {
        "value": 6,
        "weight": 6
      },
      "item-12240": {
        "value": 9,
        "weight": 5
      },
      "item-12241": {
        "value": 8,
        "weight": 2
      },
      "item-12242": {
        "value": 9,
        "weight": 7
      },
      "item-12243": {
        "value": 8,
        "weight": 4
      },
      "item-12244": {
        "value": 9,
        "weight": 3
      },
      "item-12245": {
        "value": 4,
        "weight": 9
      },
      "item-12246": {
        "value": 4,
        "weight": 3
      },
      "item-12247": {
        "value": 9,
        "weight": 2
      },
      "item-12248": {
        "value": 2,
        "weight": 1
      },
      "item-12249": {
        "value": 1,
        "weight": 3
      },
      "item-12250": {
        "value": 2,
        "weight": 2
      },
      "item-12251": {
        "value": 9,
        "weight": 1
      },
      "item-12252": {
        "value": 2,
        "weight": 7
      },
      "item-12253": {
        "value": 6,
        "weight": 3
      },
      "item-12254": {
        "value": 2,
        "weight": 8
      },
      "item-12255": {
        "value": 5,
        "weight": 9
      },
      "item-12256": {
        "value": 6,
        "weight": 5
      },
      "item-12257": {
        "value": 6,
        "weight": 9
      },
      "item-12258": {
        "value": 4,
        "weight": 1
      },
      "item-12259": {
        "value": 6,
        "weight": 1
      },
      "item-12260": {
        "value": 9,
        "weight": 1
      },
      "item-12261": {
        "value": 1,
        "weight": 5
      },
      "item-12262": {
        "value": 5,
        "weight": 4
      },
      "item-12263": {
        "value": 1,
        "weight": 5
      },
      "item-12264": {
        "value": 3,
        "weight": 7
      },
      "item-12265": {
        "value": 3,
        "weight": 1
      },
      "item-12266": {
        "value": 9,
        "weight": 2
      },
      "item-12267": {
        "value": 9,
        "weight": 8
      },
      "item-12268": {
        "value": 7,
        "weight": 9
      },
      "item-12269": {
        "value": 9,
        "weight": 1
      },
      "item-12270": {
        "value": 9,
        "weight": 1
      },
      "item-12271": {
        "value": 9,
        "weight": 6
      },
      "item-12272": {
        "value": 8,
        "weight": 8
      },
      "item-12273": {
        "value": 2,
        "weight": 1
      },
      "item-12274": {
        "value": 8,
        "weight": 7
      },
      "item-12275": {
        "value": 6,
        "weight": 4
      },
      "item-12276": {
        "value": 6,
        "weight": 5
      },
      "item-12277": {
        "value": 9,
        "weight": 4
      },
      "item-12278": {
        "value": 1,
        "weight": 6
      },
      "item-12279": {
        "value": 6,
        "weight": 7
      },
      "item-12280": {
        "value": 6,
        "weight": 1
      },
      "item-12281": {
        "value": 2,
        "weight": 4
      },
      "item-12282": {
        "value": 5,
        "weight": 2
      },
      "item-12283": {
        "value": 3,
        "weight": 9
      },
      "item-12284": {
        "value": 3,
        "weight": 5
      },
      "item-12285": {
        "value": 1,
        "weight": 4
      },
      "item-12286": {
        "value": 3,
        "weight": 3
      },
      "item-12287": {
        "value": 3,
        "weight": 9
      },
      "item-12288": {
        "value": 3,
        "weight": 8
      },
      "item-12289": {
        "value": 7,
        "weight": 4
      },
      "item-12290": {
        "value": 8,
        "weight": 4
      },
      "item-12291": {
        "value": 6,
        "weight": 8
      },
      "item-12292": {
        "value": 4,
        "weight": 6
      },
      "item-12293": {
        "value": 4,
        "weight": 2
      },
      "item-12294": {
        "value": 1,
        "weight": 6
      },
      "item-12295": {
        "value": 1,
        "weight": 5
      },
      "item-12296": {
        "value": 8,
        "weight": 4
      },
      "item-12297": {
        "value": 6,
        "weight": 7
      },
      "item-12298": {
        "value": 4,
        "weight": 3
      },
      "item-12299": {
        "value": 2,
        "weight": 1
      },
      "item-12300": {
        "value": 1,
        "weight": 9
      },
      "item-12301": {
        "value": 3,
        "weight": 6
      },
      "item-12302": {
        "value": 5,
        "weight": 9
      },
      "item-12303": {
        "value": 3,
        "weight": 4
      },
      "item-12304": {
        "value": 6,
        "weight": 1
      },
      "item-12305": {
        "value": 2,
        "weight": 1
      },
      "item-12306": {
        "value": 7,
        "weight": 2
      },
      "item-12307": {
        "value": 4,
        "weight": 6
      },
      "item-12308": {
        "value": 7,
        "weight": 2
      },
      "item-12309": {
        "value": 3,
        "weight": 9
      },
      "item-12310": {
        "value": 2,
        "weight": 5
      },
      "item-12311": {
        "value": 2,
        "weight": 8
      },
      "item-12312": {
        "value": 9,
        "weight": 7
      },
      "item-12313": {
        "value": 6,
        "weight": 5
      },
      "item-12314": {
        "value": 4,
        "weight": 1
      },
      "item-12315": {
        "value": 3,
        "weight": 3
      },
      "item-12316": {
        "value": 1,
        "weight": 1
      },
      "item-12317": {
        "value": 7,
        "weight": 4
      },
      "item-12318": {
        "value": 1,
        "weight": 8
      },
      "item-12319": {
        "value": 8,
        "weight": 3
      },
      "item-12320": {
        "value": 2,
        "weight": 8
      },
      "item-12321": {
        "value": 3,
        "weight": 1
      },
      "item-12322": {
        "value": 5,
        "weight": 3
      },
      "item-12323": {
        "value": 6,
        "weight": 7
      },
      "item-12324": {
        "value": 2,
        "weight": 5
      },
      "item-12325": {
        "value": 7,
        "weight": 3
      },
      "item-12326": {
        "value": 6,
        "weight": 9
      },
      "item-12327": {
        "value": 2,
        "weight": 8
      },
      "item-12328": {
        "value": 3,
        "weight": 3
      },
      "item-12329": {
        "value": 3,
        "weight": 9
      },
      "item-12330": {
        "value": 7,
        "weight": 2
      },
      "item-12331": {
        "value": 1,
        "weight": 6
      },
      "item-12332": {
        "value": 4,
        "weight": 3
      },
      "item-12333": {
        "value": 6,
        "weight": 1
      },
      "item-12334": {
        "value": 7,
        "weight": 8
      },
      "item-12335": {
        "value": 5,
        "weight": 1
      },
      "item-12336": {
        "value": 5,
        "weight": 1
      },
      "item-12337": {
        "value": 3,
        "weight": 5
      },
      "item-12338": {
        "value": 9,
        "weight": 2
      },
      "item-12339": {
        "value": 6,
        "weight": 7
      },
      "item-12340": {
        "value": 6,
        "weight": 5
      },
      "item-12341": {
        "value": 6,
        "weight": 4
      },
      "item-12342": {
        "value": 2,
        "weight": 4
      },
      "item-12343": {
        "value": 2,
        "weight": 6
      },
      "item-12344": {
        "value": 4,
        "weight": 1
      },
      "item-12345": {
        "value": 5,
        "weight": 2
      },
      "item-12346": {
        "value": 3,
        "weight": 4
      },
      "item-12347": {
        "value": 1,
        "weight": 6
      },
      "item-12348": {
        "value": 4,
        "weight": 1
      },
      "item-12349": {
        "value": 1,
        "weight": 7
      },
      "item-12350": {
        "value": 3,
        "weight": 8
      },
      "item-12351": {
        "value": 3,
        "weight": 1
      },
      "item-12352": {
        "value": 9,
        "weight": 6
      },
      "item-12353": {
        "value": 1,
        "weight": 2
      },
      "item-12354": {
        "value": 2,
        "weight": 1
      },
      "item-12355": {
        "value": 3,
        "weight": 9
      },
      "item-12356": {
        "value": 5,
        "weight": 3
      },
      "item-12357": {
        "value": 5,
        "weight": 8
      },
      "item-12358": {
        "value": 9,
        "weight": 3
      },
      "item-12359": {
        "value": 1,
        "weight": 1
      },
      "item-12360": {
        "value": 5,
        "weight": 9
      },
      "item-12361": {
        "value": 9,
        "weight": 3
      },
      "item-12362": {
        "value": 2,
        "weight": 5
      },
      "item-12363": {
        "value": 7,
        "weight": 4
      },
      "item-12364": {
        "value": 6,
        "weight": 1
      },
      "item-12365": {
        "value": 3,
        "weight": 2
      },
      "item-12366": {
        "value": 3,
        "weight": 3
      },
      "item-12367": {
        "value": 3,
        "weight": 5
      },
      "item-12368": {
        "value": 5,
        "weight": 8
      },
      "item-12369": {
        "value": 6,
        "weight": 2
      },
      "item-12370": {
        "value": 2,
        "weight": 9
      },
      "item-12371": {
        "value": 3,
        "weight": 2
      },
      "item-12372": {
        "value": 7,
        "weight": 8
      },
      "item-12373": {
        "value": 5,
        "weight": 4
      },
      "item-12374": {
        "value": 8,
        "weight": 7
      },
      "item-12375": {
        "value": 2,
        "weight": 4
      },
      "item-12376": {
        "value": 1,
        "weight": 7
      },
      "item-12377": {
        "value": 4,
        "weight": 1
      },
      "item-12378": {
        "value": 9,
        "weight": 5
      },
      "item-12379": {
        "value": 6,
        "weight": 9
      },
      "item-12380": {
        "value": 9,
        "weight": 5
      },
      "item-12381": {
        "value": 6,
        "weight": 2
      },
      "item-12382": {
        "value": 5,
        "weight": 8
      },
      "item-12383": {
        "value": 3,
        "weight": 9
      },
      "item-12384": {
        "value": 1,
        "weight": 5
      },
      "item-12385": {
        "value": 2,
        "weight": 3
      },
      "item-12386": {
        "value": 8,
        "weight": 1
      },
      "item-12387": {
        "value": 3,
        "weight": 5
      },
      "item-12388": {
        "value": 6,
        "weight": 4
      },
      "item-12389": {
        "value": 2,
        "weight": 1
      },
      "item-12390": {
        "value": 9,
        "weight": 7
      },
      "item-12391": {
        "value": 5,
        "weight": 6
      },
      "item-12392": {
        "value": 2,
        "weight": 8
      },
      "item-12393": {
        "value": 1,
        "weight": 7
      },
      "item-12394": {
        "value": 2,
        "weight": 3
      },
      "item-12395": {
        "value": 8,
        "weight": 1
      },
      "item-12396": {
        "value": 4,
        "weight": 3
      },
      "item-12397": {
        "value": 7,
        "weight": 1
      },
      "item-12398": {
        "value": 9,
        "weight": 4
      },
      "item-12399": {
        "value": 8,
        "weight": 1
      },
      "item-12400": {
        "value": 2,
        "weight": 8
      },
      "item-12401": {
        "value": 1,
        "weight": 9
      },
      "item-12402": {
        "value": 6,
        "weight": 5
      },
      "item-12403": {
        "value": 6,
        "weight": 6
      },
      "item-12404": {
        "value": 8,
        "weight": 1
      },
      "item-12405": {
        "value": 3,
        "weight": 5
      },
      "item-12406": {
        "value": 4,
        "weight": 7
      },
      "item-12407": {
        "value": 7,
        "weight": 6
      },
      "item-12408": {
        "value": 1,
        "weight": 6
      },
      "item-12409": {
        "value": 1,
        "weight": 8
      },
      "item-12410": {
        "value": 9,
        "weight": 1
      },
      "item-12411": {
        "value": 9,
        "weight": 1
      },
      "item-12412": {
        "value": 4,
        "weight": 6
      },
      "item-12413": {
        "value": 1,
        "weight": 1
      },
      "item-12414": {
        "value": 2,
        "weight": 9
      },
      "item-12415": {
        "value": 9,
        "weight": 8
      },
      "item-12416": {
        "value": 4,
        "weight": 1
      },
      "item-12417": {
        "value": 4,
        "weight": 1
      },
      "item-12418": {
        "value": 6,
        "weight": 7
      },
      "item-12419": {
        "value": 1,
        "weight": 7
      },
      "item-12420": {
        "value": 3,
        "weight": 4
      },
      "item-12421": {
        "value": 2,
        "weight": 9
      },
      "item-12422": {
        "value": 3,
        "weight": 8
      },
      "item-12423": {
        "value": 8,
        "weight": 4
      },
      "item-12424": {
        "value": 6,
        "weight": 2
      },
      "item-12425": {
        "value": 8,
        "weight": 2
      },
      "item-12426": {
        "value": 1,
        "weight": 1
      },
      "item-12427": {
        "value": 2,
        "weight": 9
      },
      "item-12428": {
        "value": 8,
        "weight": 6
      },
      "item-12429": {
        "value": 7,
        "weight": 1
      },
      "item-12430": {
        "value": 6,
        "weight": 7
      },
      "item-12431": {
        "value": 7,
        "weight": 1
      },
      "item-12432": {
        "value": 9,
        "weight": 7
      },
      "item-12433": {
        "value": 4,
        "weight": 3
      },
      "item-12434": {
        "value": 5,
        "weight": 9
      },
      "item-12435": {
        "value": 9,
        "weight": 3
      },
      "item-12436": {
        "value": 7,
        "weight": 6
      },
      "item-12437": {
        "value": 4,
        "weight": 5
      },
      "item-12438": {
        "value": 7,
        "weight": 5
      },
      "item-12439": {
        "value": 1,
        "weight": 7
      },
      "item-12440": {
        "value": 5,
        "weight": 3
      },
      "item-12441": {
        "value": 7,
        "weight": 7
      },
      "item-12442": {
        "value": 2,
        "weight": 1
      },
      "item-12443": {
        "value": 7,
        "weight": 9
      },
      "item-12444": {
        "value": 5,
        "weight": 4
      },
      "item-12445": {
        "value": 1,
        "weight": 7
      },
      "item-12446": {
        "value": 2,
        "weight": 8
      },
      "item-12447": {
        "value": 1,
        "weight": 7
      },
      "item-12448": {
        "value": 8,
        "weight": 3
      },
      "item-12449": {
        "value": 3,
        "weight": 2
      },
      "item-12450": {
        "value": 8,
        "weight": 1
      },
      "item-12451": {
        "value": 4,
        "weight": 7
      },
      "item-12452": {
        "value": 2,
        "weight": 3
      },
      "item-12453": {
        "value": 8,
        "weight": 6
      },
      "item-12454": {
        "value": 7,
        "weight": 6
      },
      "item-12455": {
        "value": 2,
        "weight": 4
      },
      "item-12456": {
        "value": 6,
        "weight": 2
      },
      "item-12457": {
        "value": 4,
        "weight": 6
      },
      "item-12458": {
        "value": 7,
        "weight": 4
      },
      "item-12459": {
        "value": 5,
        "weight": 5
      },
      "item-12460": {
        "value": 1,
        "weight": 6
      },
      "item-12461": {
        "value": 9,
        "weight": 5
      },
      "item-12462": {
        "value": 3,
        "weight": 5
      },
      "item-12463": {
        "value": 3,
        "weight": 3
      },
      "item-12464": {
        "value": 1,
        "weight": 2
      },
      "item-12465": {
        "value": 9,
        "weight": 2
      },
      "item-12466": {
        "value": 1,
        "weight": 2
      },
      "item-12467": {
        "value": 2,
        "weight": 6
      },
      "item-12468": {
        "value": 1,
        "weight": 6
      },
      "item-12469": {
        "value": 4,
        "weight": 3
      },
      "item-12470": {
        "value": 5,
        "weight": 3
      },
      "item-12471": {
        "value": 5,
        "weight": 7
      },
      "item-12472": {
        "value": 9,
        "weight": 2
      },
      "item-12473": {
        "value": 3,
        "weight": 7
      },
      "item-12474": {
        "value": 1,
        "weight": 9
      },
      "item-12475": {
        "value": 5,
        "weight": 7
      },
      "item-12476": {
        "value": 6,
        "weight": 3
      },
      "item-12477": {
        "value": 2,
        "weight": 1
      },
      "item-12478": {
        "value": 6,
        "weight": 1
      },
      "item-12479": {
        "value": 9,
        "weight": 5
      },
      "item-12480": {
        "value": 3,
        "weight": 2
      },
      "item-12481": {
        "value": 7,
        "weight": 9
      },
      "item-12482": {
        "value": 7,
        "weight": 7
      },
      "item-12483": {
        "value": 7,
        "weight": 5
      },
      "item-12484": {
        "value": 8,
        "weight": 3
      },
      "item-12485": {
        "value": 6,
        "weight": 3
      },
      "item-12486": {
        "value": 8,
        "weight": 5
      },
      "item-12487": {
        "value": 3,
        "weight": 3
      },
      "item-12488": {
        "value": 9,
        "weight": 7
      },
      "item-12489": {
        "value": 3,
        "weight": 2
      },
      "item-12490": {
        "value": 9,
        "weight": 6
      },
      "item-12491": {
        "value": 8,
        "weight": 2
      },
      "item-12492": {
        "value": 9,
        "weight": 6
      },
      "item-12493": {
        "value": 7,
        "weight": 7
      },
      "item-12494": {
        "value": 6,
        "weight": 1
      },
      "item-12495": {
        "value": 7,
        "weight": 2
      },
      "item-12496": {
        "value": 8,
        "weight": 7
      },
      "item-12497": {
        "value": 1,
        "weight": 4
      },
      "item-12498": {
        "value": 3,
        "weight": 8
      },
      "item-12499": {
        "value": 9,
        "weight": 1
      },
      "item-12500": {
        "value": 8,
        "weight": 3
      },
      "item-12501": {
        "value": 2,
        "weight": 7
      },
      "item-12502": {
        "value": 4,
        "weight": 5
      },
      "item-12503": {
        "value": 2,
        "weight": 8
      },
      "item-12504": {
        "value": 9,
        "weight": 5
      },
      "item-12505": {
        "value": 1,
        "weight": 4
      },
      "item-12506": {
        "value": 9,
        "weight": 7
      },
      "item-12507": {
        "value": 8,
        "weight": 1
      },
      "item-12508": {
        "value": 1,
        "weight": 6
      },
      "item-12509": {
        "value": 4,
        "weight": 7
      },
      "item-12510": {
        "value": 3,
        "weight": 4
      },
      "item-12511": {
        "value": 5,
        "weight": 8
      },
      "item-12512": {
        "value": 4,
        "weight": 4
      },
      "item-12513": {
        "value": 8,
        "weight": 4
      },
      "item-12514": {
        "value": 3,
        "weight": 1
      },
      "item-12515": {
        "value": 4,
        "weight": 1
      },
      "item-12516": {
        "value": 2,
        "weight": 7
      },
      "item-12517": {
        "value": 5,
        "weight": 8
      },
      "item-12518": {
        "value": 2,
        "weight": 8
      },
      "item-12519": {
        "value": 2,
        "weight": 1
      },
      "item-12520": {
        "value": 9,
        "weight": 7
      },
      "item-12521": {
        "value": 9,
        "weight": 7
      },
      "item-12522": {
        "value": 4,
        "weight": 2
      },
      "item-12523": {
        "value": 2,
        "weight": 3
      },
      "item-12524": {
        "value": 3,
        "weight": 3
      },
      "item-12525": {
        "value": 9,
        "weight": 8
      },
      "item-12526": {
        "value": 4,
        "weight": 3
      },
      "item-12527": {
        "value": 7,
        "weight": 3
      },
      "item-12528": {
        "value": 9,
        "weight": 1
      },
      "item-12529": {
        "value": 8,
        "weight": 1
      },
      "item-12530": {
        "value": 6,
        "weight": 5
      },
      "item-12531": {
        "value": 6,
        "weight": 9
      },
      "item-12532": {
        "value": 6,
        "weight": 8
      },
      "item-12533": {
        "value": 1,
        "weight": 9
      },
      "item-12534": {
        "value": 8,
        "weight": 4
      },
      "item-12535": {
        "value": 9,
        "weight": 3
      },
      "item-12536": {
        "value": 8,
        "weight": 9
      },
      "item-12537": {
        "value": 9,
        "weight": 8
      },
      "item-12538": {
        "value": 3,
        "weight": 9
      },
      "item-12539": {
        "value": 5,
        "weight": 5
      },
      "item-12540": {
        "value": 7,
        "weight": 3
      },
      "item-12541": {
        "value": 9,
        "weight": 8
      },
      "item-12542": {
        "value": 9,
        "weight": 1
      },
      "item-12543": {
        "value": 7,
        "weight": 9
      },
      "item-12544": {
        "value": 7,
        "weight": 7
      },
      "item-12545": {
        "value": 5,
        "weight": 2
      },
      "item-12546": {
        "value": 7,
        "weight": 9
      },
      "item-12547": {
        "value": 6,
        "weight": 7
      },
      "item-12548": {
        "value": 4,
        "weight": 5
      },
      "item-12549": {
        "value": 9,
        "weight": 5
      },
      "item-12550": {
        "value": 7,
        "weight": 8
      },
      "item-12551": {
        "value": 4,
        "weight": 9
      },
      "item-12552": {
        "value": 7,
        "weight": 8
      },
      "item-12553": {
        "value": 8,
        "weight": 8
      },
      "item-12554": {
        "value": 6,
        "weight": 3
      },
      "item-12555": {
        "value": 2,
        "weight": 2
      },
      "item-12556": {
        "value": 8,
        "weight": 8
      },
      "item-12557": {
        "value": 8,
        "weight": 8
      },
      "item-12558": {
        "value": 4,
        "weight": 4
      },
      "item-12559": {
        "value": 8,
        "weight": 6
      },
      "item-12560": {
        "value": 7,
        "weight": 4
      },
      "item-12561": {
        "value": 6,
        "weight": 9
      },
      "item-12562": {
        "value": 1,
        "weight": 8
      },
      "item-12563": {
        "value": 3,
        "weight": 1
      },
      "item-12564": {
        "value": 4,
        "weight": 1
      },
      "item-12565": {
        "value": 2,
        "weight": 1
      },
      "item-12566": {
        "value": 2,
        "weight": 5
      },
      "item-12567": {
        "value": 6,
        "weight": 9
      },
      "item-12568": {
        "value": 5,
        "weight": 8
      },
      "item-12569": {
        "value": 5,
        "weight": 4
      },
      "item-12570": {
        "value": 9,
        "weight": 5
      },
      "item-12571": {
        "value": 1,
        "weight": 2
      },
      "item-12572": {
        "value": 5,
        "weight": 2
      },
      "item-12573": {
        "value": 9,
        "weight": 1
      },
      "item-12574": {
        "value": 5,
        "weight": 9
      },
      "item-12575": {
        "value": 5,
        "weight": 9
      },
      "item-12576": {
        "value": 6,
        "weight": 7
      },
      "item-12577": {
        "value": 6,
        "weight": 9
      },
      "item-12578": {
        "value": 7,
        "weight": 8
      },
      "item-12579": {
        "value": 1,
        "weight": 6
      },
      "item-12580": {
        "value": 7,
        "weight": 5
      },
      "item-12581": {
        "value": 7,
        "weight": 5
      },
      "item-12582": {
        "value": 9,
        "weight": 7
      },
      "item-12583": {
        "value": 5,
        "weight": 8
      },
      "item-12584": {
        "value": 3,
        "weight": 6
      },
      "item-12585": {
        "value": 3,
        "weight": 8
      },
      "item-12586": {
        "value": 4,
        "weight": 7
      },
      "item-12587": {
        "value": 5,
        "weight": 7
      },
      "item-12588": {
        "value": 3,
        "weight": 1
      },
      "item-12589": {
        "value": 6,
        "weight": 7
      },
      "item-12590": {
        "value": 6,
        "weight": 5
      },
      "item-12591": {
        "value": 4,
        "weight": 8
      },
      "item-12592": {
        "value": 7,
        "weight": 5
      },
      "item-12593": {
        "value": 4,
        "weight": 6
      },
      "item-12594": {
        "value": 2,
        "weight": 9
      },
      "item-12595": {
        "value": 8,
        "weight": 2
      },
      "item-12596": {
        "value": 1,
        "weight": 2
      },
      "item-12597": {
        "value": 2,
        "weight": 5
      },
      "item-12598": {
        "value": 3,
        "weight": 1
      },
      "item-12599": {
        "value": 3,
        "weight": 3
      },
      "item-12600": {
        "value": 2,
        "weight": 7
      },
      "item-12601": {
        "value": 1,
        "weight": 2
      },
      "item-12602": {
        "value": 1,
        "weight": 9
      },
      "item-12603": {
        "value": 8,
        "weight": 8
      },
      "item-12604": {
        "value": 1,
        "weight": 2
      },
      "item-12605": {
        "value": 6,
        "weight": 5
      },
      "item-12606": {
        "value": 2,
        "weight": 1
      },
      "item-12607": {
        "value": 9,
        "weight": 7
      },
      "item-12608": {
        "value": 9,
        "weight": 3
      },
      "item-12609": {
        "value": 9,
        "weight": 8
      },
      "item-12610": {
        "value": 5,
        "weight": 5
      },
      "item-12611": {
        "value": 1,
        "weight": 4
      },
      "item-12612": {
        "value": 2,
        "weight": 8
      },
      "item-12613": {
        "value": 6,
        "weight": 5
      },
      "item-12614": {
        "value": 6,
        "weight": 4
      },
      "item-12615": {
        "value": 8,
        "weight": 8
      },
      "item-12616": {
        "value": 1,
        "weight": 4
      },
      "item-12617": {
        "value": 2,
        "weight": 8
      },
      "item-12618": {
        "value": 1,
        "weight": 1
      },
      "item-12619": {
        "value": 7,
        "weight": 8
      },
      "item-12620": {
        "value": 5,
        "weight": 5
      },
      "item-12621": {
        "value": 8,
        "weight": 2
      },
      "item-12622": {
        "value": 4,
        "weight": 6
      },
      "item-12623": {
        "value": 7,
        "weight": 1
      },
      "item-12624": {
        "value": 4,
        "weight": 4
      },
      "item-12625": {
        "value": 1,
        "weight": 5
      },
      "item-12626": {
        "value": 7,
        "weight": 8
      },
      "item-12627": {
        "value": 2,
        "weight": 4
      },
      "item-12628": {
        "value": 8,
        "weight": 9
      },
      "item-12629": {
        "value": 6,
        "weight": 6
      },
      "item-12630": {
        "value": 4,
        "weight": 2
      },
      "item-12631": {
        "value": 3,
        "weight": 1
      },
      "item-12632": {
        "value": 7,
        "weight": 4
      },
      "item-12633": {
        "value": 6,
        "weight": 9
      },
      "item-12634": {
        "value": 7,
        "weight": 5
      },
      "item-12635": {
        "value": 4,
        "weight": 7
      },
      "item-12636": {
        "value": 8,
        "weight": 8
      },
      "item-12637": {
        "value": 4,
        "weight": 4
      },
      "item-12638": {
        "value": 3,
        "weight": 1
      },
      "item-12639": {
        "value": 3,
        "weight": 1
      },
      "item-12640": {
        "value": 3,
        "weight": 6
      },
      "item-12641": {
        "value": 4,
        "weight": 9
      },
      "item-12642": {
        "value": 3,
        "weight": 1
      },
      "item-12643": {
        "value": 1,
        "weight": 8
      },
      "item-12644": {
        "value": 1,
        "weight": 3
      },
      "item-12645": {
        "value": 3,
        "weight": 9
      },
      "item-12646": {
        "value": 1,
        "weight": 6
      },
      "item-12647": {
        "value": 4,
        "weight": 4
      },
      "item-12648": {
        "value": 1,
        "weight": 8
      },
      "item-12649": {
        "value": 2,
        "weight": 2
      },
      "item-12650": {
        "value": 7,
        "weight": 2
      },
      "item-12651": {
        "value": 4,
        "weight": 3
      },
      "item-12652": {
        "value": 8,
        "weight": 4
      },
      "item-12653": {
        "value": 3,
        "weight": 7
      },
      "item-12654": {
        "value": 7,
        "weight": 7
      },
      "item-12655": {
        "value": 4,
        "weight": 4
      },
      "item-12656": {
        "value": 7,
        "weight": 2
      },
      "item-12657": {
        "value": 4,
        "weight": 8
      },
      "item-12658": {
        "value": 7,
        "weight": 6
      },
      "item-12659": {
        "value": 3,
        "weight": 6
      },
      "item-12660": {
        "value": 8,
        "weight": 1
      },
      "item-12661": {
        "value": 7,
        "weight": 9
      },
      "item-12662": {
        "value": 4,
        "weight": 7
      },
      "item-12663": {
        "value": 2,
        "weight": 3
      },
      "item-12664": {
        "value": 2,
        "weight": 3
      },
      "item-12665": {
        "value": 5,
        "weight": 5
      },
      "item-12666": {
        "value": 6,
        "weight": 5
      },
      "item-12667": {
        "value": 9,
        "weight": 2
      },
      "item-12668": {
        "value": 6,
        "weight": 1
      },
      "item-12669": {
        "value": 9,
        "weight": 4
      },
      "item-12670": {
        "value": 9,
        "weight": 7
      },
      "item-12671": {
        "value": 8,
        "weight": 9
      },
      "item-12672": {
        "value": 4,
        "weight": 5
      },
      "item-12673": {
        "value": 7,
        "weight": 7
      },
      "item-12674": {
        "value": 7,
        "weight": 5
      },
      "item-12675": {
        "value": 1,
        "weight": 5
      },
      "item-12676": {
        "value": 3,
        "weight": 8
      },
      "item-12677": {
        "value": 6,
        "weight": 5
      },
      "item-12678": {
        "value": 9,
        "weight": 5
      },
      "item-12679": {
        "value": 7,
        "weight": 4
      },
      "item-12680": {
        "value": 8,
        "weight": 7
      },
      "item-12681": {
        "value": 8,
        "weight": 2
      },
      "item-12682": {
        "value": 1,
        "weight": 3
      },
      "item-12683": {
        "value": 9,
        "weight": 9
      },
      "item-12684": {
        "value": 8,
        "weight": 7
      },
      "item-12685": {
        "value": 6,
        "weight": 1
      },
      "item-12686": {
        "value": 3,
        "weight": 7
      },
      "item-12687": {
        "value": 4,
        "weight": 6
      },
      "item-12688": {
        "value": 4,
        "weight": 9
      },
      "item-12689": {
        "value": 6,
        "weight": 5
      },
      "item-12690": {
        "value": 7,
        "weight": 6
      },
      "item-12691": {
        "value": 5,
        "weight": 2
      },
      "item-12692": {
        "value": 7,
        "weight": 7
      },
      "item-12693": {
        "value": 6,
        "weight": 4
      },
      "item-12694": {
        "value": 4,
        "weight": 7
      },
      "item-12695": {
        "value": 3,
        "weight": 9
      },
      "item-12696": {
        "value": 7,
        "weight": 4
      },
      "item-12697": {
        "value": 7,
        "weight": 5
      },
      "item-12698": {
        "value": 8,
        "weight": 9
      },
      "item-12699": {
        "value": 3,
        "weight": 3
      },
      "item-12700": {
        "value": 8,
        "weight": 5
      },
      "item-12701": {
        "value": 3,
        "weight": 9
      },
      "item-12702": {
        "value": 5,
        "weight": 8
      },
      "item-12703": {
        "value": 3,
        "weight": 7
      },
      "item-12704": {
        "value": 6,
        "weight": 5
      },
      "item-12705": {
        "value": 2,
        "weight": 6
      },
      "item-12706": {
        "value": 5,
        "weight": 2
      },
      "item-12707": {
        "value": 3,
        "weight": 9
      },
      "item-12708": {
        "value": 4,
        "weight": 9
      },
      "item-12709": {
        "value": 6,
        "weight": 5
      },
      "item-12710": {
        "value": 7,
        "weight": 3
      },
      "item-12711": {
        "value": 1,
        "weight": 2
      },
      "item-12712": {
        "value": 7,
        "weight": 1
      },
      "item-12713": {
        "value": 5,
        "weight": 1
      },
      "item-12714": {
        "value": 8,
        "weight": 9
      },
      "item-12715": {
        "value": 2,
        "weight": 7
      },
      "item-12716": {
        "value": 6,
        "weight": 2
      },
      "item-12717": {
        "value": 6,
        "weight": 7
      },
      "item-12718": {
        "value": 7,
        "weight": 6
      },
      "item-12719": {
        "value": 3,
        "weight": 7
      },
      "item-12720": {
        "value": 3,
        "weight": 5
      },
      "item-12721": {
        "value": 6,
        "weight": 4
      },
      "item-12722": {
        "value": 5,
        "weight": 6
      },
      "item-12723": {
        "value": 1,
        "weight": 9
      },
      "item-12724": {
        "value": 3,
        "weight": 4
      },
      "item-12725": {
        "value": 1,
        "weight": 3
      },
      "item-12726": {
        "value": 2,
        "weight": 2
      },
      "item-12727": {
        "value": 1,
        "weight": 6
      },
      "item-12728": {
        "value": 7,
        "weight": 2
      },
      "item-12729": {
        "value": 2,
        "weight": 1
      },
      "item-12730": {
        "value": 5,
        "weight": 4
      },
      "item-12731": {
        "value": 2,
        "weight": 6
      },
      "item-12732": {
        "value": 5,
        "weight": 8
      },
      "item-12733": {
        "value": 6,
        "weight": 5
      },
      "item-12734": {
        "value": 9,
        "weight": 2
      },
      "item-12735": {
        "value": 6,
        "weight": 2
      },
      "item-12736": {
        "value": 8,
        "weight": 2
      },
      "item-12737": {
        "value": 3,
        "weight": 8
      },
      "item-12738": {
        "value": 9,
        "weight": 1
      },
      "item-12739": {
        "value": 4,
        "weight": 8
      },
      "item-12740": {
        "value": 9,
        "weight": 1
      },
      "item-12741": {
        "value": 5,
        "weight": 5
      },
      "item-12742": {
        "value": 5,
        "weight": 3
      },
      "item-12743": {
        "value": 7,
        "weight": 6
      },
      "item-12744": {
        "value": 8,
        "weight": 7
      },
      "item-12745": {
        "value": 3,
        "weight": 8
      },
      "item-12746": {
        "value": 1,
        "weight": 4
      },
      "item-12747": {
        "value": 1,
        "weight": 3
      },
      "item-12748": {
        "value": 8,
        "weight": 8
      },
      "item-12749": {
        "value": 7,
        "weight": 3
      },
      "item-12750": {
        "value": 7,
        "weight": 6
      },
      "item-12751": {
        "value": 1,
        "weight": 5
      },
      "item-12752": {
        "value": 5,
        "weight": 9
      },
      "item-12753": {
        "value": 4,
        "weight": 5
      },
      "item-12754": {
        "value": 7,
        "weight": 5
      },
      "item-12755": {
        "value": 1,
        "weight": 9
      },
      "item-12756": {
        "value": 8,
        "weight": 9
      },
      "item-12757": {
        "value": 6,
        "weight": 1
      },
      "item-12758": {
        "value": 1,
        "weight": 8
      },
      "item-12759": {
        "value": 1,
        "weight": 3
      },
      "item-12760": {
        "value": 1,
        "weight": 1
      },
      "item-12761": {
        "value": 1,
        "weight": 2
      },
      "item-12762": {
        "value": 8,
        "weight": 8
      },
      "item-12763": {
        "value": 6,
        "weight": 6
      },
      "item-12764": {
        "value": 3,
        "weight": 2
      },
      "item-12765": {
        "value": 5,
        "weight": 5
      },
      "item-12766": {
        "value": 7,
        "weight": 5
      },
      "item-12767": {
        "value": 2,
        "weight": 9
      },
      "item-12768": {
        "value": 7,
        "weight": 4
      },
      "item-12769": {
        "value": 6,
        "weight": 5
      },
      "item-12770": {
        "value": 3,
        "weight": 2
      },
      "item-12771": {
        "value": 8,
        "weight": 8
      },
      "item-12772": {
        "value": 7,
        "weight": 3
      },
      "item-12773": {
        "value": 7,
        "weight": 7
      },
      "item-12774": {
        "value": 2,
        "weight": 3
      },
      "item-12775": {
        "value": 8,
        "weight": 3
      },
      "item-12776": {
        "value": 1,
        "weight": 1
      },
      "item-12777": {
        "value": 3,
        "weight": 5
      },
      "item-12778": {
        "value": 4,
        "weight": 8
      },
      "item-12779": {
        "value": 9,
        "weight": 2
      },
      "item-12780": {
        "value": 6,
        "weight": 5
      },
      "item-12781": {
        "value": 8,
        "weight": 3
      },
      "item-12782": {
        "value": 4,
        "weight": 6
      },
      "item-12783": {
        "value": 9,
        "weight": 7
      },
      "item-12784": {
        "value": 2,
        "weight": 4
      },
      "item-12785": {
        "value": 4,
        "weight": 2
      },
      "item-12786": {
        "value": 9,
        "weight": 2
      },
      "item-12787": {
        "value": 5,
        "weight": 2
      },
      "item-12788": {
        "value": 6,
        "weight": 4
      },
      "item-12789": {
        "value": 7,
        "weight": 2
      },
      "item-12790": {
        "value": 5,
        "weight": 2
      },
      "item-12791": {
        "value": 2,
        "weight": 5
      },
      "item-12792": {
        "value": 8,
        "weight": 4
      },
      "item-12793": {
        "value": 3,
        "weight": 8
      },
      "item-12794": {
        "value": 8,
        "weight": 6
      },
      "item-12795": {
        "value": 6,
        "weight": 4
      },
      "item-12796": {
        "value": 4,
        "weight": 9
      },
      "item-12797": {
        "value": 2,
        "weight": 2
      },
      "item-12798": {
        "value": 5,
        "weight": 7
      },
      "item-12799": {
        "value": 7,
        "weight": 3
      },
      "item-12800": {
        "value": 6,
        "weight": 9
      },
      "item-12801": {
        "value": 5,
        "weight": 7
      },
      "item-12802": {
        "value": 7,
        "weight": 6
      },
      "item-12803": {
        "value": 4,
        "weight": 9
      },
      "item-12804": {
        "value": 8,
        "weight": 9
      },
      "item-12805": {
        "value": 1,
        "weight": 7
      },
      "item-12806": {
        "value": 4,
        "weight": 6
      },
      "item-12807": {
        "value": 6,
        "weight": 9
      },
      "item-12808": {
        "value": 9,
        "weight": 3
      },
      "item-12809": {
        "value": 9,
        "weight": 7
      },
      "item-12810": {
        "value": 9,
        "weight": 5
      },
      "item-12811": {
        "value": 6,
        "weight": 1
      },
      "item-12812": {
        "value": 7,
        "weight": 8
      },
      "item-12813": {
        "value": 8,
        "weight": 1
      },
      "item-12814": {
        "value": 4,
        "weight": 9
      },
      "item-12815": {
        "value": 9,
        "weight": 8
      },
      "item-12816": {
        "value": 6,
        "weight": 1
      },
      "item-12817": {
        "value": 8,
        "weight": 4
      },
      "item-12818": {
        "value": 8,
        "weight": 8
      },
      "item-12819": {
        "value": 2,
        "weight": 2
      },
      "item-12820": {
        "value": 8,
        "weight": 7
      },
      "item-12821": {
        "value": 9,
        "weight": 2
      },
      "item-12822": {
        "value": 1,
        "weight": 7
      },
      "item-12823": {
        "value": 4,
        "weight": 8
      },
      "item-12824": {
        "value": 6,
        "weight": 7
      },
      "item-12825": {
        "value": 6,
        "weight": 7
      },
      "item-12826": {
        "value": 6,
        "weight": 5
      },
      "item-12827": {
        "value": 7,
        "weight": 2
      },
      "item-12828": {
        "value": 4,
        "weight": 4
      },
      "item-12829": {
        "value": 5,
        "weight": 6
      },
      "item-12830": {
        "value": 7,
        "weight": 5
      },
      "item-12831": {
        "value": 1,
        "weight": 9
      },
      "item-12832": {
        "value": 4,
        "weight": 6
      },
      "item-12833": {
        "value": 6,
        "weight": 1
      },
      "item-12834": {
        "value": 2,
        "weight": 9
      },
      "item-12835": {
        "value": 1,
        "weight": 3
      },
      "item-12836": {
        "value": 5,
        "weight": 8
      },
      "item-12837": {
        "value": 7,
        "weight": 6
      },
      "item-12838": {
        "value": 4,
        "weight": 6
      },
      "item-12839": {
        "value": 3,
        "weight": 7
      },
      "item-12840": {
        "value": 5,
        "weight": 3
      },
      "item-12841": {
        "value": 7,
        "weight": 5
      },
      "item-12842": {
        "value": 4,
        "weight": 6
      },
      "item-12843": {
        "value": 6,
        "weight": 2
      },
      "item-12844": {
        "value": 9,
        "weight": 2
      },
      "item-12845": {
        "value": 6,
        "weight": 7
      },
      "item-12846": {
        "value": 3,
        "weight": 5
      },
      "item-12847": {
        "value": 2,
        "weight": 7
      },
      "item-12848": {
        "value": 3,
        "weight": 3
      },
      "item-12849": {
        "value": 7,
        "weight": 6
      },
      "item-12850": {
        "value": 8,
        "weight": 5
      },
      "item-12851": {
        "value": 8,
        "weight": 1
      },
      "item-12852": {
        "value": 8,
        "weight": 5
      },
      "item-12853": {
        "value": 6,
        "weight": 4
      },
      "item-12854": {
        "value": 4,
        "weight": 4
      },
      "item-12855": {
        "value": 1,
        "weight": 9
      },
      "item-12856": {
        "value": 7,
        "weight": 6
      },
      "item-12857": {
        "value": 2,
        "weight": 8
      },
      "item-12858": {
        "value": 3,
        "weight": 6
      },
      "item-12859": {
        "value": 6,
        "weight": 4
      },
      "item-12860": {
        "value": 2,
        "weight": 8
      },
      "item-12861": {
        "value": 3,
        "weight": 2
      },
      "item-12862": {
        "value": 1,
        "weight": 5
      },
      "item-12863": {
        "value": 5,
        "weight": 4
      },
      "item-12864": {
        "value": 3,
        "weight": 7
      },
      "item-12865": {
        "value": 3,
        "weight": 4
      },
      "item-12866": {
        "value": 5,
        "weight": 2
      },
      "item-12867": {
        "value": 4,
        "weight": 7
      },
      "item-12868": {
        "value": 1,
        "weight": 1
      },
      "item-12869": {
        "value": 4,
        "weight": 7
      },
      "item-12870": {
        "value": 7,
        "weight": 5
      },
      "item-12871": {
        "value": 5,
        "weight": 7
      },
      "item-12872": {
        "value": 9,
        "weight": 3
      },
      "item-12873": {
        "value": 1,
        "weight": 2
      },
      "item-12874": {
        "value": 3,
        "weight": 8
      },
      "item-12875": {
        "value": 4,
        "weight": 9
      },
      "item-12876": {
        "value": 1,
        "weight": 5
      },
      "item-12877": {
        "value": 4,
        "weight": 7
      },
      "item-12878": {
        "value": 3,
        "weight": 9
      },
      "item-12879": {
        "value": 2,
        "weight": 8
      },
      "item-12880": {
        "value": 4,
        "weight": 1
      },
      "item-12881": {
        "value": 3,
        "weight": 5
      },
      "item-12882": {
        "value": 5,
        "weight": 7
      },
      "item-12883": {
        "value": 4,
        "weight": 5
      },
      "item-12884": {
        "value": 2,
        "weight": 8
      },
      "item-12885": {
        "value": 9,
        "weight": 8
      },
      "item-12886": {
        "value": 9,
        "weight": 7
      },
      "item-12887": {
        "value": 5,
        "weight": 3
      },
      "item-12888": {
        "value": 4,
        "weight": 5
      },
      "item-12889": {
        "value": 9,
        "weight": 9
      },
      "item-12890": {
        "value": 5,
        "weight": 9
      },
      "item-12891": {
        "value": 1,
        "weight": 6
      },
      "item-12892": {
        "value": 1,
        "weight": 5
      },
      "item-12893": {
        "value": 2,
        "weight": 6
      },
      "item-12894": {
        "value": 9,
        "weight": 2
      },
      "item-12895": {
        "value": 1,
        "weight": 9
      },
      "item-12896": {
        "value": 9,
        "weight": 7
      },
      "item-12897": {
        "value": 1,
        "weight": 1
      },
      "item-12898": {
        "value": 3,
        "weight": 6
      },
      "item-12899": {
        "value": 3,
        "weight": 6
      },
      "item-12900": {
        "value": 4,
        "weight": 4
      },
      "item-12901": {
        "value": 7,
        "weight": 1
      },
      "item-12902": {
        "value": 9,
        "weight": 6
      },
      "item-12903": {
        "value": 2,
        "weight": 3
      },
      "item-12904": {
        "value": 5,
        "weight": 6
      },
      "item-12905": {
        "value": 2,
        "weight": 5
      },
      "item-12906": {
        "value": 7,
        "weight": 5
      },
      "item-12907": {
        "value": 8,
        "weight": 3
      },
      "item-12908": {
        "value": 3,
        "weight": 5
      },
      "item-12909": {
        "value": 6,
        "weight": 2
      },
      "item-12910": {
        "value": 8,
        "weight": 6
      },
      "item-12911": {
        "value": 7,
        "weight": 3
      },
      "item-12912": {
        "value": 8,
        "weight": 2
      },
      "item-12913": {
        "value": 9,
        "weight": 5
      },
      "item-12914": {
        "value": 4,
        "weight": 5
      },
      "item-12915": {
        "value": 9,
        "weight": 3
      },
      "item-12916": {
        "value": 4,
        "weight": 2
      },
      "item-12917": {
        "value": 2,
        "weight": 3
      },
      "item-12918": {
        "value": 5,
        "weight": 5
      },
      "item-12919": {
        "value": 2,
        "weight": 3
      },
      "item-12920": {
        "value": 6,
        "weight": 1
      },
      "item-12921": {
        "value": 3,
        "weight": 7
      },
      "item-12922": {
        "value": 1,
        "weight": 3
      },
      "item-12923": {
        "value": 2,
        "weight": 9
      },
      "item-12924": {
        "value": 3,
        "weight": 9
      },
      "item-12925": {
        "value": 1,
        "weight": 2
      },
      "item-12926": {
        "value": 9,
        "weight": 6
      },
      "item-12927": {
        "value": 1,
        "weight": 3
      },
      "item-12928": {
        "value": 2,
        "weight": 8
      },
      "item-12929": {
        "value": 1,
        "weight": 1
      },
      "item-12930": {
        "value": 4,
        "weight": 1
      },
      "item-12931": {
        "value": 1,
        "weight": 5
      },
      "item-12932": {
        "value": 3,
        "weight": 4
      },
      "item-12933": {
        "value": 2,
        "weight": 8
      },
      "item-12934": {
        "value": 8,
        "weight": 8
      },
      "item-12935": {
        "value": 4,
        "weight": 2
      },
      "item-12936": {
        "value": 8,
        "weight": 8
      },
      "item-12937": {
        "value": 6,
        "weight": 2
      },
      "item-12938": {
        "value": 7,
        "weight": 5
      },
      "item-12939": {
        "value": 6,
        "weight": 5
      },
      "item-12940": {
        "value": 5,
        "weight": 5
      },
      "item-12941": {
        "value": 8,
        "weight": 9
      },
      "item-12942": {
        "value": 2,
        "weight": 7
      },
      "item-12943": {
        "value": 8,
        "weight": 8
      },
      "item-12944": {
        "value": 5,
        "weight": 1
      },
      "item-12945": {
        "value": 8,
        "weight": 4
      },
      "item-12946": {
        "value": 8,
        "weight": 7
      },
      "item-12947": {
        "value": 9,
        "weight": 6
      },
      "item-12948": {
        "value": 1,
        "weight": 4
      },
      "item-12949": {
        "value": 1,
        "weight": 9
      },
      "item-12950": {
        "value": 5,
        "weight": 8
      },
      "item-12951": {
        "value": 1,
        "weight": 6
      },
      "item-12952": {
        "value": 5,
        "weight": 6
      },
      "item-12953": {
        "value": 1,
        "weight": 4
      },
      "item-12954": {
        "value": 3,
        "weight": 6
      },
      "item-12955": {
        "value": 6,
        "weight": 5
      },
      "item-12956": {
        "value": 5,
        "weight": 7
      },
      "item-12957": {
        "value": 6,
        "weight": 1
      },
      "item-12958": {
        "value": 3,
        "weight": 5
      },
      "item-12959": {
        "value": 9,
        "weight": 2
      },
      "item-12960": {
        "value": 3,
        "weight": 6
      },
      "item-12961": {
        "value": 6,
        "weight": 9
      },
      "item-12962": {
        "value": 8,
        "weight": 7
      },
      "item-12963": {
        "value": 8,
        "weight": 7
      },
      "item-12964": {
        "value": 8,
        "weight": 2
      },
      "item-12965": {
        "value": 8,
        "weight": 2
      },
      "item-12966": {
        "value": 4,
        "weight": 1
      },
      "item-12967": {
        "value": 7,
        "weight": 8
      },
      "item-12968": {
        "value": 5,
        "weight": 4
      },
      "item-12969": {
        "value": 9,
        "weight": 1
      },
      "item-12970": {
        "value": 6,
        "weight": 4
      },
      "item-12971": {
        "value": 9,
        "weight": 1
      },
      "item-12972": {
        "value": 8,
        "weight": 6
      },
      "item-12973": {
        "value": 1,
        "weight": 5
      },
      "item-12974": {
        "value": 4,
        "weight": 3
      },
      "item-12975": {
        "value": 3,
        "weight": 8
      },
      "item-12976": {
        "value": 5,
        "weight": 9
      },
      "item-12977": {
        "value": 2,
        "weight": 4
      },
      "item-12978": {
        "value": 9,
        "weight": 5
      },
      "item-12979": {
        "value": 3,
        "weight": 9
      },
      "item-12980": {
        "value": 7,
        "weight": 1
      },
      "item-12981": {
        "value": 8,
        "weight": 7
      },
      "item-12982": {
        "value": 9,
        "weight": 5
      },
      "item-12983": {
        "value": 4,
        "weight": 5
      },
      "item-12984": {
        "value": 8,
        "weight": 8
      },
      "item-12985": {
        "value": 1,
        "weight": 3
      },
      "item-12986": {
        "value": 3,
        "weight": 8
      },
      "item-12987": {
        "value": 5,
        "weight": 7
      },
      "item-12988": {
        "value": 4,
        "weight": 8
      },
      "item-12989": {
        "value": 6,
        "weight": 6
      },
      "item-12990": {
        "value": 5,
        "weight": 9
      },
      "item-12991": {
        "value": 9,
        "weight": 2
      },
      "item-12992": {
        "value": 6,
        "weight": 6
      },
      "item-12993": {
        "value": 9,
        "weight": 5
      },
      "item-12994": {
        "value": 4,
        "weight": 3
      },
      "item-12995": {
        "value": 5,
        "weight": 2
      },
      "item-12996": {
        "value": 2,
        "weight": 2
      },
      "item-12997": {
        "value": 9,
        "weight": 4
      },
      "item-12998": {
        "value": 6,
        "weight": 2
      },
      "item-12999": {
        "value": 3,
        "weight": 6
      },
      "item-13000": {
        "value": 3,
        "weight": 8
      },
      "item-13001": {
        "value": 8,
        "weight": 6
      },
      "item-13002": {
        "value": 3,
        "weight": 3
      },
      "item-13003": {
        "value": 5,
        "weight": 8
      },
      "item-13004": {
        "value": 8,
        "weight": 8
      },
      "item-13005": {
        "value": 4,
        "weight": 6
      },
      "item-13006": {
        "value": 2,
        "weight": 6
      },
      "item-13007": {
        "value": 8,
        "weight": 6
      },
      "item-13008": {
        "value": 2,
        "weight": 5
      },
      "item-13009": {
        "value": 2,
        "weight": 2
      },
      "item-13010": {
        "value": 2,
        "weight": 2
      },
      "item-13011": {
        "value": 2,
        "weight": 8
      },
      "item-13012": {
        "value": 2,
        "weight": 5
      },
      "item-13013": {
        "value": 4,
        "weight": 2
      },
      "item-13014": {
        "value": 5,
        "weight": 2
      },
      "item-13015": {
        "value": 3,
        "weight": 8
      },
      "item-13016": {
        "value": 8,
        "weight": 7
      },
      "item-13017": {
        "value": 8,
        "weight": 8
      },
      "item-13018": {
        "value": 1,
        "weight": 1
      },
      "item-13019": {
        "value": 1,
        "weight": 8
      },
      "item-13020": {
        "value": 4,
        "weight": 8
      },
      "item-13021": {
        "value": 9,
        "weight": 6
      },
      "item-13022": {
        "value": 4,
        "weight": 6
      },
      "item-13023": {
        "value": 7,
        "weight": 5
      },
      "item-13024": {
        "value": 9,
        "weight": 3
      },
      "item-13025": {
        "value": 3,
        "weight": 8
      },
      "item-13026": {
        "value": 4,
        "weight": 4
      },
      "item-13027": {
        "value": 7,
        "weight": 4
      },
      "item-13028": {
        "value": 3,
        "weight": 6
      },
      "item-13029": {
        "value": 5,
        "weight": 6
      },
      "item-13030": {
        "value": 6,
        "weight": 2
      },
      "item-13031": {
        "value": 2,
        "weight": 7
      },
      "item-13032": {
        "value": 8,
        "weight": 2
      },
      "item-13033": {
        "value": 4,
        "weight": 6
      },
      "item-13034": {
        "value": 9,
        "weight": 8
      },
      "item-13035": {
        "value": 9,
        "weight": 1
      },
      "item-13036": {
        "value": 1,
        "weight": 9
      },
      "item-13037": {
        "value": 4,
        "weight": 7
      },
      "item-13038": {
        "value": 6,
        "weight": 6
      },
      "item-13039": {
        "value": 4,
        "weight": 2
      },
      "item-13040": {
        "value": 7,
        "weight": 1
      },
      "item-13041": {
        "value": 4,
        "weight": 1
      },
      "item-13042": {
        "value": 3,
        "weight": 2
      },
      "item-13043": {
        "value": 5,
        "weight": 9
      },
      "item-13044": {
        "value": 3,
        "weight": 6
      },
      "item-13045": {
        "value": 1,
        "weight": 3
      },
      "item-13046": {
        "value": 8,
        "weight": 7
      },
      "item-13047": {
        "value": 3,
        "weight": 3
      },
      "item-13048": {
        "value": 7,
        "weight": 6
      },
      "item-13049": {
        "value": 6,
        "weight": 2
      },
      "item-13050": {
        "value": 9,
        "weight": 5
      },
      "item-13051": {
        "value": 2,
        "weight": 8
      },
      "item-13052": {
        "value": 3,
        "weight": 8
      },
      "item-13053": {
        "value": 7,
        "weight": 5
      },
      "item-13054": {
        "value": 8,
        "weight": 4
      },
      "item-13055": {
        "value": 5,
        "weight": 9
      },
      "item-13056": {
        "value": 8,
        "weight": 7
      },
      "item-13057": {
        "value": 1,
        "weight": 1
      },
      "item-13058": {
        "value": 8,
        "weight": 2
      },
      "item-13059": {
        "value": 5,
        "weight": 4
      },
      "item-13060": {
        "value": 3,
        "weight": 1
      },
      "item-13061": {
        "value": 7,
        "weight": 2
      },
      "item-13062": {
        "value": 5,
        "weight": 7
      },
      "item-13063": {
        "value": 7,
        "weight": 2
      },
      "item-13064": {
        "value": 9,
        "weight": 6
      },
      "item-13065": {
        "value": 2,
        "weight": 8
      },
      "item-13066": {
        "value": 9,
        "weight": 3
      },
      "item-13067": {
        "value": 2,
        "weight": 9
      },
      "item-13068": {
        "value": 2,
        "weight": 3
      },
      "item-13069": {
        "value": 6,
        "weight": 5
      },
      "item-13070": {
        "value": 2,
        "weight": 2
      },
      "item-13071": {
        "value": 1,
        "weight": 7
      },
      "item-13072": {
        "value": 5,
        "weight": 4
      },
      "item-13073": {
        "value": 4,
        "weight": 9
      },
      "item-13074": {
        "value": 1,
        "weight": 1
      },
      "item-13075": {
        "value": 6,
        "weight": 8
      },
      "item-13076": {
        "value": 4,
        "weight": 2
      },
      "item-13077": {
        "value": 2,
        "weight": 6
      },
      "item-13078": {
        "value": 3,
        "weight": 1
      },
      "item-13079": {
        "value": 8,
        "weight": 7
      },
      "item-13080": {
        "value": 8,
        "weight": 5
      },
      "item-13081": {
        "value": 6,
        "weight": 1
      },
      "item-13082": {
        "value": 9,
        "weight": 6
      },
      "item-13083": {
        "value": 2,
        "weight": 4
      },
      "item-13084": {
        "value": 8,
        "weight": 9
      },
      "item-13085": {
        "value": 9,
        "weight": 2
      },
      "item-13086": {
        "value": 7,
        "weight": 1
      },
      "item-13087": {
        "value": 2,
        "weight": 8
      },
      "item-13088": {
        "value": 1,
        "weight": 9
      },
      "item-13089": {
        "value": 1,
        "weight": 1
      },
      "item-13090": {
        "value": 2,
        "weight": 7
      },
      "item-13091": {
        "value": 3,
        "weight": 5
      },
      "item-13092": {
        "value": 5,
        "weight": 8
      },
      "item-13093": {
        "value": 5,
        "weight": 8
      },
      "item-13094": {
        "value": 4,
        "weight": 5
      },
      "item-13095": {
        "value": 3,
        "weight": 7
      },
      "item-13096": {
        "value": 6,
        "weight": 9
      },
      "item-13097": {
        "value": 9,
        "weight": 5
      },
      "item-13098": {
        "value": 7,
        "weight": 6
      },
      "item-13099": {
        "value": 2,
        "weight": 2
      },
      "item-13100": {
        "value": 8,
        "weight": 9
      },
      "item-13101": {
        "value": 7,
        "weight": 1
      },
      "item-13102": {
        "value": 4,
        "weight": 2
      },
      "item-13103": {
        "value": 9,
        "weight": 6
      },
      "item-13104": {
        "value": 9,
        "weight": 8
      },
      "item-13105": {
        "value": 2,
        "weight": 4
      },
      "item-13106": {
        "value": 3,
        "weight": 7
      },
      "item-13107": {
        "value": 8,
        "weight": 5
      },
      "item-13108": {
        "value": 7,
        "weight": 2
      },
      "item-13109": {
        "value": 1,
        "weight": 7
      },
      "item-13110": {
        "value": 7,
        "weight": 4
      },
      "item-13111": {
        "value": 2,
        "weight": 2
      },
      "item-13112": {
        "value": 8,
        "weight": 6
      },
      "item-13113": {
        "value": 1,
        "weight": 5
      },
      "item-13114": {
        "value": 6,
        "weight": 4
      },
      "item-13115": {
        "value": 4,
        "weight": 2
      },
      "item-13116": {
        "value": 2,
        "weight": 5
      },
      "item-13117": {
        "value": 1,
        "weight": 6
      },
      "item-13118": {
        "value": 3,
        "weight": 2
      },
      "item-13119": {
        "value": 4,
        "weight": 9
      },
      "item-13120": {
        "value": 1,
        "weight": 9
      },
      "item-13121": {
        "value": 9,
        "weight": 7
      },
      "item-13122": {
        "value": 1,
        "weight": 5
      },
      "item-13123": {
        "value": 9,
        "weight": 5
      },
      "item-13124": {
        "value": 5,
        "weight": 6
      },
      "item-13125": {
        "value": 7,
        "weight": 9
      },
      "item-13126": {
        "value": 5,
        "weight": 2
      },
      "item-13127": {
        "value": 1,
        "weight": 8
      },
      "item-13128": {
        "value": 9,
        "weight": 5
      },
      "item-13129": {
        "value": 4,
        "weight": 5
      },
      "item-13130": {
        "value": 4,
        "weight": 6
      },
      "item-13131": {
        "value": 1,
        "weight": 9
      },
      "item-13132": {
        "value": 3,
        "weight": 9
      },
      "item-13133": {
        "value": 9,
        "weight": 5
      },
      "item-13134": {
        "value": 6,
        "weight": 9
      },
      "item-13135": {
        "value": 2,
        "weight": 4
      },
      "item-13136": {
        "value": 6,
        "weight": 6
      },
      "item-13137": {
        "value": 2,
        "weight": 3
      },
      "item-13138": {
        "value": 5,
        "weight": 1
      },
      "item-13139": {
        "value": 3,
        "weight": 7
      },
      "item-13140": {
        "value": 9,
        "weight": 5
      },
      "item-13141": {
        "value": 9,
        "weight": 2
      },
      "item-13142": {
        "value": 1,
        "weight": 1
      },
      "item-13143": {
        "value": 8,
        "weight": 3
      },
      "item-13144": {
        "value": 4,
        "weight": 7
      },
      "item-13145": {
        "value": 3,
        "weight": 3
      },
      "item-13146": {
        "value": 5,
        "weight": 5
      },
      "item-13147": {
        "value": 7,
        "weight": 2
      },
      "item-13148": {
        "value": 1,
        "weight": 8
      },
      "item-13149": {
        "value": 9,
        "weight": 7
      },
      "item-13150": {
        "value": 4,
        "weight": 5
      },
      "item-13151": {
        "value": 3,
        "weight": 3
      },
      "item-13152": {
        "value": 8,
        "weight": 8
      },
      "item-13153": {
        "value": 6,
        "weight": 3
      },
      "item-13154": {
        "value": 5,
        "weight": 5
      },
      "item-13155": {
        "value": 8,
        "weight": 6
      },
      "item-13156": {
        "value": 5,
        "weight": 2
      },
      "item-13157": {
        "value": 5,
        "weight": 3
      },
      "item-13158": {
        "value": 3,
        "weight": 1
      },
      "item-13159": {
        "value": 8,
        "weight": 9
      },
      "item-13160": {
        "value": 7,
        "weight": 8
      },
      "item-13161": {
        "value": 3,
        "weight": 4
      },
      "item-13162": {
        "value": 7,
        "weight": 9
      },
      "item-13163": {
        "value": 8,
        "weight": 1
      },
      "item-13164": {
        "value": 3,
        "weight": 8
      },
      "item-13165": {
        "value": 5,
        "weight": 6
      },
      "item-13166": {
        "value": 5,
        "weight": 6
      },
      "item-13167": {
        "value": 8,
        "weight": 8
      },
      "item-13168": {
        "value": 5,
        "weight": 8
      },
      "item-13169": {
        "value": 3,
        "weight": 7
      },
      "item-13170": {
        "value": 6,
        "weight": 9
      },
      "item-13171": {
        "value": 7,
        "weight": 3
      },
      "item-13172": {
        "value": 9,
        "weight": 7
      },
      "item-13173": {
        "value": 9,
        "weight": 3
      },
      "item-13174": {
        "value": 9,
        "weight": 7
      },
      "item-13175": {
        "value": 7,
        "weight": 9
      },
      "item-13176": {
        "value": 6,
        "weight": 8
      },
      "item-13177": {
        "value": 9,
        "weight": 4
      },
      "item-13178": {
        "value": 4,
        "weight": 1
      },
      "item-13179": {
        "value": 7,
        "weight": 6
      },
      "item-13180": {
        "value": 4,
        "weight": 6
      },
      "item-13181": {
        "value": 5,
        "weight": 2
      },
      "item-13182": {
        "value": 7,
        "weight": 2
      },
      "item-13183": {
        "value": 8,
        "weight": 8
      },
      "item-13184": {
        "value": 6,
        "weight": 8
      },
      "item-13185": {
        "value": 1,
        "weight": 2
      },
      "item-13186": {
        "value": 3,
        "weight": 7
      },
      "item-13187": {
        "value": 9,
        "weight": 5
      },
      "item-13188": {
        "value": 4,
        "weight": 4
      },
      "item-13189": {
        "value": 3,
        "weight": 8
      },
      "item-13190": {
        "value": 3,
        "weight": 5
      },
      "item-13191": {
        "value": 3,
        "weight": 8
      },
      "item-13192": {
        "value": 2,
        "weight": 7
      },
      "item-13193": {
        "value": 3,
        "weight": 7
      },
      "item-13194": {
        "value": 5,
        "weight": 8
      },
      "item-13195": {
        "value": 7,
        "weight": 7
      },
      "item-13196": {
        "value": 4,
        "weight": 4
      },
      "item-13197": {
        "value": 5,
        "weight": 4
      },
      "item-13198": {
        "value": 7,
        "weight": 9
      },
      "item-13199": {
        "value": 9,
        "weight": 7
      },
      "item-13200": {
        "value": 2,
        "weight": 7
      },
      "item-13201": {
        "value": 9,
        "weight": 4
      },
      "item-13202": {
        "value": 3,
        "weight": 5
      },
      "item-13203": {
        "value": 7,
        "weight": 8
      },
      "item-13204": {
        "value": 1,
        "weight": 4
      },
      "item-13205": {
        "value": 7,
        "weight": 2
      },
      "item-13206": {
        "value": 6,
        "weight": 5
      },
      "item-13207": {
        "value": 2,
        "weight": 4
      },
      "item-13208": {
        "value": 1,
        "weight": 4
      },
      "item-13209": {
        "value": 7,
        "weight": 1
      },
      "item-13210": {
        "value": 6,
        "weight": 2
      },
      "item-13211": {
        "value": 7,
        "weight": 6
      },
      "item-13212": {
        "value": 3,
        "weight": 4
      },
      "item-13213": {
        "value": 8,
        "weight": 9
      },
      "item-13214": {
        "value": 7,
        "weight": 5
      },
      "item-13215": {
        "value": 1,
        "weight": 7
      },
      "item-13216": {
        "value": 7,
        "weight": 6
      },
      "item-13217": {
        "value": 9,
        "weight": 8
      },
      "item-13218": {
        "value": 8,
        "weight": 7
      },
      "item-13219": {
        "value": 6,
        "weight": 1
      },
      "item-13220": {
        "value": 6,
        "weight": 1
      },
      "item-13221": {
        "value": 9,
        "weight": 7
      },
      "item-13222": {
        "value": 1,
        "weight": 7
      },
      "item-13223": {
        "value": 1,
        "weight": 4
      },
      "item-13224": {
        "value": 8,
        "weight": 9
      },
      "item-13225": {
        "value": 6,
        "weight": 3
      },
      "item-13226": {
        "value": 7,
        "weight": 8
      },
      "item-13227": {
        "value": 4,
        "weight": 4
      },
      "item-13228": {
        "value": 3,
        "weight": 7
      },
      "item-13229": {
        "value": 6,
        "weight": 6
      },
      "item-13230": {
        "value": 3,
        "weight": 6
      },
      "item-13231": {
        "value": 2,
        "weight": 6
      },
      "item-13232": {
        "value": 1,
        "weight": 7
      },
      "item-13233": {
        "value": 6,
        "weight": 3
      },
      "item-13234": {
        "value": 1,
        "weight": 4
      },
      "item-13235": {
        "value": 6,
        "weight": 1
      },
      "item-13236": {
        "value": 5,
        "weight": 9
      },
      "item-13237": {
        "value": 2,
        "weight": 6
      },
      "item-13238": {
        "value": 3,
        "weight": 9
      },
      "item-13239": {
        "value": 9,
        "weight": 9
      },
      "item-13240": {
        "value": 9,
        "weight": 8
      },
      "item-13241": {
        "value": 9,
        "weight": 1
      },
      "item-13242": {
        "value": 5,
        "weight": 9
      },
      "item-13243": {
        "value": 5,
        "weight": 8
      },
      "item-13244": {
        "value": 6,
        "weight": 1
      },
      "item-13245": {
        "value": 5,
        "weight": 1
      },
      "item-13246": {
        "value": 6,
        "weight": 1
      },
      "item-13247": {
        "value": 2,
        "weight": 9
      },
      "item-13248": {
        "value": 6,
        "weight": 8
      },
      "item-13249": {
        "value": 6,
        "weight": 4
      },
      "item-13250": {
        "value": 4,
        "weight": 3
      },
      "item-13251": {
        "value": 5,
        "weight": 1
      },
      "item-13252": {
        "value": 8,
        "weight": 2
      },
      "item-13253": {
        "value": 8,
        "weight": 7
      },
      "item-13254": {
        "value": 3,
        "weight": 4
      },
      "item-13255": {
        "value": 2,
        "weight": 6
      },
      "item-13256": {
        "value": 1,
        "weight": 9
      },
      "item-13257": {
        "value": 5,
        "weight": 4
      },
      "item-13258": {
        "value": 9,
        "weight": 6
      },
      "item-13259": {
        "value": 7,
        "weight": 2
      },
      "item-13260": {
        "value": 5,
        "weight": 7
      },
      "item-13261": {
        "value": 6,
        "weight": 1
      },
      "item-13262": {
        "value": 9,
        "weight": 7
      },
      "item-13263": {
        "value": 6,
        "weight": 4
      },
      "item-13264": {
        "value": 8,
        "weight": 2
      },
      "item-13265": {
        "value": 3,
        "weight": 4
      },
      "item-13266": {
        "value": 3,
        "weight": 1
      },
      "item-13267": {
        "value": 9,
        "weight": 1
      },
      "item-13268": {
        "value": 5,
        "weight": 7
      },
      "item-13269": {
        "value": 1,
        "weight": 8
      },
      "item-13270": {
        "value": 9,
        "weight": 4
      },
      "item-13271": {
        "value": 9,
        "weight": 5
      },
      "item-13272": {
        "value": 5,
        "weight": 8
      },
      "item-13273": {
        "value": 6,
        "weight": 5
      },
      "item-13274": {
        "value": 8,
        "weight": 6
      },
      "item-13275": {
        "value": 2,
        "weight": 5
      },
      "item-13276": {
        "value": 3,
        "weight": 7
      },
      "item-13277": {
        "value": 4,
        "weight": 1
      },
      "item-13278": {
        "value": 9,
        "weight": 9
      },
      "item-13279": {
        "value": 1,
        "weight": 4
      },
      "item-13280": {
        "value": 6,
        "weight": 3
      },
      "item-13281": {
        "value": 3,
        "weight": 7
      },
      "item-13282": {
        "value": 9,
        "weight": 2
      },
      "item-13283": {
        "value": 2,
        "weight": 1
      },
      "item-13284": {
        "value": 9,
        "weight": 2
      },
      "item-13285": {
        "value": 1,
        "weight": 5
      },
      "item-13286": {
        "value": 7,
        "weight": 1
      },
      "item-13287": {
        "value": 1,
        "weight": 8
      },
      "item-13288": {
        "value": 5,
        "weight": 7
      },
      "item-13289": {
        "value": 2,
        "weight": 7
      },
      "item-13290": {
        "value": 5,
        "weight": 9
      },
      "item-13291": {
        "value": 2,
        "weight": 6
      },
      "item-13292": {
        "value": 9,
        "weight": 2
      },
      "item-13293": {
        "value": 8,
        "weight": 4
      },
      "item-13294": {
        "value": 9,
        "weight": 9
      },
      "item-13295": {
        "value": 5,
        "weight": 5
      },
      "item-13296": {
        "value": 3,
        "weight": 7
      },
      "item-13297": {
        "value": 2,
        "weight": 6
      },
      "item-13298": {
        "value": 2,
        "weight": 6
      },
      "item-13299": {
        "value": 1,
        "weight": 8
      },
      "item-13300": {
        "value": 3,
        "weight": 6
      },
      "item-13301": {
        "value": 3,
        "weight": 9
      },
      "item-13302": {
        "value": 1,
        "weight": 9
      },
      "item-13303": {
        "value": 2,
        "weight": 8
      },
      "item-13304": {
        "value": 9,
        "weight": 5
      },
      "item-13305": {
        "value": 7,
        "weight": 2
      },
      "item-13306": {
        "value": 5,
        "weight": 5
      },
      "item-13307": {
        "value": 5,
        "weight": 6
      },
      "item-13308": {
        "value": 5,
        "weight": 1
      },
      "item-13309": {
        "value": 3,
        "weight": 3
      },
      "item-13310": {
        "value": 8,
        "weight": 2
      },
      "item-13311": {
        "value": 5,
        "weight": 5
      },
      "item-13312": {
        "value": 9,
        "weight": 5
      },
      "item-13313": {
        "value": 4,
        "weight": 4
      },
      "item-13314": {
        "value": 5,
        "weight": 3
      },
      "item-13315": {
        "value": 2,
        "weight": 1
      },
      "item-13316": {
        "value": 8,
        "weight": 1
      },
      "item-13317": {
        "value": 1,
        "weight": 8
      },
      "item-13318": {
        "value": 7,
        "weight": 2
      },
      "item-13319": {
        "value": 6,
        "weight": 9
      },
      "item-13320": {
        "value": 7,
        "weight": 4
      },
      "item-13321": {
        "value": 2,
        "weight": 3
      },
      "item-13322": {
        "value": 3,
        "weight": 3
      },
      "item-13323": {
        "value": 5,
        "weight": 2
      },
      "item-13324": {
        "value": 5,
        "weight": 4
      },
      "item-13325": {
        "value": 2,
        "weight": 8
      },
      "item-13326": {
        "value": 6,
        "weight": 9
      },
      "item-13327": {
        "value": 8,
        "weight": 8
      },
      "item-13328": {
        "value": 1,
        "weight": 9
      },
      "item-13329": {
        "value": 2,
        "weight": 9
      },
      "item-13330": {
        "value": 5,
        "weight": 3
      },
      "item-13331": {
        "value": 1,
        "weight": 5
      },
      "item-13332": {
        "value": 5,
        "weight": 8
      },
      "item-13333": {
        "value": 7,
        "weight": 1
      },
      "item-13334": {
        "value": 8,
        "weight": 8
      },
      "item-13335": {
        "value": 5,
        "weight": 7
      },
      "item-13336": {
        "value": 8,
        "weight": 5
      },
      "item-13337": {
        "value": 6,
        "weight": 7
      },
      "item-13338": {
        "value": 1,
        "weight": 2
      },
      "item-13339": {
        "value": 8,
        "weight": 4
      },
      "item-13340": {
        "value": 4,
        "weight": 2
      },
      "item-13341": {
        "value": 8,
        "weight": 5
      },
      "item-13342": {
        "value": 1,
        "weight": 6
      },
      "item-13343": {
        "value": 1,
        "weight": 1
      },
      "item-13344": {
        "value": 2,
        "weight": 3
      },
      "item-13345": {
        "value": 2,
        "weight": 5
      },
      "item-13346": {
        "value": 6,
        "weight": 8
      },
      "item-13347": {
        "value": 6,
        "weight": 4
      },
      "item-13348": {
        "value": 9,
        "weight": 2
      },
      "item-13349": {
        "value": 8,
        "weight": 5
      },
      "item-13350": {
        "value": 1,
        "weight": 6
      },
      "item-13351": {
        "value": 3,
        "weight": 7
      },
      "item-13352": {
        "value": 1,
        "weight": 1
      },
      "item-13353": {
        "value": 5,
        "weight": 6
      },
      "item-13354": {
        "value": 7,
        "weight": 8
      },
      "item-13355": {
        "value": 3,
        "weight": 8
      },
      "item-13356": {
        "value": 8,
        "weight": 7
      },
      "item-13357": {
        "value": 4,
        "weight": 7
      },
      "item-13358": {
        "value": 8,
        "weight": 9
      },
      "item-13359": {
        "value": 9,
        "weight": 9
      },
      "item-13360": {
        "value": 3,
        "weight": 4
      },
      "item-13361": {
        "value": 4,
        "weight": 5
      },
      "item-13362": {
        "value": 4,
        "weight": 6
      },
      "item-13363": {
        "value": 8,
        "weight": 2
      },
      "item-13364": {
        "value": 4,
        "weight": 6
      },
      "item-13365": {
        "value": 8,
        "weight": 9
      },
      "item-13366": {
        "value": 7,
        "weight": 8
      },
      "item-13367": {
        "value": 3,
        "weight": 9
      },
      "item-13368": {
        "value": 4,
        "weight": 1
      },
      "item-13369": {
        "value": 6,
        "weight": 6
      },
      "item-13370": {
        "value": 9,
        "weight": 3
      },
      "item-13371": {
        "value": 2,
        "weight": 1
      },
      "item-13372": {
        "value": 7,
        "weight": 2
      },
      "item-13373": {
        "value": 5,
        "weight": 2
      },
      "item-13374": {
        "value": 8,
        "weight": 6
      },
      "item-13375": {
        "value": 2,
        "weight": 3
      },
      "item-13376": {
        "value": 8,
        "weight": 1
      },
      "item-13377": {
        "value": 3,
        "weight": 9
      },
      "item-13378": {
        "value": 3,
        "weight": 4
      },
      "item-13379": {
        "value": 8,
        "weight": 2
      },
      "item-13380": {
        "value": 1,
        "weight": 6
      },
      "item-13381": {
        "value": 7,
        "weight": 9
      },
      "item-13382": {
        "value": 4,
        "weight": 4
      },
      "item-13383": {
        "value": 1,
        "weight": 7
      },
      "item-13384": {
        "value": 6,
        "weight": 8
      },
      "item-13385": {
        "value": 5,
        "weight": 4
      },
      "item-13386": {
        "value": 2,
        "weight": 7
      },
      "item-13387": {
        "value": 8,
        "weight": 2
      },
      "item-13388": {
        "value": 1,
        "weight": 1
      },
      "item-13389": {
        "value": 4,
        "weight": 2
      },
      "item-13390": {
        "value": 1,
        "weight": 5
      },
      "item-13391": {
        "value": 4,
        "weight": 8
      },
      "item-13392": {
        "value": 3,
        "weight": 2
      },
      "item-13393": {
        "value": 3,
        "weight": 9
      },
      "item-13394": {
        "value": 5,
        "weight": 8
      },
      "item-13395": {
        "value": 1,
        "weight": 6
      },
      "item-13396": {
        "value": 6,
        "weight": 9
      },
      "item-13397": {
        "value": 3,
        "weight": 5
      },
      "item-13398": {
        "value": 1,
        "weight": 4
      },
      "item-13399": {
        "value": 4,
        "weight": 2
      },
      "item-13400": {
        "value": 8,
        "weight": 1
      },
      "item-13401": {
        "value": 1,
        "weight": 6
      },
      "item-13402": {
        "value": 8,
        "weight": 7
      },
      "item-13403": {
        "value": 2,
        "weight": 4
      },
      "item-13404": {
        "value": 5,
        "weight": 4
      },
      "item-13405": {
        "value": 3,
        "weight": 7
      },
      "item-13406": {
        "value": 6,
        "weight": 1
      },
      "item-13407": {
        "value": 2,
        "weight": 4
      },
      "item-13408": {
        "value": 1,
        "weight": 8
      },
      "item-13409": {
        "value": 6,
        "weight": 6
      },
      "item-13410": {
        "value": 3,
        "weight": 4
      },
      "item-13411": {
        "value": 3,
        "weight": 5
      },
      "item-13412": {
        "value": 9,
        "weight": 4
      },
      "item-13413": {
        "value": 6,
        "weight": 9
      },
      "item-13414": {
        "value": 5,
        "weight": 9
      },
      "item-13415": {
        "value": 3,
        "weight": 2
      },
      "item-13416": {
        "value": 6,
        "weight": 1
      },
      "item-13417": {
        "value": 8,
        "weight": 5
      },
      "item-13418": {
        "value": 6,
        "weight": 8
      },
      "item-13419": {
        "value": 2,
        "weight": 8
      },
      "item-13420": {
        "value": 9,
        "weight": 7
      },
      "item-13421": {
        "value": 7,
        "weight": 5
      },
      "item-13422": {
        "value": 7,
        "weight": 4
      },
      "item-13423": {
        "value": 1,
        "weight": 8
      },
      "item-13424": {
        "value": 5,
        "weight": 9
      },
      "item-13425": {
        "value": 1,
        "weight": 8
      },
      "item-13426": {
        "value": 1,
        "weight": 3
      },
      "item-13427": {
        "value": 2,
        "weight": 7
      },
      "item-13428": {
        "value": 4,
        "weight": 7
      },
      "item-13429": {
        "value": 8,
        "weight": 3
      },
      "item-13430": {
        "value": 4,
        "weight": 3
      },
      "item-13431": {
        "value": 3,
        "weight": 8
      },
      "item-13432": {
        "value": 9,
        "weight": 2
      },
      "item-13433": {
        "value": 9,
        "weight": 4
      },
      "item-13434": {
        "value": 5,
        "weight": 9
      },
      "item-13435": {
        "value": 3,
        "weight": 6
      },
      "item-13436": {
        "value": 9,
        "weight": 4
      },
      "item-13437": {
        "value": 9,
        "weight": 3
      },
      "item-13438": {
        "value": 1,
        "weight": 4
      },
      "item-13439": {
        "value": 6,
        "weight": 4
      },
      "item-13440": {
        "value": 3,
        "weight": 7
      },
      "item-13441": {
        "value": 2,
        "weight": 1
      },
      "item-13442": {
        "value": 4,
        "weight": 1
      },
      "item-13443": {
        "value": 3,
        "weight": 6
      },
      "item-13444": {
        "value": 6,
        "weight": 8
      },
      "item-13445": {
        "value": 5,
        "weight": 8
      },
      "item-13446": {
        "value": 3,
        "weight": 7
      },
      "item-13447": {
        "value": 1,
        "weight": 8
      },
      "item-13448": {
        "value": 4,
        "weight": 3
      },
      "item-13449": {
        "value": 2,
        "weight": 7
      },
      "item-13450": {
        "value": 2,
        "weight": 4
      },
      "item-13451": {
        "value": 1,
        "weight": 1
      },
      "item-13452": {
        "value": 9,
        "weight": 5
      },
      "item-13453": {
        "value": 3,
        "weight": 2
      },
      "item-13454": {
        "value": 2,
        "weight": 3
      },
      "item-13455": {
        "value": 1,
        "weight": 9
      },
      "item-13456": {
        "value": 1,
        "weight": 5
      },
      "item-13457": {
        "value": 6,
        "weight": 2
      },
      "item-13458": {
        "value": 8,
        "weight": 5
      },
      "item-13459": {
        "value": 2,
        "weight": 7
      },
      "item-13460": {
        "value": 7,
        "weight": 1
      },
      "item-13461": {
        "value": 6,
        "weight": 4
      },
      "item-13462": {
        "value": 1,
        "weight": 3
      },
      "item-13463": {
        "value": 5,
        "weight": 3
      },
      "item-13464": {
        "value": 6,
        "weight": 4
      },
      "item-13465": {
        "value": 4,
        "weight": 5
      },
      "item-13466": {
        "value": 7,
        "weight": 2
      },
      "item-13467": {
        "value": 4,
        "weight": 2
      },
      "item-13468": {
        "value": 4,
        "weight": 6
      },
      "item-13469": {
        "value": 6,
        "weight": 3
      },
      "item-13470": {
        "value": 5,
        "weight": 8
      },
      "item-13471": {
        "value": 4,
        "weight": 8
      },
      "item-13472": {
        "value": 7,
        "weight": 1
      },
      "item-13473": {
        "value": 2,
        "weight": 5
      },
      "item-13474": {
        "value": 3,
        "weight": 5
      },
      "item-13475": {
        "value": 2,
        "weight": 3
      },
      "item-13476": {
        "value": 8,
        "weight": 8
      },
      "item-13477": {
        "value": 1,
        "weight": 6
      },
      "item-13478": {
        "value": 9,
        "weight": 6
      },
      "item-13479": {
        "value": 2,
        "weight": 5
      },
      "item-13480": {
        "value": 3,
        "weight": 6
      },
      "item-13481": {
        "value": 2,
        "weight": 3
      },
      "item-13482": {
        "value": 7,
        "weight": 1
      },
      "item-13483": {
        "value": 7,
        "weight": 1
      },
      "item-13484": {
        "value": 1,
        "weight": 1
      },
      "item-13485": {
        "value": 9,
        "weight": 6
      },
      "item-13486": {
        "value": 8,
        "weight": 2
      },
      "item-13487": {
        "value": 4,
        "weight": 7
      },
      "item-13488": {
        "value": 2,
        "weight": 7
      },
      "item-13489": {
        "value": 7,
        "weight": 1
      },
      "item-13490": {
        "value": 3,
        "weight": 4
      },
      "item-13491": {
        "value": 8,
        "weight": 4
      },
      "item-13492": {
        "value": 1,
        "weight": 5
      },
      "item-13493": {
        "value": 3,
        "weight": 6
      },
      "item-13494": {
        "value": 5,
        "weight": 2
      },
      "item-13495": {
        "value": 6,
        "weight": 4
      },
      "item-13496": {
        "value": 4,
        "weight": 4
      },
      "item-13497": {
        "value": 2,
        "weight": 8
      },
      "item-13498": {
        "value": 4,
        "weight": 4
      },
      "item-13499": {
        "value": 3,
        "weight": 2
      },
      "item-13500": {
        "value": 9,
        "weight": 3
      },
      "item-13501": {
        "value": 9,
        "weight": 7
      },
      "item-13502": {
        "value": 2,
        "weight": 4
      },
      "item-13503": {
        "value": 4,
        "weight": 2
      },
      "item-13504": {
        "value": 6,
        "weight": 5
      },
      "item-13505": {
        "value": 1,
        "weight": 3
      },
      "item-13506": {
        "value": 2,
        "weight": 9
      },
      "item-13507": {
        "value": 5,
        "weight": 8
      },
      "item-13508": {
        "value": 5,
        "weight": 1
      },
      "item-13509": {
        "value": 1,
        "weight": 9
      },
      "item-13510": {
        "value": 8,
        "weight": 8
      },
      "item-13511": {
        "value": 5,
        "weight": 5
      },
      "item-13512": {
        "value": 1,
        "weight": 6
      },
      "item-13513": {
        "value": 3,
        "weight": 4
      },
      "item-13514": {
        "value": 5,
        "weight": 9
      },
      "item-13515": {
        "value": 5,
        "weight": 6
      },
      "item-13516": {
        "value": 4,
        "weight": 5
      },
      "item-13517": {
        "value": 5,
        "weight": 2
      },
      "item-13518": {
        "value": 7,
        "weight": 7
      },
      "item-13519": {
        "value": 2,
        "weight": 5
      },
      "item-13520": {
        "value": 7,
        "weight": 6
      },
      "item-13521": {
        "value": 7,
        "weight": 3
      },
      "item-13522": {
        "value": 2,
        "weight": 6
      },
      "item-13523": {
        "value": 5,
        "weight": 3
      },
      "item-13524": {
        "value": 4,
        "weight": 6
      },
      "item-13525": {
        "value": 8,
        "weight": 3
      },
      "item-13526": {
        "value": 2,
        "weight": 8
      },
      "item-13527": {
        "value": 1,
        "weight": 6
      },
      "item-13528": {
        "value": 2,
        "weight": 8
      },
      "item-13529": {
        "value": 3,
        "weight": 2
      },
      "item-13530": {
        "value": 8,
        "weight": 4
      },
      "item-13531": {
        "value": 9,
        "weight": 8
      },
      "item-13532": {
        "value": 3,
        "weight": 1
      },
      "item-13533": {
        "value": 2,
        "weight": 7
      },
      "item-13534": {
        "value": 8,
        "weight": 5
      },
      "item-13535": {
        "value": 8,
        "weight": 8
      },
      "item-13536": {
        "value": 7,
        "weight": 3
      },
      "item-13537": {
        "value": 3,
        "weight": 5
      },
      "item-13538": {
        "value": 4,
        "weight": 5
      },
      "item-13539": {
        "value": 4,
        "weight": 8
      },
      "item-13540": {
        "value": 2,
        "weight": 3
      },
      "item-13541": {
        "value": 2,
        "weight": 4
      },
      "item-13542": {
        "value": 3,
        "weight": 5
      },
      "item-13543": {
        "value": 7,
        "weight": 5
      },
      "item-13544": {
        "value": 2,
        "weight": 8
      },
      "item-13545": {
        "value": 1,
        "weight": 9
      },
      "item-13546": {
        "value": 9,
        "weight": 3
      },
      "item-13547": {
        "value": 1,
        "weight": 9
      },
      "item-13548": {
        "value": 7,
        "weight": 1
      },
      "item-13549": {
        "value": 3,
        "weight": 9
      },
      "item-13550": {
        "value": 5,
        "weight": 7
      },
      "item-13551": {
        "value": 1,
        "weight": 1
      },
      "item-13552": {
        "value": 3,
        "weight": 4
      },
      "item-13553": {
        "value": 2,
        "weight": 6
      },
      "item-13554": {
        "value": 8,
        "weight": 4
      },
      "item-13555": {
        "value": 8,
        "weight": 7
      },
      "item-13556": {
        "value": 8,
        "weight": 8
      },
      "item-13557": {
        "value": 9,
        "weight": 9
      },
      "item-13558": {
        "value": 4,
        "weight": 8
      },
      "item-13559": {
        "value": 4,
        "weight": 1
      },
      "item-13560": {
        "value": 1,
        "weight": 5
      },
      "item-13561": {
        "value": 5,
        "weight": 6
      },
      "item-13562": {
        "value": 2,
        "weight": 1
      },
      "item-13563": {
        "value": 6,
        "weight": 3
      },
      "item-13564": {
        "value": 7,
        "weight": 1
      },
      "item-13565": {
        "value": 7,
        "weight": 7
      },
      "item-13566": {
        "value": 6,
        "weight": 5
      },
      "item-13567": {
        "value": 4,
        "weight": 7
      },
      "item-13568": {
        "value": 7,
        "weight": 9
      },
      "item-13569": {
        "value": 7,
        "weight": 8
      },
      "item-13570": {
        "value": 5,
        "weight": 7
      },
      "item-13571": {
        "value": 3,
        "weight": 7
      },
      "item-13572": {
        "value": 5,
        "weight": 6
      },
      "item-13573": {
        "value": 8,
        "weight": 9
      },
      "item-13574": {
        "value": 1,
        "weight": 9
      },
      "item-13575": {
        "value": 7,
        "weight": 5
      },
      "item-13576": {
        "value": 7,
        "weight": 4
      },
      "item-13577": {
        "value": 2,
        "weight": 9
      },
      "item-13578": {
        "value": 5,
        "weight": 5
      },
      "item-13579": {
        "value": 6,
        "weight": 3
      },
      "item-13580": {
        "value": 7,
        "weight": 7
      },
      "item-13581": {
        "value": 4,
        "weight": 8
      },
      "item-13582": {
        "value": 7,
        "weight": 7
      },
      "item-13583": {
        "value": 2,
        "weight": 2
      },
      "item-13584": {
        "value": 4,
        "weight": 9
      },
      "item-13585": {
        "value": 5,
        "weight": 2
      },
      "item-13586": {
        "value": 9,
        "weight": 8
      },
      "item-13587": {
        "value": 5,
        "weight": 1
      },
      "item-13588": {
        "value": 3,
        "weight": 9
      },
      "item-13589": {
        "value": 2,
        "weight": 2
      },
      "item-13590": {
        "value": 1,
        "weight": 8
      },
      "item-13591": {
        "value": 8,
        "weight": 7
      },
      "item-13592": {
        "value": 6,
        "weight": 8
      },
      "item-13593": {
        "value": 4,
        "weight": 9
      },
      "item-13594": {
        "value": 2,
        "weight": 8
      },
      "item-13595": {
        "value": 6,
        "weight": 2
      },
      "item-13596": {
        "value": 1,
        "weight": 2
      },
      "item-13597": {
        "value": 7,
        "weight": 3
      },
      "item-13598": {
        "value": 6,
        "weight": 9
      },
      "item-13599": {
        "value": 6,
        "weight": 7
      },
      "item-13600": {
        "value": 2,
        "weight": 5
      },
      "item-13601": {
        "value": 5,
        "weight": 5
      },
      "item-13602": {
        "value": 9,
        "weight": 3
      },
      "item-13603": {
        "value": 2,
        "weight": 2
      },
      "item-13604": {
        "value": 7,
        "weight": 4
      },
      "item-13605": {
        "value": 3,
        "weight": 6
      },
      "item-13606": {
        "value": 1,
        "weight": 3
      },
      "item-13607": {
        "value": 8,
        "weight": 1
      },
      "item-13608": {
        "value": 2,
        "weight": 7
      },
      "item-13609": {
        "value": 2,
        "weight": 8
      },
      "item-13610": {
        "value": 4,
        "weight": 8
      },
      "item-13611": {
        "value": 1,
        "weight": 9
      },
      "item-13612": {
        "value": 6,
        "weight": 7
      },
      "item-13613": {
        "value": 4,
        "weight": 1
      },
      "item-13614": {
        "value": 5,
        "weight": 1
      },
      "item-13615": {
        "value": 9,
        "weight": 9
      },
      "item-13616": {
        "value": 8,
        "weight": 3
      },
      "item-13617": {
        "value": 8,
        "weight": 3
      },
      "item-13618": {
        "value": 5,
        "weight": 1
      },
      "item-13619": {
        "value": 2,
        "weight": 3
      },
      "item-13620": {
        "value": 8,
        "weight": 7
      },
      "item-13621": {
        "value": 6,
        "weight": 9
      },
      "item-13622": {
        "value": 1,
        "weight": 6
      },
      "item-13623": {
        "value": 2,
        "weight": 3
      },
      "item-13624": {
        "value": 3,
        "weight": 4
      },
      "item-13625": {
        "value": 1,
        "weight": 5
      },
      "item-13626": {
        "value": 2,
        "weight": 9
      },
      "item-13627": {
        "value": 3,
        "weight": 6
      },
      "item-13628": {
        "value": 4,
        "weight": 2
      },
      "item-13629": {
        "value": 5,
        "weight": 7
      },
      "item-13630": {
        "value": 8,
        "weight": 8
      },
      "item-13631": {
        "value": 6,
        "weight": 3
      },
      "item-13632": {
        "value": 6,
        "weight": 5
      },
      "item-13633": {
        "value": 7,
        "weight": 1
      },
      "item-13634": {
        "value": 7,
        "weight": 3
      },
      "item-13635": {
        "value": 1,
        "weight": 4
      },
      "item-13636": {
        "value": 6,
        "weight": 9
      },
      "item-13637": {
        "value": 2,
        "weight": 9
      },
      "item-13638": {
        "value": 5,
        "weight": 9
      },
      "item-13639": {
        "value": 7,
        "weight": 8
      },
      "item-13640": {
        "value": 6,
        "weight": 2
      },
      "item-13641": {
        "value": 4,
        "weight": 1
      },
      "item-13642": {
        "value": 3,
        "weight": 3
      },
      "item-13643": {
        "value": 5,
        "weight": 9
      },
      "item-13644": {
        "value": 5,
        "weight": 1
      },
      "item-13645": {
        "value": 8,
        "weight": 6
      },
      "item-13646": {
        "value": 1,
        "weight": 3
      },
      "item-13647": {
        "value": 5,
        "weight": 5
      },
      "item-13648": {
        "value": 5,
        "weight": 4
      },
      "item-13649": {
        "value": 4,
        "weight": 7
      },
      "item-13650": {
        "value": 8,
        "weight": 9
      },
      "item-13651": {
        "value": 2,
        "weight": 1
      },
      "item-13652": {
        "value": 2,
        "weight": 9
      },
      "item-13653": {
        "value": 8,
        "weight": 3
      },
      "item-13654": {
        "value": 4,
        "weight": 1
      },
      "item-13655": {
        "value": 3,
        "weight": 3
      },
      "item-13656": {
        "value": 6,
        "weight": 9
      },
      "item-13657": {
        "value": 1,
        "weight": 2
      },
      "item-13658": {
        "value": 1,
        "weight": 4
      },
      "item-13659": {
        "value": 9,
        "weight": 8
      },
      "item-13660": {
        "value": 5,
        "weight": 6
      },
      "item-13661": {
        "value": 6,
        "weight": 9
      },
      "item-13662": {
        "value": 2,
        "weight": 5
      },
      "item-13663": {
        "value": 1,
        "weight": 5
      },
      "item-13664": {
        "value": 8,
        "weight": 7
      },
      "item-13665": {
        "value": 5,
        "weight": 8
      },
      "item-13666": {
        "value": 6,
        "weight": 9
      },
      "item-13667": {
        "value": 3,
        "weight": 3
      },
      "item-13668": {
        "value": 6,
        "weight": 6
      },
      "item-13669": {
        "value": 5,
        "weight": 8
      },
      "item-13670": {
        "value": 9,
        "weight": 9
      },
      "item-13671": {
        "value": 8,
        "weight": 1
      },
      "item-13672": {
        "value": 1,
        "weight": 4
      },
      "item-13673": {
        "value": 6,
        "weight": 5
      },
      "item-13674": {
        "value": 6,
        "weight": 4
      },
      "item-13675": {
        "value": 9,
        "weight": 8
      },
      "item-13676": {
        "value": 5,
        "weight": 9
      },
      "item-13677": {
        "value": 5,
        "weight": 5
      },
      "item-13678": {
        "value": 1,
        "weight": 1
      },
      "item-13679": {
        "value": 5,
        "weight": 4
      },
      "item-13680": {
        "value": 3,
        "weight": 8
      },
      "item-13681": {
        "value": 9,
        "weight": 4
      },
      "item-13682": {
        "value": 6,
        "weight": 4
      },
      "item-13683": {
        "value": 6,
        "weight": 6
      },
      "item-13684": {
        "value": 1,
        "weight": 6
      },
      "item-13685": {
        "value": 1,
        "weight": 8
      },
      "item-13686": {
        "value": 7,
        "weight": 6
      },
      "item-13687": {
        "value": 3,
        "weight": 6
      },
      "item-13688": {
        "value": 9,
        "weight": 3
      },
      "item-13689": {
        "value": 9,
        "weight": 8
      },
      "item-13690": {
        "value": 2,
        "weight": 3
      },
      "item-13691": {
        "value": 1,
        "weight": 5
      },
      "item-13692": {
        "value": 6,
        "weight": 7
      },
      "item-13693": {
        "value": 5,
        "weight": 8
      },
      "item-13694": {
        "value": 2,
        "weight": 9
      },
      "item-13695": {
        "value": 1,
        "weight": 8
      },
      "item-13696": {
        "value": 3,
        "weight": 8
      },
      "item-13697": {
        "value": 8,
        "weight": 1
      },
      "item-13698": {
        "value": 4,
        "weight": 4
      },
      "item-13699": {
        "value": 9,
        "weight": 1
      },
      "item-13700": {
        "value": 2,
        "weight": 9
      },
      "item-13701": {
        "value": 1,
        "weight": 3
      },
      "item-13702": {
        "value": 5,
        "weight": 2
      },
      "item-13703": {
        "value": 4,
        "weight": 8
      },
      "item-13704": {
        "value": 3,
        "weight": 8
      },
      "item-13705": {
        "value": 8,
        "weight": 2
      },
      "item-13706": {
        "value": 9,
        "weight": 5
      },
      "item-13707": {
        "value": 5,
        "weight": 4
      },
      "item-13708": {
        "value": 7,
        "weight": 4
      },
      "item-13709": {
        "value": 7,
        "weight": 7
      },
      "item-13710": {
        "value": 5,
        "weight": 7
      },
      "item-13711": {
        "value": 9,
        "weight": 5
      },
      "item-13712": {
        "value": 5,
        "weight": 8
      },
      "item-13713": {
        "value": 7,
        "weight": 2
      },
      "item-13714": {
        "value": 4,
        "weight": 5
      },
      "item-13715": {
        "value": 6,
        "weight": 1
      },
      "item-13716": {
        "value": 1,
        "weight": 1
      },
      "item-13717": {
        "value": 4,
        "weight": 5
      },
      "item-13718": {
        "value": 5,
        "weight": 4
      },
      "item-13719": {
        "value": 2,
        "weight": 3
      },
      "item-13720": {
        "value": 8,
        "weight": 9
      },
      "item-13721": {
        "value": 2,
        "weight": 3
      },
      "item-13722": {
        "value": 3,
        "weight": 6
      },
      "item-13723": {
        "value": 7,
        "weight": 4
      },
      "item-13724": {
        "value": 6,
        "weight": 8
      },
      "item-13725": {
        "value": 3,
        "weight": 2
      },
      "item-13726": {
        "value": 9,
        "weight": 2
      },
      "item-13727": {
        "value": 2,
        "weight": 1
      },
      "item-13728": {
        "value": 5,
        "weight": 1
      },
      "item-13729": {
        "value": 7,
        "weight": 3
      },
      "item-13730": {
        "value": 7,
        "weight": 6
      },
      "item-13731": {
        "value": 7,
        "weight": 1
      },
      "item-13732": {
        "value": 1,
        "weight": 6
      },
      "item-13733": {
        "value": 6,
        "weight": 1
      },
      "item-13734": {
        "value": 2,
        "weight": 4
      },
      "item-13735": {
        "value": 7,
        "weight": 6
      },
      "item-13736": {
        "value": 5,
        "weight": 9
      },
      "item-13737": {
        "value": 9,
        "weight": 9
      },
      "item-13738": {
        "value": 7,
        "weight": 8
      },
      "item-13739": {
        "value": 9,
        "weight": 6
      },
      "item-13740": {
        "value": 2,
        "weight": 1
      },
      "item-13741": {
        "value": 7,
        "weight": 6
      },
      "item-13742": {
        "value": 5,
        "weight": 2
      },
      "item-13743": {
        "value": 8,
        "weight": 3
      },
      "item-13744": {
        "value": 9,
        "weight": 4
      },
      "item-13745": {
        "value": 5,
        "weight": 3
      },
      "item-13746": {
        "value": 3,
        "weight": 5
      },
      "item-13747": {
        "value": 5,
        "weight": 4
      },
      "item-13748": {
        "value": 9,
        "weight": 5
      },
      "item-13749": {
        "value": 2,
        "weight": 9
      },
      "item-13750": {
        "value": 8,
        "weight": 3
      },
      "item-13751": {
        "value": 1,
        "weight": 2
      },
      "item-13752": {
        "value": 3,
        "weight": 8
      },
      "item-13753": {
        "value": 3,
        "weight": 4
      },
      "item-13754": {
        "value": 6,
        "weight": 5
      },
      "item-13755": {
        "value": 6,
        "weight": 7
      },
      "item-13756": {
        "value": 7,
        "weight": 9
      },
      "item-13757": {
        "value": 8,
        "weight": 2
      },
      "item-13758": {
        "value": 9,
        "weight": 6
      },
      "item-13759": {
        "value": 7,
        "weight": 4
      },
      "item-13760": {
        "value": 4,
        "weight": 3
      },
      "item-13761": {
        "value": 1,
        "weight": 7
      },
      "item-13762": {
        "value": 5,
        "weight": 8
      },
      "item-13763": {
        "value": 9,
        "weight": 2
      },
      "item-13764": {
        "value": 3,
        "weight": 5
      },
      "item-13765": {
        "value": 1,
        "weight": 7
      },
      "item-13766": {
        "value": 7,
        "weight": 2
      },
      "item-13767": {
        "value": 9,
        "weight": 4
      },
      "item-13768": {
        "value": 8,
        "weight": 1
      },
      "item-13769": {
        "value": 9,
        "weight": 7
      },
      "item-13770": {
        "value": 6,
        "weight": 2
      },
      "item-13771": {
        "value": 5,
        "weight": 6
      },
      "item-13772": {
        "value": 4,
        "weight": 2
      },
      "item-13773": {
        "value": 9,
        "weight": 7
      },
      "item-13774": {
        "value": 6,
        "weight": 8
      },
      "item-13775": {
        "value": 9,
        "weight": 7
      },
      "item-13776": {
        "value": 1,
        "weight": 2
      },
      "item-13777": {
        "value": 2,
        "weight": 3
      },
      "item-13778": {
        "value": 5,
        "weight": 2
      },
      "item-13779": {
        "value": 7,
        "weight": 2
      },
      "item-13780": {
        "value": 8,
        "weight": 9
      },
      "item-13781": {
        "value": 2,
        "weight": 7
      },
      "item-13782": {
        "value": 4,
        "weight": 7
      },
      "item-13783": {
        "value": 3,
        "weight": 2
      },
      "item-13784": {
        "value": 5,
        "weight": 2
      },
      "item-13785": {
        "value": 1,
        "weight": 3
      },
      "item-13786": {
        "value": 3,
        "weight": 3
      },
      "item-13787": {
        "value": 9,
        "weight": 7
      },
      "item-13788": {
        "value": 9,
        "weight": 8
      },
      "item-13789": {
        "value": 7,
        "weight": 3
      },
      "item-13790": {
        "value": 7,
        "weight": 4
      },
      "item-13791": {
        "value": 6,
        "weight": 5
      },
      "item-13792": {
        "value": 4,
        "weight": 6
      },
      "item-13793": {
        "value": 2,
        "weight": 5
      },
      "item-13794": {
        "value": 7,
        "weight": 6
      },
      "item-13795": {
        "value": 4,
        "weight": 2
      },
      "item-13796": {
        "value": 2,
        "weight": 5
      },
      "item-13797": {
        "value": 4,
        "weight": 2
      },
      "item-13798": {
        "value": 3,
        "weight": 3
      },
      "item-13799": {
        "value": 3,
        "weight": 9
      },
      "item-13800": {
        "value": 4,
        "weight": 9
      },
      "item-13801": {
        "value": 2,
        "weight": 6
      },
      "item-13802": {
        "value": 7,
        "weight": 8
      },
      "item-13803": {
        "value": 5,
        "weight": 9
      },
      "item-13804": {
        "value": 3,
        "weight": 6
      },
      "item-13805": {
        "value": 6,
        "weight": 4
      },
      "item-13806": {
        "value": 8,
        "weight": 3
      },
      "item-13807": {
        "value": 2,
        "weight": 5
      },
      "item-13808": {
        "value": 3,
        "weight": 6
      },
      "item-13809": {
        "value": 9,
        "weight": 3
      },
      "item-13810": {
        "value": 6,
        "weight": 1
      },
      "item-13811": {
        "value": 3,
        "weight": 3
      },
      "item-13812": {
        "value": 1,
        "weight": 6
      },
      "item-13813": {
        "value": 4,
        "weight": 3
      },
      "item-13814": {
        "value": 6,
        "weight": 8
      },
      "item-13815": {
        "value": 4,
        "weight": 3
      },
      "item-13816": {
        "value": 4,
        "weight": 4
      },
      "item-13817": {
        "value": 2,
        "weight": 2
      },
      "item-13818": {
        "value": 3,
        "weight": 2
      },
      "item-13819": {
        "value": 1,
        "weight": 7
      },
      "item-13820": {
        "value": 9,
        "weight": 4
      },
      "item-13821": {
        "value": 1,
        "weight": 1
      },
      "item-13822": {
        "value": 2,
        "weight": 2
      },
      "item-13823": {
        "value": 7,
        "weight": 4
      },
      "item-13824": {
        "value": 4,
        "weight": 2
      },
      "item-13825": {
        "value": 1,
        "weight": 1
      },
      "item-13826": {
        "value": 9,
        "weight": 9
      },
      "item-13827": {
        "value": 1,
        "weight": 6
      },
      "item-13828": {
        "value": 6,
        "weight": 3
      },
      "item-13829": {
        "value": 3,
        "weight": 1
      },
      "item-13830": {
        "value": 9,
        "weight": 3
      },
      "item-13831": {
        "value": 7,
        "weight": 9
      },
      "item-13832": {
        "value": 5,
        "weight": 1
      },
      "item-13833": {
        "value": 1,
        "weight": 5
      },
      "item-13834": {
        "value": 6,
        "weight": 4
      },
      "item-13835": {
        "value": 6,
        "weight": 9
      },
      "item-13836": {
        "value": 6,
        "weight": 3
      },
      "item-13837": {
        "value": 1,
        "weight": 6
      },
      "item-13838": {
        "value": 9,
        "weight": 2
      },
      "item-13839": {
        "value": 6,
        "weight": 9
      },
      "item-13840": {
        "value": 4,
        "weight": 8
      },
      "item-13841": {
        "value": 3,
        "weight": 6
      },
      "item-13842": {
        "value": 1,
        "weight": 3
      },
      "item-13843": {
        "value": 9,
        "weight": 7
      },
      "item-13844": {
        "value": 3,
        "weight": 6
      },
      "item-13845": {
        "value": 3,
        "weight": 2
      },
      "item-13846": {
        "value": 5,
        "weight": 9
      },
      "item-13847": {
        "value": 5,
        "weight": 3
      },
      "item-13848": {
        "value": 9,
        "weight": 3
      },
      "item-13849": {
        "value": 4,
        "weight": 9
      },
      "item-13850": {
        "value": 4,
        "weight": 1
      },
      "item-13851": {
        "value": 5,
        "weight": 3
      },
      "item-13852": {
        "value": 3,
        "weight": 3
      },
      "item-13853": {
        "value": 2,
        "weight": 6
      },
      "item-13854": {
        "value": 2,
        "weight": 8
      },
      "item-13855": {
        "value": 4,
        "weight": 8
      },
      "item-13856": {
        "value": 1,
        "weight": 7
      },
      "item-13857": {
        "value": 2,
        "weight": 9
      },
      "item-13858": {
        "value": 1,
        "weight": 8
      },
      "item-13859": {
        "value": 1,
        "weight": 4
      },
      "item-13860": {
        "value": 1,
        "weight": 1
      },
      "item-13861": {
        "value": 2,
        "weight": 1
      },
      "item-13862": {
        "value": 2,
        "weight": 5
      },
      "item-13863": {
        "value": 9,
        "weight": 3
      },
      "item-13864": {
        "value": 6,
        "weight": 9
      },
      "item-13865": {
        "value": 1,
        "weight": 8
      },
      "item-13866": {
        "value": 1,
        "weight": 2
      },
      "item-13867": {
        "value": 2,
        "weight": 5
      },
      "item-13868": {
        "value": 6,
        "weight": 3
      },
      "item-13869": {
        "value": 1,
        "weight": 3
      },
      "item-13870": {
        "value": 1,
        "weight": 4
      },
      "item-13871": {
        "value": 3,
        "weight": 8
      },
      "item-13872": {
        "value": 2,
        "weight": 9
      },
      "item-13873": {
        "value": 3,
        "weight": 8
      },
      "item-13874": {
        "value": 9,
        "weight": 7
      },
      "item-13875": {
        "value": 4,
        "weight": 3
      },
      "item-13876": {
        "value": 7,
        "weight": 9
      },
      "item-13877": {
        "value": 9,
        "weight": 3
      },
      "item-13878": {
        "value": 3,
        "weight": 7
      },
      "item-13879": {
        "value": 5,
        "weight": 5
      },
      "item-13880": {
        "value": 9,
        "weight": 1
      },
      "item-13881": {
        "value": 6,
        "weight": 4
      },
      "item-13882": {
        "value": 1,
        "weight": 3
      },
      "item-13883": {
        "value": 2,
        "weight": 7
      },
      "item-13884": {
        "value": 3,
        "weight": 3
      },
      "item-13885": {
        "value": 5,
        "weight": 3
      },
      "item-13886": {
        "value": 2,
        "weight": 6
      },
      "item-13887": {
        "value": 8,
        "weight": 3
      },
      "item-13888": {
        "value": 3,
        "weight": 2
      },
      "item-13889": {
        "value": 5,
        "weight": 1
      },
      "item-13890": {
        "value": 4,
        "weight": 3
      },
      "item-13891": {
        "value": 7,
        "weight": 9
      },
      "item-13892": {
        "value": 3,
        "weight": 7
      },
      "item-13893": {
        "value": 8,
        "weight": 6
      },
      "item-13894": {
        "value": 4,
        "weight": 5
      },
      "item-13895": {
        "value": 2,
        "weight": 4
      },
      "item-13896": {
        "value": 4,
        "weight": 7
      },
      "item-13897": {
        "value": 9,
        "weight": 6
      },
      "item-13898": {
        "value": 1,
        "weight": 3
      },
      "item-13899": {
        "value": 7,
        "weight": 3
      },
      "item-13900": {
        "value": 5,
        "weight": 5
      },
      "item-13901": {
        "value": 8,
        "weight": 5
      },
      "item-13902": {
        "value": 5,
        "weight": 6
      },
      "item-13903": {
        "value": 8,
        "weight": 2
      },
      "item-13904": {
        "value": 9,
        "weight": 9
      },
      "item-13905": {
        "value": 5,
        "weight": 2
      },
      "item-13906": {
        "value": 3,
        "weight": 9
      },
      "item-13907": {
        "value": 9,
        "weight": 8
      },
      "item-13908": {
        "value": 2,
        "weight": 1
      },
      "item-13909": {
        "value": 5,
        "weight": 1
      },
      "item-13910": {
        "value": 8,
        "weight": 3
      },
      "item-13911": {
        "value": 4,
        "weight": 5
      },
      "item-13912": {
        "value": 8,
        "weight": 1
      },
      "item-13913": {
        "value": 6,
        "weight": 2
      },
      "item-13914": {
        "value": 5,
        "weight": 8
      },
      "item-13915": {
        "value": 6,
        "weight": 9
      },
      "item-13916": {
        "value": 6,
        "weight": 3
      },
      "item-13917": {
        "value": 8,
        "weight": 1
      },
      "item-13918": {
        "value": 6,
        "weight": 9
      },
      "item-13919": {
        "value": 8,
        "weight": 3
      },
      "item-13920": {
        "value": 4,
        "weight": 9
      },
      "item-13921": {
        "value": 5,
        "weight": 9
      },
      "item-13922": {
        "value": 9,
        "weight": 4
      },
      "item-13923": {
        "value": 5,
        "weight": 8
      },
      "item-13924": {
        "value": 3,
        "weight": 5
      },
      "item-13925": {
        "value": 6,
        "weight": 2
      },
      "item-13926": {
        "value": 6,
        "weight": 3
      },
      "item-13927": {
        "value": 7,
        "weight": 3
      },
      "item-13928": {
        "value": 5,
        "weight": 5
      },
      "item-13929": {
        "value": 7,
        "weight": 4
      },
      "item-13930": {
        "value": 4,
        "weight": 9
      },
      "item-13931": {
        "value": 3,
        "weight": 3
      },
      "item-13932": {
        "value": 4,
        "weight": 6
      },
      "item-13933": {
        "value": 6,
        "weight": 8
      },
      "item-13934": {
        "value": 6,
        "weight": 1
      },
      "item-13935": {
        "value": 4,
        "weight": 2
      },
      "item-13936": {
        "value": 5,
        "weight": 1
      },
      "item-13937": {
        "value": 8,
        "weight": 8
      },
      "item-13938": {
        "value": 8,
        "weight": 3
      },
      "item-13939": {
        "value": 6,
        "weight": 1
      },
      "item-13940": {
        "value": 9,
        "weight": 1
      },
      "item-13941": {
        "value": 3,
        "weight": 2
      },
      "item-13942": {
        "value": 3,
        "weight": 4
      },
      "item-13943": {
        "value": 9,
        "weight": 2
      },
      "item-13944": {
        "value": 9,
        "weight": 4
      },
      "item-13945": {
        "value": 1,
        "weight": 9
      },
      "item-13946": {
        "value": 7,
        "weight": 6
      },
      "item-13947": {
        "value": 4,
        "weight": 4
      },
      "item-13948": {
        "value": 8,
        "weight": 5
      },
      "item-13949": {
        "value": 6,
        "weight": 4
      },
      "item-13950": {
        "value": 4,
        "weight": 4
      },
      "item-13951": {
        "value": 9,
        "weight": 4
      },
      "item-13952": {
        "value": 4,
        "weight": 4
      },
      "item-13953": {
        "value": 9,
        "weight": 1
      },
      "item-13954": {
        "value": 5,
        "weight": 8
      },
      "item-13955": {
        "value": 4,
        "weight": 3
      },
      "item-13956": {
        "value": 9,
        "weight": 8
      },
      "item-13957": {
        "value": 6,
        "weight": 2
      },
      "item-13958": {
        "value": 7,
        "weight": 7
      },
      "item-13959": {
        "value": 1,
        "weight": 2
      },
      "item-13960": {
        "value": 6,
        "weight": 1
      },
      "item-13961": {
        "value": 3,
        "weight": 8
      },
      "item-13962": {
        "value": 6,
        "weight": 5
      },
      "item-13963": {
        "value": 7,
        "weight": 2
      },
      "item-13964": {
        "value": 4,
        "weight": 5
      },
      "item-13965": {
        "value": 7,
        "weight": 6
      },
      "item-13966": {
        "value": 7,
        "weight": 4
      },
      "item-13967": {
        "value": 7,
        "weight": 3
      },
      "item-13968": {
        "value": 8,
        "weight": 2
      },
      "item-13969": {
        "value": 3,
        "weight": 6
      },
      "item-13970": {
        "value": 6,
        "weight": 2
      },
      "item-13971": {
        "value": 1,
        "weight": 2
      },
      "item-13972": {
        "value": 7,
        "weight": 6
      },
      "item-13973": {
        "value": 5,
        "weight": 5
      },
      "item-13974": {
        "value": 3,
        "weight": 3
      },
      "item-13975": {
        "value": 3,
        "weight": 6
      },
      "item-13976": {
        "value": 6,
        "weight": 3
      },
      "item-13977": {
        "value": 3,
        "weight": 2
      },
      "item-13978": {
        "value": 2,
        "weight": 9
      },
      "item-13979": {
        "value": 2,
        "weight": 5
      },
      "item-13980": {
        "value": 3,
        "weight": 2
      },
      "item-13981": {
        "value": 1,
        "weight": 8
      },
      "item-13982": {
        "value": 8,
        "weight": 1
      },
      "item-13983": {
        "value": 9,
        "weight": 2
      },
      "item-13984": {
        "value": 5,
        "weight": 6
      },
      "item-13985": {
        "value": 5,
        "weight": 3
      },
      "item-13986": {
        "value": 8,
        "weight": 7
      },
      "item-13987": {
        "value": 5,
        "weight": 6
      },
      "item-13988": {
        "value": 3,
        "weight": 2
      },
      "item-13989": {
        "value": 1,
        "weight": 6
      },
      "item-13990": {
        "value": 4,
        "weight": 9
      },
      "item-13991": {
        "value": 1,
        "weight": 3
      },
      "item-13992": {
        "value": 4,
        "weight": 4
      },
      "item-13993": {
        "value": 8,
        "weight": 3
      },
      "item-13994": {
        "value": 4,
        "weight": 1
      },
      "item-13995": {
        "value": 2,
        "weight": 8
      },
      "item-13996": {
        "value": 7,
        "weight": 4
      },
      "item-13997": {
        "value": 5,
        "weight": 1
      },
      "item-13998": {
        "value": 5,
        "weight": 6
      },
      "item-13999": {
        "value": 1,
        "weight": 3
      },
      "item-14000": {
        "value": 8,
        "weight": 8
      },
      "item-14001": {
        "value": 1,
        "weight": 6
      },
      "item-14002": {
        "value": 9,
        "weight": 5
      },
      "item-14003": {
        "value": 2,
        "weight": 9
      },
      "item-14004": {
        "value": 3,
        "weight": 5
      },
      "item-14005": {
        "value": 7,
        "weight": 6
      },
      "item-14006": {
        "value": 9,
        "weight": 8
      },
      "item-14007": {
        "value": 6,
        "weight": 4
      },
      "item-14008": {
        "value": 7,
        "weight": 8
      },
      "item-14009": {
        "value": 9,
        "weight": 4
      },
      "item-14010": {
        "value": 2,
        "weight": 1
      },
      "item-14011": {
        "value": 7,
        "weight": 5
      },
      "item-14012": {
        "value": 4,
        "weight": 3
      },
      "item-14013": {
        "value": 1,
        "weight": 9
      },
      "item-14014": {
        "value": 9,
        "weight": 4
      },
      "item-14015": {
        "value": 3,
        "weight": 4
      },
      "item-14016": {
        "value": 6,
        "weight": 4
      },
      "item-14017": {
        "value": 5,
        "weight": 1
      },
      "item-14018": {
        "value": 6,
        "weight": 4
      },
      "item-14019": {
        "value": 6,
        "weight": 8
      },
      "item-14020": {
        "value": 1,
        "weight": 1
      },
      "item-14021": {
        "value": 5,
        "weight": 6
      },
      "item-14022": {
        "value": 4,
        "weight": 8
      },
      "item-14023": {
        "value": 1,
        "weight": 9
      },
      "item-14024": {
        "value": 3,
        "weight": 8
      },
      "item-14025": {
        "value": 3,
        "weight": 3
      },
      "item-14026": {
        "value": 2,
        "weight": 8
      },
      "item-14027": {
        "value": 1,
        "weight": 4
      },
      "item-14028": {
        "value": 3,
        "weight": 4
      },
      "item-14029": {
        "value": 3,
        "weight": 7
      },
      "item-14030": {
        "value": 7,
        "weight": 5
      },
      "item-14031": {
        "value": 3,
        "weight": 3
      },
      "item-14032": {
        "value": 2,
        "weight": 4
      },
      "item-14033": {
        "value": 2,
        "weight": 6
      },
      "item-14034": {
        "value": 1,
        "weight": 4
      },
      "item-14035": {
        "value": 8,
        "weight": 2
      },
      "item-14036": {
        "value": 4,
        "weight": 7
      },
      "item-14037": {
        "value": 6,
        "weight": 6
      },
      "item-14038": {
        "value": 9,
        "weight": 2
      },
      "item-14039": {
        "value": 5,
        "weight": 7
      },
      "item-14040": {
        "value": 4,
        "weight": 8
      },
      "item-14041": {
        "value": 5,
        "weight": 2
      },
      "item-14042": {
        "value": 3,
        "weight": 5
      },
      "item-14043": {
        "value": 5,
        "weight": 7
      },
      "item-14044": {
        "value": 5,
        "weight": 4
      },
      "item-14045": {
        "value": 6,
        "weight": 7
      },
      "item-14046": {
        "value": 7,
        "weight": 2
      },
      "item-14047": {
        "value": 8,
        "weight": 6
      },
      "item-14048": {
        "value": 5,
        "weight": 8
      },
      "item-14049": {
        "value": 8,
        "weight": 4
      },
      "item-14050": {
        "value": 5,
        "weight": 8
      },
      "item-14051": {
        "value": 4,
        "weight": 2
      },
      "item-14052": {
        "value": 3,
        "weight": 5
      },
      "item-14053": {
        "value": 4,
        "weight": 1
      },
      "item-14054": {
        "value": 9,
        "weight": 8
      },
      "item-14055": {
        "value": 7,
        "weight": 1
      },
      "item-14056": {
        "value": 9,
        "weight": 5
      },
      "item-14057": {
        "value": 6,
        "weight": 4
      },
      "item-14058": {
        "value": 7,
        "weight": 7
      },
      "item-14059": {
        "value": 1,
        "weight": 2
      },
      "item-14060": {
        "value": 3,
        "weight": 2
      },
      "item-14061": {
        "value": 4,
        "weight": 1
      },
      "item-14062": {
        "value": 4,
        "weight": 8
      },
      "item-14063": {
        "value": 1,
        "weight": 6
      },
      "item-14064": {
        "value": 7,
        "weight": 7
      },
      "item-14065": {
        "value": 9,
        "weight": 7
      },
      "item-14066": {
        "value": 5,
        "weight": 7
      },
      "item-14067": {
        "value": 2,
        "weight": 9
      },
      "item-14068": {
        "value": 2,
        "weight": 9
      },
      "item-14069": {
        "value": 7,
        "weight": 2
      },
      "item-14070": {
        "value": 4,
        "weight": 9
      },
      "item-14071": {
        "value": 8,
        "weight": 1
      },
      "item-14072": {
        "value": 4,
        "weight": 7
      },
      "item-14073": {
        "value": 4,
        "weight": 7
      },
      "item-14074": {
        "value": 9,
        "weight": 6
      },
      "item-14075": {
        "value": 9,
        "weight": 1
      },
      "item-14076": {
        "value": 8,
        "weight": 9
      },
      "item-14077": {
        "value": 5,
        "weight": 8
      },
      "item-14078": {
        "value": 8,
        "weight": 1
      },
      "item-14079": {
        "value": 5,
        "weight": 4
      },
      "item-14080": {
        "value": 2,
        "weight": 4
      },
      "item-14081": {
        "value": 6,
        "weight": 4
      },
      "item-14082": {
        "value": 1,
        "weight": 8
      },
      "item-14083": {
        "value": 5,
        "weight": 2
      },
      "item-14084": {
        "value": 5,
        "weight": 9
      },
      "item-14085": {
        "value": 2,
        "weight": 4
      },
      "item-14086": {
        "value": 1,
        "weight": 8
      },
      "item-14087": {
        "value": 9,
        "weight": 5
      },
      "item-14088": {
        "value": 1,
        "weight": 9
      },
      "item-14089": {
        "value": 6,
        "weight": 1
      },
      "item-14090": {
        "value": 6,
        "weight": 7
      },
      "item-14091": {
        "value": 5,
        "weight": 1
      },
      "item-14092": {
        "value": 4,
        "weight": 8
      },
      "item-14093": {
        "value": 3,
        "weight": 8
      },
      "item-14094": {
        "value": 9,
        "weight": 6
      },
      "item-14095": {
        "value": 4,
        "weight": 5
      },
      "item-14096": {
        "value": 4,
        "weight": 5
      },
      "item-14097": {
        "value": 7,
        "weight": 2
      },
      "item-14098": {
        "value": 8,
        "weight": 3
      },
      "item-14099": {
        "value": 2,
        "weight": 1
      },
      "item-14100": {
        "value": 7,
        "weight": 4
      },
      "item-14101": {
        "value": 7,
        "weight": 3
      },
      "item-14102": {
        "value": 9,
        "weight": 9
      },
      "item-14103": {
        "value": 5,
        "weight": 9
      },
      "item-14104": {
        "value": 1,
        "weight": 3
      },
      "item-14105": {
        "value": 5,
        "weight": 8
      },
      "item-14106": {
        "value": 6,
        "weight": 5
      },
      "item-14107": {
        "value": 6,
        "weight": 1
      },
      "item-14108": {
        "value": 9,
        "weight": 6
      },
      "item-14109": {
        "value": 7,
        "weight": 4
      },
      "item-14110": {
        "value": 1,
        "weight": 5
      }