from flask import Flask
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jeegaje123'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'

mysql = MySQL()
mysql.init_app(app)
"""

app.config['SECRET_KEY'] = '66ec6299e1ce91198534fd318937cb61'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jeegaje123@localhost:3306/flask?unix_socket=/opt/lampp/var/mysql/mysql.sock'

db = SQLAlchemy(app)

from mywebsite import routes
