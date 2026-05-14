from flask import Blueprint, jsonify, request
from database.db import get_connection

users_bp = Blueprint("users", __name__)

# GET ALL USERS
@users_bp.route("/users", methods=["GET"])
def get_users():

    conn = get_connection()

    users = conn.execute(
        "SELECT * FROM users"
    ).fetchall()

    conn.close()

    return jsonify([dict(user) for user in users])


# GET USER BY ID
@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    conn = get_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    conn.close()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(dict(user))


# CREATE USER
@users_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json(force=True)

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO users (name, surname, email, password, role)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data["name"],
            data["surname"],
            data["email"],
            data["password"],
            data["role"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User created"}), 201


# UPDATE USER
@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.json

    conn = get_connection()

    conn.execute(
        """
        UPDATE users
        SET name = ?, surname = ?, email = ?, role = ?
        WHERE id = ?
        """,
        (
            data["name"],
            data["surname"],
            data["email"],
            data["role"],
            user_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User updated"})


# DELETE USER
@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    conn = get_connection()

    conn.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User deleted"})