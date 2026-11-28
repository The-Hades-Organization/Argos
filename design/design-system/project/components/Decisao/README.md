# Decisão

Cartão de uma pendência na caixa de decisões: quem pede, o quê, há quanto tempo, e as respostas, com a recomendada
primeiro.

**Anatomia.**
- Cabeçalho em `agent-waiting-bg`: ponto de estado, nome do agente, tipo · projeto em `mono-small`, idade à direita.
- Corpo em `canvas`, padding `space-3`. A pergunta em `body`; identificadores em Chip; comando em bloco `term-bg`
  com fio `border`, para não sumir no cartão no tema escuro.
- Coluna única que não cresce com o conteúdo: nome longo corta com reticências e comando largo quebra, sem alargar
  a caixa de decisões.
- Respostas: botões (permissão, plano, proposta) ou opções numeradas (pergunta). Teclas `1` a `9` escolhem; `Enter`
  aceita a recomendada.

| Tipo | Respostas |
|---|---|
| Permissão | Permitir uma vez · Sempre neste projeto · Negar |
| Pergunta | Opções do agente, a recomendada primeiro e marcada; texto livre embaixo |
| Plano | Passos numerados com o desvio de cada um ("se falhar, segue para"); Aprovar plano · Pedir mudança · Recusar |
| Proposta | O que o coordenador vai fazer, com custo estimado; Aceitar · Mudar · Cancelar |

| Estado do cartão | Como fica |
|---|---|
| Na fila | Fio `border` |
| Em foco (`J`/`K`) | Fio `agent-waiting`, ponto pulsando; o canvas enquadra o agente |
| Respondendo | O botão usado mostra o giro sem mudar de largura; os outros ficam desativados |
| Respondida | Sai da caixa; o agente volta a "Trabalhando" |

**Opção.** Linha com número, título em `body-strong` e descrição em `small`. A recomendada tem `tint-selected` e o
selo "Recomendada" com `check`; nunca é aplicada sem o dono. Hover escurece o fio; foco é o anel azul; escolhida tem
fio `text`; desativada usa `text-disabled`.

<!-- foco: pendência no pé -->
**No pé do foco (recolher, `M`).** No foco de um agente, a pendência atual encaixa no pé do terminal como esta peça
deitada. A cabeça ganha "Recolher M" depois da idade (`btn ghost xs` com `chevron-right` girado para baixo).
Recolhida, fica só a cabeça (`.dec.folded`): ponto pulsando, nome, tipo, o resumo numa linha em `mono` `text-muted`
(comando, começo da pergunta ou número de passos), a idade e "Expandir M". Nada some: o cabeçalho do foco continua
rosa, a coluna do coordenador mostra a mesma decisão, e `1 2 3` respondem com ela recolhida. O Argos lembra a escolha
para todos os agentes: a próxima pendência chega recolhida, com o fio rosa de entrada.
<!-- fim: pendência no pé -->
