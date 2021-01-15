import concurrent.futures
import threading
import requests
import time

thread_loc=threading.local()

def get_sess():
    if not hasattr(thread_loc,"session"):
        thread_loc.session=requests.Session()
    return thread_loc.session

def download_web(url):
    sess=get_sess()
    with sess.get(url) as response:
        print(f" {len(response.content)} from {url}")

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        ex.map(download_web,sites)

if __name__=="__main__":
    sites=[ "https://oko.press",
            "https://www.dwutygodnik.com"]

    start_t=time.time()
    download_all(sites)
    dura=time.time()-start_t
    print(f"Downloaded {len(sites)} in {dura} sec ")