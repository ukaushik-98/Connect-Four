import socket

def read_host() -> str:
    while True:
        host = input('Host: ').strip()
        
        if len(host) == 0:
            print('Please specify host(either a name or an IP address)')
        else:
            return host

def read_port() -> int:
    while True:
        port = int(input('Port: ').strip())

        if port < 0 or port > 65535:
            print('Ports must be an interger between 0 and 65535')

        else:
            return port

def echo(host: str, port: int):
    echo_socket = socket.socket()
    
    print('Connecting to echo server...')
    echo_socket.connect((host, port))
    print('Connected successfully!')
    
    while True:
        message_to_send = input('Message: ')
        if len(message_to_send) == 0:
            break
        else:
            bytes_to_send = (message_to_send + '\r\n').encode(encoding = 'utf-8')
            echo_socket.send(bytes_to_send)
            
            response_message_bytes = echo_socket.recv(4096)
            response_message = response_message_bytes.decode(encoding = 'utf-8').rstrip()

            print('Response: ' + response_message)

        print('Closing connection')
        echo_socket.close()
        print('Goodbye!')
        
echo(read_host(), read_port())
            
            
    
        
