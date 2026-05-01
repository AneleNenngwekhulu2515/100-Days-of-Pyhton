# lst = []
#
# with open("weather_data - Sheet1.csv") as data:
#     contents  = data.readlines()
#     lst.append(contents)
#     print(lst)

# import csv
import pandas


# with open("weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv("weather_data - Sheet1.csv")
print(data["temp"])
#return


