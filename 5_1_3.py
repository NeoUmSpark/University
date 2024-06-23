class Building:
    def __init__(self, numberOfFloors, buildingType):
        # Атрибут numberOfFloors: количество этажей в здании(int).
        self.numberOfFloors = numberOfFloors
        # Атрибут buildingType: тип здания(str).
        self.buildingType = buildingType


    def __eq__(self, other):
        #True, если здания имеют одинаковое количество этажей и тип, иначе False.
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)


    def __str__(self):
        return f"Building(numberOfFloors={self.numberOfFloors}, buildingType='{self.buildingType}')"

#Пример
building1 = Building(5, "Bricks")
building2 = Building(5, "Bricks")
building3 = Building(10, "Panel")
building4 = Building(5, "Panel")

print(building1 == building2)  # True, одинаковое уол-во этажей и тип.
print(building1 == building3)  # False, разное кол-во этажей и тип.
print(building1 == building4)  # False, одинаковое кол-во этажей, но разные типы.

#Пример __str__
print(building1)
