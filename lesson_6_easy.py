# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class triangles:	
	def __init__(self, A,B,C):
		self.A=A
		self.B=B
		self.C=C
		from math import sqrt
		self.AB = sqrt((self.B[0]-self.A[0])**2+(self.B[1]-self.A[1])**2)
		self.AC = sqrt((self.C[0]-self.A[0])**2+(self.C[1]-self.A[1])**2)
		self.BC = sqrt((self.C[0]-self.B[0])**2+(self.C[1]-self.B[1])**2)
		self.H1 = 0
		self.H2 = 0
		self.H3 = 0 
		self.S = 0
	def len_side(self):
		print ('Сторона АВ - ', self.AB, 'Сторона АС - ', self.AC, 'Сторона ВC - ',self.BC)
	def perimetr(self):
		self.P = self.AB + self.AC + self.BC
		return self.P
	def square(self):
		from math import sqrt
		p=self.perimetr()/2
		self.S = sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.AC))
		return self.S
	def heigth(self):
		self.H1 = 2*self.square()/self.AB
		self.H2 = 2*self.square()/self.BC
		self.H3 = 2*self.square()/self.AC
		return self.H1, self.H2, self.H3

tr = triangles((1,9),(2,5), (3,6))
print(tr.A)
print (tr.len_side())
print(tr.perimetr())
print(tr.square())
print(tr.heigth())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapecia:	
	def __init__(self, A,B,C,D):
		self.A=A
		self.B=B
		self.C=C
		self.D=D
		from math import sqrt
		self.AB = sqrt((self.B[0]-self.A[0])**2+(self.B[1]-self.A[1])**2)
		self.BC = sqrt((self.C[0]-self.B[0])**2+(self.C[1]-self.B[1])**2)
		self.CD = sqrt((self.D[0]-self.C[0])**2+(self.D[1]-self.C[1])**2)
		self.AD = sqrt((self.D[0]-self.A[0])**2+(self.D[1]-self.A[1])**2)
		self.AC = sqrt((self.C[0]-self.A[0])**2+(self.C[1]-self.A[1])**2)
		self.BD = sqrt((self.D[0]-self.B[0])**2+(self.D[1]-self.B[1])**2)
		self.P = 0
		self.H = 0
		self.S = 0
	def proverka(self):
		if self.AC==self.BD:
			print("Трапеция является равнобочной") 
		else:
			print("Трапеция не является равнобочной")

	def len_side(self):
		print ('Сторона АВ - ', self.AB, 'Сторона BC - ', self.BC, 'Сторона CD - ',self.CD, 'Сторона AD - ', self.AD)
	def perimetr(self):
		self.P = self.AB + self.BC + self.CD + self.AD
		return self.P
	def height(self):
		from math import sqrt
		cos_angle = (self.AB**2 + self.AD**2 - self.BD**2)/(2*self.AB**2*self.AD**2)
		sin_angle = sqrt(1-cos_angle**2)
		self.H = self.AB*sin_angle
		return self.H 
	def square(self):
		self.S = ((self.AD + self.BC)*self.height())/2
		return self.S

trap = Trapecia((1,9),(2,5),(3,6),(12,6))
print (trap.len_side())
print(trap.square())
print(trap.perimetr())
print(trap.height())
print(trap.proverka())

		

























