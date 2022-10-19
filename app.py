from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/seleccion")
def algorithms():
    return render_template("algoriSelec.html")

@app.route("/remplazo")
def remplazo():
    return render_template("estrRem.html")

def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
