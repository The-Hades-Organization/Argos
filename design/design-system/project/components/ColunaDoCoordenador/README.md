# Coluna do coordenador

Coluna fixa à esquerda da tela principal, com 392 px: o pedido ao time em cima, a caixa de decisões no meio e os
atalhos embaixo.

**Anatomia.** Fundo `surface`, fio `border` à direita. Cabeçalho com "Coordenador" em `panel-title` (Marcellus) e o
estado do agente coordenador. Campo de pedido ao time (Campo, várias linhas). "Decisões" com Contador e a lista de
Decisão, da mais antiga à mais nova; a de cima abre inteira, as outras ficam recolhidas no cabeçalho. Rodapé com os
atalhos em `kbd`.

| Estado | Como fica |
|---|---|
| Com decisões | A primeira aberta; `J`/`K` passam e o canvas enquadra |
| Vazia | "Ninguém espera você." em `section`, com o número de agentes ativos; nada de ilustração |
| Coordenador trabalhando | Estado "Trabalhando · 4s" no cabeçalho; a conversa aparece entre o campo e as decisões |
| Coordenador com erro | Campo desativado com o motivo e "Recrutar outro"; as decisões dos agentes continuam respondíveis |

**Regra.** A caixa de decisões nunca depende do coordenador: se ele cair, o dono ainda responde os agentes.
