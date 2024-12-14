2. Servidor Proxy
Sua tarefa é desenvolver um pequeno servidor proxy web capaz de armazenar em cache páginas da web. É um servidor proxy muito simples que apenas entende solicitações GET simples, mas é capaz de lidar com todos os tipos de objetos - não apenas páginas HTML, mas também imagens.

Geralmente, quando o cliente faz uma solicitação, a solicitação é enviada ao servidor web. O servidor web então processa a solicitação e envia uma mensagem de resposta ao cliente solicitante. Para melhorar o desempenho, criamos um servidor proxy entre o cliente e o servidor web. Agora, tanto a mensagem de solicitação enviada pelo cliente quanto a mensagem de resposta entregue pelo servidor web passam pelo servidor proxy. Em outras palavras, o cliente solicita os objetos via servidor proxy. O servidor proxy encaminhará a solicitação do cliente ao servidor web. O servidor web então gerará uma mensagem de resposta e a entregará ao servidor proxy, que por sua vez a envia ao cliente.

Executando o Servidor Proxy
Execute o programa do servidor proxy usando seu prompt de comando e então solicite uma página da web pelo seu navegador. Direcione as requisições para o servidor proxy usando seu endereço IP e número da porta.
Por exemplo: http://localhost:8888/www.google.com
Para usar o servidor proxy com o navegador e o proxy em computadores separados, você precisará do endereço IP no qual o servidor proxy está em execução. Nesse caso, ao executar o proxy, você precisará substituir o "localhost" pelo endereço IP do computador onde o servidor proxy está em execução. Observe também o número da porta usado. Você substituirá o número da porta usado aqui "8888" pelo número da porta que você utilizou no código do servidor, na qual o servidor proxy está ouvindo.
