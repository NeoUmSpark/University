class Animal:
    def __init__(self, name):  # Начальное состояние: животное живое и не накормленное
        self.alive = True
        self.fed = False
        self.name = name  # Индивидуальное название животного


# Класс-родитель для растений
class Plant:
    def __init__(self, name, edible=False):  # Начальное состояние: растение съедобное или несъедобное
        self.edible = edible  # По умолчанию растение несъедобное
        self.name = name  # Индивидуальное название растения


# Создаём класс-наследник для Животных - Млекопитающие
class Mammal(Animal):
    # Создаём метод eat для млекопитающих, позволяющий им есть растения
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")  # Животное съело растение
                self.fed = True  # Животное накормлено
            else:  # Если несъедобное
                print(f"{self.name} не стал есть {food.name}")  # Животное отказалось от еды
                self.alive = False  # Животное погибло из-за несъедобного растения
        else:  # Если еда не является растением
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


# Создаём класс-наследник для Животных - Хищники
class Predator(Animal):
    # Создаём метод eat для хищников, позволяющий им есть растения
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


# Создаём класс-наследник для Растений - Цветы
class Flower(Plant):
    def __init__(self, name):
        # Вызываем конструктор родительского класса и устанавливаем, что цветы несъедобные
        super().__init__(name, edible=False)  # Цветы по умолчанию несъедобные


# Создаём класс-наследник для Растений - Фрукты
class Fruit(Plant):
    def __init__(self, name):
        # Вызываем конструктор родительского класса и устанавливаем, что фрукты съедобные
        super().__init__(name, edible=True)  # Фрукты по умолчанию съедобные


# Создаём хищника
a1 = Predator('Волк с Уолл-Стрит')
# Создаём млекопитающее
a2 = Mammal('Хатико')
# Создаём цветок
p1 = Flower('Цветик семицветик')
# Создаём фрукт
p2 = Fruit('Заводной апельсин')

# Выводим имя хищника
print(a1.name)
# Выводим имя цветка
print(p1.name)

# Выводим, жив ли хищник
print(a1.alive)  # True
# Выводим, накормлено ли млекопитающее
print(a2.fed)  # False

# Хищник пытается съесть цветок
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
# Млекопитающее пытается съесть фрукт
a2.eat(p2)  # Хатико съел Заводной апельсин

# Выводим, жив ли хищник после попытки съесть несъедобное растение
print(a1.alive)  # False

# Выводим, накормлено ли млекопитающее после съедения съедобного фрукта
print(a2.fed)  # True