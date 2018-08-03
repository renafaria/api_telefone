# README #

### Para que é esse repositório? ###

Api Python para buscar o telefone de uma empresa.

### Como faço para configurar? ###
A configuração é feita ultilizando o pip para instalar as dependencias do arquivo requirements.txt

Deve-se configurar os arquivos da pasta config/*.dist, para que o programa execute a Api.

##### Exemplo arquivo api.py: #####
```
API = {
   "host": "192.168.0.2",
   "port": "8000",
   "debug": "1"
}
```