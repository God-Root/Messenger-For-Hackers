import sys, socket, select, os, time

Title =(''' 
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

print(Title)
if str(raw_input("#Get some help: 1\n#To continue for chatting and setup: 2\n-->")) == '1':
        sys.stderr.write('\nHow to get started:\n')
        sys.stderr.write('''--> set up MFH_server.py first\n--> then return to this client\n--> remember your hostname of your server\n--> remember the port of your server''')
        sys.exit()
else:
        you = str(raw_input("Please Input your name: "))

def chat_client():

    host = str(raw_input("Please Input your server hostname: "))
    port = int(raw_input("Thank you\nPlease Input your server port: "))
    print 'Thank you'
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print '---------------socket manager [OK]---------------'
    try :
        print '---------------connecting to server---------------'
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
    
    print 'Connected to remote host. You can start sending/receiving messages'
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Title)
    sys.stdout.write(you+"=> "); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Error in Windows- Solution: select on sockets on one thread and blocking local I/O on a second thread,
        # Working on this!
        # May have to use Async frameworks like Twisted
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        clientsock.close()
        for sock in read_sockets:            
            if sock == s:

                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :

                    sys.stdout.write(data)
                    sys.stdout.write(you+"=> "); sys.stdout.flush() 
                        
            
            else :

                msg = you+":"+sys.stdin.readline()
                s.send(msg)
                sys.stdout.write(you+"=> "); sys.stdout.flush() 
            
            

if __name__ == "__main__":

    sys.exit(chat_client())
