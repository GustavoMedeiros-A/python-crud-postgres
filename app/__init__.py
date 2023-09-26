from flask_migrate import Migrate
from typing import Any, Mapping, Optional

from flask import Flask

migrate = Migrate()


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5441/project_electro"


    if test_config is not None:
        app.config.from_mapping(test_config)

    from .db import db

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.debug = True

    from .controllers import (
        UserController
    )

    app.register_blueprint(UserController.blueprint)


    return app