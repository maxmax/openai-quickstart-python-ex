import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify

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

@app.route("/completion", methods=("GET", "POST"))
def completion():
    if request.method == "POST":
        completion = request.form["completion"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=completion,
            temperature=0.6,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        return redirect(url_for("completion", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("completion.html", result=result)

@app.route("/outputcode", methods=("GET", "POST"))
def outputcode():
    if request.method == "POST":
        outputcodeData = request.form["outputcode"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=outputcodeData,
            temperature=0.6,
            max_tokens=800,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        return redirect(url_for("outputcode", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("outputcode.html", result=result)

@app.route("/embeddings", methods=("GET", "POST"))
def embeddings():
    app.logger.info('testing info EMBEDDINGS log 1')
    if request.method == "POST":
        embeddingsData = request.form["embeddings"]
        app.logger.info('testing info EMBEDDINGS log 2', embeddingsData)
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            max_tokens=1000,
            input=embeddingsData,
        )
        app.logger.info('testing info EMBEDDINGS log 2', response)
        return redirect(url_for("embeddings", result=response.data[0].embedding))

    result = request.args.get("result")
    return render_template("embeddings.html", result=result)


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

@app.route('/api', methods=['GET'])
def api():
    data = [
        {
            "id": 0
        },
        {
            "id": 1
        }
    ]
    return jsonify(data)

@app.route("/examples")
def examples():
    return render_template("examples.html")
