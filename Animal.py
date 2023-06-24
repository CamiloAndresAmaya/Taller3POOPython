class Animal:
 #Atributos
 nombre ="" #Atributo estático
 edad= 8
 
 
 
 
 #Metodos
 #Metodos propios de la clase
 def _init_(self,n,e):
     self.nombre=n
     self.edad=e
     
 def registrarAnimal(self):
     self.nombre=input("Ingrese el nombre del animal")
     self.edad=int(input("Ingrese la edad del animal"))
 def mostrarAnimal(self):
     print("El animal por nombre",self.nombre,"y su edad es",self.edad)
 #duplicarEdad pedir edad, retornar esa edad duplicada
 def duplicarEdad(self,edad):
     edadDuplicada=edad*2
     return edadDuplicada
     
     
 def cambiarNombre(self):
     cambiarNombre=input("digite el numero nombre")
     self.nombre=cambiarNombre
     print("el nuevo nombre es",self.nombre)
     


#crear un objeto o instanciar clase
tigre = Animal()
tigre.nombre="Tony"
tigre.edad=5

panda = Animal()
panda.nombre="Reinaldo"
panda.edad=14

print("La edad del animal",tigre.nombre,"es",tigre.edad)
      