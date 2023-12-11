import os

class FileHelper:

    def __init__(self, file_name):
        if (os.path.exists("coins.txt") == False):
            with open('coins.txt', 'x'):
                pass
        self.my_file = open('coins.txt')
    
    def get_coins_info(self):
        self.texts = self.my_file.read()
        text_split = self.texts.split()
        return text_split

    def write(self, coin_name, coin_symbol, coin_price):
        with open('coins.txt', 'a') as myfile:
            coin_name = coin_name.replace(" ", "")
            myfile.write(coin_name + " " + coin_symbol + " " + str(coin_price) + "\n")