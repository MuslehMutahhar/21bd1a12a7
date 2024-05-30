# app/routes.py
from flask import Blueprint, request, jsonify
import requests
from uuid import uuid4
import config

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register_company():
    data = {
        "companyName": "goMart",
        "ownerName": "Rahul",
        "rollNo": "1",
        "ownerEmail": "rahul@abc.edu",
        "accessCode": "FKDLjg"
    }
    response = requests.post(config.REGISTER_URL, json=data)
    return jsonify(response.json())

@main.route('/auth', methods=['POST'])
def get_auth_token():
    data = request.get_json()
    response = requests.post(config.AUTH_URL, json=data)
    return jsonify(response.json())


