#NAMA: Dennis
#NIM: 12217031
#TANGGAL: 17 September 2018
#TOPIK PRAKTIKUM: Praktikum 04
#DESKRIPSI: jarak terdekat kumpulan titik koordinat
from math import*

def jarak_terdekat(absis, ordinat):
	if(len(absis)>1):
		for i in range(0,len(absis)):
			for j in range(0,len(absis)):
				hasil=((absis[i]-absis[j])**2)+((ordinat[i]-ordinat[j])**2)
				if(i!=j):
					if(i==0 or minimal>hasil):
						minimal=hasil
		return(round(sqrt(minimal),2))
	else:
		return(-1)
	





