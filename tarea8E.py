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
    lam=.7
    DEXP=exponencial(lam)
    Nprom=0
    tprom=0
    repetir=1000000
    for i in range(repetir):
        t=0
        T=3
        N=0
        while(t<T):
            tn=DEXP.genexp()
            N+=N+1
            t+=tn
        Nprom+=N-1
        tprom+=t

    print("El número de entradas promedio es N=",Nprom/repetir, "con un tiempo prom en el sistema:",(Nprom/repetir)/lam)
if(__name__=="__main__"):
    main()
