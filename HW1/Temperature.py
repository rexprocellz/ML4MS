class Temperature:
    def __init__(self, temp, unit) :
        self.temp = temp
        self.unit = unit

    def __str__(self):
        return f"{self.temp} {self.unit}"

    def celciusToKelvin(self):
        if self.unit == 'C':
            self.unit = 'K'
            return Temperature(self.temp + 273, self.unit)

    def kelvinToCelcius(self):
        if self.unit == 'K' :
            self.unit = 'C'
            return f"{self.temp - 273} {self.unit}"
