from flask import Flask,render_template,request,session,jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    user = 'freedb_smaddok',
    password = 'T#Ff9CR4fuHFGBM',
    host = 'sql.freedb.tech',
    database = 'freedb_sdk_db',
    port ='3306'
)
cs = db.cursor()

# cs.execute("ALTER TABLE vote ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# db.commit()

# cs.execute("DELETE FROM vote WHERE id=%s",(6,))
# db.commit()

# cs.execute("UPDATE vote SET vote1 = %s", (0,))
# db.commit()
# cs.execute("SELECT * FROM vote")
# for x in cs:
#     print(x)


# @app.route('/data_daftar',methods=['POST'])
# def data_pendaftar():
#     nama = request.form.get('nama')
#     password = request.form.get('password')
#     return render_template('daftar.html',nama=nama,password=password)


@app.route('/content/vote/add1')
def addVote():
    cs.execute("SELECT vote1 FROM vote")
    votedb = cs.fetchone()[0]
    votedb += 1
    cs.execute("UPDATE vote SET vote1=%s WHERE id=%s",(votedb,1))
    db.commit()
    return jsonify(votedb)
#------------------halaman---------------------
@app.route("/")
def utama():
    return render_template('utama.html')

@app.route('/user/login')
def login():
    return render_template('user/login.html')

@app.route('/user/daftar')
def daftar():
    return render_template('user/daftar.html')

@app.route('/content/vote')
def vote():
    return render_template('content/vote.html')

@app.route('/content/streaming')
def streaming():
    return render_template('content/streaming.html')

# app.run(debug=True)
cs.close()
db.close()