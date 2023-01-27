from flask import (
    jsonify,
    render_template,
    Blueprint,
    request
)
from flask_cors import cross_origin
from bson.objectid import ObjectId
from ...utils.error_handler import BadReqError, NotFoundError
from ..split import splitting_string
from ..middleware import connect_db

db = connect_db().finflo_chat

count_bp = Blueprint('count_bp', __name__, url_prefix='/count')



# COUNT THE UNREAD MESSAGES

@count_bp.route('/count_msgs')
@cross_origin('*')
def count_unread_msgs():

    conversation = db.conversation

    config_id = request.args.get('config_id')

    data = []

    for conv in conversation.find({'config_id': config_id}):

        data.extend(msgs for msgs in conv['message'] if msgs['is_read'] == False)
   
    return {"unread_msgs": len(data)}




# UPDATE THE MESSAGE is_reade STATUS ( TRUE / FALSE )

@ count_bp.route('/update_read', methods=['GET', 'POST'])
@ cross_origin('*')
def update_read_status():

    conversation = db.conversation

    if request.method == 'POST':

        data = request.json

        try:

            current_conv = conversation.find_one(
                {'config_id': data['config_id'], 'members': data['members']})

            conversation.update_one({'_id': ObjectId(current_conv['_id']), "message.is_read": False},
                                    {"$set": {"message.$[].is_read": data['is_read']}}, upsert=False)

    
        except Exception as e:
            raise NotFoundError("Can't able to find the conversation", status_code=404) from e

    return {
        "Message": "The message was read by the user",
        "Status": "Success"
    }
