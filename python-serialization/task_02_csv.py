import pickle
import csv
import json



def convert_csv_to_json(csv_file, json_file="data.json"):
    try:
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open(json_file, "wb") as file:
            pickle.dump(data, file, indent=4)
        return True
    except Exception as e:
        return False