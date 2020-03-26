
import asyncio
import aiohttp
import datetime
import concurrent.futures
import time
import threading
from  multiprocessing import Process
lis = {}

def prt(a, qwe):
    global lis
    b = 1
    for i in range(a):
         b = a+i
    lis[qwe] = b
    print(lis)

def asy(a,b, lis):
    with threading.Lock():
        lis[a] = b

async def sd(i, url, sesion):
    global w
    async with sesion.get(url) as req:
        r = await req.text()
        w = r


async def main():
    tasks = []
    url = 'https://onliner.by'

    async with aiohttp.ClientSession() as sesion:
        for i in range(10):
            tasks.append(sd(i, url, sesion))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t3 = datetime.datetime.now()

    a = Process(target=prt, args=(2**25,'w',))
    v = Process(target=prt, args=(2 ** 25, 'a',))
    a.start()
    v.start()
    a.join()
    v.join()
    # asyncio.get_event_loop().run_until_complete(main())
    # asyncio.run(main())
    # t = threading.Thread(target=prt, args=(2**25, 'w'))
    # t1 = threading.Thread(target=prt, args=(2 ** 25, 'a'))
    # t.start()
    # t1.start()
    # with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
    #     try:
    #         a = pool.submit(prt, *(2**25, 'w'))
    #         pool.submit(prt, *(2 ** 25, 'e'))
    #
    #     except Exception as e:
    #         print(e)

    print(lis)
    # a = prt(2**25, 'w')
    # b = prt(2**25, 'a')
    # t.join()
    # t1.join()
    print(sum([lis[i] for i in lis]))
    print(datetime.datetime.now() - t3)