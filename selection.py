import AverageTemps

city_1 = AverageTemps("Phoenix", 107)
city_2 = AverageTemps("Las Vegas", 105)
city_3 = AverageTemps("New York", 150)
city_4 = AverageTemps("Boston", 399)
city_5 = AverageTemps("Los Angeles", 82)

city_list = [city_1, city_3, city_5, city_4, city_2]

def selection_sort(cities):
    for i in range(len(cities)):
        min_index = i
        for j in range(i+1, len(cities)):
            city_i = cities[min_index]
            city_j = cities[j]
            if city_i.get_avg_temp() > city_j.get_avg_temp():
                min_index = j
        stored_copy = cities[i]
        cities[i] = cities[min_index]
        cities[min_index] = stored_copy
    return cities

result = selection_sort(city_list)
print(result)
