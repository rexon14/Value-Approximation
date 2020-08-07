from math import*
def f(x):
    F=(x**3)+2*x-8
    return(F)

epsi1=0.00001
epsi2=0.000001

a=float(input(""))
b=float(input(""))
c=b-(f(b)*(b-a)/(f(b)-f(a)))
while(abs(a-b)>epsi1):
    if(abs(f(c))<epsi2):
        a=c
        b=c
    else:
        if(f(a)*f(c)<0):
            b=c
        else:
            a=c
        c=b-(f(b)*(b-a)/(f(b)-f(a)))

print(c)
