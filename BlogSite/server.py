from flask import Flask, render_template
from datetime import datetime
from random import randint
from api_manager import ApiManager

app = Flask(__name__)
new_prediction= ApiManager('Donald')

def get_date():
    # Get today's date
    today = datetime.now()

    # Format the date as 'Month-day-year'
    #formatted_date = today.strftime("%B-%d-%Y")
    current_year=today.year

    return current_year

@app.route("/")
def home_page():
    random_number= randint(1,10)
    # current_date= get_date()
    year = get_date()
    return render_template("index.html",num= year, result=new_prediction.get_result())

if __name__ == '__main__':
    app.run(debug=True)