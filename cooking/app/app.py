from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def page():
    data = request.cookies.get("is_staff")
    if data == "b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b":
        response = make_response(render_template("flag.html"))
    else:
        response = make_response(render_template("main.html"))
    if data is None:
        response.set_cookie("is_staff", "fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa")
    return response



if __name__ == '__main__':
    app.run()
