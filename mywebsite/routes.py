from flask import request, render_template, redirect, url_for, flash
from mywebsite import app, mysql
from .form import RegistrationForm

@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/login',)
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit ():
        flash(f'Anda Berhasil Register {form.username.data} !', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form, title='Register')

@app.route('/datamahasiswa')
def data_mahasiswa():
    cursor = mysql.get_db().cursor()
    cursor.execute('''SELECT * FROM data_mahasiswa''')
    data = cursor.fetchall()
    cursor.close()
    return render_template('datamahasiswa.html', data=data)

@app.route('/datamahasiswa/simpan', methods = ['POST'])
def simpan_data():
    cursor = mysql.get_db().cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''INSERT INTO data_mahasiswa VALUES (%s,%s,%s)''', (nama,nim,alamat,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/hapus/<string:nim>')
def hapus_data(nim):
    cursor = mysql.get_db().cursor()
    cursor.execute('''DELETE FROM data_mahasiswa WHERE nim=%s''', (nim,))
    mysql.connection.commit()
    return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/update', methods=['POST'])
def update_data():
    cursor = mysql.get_db().cursor()
    nama = request.form['nama']
    nim = request.form['nim']
    alamat = request.form['alamat']
    cursor.execute('''UPDATE data_mahasiswa SET nama=%s, alamat=%s WHERE nim=%s''', (nama,alamat,nim))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('data_mahasiswa'))
