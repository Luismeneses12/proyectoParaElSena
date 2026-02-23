from ..extesions import db
from .modelcliente_cuenta import ClienteCuenta


class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    cliente_cuenta_id = db.Column(db.Integer, db.ForeignKey('cliente_cuenta.id'), nullable=False)

    cliente_cuenta = db.relationship('clienteCuenta', backref='pagos')

    def __repr__(self):
        return f'<Pago {self.id} - Monto: {self.monto}>'