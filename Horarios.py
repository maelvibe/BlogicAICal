from datetime import date
from datetime import time
from datetime import datetime


#vemos el Horario: un diccionario para bloque horario, y un diccionario de materias por dia por bloque

Horarios={"1":time(7,50,00), "2": time(8,35,00), "3": time(9,30,00),"4":time(10,10,00), "5": time(10,50,00), "6": time(11,50,00),"7":time(12,30,00), "8": time(13,10,00)}

Lunes={"1":"Consejería","2":"Folklore","3":"Matemática","4":"Matemática","5":"Inglés (Grammar, Reading, Speech)","6":"Inglés (Grammar, Reading, Speech)","7":"Ciencias Naturales","8":"Religión, Moral y Valores"}
Martes={"1": "Español", "2": "Español", "3": "Matemática", "4": "Matemática", "5": "Ciencias Naturales", "6": "Inglés (Grammar, Reading, Speech)", "7": "Inglés (Grammar, Reading, Speech)", "8": "Expresiones Artísticas"}
Miercoles={"1": "Música", "2": "Informática", "3": "Religión, Moral y Valores", "4": "Inglés (Grammar, Reading, Speech)", "5": "Inglés (Grammar, Reading, Speech)","6": "Familia y Desarrollo Comunitario", "7": "Ciencias Naturales", "8": "Ciencias Sociales"}
Jueves={"1": "Science", "2": "Science", "3": "Ciencias Sociales", "4": "Español", "5": "Español", "6": "Educación Física", "7": "Educación Física", "8": "Expresiones Artísticas"}
Viernes= {"1": "Inglés (Grammar, Reading, Speech)","2": "Inglés (Grammar, Reading, Speech)","3": "Español","4": "Español","5":"Familia y Desarrollo Comunitario","6": "Ciencias Sociales","7": "Matemática","8": "Matemática"}

DiaMaterias= {"0":Lunes,"1":Martes,"2":Miercoles,"3":Jueves,"4":Viernes}



#Esta funcion recibe una materia y un dia, y devuelve la hora de inicio. Recorre el diccionario DIaMaerias para encontrar el dia, y luego recorre el subdiccionario con el nombre de la materia para encontrar el bloque horario. Finalmente extrae las horas de inicio de el diccionario de horarios y si hay mas de una elige la mas temprana.
def Begins(Materia, Dia):
    beg=0
    diaa=DiaMaterias[str(Dia)]
    horas=[]
    
    for k,v in diaa.items():
        if v==Materia:
            h=Horarios[k]
            horas.append(h)

    if horas:
        beg=min(horas)
        end=max(horas)
    
    return beg,end





