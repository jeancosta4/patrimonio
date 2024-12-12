from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql.cursors
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey'

# Configuração de conexão com o banco de dados



def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='patrimonio',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                return redirect(url_for('register_patrimonio'))
            else:
                flash('Usuário ou senha inválidos!')
        else:
            flash('Erro ao conectar ao banco de dados.')
    return render_template('login.html')

# Rota de cadastro de patrimônio
@app.route('/register', methods=['GET', 'POST'])
def register_patrimonio():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        numero_patrimonio = request.form['numero_patrimonio']
        descricao = request.form['descricao']
        local = request.form['local']
        condicao = request.form['condicao']

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO patrimonio (numero_patrimonio, descricao, local, condicao)
                VALUES (%s, %s, %s, %s)
            """, (numero_patrimonio, descricao, local, condicao))
            connection.commit()
            cursor.close()
            connection.close()
            flash('Patrimônio cadastrado com sucesso!')
            return redirect(url_for('register_patrimonio'))
        else:
            flash('Erro ao conectar ao banco de dados.')
    return render_template('register.html')

@app.route('/report', methods=['GET'])
def report():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Conectar ao banco de dados e buscar os itens
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM patrimonio")
    items = cursor.fetchall()
    cursor.close()
    connection.close()

    # Renderizar o template com os dados
    return render_template('report.html', items=items)


# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
