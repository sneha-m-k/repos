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

	def __repr__(self):
		res=str(self.x) + " "
		if self.y >=0:
			res+=" "
		res+= str(self.y) + " "
		if self.z >=0:
			res+=" "
		res+= str(self.z) + " "
		return res
	def sq(self):
		return sqrt(self.x**2)
	def sq1(self):
	    return sqrt(self.y**2)
	def sq2(self):
	    return sqrt(self.z**2)
		
if __name__=="__main__":
	
	f1=Vector(1,2,3)
	f2=Vector(5,6,7)
	result= f1+f2
	result1=f2-f1
	print(abs(f1))
	print(f1.sq(),f1.sq1(),f1.sq2())
	print(result.x,result.y,result.z)
	print(result1.x,result1.y,result1.z)
	
	
	print(str(f1^f2))