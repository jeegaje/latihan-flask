from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template('index.html')

    return render_template('index.html')

app.run(host='localhost', port=5000, debug=True)
