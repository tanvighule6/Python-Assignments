import json
import csv

with open("data.json", "r") as json_file:
    data = json.load(json_file)

with open("output.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    header = data[0].keys()
    writer.writerow(header)

    for row in data:
        writer.writerow(row.values())

print("JSON successfully converted to CSV!")
