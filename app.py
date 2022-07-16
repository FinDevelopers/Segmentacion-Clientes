from array import array
import json
import sys
import codecs

from pyrsistent import m
from clases import Cliente ,Transaccion, Direccion
  
#Crea in diccionario de python a partir de un archivo JSON
def readJSON(json_file):
    try:
        with open(json_file, 'r') as json_object:
            return json.load(json_object)
    except FileNotFoundError: 
        print("No existe el archivo")        

#Crea un objeto Black, Gold O Classic dependiendo el tipo de cliente del JSON
def crear_cliente(obj):
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
    else:
        cliente = Cliente.Classic(
            obj['nombre'],
            obj['apellido'],
            obj['numero'],
            obj['dni'],
        )
    

    cliente.direccion = Direccion.Direccion(
        obj['direccion']['calle'],
        obj['direccion']['numero'],
        obj['direccion']['ciudad'],
        obj['direccion']['provincia'],
        obj['direccion']['pais'],
    )
    return cliente

#Creando array de objetos Transactions dentro del objeto cliente
def crear_lista_transacciones(obj):
    transacciones = []
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
        transacciones.append(transactionObj)
    return transacciones

#Devuelve el cliente con las transacciones y razonesw
def asignar_razon(cliente):

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
    return cliente
#Crea el HTML del reporte
def crear_html(cliente):

    table_rows = ''
    for transaccion in cliente.transacciones:
        table_rows += '<tr>'
        for atributo in transaccion.devolver_array():
            table_rows += f'<td>{atributo}</td>'
        table_rows += '</tr>'

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
        
        html_file.write(html_content)

def validar_json(obj):
    #print(obj.values())
    validar_llaves(obj, ['numero', 'nombre', 'apellido', 'dni', 'tipo', 'direccion', 'transacciones'])
    
    validar_numero(obj['numero'])
    validar_string(obj['nombre'])
    validar_string(obj['apellido'])
    validar_string(obj['dni'])
    validar_tipo(obj['tipo'], ['BLACK','GOLD', 'CLASSIC'], "tipo")
    validar_diccionario(obj['direccion'])

    validar_llaves(obj['direccion'], ['calle', 'numero', 'ciudad', 'provincia', 'pais'])
    
    validar_string(obj['direccion']['calle'])
    validar_string(obj['direccion']['numero'])
    validar_string(obj['direccion']['ciudad'])
    validar_string(obj['direccion']['provincia'])
    validar_string(obj['direccion']['pais'])
    validar_lista(obj['transacciones'])

    for transaccion in obj['transacciones']:
        validar_diccionario(transaccion)
        validar_llaves(transaccion, ['estado', 'tipo', 'cuentaNumero', 'cupoDiarioRestante', 'monto', 'fecha', 'numero', 'saldoEnCuenta', 'totalTarjetasDeCreditoActualmente', 'totalChequerasActualmente'])
        validar_tipo(transaccion['estado'], ['ACEPTADA','RECHAZADA'], "estado")
        validar_tipo(transaccion['tipo'],['RETIRO_EFECTIVO_CAJERO_AUTOMATICO', 'ALTA_TARJETA_CREDITO', 'ALTA_CHEQUERA', 'COMPRA_DOLAR', 'TRANSFERENCIA_ENVIADA' ,'TRANSFERENCIA_RECIBIDA'], "tipo")
        validar_numero(transaccion['cuentaNumero'])
        validar_numero(transaccion['cupoDiarioRestante'])
        validar_numero(transaccion['monto'])
        validar_string(transaccion['fecha'])
        validar_numero(transaccion['numero'])
        validar_numero(transaccion['saldoEnCuenta'])
        validar_numero(transaccion['totalTarjetasDeCreditoActualmente'])
        validar_numero(transaccion['totalChequerasActualmente'])
        
        
def validar_llaves(diccionario, arreglo_llaves):
    keys_array = []
    
    for key in diccionario.keys():
        if key not in arreglo_llaves:
            print(f"Error, hay una llave no reconocida")
            exit()
        keys_array.append(key)

    if len(set(keys_array)) != len(arreglo_llaves):
        print("Error, la cantidad de datos no es la esperada")
        exit()


    
def validar_numero(numero):
    try: 
        if numero <= -1:
            print('Error en el formato: Numero menor a 0')
            exit()
    except TypeError:
            print("Numero tiene que ser una variable numerica")
            exit()

def validar_string(string):
    string = str(string)
    if len(string.strip()) == 0:
        print("La cadena está vacía")
        exit()
    

def validar_tipo(tipo, arreglo, nombre_tipo):
    if tipo not in arreglo:
        print(f'{tipo} no es un {nombre_tipo} válido')
        exit()

def validar_diccionario(diccionario):
    if not type(diccionario) == dict:
        print("El tipo de dato no es un diccionario")
        exit()

def validar_lista(lista):
    if not type(lista) == list:
        print("El tipo de dato no es una lista")
        exit()
#Funcion principal donde se ejecuta el script.
def main():

    try:
        json_file = sys.argv[1]
    except IndexError:
        print("No se ha enviado ningun archivo como parametro") 
        exit()

    obj = readJSON(json_file)
    validar_json(obj)
    #crear una funcion para obj validarJson
    cliente = crear_cliente(obj)
    cliente.transacciones = crear_lista_transacciones(obj)
    cliente = asignar_razon(cliente)
    crear_html(cliente)    
main()


#Validar que el json venga bien
#"numero": 100001,

