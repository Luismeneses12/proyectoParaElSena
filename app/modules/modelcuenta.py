from  ..extesions import db
from .modelUsuario import Usuario
from .modeloCliente import Cliente

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_cuenta = db.Column(db.String(100), unique=True, nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    tipoDecuenta = db.Column(db.String(100), nullable=False)  
      
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    cliente = db.relationship('cliente', backref='cuentas')
    usuario = db.relationship('usuario', backref='cuentas')

    def __repr__(self):
        return f'<Cuenta {self.numero_cuenta}>'