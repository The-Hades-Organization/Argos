# Linha da sessão

Uma linha de 30 px entre o cabeçalho do foco e o terminal, com o mínimo da sessão sempre à vista: modelo e esforço,
custo, contexto, branch, diretório e squad. Existe para o terminal ficar com o resto da altura e da largura, sem
painel ao lado (direção A da Q22).

**Anatomia.**
- Faixa `surface` com fio de baixo `border`, texto em 11 px `mono` `text-muted` com números tabulares. Rótulo
  "contexto" em `sans`; o resto são valores, sem rótulo, porque o formato já diz o que são.
- Itens nesta ordem, com 16 px entre eles: modelo · esforço, custo, contexto (número e barra de 2 px por 40 px),
  branch, diretório (com Copiar), squad.
- Diretório leva o espaço que sobra e corta **no começo** (`direction: rtl` com `<bdi>`): o fim do caminho é o que
  distingue duas worktrees. O caminho inteiro fica no `title` e no balão.
- Squad é um botão fantasma pequeno (`btn ghost xs`) que abre o brief; o nome corta no fim, até 34% da linha.

**Regras.**
- Campo que o adaptador não declara some, e os outros não mudam de ordem. Nada de "US$ 0,00" ou "—".
- Contexto de 90% em diante: número, "quase cheio" e barra em `agent-error`, peso 600, igual ao rodapé do nó.
- Área do foco abaixo de 900 px: a linha guarda modelo, custo e contexto; branch, diretório e squad vão para o
  balão, e o fim da linha ganha "Detalhes I". Em qualquer largura, `I` abre e fecha o balão.
- "Copiar" tem largura mínima fixa: virar "Copiado" (com `check` em `success`) por 2 s não empurra o diretório.
- Nada aqui se edita.

| Estado | Como fica |
|---|---|
| Normal | Seis itens, diretório cortando no começo se faltar espaço |
| Janela estreita | Três itens e "Detalhes I" à direita |
| Detalhes aberto | Botão com `tint-selected`, `aria-expanded="true"` |
| Contexto alto | 90% ou mais em `agent-error` com "quase cheio" |
| Campo faltando | O item some (shell: só diretório) |
| Fora de squad | O botão do squad some; o diretório leva o espaço |
| Copiar, Squad, Detalhes | Hover `tint-hover`; foco por teclado com o anel; pressionado `tint-pressed` |

**Não fazer.** Cortar o fim do diretório; quebrar a linha em duas (ela tem altura fixa, para o terminal não mudar
de tamanho quando um valor cresce); pôr ali o estado do agente, que já está no cabeçalho.
