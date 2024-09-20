from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def m_bold():
        content = function()
        result = f'<b>{content}</b>'
        return result
    return m_bold

def make_emphasized(function):
    def m_em():
        content = function()
        result = f'<em>{content}</em>'
        return result
    return m_em

def make_underline(function):
    def m_und():
        content = function()
        result = f'<u>{content}</u>'
        return result
    return m_und

@app.route("/")
@make_bold
@make_emphasized
@make_underline
def hello_world():
    return '<p>This is a paragraph</p>'
           # '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWJibnB3cHQ2OGlpZGkwaHllYXNuc3BvNGZ1ZXE1YWJqMDEzMnF5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SXPwY2Uvhd38Y/giphy.webp">'
@app.route("/<name>/<int:number>")
def greet(name, number):
    return(f"Hello {name} you are  {number} years old")

if __name__ == "__main__":
    app.run(debug=True) # debug=True


