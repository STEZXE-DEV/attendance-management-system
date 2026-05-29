from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            login_user(user)

            if user.role == "student":
                return redirect(f"/student/{user.id}")

            if user.role == "teacher":
                return redirect(f"/teacher/{user.id}")

            if user.role == "admin":
                return redirect("/")

        return "Wrong credentials"

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect("/login")