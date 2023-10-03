from ..repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash


class UserService:
    @staticmethod
    def getAllUsers():
        return UserRepository.getAll()
    
    @staticmethod
    def createUser(data):
        verify_user_email = UserRepository.find_by_email(data['email'])
        if(verify_user_email):
            return {"message": "User cannot be created"}, 400
        
        name = data['name']
        email = data["email"]
        password = data["password"]
        pass_hash = generate_password_hash(password)
        
        return UserRepository.postUser(name, email, pass_hash)
    
    @staticmethod
    def deleteUserById(user_id):
        return UserRepository.deleteUserById(user_id)
    
    @staticmethod
    def updateUserById(user_id, user_data):
        return UserRepository.updateUserById(user_id, user_data)