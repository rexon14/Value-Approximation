from math import*
def f(x):
    F=(x**3)+2*x-8
    return(F)

epsi1=0.00001
epsi2=0.000001

a=int(input(""))
b=int(input(""))
c=(a+b)/2
while(abs(a-b)>=epsi1 and abs(f(c))>=epsi2):
    if(f(a)*f(c)<0):
        b=c
    else:
        a=c
    c=(a+b)/2
print(c)
