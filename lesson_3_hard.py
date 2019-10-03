
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


import math
example= input('')
solution = ''
example= example.split()

a=example[0] # первый элемент
b=example[2] # второй элемент
c = example[1] # знак операции

def NOD (m,n):
    m=int(m)
    n=int(n)
    m=math.fabs(m)
    while m!=0 and n!=0:
    	if m > n:
        	m %= n
    	else:
        	n %= m
    nod=int(m+n)
    return nod
    print(nod)
def selection (numerator, denominator):
	if math.fabs(numerator)>denominator:

		whole_part = int(math.fabs(numerator)//denominator)
		remainder_numerator = str(numerator-denominator*whole_part)
		whole_part = str(numerator//denominator)
		denominator = str(denominator)
		solution = whole_part + ' ' + remainder_numerator + '/' + denominator
		return (solution)
		print (solution)
	else:
		denominator = str(denominator)
		numerator = str(numerator)
		solution = numerator + '/' + denominator
		return (solution)
		print (solution)
def reduction (x,y):
    Nod = NOD (x,y)
    if x>0:
        x = int (math.fabs(x)/Nod)
        y = int(y/Nod)
        return(selection(x,y))
        print(selection(x,y))
    elif x<0:
        x = int (math.fabs(x)/Nod)
        y = int(y/Nod)
        k = selection (x,y)
        k = k.split()
        k.insert(0,'-')
        k=' '.join(k)
        return k
        print (k)

if ('/' in a)  and ('/' in b):
	xy= a.split('/')
	x=int(xy[0]) #x - числитель 1
	y=int(xy[1]) #у - знаменатель 1
	x1y1= b.split('/')
	x1=int(x1y1[0]) #x1 - числитель 2 
	y1=int(x1y1[1]) #у1 - знаменатель 2 
	denom=y*y1 # знаменатель после сложения 
	num1 = x*y1 # числитель 1 к новому знаменателю
	num2 = x1*y # числитель 2 к новому знаменателю
	if c=='-':
		num=num1-num2
	if c=='+':
		num=num1+num2
	print (reduction(num, denom))


elif ('/' in a):
	xy= a.split('/')
	x=int(xy[0])
	y=int(xy[1])
	b=int(b)
	denom=y
	num1=x
	num2=y*b
	if c=='-':
		num=num1-num2
	if c=='+':
		num=num1+num2
	print (reduction(num, denom))

elif ('/' in b):
	x1y1= b.split('/')
	x1=int(x1y1[0])
	y1=int(x1y1[1])
	a= int(a)
	denom=y1
	num1=a*y1
	num2=x1
	if c=='-':
		num=num1-num2
	if c=='+':
		num=num1+num2
	print (reduction(num, denom))
		
elif ('/' not in a) and ('/' not in b):
	if c=='-':
		n=int(a)-int(b)
		print(n)
	if c=='+':
		n=int(a)+int(b)
		print(n)

