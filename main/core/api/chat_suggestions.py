from flask import (
    jsonify,
    Blueprint,
    request
)
from bson.objectid import ObjectId
from flask_cors import cross_origin
from ..middleware import connect_db
import re
import random
from ..status import Base_Values


# db connection 
db = connect_db().finflo_chat

# blueprint
chat_helper = Blueprint('services', __name__, url_prefix='/services')


# API endpoint
@chat_helper.route('/')
@cross_origin('*')
def chat_messager():

    chat_datas = db.services
    # query_parms_Data = request.args.get('data')
    # regx = re.compile(query_parms_Data, re.IGNORECASE)
    # if query_parms_Data:
    #     try:
    # odm code updated
    #         base_query = chat_datas.find_one({'Keyword': query_parms_Data})
    #         return { "status": Base_Values.SUCCESS.value , "data" : random.choice(base_query['Answer'])}, 200
    #     except:
    #         return { "status": Base_Values.FAILURE.value , "data" : Base_Values.UTGD.value }, 200
    # else:
    #     print("goes herer")
    #     base_query = chat_datas.find_one({'Keyword': "START_CHAT"})
    #     return { "status": Base_Values.SUCCESS.value , "data" : base_query['Answer']}, 200

    base_query = chat_datas.find_one({'_id': ObjectId('6366608c7c5ad613990b8aa9')})
    print(base_query)
    return { "status": Base_Values.SUCCESS.value}, 200

