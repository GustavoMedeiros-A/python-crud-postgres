from flask import Blueprint, jsonify, request, make_response
from ..utils import helpers

from ..service.user_service import UserService


blueprint = Blueprint('users', __name__)

@blueprint.post("/api/auth/login")
def authenticate():
    return helpers.auth()


@blueprint.post('/api/auth/logout')
def logout():
    # Create a response to clear cookies
    response = make_response(jsonify({'message': 'Logged out successfully'}))
    
    # Clear all cookies by setting them with an empty value and an immediate expiration
    cookies = request.cookies
    for cookie_name in cookies.keys():
        response.delete_cookie(cookie_name)
    
    return response


@blueprint.get("/api/users")
def getUser():
    users = UserService.getAllUsers()
    return jsonify(users), 200

@blueprint.post("/api/users")
@helpers.token_required
def postUser(current_user):
    user = request.get_json()
    return UserService.createUser(user)

@blueprint.delete('/api/users/<int:user_id>')
@helpers.token_required
def deleteUser(current_user, user_id):
    result = UserService.deleteUserById(user_id)
    if 'error' in result:
        return jsonify(result), 404  # Return a 404 status code for not found
    else:
        return jsonify(result), 200

@blueprint.put('/api/users/<int:user_id>')
@helpers.token_required
def updateUser(current_user, user_id):
    user_data = request.get_json()
    result = UserService.updateUserById(user_id, user_data)
    return result