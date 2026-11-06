from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({
        "message": "Hello World!",
        "status": "success"
    }), 200


@app.route("/api", methods=["GET"])
def api_info():
    return jsonify({
        "name": "Minha Flask API",
        "version": "1.0",
        "description": "Uma API RESTful desenvolvida com Flask"
    }), 200


@app.route("/api/hello", methods=["POST"])
def receive_message():

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({
            "error": "O campo 'name' é obrigatório"
        }), 400

    return jsonify({
        "message": f"Hello, {data['name']}!"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)