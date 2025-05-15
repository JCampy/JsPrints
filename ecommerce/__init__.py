from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()

def create_FlaskApp():
    app = Flask(__name__) # Setting flask app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # IDK need for some reason
    UPLOAD_FOLDER = 'static/UPLOAD_FOLDER/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.static_folder = 'static' # make sure static folder can be accessed for css and images

    # SQLAlchemy database address
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) # initializing database with current flask app

    # importing routes.py and authenticaton.py
    from .routes import routes
    from .authentication import authentication
    
    # registers the blueprint so we can access the routes 
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    # import database tables
    from .db_models import User, Cart, Product, Shipping, Payment, Purchase_history
    
    # creating the database if it doesn't exist
    with app.app_context():
        db.create_all()

    # Tracking which user is currently logged in
    login_manager = LoginManager() # assigning variable with loginManager
    login_manager.login_view = 'authentication.login' # Setting the view to authentication.py @route /login
    login_manager.init_app(app) # initializing login manager with app

    # loading the current user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # finds current user by primary key after logging in

    return app


