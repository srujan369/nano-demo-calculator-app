from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first_number = data.get("first")
    second_number = data.get("second")
    
    if first_number is None or second_number is None:
        return jsonify({"error": "Both 'first' and 'second' numbers are required."}), 400
    
    try:
        result = first_number + second_number
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    first_number = data.get("first")
    second_number = data.get("second")
    
    if first_number is None or second_number is None:
        return jsonify({"error": "Both 'first' and 'second' numbers are required."}), 400
    
    try:
        result = first_number - second_number
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == '_main_':
    app.run(port=8080, host='0.0.0.0')
