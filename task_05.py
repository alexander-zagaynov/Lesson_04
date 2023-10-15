import os
import multiprocessing
import time


def count_words(file_name1):
    with open(file_name1, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text.split())


def count_words_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            t = multiprocessing.Process(target=print, args=(file_path, count_words(file_path)))
            processes.append(t)
            t.start()


processes = []
start_time = time.time()
count_words_dir("/home/stanislav/PycharmProjects/GB-Flask-less/sem04/")

for process in processes:
    process.join()

print(f'{time.time() - start_time}')

