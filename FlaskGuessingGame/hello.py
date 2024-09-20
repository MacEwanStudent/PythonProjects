from flask import Flask
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
@make_bold
def Init_question(low=1, high=5):
    #correct= randint(low,high)
    #correct = 3
    return f'<p>Guess a Number from {low} - {high}</p>'


@app.route("/<int:number>")
def check_guess(number):
    global correct

    result = '<p>Wrong!</p>'
    if number == correct:
        result = ('<p>Correct!</p> '
                  '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWJibnB3cHQ2OGlpZGkwaHllYXNuc3BvNGZ1ZXE1YWJqMDEzMnF5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SXPwY2Uvhd38Y/giphy.webp">')
    elif number < correct:
        result = ('<p>Too Low!</p> '
                  '<img src="https://media3.giphy.com/media/TtA5uuykQL63FlVYEz/giphy.webp?cid=ecf05e47zhs3upbkw10tqr4roxrmt6cai7gwapu2m6a42jx7&ep=v1_gifs_related&rid=giphy.webp&ct=g">')
    else:
        result = ('<p>Too High!</p> '
                  '<img src="https://media2.giphy.com/media/l0HFjskY0wUSF35G8/200w.webp?cid=ecf05e47zhs3upbkw10tqr4roxrmt6cai7gwapu2m6a42jx7&ep=v1_gifs_related&rid=200w.webp&ct=g">')

    return result


if __name__ == "__main__":
    app.run(debug=True) # debug=True

