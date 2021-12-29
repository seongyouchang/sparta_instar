from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
SECRET_KEY = 'SPARTA'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login', methods=["POST"])
def test():
    id = request.form['id']
    pw = request.form['password']
    id_hash = hashlib.sha256(id.encode('utf-8')).hexdigest()
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    print(id, id_hash, pw, pw_hash)
    return jsonify({'msg': 'good~!!!!'})


if __name__ == '__main__':
    app.run(debug=True)
