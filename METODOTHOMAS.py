import matplotlib.pyplot as plt
from numpy import zeros,arange
def thomas(D,A,S,B):
    N=len(B)
    U=zeros(N)
    alpha=zeros(N-1)
    Y=zeros(N)
    X=zeros(N)
    #fattorizzazione LU
    U[0]=D[0]
    for i in range(N-1):
        alpha[i]=A[i]/U[i]
        U[i+1]=D[i+1]-alpha[i]*S[i]
    #soluzione del sistema lineare
    #LY=B
    Y[0]=B[0]
    for i in range (1,N):
        Y[i]=B[i]-alpha[i-1]*Y[i-1]
    #UX=Y
    X[N-1]=Y[N-1]/U[N-1]
    for i in range(N-2,-1,-1):
        X[i]=(Y[i]-S[i]*X[i+1])/U[i]
    return X
#ESAME DI LUGLIO
N=30
print(N)
D=zeros(N)
for i in range(N):
    D[i]=i+1.0
A=zeros(N-1)
S=zeros(N-1)
S[0]=1.0
for i in xrange(N-1):
    A[i]=-(i+2.0-1.0)/2.0
    S[i]=+(i+2.0+1.0)/2.0
B=zeros(N)
for i in range(1,N+1):
    B[i-1]=-1.00**i
X=thomas(D,S,A,B)
print (X)
i=arange(1,N+1)
plt.figure(1)
plt.clf()
plt.plot(i,X)
plt.xlabel("n")
plt.ylabel("X")
plt.show()