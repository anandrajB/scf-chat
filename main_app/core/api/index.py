from flask import render_template, Blueprint, request

index_bp = Blueprint('index_bp', __name__, url_prefix='/')



# HOME PAGE 

@index_bp.route('/')
def index():
    return render_template('index.html')


# PROJECT AND API DESCRIPTION PAGE 

@index_bp.route('/description')
def description():
    return render_template('welcome.html')