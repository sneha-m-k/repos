n=int(input("enter a no above 1000:"))
if n>1000:
	a=n/1000
	print 1000,a
	n=n%1000
if n>500:
	b=n/500
	print 500,b
	n=n%500
if n>100:
	c=n/100
	print 100,c
	n=n%100

if n>50:
	d=n/50
	print 50,d
	n=n%50
if n>20:
	e=n/20
	n=n%20
	print 20,e
if n>10:
	f=n/10
	n=n%10
	print 10,f
if n>1:
	print 1,n