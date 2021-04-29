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
