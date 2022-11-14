import socket,sys

def client():
   host = ""
   port = 15002
   try:
      client_socket = socket.socket()
      client_socket.connect((host, port))
      message = input("saisir votre pseudo")
      client_socket.send(message.encode())
      while True:
         message = input("saisir le message -->")
         test = client_socket.getsockname()
         print (test)
         client_socket.send(message.encode())
         data =client_socket.recv(1024).decode()
         print (f"reponse serveur :{data}")
         if message == "exit":
            break
         if client_socket.getsockname():
            pass
   except BrokenPipeError:
      print ("serveur fermé")
   finally:
      client_socket.close()

if __name__=="__main__":
    sys.exit(client())