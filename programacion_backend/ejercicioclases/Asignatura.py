class asignatura:
    codigo=""
    nombre=""
    horas=0
    lista_profesores=[]
    def __init__(self,codigo,nombre,horas,lista_profesores):
        self.codigo=codigo
        self.nombre=nombre
        self.horas=horas
        self.lista_profesores=lista_profesores
        pass

    def ingreso(self,lst_asig):
        codigo=input("ingrese el codigo de la asignatura : ")
        nombre=input("ingrese nombre asignatura : ")
        while True:
            try:
                horas=int(input("ingrese horas de la asignatura : "))
                break
            except ValueError:
                print("debe ingresar un valor numerico, vuelva a intentarlo")
        lst_profes=[]
        while True:
            rut=input("ingrese rut : ")
            nom=input("ingrese nombre : ")
            profesion=input("ingrese profesion : ")
            p=profesor(rut,nom,profesion)
            lst_profes.append(p)
            resp=input("ingresar otro profesor si/no : ")
            if resp=="no":
                break
       
        asig=asignatura(codigo,nombre,horas,lst_profes)
        lst_asig.append(asig)
        pass


class profesor:
    rut=""
    nombre=""
    profesion=""
    #lista_asignaturas=[]

    def __init__(self,rut,nombre,profesion):
        self.rut=rut
        self.nombre=nombre
        self.profesion=profesion
        pass