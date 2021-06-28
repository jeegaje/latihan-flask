from flask import abort, request, render_template, redirect, url_for, flash, jsonify, make_response
from mywebsite import app, db, bcrypt
from .form import RegistrationForm, LoginForm, TambahDataMahasiswa
from .models import dataMahasiswa, DataMahasiswaSchema, dataLogin, dataAkun, DataAkunSchema, dataTest, DataTestSchema, coba, Todo, Todo_Todo, TodoSchema, cobaLagi
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/',)
def index():
    data = db.session.query(coba).all()
    return render_template('index.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = dataLogin.query.filter_by(username=form.username.data).first()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit ():
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))

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
@login_required
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
    datanim = request.args.get('nim')
    cekdata = dataMahasiswa.query.filter_by(nim=datanim).first()
    if request.method == 'POST':
        data_schema = DataMahasiswaSchema()
        error = data_schema.validate(request.args)
        if error or request.args.get('nama') == "" or request.args.get('nim') == "" or request.args.get('alamat') == "":
            return make_response("Harap isi semua parameter! Nama, Nim, dan Alamat")
        elif cekdata is None:
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
            return make_response("NIM Sudah diambil!")

    else:
        data = dataMahasiswa.query.all()
        data_schema = DataMahasiswaSchema(many=True)
        hasil = data_schema.dump(data)
        return make_response(jsonify(hasil))

@app.route('/api/datamahasiswa/<int:id>', methods=['DELETE', 'PUT'])
def api2(id):
    datanim = request.args.get('nim')
    cekdata = dataMahasiswa.query.filter_by(nim=datanim).first()

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
            return make_response("Harap isi semua parameter! Nama, Nim, dan Alamat")
        elif cekdata is None:
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
        else:
            return make_response("NIM sudah diambil!")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/akun')
@login_required
def akun():
    return render_template('account.html')

@app.route('/rizky', methods=['GET', 'POST'])
def rizki():
    data_schema = DataTestSchema(many=True)
    if request.method == 'POST':
        id = request.args.get('id')
        username = request.args.get('username')
        datetime = request.args.get('datetime')
        simpan = {
            "id" : "{}" .format(id),
            "username" : "{}" .format(username),
            "datetime" : "{}" .format(datetime),
            }
        juju = request.get_json()
        data = data_schema.load(juju)
        hasil = data_schema.dump(data.create())
        return make_response(jsonify(hasil))
    else:
        data = db.session.query(coba).all()
        hasil = data_schema.dump(data)
        return make_response(jsonify(hasil))

@app.route('/api/rizki', methods=['GET'])
def apiRizki():
   data = db.session.query(dataAkun).all()
   schema = TodoSchema(many=True)
   hasil = schema.dump(data)
   return make_response(jsonify(hasil))

@app.route('/api/rizki', methods=['POST'])
def apiRizkiPost():
   #data = request.get_json()
   id = request.args.get('id')
   password = request.args.get('password')
   last_login = request.args.get('last_login')
   username = request.args.get('username')
   full_name = request.args.get('full_name')
   status = request.args.get('status')
   account_type = request.args.get('account_type')
   date_of_birth = request.args.get('date_of_birth')
   email = request.args.get('email')
   profile_picture = request.args.get('profile_picture')
   is_active = request.args.get('is_active')
   simpan = {
       "id" : "{}" .format(id),
       "password" : "{}" .format(password),
       "last_login" : "{}" .format(last_login),
       "username" : "{}" .format(username),
       "full_name" : "{}" .format(full_name),
       "status" : "{}" .format(status),
       "account_type" : "{}" .format(account_type),
       "date_of_birth" : "{}" .format(date_of_birth),
       "email" : "{}" .format(email),
       "profile_picture" : "{}" .format(profile_picture),
       "is_active" : "{}" .format(is_active),
       }
   schema = TodoSchema()
   load = schema.load(simpan)
   db.session.add(load)
   db.session.commit()
   hasil = schema.dump(load)
   return make_response(jsonify(hasil))

@app.route('/api/rizki/<int:id>', methods=['DELETE'])
def apiRizkiDelete(id):
    hapus = db.session.query(dataAkun).filter_by(id=id).first()
    db.session.delete(hapus)
    db.session.commit()
    data = db.session.query(dataAkun).all()
    data_schema = TodoSchema(many=True)
    hasil = data_schema.dump(data)
    return make_response(jsonify(hasil))

@app.route('/api/rizki/<int:id>', methods=['PUT'])
def apiRizkiPut(id):
    update = db.session.query(dataAkun).filter_by(id=id).first()
    password = request.args.get('password')
    last_login = request.args.get('last_login')
    username = request.args.get('username')
    full_name = request.args.get('full_name')
    status = request.args.get('status')
    account_type = request.args.get('account_type')
    date_of_birth = request.args.get('date_of_birth')
    email = request.args.get('email')
    profile_picture = request.args.get('profile_picture')
    is_active = request.args.get('is_active')
    update.password = password
    db.session.commit()
    data = db.session.query(dataAkun).all()
    data_schema = TodoSchema(many=True)
    hasil = data_schema.dump(data)
    return make_response(jsonify(hasil))
