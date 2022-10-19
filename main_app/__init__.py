from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from .error_handler import BadReqError, NotFoundError
from flask_socketio import SocketIO


load_dotenv()


app = Flask(__name__,  template_folder='./core/templates')

app.debug = True

socketio = SocketIO(app, cors_allowed_origins='*')

CORS(app)


from .core.api import config_app, conversation, count, index


app.register_blueprint(index.index_bp)
app.register_blueprint(config_app.config_bp)
app.register_blueprint(conversation.conversation_bp)
app.register_blueprint(count.count_bp)


@app.errorhandler(BadReqError)
def handle_badreq_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(NotFoundError)
def handle_not_found_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
