from math import log
from random import random
class proceso_muerte_puro:
    def __init__(self,mu,ni):
        self.mu=mu#tasa de muerte
        self.ni=ni
    def muerte(self):
        i=self.ni
        tt=0
        while i>0 and tt<30:
            t=-log(random())/(self.mu*i)
            i-=1
            tt+=t
        print(tt)

def main():
    mu=0.3#tasa de muerte
    ni=1000#numero de individuos
    PNM=proceso_muerte_puro(mu,ni)
    print(PNM.muerte())

if(__name__=="__main__"):
    main()
