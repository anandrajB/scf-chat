from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from .error_handler import BadReqError, NotFoundError
from flask_socketio import SocketIO



################################
#   1.1 CORE CONFIGURATIONS    #
################################

load_dotenv()

app = Flask(__name__,  template_folder='./core/templates')

app.debug = True

socketio = SocketIO(app, cors_allowed_origins='*')

CORS(app)


## 1.2 importing functions for app registry's
# important : import this functions once after the environ is loaded check 1.1

from .core.api import (
    config_app,
    conversation,
    count,
    index,
    chat_suggestions
)



app.register_blueprint(index.index_bp)
app.register_blueprint(config_app.config_bp)
app.register_blueprint(conversation.conversation_bp)
app.register_blueprint(count.count_bp)
app.register_blueprint(chat_suggestions.chat_helper)


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
