from model.UserModel import UserModel


class UserRepository:
    @staticmethod
    def getAll():
        return UserModel.query.all()
