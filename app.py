from flask import Flask
import pyotp

app = Flask(__name__)


@app.route('/totp/<key>')
def result(key):
    totp = pyotp.TOTP(key)
    return(totp.now())

if __name__ == '__main__':
    app.run(debug=True)
