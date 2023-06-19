from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "Mi primera tarea", "done": False}]


@app.route('/health_check', methods=['GET'])
def health_check():
    return "OK"


@app.route('/todos', methods=['GET'])
def get_todos():
    json_todos = jsonify(todos)
    return json_todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return todos


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    for item in range(len(todos)):
        if item == position:

            todos.remove(todos[item])
    print("This is the position to delete: ",position)
    return todos



                



# ESTAS LINEAS SIEMPRE AL FINAL:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
