# Histórico de pendências

O que este agente já pediu e o que foi respondido, mais recente primeiro. Mostra também quem respondeu, porque o dono
responde do canvas, do celular e pela CLI, e o coordenador aprova alguns planos sozinho.

**Anatomia.**
- Mesma seção do painel de detalhes (`isec`), com o cabeçalho "Pendências" e, à direita, o total respondido.
- Linhas sem caixa, separadas por `divider`:
  - linha 1: tipo em `mono-small` `text-muted` · resumo em 12 px (até duas linhas, corta com reticências) · hora à
    direita em `mono` `text-muted` ("14h05");
  - linha 2: "→ resposta" com a resposta em 600 · quem respondeu em `text-muted` ("por você", "pelo celular", "pelo
    coordenador", "pela CLI").
- Coluna do tipo com largura fixa (64 px), para os resumos alinharem.
- Pé com "Ver todas" em botão fantasma quando o total passa de seis (as seis últimas ficam no painel).

**Regras.**
- A pendência que ainda espera resposta não entra aqui: ela fica no topo do painel como Decisão. O histórico só tem
  o que já foi respondido.
- Abrir uma linha (clique ou `Enter`) mostra o texto inteiro e, se houver, o comando em bloco `term-bg`. Abre uma de
  cada vez.
- Hover `tint-hover`; foco por teclado com anel interno de 2 px (`focus`), para não ser cortado pelas linhas
  vizinhas; aberta em `fill-1`.
- Vazio usa a peça `.empty` com "Nenhuma pendência ainda". Erro ao ler o diário diz o que falhou e oferece "Tentar de
  novo"; o botão mantém a largura com o giro enquanto tenta, e o resto do foco segue funcionando.

| Estado | Como fica |
|---|---|
| Normal | Até seis linhas e "Ver todas" |
| Hover / foco | `tint-hover` / anel interno |
| Aberta | `fill-1`, texto inteiro e o comando |
| Vazio | Peça vazia com ícone `history` |
| Erro | `triangle-alert` em `danger`, frase do que falhou e "Tentar de novo" |
| Tentando | Giro no lugar do rótulo, mesma largura |

**Não fazer.** Misturar a pendência aberta com as respondidas; esconder quem respondeu; abrir várias linhas de uma
vez.
