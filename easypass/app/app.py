from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    login = request.form.get("login")
    password = request.form.get("password")
    error = None
    if login == "admin" and password == "qwerty":
        return render_template("flag.html")
    elif login is not None:
        error = "Login or password is not correct"
    return render_template("main.html", error=error)


if __name__ == '__main__':
    app.run()
