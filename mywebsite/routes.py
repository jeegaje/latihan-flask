from flask import request, render_template, redirect, url_for
from mywebsite import app, mysql

@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/datamahasiswa')
def data_mahasiswa():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM data_mahasiswa''')
    data = cursor.fetchall()
    cursor.close()
    return render_template('datamahasiswa.html', data=data)

@app.route('/datamahasiswa/simpan', methods = ['POST'])
def simpan_data():
    cursor = mysql.connection.cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''INSERT INTO data_mahasiswa VALUES (%s,%s,%s)''', (nama,nim,alamat,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/hapus/<string:nim>')
def hapus_data(nim):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM data_mahasiswa WHERE nim=%s''', (nim,))
    mysql.connection.commit()
    return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/update', methods=['POST'])
def update_data():
    cursor = mysql.connection.cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''UPDATE data_mahasiswa SET nama=%s, alamat=%s WHERE nim=%s''', (nama,alamat,nim))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))
