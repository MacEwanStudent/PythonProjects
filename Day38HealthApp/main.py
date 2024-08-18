from nutritionix import Nutrionix
from gsheets import GSheets
from datetime import datetime

new_item = Nutrionix()
my_test= GSheets()


def get_query():
    user_input = input("Tell me which exercises you did today: ")
    new_item.set_query(user_input)
    new_item.post_request()


def build_body():
    data = new_item.get_data()
    update_info = [[item['name'], item['duration_min'], item['nf_calories']] for item in data['exercises']]
    print(update_info)

    day = datetime.today()
    day = day.strftime("%d/%m/%Y")
    current_time = datetime.now().strftime('%H:%M:%S')
    print(day, current_time)
    for index in range(len(update_info)):
        new_row = ([day,current_time] + update_info[index])

        print(new_row)
        my_test.set_row(new_row)
        my_test.update_sheet()

    return

# get_query()
# build_body()



