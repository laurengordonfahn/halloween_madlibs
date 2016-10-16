from random import choice

from flask import Flask, render_template, request, redirect


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def play_game():
    """Initiate game radio button"""

    start_game = request.args.get("play")
    
    if start_game == "No":
        return render_template("goodbye.html")
    else:
        return render_template("index.html")

@app.route('/game_add', methods=["POST"])
def game_add():
    # I HAVE TO FIGURE OUT HOW TO GET NAME INTO THIS FUNCTION MANY MAKING NAME IN EACH BUTTON WHICH BUTTON IS BEING HIT
    name = request.form.get("")
    session[name] = session[name].get(name, [])

    propernoun_value = request.form.get("proper_noun")
    session[name].append(propernoun_value)

    noun_value = request.form.get("noun")
    session[name].append(noun_value)


    verb_value = request.form.get("verb")
    session[name].append(verb_value)

    ajective_value = request.form.get("adjective")
    session[name].append(adjective_value)

    adverb_value = request.form.get("adverb")
    session[name].append(adverb_verb)


    return redirect("/game")


@app.route('/madlib')
def show_madlib():
    """Generate madlib story"""

    proper_noun = request.args.get("person")
    color = request.args.get("favorite_color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    return render_template('madlib.html',person=proper_noun,
                             favorite_color=color,
                             noun=noun,
                             adjective=adjective)



if __name__ =='__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
