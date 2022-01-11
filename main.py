import requests

class Temperature:
    def __init__(self, url="http://54.235.226.52:4000/temp/"):
        self.infos = "Class for connection to the MariaDB"
        self.url = url

    def select(self):
        response = requests.get(self.url)
        return response.json()
    def insert(self, data):
        response = requests.get(self.url+"select")
        return response.json()

if __name__ == '__main__':
    temp = Temperature()
    print(temp.select())
