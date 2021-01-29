import os
import requests
import urllib.parse
import string

from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
#from googletrans import Translator
from google_trans_new import google_translator

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
    #return render_template("index.html")
    return redirect("/index")


@app.route("/index", methods=["GET", "POST"])
def convert():

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("text") or not request.form.get("customRadioInline1"):
            note = "lacking information!"
            return render_template("index.html", note=note)

        text = request.form.get("text")
        l = len(text)


        if request.form.get("customRadioInline1") == "F":

            if request.form.get("uppercase") == "u":
                letter = text.upper()

            elif request.form.get("lowercase") == "l":
                letter = text.lower()

        elif request.form.get("customRadioInline1") == "W":

            letter = list(text)
            letter.append(" ")

            if request.form.get("uppercase") == "u":
                for i in range(len(text)):
                    if letter[i].isalpha() == False and letter[i+1].isalpha() == True:
                        temp = letter[i+1]
                        letter[i+1] = temp.upper()
                for i in range(len(text)):
                    if letter[i].isalpha() == True:
                        temp = letter[i]
                        letter[i] = temp.upper()
                        break
                letter.pop(len(text))
                le = letter
                letter = "".join(le)

            elif request.form.get("lowercase") == "l":
                for i in range(len(text)):
                    if letter[i].isalpha() == False and letter[i+1].isalpha() == True:
                        temp = letter[i+1]
                        letter[i+1] = temp.lower()
                for i in range(len(text)):
                    if letter[i].isalpha() == True:
                        temp = letter[i]
                        letter[i] = temp.lower()
                        break
                letter.pop(len(text))
                le = letter
                letter = "".join(le)


        elif request.form.get("customRadioInline1") == "S":

            letter = list(text)
            letter.append(" ")

            if request.form.get("uppercase") == "u":
                for i in range(len(text)):
                    if letter[i] == "." or letter[i] == "!" or letter[i] == "?" or letter[i] == ";":
                        for j in range(len(text)-1-i):
                            if letter[i+j].isalpha() == True:
                                temp = letter[i+j]
                                letter[i+j] = temp.upper()
                                break
                for i in range(len(text)):
                    if letter[i].isalpha() == True:
                        temp = letter[i]
                        letter[i] = temp.upper()
                        break
                letter.pop(len(text))
                le = letter
                letter = "".join(le)

            elif request.form.get("lowercase") == "l":
                for i in range(len(text)):
                    if letter[i] == "." or letter[i] == "!" or letter[i] == "?" or letter[i] == ";":
                        for j in range(len(text)-1-i):
                            if letter[i+j].isalpha() == True:
                                temp = letter[i+j]
                                letter[i+j] = temp.lower()
                                break
                for i in range(len(text)):
                    if letter[i].isalpha() == True:
                        temp = letter[i]
                        letter[i] = temp.lower()
                        break
                letter.pop(len(text))
                le = letter
                letter = "".join(le)


        # Redirect user to home page
        return render_template("index.html", text=text, letter=letter)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        #return redirect("/")
        return render_template("index.html")




@app.route("/translator", methods=["GET", "POST"])
def translator():

    if request.method == "POST":

        if not request.form.get("post"):
            info = "please input your text!"
            return render_template("translator.html", info=info)

        post = request.form.get("post")
        #translator = Translator()
        translator = google_translator()
        #tran = translator.translate(text=post, src="fr", dest="en")
        tran = translator.translate(post, lang_tgt="en")
        #translated = translator.translate(text=input_text, src="english",dest=out_lang)

        return render_template("translator.html", post=post, tran=tran)

    else:
        #return redirect("/")
        return render_template("translator.html")

