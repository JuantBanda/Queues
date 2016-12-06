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
    N=3000
    print("********inicio de la simulación para córnea*********")
    Ptpa=0
    Ptpb=0
    Pndon=0
    Pnreca=0
    Pnrecb=0
    Precola=0
    Precolb=0

    lam=19.95
    mu=8.57#tasa de pacientes que han recibido un trasplante
    la=.1*lam#tasa de llegadas de receptores con prioridad alta
    lb=.9*lam#tasa de llegadas de receptores con prioridad baja
    da=exponencial(la)
    db=exponencial(lb)
    ds=exponencial(mu)
    for k in range(N):
        TT=365# días
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

        lldon=list()
        t=0
        while(t<TT):
            ts=ds.genexp()
            lldon.append(t+ts)
            t+=ts

        ndon=len(lldon)-1
        nreca=len(llpa)-1
        nrecb=len(llpb)-1
        tea=0
        teb=0
        trasa=0
        trasb=0
        band=0
        trasa=0
        trasb
        while(lldon):
            y=lldon.pop(0)
            if(llpa and y>llpa[0]):
                xa=llpa.pop(0)
                tea+=y-xa
                trasa+=1
            elif(llpb and y>llpb[0]):
                xb=llpb.pop(0)
                teb+=y-xb
                trasb+=1
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
        if(trasa==0):
            trasa=1
        tpa=tea/trasa
        tpb=teb/trasb
        recola=len(llpa)
        recolb=len(llpb)

        Ptpa+=tpa
        Ptpb+=tpb
        Pndon+=ndon
        Pnreca+=nreca
        Pnrecb+=nrecb
        Precola+=recola
        Precolb+=recolb

    print("Totales: donadores %.2f, receptores prioridad alta %.2f, receptores prioridad baja  %.2f"%(Pndon/N,Pnreca/N,Pnrecb/N))
    print("Tiempos de espera: receptores prioridad alta %.2f, receptores prioridad baja %.2f" %(Ptpa/N, Ptpb/N))
    print("Receptores en cola: prioridad alta %.2f, prioridad baja %.2f" %(Precola/N, Precolb/N))

    print("********inicio de la simulación para riñón*********")
    Ptpa=0
    Ptpb=0
    Pndon=0
    Pnreca=0
    Pnrecb=0
    Precola=0
    Precolb=0

    lam=32.05
    mu=7.46#tasa de pacientes que han recibido un trasplante
    la=.1*lam#tasa de llegadas de receptores con prioridad alta
    lb=.9*lam#tasa de llegadas de receptores con prioridad baja
    da=exponencial(la)
    db=exponencial(lb)
    ds=exponencial(mu)
    for k in range(N):
        TT=365# días
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

        lldon=list()
        t=0
        while(t<TT):
            ts=ds.genexp()
            lldon.append(t+ts)
            t+=ts

        ndon=len(lldon)-1
        nreca=len(llpa)-1
        nrecb=len(llpb)-1
        tea=0
        teb=0
        trasa=0
        trasb=0
        band=0
        trasa=0
        trasb
        while(lldon):
            y=lldon.pop(0)
            if(llpa and y>llpa[0]):
                xa=llpa.pop(0)
                tea+=y-xa
                trasa+=1
            elif(llpb and y>llpb[0]):
                xb=llpb.pop(0)
                teb+=y-xb
                trasb+=1
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
        if(trasa==0):
            trasa=1
        tpa=tea/trasa
        tpb=teb/trasb
        recola=len(llpa)
        recolb=len(llpb)

        Ptpa+=tpa
        Ptpb+=tpb
        Pndon+=ndon
        Pnreca+=nreca
        Pnrecb+=nrecb
        Precola+=recola
        Precolb+=recolb

    print("Totales: donadores %.2f, receptores prioridad alta %.2f, receptores prioridad baja  %.2f"%(Pndon/N,Pnreca/N,Pnrecb/N))
    print("Tiempos de espera: receptores prioridad alta %.2f, receptores prioridad baja %.2f" %(Ptpa/N, Ptpb/N))
    print("Receptores en cola: prioridad alta %.2f, prioridad baja %.2f" %(Precola/N, Precolb/N))

    print("********inicio de la simulación para hígado*********")
    Ptpa=0
    Ptpb=0
    Pndon=0
    Pnreca=0
    Pnrecb=0
    Precola=0
    Precolb=0

    lam=1.01
    mu=0.35#tasa de pacientes que han recibido un trasplante
    la=.1*lam#tasa de llegadas de receptores con prioridad alta
    lb=.9*lam#tasa de llegadas de receptores con prioridad baja
    da=exponencial(la)
    db=exponencial(lb)
    ds=exponencial(mu)
    for k in range(N):
        TT=365# días
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

        lldon=list()
        t=0
        while(t<TT):
            ts=ds.genexp()
            lldon.append(t+ts)
            t+=ts

        ndon=len(lldon)-1
        nreca=len(llpa)-1
        nrecb=len(llpb)-1
        tea=0
        teb=0
        trasa=0
        trasb=0
        band=0
        trasa=0
        trasb
        while(lldon):
            y=lldon.pop(0)
            if(llpa and y>llpa[0]):
                xa=llpa.pop(0)
                tea+=y-xa
                trasa+=1
            elif(llpb and y>llpb[0]):
                xb=llpb.pop(0)
                teb+=y-xb
                trasb+=1
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

        if(trasa==0):
            trasa=1
        tpa=tea/trasa
        tpb=teb/trasb
        recola=len(llpa)
        recolb=len(llpb)

        Ptpa+=tpa
        Ptpb+=tpb
        Pndon+=ndon
        Pnreca+=nreca
        Pnrecb+=nrecb
        Precola+=recola
        Precolb+=recolb

    print("Totales: donadores %.2f, receptores prioridad alta %.2f, receptores prioridad baja  %.2f"%(Pndon/N,Pnreca/N,Pnrecb/N))
    print("Tiempos de espera: receptores prioridad alta %.2f, receptores prioridad baja %.2f" %(Ptpa/N, Ptpb/N))
    print("Receptores en cola: prioridad alta %.2f, prioridad baja %.2f" %(Precola/N, Precolb/N))

    print("********inicio de la simulación para corazón*********")
    Ptpa=0
    Ptpb=0
    Pndon=0
    Pnreca=0
    Pnrecb=0
    Precola=0
    Precolb=0

    lam=0.12
    mu=0.11#tasa de pacientes que han recibido un trasplante
    la=.1*lam#tasa de llegadas de receptores con prioridad alta
    lb=.9*lam#tasa de llegadas de receptores con prioridad baja
    da=exponencial(la)
    db=exponencial(lb)
    ds=exponencial(mu)
    for k in range(N):
        TT=365# días
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

        lldon=list()
        t=0
        while(t<TT):
            ts=ds.genexp()
            lldon.append(t+ts)
            t+=ts

        ndon=len(lldon)-1
        nreca=len(llpa)-1
        nrecb=len(llpb)-1
        tea=0
        teb=0
        trasa=0
        trasb=0
        band=0
        trasa=0
        trasb
        while(lldon):
            y=lldon.pop(0)
            if(llpa and y>llpa[0]):
                xa=llpa.pop(0)
                tea+=y-xa
                trasa+=1
            elif(llpb and y>llpb[0]):
                xb=llpb.pop(0)
                teb+=y-xb
                trasb+=1
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
        if(trasa==0):
            trasa=1
        tpa=tea/trasa
        tpb=teb/trasb
        recola=len(llpa)
        recolb=len(llpb)

        Ptpa+=tpa
        Ptpb+=tpb
        Pndon+=ndon
        Pnreca+=nreca
        Pnrecb+=nrecb
        Precola+=recola
        Precolb+=recolb

    print("Totales: donadores %.2f, receptores prioridad alta %.2f, receptores prioridad baja  %.2f"%(Pndon/N,Pnreca/N,Pnrecb/N))
    print("Tiempos de espera: receptores prioridad alta %.2f, receptores prioridad baja %.2f" %(Ptpa/N, Ptpb/N))
    print("Receptores en cola: prioridad alta %.2f, prioridad baja %.2f" %(Precola/N, Precolb/N))

if(__name__=="__main__"):
    main()
