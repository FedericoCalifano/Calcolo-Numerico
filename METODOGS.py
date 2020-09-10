import numpy as np
from numpy.linalg import eigvals
import matplotlib.pyplot as plt
import sys
def gs(A,B,X0,eps,Nitermax):
    #inizializzo i vettori
    N=len(B)
    Xnew=np.zeros(N)
    Errk=np.zeros(Nitermax)
    #M=D+L , N=U CGs=-(D+L)-1U , QGs=(D+l)-1B
    DL=np.tril(A)
    DLinv=np.linalg.inv(DL)
    U=np.triu(A,1)
    Cgs=-np.dot(DLinv,U)
    print(eigvals(Cgs))
    if np.max(np.abs(eigvals(Cgs)))>1.0:
        print("il metodo di gauss seidel non converge")
        sys.exit()
    Qgs=np.dot(DLinv,B)
    #metodo
    Errk[0]=10*eps
    icount=0
    while (Errk[icount]>eps) and icount<Nitermax:
        Xnew=np.dot(Cgs,X0)+Qgs
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