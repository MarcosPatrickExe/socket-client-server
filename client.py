from socket import *;
import threading;


def threadReceiveMessages(socketClient):
    while True:
        try:
            response = socketClient.recv(2048).decode('utf-8');
            print(f'\n{response}, \n'); # Server response
        except:
            print("\n \n => A conexão com o servidor foi perdida... aperte Enter... "); # esse Enter serve para desabilitar a outra thread
            socketClient.close();
            break; # ou use 'return'


def threadSendMessages(socketClient, nameClient):
    while True:
        try:
            message = input('\n-------------\nEscreva uma mensagem: \n');
            socketClient.send( str.encode( f'<{nameClient}>  {message}', encoding="utf-8") );
        except:
            socketClient.close();
            break; # ou use 'return'


def main():
    SERVER_NAME = gethostname();
    SERVER_PORT = 55000;

    client = socket( AF_INET,  SOCK_STREAM)  # (IPV4 enabled, TCP enabled)

    try:
        client.connect( (SERVER_NAME, SERVER_PORT) ); # The connect() func only receive a tuple 
        print('=> conectado com o servidor... ');
    except Exception as exc:
        client.close();
        print("\n \n => Erro ao tentar conectar-se ao servidor.... info: ", exc);
        return;


    userName = input('\nQual o seu nome? \n');

    sendThread = threading.Thread( target =threadSendMessages, args =[client, userName]);
    receiveThread = threading.Thread( target =threadReceiveMessages, args =[client]);
    sendThread.start();
    receiveThread.start();

main();
