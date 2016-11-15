from math import log
import random
ln=log
ru=random.uniform
class exponencial:
    def __init__(self,lam):
        self.l=lam
    def genexp(self):
        return -ln(ru(0,1))/self.l

def main():
    lam=.6#tasa de llegada
    mu=.7#tasa de servicio
    DE=exponencial(lam)
    DS=exponencial(mu)
    acumN=0
    acumtperm=0
    for i in range(10000):

        #MM1 infinito
        TT=100
        T=0
        s=1#número de servidores
        NEM=10000000000#número máximo de cliente en la cola
        so=0#servidores ocupados
        N=0 #clientes en el sistema
        NA=0#clientes atendidos
        NE=0#clientes en espera
        NF=0#número de clientes que no entran a la cola
        llegadas=list()
        salidas=list()
        tiempos=list()
        a=0
        while(a<TT):
            te=DE.genexp()
            llegadas.append(a+te)
            a+=te
        llegadas.sort()
        tiempos=llegadas[:]
        tll=llegadas[:]
        N=len(llegadas)-1
        ne=llegadas.pop(0)
        NE=0#clientes en espera de servicio
        tperm=0
        #print(tll)
        while(T<TT):
            T=tiempos.pop(0)
            if(T==ne):
                nea=ne
                ne=llegadas.pop(0)
                if(so<s):
                    ts=DS.genexp()
                    salidas.append(T+ts)
                    salidas.sort()
                    tiempos.append(T+ts)
                    tiempos.sort()
                    tp=T+ts-tll[NA]
                    #print(tll[NA])
                    NA+=1
                    so+=1
                    tperm+=tp
                else:
                    if(NE==NEM):
                        NF+=1
                    else:
                        NE+=1
            else:
                ns=salidas.pop(0)
                so-=1
                if(NE>0):
                    ts=DS.genexp()
                    salidas.append(T+ts)
                    salidas.sort()
                    tiempos.append(T+ts)
                    tiempos.sort()
                    tp=T+ts-tll[NA]
                    #print(tll[NA])
                    NA+=1
                    so+=1
                    tperm+=tp
                    NE-=NE

            if(len(llegadas)==0):
                break
        acumN+=N
        acumtperm+=tperm

    print("t prom de permanencia(teó):%.2f, t prom de permanencia(exp):%.2f"%(1/(mu-lam),acumtperm/acumN))
if(__name__=="__main__"):
    main()
