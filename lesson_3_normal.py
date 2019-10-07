# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	list_fibonachi = [1,1]
	list_fibonachi_n_m = []
	i= 1
	while i <= m:
		list_fibonachi.append(list_fibonachi[i-1] + list_fibonachi[i])
		i+=1
	list_fibonachi_n_m = list_fibonachi[n-1:m]
	return (list_fibonachi_n_m)


print (fibonacci(2,5))
print (fibonacci(1,5))
print (fibonacci(5,15))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#def sort_to_max(origin_list:list):

def sort_to_max(origin_list:list):
	for i in range(len(origin_list)-1):
		for j in range(len(origin_list)-i-1):
			if origin_list[j] > origin_list[j+1]:
				origin_list[j], origin_list[j+1]= origin_list[j+1],  origin_list[j]
	return(origin_list)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
 
def my_filter (function, lst):
    list_1 = []
    for i in range(len(lst)):
        if function(lst[i])==True:
            list_1.append(lst[i])
    return list_1

# пример
function = lambda x:  x<3
def fulfil_lst (n):
    import random
    
    m = random.randint(1,n)
    list_random = []
    i=1
    while i <= m:
	    list_random.append(random.randint(-100,100))
	    i=i+1
    return list_random
lst = fulfil_lst(10)
print (lst)
print(my_filter(function,lst))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogramm (x1, y1, x2, y2, x3, y3, x4, y4):

	import math
	a= math.sqrt((x2-x1)**2+(y2-y1)**2)
	b= math.sqrt((x3-x2)**2+(y3-y2)**2)
	c= math.sqrt((x4-x3)**2+(y4-y3)**2)
	d= math.sqrt((x1-x4)**2+(y1-y4)**2)
	print(a)
	print(b)
	print(c)
	print(d)
	if a==c and b==d:
		return ("вершинами являются")
	else:
		return('вершинами не являются')

print(parallelogramm(0,0,0,2,2,0,2,2))


