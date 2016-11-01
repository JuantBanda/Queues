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
    lam=1.5#tasa de llegada
    mu=.7#tasa de servicio
    DE=exponencial(lam)
    DS=exponencial(mu)


    TT=10
    T=0
    s=3#número de servidores
    so=0#servidores ocupados
    ne=0#nueva entrada
    ns=10000#nueva salida
    N=0 #clientes en el sistema
    NA=0#clientes atendidos
    NE=0#clientes en espera
    xns=1000
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
    #print("##############################################################")
    #print("num clientes",len(llegadas)-1)
    #ne=llegadas.pop(0)
    ne=0
    ns=1000
    #tiempos=[1.5,1.75,1.9,2.5,5,6.3,7,9,9.5, 10.1]
    #print(tiempos)
    #print("_____________________")

    while(T<TT):
        T=tiempos.pop(0)
        #print(ne)
        if(ne<ns):
            ne=llegadas.pop(0)

            if(so<2):
                ts=DS.genexp()
                #print("ts",ts)
                salidas.append(T+ts)
                salidas.sort()
                tiempos.append(T+ts)
                tiempos.sort()
                NA+=1
                so+=1
                ns=salidas[0]
        else:
            ns=salidas.pop(0)
            so-=1
            if(len(salidas)==0):
                ns=1000

        if(len(llegadas)==0):
            break

#        print("Reloj",T)
#        print("salidas",salidas)
#        print("ne>>", ne)
#        print("ns>>", ns)
#        print("_____________________")
    #print("tiempos", tiempos)
    #print("clientes atendidos", NA)

    print("Núm clientes",N,">>Clientes atendidos", NA,">>t de sim", T )



if(__name__=="__main__"):
    main()
