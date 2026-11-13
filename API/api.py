from flask import Flask, jsonify, request
import core

app = Flask(__name__)

# Mostrar estado da casa
@app.route("/estado", methods=["GET"])
def estado():
    return jsonify({
        "temperatura": core.temperatura,
        "alarme": core.alarme,
        "porta": core.porta
    })


@app.route("/temperatura", methods=["POST"])
def temperatura():
    dados = request.get_json()
    core.temperatura = dados["temperatura"]
    return jsonify({"ok": True})


@app.route("/alarme", methods=["POST"])
def alarme():
    dados = request.get_json()
    core.alarme = dados["alarme"]
    return jsonify({"ok": True})


@app.route("/porta", methods=["POST"])
def porta():
    dados = request.get_json()
    core.porta = dados["porta"]
    return jsonify({"ok": True})


app.run(port=5000)
