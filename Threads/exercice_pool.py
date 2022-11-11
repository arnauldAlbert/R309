import concurrent.futures
import requests,sys,time,statistics
import exercice_thread

def main_pool(N):
    data_time=[]
    for _ in range (1,N):
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(exercice_thread.download_urls, exercice_thread.images_urls)
        end = time.perf_counter()
        data_time.append(round(end - start, 2))
    print (f"moyenne des temps pool {round(statistics.mean(data_time),2)} secondes, écart-type = {round(statistics.stdev(data_time),2)} secondes")

if __name__=="__main__":
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        n = 10
    sys.exit(main_pool(n))