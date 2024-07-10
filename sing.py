class FordK :
    faros = 2
    def __init__(self,color = 'azul ', puertas = 5) :
        self.gh = color
        self.puertas =  puertas
      
auto1 =  FordK ()
auto2 = FordK ()
    
print ( auto1.gh , 'puertas', auto1.puertas,';'  'faros' , auto1.faros)

print (auto2.puertas)



class Car :
    def __init__ (self,color ) : 
       self.color = color

car1 = Car (2)
car2 =Car(45454)

print (car1.color) 
print (car2.color)

 
class Peugeot :
    
    def pintar (self,puerta = 2,color = 'negro') :
       
        self.puerta = puerta
        self.color= color
 
       
car1 = Peugeot ()
car1.pintar (2,'rojo')
car2 = Peugeot ()
car2.pintar ('' )
print (car1.puerta,car1.color)
print (car2.puerta,car2.color)

class Fiat :
    def __init__ (self,puerta = 2 , color = 'negro',) :
       self.puerta = puerta 
       self.color = color 
       self.radio = True
       
auto1 = Fiat ()
print (auto1.color,auto1.radio)


def sumar_numeros (n1 = 7 , n2 = 9 ) : 
    
    return n1 + n2     
         
     
    


calculadora = sumar_numeros ()


print ( calculadora )
print (sumar_numeros ())

def mostrar_palabra () : 
   print ('perro')

loc = mostrar_palabra()


class promedios () :
     def __init__ (self,nota = 5 , alumnos = 5 ) :
        self.nota = nota
        self.alumnos = alumnos
        
        
colegio1 = promedios ()

colegio2 = promedios (100,10)


print ('el promedio de colegio1 es : ' , colegio1.nota / colegio1.alumnos)
print ('el promedio de colegio2 es :', colegio2.nota / colegio2.alumnos)
      
 
def mostrar_palabras ():
    print ('qqq')
    
x = mostrar_palabras ()
    

 
...

print ('yuy')








