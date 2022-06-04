import requests
from bs4 import BeautifulSoup

# ___This class is used to extract the songs from Bill board website, and create a list called song_names.___ #
# ___ Bill board is the website used___ #
# ___ Beautiful soup library is used for scraping the data___ #


class SongsList:

    def __init__(self):
        self.song_names = None
        self.billboard_hot100 = None
        self.song_names_spans = None
        self.soup = None
        self.year = None
        self.response = None

    def song_generator(self):
        self.year = input("What year do you want to visit? Type year in yyyy-mm-dd format: ")
        self.response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{self.year}/")
        self.billboard_hot100 = self.response.text
        self.soup = BeautifulSoup(self.billboard_hot100, "html.parser")
        self.song_names_spans = self.soup.find_all("h3", class_="a-no-trucate")
        self.song_names = [song.getText().strip("\t\n") for song in self.song_names_spans]
        return self.song_names