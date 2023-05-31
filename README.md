## Portabilidade de dados:

#### Premissas:

- Ter acesso configurado no servidor remoto (SSHKey's)

- Transferência via SCP estará restrita apenas aos usuários de origem e destino (clientes) conectados ao servidor

------------

#### Cliente que está enviando dados

1 - Executar script de busca de usuário e exportar JSON com os dados desse usuário;

2 - Executar o comando: 
```
scp C:\Caminho\Arquivo.json [usuario de destino]@[ip do servidor]:/[caminho destino no servidor]
```
3 - Após envio do arquivo para o servidor, é de reponsabilidade desse cliente apagar a cópia local dos dados portados (JSON com dados do usuário) e remover usuário do banco de dados.

--------------

#### Cliente que está recebendo dados

1 - Executar o comando:

```
scp [usuario de origem]@[ip do servidor]:/[diretorio de origem]/Arquivo.json [local destino]
```

2 - Arquivo deve estar listado no diretório de destino;

3 - Executar Script que cadastra os dados do JSON enviado no banco desse cliente;

4 - Após os passos anteriores o cliente que recebeu arquivo deve executar o seguinte comando dentro do diretório /portabilidade no servidor:
```
rm [nomearquivo].json
```

--------------

OBS: Substituir conteúdo dentro de [ ] para execução dos comandos.
