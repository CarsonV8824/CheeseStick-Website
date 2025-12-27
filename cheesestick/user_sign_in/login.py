from flask_login import LoginManager
from src.main import app
from src.user_sign_in.user import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)