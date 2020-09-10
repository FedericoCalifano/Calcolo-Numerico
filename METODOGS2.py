# -*- coding: utf-8 -*-
#gauss seidel elemento per elemento
from numpy import zeros,prod,diag
import numpy as np
import sys
#non verifico la convergenza del metodo in questo modo
def gs(A,B,X0,eps,Nitermax):
    if prod(diag(A))==0:
        print("il sistema non ammette unica soluzione, la matrice A non è regolare")
        sys.exit()
    N=len(B)
    Errk=zeros(Nitermax)
    Xnew=zeros(N)
    Errk[0]=10.0*eps
    icount=0
    while (Errk[icount]>eps) and (icount<(Nitermax)):
        for i in range(N):
            Xnew[i]=(-np.sum(A[i,:i]*Xnew[:i])-np.sum(A[i,i+1:N]*X0[i+1:N])+B[i])/A[i,i]
        icount+=1
        Errk[icount]=np.max(np.abs(Xnew-X0))
        X0=Xnew.copy()
    return Xnew, Errk, icount-1
N=10
Nitermax=100
X0=np.zeros(N)
eps=0.5*10.0**(-2)
#devo definire A e B
D=np.zeros(N)
B=np.zeros(N)
for i in xrange(N):
    D[i]=5.0
    B[i]=1.0/(np.sqrt(float(i)+1))
S=np.zeros(N-1)
I=np.zeros(N-1)
for i in xrange(N-1):
    S[i]=-2.5
    I[i]=-2.5
A=np.diag(D)+np.diag(S,+1)+np.diag(I,-1)

Xnew,Errk,iterazioni=gs(A,B,X0,eps,Nitermax)
print ("soluzione approx: "), Xnew
print ("iterazioni: "), iterazioni
    