import datetime
class GetDate:
    def __init__(self):
    # Get today's date
        self.today = datetime.date.today()
        # Format the date as 'YYYY-MM-DD'
        self.formatted_today = self.today.strftime('%Y%m%d')
    def get_previous_day(self, day:int):
        '''Returns the date(YYYY-MM-DD) of days ago(as a positive integer),
        e.g day = 0 Returns today date
        e.g day= 1 Returns yesterday, day = 2 two days ago and so on...'''
        day = self.today - datetime.timedelta(days=day)
        day = day.strftime('%Y-%m-%d')
        return day

    def get_today_day(self):
        return self.formatted_today
