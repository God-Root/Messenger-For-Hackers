import sys, socket, select

print(''' 
  __  __                                                         
 |  \/  | ___  ___ ___  ___ _ __   __ _  ___ _ __     
 | |\/| |/ _ \/ __/ __|/ _ \ '_ \ / _` |/ _ \ '__|    
 | |  | |  __/\__ \__ \  __/ | | | (_| |  __/ |       
 |_|  |_|\___||___/___/\___|_| |_|\__, |\___|_|       
                                  |___/               
  _____            _   _            _                      
 |  ___|__  _ __  | | | | __ _  ___| | _____ _ __ ___      
 | |_ / _ \| '__| | |_| |/ _` |/ __| |/ / _ \ '__/ __|     
 |  _| (_) | |    |  _  | (_| | (__|   <  __/ |  \__ \     
 |_|  \___/|_|    |_| |_|\__,_|\___|_|\_\___|_|  |___/     
                                                           
 By God-Root               
''')

HOST = str(raw_input("Please input IP address :  ") )
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 

    SOCKET_LIST.append(server_socket)
    
    print "Chat server started on port " + str(PORT)
 
    while 1:

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:

            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered ourchatting room\n" % addr)
             

            else:

                try:

                    data = sock.recv(RECV_BUFFER)
                    if data:

                        broadcast(server_socket, sock, "\r" + data)  
                    else:
   
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)


                        broadcast(server_socket, sock, "Client (%s, %s)is offline\n" % addr) 


                except:
                    broadcast(server_socket, sock, "Client (%s, %s) isoffline\n" % addr)
                    continue

    server_socket.close()
    

def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:

        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :

                socket.close()

                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":
    sys.exit(chat_server())
