# Combinacion de clase persona y clase contraseña. La clase persona se usara para crear contraseñas, tambien va a haber una clase contraseña, cuando se requiera una contraseña
# Se utilizara la clase contraseña para dar una contraseña y ademas se van a poder ver las contraseñas creadas.
# Clase persona debe tener atributos: Nombre, edad, genero, peso, altura. metodos: Calcular IMC y verificar mayoria de edad
# Clase contraseña debe generar contraseñas aleatorias y verificar si son seguras(Mayusculas, minusculas y numeros)

import random
import string
# Lista de caracteres usados para la contraseña
caracteres = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    
class persona:
    def __init__(self, nombre, edad, genero, peso, altura):
        # Atributos de la clase persona
        self.nombre = nombre
        self.edad = edad
        self.genero= genero
        self.peso = peso
        self.altura = altura

        # Verificar si el usuario quiere contraseña
        seguridad = input("Escriba SI, si desea obtener una contrasena, de lo contrario escriba NO")
        if (seguridad == "SI"):
            self.contrasena = contrasena()
        else:
            self.contrasena = None
        

    # Metodo para calcular el IMC
    def imc(self):
        imc = self.peso / (self.altura**2)
        print(f"El IMC de {self.nombre} es: {imc} \n")

     # Metodo para verificar mayoria de edad
    def mayoria_edad(self):
        if (self.edad >= 18):
            print(f"{self.nombre} es mayor de edad\n")
        else:
            print(f"{self.nombre} no es mayor de edad\n")


class contrasena:
    def __init__(self):
        # Lista de las contraseñas del usuario
        self.contrasenas = []

    # Metodo para generar contraseñas aleatorias
    def generar_contrasena(self):
        contrasena = ""
        for i in range (10):
            contrasena +=random.choice(caracteres)  

        # Revisa si la contraseña cumple con los parametros 
        mayuscula = any(c.islower() for c in contrasena)
        minuscula = any(c.isupper() for c in contrasena)
        numero = any(c.isdigit() for c in contrasena)
        
        if (minuscula & mayuscula & numero ):
            verificacion = True
        else:
            verificacion = False

        print(f"Su contrasena de usuario es: {contrasena}\n")
        estado_contrasena = input("Escriba SI para guardarla o por el contrario escriba NO para desecharla")
        if (estado_contrasena == "SI"):
            self.contrasenas.append(contrasena)



if __name__ == "__main__":
    personas = []