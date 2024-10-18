from operator import index

from flask import Flask, render_template
from werkzeug.datastructures.range import Range

from data_manager import DataManager

# blog_manager= DataManager()
# blog_data= blog_manager.get_data()
app = Flask(__name__)

blog_data=[{'id': 1, 'body': 'Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.', 'title': 'The Life of Cactus', 'subtitle': 'Who knew that cacti lived such interesting lives.', 'image_url': 'https://i1.wp.com/blog.plantdelights.com/wp-content/uploads/2015/08/Ferocactus-wislizeni-A3AZ-028-in-flower.jpg'}, {'id': 2, 'body': 'Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.', 'title': 'Top 15 Things to do When You are Bored', 'subtitle': "Are you bored? Don't know what to do? Try these top 15 activities.", 'image_url': 'https://c2.staticflickr.com/4/3026/2838434910_d770a0bb94_z.jpg?zz=1'}, {'id': 3, 'body': 'Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.', 'title': 'Introduction to Intermittent Fasting', 'subtitle': 'Learn about the newest health craze.', 'image_url': 'https://dinnerthendessert.com/wp-content/uploads/2019/11/Fruit-Cake-Muffins-16x9.jpg'}]

@app.route("/")
def home():
    return render_template('index.html', data= blog_data)

@app.route("/about")
def about(name=None):
    return render_template('about.html')

@app.route("/contact")
def contact(name=None):
    return render_template('contact.html')

@app.route("/post/<int:blog_id>")
def post(blog_id):
    view_post = [dict for dict in blog_data if dict["id"]==blog_id][0]
    return render_template('post.html', blog_data = view_post)


if __name__ == "__main__":

    app.run(debug=True)

