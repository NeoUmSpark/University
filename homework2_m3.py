def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
# print_params(a)  невозможно вызвать функцию с указанием одного или нескольких эл-тов
# без указания нового значения, т.к. оно было объявлено по умолчанию
print_params(b=25)
print_params(c=[2, 3, 4])
print_params(a=32, c=[1,5])


values_list = [1, [2, 3, 4], 'super']
values_dict = {"a": False, "b": 179, "c": [4, 3, 2]}
print_params(*values_list)
print_params(**values_dict)


for key, value in values_dict.items():  # также способ распаковки из лекции
    print(key, value)


values_list_2 = ["DONG", True]
print_params(*values_list_2, 42)  # вызов функции работает. Список распаковался, новое значение добавилось
