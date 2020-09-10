import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    #scrivi l'espressione di f
    return abs(y-x) #inserisci f
    
def meteul(f):
    a=0.
    b=2.
    n=19
    h=(b-a)/n
    #inizializzo i vettori
    y0=2.
    x0=a
    X=np.zeros(n+1)
    X[0]=x0
    Y=np.zeros(n+1)
    Y[0]=y0
    print (0, X[0], Y[0])
    #algoritmo
    for i in range(n):
        X[i+1]=x0+h*(i+1)
        Y[i+1]=Y[i]+h*(f(X[i],Y[i]))
        print (i+1, X[i+1], Y[i+1])
    plt.plot(X,Y,"-b")
    plt.xlabel("x")
    plt.ylabel("$y_i$")
    plt.title("metodo di eulero")
    plt.show()
meteul(f)

