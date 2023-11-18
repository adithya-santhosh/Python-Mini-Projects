import pandas
import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature =[]
#     for row in data:
#         if row[1] != "temp":
#             temp = row[1]
#             temperature.append(int(temp))
#
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

#highest_temp = (data["temp"].max())

# monday = data[data.day == "Monday"]
# temp = monday.temp[0]
# fahrenheit = (temp*9)/5 + 32
# print(fahrenheit)
sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = ""
count = 0
grey_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])


squirrel_color_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_sq_count, red_sq_count, black_sq_count]
}
df = pandas.DataFrame(squirrel_color_count)
df.to_csv("squirrel Count.csv")
print(df)