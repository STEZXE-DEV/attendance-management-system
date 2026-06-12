import unittest
from app import app
from models import db, User, Student, Teacher, SchoolClass, Subject, Lesson, Attendance


class AttendanceTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["WTF_CSRF_ENABLED"] = False

        self.client = app.test_client()

        with app.app_context():
            db.create_all()

            # users
            admin = User(username="admin", password="admin", role="admin")
            teacher_user = User(username="t1", password="t1", role="teacher")

            db.session.add_all([admin, teacher_user])
            db.session.commit()

            # teacher
            t = Teacher(name="Nowak")
            db.session.add(t)
            db.session.commit()

            teacher_user.teacher_id = t.id
            db.session.commit()

            # class
            c = SchoolClass(name="1A")
            db.session.add(c)
            db.session.commit()

            # subject
            s = Subject(name="Math")
            db.session.add(s)
            db.session.commit()

            # student
            st = Student(name="Jan", class_id=c.id)
            db.session.add(st)
            db.session.commit()

            # lesson
            lesson = Lesson(
                day="Mon",
                hour="10",
                class_id=c.id,
                teacher_id=t.id,
                subject_id=s.id
            )
            db.session.add(lesson)
            db.session.commit()

            self.lesson_id = lesson.id
            self.student_id = st.id

    def tearDown(self):
        with app.app_context():
            db.session.rollback()
            db.session.remove()
            db.drop_all()

    def login_teacher(self):
        return self.client.post(
            "/login",
            data={"username": "t1", "password": "t1"},
            follow_redirects=True
        )

    def test_mark_attendance(self):
        self.login_teacher()

        self.client.get(
            f"/mark/{self.lesson_id}/{self.student_id}/1",
            follow_redirects=True
        )

        with app.app_context():
            a = Attendance.query.filter_by(
                lesson_id=self.lesson_id,
                student_id=self.student_id
            ).first()

            self.assertIsNotNone(a)
            self.assertTrue(a.present)

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

if __name__ == "__main__":
    unittest.main()