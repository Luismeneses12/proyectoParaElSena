from flask import Blueprint, request, jsonify
from app.modules.modelUsuario import Usuario
from app.extesions import db

usuario_blueprint = Blueprint('usuario_blueprint', __name__)

@usuario_blueprint.route('/usuarios', methods=['POST'])
def creacion_usuario():
    
    data = request.get_json()
    
    nuevo_usuario = Usuario(
        nombre=data["nombre"],
        email=data["email"],
        password=data["password"]
    )

    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify({"message": "Usuario creado exitosamente"}), 201


#metodo get para obtener todos los usuarios

@usuario_blueprint.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    usuarios_list = []
    
    for usuario in usuarios:
        usuarios_list.append({
            
            "nombre": usuario.nombre,
            "email": usuario.email
        })
    
    return jsonify(usuarios_list), 200 

#metodo put para actualizar un usuario por id
@usuario_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    data = request.get_json()
    
    usuario.nombre = data["nombre"]
    usuario.email = data["email"]
    usuario.password = data["password"]
    
    db.session.commit()
    
    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

#metodo para eleiminar un usuario por id
@usuario_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    db.session.delete(usuario)
    db.session.commit()
    
    return jsonify({"message": "Usuario eliminado exitosamente"}), 200