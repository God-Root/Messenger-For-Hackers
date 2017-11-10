import sys, socket, select, random, time


#HOST = str(raw_input("Please input IP address :  ") )


SOCKET_LIST = []
RECV_BUFFER = 4096 
x = 0

def chat_server():
    PORT = 9008

    socketnetwork = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #This process needs to change for server connection
    socketnetwork.connect(("8.8.8.8", 80))
    HOST = socketnetwork.getsockname()[0]
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    
    server_socket.listen(10)
    SOCKET_LIST.append(server_socket)
    
    print "Chat server started on port " + str(PORT) + " and on host " + str(HOST)

    while 1: #server port 9008 main-room for selecting which chat to continue on

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

        clients = []
        
        for sock in ready_to_read:
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                
                broadcast(server_socket, sockfd, "[%s:%s] entered the main-room, choose which room you want to be in\n Pick" % addr)
                while x < 10000:
                    broadcast(server_socket, sock, "\r" + clients)
                    time.sleep(5)
                    x = x + 1
            else:
                broadcast(server_socket, sockfd, "[%s:%s] type (list) to see people in chat" % addr)
            if sock.recv(RECV_BUFFER) == clients:
                PORT2 = random.randint(8000, 9000)
            	broadcast(server_socket, sockfd, 'You will be connected to' + clients + PORT2)
            	try:
                    server_socket.bind((HOST2, PORT))
                except socket.error as e:
                    while e.errno == 98:
                        PORT2 = random.randint(8000, 9000)
                        server_socket.bind((HOST2, PORT))
                server_socket.listen(10)
                SOCKET_LIST.append(server_socket)


    server_socket.close()

    while PORT <> 9008: #server functionality for sending messages
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
                            broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
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
