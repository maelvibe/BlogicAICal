#Este script recibe una lista y la convierte un diccionario donde cada seccion de cada materia esta separado
def Diccionador(ListIn):
    DictOut={}
    Nume=0
    for i in ListIn:
        txt= ListIn[Nume]
        #Esta seccion detecta las subsecciones de cada materia para delimitarlas en strings en variables separadas, bucando el texto posterior donde termina la variable. 
        sep1=txt.find("Materia:")
        FechaA=txt[0:sep1]
        Fecha= FechaA.strip()
        sep2=txt.find("Tema:")
        Mate=txt[sep1:sep2]
        sep3=txt.find("Actividades:")
        Tema=txt[sep2:sep3]
        sep4=txt.find("Evaluación:")
        Actividades=txt[sep3:sep4]
        sep5=txt.find("Observaciones:")
        Evaluacion= txt[sep4:sep5]
        sep6=txt.find("Enlaces:")
        Observaciones= txt[sep5:sep6]
        Enlaces=txt[sep6:]

        #La seccion "Materia" incluye el nombre del Maestr@; asi que la subdivido para extraerlo Aparte
        Mat=Mate.split("[")
        Materia=Mat[0]
        Doce=Mat[1]
        sep7=Doce.find(" - ")
        Docente="Docente:"+Doce[0:sep7]

        Lista=[Fecha, Materia, Docente, Tema, Actividades, Evaluacion, Observaciones, Enlaces]
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
