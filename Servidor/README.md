1. Servidor Web
Você desenvolverá um servidor web que responderá a uma requisição HTTP por vez. Seu servidor web deve aceitar e analisar a requisição HTTP, obter o arquivo solicitado do sistema de arquivos do servidor, criar uma mensagem de resposta HTTP composta pelo arquivo solicitado precedido por linhas de cabeçalho e, em seguida, enviar a resposta diretamente para o cliente. Se o arquivo solicitado não estiver presente no servidor, o servidor deve enviar uma mensagem HTTP "404 Não Encontrado" de volta ao cliente.

Executando o Servidor 
Coloque um arquivo HTML (por exemplo, HelloWorld.html) no mesmo diretório em que o servidor está localizado. Execute o programa do servidor. Determine o endereço IP do host que está executando o servidor (por exemplo, 128.238.251.26). De outro host, abra um navegador e forneça o URL correspondente. Por exemplo:
http://128.238.251.26:6789/HelloWorld.html
‘HelloWorld.html’ é o nome do arquivo que você colocou no diretório do servidor. Observe também o uso do número da porta após os dois pontos. Você precisa substituir esse número de porta pelo número da porta que você usou no código do servidor. No exemplo acima, usamos o número da porta 6789. O navegador deve então exibir o conteúdo de HelloWorld.html. Se você omitir ":6789", o navegador assumirá a porta 80 e você obterá a página da web do servidor apenas se o seu servidor estiver ouvindo na porta 80.
Em seguida, tente obter um arquivo que não esteja presente no servidor. Você deve receber uma mensagem "404 Não Encontrado".
