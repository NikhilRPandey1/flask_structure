from flask import request, render_template
from .models import User
from ..extensions import db


def register():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        new_user = User(
            username=username,
            email=email,
            password_hash=password,
        )
        db.session.add(new_user)
        db.session.commit()

    # Your login logic here
    return render_template("register.html")
