data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    result = 0
    for data in data_structure:
        data_type = type(data)
        if data_type == int:
            result += data
        elif data_type == str:
            result += len(data)
        elif data_type in [list, tuple, set]:
            result += calculate_structure_sum(data)  # рекурсия для перезапуска списка и пр. по функции
        elif data_type == dict:
            result += calculate_structure_sum(data.values())
            result += calculate_structure_sum(data.keys())
    return result

res = calculate_structure_sum(data_structure)
print(res)
