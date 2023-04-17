# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib

from os.path import join, abspath

datapach = join(".", "seminars_7")
filename = join(datapach, 'data.txt')

file = open('seminars_7/data.txt', mode='r', encoding='UTF-8')

list_ = [el.strip().split('#') for el in file]
print(list_)

file.close()


# from os.path import join


# datapath = join(".", "task_7.2_data")

# with open(join(datapath, "task_7.2_data.csv"), mode="r", encoding="utf-8") as data_file:
#     data = [line.strip().split("#") for line in data_file]

# # new_data2 = [f"{fio[0]} {fio[1][0]}.{fio[2][0]}." for fio in data]
# new_data2 = [f"{surname} {name[0]}.{parent[0]}." for surname, name, parent in data]

# print(*new_data2, sep="\n")

# # Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# with open(join(datapath, "result", "new_task_7.2_data.csv"), mode="w", encoding="utf-8") as data_file:
#     [data_file.write(el+"\n") for el in new_data2]
