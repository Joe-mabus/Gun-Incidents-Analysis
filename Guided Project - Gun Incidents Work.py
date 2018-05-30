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

    def counts_unique(index, list):
        things = [row[index] for row in list]

        dictionary = {}

        for each in things:
            if each in dictionary:
                dictionary[each] += 1
            else:
                dictionary[each] = 1
        return dictionary

    def list_comprehension(index, list):
        things = [row[index] for row in list]
        return things

    def onehundredk_calc(counting, legend):
        dictionary = {}

        for k, v in counting.items():
            dictionary[k] = (v / legend[k]) * 100000
        return dictionary


homicide_race_counts = {}

homicide_race_counts = {}

incidents_dataset = Dataset(incidents)

incidents_headers = incidents_dataset.header
incidents_data = incidents_dataset.data

census_dataset = Dataset(census)

census_headers = census_dataset.header
census_data = census_dataset.data

year_counts = Dataset.counts_unique(1, incidents_data)
sex_count = Dataset.counts_unique(5, incidents_data)
race_counts = Dataset.counts_unique(7, incidents_data)
intent_counts = Dataset.counts_unique(3, incidents_data)

races = Dataset.list_comprehension(7, incidents_data)
intents = Dataset.list_comprehension(3, incidents_data)

dates = []

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in incidents_data]

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

mapping = {}

mapping["Asian/Pacific Islander"] = int(census[1][14]) + int(census[1][15])
mapping["Black"] = int(census[1][12])
mapping["Native American/Native Alaskan"] = int(census[1][13])
mapping["Hispanic"] = int(census[1][11])
mapping["White"] = int(census[1][10])

race_per_hundredk = Dataset.onehundredk_calc(race_counts, mapping)

homicide_race_counts = {}


for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 0

homicide_race_counts_perhundredk = Dataset.onehundredk_calc(homicide_race_counts, mapping)


# for k, v in homicide_race_counts.items():
#     homicide_race_counts_perhundredk[k] = (v / mapping[k]) * 100000

print(intent_counts)
print(homicide_race_counts_perhundredk)
