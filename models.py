from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))

    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))


class SchoolClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    class_id = db.Column(db.Integer, db.ForeignKey("school_class.id"))


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    class_id = db.Column(db.Integer, db.ForeignKey("school_class.id"))


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    day = db.Column(db.String(20))
    hour = db.Column(db.String(20))

    class_id = db.Column(db.Integer, db.ForeignKey("school_class.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    lesson_id = db.Column(db.Integer, db.ForeignKey("lesson.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    present = db.Column(db.Boolean, default=False)