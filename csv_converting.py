
import csv
import json

with open('conflict_data/conflict_data_full_lined.json') as file:
    conflict_data = json.load(file)

india_2001 = [["id", "best", "high", "low"]]

for incident in conflict_data:
    if incident["country"] == "India":
        if incident["year"]:
            relevant_data = [incident["id"], incident["best"], incident["high"], incident["low"]]
            india_2001.append(relevant_data)

# print(india_2001)

with open('conflict_data/relevant_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(india_2001)