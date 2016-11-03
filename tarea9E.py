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
    lam=2#tasa de llegada
    mu=.7#tasa de servicio
    DE=exponencial(lam)
    DS=exponencial(mu)

    #MM33
    TT=100
    T=0
    s=3#número de servidores
    NEM=3#número máximo de cliente en la cola
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
    #llegadas=[1.5,1.75,1.9,2.5,5,6.3,7,9,9.5, 10.1]
    llegadas.sort()
    tiempos=llegadas[:]
    N=len(llegadas)-1
    #print("##############################################################")
    #print("llegadas", llegadas)
    ne=llegadas.pop(0)
    Ta=tiempos[0]
    NE=0#clientes en espera de servicio
    while(T<TT):
        T=tiempos.pop(0)
        #print(ne)
        if(T==ne):
            ne=llegadas.pop(0)
            if(so<s):
                ts=DS.genexp()
                #print("ts",ts)
                salidas.append(T+ts)
                salidas.sort()
                tiempos.append(T+ts)
                tiempos.sort()
                NA+=1
                so+=1
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
                #print("ts holas>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",ts)
                salidas.append(T+ts)
                salidas.sort()
                tiempos.append(T+ts)
                tiempos.sort()
                NA+=1
                so+=1
                NE-=NE

        if(len(llegadas)==0):
            break

        #print("Reloj",T)
        #print("salidas",salidas)
        #print("_____________________")

    print("Núm cl>>",N,"Cl atendidos>>", NA-len(salidas),
    "Cl en cola>>",N-NA-NF,"cl en serv>>",len(salidas), "Fuga de cl>>",NF,"t de sim>>", T )



if(__name__=="__main__"):
    main()
