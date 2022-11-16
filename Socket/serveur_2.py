import socket,sys
import threading
import time

liste =[]


def ecoute(conn, address):
    i=1
    pseudo = conn.recv(1024).decode()
    verrou = threading.Lock()
    data=""
    try:
        while str(data).lower() != "bye" and str(data).lower() != "exit":
            data = conn.recv(1024).decode()
            if len(data)==0:
                break
            print(f"{pseudo} --> {data} \n")
            conn.send(data.encode())
            i=i+1
    except OSError:
        print("connection fermée")


    if str(data).lower() == "exit":
        verrou.acquire()
        for c in liste:
            if c!=conn:
                c.send("bye".encode())
                c.close()

        verrou.release()

    #if str(data).lower() == "bye":
        #conn.send("bye".encode())
    conn.close()
    verrou.acquire()
    liste.remove(conn)
    verrou.release()

def serveur():
    port = 15003
    host = ""
    try :
        serveur_socket = socket.socket()
        serveur_socket.bind((host,port))
        serveur_socket.listen(5)
        while True:
            conn, address = serveur_socket.accept()
            liste.append(conn)
            c = threading.Thread(target=ecoute,args=(conn,address))
            c.start()




    except KeyboardInterrupt:
        print("fermeture du serveur")
    finally:
        #for c in liste:
        #   c.close()
        serveur_socket.close()

    print("fermeture du serveur")

if __name__=="__main__":
    sys.exit(serveur())