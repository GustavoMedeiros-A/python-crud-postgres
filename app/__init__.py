from flask_migrate import Migrate
from typing import Any, Mapping as TypingMapping, Optional

from flask import Flask

migrate = Migrate()


def create_app(test_config: Optional[TypingMapping[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5441/project_electro"


    if test_config is not None:
        app.config.from_mapping(test_config)

    from .db import db

    db.init_app(app)
    migrate.init_app(app, db)


    from .controllers import (
        user_controller
    )

    app.register_blueprint(user_controller.blueprint)


    return app
