#from collections import defaultdict
from random import random
from math import log
#import random
#ru=random.uniform
class procesoMarkov(dict):
    def __init__(self):
        dict.__init__(self)
        self.N=set()
        self.tiempos=dict()
    #    self.visitas=dict()
        #self.res=dict()
        #self.vecinos=dict()

    def agrega(self,x,y,tasa):
        self.N.add(x)
        self.N.add(y)
        self[x,y]=tasa
        self.tiempos[x,y]=-log(random())/tasa

    def verifica(self):
        for i in self.N:
            sum=0
            for j in self.N:
                if(i,j) in self:
                    sum+=self[i,j]
            self[i,i]=-sum
        return self

    def calculos(self):
        #self.verifica()
        print(self)
        print(self.tiempos)
        mt=min(self.tiempos.values())#mínimo tiempo
        print (mt)
        for (i,j) in self:
            if(self.tiempos[i,j]==mt):
                mv=(i,j)
                print(i)
                break
        print(mv)
        #return self.tiempos

def main():

    PM=procesoMarkov()
    PM.agrega('a','b',3.5)
    PM.agrega('a','c',3.2)
    PM.agrega('a','d',1.8)
    PM.agrega('b','a',3.1)
    PM.agrega('b','c',2.2)
    PM.agrega('b','d',2.8)
    PM.agrega('c','a',3.0)
    PM.agrega('c','b',0.2)
    PM.agrega('c','d',1.9)
    PM.agrega('d','a',2.0)
    PM.agrega('d','b',1.2)
    PM.agrega('d','c',1.5)
    #print(PM.verifica())
    print(PM.calculos())


if(__name__=="__main__"):
    main()
