from flask import Blueprint, jsonify
from models import Attendance, Lesson

student_bp = Blueprint("student", __name__)


@student_bp.route("/api/student/<int:student_id>/attendance")
def student_attendance(student_id):

    attendance = Attendance.query.filter_by(
        student_id=student_id
    ).all()

    result = []

    for row in attendance:

        lesson = Lesson.query.get(row.lesson_id)

        result.append({
            "topic": lesson.topic,
            "lesson_date": lesson.lesson_date,
            "status": row.status
        })

    return jsonify(result)