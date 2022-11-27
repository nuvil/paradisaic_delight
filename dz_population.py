from abc import ABC, abstractmethod


class Alive(ABC):
    COUNT = 0

    @abstractmethod
    def info_population(self):
        return self.COUNT


class Plants(Alive):
    def __init__(self, count, koef_grown):
        self.count = count
        self.koef_grown = koef_grown

    def info_population(self):
        return self.count

    def year_after(self):
        self.count *= self.koef_grown

    def rabbits_food(self, rabbits):
        self.count -= rabbits.count * 8


class Rabbits(Alive):
    def __init__(self, count, koef_repr):
        self.count = count
        self.koef_repr = koef_repr

    def info_population(self):
        return self.count

    def year_after(self):
        self.count *= self.koef_repr

    def fox_food(self, fox):
        self.count -= fox.count * 3


class Fox(Alive):
    def __init__(self, count, koef_repre):
        self.count = count
        self.koef_repre = koef_repre

    def info_population(self):
        return self.count

    def year_after(self):
        self.count *= self.koef_repre


class Forest_boy():
    def control(self, rabbits, plants, fox):
        return True if rabbits.count * 7 < plants.count and fox.count * 3 < rabbits.count else False

    def is_add_plants_or_rabbits(self, rabbits, plants, fox):
        if not self.control(rabbits, plants, fox):
            print("rabbits:", rabbits.count, "plants:", plants.count)
            count_plants = int(input("how many plants add?"))
            plants.count += count_plants
        if not self.control(rabbits, plants, fox):
            print("rabbits:", rabbits.count, "fox:", fox.count)
            count_rabbits = int(input("how many rabbit add?"))
            rabbits.count += count_rabbits


plants = Plants(80, 20)
rabbits = Rabbits(10, 10)
fox = Fox(4, 2)
forest_boy = Forest_boy()
year = 1
while year < 10:
    print("year:", year)
    print("plants:", plants.info_population())
    print("rabbits:", rabbits.info_population())
    print("fox:", fox.info_population())
    rabbits.year_after()
    plants.year_after()
    fox.year_after()
    rabbits.fox_food(fox)
    plants.rabbits_food(rabbits)
    forest_boy.is_add_plants_or_rabbits(rabbits, plants, fox)
    if plants.count <= 0:
        print("популяция растений умерло")
        break
    if rabbits.count <= 0:
        print("популяция кроликов умерло")
        break
    year += 1
