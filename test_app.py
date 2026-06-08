import unittest

from app import app
from models import db, User


class FlaskTestCase(unittest.TestCase):

    def setUp(self):

        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

        self.app = app.test_client()

        with app.app_context():
            db.create_all()

            admin = User(
                username="admin",
                password="admin",
                role="admin"
            )

            db.session.add(admin)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    # ---------------- TEST LOGOWANIA ----------------
    def test_login(self):

        response = self.app.post(
            "/login",
            data={
                "username": "admin",
                "password": "admin"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

    # ---------------- TEST BLOKADY ----------------
    def test_admin_requires_login(self):

        response = self.app.get("/admin")

        self.assertEqual(response.status_code, 302)

    # ---------------- TEST STRONY LOGIN ----------------
    def test_login_page(self):

        response = self.app.get("/login")

        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()