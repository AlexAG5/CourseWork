import requests
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
vk_token = config["VK"]["vk_token"]
token = config["Yandex"]["token"]
version = 5.131
user_id = input("Введите краткое имя или VK ID: ")


def get_owner_id():
    url = "http://api.vk.com/method/"
    get_id_url = url + "users.get"
    params = {"access_token": vk_token,
              "v": version,
              "user_ids": user_id}
    req = requests.get(get_id_url, params=params).json()
    vk_id = req["response"][0]["id"]
    return vk_id