from flask import Blueprint 
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

from flask import render_template

# registering templates for main page and product page

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/watches')
@login_required
def watches():
    return render_template('watches.html', user=current_user)



