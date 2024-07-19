class Alumnos:
    """ Representa a una entidad alumno """
    
    def __init__(self, nombre, nota1, nota2, nota3):
        """ Método de inicialización de un alumno """
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcular_promedio(self, nota1, nota2, nota3):
        promedio_final = (nota1+nota2+nota3)/3
        return promedio_final
        
    def situacion_final(promedio_final):
        if promedio_final >= 4:
            situacion_alumno = "Aprobado"
        else: 
            situacion_alumno = "Reprobado"
        return situacion_alumno


