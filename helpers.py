from flask import request, jsonify
from repository.UserRepository import UserRepository
from werkzeug.security import check_password_hash


def auth():
    auth = request.authorization
    if not auth or not auth.name or not auth.password:
        return jsonify({"message": "Invalid username or password"})
    
    user = UserRepository.get_user_by_name(auth.name)
    if not user:
        return jsonify({"message": "user not found"}), 401
    
    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode()
    
    
