# 9.	Дана функция которая запрашивает у пользователя определённые данные для регистрации на портале и запоминает их.
# Напишите декоратор,
# который будет засекать время проведённое пользователем на портале при регистрации.
# import time
#
#
# def reg_time(func):
#     print("====registration===")
#
#     def inner():
#         start_time = time.time()
#         func()
#         print(f'registration time: {time.time() - start_time}')
#
#     return inner
#
#
# @reg_time
# def registration():
#     surname = input("enter you surname: ")
#     name = input("enter you name: ")
#     age = input("enter you age: ")
#     phone = input("enter you number phone: ")
#
#
# registration()



# 8.Дана функция, которая выводит все простые числа в промежутке от 1 до 100.
# Написать декоратор который будет проверять время работы этой функции.
# Задекорировать функцию.
# Вывести время работы этой функции,
# а так же сами простые числа.
# import time
#
#
# def my_decorator(func):
#     def inner():
#         start_time = time.time()
#         func()
#         print(f'function running time: {time.time() - start_time}')
#
#     return inner
#
#
# @my_decorator
# def number():
#     lst = []
#     for i in range(1, 101):
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
#     print(*lst)
#
#
# number()
