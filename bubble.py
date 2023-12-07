import AverageTemps

city_1 = AverageTemps("Phoenix", 107)
city_2 = AverageTemps("Las Vegas", 105)
city_3 = AverageTemps("New York", 150)
city_4 = AverageTemps("Boston", 399)
city_5 = AverageTemps("Los Angeles", 82)

city_list = [city_1, city_3, city_5, city_4, city_2]

def bubble_sort(cities):
    cities_length = len(cities)
    for n in range(cities_length):
        for i in range(cities_length-n-1):
            if cities[i].get_avg_temp() > cities[i+1].get_avg_temp():
                cities[i], cities[i+1] = cities[i+1], cities[i]
    return cities

result = bubble_sort(city_list)
print(result)
