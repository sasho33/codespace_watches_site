from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


db=SQLAlchemy()


def create_app():
      # initializing the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fiuvnrovmGVrivjrmivmrivmrivr454545imifm'
    # initializing the data base
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    db.init_app(app)

    # now for registering the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    
    #  for creating database
    # from .models import User
    from . import models
    from .models import User

    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
