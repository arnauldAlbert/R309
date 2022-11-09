import sys
import threading
import time
from threading import Thread
from random import randint
from time import sleep

def mafonction(nom : str):
    verrou = threading.Lock()
    verrou.acquire()
    print ("ma fonction renvoie", nom, "thread : ",threading.current_thread().name," \n")
    verrou.release()
    i = randint(0,2)
    sleep(i+1)
    verrou.acquire()
    print(f"thread : {threading.current_thread().name} a dormi {i+1} secondes \n")
    verrou.release()

def main():
    start = time.perf_counter()
    fil1 = Thread(target=mafonction, args=["fonction 1"])
    fil2 = Thread(target=mafonction, args=["fonction 2"])
    fil1.start()
    fil2.start()
    sleep(0.1)
    fil2.join()
    fil1.join()
    end = time.perf_counter()
    print(f"fin d'execution en {round(end-start,4)} secondes")

if __name__ == "__main__":
    sys.exit(main())
