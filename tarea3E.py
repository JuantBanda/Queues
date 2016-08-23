import random
#import math
import matplotlib.pyplot as plt
import numpy as np
from pylab import figure, axes, pie, title, show, legend
from math import log, sqrt, cos
ln=log
ru=random.uniform
raiz=sqrt

class exponencial:
    def __init__(self,lam):
        self.l=lam
    def genexp(self):
        return -ln(ru(0,1))/self.l

class erlang(exponencial):
    def __init__(self,lam, n):
        exponencial.__init__(self,lam)
        self.ll=lam
        self.nn=n
    def generlang(self):
        y=[self.genexp() for x in range(self.nn)]
        return sum(y)

class normal:
    #def __init__(self):
    def gennorm(self):
        print
        return raiz(-2*ln(ru(0,1)))*cos(2*3.1416*ru(0,1))

lam=3
NN=1000
DEXP=exponencial(lam)
DEr=erlang(lam,NN)
DNM=normal()
k=round(1+3.3*ln(NN,10))
MexpE=list()
MexpT=list()
MnormE=list()
MnormT=list()
MerlangE=list()

for i in range(NN):
    MexpE.append(DEXP.genexp())
    MexpT.append(random.expovariate(lam))
    MnormE.append(DNM.gennorm())
    MnormT.append(random.normalvariate(0,1))#mu=0 sigma=1
    MerlangE.append(DEr.generlang())

VEexpE=sum(MexpE)/NN
VEnormE=sum(MnormE)/NN
VEerlangE=sum(MerlangE)/NN

plt.ion()
plt.hist(MexpE,bins=k)
plt.savefig("figexpE.png")
plt.close()
plt.hist(MexpT,bins=k)
plt.savefig("figexpT.png")
plt.close()
plt.hist(MnormE,bins=k)
plt.savefig("fignormE.png")
plt.close()
plt.hist(MnormT,bins=k)
plt.savefig("fignormT.png")
plt.close()

FexpE=np.histogram(MexpE,k)
FexpE=FexpE[0]
Fr_expE=list()#Frecuencia relativa
Fa_expE=list()
Fr_expE=FexpE/NN
Fa_expE.append(Fr_expE[0])
FexpT=np.histogram(MexpT,k)
FexpT=FexpT[0]
Fr_expT=list()#Frecuencia relativa
Fa_expT=list()
Fr_expT=FexpT/NN
Fa_expT.append(Fr_expT[0])

FnormE=np.histogram(MnormE,k)
FnormE=FnormE[0]
Fr_normE=list()#Frecuencia relativa
Fa_normE=list()
Fr_normE=FnormE/NN
Fa_normE.append(Fr_normE[0])
FnormT=np.histogram(MnormT,k)
FnormT=FnormT[0]
Fr_normT=list()#Frecuencia relativa
Fa_normT=list()
Fr_normT=FnormT/NN
Fa_normT.append(Fr_normT[0])

for i in range(1,k):
    Fa_expE.append(Fr_expE[i]+Fa_expE[i-1])
    Fa_expT.append(Fr_expT[i]+Fa_expT[i-1])
    Fa_normE.append(Fr_normE[i]+Fa_normE[i-1])
    Fa_normT.append(Fr_normT[i]+Fa_normT[i-1])

plt.plot(Fa_expE, label="Exp E", linewidth=5, color="blue")
plt.plot(Fa_expE, label="Exp T", linewidth=5, color="red", linestyle="dashed")
plt.legend()
plt.savefig("figExpAcum.png")
plt.close()

plt.plot(Fa_normE, label="Norm E", linewidth=5, color="blue")
plt.plot(Fa_normE, label="Norm T", linewidth=5, color="red", linestyle="dashed")
plt.legend()
plt.savefig("figNormAcum.png")
plt.close()

print("V esp E de exp",VEexpE, "; ""V esp T de exp", 1/lam)
print("V esp E de norm",VEnormE, "; ""V esp T de norm", "0")
print("V esp E de erlang",VEerlangE, "; ""V esp T de erlang", NN/lam)
