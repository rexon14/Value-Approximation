#NIM	: 12217031
#NAMA	: Dennis
#TANGGAL: 22 Oktober 2018
#TOPIK PRAKTIKUM : Praktikum 08
#DESKRIPSI : Polinom Lagrange

def lagrange(X, Y, a, n):
	b = 0
	for i in range (n+1):
		pi=1
		for j in range(n+1):
			if (i!=j) :
				pi = pi*(a-X[j])/(X[i]-X[j])
		b = b+Y[i]*pi
	return(b)
X = [8.0,9.0,9.5]
Y = [2.0794,2.1972,2.513]
a = 9.2
n = 2
print(lagrange(X, Y, a, n))
