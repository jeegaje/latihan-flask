from mywebsite import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class dataMahasiswa(db.Model):
   __tablename__ = "data_mahasiswa_baru"
   id = db.Column(db.Integer, primary_key=True)
   nama = db.Column(db.String(50))
   alamat = db.Column(db.String(80))
   nim = db.Column(db.String(20), unique=True)

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

class dataLogin(db.Model):
   __tablename__ = "data_login"
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(40))
   email = db.Column(db.String(120))
   password = db.Column(db.String(150))

   def __repr__(self):
       return f"{self.id}"

db.create_all()

class DataMahasiswaSchema(ModelSchema):
   class Meta(ModelSchema.Meta):
       model = dataMahasiswa
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   nama = fields.String(required=True)
   alamat = fields.String(required=True)
   nim = fields.String(required=True)
