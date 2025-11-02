from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ip_push', methods=['POST'])
def ip_push():
    data = request.get_json()
    print("Pushed IP:", data)
    return jsonify({"status": "IP received"}), 200

@app.route('/api/domain_push', methods=['POST'])
def domain_push():
    data = request.get_json()
    print("Pushed Domain:", data)
    return jsonify({"status": "Domain received"}), 200

@app.route('/api/hash_push', methods=['POST'])
def hash_push():
    data = request.get_json()
    print("Pushed Hash:", data)
    return jsonify({"status": "Hash received"}), 200

@app.route('/api/ip_delete', methods=['POST'])
def ip_delete():
    data = request.get_json()
    print("Deleted IP:", data)
    return jsonify({"status": "IP deleted"}), 200

@app.route('/api/domain_delete', methods=['POST'])
def domain_delete():
    data = request.get_json()
    print("Deleted Domain:", data)
    return jsonify({"status": "Domain deleted"}), 200

@app.route('/api/hash_delete', methods=['POST'])
def hash_delete():
    data = request.get_json()
    print("Deleted Hash:", data)
    return jsonify({"status": "Hash deleted"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=80)  # Run on http://localhost/api/...
