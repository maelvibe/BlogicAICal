
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import re
from Horarios import Begins
from pathlib import Path
import os
import pytz


def Eventar(DictIn):

    cal = "BEGIN:VCALENDAR\nPRODID:-//Google Inc//Google Calendar 70.9054//EN\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:3CIJA\nX-WR-TIMEZONE:America/Panama\nX-WR-CALDESC:Calendario de 3ro C"
    with open('Sq.txt') as f:
        se = f.readlines()
        se1=str(se)[2:-2]
        s=int(se1)
 

    #Recorremos el diccionario:
    for i in DictIn:
        s=s+1
        #Primero Ponemos la fecha en el formato datetime para poder extraer el día de la semana
        #Elimino el whitespace inicial en la fecha: Esto no se hizo en el modulo Diccionador porque por el formato que tiene, era mas facil diccionarlo como estaba. Con el diccionario ya creado, se puede extraer más facilmente ese espacio en blanco. 
        FechaWS= DictIn[i]["Fecha"]
        StriniFecha= FechaWS[2:]
        DatefinFecha= datetime.strptime(StriniFecha, '%d/%m/%Y').date()
        
        if i==0:
            mindate=DatefinFecha
        elif i>=1 and DatefinFecha<=mindate:
            mindate=DatefinFecha


        #Extraemos el dia de la semana
        
        DiaSem= DatefinFecha.weekday()

        #Determinamos la hora de Inicio de acuerdo a la materia y el día

        Materia= DictIn[i]["Materia"].strip()

        #ADAPTACIONES POR EXPRESIONES ARTISTICAS - Esta materia puede ser arte, folklore o música, dependiendo del día. Por lo tanto, estas lineas le cambian el nombre según el día
        if Materia == "Expresiones Artísticas" and DiaSem==0 : Materia="Folklore"
        elif Materia == "Expresiones Artísticas" and DiaSem==2 : Materia="Música"

        Ini, Fini= Begins(Materia, DiaSem)
        Inicio= datetime.combine(DatefinFecha, Ini)
        IniICS=Inicio.strftime('%Y%m%d'+'T'+'%H%M%S')


        Finala= datetime.combine(DatefinFecha, Fini)
        Final= Finala + timedelta(minutes=40)
        FiniICS=Final.strftime('%Y%m%d'+'T'+'%H%M%S')


        ahorita=datetime.now()
        ahora= ahorita.strftime('%Y%m%d'+'T'+'%H%M%S'+'Z')

        #La descripcion sale de BLogic con literales como string. Al adosarlos a otros string en el ICS, lee los literales y los caracteres especiales y daña el archivo. El siguiente codigo tiene como finalidad buscar esos literales y representarlos literalmente. 
        

        tem=str(DictIn[i]["Tema"])
        acti= str(DictIn[i]["Actividades"])
        temacti=tem+acti
        rtemacti=[temacti]

        #Substrings para el armado del string principal. 
        summary= '\nSUMMARY:'+ Materia 
        dtstamp= '\nDTSTAMP:'+ ahora 
        UID = '\nUID:'+ str(s+1000001)
        seq= '\nSEQUENCE:'+str(s)
        created = '\nCREATED:20230101T000000Z'
        description= '\nDESCRIPTION:'+ str(rtemacti)[1:-1] +'\n'
        dtend= '\nDTEND;TZID=America/Panama:'+ FiniICS
        dtstart='\nDTSTART;TZID=America/Panama:' + IniICS
        name= '\nNAME:'+ Materia 
        loc= r"LOCATION:Instituto Justo Arosemena\, Brisas del Golf\, San Miguelito\, Panamá"


        # Agregar Elementos
        event='\nBEGIN:VEVENT'+ summary + dtstamp + UID + seq +created + description+ loc + dtend+ dtstart + name
        o='\nTRANSPARENCY:OPAQUE\nEND:VEVENT'
        evento=event + o
        cal= cal + evento

    cal=cal+ '\nEND:VCALENDAR'
    maxdate=mindate+timedelta(days=4)
    

    path = r'C:/Users/DELL/Desktop/Reader/Calendario'
    file_name = 'Agenda-'+ str(mindate)+" al "+ str(maxdate) +".ics"
    with open(os.path.join(path, file_name), 'w',encoding='utf-8') as fp:
        fp.write(cal)

    return 