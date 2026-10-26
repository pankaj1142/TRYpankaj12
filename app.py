
from flask import Flask, render_template, request, redirect, session
import os
import secrets

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

# Demo login credentials
USERNAME = "pankaj"
PASSWORD = "12345"


@app.route("/")
def home():
    if session.get("logged_in"):
        return render_template("Login.html", logged_in=True, error=None)

    return render_template("Login.html", logged_in=False, error=None)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return redirect("/")

    return render_template(
        "Login.html",
        logged_in=False,
        error="Invalid username or password!"
    ), 401


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
