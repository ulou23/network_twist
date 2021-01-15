import requests
import time
import multiprocessing

sess=None

def set_global_sess():
    global sess
    if not sess:
        sess=requests.Session()

def download_web(url):
    with sess.get(url) as response:
        name=multiprocessing.current_process().name
        print(f"{name}  read : {len(response.content)} from {url}")

def download_all(sites):
    with multiprocessing.Pool(initializer=set_global_sess) as  pool:
        pool.map(download_web,sites)

if __name__=="__main__":
    sites=[ "https://oko.press",
            "https://www.dwutygodnik.com"]

    start_t=time.time()
    download_all(sites)
    dura=time.time()-start_t
    print(f"Downloaded {len(sites)} in {dura} sec ")