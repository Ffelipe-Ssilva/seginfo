## Portabilidade de dados:

#### Premissas:

- Ter acesso configurado no servidor remoto (SSHKey's)

- Transferência via SCP estará restrita apenas aos usuários de origem e destino (clientes) conectados ao servidor

------------

#### Cliente que está enviando dados

1 - Digitar o comando: 
```
scp C:\Caminho\Arquivo.json [usuario de destino]@[ip do servidor]:/[caminho destino no servidor]
```

--------------

#### Cliente que está recebendo dados

1 - digitar o comando:

```
scp [usuario de origem]@[ip do servidor]:/[diretorio de origem]/Arquivo.json [local destino]
```

2 - Arquivo deve estar listado no diretório de destino

-----------

#### Após baixar o arquivo:

1 - Cliente que recebeu arquivo deve executar o seguinte comando dentro do diretório /portabilidade no servidor:

```
rm [nomearquivo].json
```

--------------

OBS: Substituir conteúdo dentro de [ ] para execução dos comandos.