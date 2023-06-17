from flask import Flask, request, render_template
import codecs
app = Flask(__name__,static_folder='static')

player = "ごはん"
#メニュー
@app.route("/")
def menu():
    lines = []
    file = codecs.open("articles.txt","r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("form.html", player=player,lines=lines)
    





#お問い合わせ
@app.route("/form")
def form():
    
    return render_template("form.html")

#フォームの設定
@app.route("/result", methods=["POST"])
def result():
    morning = request.form["morning"]
    lunch = request.form["lunch"]
    dinner = request.form["dinner"]
    calori = request.form["calori"]
    day = request.form["day"]

    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(f"{morning}, {lunch}, {dinner},{calori},{day}\n")
    file.close()
    return render_template("result.html", morning=morning,lunch=lunch,dinner=dinner,calori=calori,day=day)

#アプリの説明
@app.route("/home")
def home():
    return render_template("home.html")