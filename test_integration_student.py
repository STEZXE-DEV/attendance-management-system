import unittest
from app import app
from models import db, User, Student, SchoolClass


class StudentTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["WTF_CSRF_ENABLED"] = False

        self.client = app.test_client()

        with app.app_context():
            db.create_all()

            c = SchoolClass(name="1A")
            db.session.add(c)
            db.session.commit()

            st = Student(name="Jan", class_id=c.id)
            db.session.add(st)
            db.session.commit()

            u = User(username="u1", password="u1", role="student")
            db.session.add(u)
            db.session.commit()

            u.student_id = st.id
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.rollback()
            db.session.remove()
            db.drop_all()

    def login_student(self):
        return self.client.post(
            "/login",
            data={"username": "u1", "password": "u1"},
            follow_redirects=True
        )

    def test_student_panel(self):
        self.login_student()

        response = self.client.get("/student", follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Jan", response.data)

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()


if __name__ == "__main__":
    unittest.main()