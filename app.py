from flask import Flask
from flask import render_template

from routes.users import users_bp
from routes.attendance import attendance_bp
from routes.student import student_bp
from routes.teacher import teacher_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)

@app.route("/")
def home():
    return "Attendance System API"


@app.route("/student/<int:student_id>")
def student_panel(student_id):
    return render_template("student.html", student_id=student_id)


if __name__ == "__main__":
    app.run(debug=True)