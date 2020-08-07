#NIM : 12217031
#Nama : Dennis
#Tanggal : 29 Oktober 2018
#Topik praktikum : Praktikum 09
#Deskripsi : program kaidah trapesium, titik tengah dan simpson 1/3

def f(x):
	fungsi = 1/(1+x)
	return fungsi
def trapesium(a,b,n):
	h = (b-a)/n
	x = a
	r = f(a) + f(b)
	sigma=0
	
	for i in range(1,n):
		x = x+h
		sigma=sigma+f(x)
	r = (r+2*sigma)*h/2
	return "%.10f"%r
def titiktengah(a,b,n):
	h = (b-a)/n
	x = a+h/2
	sigma = f(x)
	for i in range(1,n):
		x=x+h
		sigma=sigma+f(x)
	r = sigma*h
	return "%.10f"%r
def simpson(a,b,n):
	h = (b-a)/n
	x = a
	r = f(a) + f(b)
	sigma = 0
	for i in range(1,n):
		x = x+h
		if(i%2==1):
			sigma=sigma+4*f(x)
		else:
			sigma=sigma+2*f(x)
	r = (r+sigma)*h/3
	return "%.10f"%r

var=str(input())
if(var=='a'):
	l=int(input())
	u=int(input())
	n=int(input())
	print(trapesium(l,u,n))
elif(var=='b'):
	l=int(input())
	u=int(input())
	n=int(input())
	print(titiktengah(l,u,n))
elif(var=='c'):
	l=int(input())
	u=int(input())
	n=int(input())
	print(simpson(l,u,n))



