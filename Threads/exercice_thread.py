import threading
import requests,sys,time,statistics

images_urls=[
    "http://1.bp.blogspot.com/-i1Gr4NezCGE/ULjU4Y816bI/AAAAAAAAOEY/aLGC9wzAHdc/w1200-h630-p-k-no-nu/Akira+Wallpapers+01.jpg",
    "https://mir-s3-cdn-cf.behance.net/project_modules/1400/c068f451582427.58f316acc1842.jpg",
    "https://bowlivestorage.blob.core.windows.net/beastsofwarlivesite/2014/04/HellDorado-logo-2.jpg"
]

def download_urls(img_url:str):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
       # print(f"{img_name} was downloaded")

def main_thread(N):
    data_time=[]
    for _ in range(1,N):
        start = time.perf_counter()
        fil1 = threading.Thread(target = download_urls, args = [images_urls[0]])
        fil2 = threading.Thread(target=download_urls, args=[images_urls[1]])
        fil3 = threading.Thread(target=download_urls, args=[images_urls[2]])
        fil1.start()
        fil2.start()
        fil3.start()
        fil1.join()
        fil2.join()
        fil3.join()
        end = time.perf_counter()
        data_time.append(round(end-start,2))
    print (f"moyenne des temps thread {round(statistics.mean(data_time),2)} secondes, écart-type = {round(statistics.stdev(data_time),2)} secondes")

if __name__=="__main__":
    if len(sys.argv)>=2:
        n = int(sys.argv[1])
    else:
        n=10
    sys.exit(main_thread(n))