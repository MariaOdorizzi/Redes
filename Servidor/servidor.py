import socket
import os

# Função que cria a resposta HTTP
def create_http_response(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):  # Verifica se o caminho é válido
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Resposta HTTP 200 OK
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: text/html; charset=UTF-8\r\n"
        header += f"Content-Length: {len(content)}\r\n"
        header += "Connection: close\r\n\r\n"
        
        return header.encode() + content
    else:
        # Resposta HTTP 404 Not Found
        header = "HTTP/1.1 404 Not Found\r\n"
        header += "Content-Type: text/html; charset=UTF-8\r\n"
        header += "Connection: close\r\n\r\n"
        body = "<html><body><h1>404 - Página Não Encontrada</h1></body></html>"
        return header.encode() + body.encode()

# Função principal que inicializa o servidor
def start_server(host='127.0.0.1', port=8080):
    # Cria um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor iniciado em http://{host}:{port}")

    while True:
        try:
            # Aceita conexão do cliente
            client_socket, client_address = server_socket.accept()
            print(f"Conexão recebida de {client_address}")

            # Recebe a requisição HTTP
            request = client_socket.recv(1024).decode()
            print("Requisição recebida:\n", request)

            # Processa a primeira linha da requisição
            lines = request.splitlines()
            if lines:
                method, path, _ = lines[0].split()
                if method == "GET":
                    # Ajusta o caminho do arquivo solicitado
                    file_path = '.' + path if path != '/' else './index.html'

                    # Gera a resposta HTTP
                    response = create_http_response(file_path)
                else:
                    # Método não permitido
                    response = "HTTP/1.1 405 Method Not Allowed\r\n\r\nMétodo não permitido".encode()

                # Envia a resposta
                client_socket.sendall(response)
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            # Fecha a conexão com o cliente
            client_socket.close()

if __name__ == "__main__":
    start_server()
