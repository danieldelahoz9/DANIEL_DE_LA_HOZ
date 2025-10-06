from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = "clave_secreta_demo"

# Base temporal de usuarios
usuarios = {}

# Ruta para registrar usuarios (POST)
@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    usuario = data["username"]
    contrasena = data["password"]

    if usuario in usuarios:
        return jsonify({"success": False, "message": "El usuario ya existe"}), 400

    usuarios[usuario] = contrasena
    return jsonify({"success": True, "message": "Usuario registrado correctamente"}), 201


# Ruta para iniciar sesión (POST)
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    usuario = data["username"]
    contrasena = data["password"]

    if usuario in usuarios and usuarios[usuario] == contrasena:
        return jsonify({"success": True, "message": "Autenticación satisfactoria"}), 200
    else:
        return jsonify({"success": False, "message": "Error en autenticación"}), 401


# Ruta GET para ver usuarios (solo de prueba)
@app.route('/api/users', methods=['GET'])
def api_users():
    return jsonify({"usuarios": list(usuarios.keys())})


if __name__ == '__main__':
    app.run(debug=True)
