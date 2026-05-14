from flask import Blueprint, jsonify, request
from database.db import get_connection
from datetime import datetime

attendance_bp = Blueprint("attendance", __name__)

# GET ATTENDANCE
@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():

    conn = get_connection()

    attendance = conn.execute("""
        SELECT attendance.id,
               users.name,
               users.surname,
               attendance.status,
               attendance.created_at
        FROM attendance
        JOIN users ON attendance.student_id = users.id
    """).fetchall()

    conn.close()

    return jsonify([dict(row) for row in attendance])


# CREATE ATTENDANCE
@attendance_bp.route("/attendance", methods=["POST"])
def create_attendance():

    data = request.json

    conn = get_connection()

    conn.execute("""
        INSERT INTO attendance
        (student_id, lesson_id, status, created_by, created_at)
        VALUES (?, ?, ?, ?, ?)
    """,
    (
        data["student_id"],
        data["lesson_id"],
        data["status"],
        data["created_by"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Attendance added"}), 201