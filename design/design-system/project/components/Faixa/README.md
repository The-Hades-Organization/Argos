# Faixa

Aviso de largura inteira no topo de uma área: o que aconteceu com o que você está olhando e, se houver, a ação que
resolve. Usada na tela Adaptadores (recarga, não carrega, pasta ilegível) e nos estados de erro do app.

**Anatomia.**
- Fio de 2 px à esquerda na cor do tom e fundo `*-bg` do mesmo tom; ícone de 16 px na cor do tom; texto 12 px
  `text` com a primeira frase em 600; complemento em `text-muted`.
- Ação opcional à direita, botão fantasma pequeno (`btn ghost xs`).
- Tons: info (`refresh-cw`, recarga), sucesso (`check`), aviso (`triangle-alert` em `warn`), erro
  (`triangle-alert` em `danger`).

**Regras.**
- Erro anuncia ao leitor de tela (`role="alert"`); os outros tons, `role="status"`.
- Fica no fluxo, não flutua: empurra o conteúdo, sem sombra. O que flutua e some sozinho é o aviso de baixo (toast).
- Uma faixa por área. A informação mais grave ganha o lugar.
- Texto longo quebra; caminho em `mono` quebra em qualquer ponto.

| Estado | Como fica |
|---|---|
| Info | Fio e ícone `info`, fundo `info-bg` |
| Sucesso | `success`, `success-bg` |
| Aviso | `warn`, `warn-bg` |
| Erro | `danger`, `danger-bg`, com a ação que resolve |

**Não fazer.** Faixa para o que é de um item só (vai no item); duas faixas empilhadas; fechar a faixa de erro
sem resolver.
