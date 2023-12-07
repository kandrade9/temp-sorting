import AverageTemps

city_1 = AverageTemps("Phoenix", 107)
city_2 = AverageTemps("Las Vegas", 105)
city_3 = AverageTemps("New York", 150)
city_4 = AverageTemps("Boston", 399)
city_5 = AverageTemps("Los Angeles", 82)

city_list = [city_1, city_3, city_5, city_4, city_2]

def insertion_sort(cities):
    for i in range(1, len(cities)):
        key = cities[i]
        j = i - 1
        while j >= 0 and key.get_avg_temp() < cities[j].get_avg_temp():
            cities[j+1] = cities[j]
            j -= 1
        cities[j+1] = key
    return cities

result = insertion_sort(city_list)
print(result)
