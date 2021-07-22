#! python3
import json
#letratupla=["A","As","B","C","Cs","D","Ds","E","F","Fs","G","Gs"]
#freqtupla=[220,233,247,262,277,293,311,329,349,369,391,415]
Quintas= ["F","C","G","D","A","E","B","F#","C#","G#","D#","A#"]
Frecuencias=[349,262,391,293,220,329,311,369,277,293,415,329,233]
unota=""
indexNota=[]
i=q=j=0
freq=0
modif=""


class Nota:
    def __init__(self):
        self.nota=input("Ingrese la nota tónica: ")
        self.modo=input("Introduzca el modo: ")
        #self.modo=[]
    #    self.modo.append(self.modoinput)
        self.p1cdq="--"
        self.p2cdq="--"
        self.A="--"
        self.As="--"
        self.B="--"
        self.C="--"
        self.Cs="--"
        self.D="--"
        self.Ds="--"
        self.E="--"
        self.F="--"
        self.Fs="--"
        self.G="--"
        self.Gs="--"
    def freefretb(self):
        self.A="--"
        self.As="--"
        self.B="--"
        self.C="--"
        self.Cs="--"
        self.D="--"
        self.Ds="--"
        self.E="--"
        self.F="--"
        self.Fs="--"
        self.G="--"
        self.Gs="--"
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
        return print(self.modo,x)
    def Obtenerpenta(self):
        j=1
        self.ordenq=int(input("Pulse 0 para no ordenar la cifra : "))
        self.penta=[]
        self.penta.append(self.freq)
        self.escala=[]
        while j<5:
            if (1.5**j*self.freq)<440:
                self.penta.append(1.5**j*self.freq)
                #self.freq.append(1.5**j*self.freq)             // Por si necesito crear una nueva salida desde esta funcion
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
        self.escala=list.copy(self.penta)
    #    self.escala.sort(key = lambda x:self.escala[x]>=self.freq)
    #    self.escala.sort(key = lambda x:self.escala[x]<self.freq,reverse=True)
        print(list(self.escala))
        self.etiqueta="pentatonica"
        return self
        #freq2k(self)
        #self.tonohz=self.penta[0]
        #print(list(self.cifra))

    def freq2ks(self):
        #if modif!="Y":
        #    self.escala=list.copy(self.penta)
        self.cifra=[]
        for hertz in (self.escala):
            if hertz<225:
                self.cifra.append("A ")
                self.A="A "
                continue
            elif hertz<240:
                self.cifra.append("A#")
                self.As="A#"
                continue
            elif hertz<255:
                self.cifra.append("B ")
                self.B="B "
                continue
            elif hertz<270:
                self.cifra.append("C ")
                self.C="C "
                continue
            elif hertz<285:
                self.cifra.append("C#")
                self.Cs="C#"
                continue
            elif hertz<305:
                self.cifra.append("D ")
                self.D="D "
                continue
            elif hertz<320:
                self.cifra.append("D#")
                self.Ds="D#"
                continue
            elif hertz<340:
                self.cifra.append("E ")
                self.E="E "
                continue
            elif hertz<360:
                self.cifra.append("F ")
                self.F="F "
                continue
            elif hertz<380:
                self.cifra.append("F#")
                self.Fs="F#"
                continue
            elif hertz<405:
                self.cifra.append("G ")
                self.G="G "
                continue
            elif hertz<425:
                self.cifra.append("G#")
                self.Gs="G#"
                continue
        print("La tónica es "+self.nota)
        print("Las frecuencias ")
        print(list(self.escala))
        print(f'La cifra de su escala {self.etiqueta} en clave de {self.nota} ')
        print(list(self.cifra))
        return self

    def freq2kus(self):
    #    if modif!="Y":
    #        self.escala=list.copy(self.penta)
        self.cifra=[]
        #self.cifra.clear()
        for hertz in self.escala:
            if hertz<225:
                self.cifra.append("A ")
                self.A="A "
                continue
            elif hertz<240:
                self.cifra.append("A#")
                self.As="A#"
                continue
            elif hertz<255:
                self.cifra.append("B ")
                self.B="B "
                continue
            elif hertz<270:
                self.cifra.append("C ")
                self.C="C "
                continue
            elif hertz<285:
                self.cifra.append("C#")
                self.Cs="C#"
                continue
            elif hertz<305:
                self.cifra.append("D ")
                self.D="D "
                continue
            elif hertz<320:
                self.cifra.append("D#")
                self.Ds="D#"
                continue
            elif hertz<340:
                self.cifra.append("E ")
                self.E="E "
                continue
            elif hertz<360:
                self.cifra.append("F ")
                self.F="F "
                continue
            elif hertz<380:
                self.cifra.append("F#")
                self.Fs="F#"
                continue
            elif hertz<405:
                self.cifra.append("G ")
                self.G="G "
                continue
            elif hertz<425:
                self.cifra.append("G#")
                self.Gs="G#"
            elif hertz<440:
                self.cifra.append("A ")
                self.A="A "
                continue
        print("La tónica es "+self.nota)
        print("Las frecuencias ordenadas ")
        print(list(self.escala))
        print(f'La cifra de su escala {self.etiqueta} en clave de {self.nota} ')
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

    def funciontonal(self):
        self.tonohz=int(input("Ingrese el tono: "))
        self.intervalo=int(input("Ingrese el intervalo: "))
        #self.tonohz=[]
        #if self.tonohz==0:
            #self.tonohz=input("Ingrese el tono: ")
        self.tonoTeorico=self.tonohz*2**(self.intervalo/12)
        return self.tonoTeorico

    def ftonal(self,inter):
        #self.tonohz=[]
        #if self.tonohz==0:
            #self.tonohz=input("Ingrese el tono: ")ç
        self.tonoTeorico=int()
        if (self.freq*2**(inter/12)) <430:
            self.tonoTeorico=int(self.freq*2**(inter/12))
        else:
            self.tonoTeorico=int(self.freq*2**(inter/12))
            self.tonoTeorico=self.tonoTeorico/2
        return self.tonoTeorico

    def Modos(self):
        self.menores=[]
        self.mayores=[]
        for int in self.escala:
            if int < self.freq:
                self.menores.append(int)
            else:
                self.mayores.append(int)
        pass
        self.mayores.sort()
        self.menores.sort(reverse=True)
        for int in self.menores:
            self.mayores.append(int)
        pass
    #    self.nescala=list.copy(self.mayores)

        self.etiqueta=self.modo
        modif="Y"
        if self.modo == 'jonico':
            print("escala mayor reconocida")
            self.intervalo=[5,11]
            for inter in self.intervalo:
                self.ftonal(inter)
                self.mayores.append(self.tonoTeorico)
                print("añadido intervalo de ")
                print(inter)
        if self.modo == 'dorico': #hace falta quitar notas!
            print("modo dorico reconocido")
            self.intervalo=[3,5,10]
            for inter in self.intervalo:
                if inter==5:
                    self.ftonal(inter)
                    self.mayores[2]=self.tonoTeorico
                else:
                    self.ftonal(inter)
                    self.mayores.append(self.tonoTeorico)
        if self.modo == "Lidio":
            print("modo lidio reconocido")
            self.intervalo=[6,11]
            for inter in self.intervalo:
                self.ftonal(inter)
                self.mayores.append(self.tonoTeorico)
        if self.modo == "Mixo":
            print("modo mixolidio reconocido")
            self.intervalo=[5,10]
            for inter in self.intervalo:
                self.ftonal(inter)
                self.mayores.append(self.tonoTeorico)
        if self.modo == 'Eolico':
            print("modo eolico reconocido")
            self.intervalo=[3,5,8,10]
            for inter in self.intervalo:
                if inter==3:
                    self.ftonal(inter)
                    self.mayores[2]=self.tonoTeorico
                elif inter==8:
                    self.ftonal(inter)
                    self.mayores[4]=self.tonoTeorico
                else:
                    self.ftonal(inter)
                    self.mayores.append(self.tonoTeorico)
        print(list(self.mayores))
        self.escala=self.mayores
        return self
    #def modoJonico(self):
    #    if self.posiquinta==0:
        #    print("La escala jónica de Fa   F  G  A  C  Bb  D  E")
        #    self.cifra.append("Bb")
        #    self.Bb="Bb"
        #    self.cifra.append("E")
        #    self.E="E"
    #    else:
        #    print("La escala jónica de "+self.nota)
        #    self.Jonico=[]
        #    self.Jonico.append(Quintas[(self.posiquinta-1)])
        #    self.cifra.append(Quintas[(self.posiquinta+5)])
        #    [*self.Jonico,*self.cifra]
        #    print(list([*self.Jonico,*self.cifra]))
    #    return self
    def imprPaintFret(self):
        print('\n \n')
        print(f'{self.E}|--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}--{self.As}--{self.B}--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}--{self.F}--{self.Fs}---------------|')
        print(f'{self.B}|--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}--{self.As}--{self.B}--{self.C}--{self.Cs}---------------|')
        print(f'{self.G}|--{self.Gs}--{self.A}--{self.As}--{self.B}--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}---------------|')
        print(f'{self.D}|--{self.Ds}--{self.E}--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}--{self.As}--{self.B}--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}---------------|')
        print(f'{self.A}|--{self.As}--{self.B}--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}--{self.As}--{self.B}---------------|')
        print(f'{self.E}|--{self.F}--{self.Fs}--{self.G}--{self.Gs}--{self.A}--{self.As}--{self.B}--{self.C}--{self.Cs}--{self.D}--{self.Ds}--{self.E}--{self.F}--{self.Fs}---------------|')
        print(f'0|   1   x   3   x   5   x   7   x   9   x   x   12   x   x   15  ')

        return print('\n Rock  \n     n \n                 "Roll ')


nota1=Nota()

nota1.ObtenerNota()
nota1.Obtenerpenta()
nota1.freq2kus()
nota1.imprPaintFret()
nota1.freefretb()
nota1.ObtenerNota()
nota1.Obtenerpenta()
nota1.Modos()
nota1.freq2kus()
#nota1.penta.clear()
#nota1.Obtenerpenta()
nota1.imprPaintFret()
nota1.Obtenerpenta()
nota1.Modos()
nota1.freq2ks()
nota1.imprPaintFret()
#if nota1.ordenq!= 0:
#    nota1.freq2ks()
#else:

#print(list(nota1.cifra))
#print(list(nota1.escala))
#nota1.imprPaintFret()
#nota1.freq2kus()
#nota1.funciontonal()
#nota1.modoJonico()
#nota1.circuloquintas()
#nota1.imprPaintFret()
#nota2=Nota(self.nota="A")
#nota2.imprPaintFret()
#nota3=Nota(self.nota="As")
#nota3.imprPaintFret()

#Paso2=Escala(tnota,tmodo)
