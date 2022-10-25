import json

with open('general-01_2022_06_20.json') as midjourneydata:
    midjourneydataset = json.load(midjourneydata)

print(len(midjourneydataset))
print(midjourneydataset["messages"][0][0])