from flask import jsonify, Blueprint, request
from flask_cors import cross_origin
from ..middleware import connect_db

db = connect_db().finflo_chat

chat_helper = Blueprint('services', __name__, url_prefix='/services')


@chat_helper.route('/')
@cross_origin('*')
def count_unread_msgs():

    chatter_helper = db.services
    

    config_id = request.args.get('data')

    # data = []

    # for conv in conversation.find({'config_id': config_id}):

    #     for msgs in conv['message']:

    #         if msgs['is_read'] == False:

    #             data.append(msgs)

    # print(len(data))
    return {"vanakkam": config_id}
    
