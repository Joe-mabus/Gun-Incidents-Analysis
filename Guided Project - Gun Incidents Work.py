import csv
import datetime

f1 = open("guns.csv", "r")

incidents = (list(csv.reader(f1)))

f2 = open("census.csv", "r")

census = (list(csv.reader(f2)))


class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]


incidents_dataset = Dataset(incidents)

incidents_headers = incidents_dataset.header
incidents_data = incidents_dataset.data

census_dataset = Dataset(census)

census_headers = census_dataset.header
census_data = census_dataset.data

years = [row[1] for row in incidents_data]

year_counts = {}

for each in years:
    if each in year_counts:
        year_counts[each] += 1
    else:
        year_counts[each] = 1

dates = []


dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in incidents_data]

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

sex = [row[5] for row in incidents_data]

sex_count = {}

for each in sex:
    if each in sex_count:
        sex_count[each] += 1
    else:
        sex_count[each] = 1

races = [row[7] for row in incidents_data]

race_counts = {}

for each in races:
    if each in race_counts:
        race_counts[each] += 1
    else:
        race_counts[each] = 1

intents = [row[3] for row in incidents_data]

intent_counts = {}

for each in intents:
    if each in intent_counts:
        intent_counts[each] += 1
    else:
        intent_counts[each] = 1

mapping = {}

mapping["Asian/Pacific Islander"] = int(census[1][14]) + int(census[1][15])
mapping["Black"] = int(census[1][12])
mapping["Native American/Native Alaskan"] = int(census[1][13])
mapping["Hispanic"] = int(census[1][11])
mapping["White"] = int(census[1][10])

race_per_hundredk = {}


for k, v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

homicide_race_counts = {}


for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 0


homicide_race_counts_perhundredk = {}


for k, v in homicide_race_counts.items():
    homicide_race_counts_perhundredk[k] = (v / mapping[k]) * 100000

print(homicide_race_counts_perhundredk)
