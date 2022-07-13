

class Cliente(object):
    transacciones = [      
         {
            "estado": "ACEPTADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuenta_numero": 190,
            "cupo_diario_restante": 9000,
            "monto": 1000,
            "fecha": "10/10/2022 16: 00: 55",
            "saldo_en_cuenta": 100000,
            "total_tarjetas_credito" : 5,
            "total_chequeras" : 2
        }
    ]
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni

    def validar_retiro_efectivo(self,transacciones):
        pass
    def validar_tarjeta_credito(self,transacciones):
        pass
    def validar_chequera(self,transacciones):
        pass
    def validar_compra_dolar(self, transacciones):
        pass
    def transferencia_enviada(self, transacciones):
        pass
    def transferencia_recibida(self, transacciones):
        pass


class Classic(Cliente):

    def validar_retiro_efectivo(self, transacciones):
        for transaccion in transacciones:
            if transaccion['monto'] < transaccion['cupo_diario_restante']:
                if 10000 > transaccion['monto'] >= 1:
                    return True
            else:
                return False
                

    def validar_tarjeta_credito(self, transacciones):
        return False               
        
    def validar_chequera(self, transacciones):
        return False

    def validar_compra_dolar(self, transacciones):
        return False

    def transferencia_enviada(self, transacciones):
        comision = 0.01
        for transaccion in transacciones:
            if transaccion['monto'] + (transaccion['monto'] * comision) <= transaccion['saldo_en_cuenta']:
                return True
            else:
                return False 

    def transferencia_recibida(self, transacciones):
        for transaccion in transacciones:
            if transaccion['monto'] <= 150000:
                return True
            else:
                return False   


class Gold(Cliente):
    pass
class Black(Cliente):
    pass
a = Classic('juan','perez',234234,44213443)
b = a.transacciones
print(a.transferencia_enviada(b))