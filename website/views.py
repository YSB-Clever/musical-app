from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/beats')
def beats():        
    return render_template('beats.html', user=current_user)

@views.route('/background')
def background():        
    return render_template('background.html', user=current_user)