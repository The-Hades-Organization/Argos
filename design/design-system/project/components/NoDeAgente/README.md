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
| Hover | Só o fio escurece (`border-hover`) |
| Selecionado | Colchetes de canto em `select-mark`, 7 px para fora; os cabos dele em `cable-active` |
| Foco (teclado) | Anel `focus` de 2 px; com seleção, os dois aparecem juntos |
| Zoom distante | Vira célula (168 × 44): nome e estado, na mesma posição. Esperando e erro mantêm fio e fundo do estado |

**Não fazer.** Seleção em cor de estado; sombra no nó; esconder o estado quando o nó encolhe.
