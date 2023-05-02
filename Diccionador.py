#Este script recibe una lista y la convierte un diccionario donde cada seccion de cada materia esta separado
from datetime import datetime
from datetime import date
from Horarios import DiaSem



def Diccionador(ListIn):
    DictOut={}
    Nume=0
    for i in ListIn:
        txt= ListIn[Nume]
        #Esta seccion detecta las subsecciones de cada materia para delimitarlas en strings en variables separadas, bucando el texto posterior donde termina la variable. 
        Fecha= txt[0:txt.find("Materia:")].strip()
        Mate=txt[txt.find("Materia:"):txt.find("Tema:")]
        Tema=txt[txt.find("Tema:"):txt.find("Actividades:")]
        Actividades=txt[txt.find("Actividades:"):txt.find("Evaluación:")]
        Evaluacion= txt[txt.find("Evaluación:"):txt.find("Observaciones:")]
        Observaciones= txt[txt.find("Observaciones:"):txt.find("Enlaces:")]
        Enlaces=txt[txt.find("Enlaces:"):]

        #La seccion "Materia" incluye el nombre del Maestr@; asi que la subdivido para extraerlo Aparte
        Mat=Mate.split("[")
        Materia=Mat[0].strip()
        Doce=Mat[1]
        Docente="Docente:"+Doce[0:Doce.find(" - ")]

        #determinar Dia de la Semana:
        f=datetime.strptime(Fecha, 'Fecha:  %d/%m/%Y').date()
        DS= DiaSem(f.weekday())
        Dia= "Dia: " + str(DS)


        Lista=[Dia,Fecha, Materia, Docente, Tema, Actividades, Evaluacion, Observaciones, Enlaces]
        #Una vez que estan todas las variables separadas, voy a unirlas en un Diccionario, haciendoles un split al nombre de la seccion para cargar la primera parte como key y la segunda parte como contenido.
        #El diccionario donde irán las variables será un subdiccionario que se agregará a un diccionario del total de materias
        SubDict={}
        Num=0
        for i in Lista:
            txt=Lista[Num]
            Nom=txt.split(":",1)
            SubDict[Nom[0]] = Nom[1]
            Num=Num+1
        DictOut[Nume]=SubDict
        Nume=Nume+1

    print("Clases Extraidas", Nume)
    return DictOut
