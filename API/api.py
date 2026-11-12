from flask import Flask, jsonify, request
import core

app = Flask(__name__)


# ver o estado
@app.route("/estado", methods=["GET"])
def pegar_estado():
    return jsonify({"temperatura": core.temperatura, "alarme": core.alarme, "porta": core.porta})


# mudar a temperatura
@app.route("/temperatura", methods=["POST"])
def mudar_temperatura():
    dados = request.get_json()
    core.temperatura = dados["temperatura"]
    return jsonify({"ok": True})


# ligar/desligar o alarme
@app.route("/alarme", methods=["POST"])
def mudar_alarme():
    dados = request.get_json()
    core.alarme = dados["alarme"]
    return jsonify({"ok": True})


# abrir/fechar a porta
@app.route("/porta", methods=["POST"])
def mudar_porta():
    dados = request.get_json()
    core.porta = dados["porta"]
    return jsonify({"ok": True})


app.run(port=5000)
