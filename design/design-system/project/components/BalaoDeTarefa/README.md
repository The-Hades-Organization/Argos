# Balão de tarefa

Aparece ao soltar um squad no canvas, junto da planta: pede a tarefa e convoca. Enquanto ele está aberto, os nós da
planta ficam em "A recrutar".

**Por que balão.** A tarefa é a única coisa que falta para convocar; o resto do squad já está à vista na planta. Um
diálogo no meio da tela esconderia justamente o que você está convocando.

**Anatomia.**
- Painel `surface`, fio `border`, sombra `elev-float`, ancorado abaixo do quadro do squad.
- Título "Tarefa para <squad>" em `display` 15 px.
- Campo da tarefa (Campo, uma linha; colar uma issue preenche).
- Linha de ação: chip da worktree que será criada, custo estimado em `text-muted`, "Tirar do canvas" (fantasma) e
  "Convocar N" (primária, a única da tela neste momento) com `Enter`.

| Estado | Como fica |
|---|---|
| Vazio | Placeholder no campo; Convocar desabilitado |
| Preenchido | Convocar habilitado |
| Hover, pressionado, foco | Os do Campo e do Botão |
| Convocando | Campo desabilitado; Convocar com spinner e a mesma largura |
| Erro | Campo com fio `danger`, ajuda em `danger` dizendo quem falhou e o que não foi iniciado; ação vira "Tentar de novo" |

**Teclado.** `Enter` convoca, `Esc` fecha o balão e mantém a planta solta, `Esc` de novo tira do canvas.

**Não fazer.** Pedir de novo papéis, modelos ou diretório (já estão na planta); duas primárias.
