from flask import Flask, request, jsonify

app = Flask(__name__)

# 存储 API 密钥和安全参数（实际数据）
api_keys = {
    "customer_1_api_key": {"token": "customer_1_secure_token", "param1": "customer1_value1", "param2": "customer1_value2"},
    "customer_2_api_key": {"token": "customer_2_secure_token", "param1": "customer2_value1", "param2": "customer2_value2"}
}

@app.route('/auth', methods=['POST'])
def authenticate():
    api_key = request.form.get('api_key')
    if api_key in api_keys:
        return jsonify({"token": api_keys[api_key]["token"]})
    else:
        return jsonify({"error": "Invalid API key"}), 401

@app.route('/get_params', methods=['POST'])
def get_params():
    token = request.form.get('token')
    for key, value in api_keys.items():
        if value["token"] == token:
            return jsonify({"param1": value["param1"], "param2": value["param2"]})
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
