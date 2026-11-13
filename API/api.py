from flask import Flask, jsonify, request
import core

app = Flask(__name__)



@app.route("/estado", methods=["GET"])
def pegar_estado():
    return jsonify({"temperatura": core.temperatura, "alarme": core.alarme, "porta": core.porta})


@app.route("/temperatura", methods=["POST"])
def mudar_temperatura():
    dados = request.get_json()
    core.temperatura = dados["temperatura"]
    return jsonify({"ok": True})


@app.route("/alarme", methods=["POST"])
def mudar_alarme():
    dados = request.get_json()
    core.alarme = dados["alarme"]
    return jsonify({"ok": True})


@app.route("/porta", methods=["POST"])
def mudar_porta():
    dados = request.get_json()
    core.porta = dados["porta"]
    return jsonify({"ok": True})


app.run(port=5000)
