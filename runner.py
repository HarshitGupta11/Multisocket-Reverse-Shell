from threading import Thread
import socket
import sys,select
from queue import Queue
import signal

def handler(signum,frame):
    raise(Exception)

class Client():
    def __init__(self,q,conn):
        self.q=q
        self.conn=conn

    def command_sender(self):
        while True:
            cmd=self.q.get()
            if len(cmd)>0:
                print("Got Commands in Queue.......")
                self.conn.send(str.encode(cmd))
        
class ThreadRunner():
    def __init__(self):
        self.s=socket.socket()
        self.clients=[]

    def send_commands(self,cmd):
        for c in self.clients:
            c.q.put(cmd)
        
    def bind(self,host,port):
        self.s.bind((host,port))
        self.s.listen(5)

    def start(self):
        self.bind('',8888)
        while True:
            signal.signal(signal.SIGALRM,handler)
            signal.alarm(100)
            try:
                while True:
                    conn,addr=self.s.accept()
                    print("Connection has been established | " + "IP " + addr[0] + " | Port " + str(addr[1]))
                    obj=Client(Queue(),conn)
                    t=Thread(target=obj.command_sender)
                    t.start()
                    self.clients.append(obj)
            except:
                _=1
            signal.alarm(0)
            print("Listening for Commands...............")
            i,o,e=select.select([sys.stdin],[],[],100)
            if i:
                print("Sending Command")
                cmd=sys.stdin.readline().strip()
                self.send_commands(cmd)
            print("Commands Sent")

def main():
    tr=ThreadRunner()
    tr.start()

if __name__=="__main__":
    main()

            
