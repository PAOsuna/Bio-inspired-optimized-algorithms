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


@app.route("/pso")
def pso():
    return render_template("pso.html")


@app.route("/cruce")
def cruce():
    return render_template("cruce.html")
    
@app.route("/aco")
def aco():
    return render_template("aco.html")

@app.route("/pso-algoritmo")
def psoAlgoritmo():
    return render_template("pso-algoritmo.html")

@app.route("/pso-parametro")
def psoParametro():
    return render_template("pso-parametros.html")

@app.route("/pso-topologias")
def psoTopologias():
    return render_template("pso-topologias.html")

@app.route("/pso-funcionamiento")
def psoFuncionamiento():
    return render_template("pso-funcionamiento.html")

@app.route("/pso-variantes")
def psoVariantes():
    return render_template("pso-variantes.html")



def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
