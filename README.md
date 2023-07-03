# Bot Feliz Aniversário - Facebook

Este é um script em Python para postar mensagens de feliz aniversário na sua própria linha do tempo do Facebook. O script verifica os amigos que estão aniversariando no dia atual e seleciona uma mensagem aleatória para enviar a cada um deles.

## Pré-requisitos

- Python 3.x
- Biblioteca `facebook-sdk` instalada. Você pode instalá-la usando o seguinte comando:

````pip install facebook-sdk  ````



## Configuração

1. Obtenha um token de acesso do Facebook para autenticação. Você pode criar um aplicativo no [Facebook Developers](https://developers.facebook.com) e gerar um token de acesso com as permissões necessárias.
2. Substitua `'YOUR_ACCESS_TOKEN'` pelo seu próprio token de acesso no arquivo `bot_feliz.py`.

## Uso

1. Execute o script `bot_feliz.py` no seu terminal ou IDE Python.
2. O script irá verificar os amigos aniversariantes no dia atual e postar uma mensagem de feliz aniversário na sua própria linha do tempo do Facebook.

## Customização

- Você pode adicionar suas próprias mensagens de feliz aniversário no script. Basta adicionar as mensagens desejadas na lista `frases` do arquivo `bot_feliz.py`.
- Se desejar postar em uma página que você administra, em vez da sua própria linha do tempo, você precisará obter um token de acesso com as permissões adequadas para a página e modificar a função `postar_mensagem_aniversario` no arquivo `bot_feliz.py` para usar a ID da página em vez de `"me"`.

## Limitações

Lembre-se de que a API do Facebook não permite mais postagens automáticas em nome dos usuários em suas linhas do tempo. Portanto, o script postará as mensagens na sua própria linha do tempo.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas, bugs ou tiver sugestões de melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

