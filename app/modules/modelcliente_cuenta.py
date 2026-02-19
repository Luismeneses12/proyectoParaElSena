from ..extesions import db
from .modeloCliente import Cliente
from .modelcuenta import Cuenta

class ClienteCuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id'), nullable=False)
    
    capitalInicial = db.Column(db.Float, nullable=False)
    capitalRestante = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    tipoComportaminento = db.Column(db.String(100), nullable=False)
    
    
    cliente = db.relationship('cliente', backref='cliente_cuentas')
    cuenta = db.relationship('Cuenta', backref='cliente_cuentas')