#! python3
#letrat=["A","As","B","C","Cs","D","Ds","E","F","Fs","G","Gs"]
#freqt=[220,233,247,262,277,293,311,329,349,369,391,415]
Quintas= ["F","C","G","D","A","E","B","F#","C#","G#","D#","A#"]
Frecuencias=[349,262,391,293,220,329,311,369,277,293,391,329,233]
unota=""
indexNota=[]
i=q=j=0
freq=0


class Nota:
    def __init__(self):
        self.nota=input("Ingrese la nota tónica: ")
        self.modo=input("Introduzca el modo: ")
        self.p1cdq=0
        self.p2cdq=0
    def ObtenerNota(self):
        i=0
        for x in Quintas:
            if x != self.nota:
                i+=1
                continue
            else:
                posiquinta=i
                self.posiquinta=posiquinta
                indexNota.append(x)
                print("encontrada, es")
                freq=Frecuencias[i]
                self.freq=freq
                print(self.freq)
                indexNota.append(i)

                break
        return print(x)
    def Obtenerpenta(self):
        j=1
        self.ordenq=int(input("Pulse 0 para no ordenar la cifra : "))
        self.penta=[]
        self.penta.append(self.freq)
        while j<5:
            if (1.5**j*self.freq)<440:
                self.penta.append(1.5**j*self.freq)
                #print(sorted(self.penta))
                j+=1
                continue
            elif (1.5**j*self.freq)>3519:
                self.penta.append(1.5**j*self.freq/16)
                #print(sorted(self.penta))
                j+=1
                continue
            elif (1.5**j*self.freq)>1759:
                self.penta.append(1.5**j*self.freq/8)
                #print(sorted(self.penta))
                j+=1
                continue
            elif (1.5**j*self.freq)>879:
                self.penta.append(1.5**j*self.freq/4)
                #print(sorted(self.penta))
                print(j)
                j+=1
                continue
            else:
                self.penta.append(1.5**j*self.freq/2)
                #print(sorted(self.penta))
                j+=1
                continue
        return self
        #freq2k(self)
        #self.tonohz=self.penta[0]
        print(list(self.penta))
        #print(list(self.cifra))

    def funciontonal(self):
        self.tonohz=int(input("Ingrese el tono: "))
        self.intervalo=int(input("Ingrese el intervalo: "))
        #self.tonohz=[]
        #if self.tonohz==0:
            #self.tonohz=input("Ingrese el tono: ")
        tonoTeorico=self.tonohz*2**(self.intervalo/12)
        return tonoTeorico


    def freq2ks(self):
        self.cifra=[]
        for hertz in sorted(self.penta):
            if hertz<225:
                self.cifra.append("A")
                continue
            elif hertz<240:
                self.cifra.append("A#")
                continue
            elif hertz<255:
                self.cifra.append("B")
                continue
            elif hertz<270:
                self.cifra.append("C")
                continue
            elif hertz<285:
                self.cifra.append("C#")
                continue
            elif hertz<305:
                self.cifra.append("D")
                continue
            elif hertz<320:
                self.cifra.append("D#")
                continue
            elif hertz<340:
                self.cifra.append("E")
                continue
            elif hertz<360:
                self.cifra.append("F")
                continue
            elif hertz<380:
                self.cifra.append("F#")
                continue
            elif hertz<405:
                self.cifra.append("G")
                continue
            elif hertz<425:
                self.cifra.append("G#")
                continue
        print("La tónica es "+self.nota)
        print("Las frecuencias ")
        print(list(self.penta))
        print("La cifra de su pentatónica ordenada ")
        print(list(self.cifra))
        return self

    def freq2kus(self):
        self.cifra=[]
        for hertz in self.penta:
            if hertz<225:
                self.cifra.append("A")
                continue
            elif hertz<240:
                self.cifra.append("A#")
                continue
            elif hertz<255:
                self.cifra.append("B")
                continue
            elif hertz<270:
                self.cifra.append("C")
                continue
            elif hertz<285:
                self.cifra.append("C#")
                continue
            elif hertz<305:
                self.cifra.append("D")
                continue
            elif hertz<320:
                self.cifra.append("D#")
                continue
            elif hertz<340:
                self.cifra.append("E")
                continue
            elif hertz<360:
                self.cifra.append("F")
                continue
            elif hertz<380:
                self.cifra.append("F#")
                continue
            elif hertz<405:
                self.cifra.append("G")
                continue
            elif hertz<425:
                self.cifra.append("G#")
                continue
        print("La tónica es "+self.nota)
        print("Las frecuencias ")
        print(list(self.penta))
        print("La cifra de su pentatónica natural")
        print(list(self.cifra))
        return self.cifra

    def circuloquintas(self):
        self.p1cdq=int(input("Pulse 0 para ver la posicion de tu tono : "))
        if self.p1cdq==0:
            print(self.posiquinta)
        self.p2cdq=int(input("Pulse 0 para ver el orden de quintas : "))
        if self.p2cdq==0:
            print(list(Quintas))
        return(self)

    def modoJonico(self):
        if self.posiquinta==0:
            print("La escala jónica de Fa   F  G  A  C  Bb  D  E")
        else:
            print("La escala jónica de "+self.nota)
            self.Jonico=[]
            self.Jonico.append(Quintas[(self.posiquinta-1)])
            self.cifra.append(Quintas[(self.posiquinta+5)])
            [*self.Jonico,*self.cifra]
            print(list([*self.Jonico,*self.cifra]))

nota1=Nota()

nota1.ObtenerNota()
nota1.Obtenerpenta()
##if nota1.ordenq!= 0:
    ##nota1.freq2ks()
##else:
    ##nota1.freq2kus()
nota1.freq2kus()
nota1.funciontonal()
nota1.modoJonico()
nota1.circuloquintas()

#Paso2=Escala(tnota,tmodo)
