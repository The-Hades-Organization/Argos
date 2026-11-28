# Lista de adaptadores

A lista da tela Adaptadores: os tipos de agente que o Argos sabe rodar, em dois grupos, cada um com o estado e
quantos agentes vivos o usam. Escolher um mostra o contrato dele ao lado.

**Anatomia.**
- Fundo `surface`, itens com 2 px entre si e 4 px de recuo lateral, para os realces não se fundirem.
- Rótulo de grupo fixo no topo ao rolar ("De fábrica", "Seus"), 11 px 600 `text-muted`, com a contagem em `mono`.
- Item em duas linhas: nome (13 px 600) e vivos (`mono` 11 px `text-muted`) em cima; id (`mono` 11 px) e estado
  embaixo. Uma terceira linha opcional (11 px `text-muted`) diz o que a forma não diz: "seu · substitui o de
  fábrica", "o coordenador usa", "2 vivos usam a última versão lida".
- Estado com forma e palavra, nunca só cor: pronto (`check` em `success`), não carrega (`triangle-alert` em
  `danger`), programa não encontrado, arquivo apagado e contrato mais novo (`triangle-alert` em `warn`), não lido
  (`circle-dashed`, nome em `text-muted`), testando (giro).

**Regras.**
- Não carrega leva um fio de 2 px `danger` à esquerda: na lista inteira, o quebrado se acha sem ler.
- Hover `tint-hover`, selecionado `tint-selected` (mais forte que o hover), foco por teclado com o anel por dentro.
  A seleção não muda o peso do nome.
- `↑ ↓` passam de item; digitar filtra pelo nome e pelo id, com o trecho sublinhado, como no Recrutar.
- Janela estreita (`slim`): só nome e estado.
- Grupo "Seus" vazio usa a peça Vazio: "Nenhum adaptador seu", "copie um de fábrica com Duplicar".

| Estado | Como fica |
|---|---|
| Normal | Duas linhas, sem fundo |
| Hover | `tint-hover` |
| Selecionado | `tint-selected` |
| Foco | Anel `focus` de 2 px por dentro |
| Não carrega | Fio `danger` à esquerda, estado em `danger` 600 |
| Aviso | Estado em `warn` 600 (programa não encontrado, arquivo apagado, contrato mais novo) |
| Não lido | Nome em `text-muted`, `circle-dashed` |
| Testando | Giro no lugar do ícone |

**Não fazer.** Esconder um adaptador que não carrega (ele some do Recrutar, não daqui); estado só por cor; ícone
próprio por agente na lista (o nome já identifica, e ícone de marca de terceiro não entra no app).
