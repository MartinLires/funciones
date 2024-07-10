class  Ropa :
    def __init__ (self ,l = 8 ,m= 5  ) :
        self.l =  l
        self.m = m
        
        
        
class Remera (Ropa) :
    
     ...
     
     
class Chomba (Remera) :
    pass


talle = Remera (7,1)

 






def calcular_promedio_alumnos(total_alumnos, total_notas):
    
    promedio = total_notas / total_alumnos
    return promedio

total_alumnos = 50
total_notas = 455

promedio_notas = calcular_promedio_alumnos(total_alumnos, total_notas)

print (promedio_notas)

