# Faixa do squad

O squad convocado recolhido: o quadro da planta encolhe para uma faixa com uma célula por agente. Libera o canvas
para o resto do trabalho sem perder de vista quem do squad espera você.

**Por que recolher.** Quatro nós de 480 × 320 tomam o canvas inteiro. Na faixa, o squad ocupa 96 px de altura e
continua dizendo o estado de cada um; `F` ou Desdobrar devolve a planta com os nós vivos.

**Anatomia.**
- Quadro `room` com 96 px de altura; rótulo com o nome e o resumo em `mono-small`: início, gasto de estimado e o
  critério de pronto em números.
- Células (168 × 44) da peça de zoom distante do Nó de agente, uma por papel, na ordem da planta.
- "Desdobrar" (fantasma, ícone `maximize`) no canto direito.

| Estado | Como fica |
|---|---|
| Em andamento | Células com o estado de cada agente; quem aguarda outro papel diz o quê ("Aguarda o patch") |
| Esperando você | A célula fica `agent-waiting` / `agent-waiting-bg` com pulso; o pedido também está na Coluna do coordenador |
| Erro | Célula com fio `agent-error`; o resumo diz onde parou |
| Pronto | Todas entregues, rótulo em `text-muted`, resumo com custo final e critério cumprido |
| Hover | Só o fio do quadro escurece |
| Selecionado | Colchetes de canto em `select-mark` |
| Foco (teclado) | Anel `focus` |

**Não fazer.** Esconder a célula que espera você; somar os estados num número só; recolher sozinho um squad que
alguém está olhando.
