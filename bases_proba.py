class espacio_muestral(dict):
    def __init__(self):
        self.elementos=dict()

    def agregar_elemento(self, elem):
        self.elementos.append(elem)


class evento(dict):
    def __init__(self):
        self.elemA=set()

    def agregar_elemento(self, elem):
        self.elementos.append(elem)
        #for key, value in self.iteritems():
        #    elemA.add(value)
    def union(self, B):
        elemA = set()
        elemB = set()
        a=dict()
        un=dict()
        for key, value in self.items():
            elemA.add(value)
        for key, value in B.items():
            elemB.add(value)
        a=list(elemA|elemB)
        k=1
        for i in a:
            un[k]=i
            k+=1
        return un

    def interseccion(self, B):
        elemA = set()
        elemB = set()
        a=dict()
        int=dict()
        for key, value in self.items():
            elemA.add(value)
        for key, value in B.items():
            elemB.add(value)
        a=list(elemA&elemB)
        k=1
        for i in a:
            int[k]=i
            k+=1
        return int

EM=espacio_muestral()
EM[1]=0.3
EM[2]=0.2
EM[3]=0.5
EM[4]=0.1
EM[5]=0.5
EM[6]=0.4
EM[7]=0.9

A=evento()
A[1]=EM[2]
A[2]=EM[3]
A[3]=EM[4]

B=evento()
B[1]=EM[2]
B[2]=EM[7]



print("Espacio muestral",EM)
print("Evento A:",A)
print("Evento B:",B)
print("La unión de A y B es:", A.union(B))
print("La intersección de A y B es:", A.interseccion(B))
