import math
from tokenize import Double


class Persona:
    tipoDoc="T.I"
    documento="1104544674"
    nombre="Cristian"
    apellido="Duque"
    peso=48
    estatura=1.68
    edad=18
    sexo="Masculino"
    
    def _init_(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo):
        self._tipoDoc="T.I"
        self._documento="1104544674"
        self._nombre="Andre"
        self._apellido="Castañeda"
        self._peso=48
        self._estatura=1.68
        self._edad=18
        self._sexo="Masculino"
        
    def pedirDatos(self):
        self.__tipoDoc=input("Digite su tipo de Documento")
        self.__documento=input("Digite su Documento")
        self.__nombre=input("Digite su nombre")
        self.__apellido=input("Digite su apellido")
        self.__peso=float(input("Digite su peso"))
        self.__estatura=float(input("Digite su estatura"))
        self.__edad=int(input("Digite su edad"))
        self.__sexo=input("Digite su sexo")
        
    def mostrarPersona(self):
        print("Los Datos De El Paciente",self.__nombre,self.__apellido,"Son Los Siguientes:\nTipo De Documento:",self.__tipoDoc,"\nNumero De Documento:",self.__documento,"\nEdad:",self.__edad,"Años\nGenero:",self.__sexo,"\nPeso:",self.__peso,"kg\nEstatura",self.__estatura,"m")
    def calcularImc(self):
        elevaciónEstatura=math.pow(self.__estatura,2)
        imc=self.__peso/elevaciónEstatura
        print("Su imc es:",imc)
        if imc <20.0:
            pesoPersona="El peso está por debajo de lo ideal"
        elif imc>=20.0 and imc<=25.0:
            pesoPersona="El peso   es ideal"
        else:
            pesoPersona="Tiene Sobrepeso"
        
        return pesoPersona
    def mayorEdad(self):
        if self.__edad >=18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")