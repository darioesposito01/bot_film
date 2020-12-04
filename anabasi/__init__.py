from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db,render_as_batch=True)
    else:
        migrate.init_app(app, db)

from anabasi import models, routs

