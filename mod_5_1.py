from http.cookiejar import http2time
from tkinter.font import names


class House:
    def __init__(self, name, number_of_floors):
        self.name = names
        self.number_of_floors = number_of_floors
    def go_to (self,new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            return new_floor
        else:
            return "Такого этажа не существует"

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.go_to(18))
print(h2.go_to(2))




