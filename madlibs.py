from random import choice

from flask import Flask, render_template, request, redirect, session



# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

app.secret_key = "rainy sunday"

@app.route('/')
def play_game():
    """Initiate game radio button"""

    return render_template("index.html")

@app.route("/choice",methods=["POST"])
def choice():

    shouldplay = request.form.get("play")

    if shouldplay == "yes":
        return redirect("/game")
    else:
        return redirect("/goodbye")

@app.route("/goodbye")
def goodbye():
    return render_template("goodbye.html")


@app.route("/game")
def game():

    propernoun = session["proper_noun"]
    noun = session["noun"]
    verb = session["verb"]
    adjective = session["adjective"]
    adverb = session["adverb"]
    exclamation = session["exclamation"]

    return render_template("game.html", testdata=session, propernoun=propernoun, noun=noun, verb=verb, adjective=adjective, adverb=adverb, exclamation=exclamation)

    #    start_game = request.args.get("play")
    #

    #if start_game == "No":
    #return render_template("goodbye.html")

@app.route('/game_add', methods=["POST"])
def game_add():
    # I HAVE TO FIGURE OUT HOW TO GET NAME INTO THIS FUNCTION MANY MAKING NAME IN EACH BUTTON WHICH BUTTON IS BEING HIT
    print request.form
    word_type_list = request.form.get("name")
    if word_type_list != "done":

        word_type = request.form.get("name")
        session[word_type] = session.get(word_type, [])

        if word_type == "proper_noun":
            propernoun_value = request.form.get("proper_noun")
            session[word_type].append(propernoun_value)
        if word_type == "noun":
            noun_value = request.form.get("noun")
            session[word_type].append(noun_value)
        if word_type =="verb":
            verb_value = request.form.get("verb")
            session[word_type].append(verb_value)
        if word_type == "adjective":
            adjective_value = request.form.get("adjective")
            session[word_type].append(adjective_value)
        if word_type == "adverb" :
            adverb_value = request.form.get("adverb")
            session[word_type].append(adverb_value)
        if word_type == "exclamation" :
            exclamation_value = request.form.get("exclamation")
            session[word_type].append(exclamation_value)
        return redirect("/game" )
    else:
        return redirect('/choose_story')


@app.route('/choose_story')
def choose_story():
    story_dictionary = { "/show_story/axe_murder" : "Axe Murder"}
    
    return render_template("choose_story.html", story_dictionary=story_dictionary)

@app.route('/show_story/<story_name>')
def show_story(story_name):

    if story_name == "axe_murder":
       noun1 = choice(session["noun"])
       

       noun2 = choice(session["noun"])
    return render_template(story_name + ".html")





if __name__ =='__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
