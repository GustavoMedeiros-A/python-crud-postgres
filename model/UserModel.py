from ..app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None
    
    @classmethod
    def find_by_id(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        if user:
            return user
        return None
    
    @classmethod
    def create(cls, name, email, password):
        new_user = cls(name=name, email=email, password=password)  
        db.session.add(new_user)
        db.session.commit()
        return new_user


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    