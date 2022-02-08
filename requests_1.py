import requests
import re
import json
import os


class A:
    def __init__(self, json_file_path, url_adress):
        self.json_file_path = json_file_path
        self.url_adress = url_adress
        with open(json_file_path, "r") as f:
            self.data = json.load(f)
            self.a = re.findall("https:.*?/python.png" and "https:.*?/image/jpeg", self.data)
            self._image_list = self.a

    def image_list(self):
        return self._image_list

    def jpj_dowload(self):
        self.download_list = re.findall("https:.*?/image/jpeg", self.data)
        for image in self.download_list:
            response = requests.get(image)
            return response





