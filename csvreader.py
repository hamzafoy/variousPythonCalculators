import csv

csv.list_dialects()
with open("siege_locations.csv") as test_csv:
    csv_reading = csv.reader(test_csv, delimiter=',', quotechar='"')
    for row in csv_reading:
        print(row)
