# Дан список:
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Выпишем начальное значение индекса элемента в отдельную переменную a:
a = 0

# Задаю цикл while, где индекс элемента меньше длины списка.
# Ввожу новую переменную b (индекс элемента) и одновременно задаю новое значение переменной a (перебор вариантов)
while a < len(my_list):
    b = my_list[a]
    a = a + 1

# Игнорирую 0 c помощью оператора continue (по условию 0 - не положительное, не отрицательное число)
    if b == 0:
        continue

# Игнорирую отрицательные числа c помощью оператора continue (не подходят по условию задачи)
    elif b < 0:
        continue

# Ввожу оператор else для того, чтобы вывести положительные числа, таким образом решая задачу
    else:
        print(b)




