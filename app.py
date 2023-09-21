from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5441/project_electro"
    api = Api(app)

    from controllers import UserController
    app.register_blueprint(UserController.blueprint)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    return app


create_app()
