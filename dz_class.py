# 1
#
# class MoneyBox:
#     def __init__(self, capacity, coin=0):
#         self.capacity = capacity
#         self.coin = coin
#
#     def can_add(self, coin):
#         return self.capacity - coin >= 0
#
#     def add(self, coin):
#         if self.can_add(coin):
#             self.capacity -= coin
#             self.coin += coin
#             print("count coin:", self.coin)
#         else:
#             print("can't to add coin")
#
#
# pigbox = MoneyBox(20)
# pigbox.add(10)
# pigbox.add(4)
# pigbox.add(4)
# pigbox.add(8)
# pigbox.add(2)
#
# 2.
# from abc import ABC, abstractmethod
#
#
# class Employee(ABC):
#
#     @abstractmethod
#     def info(self):
#         print()
#
#
# class Trainee(Employee):
#     def info(self):
#         print("Уровень допуска:1\n" "з/п:300$\n""стажер")
#
#
# class Worker(Employee):
#     def info(self):
#         print("Уровень допуска:2\n"
#               "з/п:600$\n"
#               "работник")
#
#
# class Head_of_Department(Employee):
#     def info(self):
#         print("Уровень допуска:3\n"
#               "з/п:2650$\n"
#               "начальник отдела")
#

# class Director(Employee):
#     def info(self):
#         print("Уровень допуска:4\n"
#               "з/п:3500$\n"
#               "директор")
#
#
# lvl = int(input("Введите уровень допуска:"))
# if lvl == 1:
#     iva = Trainee()
#     iva.info()
# elif lvl == 2:
#     iva = Worker()
#     iva.info()
# elif lvl == 3:
#     iva = Head_of_Department()
#     iva.info()
# elif lvl == 4:
#     iva = Director()
#     iva.info()


# 4.
# class Stock:
#     def __init__(self, goods: list):
#         self.goods = goods
#
#     def is_good(self, good):
#         if good in self.goods:
#             return True
#         else:
#             return False
#
#     def info_goods(self):
#         print(f" goods: {self.goods}")
#
#
#
# class Shop:
#     def __init__(self, goods: list):
#         self.goods = goods
#
#     def is_good(self, good):
#         if good in self.goods:
#             print(f"we have {good} in our shop")
#         else:
#             print("Ok. We looh this good in stock")
#             if stock.is_good(good):
#                 print("We have this good in our stock ")
#                 self.goods.append(good)
#             else:
#                 print("no good in our stock")
#
# class Buyer():
#     def buy_good(self,good):
#         Evroopt.is_good(good)
#
#
#
# stock_goods = [
#     "milk", "borjomi", "pepsi", "sprite", "coca-cola", "banana",
#     "melon", "watermelon", "cheese", "butter", "meat", "potato"
# ]
#
# shop_goods = [
#     "milk", "coca-cola", "banana",
#     "melon", "cheese", "meat", "tomato", "potato"
# ]
#
# stock = Stock(stock_goods)
# Evroopt = Shop(shop_goods)
# Petya = Buyer()
#
# for i in range(5):
#     good = input()
#     Petya.buy_good(good)
