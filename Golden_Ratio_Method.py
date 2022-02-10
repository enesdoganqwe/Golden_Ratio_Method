import math

xalt=0
xust=4
DX=0.0001   # Bu değeri biz belirliyoruz.
tau=0.38197

def f(x):
    f=(x-1)**2*(x-2)*(x-3)
    return f

def Calculations():
    global xalt,xust,DX,tau
    eps=DX/(xust-xalt) # Tolerans değeri.
    N=-2.078*math.log(eps) # İterasyon sayısı.
    N=round(N) 
    x1=xalt+tau*(xust-xalt)
    f1=f(x1)
    x2=xust-tau*(xust-xalt)
    f2=f(x2)
    return N,f1,f2,x1 ,x2

N, f1, f2, x1, x2 = Calculations()

for k in range (1,N):
    if f1>f2:
        xalt = x1
        x1 = x2
        f1 = f2
        x2 = xust - tau * (xust - xalt)
        f2 = f(x2)
    else :
        xust = x2
        x2 = x1
        f2 = f1
        x1 = xalt + tau * (xust - xalt)
        f1 = f(x1)

# Deneme yazısı
print("x1 değeri = {}  , x2 değeri ={} , f1 değeri ={}  , f2 değeri = {}".format(x1,x2,f1,f2))
