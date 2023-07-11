import socket;
from socket import timeout;
import logging;


HOST = socket.gethostname();
PORT = 55000;

print("Server IP: ", socket.gethostbyname(HOST)," // Server name: ", HOST);


s = socket.socket( socket.AF_INET6, socket.SOCK_STREAM );
s.bind((HOST, PORT)); # vinculando HOST and PORT
s.listen(); # stop the code here until receive a new connection
s.settimeout(5.0)
print("Server is wating connection..... wating for 5 seconds.."); 


try:
    # Here below only executes when client has been conected:
    newSocketConnection, clientAddr = s.accept(); # accept return a tuple()  with 2 variables
    print("client connected!  address: ",clientAddr);

    while(True):
        print("listenning while.....")
        message = newSocketConnection.recv( buffsize= 1024); # 1024 byte will be receive from client
    
        if not message:
            print("NOT DATA FOUND !" );
            newSocketConnection.close();
            break;
        else:
            print("send all message to clients sockets...." );
            newSocketConnection.sendall(message);


except timeout as timeoutError:
    print("Timeout expirado!");
    logging.error(msg= timeoutError);

finally:
    print("Encerrando socket de configuracao no servidor....");
    s.close();



#socket.setdefaulttimeout(5);
#print( "timeout zerado..." );