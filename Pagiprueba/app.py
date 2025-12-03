from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('indexx.html')

@app.route("/loginlink")
def hone1():
    return render_template('Loginlink.html')

@app.route("/loginpetstore")
def home2():
    return render_template('loginpetstore.html')

@app.route("/petlink")
def home3():
    return render_template('petlink.html')

@app.route("/petstores")
def home4():
    return render_template('petstores.html')

if __name__ == '__main__':
    app.run(debug=True)