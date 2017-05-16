from flask import (Flask, request,
                   render_template)
import sys
import subprocess

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    response = None
    if request.form.get("ip"):
        try:
            result = subprocess.run(
                "ping -c 4 " + request.form.get("ip"),
                shell=True,
                timeout=10,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            response = result.stdout.decode("utf8")
        except Exception as e:
            response = "Unknown error was occured: {}".format(e)
    return render_template("main.html", response=response)


if __name__ == '__main__':
    app.run()
