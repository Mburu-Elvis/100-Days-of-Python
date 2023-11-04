import csv

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temparatures = []
    for row in data:
        if row[1] == "temp":
            temparatures.append(row[1])
        else:
            temparatures.append(int(row[1]))
    for temp in temparatures:
        print(temp)