import unittest
from app import app
from models import db, User, SchoolClass, Student
import gc


class AdminCRUDTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["WTF_CSRF_ENABLED"] = False

        self.client = app.test_client()

        with app.app_context():
            db.create_all()

            admin = User(username="admin", password="admin", role="admin")
            db.session.add(admin)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.rollback()
            db.session.remove()
            db.drop_all()

    def login(self):
        return self.client.post(
            "/login",
            data={"username": "admin", "password": "admin"},
            follow_redirects=True
        )

    # ---------------- CREATE CLASS ----------------
    def test_create_class(self):
        self.login()

        self.client.post(
            "/admin/add_class",
            data={"name": "3A"},
            follow_redirects=True
        )

        with app.app_context():
            c = SchoolClass.query.filter_by(name="3A").first()
            self.assertIsNotNone(c)

    # ---------------- DELETE CLASS ----------------
    def test_delete_class(self):
        self.login()

        with app.app_context():
            c = SchoolClass(name="3B")
            db.session.add(c)
            db.session.commit()
            cid = c.id

        self.client.get(
            f"/admin/delete_class/{cid}",
            follow_redirects=True
        )

        with app.app_context():
            c = db.session.get(SchoolClass, cid)
            self.assertIsNone(c)

    # ---------------- CREATE STUDENT ----------------
    def test_create_student(self):
        self.login()

        with app.app_context():
            c = SchoolClass(name="1A")
            db.session.add(c)
            db.session.commit()
            cid = c.id

        self.client.post(
            "/admin/add_student",
            data={
                "name": "Jan",
                "class_id": cid
            },
            follow_redirects=True
        )

        with app.app_context():
            s = Student.query.filter_by(name="Jan").first()
            self.assertIsNotNone(s)

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()
        gc.collect()

if __name__ == "__main__":
    unittest.main()