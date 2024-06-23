class Building:
    total = 0

    def __init__(self):
        Building.total += 1

    def __str__(self):
        return f"Порядковый номер здания: {Building.total}"


buildings = []

for i in range(40):
    building = Building()
    buildings.append(building)
    print(building)

# Проверка количества созданных объектов
print(f"Всего создано зданий: {Building.total}")