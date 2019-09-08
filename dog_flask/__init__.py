from flask import Flask

from dog_flask.extensions import db, migrate
from dog_flask.routes import main


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app
