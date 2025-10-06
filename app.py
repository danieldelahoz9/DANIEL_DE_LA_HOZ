from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_secreta_demo"

# Almacenamiento temporal de usuarios (solo mientras corre el servidor)
usuarios = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['username']
        contrasena = request.form['password']

        if usuario in usuarios:
            flash('El usuario ya está registrado.', 'error')
        else:
            usuarios[usuario] = contrasena
            flash('Registro exitoso. Ahora puede iniciar sesión.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        contrasena = request.form['password']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            flash('Autenticación satisfactoria', 'success')
        else:
            flash('Error en autenticación', 'error')
        return redirect(url_for('home'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
