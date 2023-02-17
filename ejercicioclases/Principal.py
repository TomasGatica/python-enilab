from stringprep import in_table_a1
from Asignatura import *
a=asignatura(0,0,0,0)
lista_asignaturas=[]
for i in range(2):
    a.ingreso(lista_asignaturas)
for i in lista_asignaturas:
    print("\tdatos asignatura")
    print("\t================")
    print("\t\tcodigo",i.codigo,"nombre",i.nombre,"horas",i.horas)
    print("\t\tlista de profesores")
    print("\t\t===================")
    for x in i.lista_profesores:
        print("\t\t\trut",x.rut,"nombre",x.nombre,"profesion",x.profesion)
