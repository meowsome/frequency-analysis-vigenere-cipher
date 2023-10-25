from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from decipher import decrypt_given_keylength, decrypt_range_keylength, validate_input, get_score

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["2/second", "60/minute"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    invalid_reason = validate_input(request.form['ciphertext'], request.form['keylength'], request.form['auto'])

    if not invalid_reason:
        try:
            plaintext, key, note = (None, None, None)
            if not request.form['auto'] == "true":
                plaintext, key, note = decrypt_given_keylength(ciphertext=request.form['ciphertext'], keylength=int(request.form['keylength']))
            else:
                plaintext, key, note = decrypt_range_keylength(ciphertext=request.form['ciphertext'])
            score = get_score(plaintext)
        except IndexError:
            return jsonify({'error': True, 'message': "An unknown error occurred with the algorithm. Please try a different ciphertext and keylength combination."})
        else:
            return jsonify({'error': False, 'message': plaintext, 'key': key, 'score': score, 'note': note})
    else:
        return jsonify({'error': True, 'message': invalid_reason})

if __name__ == "__main__":
    app.run(debug=True)