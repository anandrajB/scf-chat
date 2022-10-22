from flask import jsonify, render_template, Blueprint, request
from flask_cors import cross_origin
from bson.objectid import ObjectId
from main_app.error_handler import BadReqError, NotFoundError
from ..utils import splitting_string
from ..middleware import connect_db

db = connect_db().finflo_chat

config_bp = Blueprint('config_bp', __name__, url_prefix='/config')


@config_bp.route('/create_config', methods=['POST'])
@cross_origin('*')
def create_config():

    config = db.config

    data = request.json

    try:
        current_conf = None

        try:
            current_conf = config.find_one({'domain_url': data['domain_url']})

            xpaths = {
                'label': data['label'],
                'xpath': data['xpath']
            }

            config.update_one({'_id': current_conf['_id']}, {
                              '$push': {'xpath': xpaths}})

            print('Updated')

            return {'Status': 'Success', 'Message': 'Xpath inserted successfully'}

        except Exception:

            current_conf = None
    except Exception:

        raise NotFoundError("Configuration not found", status_code=404)

    try:
        if not current_conf:

            current_conf = config.insert_one(
                {'domain_url': data['domain_url'], 'xpath': []})

            xpaths = {
                'label': data['label'],
                'xpath': data['xpath']
            }

            config.update_one({'_id': current_conf.inserted_id}, {
                              '$push': {'xpath': xpaths}})

            print('Updated')

            return {"Status": 'Success', "Message": "The configuration is created and xpath is inserted successfully"}

    except Exception:

        raise BadReqError(
            'Configuration is not created, Check the values', status_code=400)

    return jsonify({"Status": "Successfully created configuration"})


@config_bp.route('/get_config')
@cross_origin('*')
def get_config():

    config = db.config

    args = request.args
    domain_url = args.get('domain_url')

    conf = None

    try:

        conf = config.find_one({'domain_url': domain_url})

        data = {
            '_id': str(conf['_id']),
            'Domain_URL': conf['domain_url'],
            'xpath': conf['xpath']
        }

        return jsonify(data), 200
    except:

        raise NotFoundError("Domain not found", status_code=404)
