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

    def onehundredk_calc(list, legend):
        dictionary = {}

        for k, v in list.items():
            dictionary[k] = (v / legend[k]) * 100000
        return dictionary

    def slicing_counts_unique(demographic, funnel, search_term):
        dictionary = {}

        for i, each in enumerate(demographic):
            if funnel[i] == search_term:
                if each in dictionary:
                    dictionary[each] += 1
                else:
                    dictionary[each] = 0
        return dictionary

# is_number doesn't work yet.
#     def is_number(point):
#         try:
#             float(point)
#             return True
#         except ValueError:
#             return False


incidents_dataset = Dataset(incidents)

incidents_headers = incidents_dataset.header
incidents_data = incidents_dataset.data

census_dataset = Dataset(census)

census_headers = census_dataset.header
census_data = census_dataset.data

year_counts = Dataset.counts_unique(1, incidents_data)
gender_counts = Dataset.counts_unique(5, incidents_data)
race_counts = Dataset.counts_unique(7, incidents_data)
intent_counts = Dataset.counts_unique(3, incidents_data)

races = Dataset.list_comprehension(7, incidents_data)
gender = Dataset.list_comprehension(5, incidents_data)
intents = Dataset.list_comprehension(3, incidents_data)

dates = []

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in incidents_data]

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1


# want to take all the int() functions out of this and convert all to numbers
race_mapping = {}

race_mapping["Asian/Pacific Islander"] = int(census[1][14]) + int(census[1][15])
race_mapping["Black"] = int(census[1][12])
race_mapping["Native American/Native Alaskan"] = int(census[1][13])
race_mapping["Hispanic"] = int(census[1][11])
race_mapping["White"] = int(census[1][10])

# also want to determine numbers by male and female.

homicide_gender_counts = Dataset.slicing_counts_unique(gender, intents, 'Homicide')

# homicide_gender_counts_perhundredk = Dataset.onehundredk_calc(homicide_gender_counts, race_mapping)

incident_counts_M = Dataset.slicing_counts_unique(intents, gender, 'M')

incident_counts_F = Dataset.slicing_counts_unique(intents, gender, 'F')

race_per_hundredk = Dataset.onehundredk_calc(race_counts, race_mapping)

homicide_race_counts = Dataset.slicing_counts_unique(races, intents, 'Homicide')

homicide_race_counts_perhundredk = Dataset.onehundredk_calc(homicide_race_counts, race_mapping)


# print(race_per_hundredk)
print(incident_counts_M)
print(incident_counts_F)
# print(homicide_gender_counts_perhundredk)
# print(homicide_race_counts_perhundredk)
