#NIM : 12217031
#Nama : Dennis
#Tanggal : 29 Oktober 2018
#Topik praktikum : Praktikum 09
#Deskripsi : program metode runge kutta orde 4

def f(x,y):
	fungsi = (x*0) + 1 + (y*y)
	return fungsi
def runge_kutta(x0,y0,b,h):
	n = (b-x0)/h
	y = y0
	x = x0
	
	for i in range (1,int(n+1)):
		k1 = h*f(x,y)
		k2 = h*f(x + (h/2), y + (k1/2))
		k3 = h*f(x + (h/2), y + (k2/2))
		k4 = h*f(x +h,y+k3)
		y = y +(k1 + (2*k2) + (2*k3) + k4)/6
		x = x +h
	return y

