import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

@app.route("/question", methods=("GET", "POST"))
def question():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.6,
        )
        return redirect(url_for("question", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("question.html", result=result)

@app.route("/image", methods=("GET", "POST"))
def image():
    if request.method == "POST":
        image = request.form["image"]
        response = openai.Image.create(
            prompt=image,
            n=1,
            size="1024x1024"
        )
        return redirect(url_for("image", result=response['data'][0]['url']))

    result = request.args.get("result")
    return render_template("image.html", result=result)

@app.route("/examples")
def examples():
    return render_template("examples.html")
