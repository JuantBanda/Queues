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
    lam=1.4#tasa de llegada
    mu=1.5#tasa de servicio
    DE=exponencial(lam)
    DS=exponencial(mu)

    #M/M/3/3/10
    TT=100
    T=0
    s=3#número de servidores y máximo de lugares en cola
    N= 10 #clientes en el sistema
    oc=0

    intentos=0
    rechazos=0
    t_intento=list()
    t_atencion=list()

    for i in range(N):
        t_intento.append(DE.genexp())
    t_intento.sort()

    while(T<TT):
        if (len(t_atencion)==0 or(len(t_intento)>0 and t_intento[0]<t_atencion[0])):
            T=t_intento.pop(0)
            intentos+=1
            if(oc<s):
                t_atencion.append(T+DS.genexp())
                t_atencion.sort()
                oc+=1
            else:
                t_intento.append(T+DE.genexp())
                t_intento.sort()
                rechazos+=1
        else:
            T=t_atencion.pop(0)
            oc-=1
            t_intento.append(T+DE.genexp())
            t_intento.sort()


    print("Intentos>>",intentos,"Rechazos>>",rechazos, "Tiempo>>", T)


if(__name__=="__main__"):
    main()
