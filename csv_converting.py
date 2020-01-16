
import csv
import json

with open('conflict_data/conflict_data_full_lined.json') as file:
    conflict_data = json.load(file)

india = [["id","year", "best", "high", "low"]]

for incident in conflict_data:
    if incident["country"] == "India":
        relevant_data = [incident["id"],incident["year"], incident["best"], incident["high"], incident["low"]]
        india.append(relevant_data)

with open('conflict_data/relevant_data_years.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(india)

