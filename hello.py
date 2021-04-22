from flask import Flask, request, render_template
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
    return render_template('datamahasiswa.html')

app.run(host='localhost', port=5000, debug=True)
