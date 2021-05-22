from flask import request, render_template, redirect, url_for, flash, jsonify, make_response
from mywebsite import app, db
from .form import RegistrationForm
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

dataMahasiswa = [
    {
        "nama" : "Angga Jiyan",
        "nim" : "123001",
        "alamat" : "Sidoarjo, Jawa Timur"
    },
    {
        "nama" : "Fajar Chandra",
        "nim" : "123002",
        "alamat" : "Malang, Jawa Timur"
    },
    {
        "nama" : "Naufal Tamaam",
        "nim" : "123003",
        "alamat" : "Gresik, Jawa Timur"
    }
]

class dataMahasiswa(db.Model):
   __tablename__ = "data_mahasiswa_baru"
   id = db.Column(db.Integer, primary_key=True)
   nama = db.Column(db.String(20))
   alamat = db.Column(db.String(80))
   nim = db.Column(db.String(20))

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

   def __init__(self, nama, alamat, nim):
       self.nama = nama
       self.alamat = alamat
       self.nim = nim

   def __repr__(self):
       return f"{self.id}"

class DataMahasiswaSchema(ModelSchema):
   class Meta(ModelSchema.Meta):
       model = dataMahasiswa
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   nama = fields.String(required=True)
   alamat = fields.String(required=True)
   nim = fields.String(required=True)

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
        data = dataMahasiswa.query.all()
        return render_template('datamahasiswa.html', data=data)

@app.route('/datamahasiswa/simpan', methods = ['POST'])
def simpan_data():
        nama = request.form['nama']
        nim = request.form['nim']
        alamat = request.form['alamat']
        simpan = dataMahasiswa(nama=nama, nim=nim, alamat=alamat)
        db.session.add(simpan)
        db.session.commit()
        return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/hapus/<int:id>')
def hapus_data(id):
        hapus = dataMahasiswa.query.filter_by(id=(id)).first()
        db.session.delete(hapus)
        db.session.commit()
        return redirect(url_for('data_mahasiswa'))

@app.route('/datamahasiswa/update/<int:id>', methods=['POST'])
def update_data(id):
        nama = request.form['nama']
        nim = request.form['nim']
        alamat = request.form['alamat']
        update = dataMahasiswa.query.filter_by(id=(id)).first()
        update.nama = nama
        update.nim = nim
        update.alamat = alamat
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
        nama = request.args.get('nama')
        nim = request.args.get('nim')
        alamat = request.args.get('alamat')
        simpan = {
            "nama" : "{}" .format(nama),
            "nim" : "{}" .format(nim),
            "alamat" : "{}" .format(alamat)
            }
        data_schema = DataMahasiswaSchema()
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
        nama = request.args.get('nama')
        nim = request.args.get('nim')
        alamat = request.args.get('alamat')
        update = dataMahasiswa.query.filter_by(id=(id)).first()
        update.nama = nama
        update.nim = nim
        update.alamat = alamat
        db.session.commit()
        data_schema = DataMahasiswaSchema()
        hasil = data_schema.dump(update)
        return make_response(jsonify(hasil))
