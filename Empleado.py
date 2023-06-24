from salud.Persona import Persona 

class Empleado(Persona):
    #Atributos
    cargo="Gerente"
    valorHora=50000
    horasTrabajadas=5
    departamento="Bucaramanga"
    valorTotalHonorarios=0.0  
    #metodo
    def calcularHonorarios(self):
        valorTotal=self.valorHora*self.horasTrabajadas
        porcentaje= 0.00966*valorTotal
        self.valorTotalHonorarios=valorTotal-porcentaje
    def imprimirEmpleado(self):
        print(f"Según La Nomina, Los Datos Del Empleado Identificado Con {self.tipoDoc} {self.documento}, con Nombre y Apellido {self.nombre} {self.apellido} Son Los Siguientes:\nCargo: {self.cargo}\nHoras Trabajadas: {self.horasTrabajadas}\nValor Por Hora {self.valorHora}\nTotal A Pagar: {self.valorTotalHonorarios}")


