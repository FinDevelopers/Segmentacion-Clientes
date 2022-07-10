import json

class Cliente(object):

    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni

    def puede_crear_chequera():
        pass
    
    def puede_crear_tarjeta_credito():
        pass

    def puede_comprar_dolar():
        pass


class Classic(Cliente):
    def puede_crear_chequera():
        return False
    def puede_crear_tarjeta_credito():
        return False
    def puede_comprar_dolar():
        return False

class Gold(Cliente):
    def puede_crear_chequera():
        return True
    
    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar():
        return True

class Black(Cliente):
    def puede_crear_chequera():
        return True
    
    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar():
        return True


class Cuenta(object):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible):
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.monto = monto
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible = saldo_descubierto_disponible


class Direccion(object):
    def __init__(self, calle,numero,ciudad,provincia,pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
    
def readJSON(json_file):
    with open(json_file, 'r') as json_object:
        return json.load(json_object)

obj = readJSON('test.json')
if obj['tipo']== 'BLACK':
    cliente = Black(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'GOLD':
    cliente = Gold(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'CLASSIC':
    cliente = Classic(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
else:
    raise Exception(f"No existe el tipo de cliente {obj['tipo']}") 

print(cliente.dni)

#Como se relacionan las clases
#Cual es la relación entre transacción y cuenta
#¿Cuál es el objetivo principal de sprint?
#Que sería razón
#Hay q definir dirección?