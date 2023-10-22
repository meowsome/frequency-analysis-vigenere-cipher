from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    keylength = request.form['keylength']
    print(ciphertext, keylength)
    return 'hi'