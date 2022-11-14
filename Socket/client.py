import socket,sys

def client():
   host = ""
   port = 15000
   client_socket = socket.socket()
   client_socket.connect((host, port))
   message = input("saisir le message -->")
   client_socket.send(message.encode())
   data =client_socket.recv(1024).decode()
   print (f"reponse serveur :{data}")
   client_socket.close()

if __name__=="__main__":
    sys.exit(client())