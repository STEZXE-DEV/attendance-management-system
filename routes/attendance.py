from flask import Blueprint, jsonify, request
from models import Attendance
from db import db
from datetime import datetime

attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():

    attendance = Attendance.query.all()

    return jsonify([
        {
            "id": row.id,
            "student_id": row.student_id,
            "lesson_id": row.lesson_id,
            "status": row.status
        }
        for row in attendance
    ])


@attendance_bp.route("/attendance", methods=["POST"])
def create_attendance():

    data = request.get_json()

    attendance = Attendance(
        student_id=data["student_id"],
        lesson_id=data["lesson_id"],
        status=data["status"],
        created_by=data["created_by"],
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    db.session.add(attendance)
    db.session.commit()

    return jsonify({"message": "Attendance added"}), 201
