from flask import request, jsonify
from ..model.UserModel import UserModel


class UserRepository:


    @staticmethod
    def getAll():
        users = UserModel.query.all()
        return [user.as_dict() for user in users]
    
    
    @staticmethod
    def postUser(user):
        verify_user_email = UserModel.find_by_email(user['email'])
        if(verify_user_email):
            return {"message": "User cannot be created"}, 400
        new_user  = UserModel.create(user['name'], user['email'], user['password'])
        return {"message": "User created successfully", "user": {"name": new_user.name, "email": new_user.email}}, 201


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
    



