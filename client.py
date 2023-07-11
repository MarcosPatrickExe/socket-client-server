from socket import *;

SERVER_NAME = gethostname();
SERVER_PORT = 55000;

        
try:
               #  IPV4 enabled, TCP enabled
    sok = socket(    AF_INET,   SOCK_STREAM)
    sok.connect( (gethostname(), SERVER_PORT) );        # The connect() func only receive a tuple 
    sok.sendall( str.encode( "Hello my friend!!!", encoding="utf-8") );

    response = sok.recv(1024);
    print("Server response: ", response.decode() );


except TimeoutError as timeErr:
    print("\n \n Tempo de conexão com o servidor excedida... ", timeErr);
finally:
    print("\n Encerrando socket de configuracao do cliente TCP....");
    sok.close();
