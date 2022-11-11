import requests,sys,time,statistics
import exercice_thread
from multiprocessing import Process

def main_processus(N):
    data_time = []
    for _ in range(1, N):
        start = time.perf_counter()
        p1 = Process(target = exercice_thread.download_urls, args = (exercice_thread.images_urls[0],))
        p2 = Process(target=exercice_thread.download_urls, args=(exercice_thread.images_urls[1],))
        p3 = Process(target=exercice_thread.download_urls, args=(exercice_thread.images_urls[2],))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p2.join()
        end = time.perf_counter()
        data_time.append(round(end - start, 2))
    print(f"moyenne des temps processus {round(statistics.mean(data_time), 2)} secondes, écart-type = {round(statistics.stdev(data_time), 2)} secondes")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        n = 10
    sys.exit(main_processus(n))