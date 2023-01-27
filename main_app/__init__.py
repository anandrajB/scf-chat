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
# app.config['SECRET_KEY'] = 'finflo!#Vcws2deproduction!#!!WS'
app.debug = True


# if os.environ.get('FLASK_ENV') == 'production':
#     origins = [
#         'http://go-concord.herokuapp.com',
#         'https://go-concord.herokuapp.com',
#     ]
# else:
#     origins = "*"


# SOCKET INITIALIZATION
socketio = SocketIO(app , cors_allowed_origins = "*")

## 1.2 importing functions for app registry's
# important : import this functions once after the environ is loaded check 1.1

from .core.api import (
    configuration,
    conversation,
    count,
    index,
    chat_suggestions
)



app.register_blueprint(index.index_bp)
app.register_blueprint(configuration.config_bp)
app.register_blueprint(conversation.conversation_bp)
app.register_blueprint(count.count_bp)
app.register_blueprint(chat_suggestions.chat_helper)
CORS(app)


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
