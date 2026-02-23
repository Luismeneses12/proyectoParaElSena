from flask import Flask
from .extesions import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    from .modules.modelcliente_cuenta import ClienteCuenta
    from .modules.modelcuotas import Cuota
    from .modules.modelpago import Pago
    from .modules.modeloCliente import Cliente
    from .modules.modelcuenta import Cuenta
    from .modules.modelUsuario import Usuario   
    
    #rutar de los blueprints
    from .routes.roterUsuario.usuario_bueprint import usuario_blueprint
    app.register_blueprint(usuario_blueprint)     

    return app
