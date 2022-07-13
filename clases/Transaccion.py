class Transaccion(object):
    def __init__(self, estado, tipo, cuenta_numero, cupo_diario_restante, monto, fecha, saldo_en_cuenta, total_tarjetas_credito, total_chequeras):
        self.estado = estado
        self.tipo = tipo
        self.cuenta_numero = cuenta_numero
        self.cupo_diario_restante = cupo_diario_restante
        self.monto = monto
        self.fecha = fecha
        self.saldo_en_cuenta = saldo_en_cuenta
        self.total_tarjetas_credito = total_tarjetas_credito
        self.total_chequeras = total_chequeras
    
    razon = ''

    