from flask import Flask, request, render_template, redirect
from string import ascii_lowercase

app = Flask(__name__)


def rotate(text, shift):
    alphabet = ascii_lowercase
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, new_alphabet)
    return text.translate(table)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        kind = request.args.get("hash")
        if kind is None:
            return render_template("main.html")
        if rotate(kind, -3) == "granted":
            return render_template("flag.html")
        else:
            return render_template("fail.html")
    else: # request.method == "POST"
        return redirect("/rotalive/?hash={}".format(rotate("denied", 3)))


if __name__ == '__main__':
    app.run()
