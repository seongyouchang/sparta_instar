from flask import Flask, render_template,request,jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.nvsfa.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route("/")
def home():
    return render_template('join1.html')

@app.route("/id_check", methods=["POST"])
def id_post():
    id_receive = request.form['id_give']
    id_list = list(db.join.find({},{'_id':False}))

    user_id=[]
    #print(id_receive)
    #print(id_list)

    for person in id_list:
        value=person['id']
        user_id.append(value)

    if id_receive in user_id: #중복된 아이디일 경우
        return jsonify(True)
    else:                      #중복되지 않는 아이디일 경우
        return jsonify(False)

@app.route("/register", methods=["POST"])
def inform_post():
    id_receive=request.form['id_give']
    pw1_receive=request.form['pw1_give']
    pw2_receive=request.form['pw2_give']
    nick_receive=request.form['nick_give']
    email_receive=request.form['email_give']

    #print(id_receive,pw1_receive,pw2_receive,nick_receive,email_receive)
    if '@' not in email_receive:
        return jsonify(0)

    if pw1_receive == pw2_receive:
        doc={
            'id':id_receive,
            'pw':pw1_receive,
            'nick':nick_receive,
            'email':email_receive
        }
        db.join.insert_one(doc)
        return jsonify(1)
    else:
        return jsonify(2)

if __name__ == '__main__':
    app.run(debug=True)


