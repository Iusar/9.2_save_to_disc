import requests
import json

# Исходные данные

file_name = "Test1.docx"
test_file_path = 'C:\\Test\\' + file_name
current_token = 


class YaUploader:
    def __init__(self, file_path: str, token):
        self.target_path = "/" + file_name
        self.file_path = file_path
        self.token = token
        self.uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.params_for_get = {'path': self.target_path, 'overwrite': True}
        self.params_for_put = {'path': self.file_path}
        self.headers = {'Authorization': 'OAuth ' + self.token}

    # Получаем временную ссылку
    def get_load_url(self):
        get_link = requests.get(url=self.uri,
                                params=self.params_for_get,
                                headers=self.headers)

        if get_link.status_code == 200:
            link = get_link.json()
            return link
        else:
            print(f'Again error :( {get_link.status_code}')

    # Загружаем файл
    def upload(self):
        upload_link = self.get_load_url()
        use_link = requests.put(url=upload_link['href'],
                                params=self.params_for_put,
                                headers=self.headers)
        if use_link.status_code == 201:
            print('Файл успешно загружен!')
        else:
            print('Ошибка загрузки')
        pass


if __name__ == '__main__':
    uploader = YaUploader(test_file_path, current_token)
    result = uploader.upload()
