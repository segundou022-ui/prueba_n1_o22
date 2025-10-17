from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask desplegado correctamente en Render 🚀"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("📩 Datos recibidos:", data)
    return jsonify({"status": "ok", "received": data}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
