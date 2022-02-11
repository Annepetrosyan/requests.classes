import requests
import json
import threading
import os


class ImageThreading:

    def __init__(self, json_file):
        self.json_file = json_file

    def read(self):
        with open(json_file, "r") as file:
            data = json.load(file)
            data = dict(data)
            for key, value in data.items:
                self.key = key
                self.value = value


    def download_image(self):
        with open(f"{self.key}.jpeg", "wb") as photo:
            try:
                response = requests.get(self.value)
            except Exception as err:
                print(f"smth happened {err}")
            if response.status_code == 200:
                photo.write(response.content)
                print(f"image {self.key} is downloaded")

    def thread(self, a):
        thread_list = []
        for i in range(a):
            x = threading.Thread(target= download_image)
            thread_list.append(x)
            x.start()



json_file_1 = json_file = os.path.join(os.getcwd(), "json_1.json")
a = ImageThreading(json_file)
a.thread(4)

