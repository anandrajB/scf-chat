from flask import jsonify, Blueprint, request
from flask_cors import cross_origin
from bson.objectid import ObjectId
from main_app.error_handler import BadReqError, NotFoundError
from ..utils import splitting_string
from ..middleware import connect_db
from main_app import socketio


db = connect_db().finflo_chat

conversation_bp = Blueprint('conversation_bp', __name__, url_prefix='/conv')


@conversation_bp.route('/conversation', methods=['GET', 'POST'])
@cross_origin('*')
def conversation():

    conversation = db.conversation

    if request.method == 'POST':
        data = request.json

        try:

            current_conv = None

            try:

                current_conv = conversation.find_one(
                    {'config_id': data['config_id'], 'members': data['members']})

                message = {'text': data['text'],
                           'time': datetime.datetime.utcnow(),
                           'sender': data['sender'],
                           'is_read': data['is_read']}

                conversation.update_one(
                    {'_id': ObjectId(current_conv['_id'])}, {'$push': {'message': message}})

                print('updated')

            except Exception as e:
                current_conv = None

            try:
                # users = splitting_string(members)

                if not current_conv:

                    current_conv = conversation.find_one(
                        {'config_id': data['config_id'], 'members': data['members']})

                    message = {'text': data['text'],
                               'time': datetime.datetime.utcnow(),
                               'sender': data['sender'],
                               'is_read': data['is_read']}

                    conversation.update_one(
                        {'_id': ObjectId(current_conv['_id'])}, {'$push': {'message': message}})

                print('updated')
            except Exception as e:

                current_conv = None
        except Exception as e:
            raise NotFoundError(
                'Conversation between users not found', status_code=404)

        try:
            # 2. If no conversation, create new one

            if not current_conv:

                if len(data['members']) >= 2 and data['party'] is not None:

                    current_conv = conversation.insert_one(
                        {'config_id': data['config_id'], 'members': data['members'], 'party': data['party'],
                         'subject': data['subject'], 'message': []})

                    message = {'text': data['text'],
                               'time': datetime.datetime.utcnow(),
                               'sender': data['sender'],
                               'is_read': data['is_read']}

                    conversation.update_one(
                        {'_id': ObjectId(current_conv.inserted_id)}, {'$push': {'message': message}})

                else:

                    return {"Status": "Failure", "Message": "You have to select members to initiate a chat."}, 400

        except Exception as e:
            raise BadReqError(
                "Cannot able to create a conversation", status_code=400)

    return {"Status": "Success"}


@conversation_bp.route('/msgs')
@cross_origin('*')
def messages():

    conversation = db.conversation

    args = request.args

    members = args.get('members')
    config_id = args.get('config_id')

    try:

        users = splitting_string(members)

        current_conv = conversation.find_one(
            {'config_id': config_id, 'members': users})

        data = {
            "message": current_conv['message'],
            "subject": current_conv['subject'],
        }

        return jsonify(data), 200

    except Exception as e:

        return NotFoundError("Conversation not found", status_code=404)


@conversation_bp.route('/convo_list')
@cross_origin('*')
def get_convos():
    conversation = db.conversation

    args = request.args

    user = args.get('user')
    config_id = args.get('config')

    final_data = []

    for conv in conversation.find({'config_id': config_id, "members": user}):

        count_unread_msgs = []

        for msgs in conv['message']:

            if msgs["is_read"] == False:

                count_unread_msgs.append(msgs)
            else:
                count_unread_msgs = []

        data = {
            'members': conv['members'],
            'party': conv['party'],
            'message': conv['message'],
            'unread_msgs': len(count_unread_msgs)
        }

        final_data.append(data)

    return jsonify(final_data), 200


@socketio.on('messages')
def conversation():

    conversation = db.conversation

    if request.method == 'POST':
        data = request.json

        try:

            current_conv = None

            try:

                current_conv = conversation.find_one(
                    {'config_id': data['config_id'], 'members': data['members']})

                message = {'text': data['text'],
                           'time': datetime.datetime.utcnow(),
                           'sender': data['sender'],
                           'is_read': data['is_read']}

                conversation.update_one(
                    {'_id': ObjectId(current_conv['_id'])}, {'$push': {'message': message}})

                print('updated')

            except Exception as e:
                current_conv = None

            try:
                # users = splitting_string(members)

                if not current_conv:

                    current_conv = conversation.find_one(
                        {'config_id': data['config_id'], 'members': data['members']})

                    message = {'text': data['text'],
                               'time': datetime.datetime.utcnow(),
                               'sender': data['sender'],
                               'is_read': data['is_read']}

                    conversation.update_one(
                        {'_id': ObjectId(current_conv['_id'])}, {'$push': {'message': message}})

                print('updated')
            except Exception as e:

                current_conv = None
        except Exception as e:
            raise NotFoundError(
                'Conversation between users not found', status_code=404)

        try:
            # 2. If no conversation, create new one

            if not current_conv:

                if len(data['members']) >= 2 and data['party'] is not None:

                    current_conv = conversation.insert_one(
                        {'config_id': data['config_id'], 'members': data['members'], 'party': data['party'],
                         'subject': data['subject'], 'message': []})

                    message = {'text': data['text'],
                               'time': datetime.datetime.utcnow(),
                               'sender': data['sender'],
                               'is_read': data['is_read']}

                    conversation.update_one(
                        {'_id': ObjectId(current_conv.inserted_id)}, {'$push': {'message': message}})

                else:

                    return {"Status": "Failure", "Message": "You have to select members to initiate a chat."}, 400

        except Exception as e:
            raise BadReqError(
                "Cannot able to create a conversation", status_code=400)

    return {"Status": "Success"}
