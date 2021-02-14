from math import sqrt

class Vector:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def __add__(self,other):
		return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

	def __sub__(self,other):
		return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

	def __xor__(self,other):
		return Vector(self.x*other.x,self.y*other.y,self.z*other.z)

f1=Vector(1,2,3)
f2=Vector(5,6,7)
result= f1+f2
result1=f2-f1
print(result.x,result.y,result.z)
print(result1.x,result1.y,result1.z)
