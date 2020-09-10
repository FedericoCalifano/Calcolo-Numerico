# -*- coding: utf-8 -*-
#metodo di newton per i sistemi n=2 :
#f(x,y)=0
#g(x,y)=0
from numpy import zeros
import numpy as np
import sys
import matplotlib.pyplot as plt
#funzioni esterne 
def f(x,y):
    return 2.0*x-0.0002*x*y-0.0001*x**2
def g(x,y):
    return 4.0*y-0.0003*y**2 -0.0004*x*y
def derxx_f(x,y):
    return 2.0-2.0*y*10**-4 -2.0*x*10**-4
def derxy_f(x,y):
    return -2.0*x*10**-4
def derxx_g(x,y):
    return 4.0-6.0*y*10**-4 -4.0*x*10**-4
def derxy_g(x,y):
    return -4.0*y*10**-4
#
def newton(xold,yold,nitermax,eps):
    #inizializzazione vettori
    err=zeros(nitermax+1)
    err[0]=eps+1.0
    
    #
    #metodo
    it=0
    while (err[it]>eps) and (it<nitermax):
        fold,gold=f(xold,yold),g(xold,yold)
        fxold,fyold=derxx_f(xold,yold),derxy_f(xold,yold)
        gxold,gyold=derxx_g(xold,yold),derxy_g(xold,yold)
        jacobian=fxold*gyold -fyold*gxold
        if jacobian!=0:
            xnew=xold-(fold*gyold-gold*fyold)/(jacobian)
            ynew=yold-(gold*fxold-fold*gxold)/(jacobian)
        else:
            print("non è garantita la convergenza del metodo")
            sys.exit()
        it+=1
        err[it]=np.max(np.abs([xnew-xold,ynew-yold]))
        print(jacobian)
        xold,yold=xnew,ynew
    return xnew,ynew,err,it
nitermax=30
xold,yold=3988,7988
eps=0.5*10.0**-7
xnew,ynew,err,iterazioni=newton(xold,yold,nitermax,eps)
print ("la soluzione approssimata: "),[xnew,ynew]
print("n.iter: "),iterazioni
plt.figure(1)
plt.clf()
plt.plot(err,'-o')
plt.xlabel("iter")
plt.show()