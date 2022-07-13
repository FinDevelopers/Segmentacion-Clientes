from Transaccion import *

class Cliente(object):
    transacciones = []
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni

    def validar_retiro_efectivo(self,transaccion):
        pass
    def validar_tarjeta_credito(self,transaccion):
        pass
    def validar_chequera(self,transaccion):
        pass
    def validar_compra_dolar(self, transaccion):
        pass
    def transferencia_enviada(self, transaccion):
        pass
    def transferencia_recibida(self, transaccion):
        pass


class Classic(Cliente):
    def validar_retiro_efectivo(self, transaccion):
        if transaccion.monto <= transaccion.cupo_diario_restante:
            if transaccion.saldo_en_cuenta > transaccion.monto >= 1:
                return True
            else:
                return 'Saldo insuficiente'
        else:
            return 'Excedió el cupo diario'
                
    def validar_tarjeta_credito(self, transaccion):
        return 'Cliente Classic no puede tener tarjeta de crédito'               
        
    def validar_chequera(self, transaccion):
        return 'Cliente Classic no puede tener chequera'

    def validar_compra_dolar(self, transaccion):
        return 'CLiente Classic no puede comprar dólares'

    def transferencia_enviada(self, transaccion):
        comision = 0.01
        if transaccion.monto + (transaccion.monto * comision) <= transaccion.saldo_en_cuenta:
            return True
        else:
            return 'Saldo Insuficiente' 

    def transferencia_recibida(self, transaccion):
        if transaccion.monto <= 150000:
            return True
        else:
            return 'Cliente Classic no puede recibir más de $150.000 sin previo aviso'   


class Gold(Cliente):
    def validar_retiro_efectivo(self, transaccion):
        if transaccion.monto <= transaccion.cupo_diario_restante:
            if transaccion.saldo_en_cuenta + 10000 >= transaccion.monto >= 1:
                return True
            else:
                return 'Saldo insuficiente'
        else:
            return 'Excedió el cupo diario'
                
    def validar_tarjeta_credito(self, transaccion):
        if transaccion.total_tarjetas_credito == 0:
            return True
        else:
            return 'Cliente Gold no puede tener más de una tarjeta de crédito'
               
        
    def validar_chequera(self, transaccion):
        if transaccion.total_chequeras == 0:
            return True
        else:
            return 'Cliente Gold no puede tener más de una chequera'

    def validar_compra_dolar(self, transaccion):
        if transaccion.monto <= transaccion.saldo_en_cuenta:
            return True
        else:
            return 'Saldo Insuficiente' 

    def transferencia_enviada(self, transaccion):
        comision = 0.005
        if transaccion.monto + (transaccion.monto * comision) <= transaccion.saldo_en_cuenta + 10000:
            return True
        else:
            return 'Saldo Insuficiente' 

    def transferencia_recibida(self, transaccion):
        if transaccion.monto <= 500000:
            return True
        else:
            return 'Cliente Gold no puede recibir más de $500.000 sin previo aviso'   


class Black(Cliente):
    def validar_retiro_efectivo(self, transaccion):
        if transaccion.monto <= transaccion.cupo_diario_restante:
            if transaccion.saldo_en_cuenta + 10000 >= transaccion.monto >= 1:
                return True
            else:
                return 'Saldo insuficiente'
        else:
            return 'Excedió el cupo diario'
                
    def validar_tarjeta_credito(self, transaccion):
        if transaccion.total_tarjetas_credito <= 4:
            return True
        else:
            return 'Cliente Black no puede tener más de 5 tarjetas de crédito'
               
        
    def validar_chequera(self, transaccion):
        if transaccion.total_chequeras <= 1:
            return True
        else:
            return 'Cliente Black no puede tener más de dos chequeras'

    def validar_compra_dolar(self, transaccion):
        if transaccion.monto <= transaccion.saldo_en_cuenta:
            return True
        else:
            return 'Saldo Insuficiente' 

    def transferencia_enviada(self, transaccion):
        if transaccion.monto <= transaccion.saldo_en_cuenta + 10000:
            return True
        else:
            return 'Saldo Insuficiente' 

    def transferencia_recibida(self, transaccion):
        return True
        

# pruebas
"""a = Black('juan','perez',234234,44213443)
c = Transaccion('ACEPTADA', 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO', 19, 100000, 10000, '10/10/2022 16:00:55', -1, 4 , 1)
a.transacciones.append(c)
b = a.transacciones
print(a.transferencia_recibida(b[0]))"""