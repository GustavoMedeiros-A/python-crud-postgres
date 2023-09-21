from flask import Blueprint, jsonify, request
from service.UserService import UserService

blueprint = Blueprint('users', __name__)


@blueprint.get("/api/users")
def getUser():
    return UserService.getAllUsers()
