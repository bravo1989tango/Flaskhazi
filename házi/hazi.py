from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/Fakebook")
def Fakebook():
    return render_template("Fakebook/Fakebook.html")

@app.route("/portfolio/1")
def Egy():
    return render_template("Fakebook/1.html")

@app.route("/portfolio/Boogle")
def Boogle():
    return render_template("Boogle/index.html")

@app.route("/portfolio/Login")
def Login():
    return render_template("Boogle/login.html")

@app.route("/portfolio/Hajszalon")
def Hajszalon():
    return render_template("Hajszalon/index.html")

@app.route("/portfolio/index")
def Hajszalonindex():
    return render_template("Hajszalon/index.html")

@app.route("/portfolio/egyeb")
def Hajszalonegyeb():
    return render_template("Hajszalon/egyeb.html")

@app.route("/portfolio/festes")
def Hajszalonfestes():
    return render_template("Hajszalon/festes.html")

@app.route("/portfolio/vagas")
def Hajszalonvagas():
    return render_template("Hajszalon/vagas.html")

if __name__ == '__main__':
    app.run()
