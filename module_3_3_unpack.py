def print_params(a=1, b='Строка', c=True):
    print(a, b, c)

# Функция с параметрами по умолчанию:
print_params()
print_params(1, 'two', 1 == 1)
print_params(1, 1 == 1)
print_params(b=25)
print_params(c=[1, 2, 3])


# Распаковка параметров:
print()
values_list = ['Число', 1, True]
values_dict = {'a': 1, 'b': 'Строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)


# Распаковка + отдельные параметры
print()
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)







