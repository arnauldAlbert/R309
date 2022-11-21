import sys, socket, threading, signal, queue, time, os

liste_connection = []
liste_queue=[]
liste_thread = []
qu = queue.Queue()

def ecoute(conn, q):
    pseudo = conn.recv(1024).decode()
    verrou = threading.Lock()
    data = ""
    try :
        while str(data).lower().strip() != "bye" and str(data).lower().strip() != "exit":
            data = conn.recv(1024).decode()
            if len(data) == 0:
                break
            print(f"{pseudo} --> {data} \n")
            conn.send(data.encode())
        if str(data).lower().strip() == "exit":
            verrou.acquire()
            liste_connection.remove(conn)
            verrou.release()
            conn.close()
            q.put("exit")

    except OSError:
        print("connection fermée")
    print (f"fin thread {pseudo}")

def deconnection(qu):
    flag = 0
    while True:
        for q in liste_queue:
            if not q.empty():
                if q.get() == "exit":
                    flag = 1
        if flag == 1:
            for qq in liste_queue:
                qq.put("exit")
            try:
                print("envoi du signal de terminaison")
                for c in liste_connection:
                    c.send("bye".encode())
                time.sleep(1)
                signal.pthread_kill(threading.main_thread().ident,signal.SIGUSR1)
            except BrokenPipeError:
                print("erreur écriture socket fermée")
            except ConnectionResetError:
                print("connection fermée du coté serveur")
            qu.put("fin")
            break
    print("sortie")

def arret(signnum,stack):
    sys.exit()


def serveur(host, port):
    try:
        serveur_socket = socket.socket()
        serveur_socket.setsockopt()
        serveur_socket.bind((host,port))
        serveur_socket.listen(5)
        print ("demarrage écoute")
        signal.signal(signal.SIGUSR1,arret)
        dec=threading.Thread(target=deconnection,args=(qu,))
        dec.start()
        while True:
            conn, address = serveur_socket.accept()
            if conn != None:
                print(f"connection acceptée {address}")
                liste_connection.append(conn)
                q=queue.Queue()
                liste_queue.append(q)
                c = threading.Thread(target=ecoute,args=(conn,q))
                liste_thread.append(c)
                c.start()
                print("démarrage processus")
            if not qu.empty():
                print ("fin du programme")
                serveur_socket.close()
                break
    except TimeoutError:
        print("erreur de Timeout")
    except socket.gaierror:
        print ("nom d'hôte invalide")
    except ConnectionResetError:
        print ("fermeture de connection brutale")
    except KeyboardInterrupt:
        print ("fermeture du serveur demandée")
    for t in liste_thread:
        t.join()

    print ("fin du programme")
    serveur_socket.close()
    exit()

if __name__ == "__main__":
    """port = 15004
    host = "127.0.0.1"
    flag_exit = 0
    try:
        if len(sys.argv) >= 3:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                print(f"la syntaxe est 'python serveur_3.py port' ou port est un entier supérieur à 2000")
            host = sys.argv[1]
            port = int(sys.argv[2])

        else:
            print(f"le port par défaut est 15002. pour modifier le port, la syntaxe est 'python serveur_3.py port' ou port est un entier supérieur à 2000")
        sys.exit(serveur(host,port))
    except TypeError:
        print (f"la syntaxe est 'python serveur_3.py port' ou port est un entier supérieur à 2000" )
    """
    host = sys.argv[1]
    port = int(sys.argv[2])
    sys.exit(serveur(host, port))

