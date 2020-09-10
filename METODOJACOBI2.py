import numpy as np
def jacobi(A,B,X0,eps,Nitermax):
    #inizializzazione vettori
    N=len(B)
    Xnew=np.zeros(N)
    Errk=np.zeros(Nitermax)
    err=10*eps
    Errk[0]=err
    icount=0
    while (err>eps) and (icount<Nitermax):
        for i in xrange(N):
            Xnew[i]=(-np.sum(A[i,:]*X0[:])+A[i,i]*X0[i]+B[i])/A[i,i]
        icount+=1
        err=np.max(np.abs(Xnew-X0))
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

Xnew,Errk,iterazioni=jacobi(A,B,X0,eps,Nitermax)
print ("soluzione approx: "), Xnew
print ("iterazioni: "), iterazioni