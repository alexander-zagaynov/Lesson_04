import os
import threading
import time


def count_words(file_name1):
    with open(file_name1, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text.split())


def count_words_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            t = threading.Thread(target=print, args=(file_path, count_words(file_path)))
            threads.append(t)
            t.start()


threads = []
start_time = time.time()
count_words_dir("/home/stanislav/PycharmProjects/GB-Flask-less/sem04/")

for thread in threads:
    thread.join()

print(f'{time.time() - start_time}')
