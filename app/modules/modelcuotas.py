from  ..extesions  import db
from . modelcliente_cuenta import ClienteCuenta
 

class Cuota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    fecha_vencimiento = db.Column(db.DateTime, nullable=False)
    
    usuarioCuenta = db.Column(db.Integer, db.ForeignKey('cliente_cuenta.id'), nullable=False)

    cliente_cuenta = db.relationship('ClienteCuenta', backref='cuotas') 


    def __repr__(self):
        return f'<Cuota {self.id} - Monto: {self.monto}>'
