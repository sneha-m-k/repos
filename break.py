n=int(input("enter a no above 1000:"))
if n>1000:
	a=n/1000
	print 1000,a
	b=n%1000
	if b>500:
		c=b/500
		print 500,c
		d=b%500
		if d>100:
			e=d/100
			print 100,e
			f=d%100

			if f>50:
				g=f/50
				print 50,g
				h=f%50
				if h>20:
					i=h/20
					j=h%20
					print 20,i
					if j>10:
						k=j/10
						l=j%10
						print 10,k
						if l>1:
							print 1,l
					
					





