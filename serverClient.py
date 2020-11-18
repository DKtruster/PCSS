import socket
import threading
import time

def clientServerReceive():
    s = socket.socket()
    port = 20000
    s.connect(('127.0.0.1', port))
    print(s.recv(1024))
    time.sleep(1)
    clientServerSend()
    # s.close()

def clientServerSend():
    threadSend = threading.Thread(target=clientServerReceive)
    threadSend.start()

def serverSend(boardArray):
    # Next 15 lines made with help from the lecture 7 powerpoint: "Lecture 7: Network Programming", by Jesper Rindom Jensen
    s = socket.socket()
    port = 20001
    print("PORT CREATED SERVER_SENDING")

    s.bind(('', port))
    print("Socket binded to %s" % (port))

    s.listen(5)
    print("SOCKET LISTENING")

    while True:
        # Next 5 lines made with help from the lecture 7 powerpoint: "Lecture 7: Network Programming", by Jesper Rindom Jensen
        c, addr = s.accept()
        print("Got information from", addr)
        output = (str(boardArray[4])+" "+str(boardArray[3])+" "+str(boardArray[2])+" "+str(boardArray[1])+" "+str(boardArray[0]))
        c.sendall(output.encode("utf-8"))
        c.close()
        return True
