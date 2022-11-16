import socket,sys
import threading, queue
import time


def lecture(client_socket,q):
    try :
        message=""
        while message.lower() != "exit" and message.lower() != "bye":
            message = client_socket.recv(1024).decode()
            if message != None:
                print (f"response serveur : {message}")
            if not q.empty() :
                if q.get() == "exit":
                    break
        client_socket.close()
    except OSError:
        print ("connection fermée")
    exit()

def client(host,port):

   try:
      client_socket = socket.socket()
      client_socket.connect((host, port))

      message = input("saisir votre pseudo: ")
      client_socket.send(message.encode())
      q = queue.Queue()
      fil = threading.Thread(target=lecture, args=(client_socket, q))
      fil.start()
      while message.lower() != "exit" and message.lower() != "bye":
         time.sleep(0.1)
         message = input("saisir le message --> ")
         client_socket.send(message.encode())
         if not q.empty():
             if q.get() == "exit":
                break
      q.put("exit")
      fil.join()
      try:
        client_socket.close()
      except Exception:
          print ("connection déja fermée")
   except ConnectionRefusedError:
       print("connection refusée par le serveur")
   except BrokenPipeError:
      print ("serveur fermé")
   except OSError:
       print ("connection fermée du coté serveur")
   finally:
      client_socket.close()
   exit()

if __name__=="__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    sys.exit(client(host,port))