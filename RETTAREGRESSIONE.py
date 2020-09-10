import numpy as np
import scipy
import matplotlib.pyplot as plt
#dati iniziali
Xn=np.array([2,3,4,5,6,8,10])
Fn=np.array([7.0,8.3,9.4,11.3,12.3,14.4,15.9])
#calcolo coefficienti retta di regressione
p=scipy.polyfit(Xn,Fn,1)
print p
#grafico della retta di regressione
X2=np.linspace(Xn[0],Xn[-1])
Y2=scipy.polyval(p,X2)
plt.figure()
plt.plot(Xn,Fn,'ro',X2,Y2,'b')
plt.ylabel("F(X)")
plt.xlim(1,11)
plt.show()