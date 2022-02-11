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


    def download_image(self, key, value):
        with open(f"{key}.jpeg", "wb") as photo:
            try:
                response = requests.get(value)
            except Exception as err:
                print(f"smth happened {err}")
            if response.status_code == 200:
                photo.write(response.content)
                print(f"image {key} is downloaded")

    def thread(self, a):
        for i in range(a):
            x = threading.Thread(target= download_image)
            thread_list.append(x)
            x.start()







json_file_1 = json_file = os.path.join(os.getcwd(), "json_1.json")
a = ImageThreading(json_file)
a.thread(4)

