# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def upwind(alpha,Xi,Tj,phi_t0,psi_x0):
    #inizializzazione matrice U
    N=len(Xi)
    M=len(Tj)
    U=np.zeros((N,M))
    #condizione iniziale
    for i in xrange(N):
        U[i,0]=phi_t0(Xi[i])
    #condizione al bordo
    U[0,:]=psi_x0(Tj)
    #algoritmo
    for j in xrange(M-1):
        U[1:N,j+1]=(1.0-alpha)*U[1:N,j]+alpha*U[0:N-1,j]
    return U
#ESAME DI LUGLIO
c=0.5
a=-5.
b=5.
T0=0.
T=10.
N=42
M1=21
M2=41
Xi=np.linspace(a,b,N)
h=Xi[1]-Xi[0]
Tj1=np.linspace(T0,T,M1)
Tj2=np.linspace(T0,T,M2)
k1=Tj1[1]-Tj1[0]
k2=Tj2[1]-Tj2[0]
alpha1=c*k1/h
alpha2=c*k2/h
#definisco le funzioni phi e psi:
phi_t0= lambda x: 1.0/(np.sqrt(x**2 +2.0))
psi_x0= lambda t: 1.0/(np.sqrt( (5.0+t/2.0)**2 +2.0))
print('il numero di Courant per 21 nodi temporali: '),alpha1
print("il numero di Courant per 42 nodi temporali: "), alpha2
print
Uij1=upwind(alpha1,Xi,Tj1,phi_t0,psi_x0)
Uij2=upwind(alpha2,Xi,Tj2,phi_t0,psi_x0)
plt.figure(1)
plt.clf()
plt.plot(Xi,Uij1,'b')
plt.plot(Xi,Uij2,'g')
plt.show()

