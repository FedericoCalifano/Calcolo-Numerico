# -*- coding: utf-8 -*-
#OSS: I NODI DEVONO ESSERE EQUISPAZIATI E DISPARI IN NUMERO xi=x0+ih con i=0,..,n e h=(b-a)/n
def parabola(xnodi,fnodi):
    from numpy import sum
    import sys
    if len(xnodi)%2==0:
        print ("il metodo delle parabole non può essere utilizzato per un numero di nodi dispari")
        sys.exit()
    N=len(xnodi)-1
    h=xnodi[1]-xnodi[0]
    Ip=h/3.0 *(fnodi[0]+fnodi[N]+4.0* sum(fnodi[1:N:2]) +2.0* sum(fnodi[2:N:2]))
    return Ip
#
def trapezi(xnodi,fnodi):
    from numpy import sum
    N=len(xnodi)-1
    h=xnodi[1]-xnodi[0]
    It=h/2.0 *(fnodi[0]+fnodi[N]+2.0* sum(fnodi[1:N]))
    return It
import numpy as np
from scipy import integrate
xnodi=np.linspace(0.,84.,num=15)
fnodi=np.array([124.,134.,148.,156.,147.,133.,121.,109.,99.,85.,78.,89.,104.,116.,123.])
It1=integrate.trapz(fnodi,xnodi)
Ip1=integrate.simps(fnodi,xnodi)
print ("Ip con sommatoria: "),parabola(xnodi,fnodi)
print("Ip1 con integrate.simps: "),Ip1
print ("It con sommatoria: "),trapezi(xnodi,fnodi)
print("It1 con np.trapz: "),It1