#Este escript recibe la ruta del archivo en PDF y devuelve la ruta de un archivo JSon que contiene el contenido del PDF separado por materia. El archivo es creado en este script.
#Arte aparece como una sola materia en Blogic (Expresiones Artisticas) pero puede ser Folklore, Musica o Arte, por lo tanto hay que modificarlo en la seccion indicada en el scrpt de Eventador - Está ahí porque para saber cuál materia es, primero es necesario extraer el día de la semana. 
import json
from Recorrepaginas import* #Esta funcion recorre todas las paginas del PDF y las guarda con su texto íntegro en una lista, por cada media pagina.
from Listador import* #Este script separa materia por materia en strings diferentes dentro de una lista
from Diccionador import* #Este script genera el diccionario para el json
from Eventador import* #VERSION 2: Este script convierte la variable DictPrevio en un evento. 
from pathlib import Path #Permite exraer el filepath del json final


#Aún no sé qué hacer con este JSON ya que cambié el engoque a la creación de un ICS, lo voy a comentar pero no lo voy a borrar. 

def Reader(ARFile):
    #Este script toma un pdf de Active Reports Generado por BLogic de Instituto Justo Arosemena, lo separa por materias, y carga cad materia de la agenda por separado en un json
    print(ARFile)
    ListPorPag=TextoCompleto(ARFile) #se obtiene una lista donde cada página es un item.
    ListPorMat=Listador(ListPorPag) #se obteiene una lista con cada materia separada en string completo
    DictPrevio=Diccionador(ListPorMat) #Envia la lista por materia y recibe un diccionario donde cada seccion de cada materia esta separado
    Evento=Eventar(DictPrevio)#Envia el DictPrevio al Eventador


    #El diccionario previo obtenido se vuelca a un json. Se usa jsondump porque permite mantener las tildes del texto.

    filen='Output\\Agenda.json'
    with open(filen, 'w', encoding="utf-8") as fichero:
        str(DictPrevio).encode('utf-8')
        json.dump(DictPrevio, fichero, indent=4, ensure_ascii=False)
    filena=str(Path.cwd())
    filename= filena+"\\"+filen
    return (filename)




def Caller(file):
    print (Reader(file))
