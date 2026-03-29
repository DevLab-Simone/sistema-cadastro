from flask import Flask, render_template, request, redirect

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    usuarios.append({
        "nome": nome,
        "idade": idade,
        "email": email
    })

    return redirect('/usuarios')

@app.route('/usuarios')
def listar():
    return render_template('lista.html', usuarios=usuarios)

app.run(debug=True)