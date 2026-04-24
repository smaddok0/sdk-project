from flask import Flask,render_template,request,session,jsonify,redirect,url_for
import psycopg2,os
app = Flask(__name__)
app.secret_key = '*smaddok'

# db_link = os.getenv('db_link')
# db = psycopg2.connect(db_link)
db = psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")
cs = db.cursor()
def vote_default():
    dfl_vote = "UPDATE vote SET vote1=0, vote2=0 , vote3=0"
    test_vote = "SELECT * FROM vote"
    cs.execute(dfl_vote)
    db.commit()
    cs.execute(test_vote)
    print(cs.fetchall())

# import mysql.connector
# db = mysql.connector.connect(
#     user = 'freedb_smaddok',
#     password = 'T#Ff9CR4fuHFGBM',
#     host = 'sql.freedb.tech',
#     database = 'freedb_sdk_db',
#     port ='3306'
# )
# cs = db.cursor()

# cs.execute("ALTER TABLE vote ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# db.commit()

# cs.execute("DELETE FROM vote WHERE id=%s",(6,))
# db.commit()

# cs.execute("UPDATE vote SET vote1 = %s", (0,))
# db.commit()
# cs.execute("SELECT * FROM vote")
# ax = cs.fetchall()
# for x in ax:
#     print(x)


# @app.route('/data_daftar',methods=['POST'])
# def data_pendaftar():
#     nama = request.form.get('nama')
#     password = request.form.get('password')
#     return render_template('daftar.html',nama=nama,password=password)
# ------------vote1------------
@app.route('/content/vote/preview1')
def addVote_p1():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote1 FROM vote")
            votedb = cs.fetchone()[0]
            return jsonify(votedb)
    
@app.route('/content/vote/add1')
def addVote1():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote1 FROM vote")
            votedb = cs.fetchone()[0]
            votedb += 1
            cs.execute("UPDATE vote SET vote1=%s WHERE id=%s",(votedb,1))
            db.commit()
            return jsonify(votedb)


# --------------------vote2---------------
@app.route('/content/vote/preview2')
def addVote_p2():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote2 FROM vote")
            votedb = cs.fetchone()[0]
            return jsonify(votedb)
    
@app.route('/content/vote/add2')
def addVote2():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote2 FROM vote")
            votedb = cs.fetchone()[0]
            votedb += 1
            cs.execute("UPDATE vote SET vote2=%s WHERE id=%s",(votedb,1))
            db.commit()
        return jsonify(votedb)


# -----------------------vote3-----------------
@app.route('/content/vote/preview3')
def addVote_p3():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote3 FROM vote")
            votedb = cs.fetchone()[0]
            return jsonify(votedb)
    
@app.route('/content/vote/add3')
def addVote3():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            cs.execute("SELECT vote3 FROM vote")
            votedb = cs.fetchone()[0]
            votedb += 1
            cs.execute("UPDATE vote SET vote3=%s WHERE id=%s",(votedb,1))
            db.commit()
        return jsonify(votedb)

#--------------------login--------------------
@app.route('/user/daftar/submit', methods=['POST'])
def input_daftar():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            data = request.json
            nama = data.get('user')
            password = data.get('password')

            cs.execute("SELECT 1 FROM users WHERE nama = %s",(nama,))
            current = cs.fetchone()

            if current:
                return jsonify({"ada":'coba nama lain'})
            else:
                if password == "":
                    return jsonify({"pass":'masukkan password'})
                else:
                    cs.execute("INSERT INTO users (nama,password) VALUES(%s,%s)",(nama,password))
                    db.commit()
                    return jsonify({"redirect":'/user/login'})
    
@app.route('/user/login/submit', methods=['POST'])
def input_login():
    db_link = os.getenv('db_link')
    # with psycopg2.connect("postgresql://neondb_owner:npg_7pAzTFnJLRE0@ep-frosty-queen-akblv49h-pooler.c-3.us-west-2.aws.neon.tech/sdk_db?sslmode=require&channel_binding=require")as db :
    with psycopg2.connect(db_link)as db :
        with db.cursor()as cs:
            data = request.json
            nama = data.get('user')
            password = data.get('password')

            cs.execute('SELECT * FROM users WHERE nama = %s',(nama,))
            terdaftar = cs.fetchone()
            if terdaftar and not None:
                if password == terdaftar[1]:
                    session['user'] = terdaftar[0]
                    return jsonify({'ada':'ada'})
                else:
                    return jsonify({'salah':'password salah'})
            else:
                return jsonify({'belum':'belum terdaftar'})
               
@app.route('/user/logout/submit')
def input_logout():
    session.clear()
    return redirect('/')

#------------------komen--------------------
@app.route('/streaming/komen', methods=['POST'])
def komen():
    data = request.json
    cmd = data['komen']
    return jsonify(cmd)


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
# cs.close()
# db.close()



# cs.execute("UPDATE users SET nama=%s,password=%s",())
# cs.execute("SELECT * FROM users")
# print(cs.fetchall())