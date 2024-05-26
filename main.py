from fake_math import divide as f_d
from true_math import divide as t_d

res1 = f_d(69, 3)
res2 = f_d(3, 0)
res3 = t_d(49, 7)
res4 = t_d(15, 0)
print('Результат 1:', res1)
print('Результат 2:', res2)
print('Результат 3:', res3)
print('Результат 4:', res4)
