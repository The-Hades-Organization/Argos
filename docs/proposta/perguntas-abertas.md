# Perguntas abertas

O que esta proposta não decide. Cada pergunta traz as opções e o que cada uma custa; a escolha é do dono.

## Como o dono acompanha e responde pelo celular

O app é desktop gpui. O supervisor de sessões ([arquitetura.md](arquitetura.md#acesso-pelo-celular)) já tem o estado e
o canal de resposta de cada agente, então todas as opções partem dele.

| Opção | Como funciona | Custa | Bom para |
|---|---|---|---|
| Página no Hades-Panel | O painel web mostra a fila de "esperando você" e responde pelo supervisor | Depende do Hades-Panel, fora do escopo desta unidade; a página precisa de autenticação no supervisor | Quem já abre o painel pelo celular e pelo túnel |
| Notificação com resposta | O supervisor manda notificação push quando um agente espera; permissão e pergunta curta respondidas pela própria notificação | Serviço de push de terceiro ou próprio; resposta limitada a botões e texto curto | Responder rápido sem abrir nada |
| Página própria do supervisor | O supervisor serve uma página mínima (fila, resposta, últimas linhas do terminal) pelo túnel que a Hades já usa | Mais uma superfície de interface para manter; autenticação, limite de taxa e auditoria no supervisor | Independência do painel |
| Só leitura no celular | O celular vê estado e terminal; responder exige a mesa | Nenhum risco de aprovar comando pelo celular; perde o caso de uso principal fora da mesa | Começar pequeno |

Em todas, responder uma permissão pelo celular é aprovar um comando que o agente vai rodar na máquina. A operação
precisa de identidade conferida no supervisor, limite de taxa e registro no diário (quem, o quê, qual agente, quando).

## Trocar o modelo de um agente no meio do trabalho

Alguns agentes trocam de modelo sem reiniciar a sessão; outros só aceitam o modelo na linha de comando. O contrato de
adaptador ([arquitetura.md](arquitetura.md#contrato-de-adaptador)) ainda não declara essa troca, e a tela de foco
não a oferece.

| Opção | Como funciona | Custa |
|---|---|---|
| Parte opcional nova do contrato | O adaptador declara como pedir a troca (comando dentro da sessão, tecla, argumento de retomada) e como confirmar que ela pegou; o foco ganha "Trocar modelo", desabilitado com o motivo quando o adaptador não declara | Uma sétima parte no contrato, um estado "trocando" com prazo e o caso da troca que não confirma |
| Recrutar de novo com outro modelo | O dono dispensa e recruta com o modelo novo, retomando a sessão quando o adaptador sabe retomar | Nada novo no contrato; perde o que não estiver salvo na sessão |
| Fora do Argos | O dono troca pelo próprio terminal do agente, com o teclado no terminal | Nada; o rodapé do nó mostra o modelo só quando o adaptador o lê de novo |

