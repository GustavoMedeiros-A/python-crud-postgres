from functools import wraps
from flask import request, jsonify, make_response
from ..repository.UserRepository import UserRepository
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from .config import SECRET_KEY
import jwt

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Invalid username or password"})
    
    user = UserRepository.get_user_by_name(auth.username)
    if not user:
        return jsonify({"message": "user not found"}), 401
    
    
    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({"username": user.name, "exp": datetime.now() + timedelta(hours=12)}, SECRET_KEY, algorithm="HS512")
        response = make_response(jsonify({"message": "Validated successfully", "user": {
            "name: ": user.name, "email: ": user.email
        }, 'token' : token, 'exp': datetime.now() + timedelta(hours=12)}))
        response.set_cookie('token', token, expires=datetime.now()  + timedelta(hours=12), domain='localhost', path='/')
        return response


    return jsonify({"message": "could not verify", "WWW-Authenticate": "Basic auth = 'Login Required"})
    
    

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("token")
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            print("TOKEN: " + token)
            print("SECRET_KEY: " + SECRET_KEY)
            data = jwt.decode(token, algorithms='HS512', verify=False, key=SECRET_KEY)
            current_user = UserRepository.get_user_by_name(data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)

    return decorated