# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте асинхронный подход.

import asyncio
import aiohttp
import time


urls = ['https://mail.ru',
        'https://google.ru',
        'https://yandex.ru',
        'https://gmail.com',
        'https://yahoo.com'
        ]


async def download_url(url1, file_name1):
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as response:
            with open(file_name1, 'w', encoding='utf-8') as f:
                f.write(await response.text())


async def main():
    tasks = []

    for url in urls:
        file_name = url.replace('/', '').replace(':', '_').replace('.', '_')
        t = asyncio.ensure_future(download_url(url, f'task03_{file_name}.txt'))
        tasks.append(t)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
    print(f'{time.time() - start_time}')