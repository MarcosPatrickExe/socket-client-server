import socket;
from socket import timeout;
import logging;
from threading import Thread;


clients = []
HOST = socket.gethostname();
PORT = 55000;
TIMEOUT = 20.0;


print("\nServer IP: ", socket.gethostbyname(HOST)," // Server name: ", HOST);


def clientThread( clientSocket):
    while True:
        try:
            # Esperando nova resposta para executar as linhas abaixo....
            message = clientSocket.recv(2048);  # 2048 bytes will be receive from client
            broadcastMessage( message);
            print("\n", message.decode());
            # clientSocket.sendall(message.encode());
        except:
            print("\n \n => Cliente desconectado.....");
            clients.remove(clientSocket);
            return; #ou use 'break;'


def broadcastMessage( newMessage):
    for clientItem in clients:
      # if clientItem != clientCurrent
        try:
            clientItem.send( newMessage );
        except:
            #print("\n \n => Erro ao enviar mensagens para os clients conectados... info: ", exc);
            clients.remove(clientItem);


def init():
    try:
                        # IPV4 enabled,  TCP enabled
        server = socket.socket( socket.AF_INET, socket.SOCK_STREAM );
        server.bind((HOST, PORT)); # vinculando HOST and PORT
        server.listen(); # stop the code here until receive a new connection
        server.settimeout(TIMEOUT)
        print("Server is waiting connection..... time left: ",TIMEOUT," seconds... \n"); 

        while True:
            # A linha abaixo somente eh executada quando um novo socket se conecta...
            clientSocket, clientAddr = server.accept(); # accept return a tuple()  with 2 variables
            print("\n client connected!  address: ", clientAddr[0], "/ port: ", clientAddr[1] );
            clients.append( clientSocket);
            thread = Thread(target =clientThread, args=[clientSocket]);
            thread.start();

    except Exception as exce:
        if len(clients) == 0:
            logging.error("\n \n => Timeout expirou e nenhum cliente foi detectado! Encerrando servidor... ", exce);
            server.close();
            return
   
init();
