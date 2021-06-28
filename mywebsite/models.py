from mywebsite import db, login_manager, Base
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return dataLogin.query.get(int(user_id))

dataTest = Base.classes.data_test
dataAkun = Base.classes.core_user
coba = Base.classes.data_test2
cobaLagi = Base.classes.todos
#dataAkun = db.Table('core_user', db.metadata, autoload=True, autoload_with=db.engine)

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

class dataLogin(db.Model, UserMixin):
   __tablename__ = "data_login"
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(40))
   email = db.Column(db.String(120))
   password = db.Column(db.String(150))

   def __repr__(self):
       return f"{self.id}"

class dataTest2(db.Model):
   __tablename__ = "data_test2"
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(40))
   datetime = db.Column(db.DateTime(6))

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

db.create_all()

class DataMahasiswaSchema(SQLAlchemySchema):
   class Meta:
       model = dataMahasiswa
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   nama = fields.String(required=True)
   alamat = fields.String(required=True)
   nim = fields.String(required=True)

class DataAkunSchema(SQLAlchemySchema):
   class Meta:
       model = dataAkun
       sqla_session = db.session
   id = fields.String(required=True)
   password = fields.String(required=True)
   last_login = fields.DateTime(required=True)
   username = fields.String(required=True)
   full_name = fields.String(required=True)
   status = fields.String(required=True)
   account_type = fields.String(required=True)
   date_of_birth = fields.String(required=True)
   email = fields.String(required=True)
   profile_picture = fields.String(required=True)
   is_active = fields.Number(dump_only=True)

class DataTestSchema(SQLAlchemySchema):
   class Meta:
       model = dataTest2
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   username = fields.String(required=True)
   datetime = fields.DateTime(required=True)


#======================================================

# Model
class Todo(db.Model):
   __tablename__ = "todos"
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(20))
   todo_description = db.Column(db.String(100))

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

   def __init__(self, title, todo_description):
       self.title = title
       self.todo_description = todo_description

   def __repr__(self):
       return f"{self.id}"

class Todo_Todo(db.Model):
   __tablename__ = "todos2"
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(20))
   todo_description = db.Column(db.String(100))

   def __repr__(self):
       return f"{self.id}"

db.create_all()

class TodoSchema(SQLAlchemySchema):
   class Meta:
       model = dataAkun
       sqla_session = db.session
   id = fields.String(required=True)
   password = fields.String(required=True)
   last_login = fields.String(required=True)
   username = fields.String(required=True)
   full_name = fields.String(required=True)
   status = fields.String(required=True)
   account_type = fields.String(required=True)
   date_of_birth = fields.String(required=True)
   email = fields.String(required=True)
   profile_picture = fields.String(required=True)
   is_active = fields.String(required=True)
