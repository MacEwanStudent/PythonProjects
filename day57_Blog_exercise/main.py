from flask import Flask, render_template
from datetime import datetime
from api_manager import ApiManager

app = Flask(__name__)
blog_info = ApiManager()

def get_date():
    # Get today's date
    today = datetime.now()
    current_year = today.year
    return current_year


@app.route('/')
def home():
    return render_template("index.html",blogs=blog_info.get_blogs())
@app.route('/<num>')
def get_blog(num):
    return render_template("post.html", blog=blog_info.get_blog(num))


if __name__ == "__main__":
    app.run(debug=True)
