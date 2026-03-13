
from flask import Flask, render_template, request
from consulta import consultar_veiculo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    dados = None
    erro = None

    if request.method == "POST":
        placa = request.form.get("placa")
        if not placa:
            erro = "Digite uma placa válida."
        else:
            try:
                dados = consultar_veiculo(placa)
            except Exception as e:
                erro = f"Erro na consulta: {e}"

    return render_template("index.html", dados=dados, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
