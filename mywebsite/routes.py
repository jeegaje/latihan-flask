from flask import abort, request, render_template, redirect, url_for, flash, jsonify, make_response
from mywebsite import app, db, bcrypt
from .form import RegistrationForm, LoginForm, TambahDataMahasiswa
from .models import dataMahasiswa, DataMahasiswaSchema, dataLogin

@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = dataLogin.query.filter_by(username=form.username.data).first()
    if form.validate_on_submit ():
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Kamu Berhasil Login! Selamat Datang { form.username.data }!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Kamu Gagal Login! Periksa username atau password anda!', 'danger')
    return render_template('login.html', form=form , title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    cekDataEmail = dataLogin.query.filter_by(email=form.email.data).first()
    cekDataUsername = dataLogin.query.filter_by(username=form.username.data).first()
    if form.validate_on_submit ():
        if cekDataEmail is None:
            if cekDataUsername is None:
                pass_generate = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = dataLogin(username=form.username.data, email=form.email.data, password=pass_generate)
                db.session.add(user)
                db.session.commit()
                flash(f'Anda Berhasil Register, Silahkan Login !', 'success')
                return redirect(url_for('login'))
            else:
                flash(f'Username sudah terdaftar! Coba Login!', 'danger')
        else:
            flash(f'Email sudah terdaftar! Coba Login!', 'danger')
    return render_template('register.html', form=form, title='Register')

@app.route('/datamahasiswa')
def data_mahasiswa():
        form = TambahDataMahasiswa()
        data = dataMahasiswa.query.all()
        return render_template('datamahasiswa.html', data=data, form=form, title='Data Mahasiswa')

@app.route('/datamahasiswa/simpan', methods = ['POST'])
def simpan_data():
        form = TambahDataMahasiswa()
        cekDataNim = dataMahasiswa.query.filter_by(nim=form.nim.data).first()
        if cekDataNim is None:
            simpan = dataMahasiswa(nama=form.nama.data, nim=form.nim.data, alamat=form.alamat.data)
            db.session.add(simpan)
            db.session.commit()
        else:
            flash(f'NIM sudah diambil!', 'danger')
        return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/hapus/<int:id>')
def hapus_data(id):
        hapus = dataMahasiswa.query.filter_by(id=(id)).first()
        db.session.delete(hapus)
        db.session.commit()
        return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/update/<int:id>', methods=['POST'])
def update_data(id):
        form = TambahDataMahasiswa()
        update = dataMahasiswa.query.filter_by(id=(id)).first()
        update.nama = form.nama.data
        update.nim = form.nim.data
        update.alamat = form.alamat.data
        db.session.commit()
        return redirect(url_for('data_mahasiswa'))
"""
@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        nama = request.args.get('nama')
        nim = request.args.get('nim')
        alamat = request.args.get('alamat')
        response = {
            "nama" : "{}" .format(nama),
            "nim" : "{}" .format(nim),
            "alamat" : "{}" .format(alamat)
            }
        res = make_response(jsonify(response))
        return res
    else:
        return jsonify(dataMahasiswa)
"""
@app.route('/api/datamahasiswa', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        data_schema = DataMahasiswaSchema()
        error = data_schema.validate(request.args)
        if error or request.args.get('nama') == "" or request.args.get('nim') == "" or request.args.get('alamat') == "":
            return (make_response("Harap isi semua parameter! Nama, Nim, dan Alamat"))
        else:
            nama = request.args.get('nama')
            nim = request.args.get('nim')
            alamat = request.args.get('alamat')
            simpan = {
                "nama" : "{}" .format(nama),
                "nim" : "{}" .format(nim),
                "alamat" : "{}" .format(alamat)
                }
            data = data_schema.load(simpan)
            hasil = data_schema.dump(data.create())
            return make_response(jsonify(hasil))

    else:
        data = dataMahasiswa.query.all()
        data_schema = DataMahasiswaSchema(many=True)
        hasil = data_schema.dump(data)
        return make_response(jsonify(hasil))

@app.route('/api/datamahasiswa/<int:id>', methods=['DELETE', 'PUT'])
def api2(id):

    if request.method == 'DELETE' :
        hapus = dataMahasiswa.query.filter_by(id=(id)).first()
        db.session.delete(hapus)
        db.session.commit()
        data = dataMahasiswa.query.all()
        data_schema = DataMahasiswaSchema(many=True)
        hasil = data_schema.dump(data)
        return make_response(jsonify(hasil))
    if request.method == 'PUT':
        data_schema = DataMahasiswaSchema()
        error = data_schema.validate(request.args)
        if error or request.args.get('nama') == "" or request.args.get('nim') == "" or request.args.get('alamat') == "":
            return (make_response("Harap isi semua parameter! Nama, Nim, dan Alamat"))
        else:
            nama = request.args.get('nama')
            nim = request.args.get('nim')
            alamat = request.args.get('alamat')
            update = dataMahasiswa.query.filter_by(id=(id)).first()
            update.nama = nama
            update.nim = nim
            update.alamat = alamat
            db.session.commit()
            hasil = data_schema.dump(update)
            return make_response(jsonify(hasil))
