class Transaccion(object):
    razon = ''

    def __init__(self, estado, tipo, cuenta_numero, cupo_diario_restante, monto, fecha, numero, saldo_en_cuenta, total_tarjetas_credito, total_chequeras):
        self.estado = estado
        self.tipo = tipo
        self.cuenta_numero = cuenta_numero
        self.cupo_diario_restante = cupo_diario_restante
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldo_en_cuenta = saldo_en_cuenta
        self.total_tarjetas_credito = total_tarjetas_credito
        self.total_chequeras = total_chequeras

    def devolver_array(self):
        return [
            self.numero,
            self.fecha, 
            self.tipo,
            self.estado,  
            f"${self.monto}",
            self.razon,
        ]

    

    