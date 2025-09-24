from flask import Flask, request, jsonify
from skippy_mind_entry import receive_input

app = Flask(__name__)

@app.route("/mind", methods=["POST"])
def mind_entry():
    payload = request.json
    result = receive_input(payload)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8088)
