from flask import Blueprint, render_template

teacher_bp = Blueprint("teacher", __name__)


@teacher_bp.route("/teacher/<int:teacher_id>")
def teacher_panel(teacher_id):
    return render_template("teacher.html", teacher_id=teacher_id)
