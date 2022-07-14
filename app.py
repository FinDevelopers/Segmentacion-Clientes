import json
from pydoc import cli
from clases import Cliente ,Transaccion, Direccion
  
#Guarda un objeto un objetos JSON en un diccionario de python 
def readJSON(json_file):
    with open(json_file, 'r') as json_object:
        return json.load(json_object)

#Crea un diccionario con la información del JSON
obj = readJSON('eventos_classic.json')

#Crea un objeto Black, Gold O Classic dependiendo el tipo de cliente del JSON

if obj['tipo']== 'BLACK':
    cliente = Cliente.Black(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['dni'],
    )
elif obj['tipo'] == 'GOLD':
    cliente = Cliente.Gold(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['dni'],
    )
elif obj['tipo'] == 'CLASSIC':
    cliente = Cliente.Classic(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['dni'],
    )
else:
    raise Exception(f"No existe el tipo de cliente {obj['tipo']}") 

cliente.direccion = Direccion.Direccion(
    obj['direccion']['calle'],
    obj['direccion']['numero'],
    obj['direccion']['ciudad'],
    obj['direccion']['provincia'],
    obj['direccion']['pais'],
)

#Creando array de objetos Transactions dentro del objeto cliente
for transaction in obj['transacciones']:
    transactionObj = Transaccion.Transaccion(
        transaction['estado'],
        transaction['tipo'],
        transaction['cuentaNumero'],
        transaction['cupoDiarioRestante'],
        transaction['monto'],
        transaction['fecha'],
        transaction['numero'],
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
        elif transaction.tipo == 'COMPRA_DOLAR':
            if cliente.validar_compra_dolar(transaction) != True:
                transaction.razon = cliente.validar_compra_dolar(transaction)
        elif transaction.tipo == 'TRANSFERENCIA_ENVIADA':
            if cliente.transferencia_enviada(transaction) != True:
                transaction.razon = cliente.transferencia_enviada(transaction)
        elif transaction.tipo == 'TRANSFERENCIA_RECIBIDA':
            if cliente.transferencia_recibida(transaction) != True:
                transaction.razon = cliente.transferencia_recibida(transaction)

table_rows = ''
for transaccion in cliente.transacciones:
    table_rows += '<tr>'
    for atributo in transaccion.devolver_array():
        table_rows += f'<td>{atributo}</td>'
    table_rows += '</tr>'


import codecs

with codecs.open('prueba.html', 'w', "utf-8") as html_file:

    html_content = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>Reporte</title>
    </head>
    <body>
        <main class="container pt-5">
            <div class="row">
                <div class="col-12">
                    <h1 class="text-center mb-4">Reporte de Transacciones</h1>
                    <div class="card mx-auto mb-4 w-50 border border-1 border-dark">
                        <div class="card-header"> 
                            <h3>Cliente {cliente.__class__.__name__} {cliente.nombre} {cliente.apellido}</h3>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">Número de cuenta: {cliente.numero}</li>
                            <li class="list-group-item">DNI: {cliente.dni}</li>
                            <li class="list-group-item">Dirección: {cliente.direccion}</li>
                          </ul>
                    </div>

                    <table class="table table-striped table-bordered border border-1 border-dark">
                        <thead>
                            <tr>
                                <th scope="col">Nro.</th>
                                <th scope="col">Fecha</th>
                                <th scope="col">Tipo</th>
                                <th scope="col">Estado</th>
                                <th scope="col">Monto</th>
                                <th scope="col">Razón</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </main>
    </body>
</html>
    """
    
    # writing the code into the file
    html_file.write(html_content)






""" for i in range(len(cliente.transacciones)):
    print(cliente.transacciones[i].devolver_array())
 """

""" 
from pprint import pprint
print(cliente.direccion) """

#Como se relacionan las clases
#Cual es la relación entre transacción y cuenta
#¿Cuál es el objetivo principal de sprint?
#Que sería razón
#Hay q definir dirección?