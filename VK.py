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
        url_list = []
        sorted_likes = []
        max_size = {}

        for items in photos:
            like = str(items["likes"]["count"])
            if like != like:
                sorted_likes.append(like)
            elif like == like in sorted_likes:
                like = str(items['likes']['count']) + "_" + time.strftime('%Y-%m-%d', time.gmtime(items["date"]))
            sorted_likes.append(like)

        for items in photos:
            url = str(items["sizes"][-1]["url"])
            url_list.append(url)

        for i in range(len(sorted_likes)):
            key = sorted_likes[i]
            value = url_list[i]
            max_size[key] = value
        return max_size

    def get_photo_json(self):
        all_photos = self.search_photo_profile()
        sorted_likes = []
        url_list = []
        size_list = []

        for items in all_photos:
            like = str(items["likes"]["count"])
            if like != like:
                sorted_likes.append(like)
            elif like == like in sorted_likes:
                like = str(items['likes']['count']) + "_" + time.strftime('%Y-%m-%d', time.gmtime(items["date"]))
            sorted_likes.append(like)

        for items in all_photos:
            url = str(items["sizes"][-1]["url"])
            url_list.append(url)

        for items in all_photos:
            size = items['sizes'][-1]['type']
            size_list.append(size)
        photos_names = {"names": list(map(lambda u: u, sorted_likes))}
        url_dict = {"url": list(map(lambda u: u, url_list))}
        size_dict = {"size": list(map(lambda u: u, size_list))}
        merged_dict = {**photos_names, **url_dict, **size_dict}
        photos_list = []

        for items in merged_dict:
            photos_dict = {
                "name": merged_dict.get('names'),
                "url": merged_dict.get('url'),
                "size": merged_dict.get('size')}
            photos_list.append(photos_dict)
        import_photos = json.dumps(merged_dict, indent=4)
        with open("import_photos.json", "w") as file:
            file.write(import_photos)
        print('Информация о фото записана в import_photos.json')