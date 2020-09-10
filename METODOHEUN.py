import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return abs(y-x) #inserisci f
def metheun(f):
    #dati input
    a=0.
    b=2.
    y0=2.
    #nodi
    n=19
    h=(b-a)/n
    #inizializzo i vettori
    X=np.zeros(n+1)
    Y=np.zeros(n+1)
    X[0]=a
    Y[0]=y0
    print (0, X[0], Y[0])
    #algoritmo Heun
    for i in range(n):
        X[i+1]=X[0]+(i+1)*h
        Y[i+1]=Y[i]+0.5*h*(f(X[i],Y[i])+f(X[i]+h,Y[i]+h*f(X[i],Y[i])))
        print(i+1, X[i+1], Y[i+1])
    plt.plot(X,Y,"-o")
    plt.xlabel("X")
    plt.ylabel("$y_i$")
    plt.title("metodo di heun")
    plt.show()
metheun(f)