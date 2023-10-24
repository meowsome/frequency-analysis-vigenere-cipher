from flask import Flask, render_template, request, jsonify
from decipher import decrypt_given_keylength, validate_input, get_score
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    invalid_reason = validate_input(request.form['ciphertext'], request.form['keylength'])

    if not invalid_reason:
        try:
            plaintext, key = decrypt_given_keylength(ciphertext=request.form['ciphertext'], keylength=int(request.form['keylength']))
            score = get_score(plaintext)
        except IndexError:
            return jsonify({'error': True, 'message': "An unknown error occurred with the algorithm. Please try a different ciphertext and keylength combination."})
        else:
            return jsonify({'error': False, 'message': plaintext, 'key': key, 'score': score})
    else:
        return jsonify({'error': True, 'message': invalid_reason})

if __name__ == "__main__":
    app.run(debug=True)