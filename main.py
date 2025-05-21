import json
from machine_measurements import parse_payload

def initial_data():
    with open("semAggregated.json", "r", encoding="utf-8") as f:
        raw_python_payload = json.load(f)
    # print(json.dumps(raw_python_payload, indent=4, sort_keys=True))

    raw_data = parse_payload(raw_python_payload)
    return raw_data


initial_data()