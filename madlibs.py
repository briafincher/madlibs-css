"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("home.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    print dir(request)

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """lets user input madlib words"""

    game_on = request.args.get("game")

    return render_template("game.html", game_on=game_on)

    # if answer:
    #     return render_template("game.html")
    # else:
    #     return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """uses inputs in madlib"""

    char1 = request.args.get("char1")
    char2 = request.args.get("char2")
    char3 = request.args.get("char3")
    char4 = request.args.get("char4")
    char5 = request.args.get("char5")
    char6 = request.args.get("char6")
    place = request.args.get("place")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    adjective4 = request.args.get("adjective4")
    group = request.args.get("group")
    verb = request.args.get("verb")
    physical_trait = request.args.get("physical_trait")
    noun = request.args.get("noun")

    return render_template("madlib.html",
                        char1=char1,
                        char2=char2,
                        char3=char3,
                        char4=char4,
                        char5=char5,
                        char6=char6,
                        place=place,
                        adjective1=adjective1,
                        adjective2=adjective2,
                        adjective3=adjective3,
                        adjective4=adjective4,
                        group=group,
                        verb=verb,
                        physical_trait=physical_trait,
                        noun=noun)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
