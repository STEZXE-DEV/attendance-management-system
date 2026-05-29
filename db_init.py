from app import app
from models import db, User, Student, Teacher, SchoolClass, Subject, Lesson


def init_db():
    with app.app_context():

        # tworzy tabele jeśli nie istnieją
        db.create_all()

        if User.query.first():
            print("DB już zainicjalizowana")
            return

        # ---------------- KLASY ----------------
        c1 = SchoolClass(name="1A")
        c2 = SchoolClass(name="2B")
        db.session.add_all([c1, c2])
        db.session.commit()

        # ---------------- PRZEDMIOTY ----------------
        subjects = [
            Subject(name="Matematyka"),
            Subject(name="Polski"),
            Subject(name="Biologia"),
            Subject(name="Fizyka"),
            Subject(name="WF"),
            Subject(name="Historia"),
            Subject(name="Informatyka"),
        ]
        db.session.add_all(subjects)
        db.session.commit()

        # ---------------- NAUCZYCIELE ----------------
        t1 = Teacher(name="Anna", class_id=c1.id)
        t2 = Teacher(name="Jan", class_id=c2.id)
        db.session.add_all([t1, t2])
        db.session.commit()

        # ---------------- UCZNIOWIE ----------------
        s1 = Student(name="Adam", class_id=c1.id)
        s2 = Student(name="Kasia", class_id=c1.id)
        s3 = Student(name="Piotr", class_id=c2.id)
        db.session.add_all([s1, s2, s3])
        db.session.commit()

        # ---------------- USERZY ----------------
        admin = User(username="admin", password="admin", role="admin")

        u1 = User(username="t1", password="t1", role="teacher", teacher_id=t1.id)
        u2 = User(username="t2", password="t2", role="teacher", teacher_id=t2.id)

        u3 = User(username="s1", password="s1", role="student", student_id=s1.id)
        u4 = User(username="s2", password="s2", role="student", student_id=s2.id)

        db.session.add_all([admin, u1, u2, u3, u4])
        db.session.commit()

        # ---------------- LEKCJE ----------------
        l1 = Lesson(day="Pon", hour="08:00", class_id=c1.id, teacher_id=t1.id, subject_id=subjects[0].id)
        l2 = Lesson(day="Pon", hour="09:00", class_id=c1.id, teacher_id=t1.id, subject_id=subjects[1].id)

        db.session.add_all([l1, l2])
        db.session.commit()

        print("DB zainicjalizowana ✔")


if __name__ == "__main__":
    init_db()