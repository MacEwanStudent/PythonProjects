from datetime import datetime
from bs4 import BeautifulSoup
import requests
class BillboardSongs:
    def __init__(self, date = "2024-08-30"):
        '''The constructor takes a date in the format YYYY-MM-DD, if no date is specified,
        it will automatically set the date variable to todays date
        :param date: Date for specific week of desired top 100 billboard songs
        '''
        # The website is hard coded into the class because the BillboadSong Class
        # uses web Scraping to get the information of the top 100 songs,
        # Websites use different html tags layouts and different class/id naming.
        self.__billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date}/"
        self.__song_info = []
        self.__get_top_songs()

    def __get_top_songs(self):
        response = requests.get(self.__billboard_endpoint)
        yc_web_page = response.text
        # For the next steps, it is required to view the source html on the target website
        # to identify the tags and class/id naming containing the desired information.
        # In this case, the desired data are Songs names and Artists names.
        soup = BeautifulSoup(yc_web_page, "html.parser")
        songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

        song_titles = [song.find("h3").text.strip() for song in songs]
        song_artist = [song.find(name="li", class_="lrv-u-width-100p").find("span").text.strip() for song in songs]

        self.__song_info = [[x, y] for x, y in zip(song_titles, song_artist)]

    def get_songs_info(self):
        return self.__song_info

