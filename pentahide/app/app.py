from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def main_page():
    response = make_response(render_template("main.html"))
    response.headers["X-Flag"] = "uctflookforflagandyouwillwin"
    return response


if __name__ == '__main__':
    app.run()
