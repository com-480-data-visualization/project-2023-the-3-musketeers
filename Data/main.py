# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

data = {
    "key": "sugar",
    "ratings": {
        "with": {
            "q1": 0.4,
            "q2": 0.5,
            "min": 0.1,
            "max": 0.8,
            "median": 0.55
        },
        "without": {
            "q1": 0.65,
            "q2": 0.7,
            "min": 0.5,
            "max": 0.75,
            "median": 0.66
        }
    },
    "top5": {
        "with": ['sweet', 'smooth'],
        "without": ['dry']
    },
    "percentage": '95%'
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

