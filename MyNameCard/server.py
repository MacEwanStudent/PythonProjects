from flask import Flask, render_template
from random import randint

app = Flask(__name__)
correct = 3


def make_bold(function):
    def m_bold():
        content = function()
        result = f'<b>{content}</b>'
        return result
    return m_bold


@app.route("/")
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) # debug=True

