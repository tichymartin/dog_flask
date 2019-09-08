from flask import Flask
from flask_admin.contrib.sqla import ModelView

from dog_flask.extensions import db, migrate, admin
from dog_flask.routes import main
from dog_flask.models import Post


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    admin.add_view(ModelView(Post, db.session))
    app.register_blueprint(main)

    return app
