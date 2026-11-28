# Planta do squad

O squad desenhado no próprio canvas antes de existir: um quadro tracejado com o nome, nós tracejados por papel e cabos
com o nome do que passa de um para outro. É a mesma forma na proposta do coordenador, no squad solto esperando a tarefa
e no squad desdobrado depois da convocação.

**Por que tracejado.** Tracejado quer dizer "ainda não roda". O nó só vira um Nó de agente sólido quando o agente
nasce, então ninguém confunde um papel planejado com um terminal vivo.

**Anatomia.**
- Quadro em `room`: fio tracejado `border-hover`, rótulo em `display` 15 px sobre `canvas`, resumo em `mono-small`
  `text-muted` (estado · agentes · custo estimado).
- Nó tracejado (230 × 116): fundo `canvas`, fio tracejado `border-hover`; cabeçalho com papel em 600 13 px e o tipo
  do agente em `mono-small` à direita; corpo com Modelo e Entrega.
- Cabo: traço `cable` de 1,5 px; rótulo em `mono-small` `text-muted` sobre `canvas`, no meio do trecho reto. Com o nó
  selecionado, cabo em `cable-active` e rótulo em `text`.

| Estado | Como fica |
|---|---|
| Proposta | Tracejado `border-hover`, tipo do agente no cabeçalho |
| Mudou | Fio `info` e selo "Mudou · era …" em `info` / `info-bg`; some quando você abre o nó |
| A recrutar | O tipo dá lugar ao estado "A recrutar" (forma de Iniciando); fica assim até Convocar |
| Hover | Só o fio escurece (`text-muted`) |
| Selecionado | Colchetes de canto em `select-mark`, como no Nó de agente; cabos dele em `cable-active` |
| Foco (teclado) | Anel `focus` de 2 px |
| Convocado | Cada nó vira um Nó de agente sólido no mesmo lugar; o quadro pode recolher na Faixa do squad |

**Teclado.** `S` abre a paleta, `Enter` solta o squad no centro do quadro, `Esc` tira do canvas, `F` recolhe ou desdobra.

**Não fazer.** Nó tracejado com terminal; cor de estado no nó planejado; cabo sem rótulo quando o papel entrega um
arquivo.
