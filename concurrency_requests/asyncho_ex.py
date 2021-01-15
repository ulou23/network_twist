import asyncio
import time
import aiohttp

async def download_web(sess,url):
    async with sess.get(url) as response:
        print( " Read {0} from {1} ".format(response.content_length,url))

async def download_all(sites):
    async with aiohttp.ClientSession() as sess:
        tasks=[]
        for url in sites:
            task=asyncio.ensure_future(download_web(sess,url))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True)


if __name__=="__main__":
    sites=[ "https://oko.press",
            "https://www.dwutygodnik.com"]

    start_t=time.time()
    asyncio.get_event_loop().run_until_complete(download_all(sites))

    dura=time.time()-start_t
    print(f"Downloaded {len(sites)} in  {dura} sec")