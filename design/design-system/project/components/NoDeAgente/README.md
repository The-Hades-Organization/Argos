# Nó de agente

A peça do canvas que mostra um agente: cabeçalho com nome, tipo e estado; terminal ao vivo; rodapé com modelo, custo e
contexto.

**Anatomia.**
- Cabeçalho em `node-header`: nome em `node-title`, tipo em `mono-small`, estado à direita.
- Corpo em `term-bg` com `term`/`mono`; o terminal é escuro nos dois temas.
- Rodapé em `mono-small`, números tabulares: modelo · esforço à esquerda, custo · contexto à direita.
- Tamanho padrão `node-agent-w` × `node-agent-h` (480 × 320) a 100%; sem sombra, separado por fio.

| Estado | Como fica |
|---|---|
| Iniciando, trabalhando, ocioso | Fio `border`, só o indicador muda |
| Esperando você | Faixa de 3 px no topo, fio e cabeçalho em `agent-waiting` / `agent-waiting-bg`, pulso no ponto |
| Erro | Fio `agent-error`; o rodapé troca o custo por "Ver as últimas linhas" |
| Encerrado | Nome e tipo em `text-disabled`, corpo em `fill-1`; sai do canvas ao ir para o histórico |
| Esqueleto | Abrindo um canvas que passa de 1 s: o nó na posição e no tamanho salvos, com nome e tipo, "Lendo", e barras no lugar do terminal e do rodapé. Sem tela branca; com movimento reduzido as barras não pulsam |
| Desatualizado | O supervisor não responde: o último estado lido, sem pulso, com a marca `circle-dashed` e a hora ("às 14h31"); terminal em `term-muted` com "Parado na tela de 14h31 · não aceita digitação" no pé; rodapé em `text-disabled`. Mantém fio e fundo do estado, para quem esperava continuar à vista |
| Hover | Só o fio escurece (`border-hover`) |
| Selecionado | Colchetes de canto em `select-mark`, 7 px para fora; os cabos dele em `cable-active` |
| Foco (teclado) | Anel `focus` de 2 px; com seleção, os dois aparecem juntos |
| Zoom distante | Vira célula (168 × 44): nome e estado, na mesma posição. Esperando e erro mantêm fio e fundo do estado |

<!-- peças:inicio -->
## Peças do rodapé e do terminal

**Barra de contexto.** Fio de 2 px no pé do rodapé, da esquerda, na largura do contexto usado; em `text-muted`. De
90% em diante, fio e número em `agent-error` com "quase cheio" e peso 600. Fica só no nó: não entra na caixa de
decisões. Adaptador que não declara contexto mostra "contexto não informado", nunca zero.

**Linhas novas.** Quando o dono rolou o terminal para cima e chega saída, aparece "↓ N linhas novas" no canto de
baixo do terminal, em `surface` com fio `border`. Clique ou `Enter` (com foco) volta ao fim e o aviso some. Hover
escurece o fio (`border-hover`); foco por teclado tem o anel `focus`.

**Campo de prompt.** Com o nó selecionado, `P` abre o campo no lugar do rodapé, já em foco (fio `focus`, fundo
`fill-1`, texto de exemplo em `text-placeholder`). Cresce até quatro linhas tomando altura do terminal, então o nó
não muda de tamanho; passou disso, rola dentro. Como em todo campo de prompt do Argos, `Enter` quebra linha e
`Ctrl+Enter` envia; `Esc` fecha sem enviar. Enviar fecha o campo na hora (o texto vai ao terminal), então não há
estado de carregando. Nó encerrado não abre o campo.

**Teclado no terminal.** Um clique no corpo dá o teclado ao agente: o nó ganha o anel de foco e o rodapé troca por
"Teclado no terminal", com `Ctrl+]` ou clique fora para voltar ao canvas. `Esc` fica com o agente.
<!-- peças:fim -->

**Não fazer.** Seleção em cor de estado; sombra no nó; esconder o estado quando o nó encolhe.
