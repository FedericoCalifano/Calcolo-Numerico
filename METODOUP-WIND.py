# -*- coding: utf-8 -*-
#dati di input
#c velocità di trasporto
#T0,T intervallo temporale
#a,b intervallo spaziale
#M passi temporali
#N nodi spaziali interni
#
#dati di output
# Xi, Tj nodi 
#U[0:N+1,0:M] soluzione approssimata
#
#function
#phi_t0(x):condizione iniziale
#psi_xl(t):condizione bordo sinistro
#psi_xr(t):condizione bordo destro
import numpy as np
import sys
import matplotlib.pyplot as plt
#condizioni iniziali e al bordo
phi_t0= lambda x:
psi_xl= lambda t:
psi_xr= lambda t:
#dati di input
dati_input=raw_input("inserire i valori c,T0,T,a,b,M,N separati da uno spazio: ")
dati=[]
for valore in dati_input:
    try: 
        dati.append(float(valore))
    except:
        print("i dati inseriti devono essere separati da uno spazio")
        sys.exit()
if len(dati)!=7:
    print("devi inserire 7 numeri")
    sys.exit()
c,T0,T,a,b,M,N=dati[0],dati[1],dati[2],dati[3],dati[4],int(dati[5]),int(dati[6])
#nodi
h=(b-a)/(N+1)
k=(T-T0)/M
Xi=np.linspace(a,b,N+2)
Tj=np.linspace(T0,T,M+1)
#numero di courant
alpha=c*k/h
print("numero di courant: ",alpha)
def upwind(Xi,Tj,N,M,psi_xr,psi_xl,phi_t0,alpha):
    U=np.zeros((N+2,M+1))
    #condizione iniziale
    for i in xrange(N+2):
        U[i,0]=phi_t0(Xi[i])
    #condizioni al bordo
    U[0,:]=psi_xl(Tj)
    U[N+1,:]=psi_xr(Tj)
    #algoritmo
    for j in xrange(M):
        U[1:N+1,j+1]=(1-alpha)*U[1:N+1,j]+alpha*U[0:N,J]
    #grafico 2D
    plt.figure(1)
    plt.clf()
    plt.plot(Xi,U)
    plt.show()
    