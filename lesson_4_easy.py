# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
lst = [random.randint(-100, 100) for el in range(10) ]
print('lst = ', lst)
lst_new = [el**2 for el in lst ]
print('lst_new = ', lst_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_1 = ['яблоко','банан','груша','арбуз']
fruits_2 = ['киви','арбуз','дыня','персик','ананас', 'яблоко']
fruits_3 = [el for el in fruits_1 if el in fruits_2]
print('Общие фрукты:', fruits_3)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
Lst = [random.randint(-100, 100) for el in range(10) ]
print (Lst)
Lst_new = [el for el in Lst if el%3==0 and el>0 and el%4!=0 ]
print('lst_new = ', Lst_new)



