# Paleta de squads

A biblioteca de squads como paleta flutuante do canvas. Lista os squads salvos; o selecionado mostra as últimas
convocações e leva ao Histórico filtrado. Arrastar um item para o canvas solta a Planta do squad.

**Por que paleta e não tela.** Escolher um squad é parte do trabalho no canvas: a paleta fica ao lado do que está
rodando, e o histórico aparece no ponto da escolha, sem trocar de tela.

**Anatomia.**
- Painel `surface` com fio `border` e sombra `elev-float` (é flutuante), 340 px.
- Título em `display` 15 px com o ícone `users`; dica "arraste para o canvas" em `text-muted`.
- Busca em `field` de 28 px.
- Item: nome 600 13 px, papéis em `text-muted`, linha de uso em `mono-small` (vezes · custo médio · última). Itens
  separados por `divider`.
- Histórico do selecionado: até três linhas (data, alvo, resultado em `success` ou `danger`, custo) e o atalho
  "Ver as N no Histórico".
- Rodapé: "Novo squad" (fantasma) e a contagem de aposentados, que abre a lista deles.
- Arrastar: contorno tracejado `text-muted` onde a planta cai; o nó vivo que precisa sair deixa um contorno `divider`
  e uma seta tracejada até o lugar novo.

| Estado | Como fica |
|---|---|
| Normal | Fundo `surface` |
| Hover | Fundo `fill-1`, mais fraco que o selecionado |
| Selecionado | Fundo `tint-selected` e o histórico aberto; o peso do texto não muda |
| Foco (teclado) | Anel `focus` |
| Arrastando | O item segue selecionado; no canvas, o contorno de onde cai e quem se afasta |
| Proposta | Linha de uso diz "proposta" até a primeira convocação |
| Aposentado | Fora da lista principal; aberto pelo rodapé, com o nome em `text-muted` e a data |
| Manifesto inválido | O item fica, com o arquivo e o erro em `danger` e "Abrir o arquivo" |
| Vazia | Nenhum squad: diz onde eles moram e como criar |
| Busca sem resultado | Diz o que procurar (papel ou tipo de agente) |

**Teclado.** `S` abre, setas passam de item, `Enter` solta o squad no centro do quadro visível, `Esc` fecha.

**Não fazer.** Soltar por cima de um nó vivo; esconder o squad com manifesto inválido; abrir diálogo para escolher.
