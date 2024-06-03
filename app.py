from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/insert_membership', methods=['POST'])
def insert_membership():
    data = request.json
    print(f"Recibido: {data}")
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
    