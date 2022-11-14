import socket,sys
import threading

def ecoute(conn, address):
    i=1
    pseudo = conn.recv(1024).decode()

    while True:
        data = conn.recv(1024).decode()
        print(f"{pseudo} --> {data} \n")
        reply = f"reçu {i}"
        conn.send(reply.encode())
        i=i+1
        if str(data).lower() == "exit":
            break
    conn.close()

def serveur():
    port = 15002
    host = ""
    try :
        serveur_socket = socket.socket()
        serveur_socket.bind((host,port))
        serveur_socket.listen(5)
        liste =[]
        i=0
        while i < 10:
            conn, address = serveur_socket.accept()
            c = threading.Thread(target=ecoute,args=(conn,address))
            c.start()
            liste.append(c)
            i = i+1

    except KeyboardInterrupt:
        print("fermeture du serveur")
    finally:
        serveur_socket.close()


if __name__=="__main__":
    sys.exit(serveur())