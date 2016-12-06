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
    N=500
    print("********Cola con 3 prioridades*********")
    Ptpa=0
    Ptpb=0
    Ptpc=0
    Pns=0
    Pnreca=0
    Pnrecb=0
    Pnrecc=0
    Precola=0
    Precolb=0
    Precolc=0


    mu=10#tasa de servicio
    la=3#tasa de llegadas tipo A
    lb=7#tasa de llegadas tipo B
    lc=8#tasa de llegadas tipo B
    da=exponencial(la)
    db=exponencial(lb)
    dc=exponencial(lc)
    ds=exponencial(mu)
    for k in range(N):
        TT=100
        T=0
        t=0
        llpa=list()
        while(t<TT):
            ta=da.genexp()
            llpa.append(t+ta)
            t+=ta
        t=0
        llpb=list()
        while(t<TT):
            tb=db.genexp()
            llpb.append(t+tb)
            t+=tb

        t=0
        llpc=list()
        while(t<TT):
            tc=dc.genexp()
            llpc.append(t+tc)
            t+=tc

        lls=list()
        t=0
        while(t<TT):
            ts=ds.genexp()
            lls.append(t+ts)
            t+=ts

        ns=len(lls)-1
        nreca=len(llpa)-1
        nrecb=len(llpb)-1
        nrecc=len(llpc)-1
        tea=0
        teb=0
        tec=0
        trasa=0
        trasb=0
        trasc=0
        band=0
        while(lls):
            y=lls.pop(0)
            if(llpa and y>llpa[0]):
                xa=llpa.pop(0)
                tea+=y-xa
                trasa+=1
            elif(llpb and y>llpb[0]):
                xb=llpb.pop(0)
                teb+=y-xb
                trasb+=1
            elif(llpc and y>llpc[0]):
                xc=llpc.pop(0)
                tec+=y-xc
                trasc+=1

            else:
                band=1
            if(band==1):
                band=0
                if(llpa and y>llpa[0]):
                    xa=llpa.pop(0)
                    trasa+=1
                elif(llpb and y>llpb[0]):
                    xb=llpb.pop(0)
                    trasb+=1
                elif(llpc and y>llpc[0]):
                    xc=llpc.pop(0)
                    trasc+=1
        if(trasa==0):
            trasa=1
        if(trasb==0):
            trasb=1
        if(trasc==0):
            trasc=1
        tpa=tea/trasa
        tpb=teb/trasb
        tpc=tec/trasc
        recola=len(llpa)
        recolb=len(llpb)
        recolc=len(llpc)

        Ptpa+=tpa
        Ptpb+=tpb
        Ptpc+=tpc
        Pns+=ns
        Pnreca+=nreca
        Pnrecb+=nrecb
        Pnrecc+=nrecc
        Precola+=recola
        Precolb+=recolb
        Precolc+=recolc

    print("Totales: Salidas %.2f, entradas tipo A %.2f, entradas tipo B  %.2f, entradas tipo C  %.2f"%(Pns/N,Pnreca/N,Pnrecb/N, Pnrecc/N))
    print("Tiempos de espera: tipo A %.2f, tipo B %.2f, tipo C %.2f" %(Ptpa/N, Ptpb/N, Ptpc/N))
    print("Clientes en cola: tipo A %.2f, tipo B %.2f,  tipo C %.2f" %(Precola/N, Precolb/N, Precolc/N))


if(__name__=="__main__"):
    main()
