# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
	number = number*(10**(ndigits+1))
	number_round = list(str(number%10))
	if int(number_round[0])<5:
		number = (number//10)/(10**(ndigits))
	elif int(number_round[0]) >5:
		number = (number//10+1)/(10**(ndigits))
	return (number)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(3.56738,3))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	ticket_number = list(str(ticket_number))
	if len(ticket_number)<6 or len(ticket_number)>6:
		return ("Паленый билет")
	if (int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2]))==(int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5])):
		return (" Cчастливый билет")
	else:
		return ('Купи другой билет')


import random
a = random.randint(100000,1000000)
print(a)
print(lucky_ticket(a))



    


print(lucky_ticket(123006))
print(lucky_ticket(12321)) 
print(lucky_ticket(436751))








