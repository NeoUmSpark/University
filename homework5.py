my_list = ["apple", "peach", "orange", "banana", "kiwi", "grapefruit"]
print("List: ", my_list)
print("First and last element: ", my_list[0], my_list[-1])
print("Sublist: ", my_list[3:6])
my_list[3] = "cucumber"
print("Modified list: ", my_list)

my_dict = {"Settings": "Настройки", "Power": "Сила", "Chainsaw": "Бензопила"}
print("Dictionary: ", my_dict)
print("Translation: ", my_dict.get("Settings"))
my_dict.update({"Power": "Мощь",        # изменили значение для существующего ключа
                "Georgia": "Грузия"})   # добавили ключ и значение
print("Modified dictionary: ", my_dict)
