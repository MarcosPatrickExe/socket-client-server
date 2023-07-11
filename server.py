import socket;
from socket import timeout;
import logging;


HOST = socket.gethostname();
PORT = 55000;

print("Server IP: ", socket.gethostbyname(HOST)," // Server name: ", HOST);

                   # IPV4 enabled,  TCP enabled
socketConfig = socket.socket( socket.AF_INET, socket.SOCK_STREAM );
socketConfig.bind((HOST, PORT)); # vinculando HOST and PORT
socketConfig.listen(); # stop the code here until receive a new connection
socketConfig.settimeout(15.0)
print("Server is waiting connection..... time left: 15 seconds..."); 


try:
    # Here below only executes when client has been conected:
    clientSocket, clientAddr = socketConfig.accept(); # accept return a tuple()  with 2 variables
    print("client connected!  address: ", clientAddr[0], "/ port: ", clientAddr[1] );

    while(True):
        print("listenning while.....")
        message = clientSocket.recv(1024); # 1024 byte will be receive from client
    
        if not message:
            print("NOT DATA FOUND !" );
            clientSocket.close();
            break;
        else:
            print("Client message: ", message.decode());
            print("send all message to clients sockets...." );
            clientSocket.sendall(message);


except timeout as timeoutError:
    print("Timeout expirado!");
    logging.error(msg= timeoutError);

finally:
    print("Encerrando socket de configuracao do servidor socket TCP....");
    socketConfig.close();

