import sys
import threading
import time
from threading import Thread
from random import randint
from time import sleep

class monthread(Thread):
    def __init__(self,msg):
        super().__init__()
        self.msg = msg

    def run(self):
        verrou = threading.Lock()
        verrou.acquire()
        print(f"ma fonction renvoie {self.msg}, thread : {threading.current_thread().name} \n")
        verrou.release()
        i = randint(0, 2)
        sleep(i + 1)
        verrou.acquire()
        print(f"thread : {threading.current_thread().name} a dormi {i + 1} secondes \n")
        verrou.release()


def mafonction(nom : str):
    verrou = threading.Lock()
    verrou.acquire()
    print ("ma fonction renvoie", nom, "thread : ",threading.current_thread().name," \n")
    print(f"identité : {threading.get_ident()} et identité du lanceur {threading.get_native_id()}")
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
    fil3 = monthread("mon Thread 1")
    fil3.start()
    fil1.start()
    fil2.start()
    print (f" liste {threading.active_count()} et {threading.enumerate()}")
    sleep(0.1)
    fil2.join()
    fil1.join()
    fil3.join()
    end = time.perf_counter()
    print(f"fin d'execution en {round(end-start,4)} secondes")

if __name__ == "__main__":
    sys.exit(main())
