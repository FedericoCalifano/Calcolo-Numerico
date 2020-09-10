#Soluzione problema differenziale ai limiti con metodo alle differenze finite
# y''=p(x)y'+q(x)y-r(x)
#y(a)=alpha
#y(b)=beta
#passo h=(b-a)/N+1
#
#definiamo una function che restituisca la matrice dei coefficienti S e il vettore dei termini noti B
import sys
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
def ODE_sistlin(alpha,beta,Xi,p,q,r):
    #inizializzazione array
    N=len(Xi)-2
    h=Xi[1]-Xi[0]
    S=np.zeros((N,N))
    B=np.zeros(N)
    #nodo x_1
    S[0,0]=2.0+h**2 * q(Xi[1])
    S[0,1]=-1.0+(h/2) * p(Xi[1])
    B[0]=h**2 * r(Xi[1])+(1.0+(h/2)*p(Xi[1]))*alpha
    #nodi interni
    for i in range (2,N):
        S[i-1,i-1]=2.0 +h**2 *q(Xi[i])
        S[i-1,i]=-1.0+(h/2)*p(Xi[i])
        S[i-1,i-2]=-1.0-(h/2)*p(Xi[i])
        B[i-1]=h**2 *r(Xi[i])
    #nodo x_N
    S[N-1,N-1]=2.0+ h**2 *q(Xi[N])
    S[N-1,N-2]=-1.0-h*0.5*p(Xi[N])
    B[N-1]=h**2 *r(Xi[N])+(1.0-h*0.5*p(Xi[N]))*beta
    return S, B
def metdfin():
    #termini noti p.differenziale
    p= lambda x:2.0/x
    q= lambda x:-2.0/x**2
    r= lambda x:-np.sin(np.log(x))/x
    #dati input
    coefficienti=raw_input("inserisci a,b,alpha,beta,N separati da uno spazio: ")
    num=[]
    for numero in coefficienti.split():
        try:
            num.append(float(numero))
        except:
            print("i numeri devono essere separati da uno spazio")
            sys.exit()
    if len(num)!=5:
        print("devi inserire 5 numeri")
        sys.exit()
    #dati input
    a, b , alpha, beta, N=num[0], num[1], num[2], num[3], num[4]
    print ("dati input: "), a, b ,alpha, beta, N
    #passo
    h=(b-a)/(N+1)
    Xi=a +np.arange(N+2)*h
    A,B=ODE_sistlin(alpha,beta,Xi,p,q,r)
    Yi=np.linalg.solve(A,B)
    Yi=np.concatenate(([alpha],Yi,[beta]))
    print Xi
    print Yi
    plt.figure(1)
    plt.plot(Xi,Yi,"b*-")
    plt.xlabel("x")
    plt.show()
