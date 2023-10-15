import requests
import multiprocessing
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

processes = []
start_time = time.time()
for url in urls:
    file_name = url.replace('/', '').replace(':', '_').replace('.', '_')
    t = multiprocessing.Process(target=download_url, args=(url, f'task02_{file_name}.txt'))
    processes.append(t)

for process in processes:
    process.start()

for process in processes:
    process.join()

print(f'{time.time() - start_time}')
