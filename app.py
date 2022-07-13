import json
from clases import Cliente ,Transaccion
  
#Guarda un objeto un objetos JSON en un diccionario de python 
def readJSON(json_file):
    with open(json_file, 'r') as json_object:
        return json.load(json_object)

#Crea un diccionario con la información del JSON
obj = readJSON('test.json')

#Crea un objeto Black, Gold O Classic dependiendo el tipo de cliente del JSON
if obj['tipo']== 'BLACK':
    cliente = Cliente.Black(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'GOLD':
    cliente = Cliente.Gold(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'CLASSIC':
    cliente = Cliente.Classic(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
else:
    raise Exception(f"No existe el tipo de cliente {obj['tipo']}") 

#Creando array de objetos Transactions dentro del objeto cliente
for transaction in obj['transacciones']:
    transactionObj = Transaccion.Transaccion(
        transaction['estado'],
        transaction['tipo'],
        transaction['cuentaNumero'],
        transaction['cupoDiarioRestante'],
        transaction['monto'],
        transaction['fecha'],
        transaction['saldoEnCuenta'],
        transaction['totalTarjetasDeCreditoActualmente'],
        transaction['totalChequerasActualmente'],
    )
    cliente.transacciones.append(transactionObj)

#Obtiene la razón de porque los cheques rechazados fueron rechazados
for transaction in cliente.transacciones:
    if transaction.estado == 'RECHAZADA':
        if transaction.tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            if cliente.validar_retiro_efectivo(transaction) != True:
                transaction.razon = cliente.validar_retiro_efectivo(transaction)
        elif transaction.tipo == 'ALTA_TARJETA_CREDITO':
            if cliente.validar_tarjeta_credito(transaction) != True:
                transaction.razon = cliente.validar_tarjeta_credito(transaction)
        elif transaction.tipo == 'ALTA_CHEQUERA':
            if cliente.validar_chequera(transaction) != True:
                transaction.razon = cliente.validar_chequera(transaction)
        elif transaction.tipo == 'COMPRAR_DOLAR':
            if cliente.validar_compra_dolar(transaction) != True:
                transaction.razon = cliente.validar_compra_dolar(transaction)
        elif transaction.tipo == 'TRANSFERENCIA_ENVIADA':
            if cliente.transferencia_enviada(transaction) != True:
                transaction.razon = cliente.transferencia_enviada(transaction)
        elif transaction.tipo == 'TRANSFERENCIA_RECIBIDA':
            if cliente.transferencia_recibida(transaction) != True:
                transaction.razon = cliente.transferencia_recibida(transaction)






from pprint import pprint
for transaccion in cliente.transacciones:
    pprint(vars(transaccion))

#Como se relacionan las clases
#Cual es la relación entre transacción y cuenta
#¿Cuál es el objetivo principal de sprint?
#Que sería razón
#Hay q definir dirección?