import time
from tqdm import tqdm


from VK import VkPhotos
from Yandex import YaUploader

with open("token.txt", "r") as file_object:
    vk_token = file_object.read().strip()


def main():
    token = input("Введите токен Яндекс.Диска: ")
    owner_id = input("Введите VK id: ")
    photo_count = int(input("Введите количество фотографий: "))
    path_to_folder = input("Введите имя папки на Яндекс.Диске: ")
    vk_version = 5.131
    user_vk = VkPhotos(vk_token, vk_version, owner_id, photo_count)
    uploader = YaUploader(token)
    uploader.get_folder(path_to_folder)
    max_p = user_vk.parse_size_photo()
    prog_bar = tqdm(total=len(max_p))
    for keys, values in max_p.items():
        photo_url = values
        disk_file_path = f"/{path_to_folder}/{keys}"
        uploader.get_link_to_disk(disk_file_path)
        uploader.upload_files_to_disk(disk_file_path, photo_url)
        time.sleep(0.5)
        prog_bar.update(1)
    prog_bar.close()
    user_vk.get_photo_json()


if __name__ == "__main__":

    main()