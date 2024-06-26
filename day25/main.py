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

# print(data["temp"])   # temperature data: just name the name of the column

data_dict = data.to_dict() # Convert DataFrame to a dictionary

data_list = data['temp'].to_list() # Convert Series to a list

# print(data_dict)
# print(data_list)

# Calculate average temperature
avg_temp = data['temp'].mean()
# print(f"Average temperature: {round(avg_temp, 2)}")

# Get the maximum temperature
max_temp = data['temp'].max()
# print(f"Maximum temperature: {max_temp}")

# Get minimum temperature
# print(data.temp.min()) # DataFrame.column_name -> Series

# Get data of one row. Thursday
thursday = data[data.day == "Thursday"]
monday = data[data.day == "Monday"]
# print(thursday)
# print(monday)

# Get row with highest temperature of the week
max_temp_day = data[data.temp == max_temp]
# print(max_temp_day) 

# Convert Monday temperature from Celsius to Fahrenheit (C * 9/5 + 32)
monday_celsius = data.temp[data.day == 'Monday']
monday_fahrenheit = monday_celsius * 9 / 5 + 32
# print(monday_fahrenheit)

# Create a new DataFrame from scratch
new_data_dict = {
    "students": ["Maria", "Anna", "John", "Kate"],
    "scores": [99, 78, 89, 67]
}

data_frame = pandas.DataFrame(new_data_dict)

# print(data_frame)

# Create a dataframe into a csv file
# data_frame.to_csv("day25/student_scores.csv")

# Count squirrels in Central Park (New York). https://thesquirrelcensus.com && 
# https://data.cityofnewyork.us (download CSV data)
# Create a CSV file 'squirrel_count.csv' Fur Color, Count
data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_counts = data["Primary Fur Color"].value_counts()

new_dataframe = pandas.DataFrame(fur_color_counts)

new_dataframe.to_csv("day25/squirrel_count.csv")





 
