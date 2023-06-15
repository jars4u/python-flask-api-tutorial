from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{ "label": "Mi primera tarea", "done": False }]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'










# ESTAS LINEAS SIEMPRE AL FINAL:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
