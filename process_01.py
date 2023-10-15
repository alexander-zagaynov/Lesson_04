import multiprocessing
import time


def worker(num):
    print(f'запущен прецесс {num}')
    time.sleep(3)
    print(f'Завершен процесс {num}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()  # p.start()

    for p in processes:
        # поменяли местами p.start()
        p.join()

    print('Все процессы завершили работу')



