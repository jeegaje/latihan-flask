from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = '66ec6299e1ce91198534fd318937cb61'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jeegaje123'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'

mysql = MySQL()
mysql.init_app(app)

from mywebsite import routes
