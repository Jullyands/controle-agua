# Controle de Níveis de Água
### Autor: Anna Jullya

Este projeto em python foi feito para praticar o uso de biblioteca e comandos como **colorama**, **fore** e **style**. O programa será executado normalmente no terminal, sem exigir valor de entrada. O valor é alterado dentro do código.

A linha 5 inicia a lista com as mensagens, as mensagens aparecem coloridas na tela por conta do comando que aparece na terceira linha **"from colorama import Fore, Style"**.

Na linha 16, o **"valor_definido"** é o valor que substitui a entrada, para mostrar outra mensagem é necessário alterar esse valor.

Na linha 18, **"resposta"** utiliza o **"valor_definido"** para encontrar, com a função, a mensagem. A função utiliza **"[nivel-1]"** para que o código considere que a linha 6 é o nível 1, com a ausência da conta a resposta entregaria a mensagem o próximo nível.

O programa é orientado no final para resetar o comando de cores após executado, evitando que as próximas mensagens no terminal apareçam coloridas.
