from flask import render_template, Blueprint, request

index_bp = Blueprint('index_bp', __name__, url_prefix='/home')


@index_bp.route('/')
def index():
    return render_template('index.html')
