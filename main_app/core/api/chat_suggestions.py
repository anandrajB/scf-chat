from flask import jsonify, Blueprint, request
from flask_cors import cross_origin
from ..middleware import connect_db

db = connect_db().finflo_chat

chat_helper = Blueprint('services', __name__, url_prefix='/services')


@chat_helper.route('/')
@cross_origin('*')
def count_unread_msgs():

    chat_datas = db.services
    

    config_id = request.args.get('data')

    # data = []
    # print(chatter_helper.find_one())
    # data = {
    #         'Domain_URL': conf['keyword'],
    #         'xpath': conf['answer']
    #     }   
    print(chat_datas.find_one())


    # for conv in conversation.find({'config_id': config_id}):

    #     for msgs in conv['message']:

    #         if msgs['is_read'] == False:

    #             data.append(msgs)

    # print(len(data))
    return {"vanakkam": config_id}
    
