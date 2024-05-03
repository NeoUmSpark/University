immutable_var = 5, False, "Andromeda", [8, 9]
print("Immutable tuple: ", immutable_var)
# immutable_var[1] = True
# print(immutable_var)  # выдается ошибка, поскольку кортеж не поддерживает обащение по элементам

mutable_list = [6, True, "Basalt", (1, 3)]
print("Mutable list: ", mutable_list)
mutable_list[1] = False
mutable_list.remove("Basalt")
mutable_list.append("number")
mutable_list.extend("даздравтсвуетсанкт-петербург")
print("Changed mutable list: ", mutable_list)
