from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    role = db.Column(db.String(20), nullable=False)


class ClassGroup(db.Model):

    __tablename__ = "class_groups"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)


class Lesson(db.Model):

    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)

    class_id = db.Column(
        db.Integer,
        db.ForeignKey("class_groups.id")
    )

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    topic = db.Column(db.String(200))
    lesson_date = db.Column(db.String(50))


class Attendance(db.Model):

    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    lesson_id = db.Column(
        db.Integer,
        db.ForeignKey("lessons.id")
    )

    status = db.Column(db.String(20))

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(db.String(100))