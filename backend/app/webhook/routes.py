from flask import Blueprint, json, request, jsonify
from app.extensions import insert_event, get_all_events
from app.webhook.utils.receiver_helper import extract_event_from_response

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    event = extract_event_from_response(request.json)
    insert_event(event)
    return "Success"

@webhook.route("/event/all", methods=["POST"])
def get_all_event_route():
    events = get_all_events()
    return jsonify(events)

@webhook.route("/event/insert", methods=["POST"])
def insert_event_route():
    data = request.json
    event = insert_event(data)
    return jsonify(event)