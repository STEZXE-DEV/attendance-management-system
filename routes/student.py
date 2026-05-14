from flask import Blueprint, jsonify
from database.db import get_connection

student_bp = Blueprint("student", __name__)

@student_bp.route("/api/student/<int:student_id>/attendance")
def student_attendance(student_id):

    conn = get_connection()

    data = conn.execute("""
        SELECT 
            lessons.topic,
            lessons.lesson_date,
            attendance.status
        FROM attendance
        JOIN lessons ON attendance.lesson_id = lessons.id
        WHERE attendance.student_id = ?
        ORDER BY lessons.lesson_date DESC
    """, (student_id,)).fetchall()

    conn.close()

    return jsonify([dict(row) for row in data])