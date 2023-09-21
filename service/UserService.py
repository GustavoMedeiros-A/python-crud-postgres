from repository.UserRepository import UserRepository


class UserService:
    @staticmethod
    def getAllUsers():
        return UserRepository.getAll()
    
    @staticmethod
    def createUser(data):
        return UserRepository.postUser(data)
    
    @staticmethod
    def deleteUserById(user_id):
        return UserRepository.deleteUserById(user_id)
    
    @staticmethod
    def updateUserById(user_id, user_data):
        return UserRepository.updateUserById(user_id, user_data)