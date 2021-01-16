import asyncio
import aiohttp

async def task(name,work_qu):
    async with aiohttp.ClientSession() as sess:
        while not work_qu.empty():
            url=await work_qu.get()
            print(f"Task {name} get {url}")
            async with sess.get(url) as res:
                await res.text()

async def main():
    work_gu=asyncio.Queue()
    for url in [ "https://linkedin.com", "http://twitter.com", "https://realpython.com", "https://medium.com", 'https://tortoise-orm.readthedocs.io'] :
        await work_gu.put(url)

    await asyncio.gather(asyncio.create_task(task("one",work_gu)),
                             asyncio.create_task(task("two",work_gu)),)

if __name__=="__main__":
    asyncio.run(main())