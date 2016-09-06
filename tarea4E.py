from collections import defaultdict
from random import random
class cadenasMarkov(dict):
    def __init__(self):
        dict.__init__(self)
        self.N=set()
        self.visitas=dict()
        self.res=dict()
        #self.vecinos=dict()

    def agrega(self,x,y,p):
        self.N.add(x)
        self.N.add(y)
        self[x,y]=p

    def verifica(self):
        for i in self.N:
            sum=0
            for j in self.N:
                if(i,j) in self:
                    sum+=self[i,j]
            if(sum<1):
                self[i,i]=1-sum
            else:
                print("--Error--")
        #return self

    #ei estado inicial
    def trans(self, ei, pasos):
        self.verifica()
        #print(self)
        for i in  self.N:
            self.visitas[i]=0
            self.res[i]=0
        #print(self.visitas)
        for i in range(pasos):
            na=random()
            #print(na)
            sp=0 #suma de probabilidades
            for j in self.N:
                if(ei,j) in self and  sp<na:
            #        print(ei,j)
                    sp+=self[ei,j]
                    self.visitas[j]+=1
                    pos=j
            #print(sp)
            ei=pos
        for i in self.N:
            self.res[i]=self.visitas[i]/pasos
        return self.res

def main():

    CM=cadenasMarkov()
    CM.agrega('a','b',2/9)
    CM.agrega('a','c',1/9)
    CM.agrega('b','a',6/9)
    CM.agrega('b','c',1/9)
    CM.agrega('c','a',0)
    CM.agrega('c','b',6/9)
    print(CM.trans('a',10000))
    #print(CM.verifica())
    #sump=dict()
    #aux=dict()
    #edos=CM.N
    #print(edos)
    #for i in edos:
    #    sump[i]=0

    #Rep=5
    #for i in range(Rep):
    #for j in edos:
        #sump[j]+=CM.trans('a',100)[j]
    #    print(CM.trans('a',5)[j])
    #print(sump)

if(__name__=="__main__"):
    main()
