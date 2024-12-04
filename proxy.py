import socket
import os

# Configuração do servidor
endereco_servidor = '127.0.0.1'  # Endereço IP local
porta_servidor = 8080           # Porta onde o servidor vai rodar

def criar_resposta(requisicao):
    """
    Processa a requisição HTTP e retorna a resposta HTTP.
    """
    try:
        # Obter a linha inicial da requisição
        linha_requisicao = requisicao.splitlines()[0]
        metodo_http, caminho_arquivo, _ = linha_requisicao.split()

        # Verificar se o método é GET
        if metodo_http != "GET":
            return "HTTP/1.1 405 Method Not Allowed\r\n\r\nMétodo não permitido".encode()

        # Ajustar o caminho do arquivo solicitado
        if caminho_arquivo == "/":
            caminho_arquivo = "/index.html"  # Arquivo padrão

        caminho_completo = caminho_arquivo.lstrip('/')  # Remove a barra inicial

        # Verificar se o arquivo solicitado existe
        if os.path.exists(caminho_completo):
            with open(caminho_completo, 'rb') as arquivo:
                conteudo_arquivo = arquivo.read()

            # Construir resposta HTTP com código 200
            cabecalho_http = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Length: {len(conteudo_arquivo)}\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
            )
            return cabecalho_http.encode() + conteudo_arquivo
        else:
            # Construir resposta HTTP com código 404
            resposta_404 = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
                "<h1>404 - Página Não Encontrada</h1>"
                "<p>O arquivo solicitado não foi encontrado no servidor.</p>"
            )
            return resposta_404.encode()
    except Exception as erro:
        # Construir resposta HTTP com código 500 em caso de erro
        resposta_500 = (
            "HTTP/1.1 500 Internal Server Error\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n\r\n"
            f"<h1>Erro Interno no Servidor</h1><p>{erro}</p>"
        )
        return resposta_500.encode()

def iniciar_servidor():
    """
    Inicializa o servidor e espera por conexões.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((endereco_servidor, porta_servidor))
        servidor.listen(1)
        print(f"Servidor rodando em http://{endereco_servidor}:{porta_servidor}/")

        while True:
            # Aceitar conexão de um cliente
            cliente, endereco_cliente = servidor.accept()
            with cliente:
                print(f"Conexão recebida de {endereco_cliente}")

                # Receber dados da requisição
                dados_requisicao = cliente.recv(1024).decode()
                print(f"Requisição recebida:\n{dados_requisicao}")

                # Processar a requisição e criar a resposta
                resposta_http = criar_resposta(dados_requisicao)

                # Enviar a resposta para o cliente
                cliente.sendall(resposta_http)

if __name__ == "__main__":
    iniciar_servidor()
