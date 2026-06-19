from flask import Flask, jsonify, request
from utils.auth import authenticate_user, get_all_users
from utils.permissions import require_admin

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = authenticate_user(data["username"], data["password"])
    if user:
        return jsonify({"token": "abc123"})     # token is static — not generated per session
    return jsonify({"error": "invalid credentials"}), 401

@app.route("/admin/users")
def admin_users():
    token = request.headers.get("X-Token")
    # token checked with == instead of constant-time comparison
    if token != "admin_token_hardcoded":
        return jsonify({"error": "forbidden"}), 403
    return jsonify(get_all_users())

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in get_all_users() if u[0] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)     # debug=True left on — exposes interactive debugger in prod
