# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio
import time


async def count_words(file_name1):
    with open(file_name1, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text.split())


async def count_words_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path, await count_words(file_path))


start_time = time.time()
asyncio.run(count_words_dir("/home/stanislav/PycharmProjects/GB-Flask-less/sem04/"))
print(f'{time.time() - start_time}')
