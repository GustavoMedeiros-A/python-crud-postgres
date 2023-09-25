from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5441/project_electro"

    migrate.init_app(app, db)
    db.init_app(app)
    
    app.debug = True

    from .controllers import UserController
    app.register_blueprint(UserController.blueprint)

    return app


if __name__ == "__main__":
    create_app().run()
