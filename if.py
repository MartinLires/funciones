
    
    
def mostrar_palabra () :
     j1 = 'perro,'
     j2= '   gato'
     return j1 + j1 +j2
    
animales = mostrar_palabra ()
lsdf =mostrar_palabra ()
print (animales)
print (lsdf)



if True:
    print('hola')
    
print (mostrar_palabra())


class  Persona :
    def __init__(self,edad ,calzado) :
        self.edad = edad
        self.calzado = calzado
        
romario = Persona (81 , 28)
ronaldinho = Persona (12,25)
print ( ronaldinho.calzado)


def calcular_promedio(cantidad_alumnos, suma_notas):
    if cantidad_alumnos > 0:
        promedio = suma_notas / cantidad_alumnos
        return promedio
    else:
        return "La cantidad de alumnos debe ser mayor que cero."

# Ejemplo con los datos proporcionados (50 alumnos, suma de notas 157)
cantidad_alumnos = 50
suma_notas = 157

promedio_notas = calcular_promedio(cantidad_alumnos, suma_notas)
print(f"El promedio de notas es: {promedio_notas}")


class Colegio_nacional:
    def __init__(self, cantidad_alumnos, suma_notas):
        self.cantidad_alumnos = cantidad_alumnos
        self.suma_notas = suma_notas

    def calcular_promedio(self):
        if self.cantidad_alumnos > 0:
            promedio = self.suma_notas / self.cantidad_alumnos
            return promedio
        else:
            return "La cantidad de alumnos debe ser mayor que cero."

# Crear una instancia de la clase Colegio_nacional con los datos proporcionados
mi_colegio = Colegio_nacional(cantidad_alumnos=50, suma_notas=157)

# Calcular y mostrar el promedio de notas
promedio_notas = mi_colegio.calcular_promedio()

 
 
def saludar () : 
    return 'hola'

gente = saludar ()
print (gente)

    
import string_1

print (string_1.restar(8,7))


