grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_new = list(students)  # перевел множество учеников в список для сортировки
students_new.sort()  # сортировка по алфавиту

avg_grades_for_students = {}  # пустой словарь для внесения учеников с оценками

for i, student in enumerate(students_new):
    avg_grades_for_students[student] = sum(grades[i]) / len(grades[i])
# в цикле перебрал учеников (student) по алфавиту со средним арифметическим от оценок (i)
print("Средний балл учеников: ", avg_grades_for_students)
