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
    lam=1.5
    DEXP=exponencial(lam)
    t=0
    T=30
    N=0
    while(t<T):
        tn=DEXP.genexp()
        N+=N+1
        t+=tn
    print("El número de entradas en t=",t, "es:",N-1)
if(__name__=="__main__"):
    main()
