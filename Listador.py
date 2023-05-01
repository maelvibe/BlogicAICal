#Este script separa materia por materia en strings diferentes dentro de una lista

def Listador(Dict):
    ListOut=[]
    Nume=0
    for i in Dict:
        txt=Dict[Nume]
        splt=txt.split("Fecha (d/m/a):") #Este string es unico en cada materia y indica donde empieza una materia, asi que se usa como separador. 
        Num=0
        for i in splt:
            if splt[Num] != "":
                txt2="Fecha: "+splt[Num]
                ListOut.append(txt2)
            Num=Num+1
        Nume=Nume+1

    print("Ordenando Materias de media pagina:",Nume)    
    return (ListOut)
