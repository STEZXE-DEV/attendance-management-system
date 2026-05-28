from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import *

with app.app_context():
    db.create_all()

from routes.users import users_bp
from routes.student import student_bp
from routes.teacher import teacher_bp
from routes.attendance import attendance_bp

app.register_blueprint(users_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(attendance_bp)

with app.app_context():

    if User.query.count() == 0:

        admin = User(
            name="Admin",
            surname="System",
            email="admin@test.com",
            password="1234",
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)