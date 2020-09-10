import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return abs(y-x)
def metrk(f):
    #dati input
    a=0.
    b=2.
    y0=2.
    #nodi
    n=19
    h=(b-a)/n
    #inizializzazione vettori
    X=np.zeros(n+1)
    Y=np.zeros(n+1)
    X[0]=a
    Y[0]=y0
    print(0, X[0], Y[0])
    k1=np.zeros(n+1)
    k2=np.zeros(n+1)
    k3=np.zeros(n+1)
    k4=np.zeros(n+1)
   #algoritmo
    for i in range (n):
        X[i+1]=X[0]+h*(i+1)
        #funzioni k
        k1[i]=f(X[i],Y[i])
        k2[i]=f(X[i]+h/2,Y[i]+(h/2)*k1[i])
        k3[i]=f(X[i]+h/2,Y[i]+(h/2)*k2[i])
        k4[i]=f(X[i]+h,Y[i]+h*k3[i])
        #
        Y[i+1]=Y[i]+(1.0/6)*h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])
        print (i+1, X[i+1], Y[i+1])
    plt.plot(X,Y,"-o")
    plt.xlabel("X")
    plt.ylabel("$y_i$")
    plt.title("metodo runge-kutta classico")
    plt.show()
metrk(f)