from flask import Flask, jsonify
import core

app = Flask(__name__)

@app.route("/estado", methods=["GET"])
def pegar_estado():
    return jsonify({"temperatura": core.temperatura, "alarme": core.alarme, "porta": core.porta})

if __name__ == "__main__":
    app.run(port=5000)