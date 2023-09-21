from repository.UserRepository import UserRepository


class UserService:
    @staticmethod
    def getAllUsers():
        return UserRepository.getAll()
