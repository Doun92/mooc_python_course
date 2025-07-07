# Write your solution here
import math

def greatest_distance(stations: dict):
    print(stations)

    list_stations = []
    for k in stations.keys():
        list_stations.append(k)


    greatest = 0
    station1 = ""
    station2 = ""
    i= 0
    while i < len(list_stations):
        for j in list_stations:
            d = distance(stations, list_stations[i], j) 
            if d > greatest:
                greatest = d
                station1 = list_stations[i]
                station2 = j

        i += 1

    return station1, station2, greatest

def distance(stations: dict, station1: str, station2: str):
    for k, v in stations.items():
        if k == station1:
            longitude1 = v[0]
            latitude1 = v[1]
        if k == station2:
            longitude2 = v[0]
            latitude2 = v[1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def get_station_data(filename: str):
    try:
        with open(f"src\\{filename}", "r") as f:
            data = f.readlines()
    except:
        with open(filename, "r") as f:
            data = f.readlines()

    dict_stations = {}
    for row in data:
        row = row.strip()
        if "id" in row:
            continue
        else:
            row_as_list = row.split(";")
            dict_stations[row_as_list[3]] = (float(row_as_list[0]), float(row_as_list[1]))

    return dict_stations

if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    # greatest_distance(stations)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)