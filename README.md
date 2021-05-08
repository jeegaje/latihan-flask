# latihan-flask

## Instalasi

Requirement :
* Python
* Pip & Virtual Environtment

Setelah requirement diatas sudah terpenuhi, install flask

Cara Install Flask :
1. Buka Console
2. Masuk ke virtual environment
3. Install flask `pip install flask`
4. Install extension flask
   Ada banyak extension pada flask, untuk saat ini saya butuh flask-mysqldb (Untuk koneksi mysql ke flask)
   install dengan `pip install flask-mysqldb`


## Run

Untuk menjalankan aplikasi sederhana

1. Buat file berekstesi .py (Contoh : **run.py**)
2. Pada **run.py** tulis kode berikut

   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
    return 'Hello, World!'

   app.run(debug=True)
3. Buka console, lalu tempatkan pada lokasi file **run.py** tersebut
4. Jalankan aplikasi dengan `python3 run.py`

## Penjelasan Kode

   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello_world():
    return 'Hello, World!'

   app.run(debug=True)
   ```

* Pertama lakukan import dari modul flask `from flask import Flask`
  modul **Flask** ini wajib kita import
* Kedua kita deklarasikan ```Flask(__name__)``` pada variabel `app`
  Hal ini dilakukan agar aplikasi nanti bisa mengidentifikasi template dan static file yang dibutuhkan nantinya
* Ketika adalah bagian **route**
  Bagian ini untuk mendeklarasikan URL apa saja yang kita butuhkan
* Terakhir method **run** sebagai perintah untuk menjalankan aplikasi
  argumen `debug=True` untuk mengaktifkan mode debugging

## Route

1. Route utama
   ```python
   @app.route('/')
   def index():
    return render_template('index.html')
   ```
   * Ini adalah halaman awal saat mengakses website
   * halaman ini berisi **index.html** yang berada pada folder **templates**
2. Route data mahasiswa
   ```python
   @app.route('/datamahasiswa')
   def data_mahasiswa():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM data_mahasiswa''')
    data = cursor.fetchall()
    cursor.close()
    return render_template('datamahasiswa.html', data=data)
   ```
   * ini adalah halaman **data mahasiswa** yang menampilkan tabel data mahasiswa dari database
   * `cursor.execute('''SELECT * FROM data_mahasiswa''')` ini merupakan query untuk memperoleh data dari database
   * `cursor.fetchall()` untuk mengambil semua data pada query sebelumya
3. Route simpan data
   ```python
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
   ```
   * ini merupakan route untuk menyimpan data yang ditambahkan ke dalam database
   * `nama = request.form['nama']` ini perintah untuk mengambil data dari form degan label **nama**, lalu disimpan pada variabel **nama**
   * `cursor.execute('''INSERT INTO data_mahasiswa VALUES (%s,%s,%s)''', (nama,nim,alamat,))` ini merupakan query untuk memasukan data dari inputan user
   * `mysql.connection.commit()` ini perintah untuk commit ke database
4. Route hapus data
   ```python
   app.route('/datamahasiswa/hapus/<string:nim>')
   def hapus_data(nim):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM data_mahasiswa WHERE nim=%s''', (nim,))
    mysql.connection.commit()
    return redirect(url_for('data_mahasiswa'))
   ```
   * ini merupakan route untuk menghapus data berdasarkan nim
   * `cursor.execute('''DELETE FROM data_mahasiswa WHERE nim=%s''', (nim,))` ini merupakan query untuk menghapus data sesuai denga nim
   * `mysql.connection.commit()` ini perintah untuk commit ke database
5. Route update data
   ```python
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
    ```
    * Ini merupakan route untuk update data sesuai dengan inputan user
    * `nama = request.form['nama']` ini perintah untuk mengambil data dari form degan label **nama**, lalu disimpan pada variabel **nama**
    * `cursor.execute('''UPDATE data_mahasiswa SET nama=%s, alamat=%s WHERE nim=%s''', (nama,alamat,nim))` ini merupakan query utuk mengupdate data sesuai inputan user
    * `mysql.connection.commit()` ini perintah untuk commit ke database

