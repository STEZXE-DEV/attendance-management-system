from flask import Blueprint, jsonify, request
from models import User
from db import db

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return jsonify([
        {
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ])


@users_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    user = User(
        name=data["name"],
        surname=data["surname"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201
