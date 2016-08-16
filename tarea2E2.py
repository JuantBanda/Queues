import random
import math

def comb(n,x):
    f = math.factorial
    return f(n)/(f(n-x)*f(x))
def prodprob(p,n,x):
    return (p**x)*((1-p)**(n-x))

class bernoulli:
    def __init__(self, p):
        self.proba=p
    def genbern(self):
        num=random.uniform(0,1)
        if(num>self.proba):#fracaso
            d=0
        else:#éxito
            d=1
        return(d)
    #def probbern

p=1/6#prob real
DB=bernoulli(p)
n=10000
cuentaexitos=0
for i in range(n):
    if(DB.genbern()==1):
        cuentaexitos+=1
pexp=cuentaexitos/n
print("**Pruebas Bernoulli**")
print("Prob bernoulli experimental",pexp)

class binomial(bernoulli):
    def __init__(self,p,n,x):
        bernoulli.__init__(self,p)
        self.ne=n #núm de ensayos
        self.pe=p
        self.xx=x
    def genbin(self):
        cuentaexitos=0
        for i in range(0,self.ne):
            if(self.genbern()==1):
                cuentaexitos+=1
        return cuentaexitos
    def probbin(self):
        return comb(self.ne,self.xx)*prodprob(self.pe,self.ne,self.xx)

p=0.6 #prob real
n=8
x=3
DBN=binomial(p,n,x)
N=1000
NE=0
for i in range(0,N):
    NE+=DBN.genbin()

promNE=NE/N
print("**Pruebas Binomial**")
print("Prob binomial (%f,%d,%d):"%(p,n,x),DBN.probbin())
print("V esp experimental:",promNE, "~~ V esp fórmula:", n*p)


class multinomial:
    def __init__(self, x,p,n):
        self.xs=x
        self.prob=p
        self.nn=n
    def genmn(self):
        if(sum(self.prob)==1 and sum(self.xs)==self.nn):
            f=math.factorial
            fn=f(self.nn)
            fns=1
            ps=1
            for i in range(0,len(self.xs)):
                fns=fns*f(self.xs[i])
                ps=ps*(self.prob[i])**self.xs[i]
            return (fn/fns)*ps
        else:
            return("Error de captura")

x=[2,1,3]
p=[2/9,1/6,11/18]
n=6
DMN=multinomial(x,p,n)
print("**Pruebas multinomial**")
print("Prob multinomial",DMN.genmn())


class geometrica(bernoulli):
    def __init__(self,p,x):
        bernoulli.__init__(self,p)
        self.pe=p
        self.xx=x
    def gengeom(self):
        cuentaensayos=0
        while(1):
            pr=self.genbern()
            cuentaensayos+=1
            if(pr==1):
                break
        return cuentaensayos
    def probgeom(self):
        rf=1
        return prodprob(self.pe,self.xx,rf)



p=0.4 #prob real
x=10
DG=geometrica(p,x)
#print("Prob geom",DG.gengeom())

N=10000
NE=0
for i in range(0,N):
    NE+=DG.gengeom()

promNE=NE/N
print("**Pruebas Geométrica**")
print("Prob Geom (%f,%d):"%(p,x),DG.probgeom())
print("V esp experimental:",promNE, "~~ V esp fórmula:", 1/p)

class pascal(bernoulli):
    def __init__(self,p,r,x):
        bernoulli.__init__(self,p)
        self.pe=p
        self.rr=r
        self.xx=x
    def genpascal(self):
        cuentaensayos=0
        cuentar=0
        while(1):
            pr=self.genbern()
            cuentaensayos+=1
            if(pr==1):
                cuentar+=1
                if(cuentar==self.rr):
                    break
        return cuentaensayos
    def probpascal(self):
        return comb(self.xx-1,self.rr-1)*prodprob(self.pe,self.xx,self.rr)

p=0.4 #prob real
x=10
r=3
DP=pascal(p,r,x)
N=10000
NE=0
for i in range(0,N):
    NE+=DP.genpascal()
promNE=NE/N
print("**Pruebas Pascal**")
print("Prob Pascal (%f,%d,%d):"%(p,r,x),DP.probpascal())
print("V esp experimental:",promNE, "~~ V esp fórmula:", r/p)

class poisson(binomial):
    def __init__(self,lamda,n,x):
        #binomial.__init__(self,p,n,x)
        self.lam=lamda
        self.nn=n
        self.xx=x
    def genpoisson(self):
        p=self.lam/self.nn
        x=1
        DBN=binomial(p,self.nn,x)
        return DBN.genbin()
    def probpoisson(self):
        return ((self.lam**self.xx)*math.exp(-self.lam))/math.factorial(self.xx)

lamda=2
n=1000
x=3
DPP=poisson(lamda,n,x)
N=1000
NE=0
for i in range(0,N):
    NE+=DPP.genpoisson()
promNE=NE/N
print("**Pruebas Poisson**")
print("Prob Poisson (%f,%d,%x):"%(lamda,n,x),DPP.probpoisson())
print("V esp experimental:",promNE, "~~ V esp fórmula:", lamda)
