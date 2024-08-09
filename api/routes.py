from flask import Blueprint, jsonify, request, current_app
from services.api_service import get_user_ids, get_event_ids, get_event_and_user_image, post_data
from models.face_recognition import process_event_data
from services.task_queue import add_task
import base64
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/wholetrigger', methods=['GET'])
def whole_trigger():
    add_task(process_whole_trigger)
    return jsonify({"message": "wholetrigger function added to queue successfully."})

@api_bp.route('/singleuserimage/<EventId>/<UserId>', methods=['POST'])
def receive_data(EventId, UserId):
    data = request.get_json() if request.is_json else {}
    data['EventId'] = EventId
    data['UserId'] = UserId
    
    add_task(process_single_user_image, data)
    return 'Success: single user checking with event data has been queued'

def process_whole_trigger():
    # admin_ids = get_admin_ids()
    # if admin_ids:
    #     for admin_id in admin_ids:
    # event_ids = get_event_ids()
    # print("evet_id",event_id)
    # if event_ids:
    #     for event_id in event_ids:
    #         user_ids=get_user_ids(event_id)
    #         print("user_id",user_ids)
    #         if user_ids:
    #             for user_id in user_ids:
                    user_id=1
                    event_id=1
                    data = get_event_and_user_image(user_id, event_id)
                    print("data",data)
                    if data:
                        processed_data = process_event_data(data)
                        post_data(processed_data)

def process_single_user_image(data):
    api_url = f"{current_app.config['API_URL']}/getAllEventFolderAndOneUseImage/{data['UserId']}"
    headers = {"Content-Type": "application/json"}
    response = get_event_and_user_image(api_url, headers, {"eventId": data['EventId']})
    
    if response:
        processed_data = process_event_data(response)
        post_data(processed_data)