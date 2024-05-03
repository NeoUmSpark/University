grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
studentsnew = list(students)  # перевел множество учеников в список для сортировки
studentsnew.sort()

avg_grades = [sum(grades[0]) / len(grades[0]),
      sum(grades[1]) / len(grades[1]),
      sum(grades[2]) / len(grades[2]),
      sum(grades[3]) / len(grades[3]),
      sum(grades[4]) / len(grades[4])]  # вычислил средний балл

avg_grades_for_students = dict(zip(studentsnew, avg_grades))  # функция zip
# поэлементно сгруппировала объекты в указаных списках
print("Средний балл учеников: ", avg_grades_for_students)
