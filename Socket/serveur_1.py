import socket,sys

def serveur():
    port = 15000
    host = ""

    serveur_socket = socket.socket()
    serveur_socket.bind((host,port))
    serveur_socket.listen(5)
    while True :
        conn, address = serveur_socket.accept()

        data = conn.recv(1024).decode()
        print (f"(adresse {address[0]} port :{address[1]}) -->  {data}")
        reply = f"bienvenue sur le serveur de Nono. votre adresse est {address[0]} port :{address[1]}"
        conn.send(reply.encode())
        conn.close()

if __name__=="__main__":
    sys.exit(serveur())