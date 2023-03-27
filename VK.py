import requests
import time
import json


class VkPhotos:
    url = "http://api.vk.com/method/"

    def __init__(self, vk_token: str, version: float, owner_id, count):
        self.params = {"access_token": vk_token,
                       "v": version,
                       "owner_id": owner_id,
                       "count": count}

    def search_photo_profile(self):
        search_photo_url = self.url + "photos.get"
        photo_params = {"album_id": "profile",
                        "extended": 1,
                        "feed_type": "likes",
                        "photo_sizes": 1}
        req = requests.get(search_photo_url, params={**self.params, **photo_params}).json()
        return req["response"]["items"]

    def parse_size_photo(self):
        photos = self.search_photo_profile()
        max_size = {(str(items["likes"]["count"]) + "_" + time.strftime('%Y-%m-%d', time.gmtime(items["date"]))):
                    items["sizes"][-1]["url"] for items in photos}
        print(max_size)
        return max_size

    def get_photo_json(self):
        all_photos = self.search_photo_profile()
        photos_list = []
        for items in all_photos:
            photos_dict = {
                "file_name": (str(items['likes']['count']) + "_" + time.strftime('%Y-%m-%d', time.gmtime(items["date"]))+'.jpg'),
                "size": items['sizes'][-1]['type'], "url": items['sizes'][-1]['url']}
            photos_list.append(photos_dict)
        import_photos = json.dumps(photos_list, indent=4)
        with open("import_photos.json", "w") as file:
            file.write(import_photos)
        print('Информация о фото записана в import_photos.json')