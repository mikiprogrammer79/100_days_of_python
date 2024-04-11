# with open("day25/weather_data.csv") as data:
#     data_items = data.readlines()

# print(data_items)

#####################################CSV method#################################################

# import csv

# with open("day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

#################################Pandas method####################################################
import pandas

data = pandas.read_csv("day25/weather_data.csv")  #type(data) -> DataFrame

print(data["temp"])   # temperature data: just name the name of the column

data_dict = data.to_dict() # Convert DataFrame to a dictionary

data_list = data['temp'].to_list() # Convert Series to a list

# print(data_dict)
# print(data_list)

# Calculate average temperature
sum = 0
for value in data_list:
    sum += value
avg_temp = sum / len(data_list)
print(round(avg_temp, 2))