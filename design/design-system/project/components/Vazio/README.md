# Vazio

O que aparece no lugar de uma lista, de uma área ou do canvas quando não há nada a mostrar, ou quando o que
deveria estar ali não pôde ser lido. Diz o que falta e a próxima ação, nunca só "nada aqui".

**Anatomia.**
- Na lista ou na coluna: fio tracejado `border-hover`, título 13 px 600 `text`, texto 12 px `text-muted`, ação
  fantasma opcional. Encosta à esquerda.
- No canvas (`big`): cartão `surface` com fio `border`, centrado no canvas; título 24/30 na fonte de exibição,
  texto 13 px `text-muted`, uma ação primária e, na primeira vez, um exemplo do que pedir ao coordenador, em `mono`,
  sob um fio `divider`.
- Janela estreita ou depois de uso (`big slim`): título 18/24, uma frase e a ação. Sem exemplo.
- Tela de falha (`big fail`): no lugar do canvas, quando o app não tem estado nenhum para mostrar. Fio de 2 px
  `danger` à esquerda, ícone `triangle-alert` em `danger` antes do título, o motivo e o caminho do log numa lista
  (`dl`) com Copiar, e "Tentar de novo" como primária. Anuncia ao leitor de tela (`role="alert"`).

**Regras.**
- Uma ação primária no máximo, e ela é a que resolve (Recrutar, Tentar de novo).
- O vazio da primeira vez é enxuto: uma frase, Recrutar e o exemplo. Sem tour nem passos.
- Vazio depois de uso não repete a explicação; aponta onde o que saiu foi parar (Histórico).
- Falha que deixa ver alguma coisa usa a Faixa no topo da área, não esta tela.

| Variante | Como fica |
|---|---|
| Lista ou coluna | Tracejado, à esquerda, ação fantasma |
| Canvas · primeira vez | Cartão central, título de exibição, Recrutar e o exemplo |
| Canvas · depois de uso, estreito | Cartão menor, uma frase e Recrutar |
| Tela de falha | Fio `danger`, ícone, motivo, log com Copiar, Tentar de novo |

**Não fazer.** Ilustração ou mascote; "Nada por aqui!"; duas primárias; esconder o caminho do log na falha.
