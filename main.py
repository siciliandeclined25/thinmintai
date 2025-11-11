import gpt4all
from flask import Flask, render_template, request

# create flask app object
app = Flask(__name__)

from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # downloads / loads a 4.66GB LLM

ideaprompt = ""
extraprompt = ""


# set route for / AKA when the page is accessed
@app.route("/")
def main():
    return render_template("ai.html")


@app.route("/prompt", methods=["POST"])
def getPostRequest():
    a = model.generate(
        "Manipulate me and "
        + request.form["mani"]
        + " with the prompt:"
        + request.form["prompt"],
        max_tokens=100,
    )
    return a


if __name__ == "__main__":
    app.run(host="0.0.0.0")
