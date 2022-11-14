import socket,sys
import threading

def ecoute(conn, address):
    data = conn.recv(1024).decode()
    print(f"(adresse {address[0]} port :{address[1]}) -->  {data}")
    reply = f"bienvenue sur le serveur de Nono. votre adresse est {address[0]} port :{address[1]}"
    conn.send(reply.encode())
    conn.close()

def serveur():
    port = 15000
    host = ""

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

    for c in liste:
        c.join()

if __name__=="__main__":
    sys.exit(serveur())