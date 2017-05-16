from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/api/monkey/')
def feed_monkey():
    food = request.args.get('food').lower().replace('-', ' ').replace('%20', ' ').replace('_', ' ')
    food_words = food.split(' ')
    if len(food_words) == 2 and food_words[1] == "bananas":
        try:
            banana_count = int(food_words[0])
            if banana_count >= 5:
                return "Very good, flag is uctfhungryanimalsknowflags"
            else:
                return "It's very few for me, I'm big monkey"
        except:
            return "Bananas? How many bananas?"
    elif food == "bananas":
        return "Bananas? How many bananas?"
    elif food in ["banana", "one banana", "a banana", "the banana"]:
        return "It's very few for me, I'm big monkey"
    else:
        return "I don't want to eat it"


@app.route('/')
def main_page():
    return render_template("main.html")


if __name__ == '__main__':
    app.run()
