from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessária para utilizar sessões

# Simulação de um banco de dados simples
users_db = {
    "usuario@example.com": "senha123"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    # Verificar se as credenciais estão corretas
    if email in users_db and users_db[email] == senha:
        flash('Login bem-sucedido!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Credenciais inválidas', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)