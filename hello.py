from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jeegaje123'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template('index.html')

    return render_template('index.html')

@app.route('/datamahasiswa')
def data_mahasiswa():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM data_mahasiswa''')
    jumlah = cursor.fetchall()
    cursor.close()
    return render_template('datamahasiswa.html', jumlahData=jumlah)

@app.route('/simpan', methods = ['POST'])
def simpan_data():
    cursor = mysql.connection.cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''INSERT INTO data_mahasiswa VALUES (%s,%s,%s)''', (nama,nim,alamat,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))

@app.route('/hapus/<string:nim>')
def hapus_data(nim):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM data_mahasiswa WHERE nim=%s''', (nim,))
    mysql.connection.commit()
    return redirect(url_for('data_mahasiswa'))

@app.route('/update', methods=['POST'])
def update_data():
    cursor = mysql.connection.cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''UPDATE data_mahasiswa SET nama=%s, alamat=%s WHERE nim=%s''', (nama,alamat,nim))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))

app.run(host='localhost', port=5000, debug=True)
