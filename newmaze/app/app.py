from flask import Flask, render_template
import string, random
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)
alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase


def generate():
    return ''.join([random.choice(alphabet) for _ in range(32)])
ARRAY = [generate() for _ in range(1024)]


@app.route('/')
def welcome():
    return render_template(
        "start.html",
        start=ARRAY[0]
    )


@app.route('/image/<image>')
def render_image(image):
    if image in ARRAY:
        pos = ARRAY.index(image)
        line = ARRAY[(pos+1) % len(ARRAY)]
        buffer = BytesIO()
        qrcode.make(line).save(buffer, format="PNG")
        context = {
            "image": base64.b64encode(buffer.getvalue()).decode()
        }
        if pos == len(ARRAY) - 1:
            context["flag"] = "uctf_new_qr_is_harder_than_old"
        return render_template("step.html", **context)
    else:
        return "Not found"


if __name__ == '__main__':
    app.run()
