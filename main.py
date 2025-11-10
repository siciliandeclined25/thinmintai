from flask import Flask, render_template

# create flask app object
app = Flask(__name__)


# set route for / AKA when the page is accessed
@app.route("/")
def main():
    return render_template("ai.html")


if __name__ == "__main__":
    app.run()
