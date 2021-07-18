#! python3        #PorHacer:  Sensibilidad, arreglar defectos/artefactos. Convertir en fichero de texto con extension .tex
#AutoLateX Templater - s. anarcoiris@pm.me                    ::::===>>> implementar plantillas para completar una primera vrsión!
import docx
import json
   #Prueba para arreglar el formato de las tildes, etc...
   #sys.setdefaultencoding('utf-8')
import sys
#s.encode('utf-8')

orden={"Número":[],"Título":[],"Texto":[]}
i = 0
n = 0
numT = 0
Title = []
fullText = []


def getText(filename):
    doc = docx.Document(filename)
    #fullText = []
    for para in doc.paragraphs:
        if len(para.text) > 40:   #Filtro de Title/Body      --- introducir parametro de sensibilidad,
            fullText.append("\newline " + para.text)
    return fullText            #return '\n'.join(fullText)

def getTitle(filename):
    doc = docx.Document(filename)
    #Title = []
    for para in doc.paragraphs:
        if len(para.text) < 40 and len(para.text) > 3:  #Filtro de Title
            orden["Título"].append(" \newpage " + " \chapter{" + para.text + "}")
    return orden #    return Title     return '\n'.join(Title)

def nTitle(filename, n):  #aquí empieza la parte experimental
    doc = docx.Document(filename)
    Title = []
    for para in doc.paragraphs:
        if len(para.text) < 40 and len(para.text) > 3:
            Title.append(" \newpage " + " \chapter{" + para.text + "}")
    print(Title)    #print(Title[(numT)])
    return '\n'.join(Title[n])

def textChain(filename,divi):
    claves(divi)
    getTitle(filename)
    i=0         #Se trata de encadenar los textos que pertenezcan al mismo capítulo.
    doc = docx.Document(filename) #Debería añadir el vector formado por los appends anteriores a la lista cuando encuentre un paragraph de entre menos de 25 y mas de 1
    fullText = []
    nText = []
    Separar=""

    for para in doc.paragraphs:
        if len(para.text) < 4:
            #print("detectado renglón, omitiendo")
            continue
        elif len(para.text) > 40: #   if len(para.text) < 25 and len(para.text) > 1:
            fullText.append(' \newline '+para.text)         #    continue
        #    print(fullText)
            i+=1
            continue
        elif i>1:                                  #print(fullText[i]) UN (posible) TITULO!
            #print(fullText)
            x = Separar.join(fullText) #i+=1  ¡¡ Aqui estaría juntando las strings ordenadas en una sola para asociarla a su Titulo correspondiente (EJ Capitulo 1 + párrafos 1,2,3...5)
        #    print(fullText)
            orden["Texto"].append(x) # Aquí quedan ordenados pEj - Parrafos del Capítulo 1, 2, 3...
            fullText.clear()
            monta=dict(zip(Title,nText))
            dict(monta)
            with open('monta.txt', 'w', encoding='utf-8') as fp:
                json.dump(monta, fp, ensure_ascii=False)
            dict(orden)
            with open(filename+'.tex', 'w', encoding='utf-8') as fp:
                json.dump(orden, fp, ensure_ascii=False)
            #print(dict(monta))
            #print([i for i in zip(Title,nText)])
            #n+=1 sin uso - nTitle[n!]
            #print(nText)
            continue
        else:
            i+=1
            continue

        return print(tuple(monta))
    #print(tuple(monta))
    #print([i for i in zip(Title[n],nText)])
    return monta
#    monta = {}
#    f = open("dict.txt","w")             TERRIBLES PRUEBAS
#    f.write( str(dict) )
#    f.close()
#    orden["Título"].append()         ^^ ^^      Esta idea promete. ^^ ^^
    #orden.keys()=Title
    #orden[Title]


def dumpJson(outname,filename,divi):
    textChain(filename,divi)
    monta=dict(zip(Title,nText))
    dict(monta)
    with open('monta.txt', 'w', encoding='utf-8') as fp:
        json.dump(monta, fp, ensure_ascii=False)
    dict(orden)
    with open(filename+'.tex', 'w', encoding='utf-8') as fp:
        json.dump(orden, fp, ensure_ascii=False)

    #print(monta)
            # else:    #if len(para.text) < 25 and len(para.text) > 1:
                    #    break
    #fullText.append("'newpage " + nText)
    #return '\n'.join(fullText)

def getTupla(filename):
    getTitle(filename)
    getText(filename)
    zipped=zip(Title,fullText)
    tuple(zipped)
    print(tuple(zipped))
    #print(list(zip(Title,fullText)))
    print([i for i in zip(Title,fullText)])
    return zipped

def troceo(filename,n):
    getTitle(filename)
    getText(filename)
    return print(list(zip(*[iter(Title)]*n)))


def claves(divi):
    count=0
    while count < divi:
        orden["Número"].append(count)
        count+=1
    print(orden["Número"])
    return orden["Número"]
