from flask import Flask, render_template, request, redirect, session
from functools import wraps

from models import db, User, Student, Teacher, SchoolClass, Subject, Lesson, Attendance

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret"

db.init_app(app)


# ---------------- AUTH ----------------
def login_required(f):
    @wraps(f)
    def w(*a, **k):
        if "user_id" not in session:
            return redirect("/login")
        return f(*a, **k)
    return w


def role_required(role):
    def d(f):
        @wraps(f)
        def w(*a, **k):
            if session.get("role") != role:
                return redirect("/login")
            return f(*a, **k)
        return w
    return d


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    if "role" not in session:
        return redirect("/login")
    return redirect(f"/{session['role']}")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if u:
            session["user_id"] = u.id
            session["role"] = u.role
            return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ---------------- ADMIN ----------------
@app.route("/admin")
@login_required
@role_required("admin")
def admin():
    return render_template(
        "admin.html",
        classes=SchoolClass.query.all(),
        students=Student.query.all(),
        teachers=Teacher.query.all(),
        subjects=Subject.query.all(),
        lessons=Lesson.query.all()
    )

@app.route("/admin/add_lesson", methods=["POST"])
@login_required
@role_required("admin")
def add_lesson():
    db.session.add(Lesson(
        day=request.form["day"],
        hour=request.form["hour"],
        class_id=request.form["class_id"],
        teacher_id=request.form["teacher_id"],
        subject_id=request.form["subject_id"]
    ))
    db.session.commit()
    return redirect("/admin")

@app.route("/admin/delete_lesson/<int:id>")
@login_required
@role_required("admin")
def delete_lesson(id):
    db.session.delete(Lesson.query.get(id))
    db.session.commit()
    return redirect("/admin")

@app.route("/admin/add_class", methods=["POST"])
@login_required
@role_required("admin")
def add_class():
    db.session.add(SchoolClass(name=request.form["name"]))
    db.session.commit()
    return redirect("/admin")


@app.route("/admin/delete_class/<int:id>")
@login_required
@role_required("admin")
def del_class(id):
    db.session.delete(SchoolClass.query.get(id))
    db.session.commit()
    return redirect("/admin")


@app.route("/admin/add_student", methods=["POST"])
@login_required
@role_required("admin")
def add_student():
    db.session.add(Student(
        name=request.form["name"],
        class_id=request.form["class_id"]
    ))
    db.session.commit()
    return redirect("/admin")


@app.route("/admin/delete_student/<int:id>")
@login_required
@role_required("admin")
def del_student(id):
    db.session.delete(Student.query.get(id))
    db.session.commit()
    return redirect("/admin")


# ---------------- TEACHER ----------------
@app.route("/teacher")
@login_required
@role_required("teacher")
def teacher():
    u = User.query.get(session["user_id"])
    t = Teacher.query.get(u.teacher_id)

    return render_template(
        "teacher.html",
        lessons=Lesson.query.filter_by(teacher_id=t.id).all()
    )


@app.route("/lesson/<int:id>")
@login_required
@role_required("teacher")
def lesson(id):
    l = Lesson.query.get(id)

    students = Student.query.filter_by(class_id=l.class_id).all()

    att = Attendance.query.filter_by(lesson_id=id).all()
    att_map = {a.student_id: a.present for a in att}

    return render_template(
        "lesson.html",
        lesson=l,
        students=students,
        att_map=att_map
    )


@app.route("/mark/<int:lid>/<int:sid>/<int:v>")
@login_required
@role_required("teacher")
def mark(lid, sid, v):

    r = Attendance.query.filter_by(
        lesson_id=lid,
        student_id=sid
    ).first()

    if not r:
        r = Attendance(lesson_id=lid, student_id=sid)

    r.present = bool(v)

    db.session.add(r)
    db.session.commit()

    return redirect(f"/lesson/{lid}")


# ---------------- STUDENT (NAPRAWIONE) ----------------
@app.route("/student")
@login_required
@role_required("student")
def student():
    u = User.query.get(session["user_id"])
    s = Student.query.get(u.student_id)

    records = (
        db.session.query(Attendance, Lesson, Subject)
        .join(Lesson, Attendance.lesson_id == Lesson.id)
        .join(Subject, Lesson.subject_id == Subject.id)
        .filter(Attendance.student_id == s.id)
        .all()
    )

    return render_template(
        "student.html",
        student=s,
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)