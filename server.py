import socket;
from socket import timeout;
import logging;


HOST = socket.gethostname();
PORT = 55000;
TIMEOUT = 20.0;

print("Server IP: ", socket.gethostbyname(HOST)," // Server name: ", HOST);

                   # IPV4 enabled,  TCP enabled
socketConfig = socket.socket( socket.AF_INET, socket.SOCK_STREAM );
socketConfig.bind((HOST, PORT)); # vinculando HOST and PORT
socketConfig.listen(); # stop the code here until receive a new connection
socketConfig.settimeout(TIMEOUT)
print("Server is waiting connection..... time left: ",TIMEOUT," seconds... \n"); 


try:
    # Here below only executes when client has been conected:
    clientSocket, clientAddr = socketConfig.accept(); # accept return a tuple()  with 2 variables
    print("\n client connected!  address: ", clientAddr[0], "/ port: ", clientAddr[1] );


    while(True):
        message = clientSocket.recv(1024);  # 1024 bytes will be receive from client
    
        if not message:
            print("\n NOT DATA FOUND !" );
            clientSocket.close();           # the 'clientSocket' oject will be empty now...
            break;
        else:
            print("\n Client message: ", message.decode());
            print("send all message to clients sockets...." );
            clientSocket.sendall(message);


except timeout as timeoutError:
    print("\n \nTimeout expirado!");
    logging.error(msg= timeoutError);

finally:
    print("\nEncerrando socket de configuracao do servidor TCP....");
    socketConfig.close();

