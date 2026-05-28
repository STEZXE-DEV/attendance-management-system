from flask import Blueprint, jsonify, request
from models import User
from app import db

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "role": user.role
        })

    return jsonify(result)


@users_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    new_user = User(
        name=data["name"],
        surname=data["surname"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created"
    }), 201