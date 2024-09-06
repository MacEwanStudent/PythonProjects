import pandas as pd
class DataManager:
    def __init__(self, date: str, price: float):
        self.__data = {date: price}
        self.__all_data = {}
        self.__load_file()
        self.__save_file()

    def __load_file(self):
        try:
            df = pd.read_csv('item_price.csv')
            self.__all_data = df.set_index('DATE').to_dict()['PRICE']
        except FileNotFoundError:
            self.__all_data = {}


        self.__all_data.update(self.__data)

    def __save_file(self):

        # Convert the dictionary into a pandas DataFrame
        df = pd.DataFrame(list(self.__all_data.items()), columns=["DATE", "PRICE"])

        # Save the DataFrame to a CSV file
        df.to_csv("item_price.csv", index=False)