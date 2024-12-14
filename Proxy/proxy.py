import socket
import os
import mimetypes  # Biblioteca para detectar o tipo de conteúdo

def create_http_response(file_path):
    """
    Gera a resposta HTTP com base no arquivo solicitado.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as f:
                content = f.read()

            # Detecta o tipo do conteúdo
            content_type, _ = mimetypes.guess_type(file_path)
            if not content_type:
                content_type = 'application/octet-stream'  # Tipo genérico

            # Resposta HTTP 200 OK
            header = "HTTP/1.1 200 OK\r\n"
            header += f"Content-Type: {content_type}; charset=UTF-8\r\n"
            header += f"Content-Length: {len(content)}\r\n"
            header += "Connection: close\r\n\r\n"

            return header.encode() + content
        except Exception as e:
            return generate_500_response(str(e))
    else:
        return generate_404_response()

def generate_404_response():
    """
    Gera uma resposta HTTP 404 - Conteúdo Não Encontrado.
    """
    header = "HTTP/1.1 404 Not Found\r\n"
    header += "Content-Type: text/html; charset=UTF-8\r\n"
    header += "Connection: close\r\n\r\n"
    body = "<html><body><h1>404 - Conteúdo Não Encontrado</h1></body></html>"
    return header.encode() + body.encode()

def generate_500_response(error_message):
    """
    Gera uma resposta HTTP 500 - Erro Interno no Servidor.
    """
    header = "HTTP/1.1 500 Internal Server Error\r\n"
    header += "Content-Type: text/html; charset=UTF-8\r\n"
    header += "Connection: close\r\n\r\n"
    body = f"<html><body><h1>500 - Problema Interno no Servidor</h1><p>{error_message}</p></body></html>"
    return header.encode() + body.encode()

def start_server(host='127.0.0.1', port=8080):
    """
    Inicializa o servidor HTTP básico.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Permite até 5 conexões pendentes

    print(f"Servidor rodando em http://{host}:{port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Conexão recebida de {client_address}")

            # Recebe a requisição HTTP
            request = client_socket.recv(1024).decode()
            print("Requisição recebida:\n", request)

            # Processa a primeira linha da requisição
            lines = request.splitlines()
            if not lines:
                continue  # Evita falhas com requisições malformadas
            
            method, path, _ = lines[0].split()
            if method != "GET":
                # Responde com 405 para métodos não suportados
                response = "HTTP/1.1 405 Method Not Allowed\r\n\r\nOperação não permitida".encode()
            else:
                # Normaliza o caminho do arquivo solicitado
                safe_path = os.path.normpath('.' + path)
                if safe_path == './':
                    safe_path = './index.html'  # Página padrão

                # Gera a resposta HTTP
                response = create_http_response(safe_path)

            client_socket.sendall(response)
        except Exception as e:
            print(f"Erro: {e}")
            client_socket.sendall(generate_500_response(str(e)))
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
