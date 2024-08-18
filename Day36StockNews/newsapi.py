import requests
from mylib.myinfo import MyInfo


class NewsAPI:
    def __init__(self, date_from, date_to, topic="Tesla Inc", articles = 3):
        self.__url= "https://newsapi.org/v2/everything"
        self.__my_keys = MyInfo()
        self.__apikey = self.__my_keys.get_info("NewsApi","NEWS_API_KEY")
        self.__params = {
            "apiKey": self.__apikey,
            "q": topic,
            "from" : date_from,
            "to": date_to,
            "sortBy": "popularity",
            "pageSize": "3",
            "language": "en"
        }
        self.__data = {'status': 'ok', 'totalResults': 135, 'articles': [{'source': {'id': 'business-insider', 'name': 'Business Insider'}, 'author': 'Kwan Wei Kevin Tan', 'title': 'The core crew that helped Sam Altman start OpenAI has dwindled from 10 to 2', 'description': 'The ChatGPT maker has seen multiple top-level exits in recent months.', 'url': 'https://www.businessinsider.com/crew-of-10-helped-sam-altman-found-openai-dwindled-2-2024-8', 'urlToImage': 'https://i.insider.com/66b1879ea5247369a3e9a5ca?width=1200&format=jpeg', 'publishedAt': '2024-08-06T03:59:35Z', 'content': "Elon Musk, Sam Altman, and Greg Brockman were part of OpenAI's 11 founding members. Musk left the company's board in 2018. On Monday, OpenAI confirmed that its president, Brockman has taken an extend… [+5003 chars]"}, {'source': {'id': None, 'name': '9to5Mac'}, 'author': 'Ben Lovejoy', 'title': 'AAPL stock fell 10% after Warren Buffett sell-off, but investors shouldn’t panic', 'description': 'AAPL stock fell 10% at market opening this morning, to less than $200. It followed weekend filings by Warren Buffett’s Berkshire Hathaway, disclosing that the conglomerate had reduced its holding by half.\n\n\n\nThe reason for the sell-off isn’t clear, but commen…', 'url': 'https://9to5mac.com/2024/08/05/aapl-stock-fell-after-buffett-sell-off/', 'urlToImage': 'https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2024/08/AAPL-stock-fell.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1', 'publishedAt': '2024-08-05T13:31:57Z', 'content': 'AAPL stock fell 10% at market opening this morning, to less than $200. It followed weekend filings by Warren Buffett’s Berkshire Hathaway, disclosing that the conglomerate had reduced its holding by … [+3150 chars]'}, {'source': {'id': None, 'name': 'WOODTV.com'}, 'author': 'Susan Samples', 'title': 'Video of road rage slap prompts assault charge against unapologetic driver', 'description': 'A Grand Rapids woman is facing a misdemeanor assault charge after she slapped a woman in another car in a road rage incident on July 13.', 'url': 'https://www.woodtv.com/news/target-8/video-of-road-rage-slap-prompts-assault-charge-against-unapologetic-driver/', 'urlToImage': 'https://media.zenfs.com/en/wood_articles_694/1787b84a3ae43645801f989e7eaed0d8', 'publishedAt': '2024-08-03T00:29:22Z', 'content': 'GRAND RAPIDS, Mich. (WOOD) A Grand Rapids woman is facing a misdemeanor assault charge after she slapped a woman in another car in a road rage incident on July 13.\r\nThe confrontation was caught on ca… [+8160 chars]'}]}

    def get_news(self):
        response = requests.get(self.__url, self.__params)
        self.__data = response.json()
        print(self.__data)

    def get_articles(self):
        my_list = [[item["title"], item["description"]] for item in self.__data["articles"]]
        return my_list


