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
    import re
    regx = re.compile("^Can i know the limit amount", re.IGNORECASE)

    cs = chat_datas.find_one({'Keyword': regx})
    print(cs['Answer'])
   


    # print(conv)
    return {"vanakkam": config_id}
    
