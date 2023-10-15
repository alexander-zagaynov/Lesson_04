import requests
import threading
import time


def download_url(url, file_name):
    response = requests.get(url)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(response.text)


urls = ['https://mail.ru',
       'https://google.ru',
       'https://yandex.ru',
       'https://gmail.com',
       'https://yahoo.com',
       ]

threads = []
start_time = time.time()

for url in urls:
    file_name = url.replace('/', '').replace(':', '_').replace('.', '_')
    t = threading.Thread(target=download_url, args=(url, f'task01_{file_name}.txt'))
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'{time.time() - start_time}')