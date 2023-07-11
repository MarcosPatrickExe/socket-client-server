from socket import *;

HOST = '172.18.64.1';
PORT = 55000;

            #IPV4 enabled,  TCP enabled
sok = socket( AF_INET, SOCK_STREAM);
sok.connect( (HOST, PORT) );

sok.sendall( str.encode( "Hello my friend!!!", encoding="utf-8") );

response = sok.recv(1024);
print("Server response: ", response.decode() );
