# Trilho

Barra vertical de 56 px à esquerda, escura nos dois temas (`rail`), com a marca do Argos e cinco destinos: Canvas,
Squads, Histórico, Adaptadores e Configuração.

**Anatomia.** Ícones de 16 px em botões de 36 × 36, texto `on-rail`. O destino atual em `on-rail` a 12% de fundo. O
contador de "esperando você" fica sobre o ícone do Canvas, em `agent-waiting`. Configuração fica no pé.

**Estados.** Normal a 72% de opacidade; hover e selecionado a 100%; foco com o anel `focus`. Cada botão tem nome
acessível e dica com o nome. O trilho não abre em texto: os cinco destinos cabem em ícone, e o nome aparece na dica.
