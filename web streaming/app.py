from flask import Flask,render_template,request,session
import mysql.connector

app = Flask(__name__)

# @app.route('/data_daftar',methods=['POST'])
# def data_pendaftar():
#     nama = request.form.get('nama')
#     password = request.form.get('password')
#     return render_template('daftar.html',nama=nama,password=password)



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

