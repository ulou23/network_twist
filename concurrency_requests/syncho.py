import requests
import time

def download_web(url,sess):
    with sess.get(url) as response:
        print(f" {len(response.content)} from {url}")

def download_all(sites):
    with requests.Session() as sess:
        for url in sites:
            download_web(url,sess)

if __name__=="__main__":
    sites=[ "https://oko.press",
            "https://www.dwutygodnik.com"]

    start_t=time.time()
    download_all(sites)
    dura=time.time()-start_t
    print(f"Downloaded {len(sites)} in {dura} sec ")