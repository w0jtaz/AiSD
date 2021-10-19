class House:
    doors: int
    color: str

    def __init__(self, doors: int,color: str) -> None:
        self.doors = doors
        self.color = color

    def change_color(self, new_color :str) -> None:
        if new_color == self.color:
            # print('Operacja niedozwolona')
            # return
            raise ValueError('Operacja niedozwolona') #wyrzucenie wyjątku

        self.color = new_color

    def __str__(self) -> str:
        return  'liczba drzwi: {0}, kolor: {1}'\
            .format(self.doors, self.color)


    def __len__(self) -> int:
        return 102


green_house: House = House(doors=20, color='green')
print(green_house.doors)
print(green_house.color)

print(green_house)

blue_house: House = House(doors=10, color='blue')

print(blue_house.__len__())




def sum_(x: int, y: int ) -> int:
    return x + y


assert sum(2, 6) == 8
assert sum(12, 16) == 28 # sprawdzanie poprawnosci