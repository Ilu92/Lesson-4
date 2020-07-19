# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

my_list = [1, 4, 5, 6, 6, 7, 39, 40, 41, 42, 78, 120, 50]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 6] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
