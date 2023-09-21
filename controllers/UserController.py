from flask import Blueprint, jsonify, request
from service.UserService import UserService

blueprint = Blueprint('users', __name__)


@blueprint.get("/api/users")
def getUser():
    users = UserService.getAllUsers()
    return jsonify(users)

@blueprint.post("/api/users")
def postUser():
    user = request.get_json()
    return UserService.createUser(user)

@blueprint.delete('/api/users/<int:user_id>')
def deleteUser(user_id):
    result = UserService.deleteUserById(user_id)
    if 'error' in result:
        return jsonify(result), 404  # Return a 404 status code for not found
    else:
        return jsonify(result), 200

@blueprint.put('/api/users/<int:user_id>')
def updateUser(user_id):
    user_data = request.get_json()
    result = UserService.updateUserById(user_id, user_data)
    return result