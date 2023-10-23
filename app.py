from flask import Flask, render_template, request
from decipher import decrypt_given_keylength
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    print(request.form['ciphertext'])
    plaintext = decrypt_given_keylength(ciphertext=request.form['ciphertext'], keylength=int(request.form['keylength']))
    return plaintext

if __name__ == "__main__":
    app.run(debug=True)