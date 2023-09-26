from ..model.UserModel import UserModel
from flask import jsonify


class UserRepository:


    @staticmethod
    def getAll():
        users = UserModel.query.all()
        return [user.to_dict() for user in users]
    
    @staticmethod
    def find_by_email(email):
        return UserModel.find_by_email(email)
    
    
    @staticmethod
    def postUser(name, email, password):
        new_user  = UserModel.create(name, email, password)
        return jsonify({"message": "User created successfully", "user": {"name": new_user}}), 201


    @staticmethod
    def updateUserById(user_id, user_data):
        user = UserModel.query.get(user_id)
        
        if user:
            user.name = user_data.get('name', user.name)
            user.email = user_data.get('email', user.email)
            user.password = user_data.get('password', user.password)
            
            user.save() 
            
            return {"message": f"User {user.name} updated successfully"}
        else:
            return {"error": "User not found"}
        

    @staticmethod
    def get_user_by_name(username):
        try: 
            return UserModel.query.filter(UserModel.name == username).one()
        except:
            return None

    @staticmethod
    def deleteUserById(user_id):
        user = UserModel.find_by_id(user_id)
        UserModel.delete(user)
        return {"message": "User deleted successfully"}
    



