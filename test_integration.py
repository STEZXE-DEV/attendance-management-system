import unittest

from app import app
from models import db, User, SchoolClass


class IntegrationTest(unittest.TestCase):

    def setUp(self):

        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

        self.client = app.test_client()

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

    # ---------------- LOGIN + ADMIN ----------------
    def test_login_and_open_admin_panel(self):

        response = self.client.post(
            "/login",
            data={
                "username": "admin",
                "password": "admin"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.get("/admin")

        self.assertEqual(response.status_code, 200)

    # ---------------- DODAWANIE KLASY ----------------
    def test_add_class(self):

        # login
        self.client.post(
            "/login",
            data={
                "username": "admin",
                "password": "admin"
            }
        )

        # dodanie klasy
        self.client.post(
            "/admin/add_class",
            data={
                "name": "3C"
            },
            follow_redirects=True
        )

        with app.app_context():

            c = SchoolClass.query.filter_by(name="3C").first()

            self.assertIsNotNone(c)

    # ---------------- BLOKADA ADMINA ----------------
    def test_admin_requires_login(self):

        response = self.client.get("/admin")

        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()