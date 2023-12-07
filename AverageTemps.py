class AverageTemps:
    def __init__(self, city, avg_temp):
        self.city = city
        self.avg_temp = avg_temp

    def get_city(self):
        return self.city

    def set_city(self, new_city):
        self.city = new_city
        return self.city

    def get_avg_temp(self):
        return self.avg_temp

    def set_avg_temp(self, new_temp):
        self.avg_temp = new_temp
        return self.avg_temp

    def __repr__(self):
        return self.city + ": " + str(self.avg_temp)