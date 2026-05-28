from flask import Flask, render_template
from db import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    import models
    db.create_all()

from routes.users import users_bp
from routes.student import student_bp
from routes.teacher import teacher_bp
from routes.attendance import attendance_bp

app.register_blueprint(users_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(attendance_bp)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
