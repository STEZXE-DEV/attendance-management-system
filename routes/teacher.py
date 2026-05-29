from flask import Blueprint, render_template
from flask_login import login_required

teacher_bp = Blueprint("teacher", __name__)

@login_required
@teacher_bp.route("/teacher/<int:teacher_id>")

@teacher_bp.route("/teacher/<int:teacher_id>")
def teacher_panel(teacher_id):
    return render_template("teacher.html", teacher_id=teacher_id)
