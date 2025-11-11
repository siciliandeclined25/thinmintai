import gpt4all
from flask import Flask, render_template, request

# create flask app object
app = Flask(__name__)

from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # downloads / loads a 4.66GB LLM

ideaprompt = ""
extraprompt = ""
head = """<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>"""


# set route for / AKA when the page is accessed
@app.route("/")
def main():
    return render_template("ai.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/prompt", methods=["POST"])
def getPostRequest():
    a = model.generate(
        "(DONT INCLUDE YOUR THOUGHT PROCESS AT ALL) Manipulate me and "
        + request.form["mani"]
        + " with the prompt:"
        + request.form["prompt"],
        max_tokens=100,
    )
    return (
        head
        + "<h1>Response</h1><br><hr><code>"
        + a
        + "<br></code><a href='/'>Return back to prompt window</a><br>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
