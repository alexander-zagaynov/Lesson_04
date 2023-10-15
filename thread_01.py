import threading
import time


def worker(num):
    print(f'начало работы потока {num}')
    time.sleep(3)
    print(f'конец работы потока {num}')

# создали 5 потоков


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)


for t in threads:
    t.start()
    t.join()

print('все потоки завершили работу')

