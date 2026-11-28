# Painel de detalhes

Lista do que se sabe de um agente, no painel da direita do foco: de onde veio, onde trabalha, quanto já custou. É a
única peça que mostra tudo junto; o nó e a caixa de decisões mostram só o que muda a próxima ação.

**Anatomia.**
- Seção com cabeçalho fixo (`isec-h`): rótulo em 12/16 600 e, à direita, contagem ou ação. O mesmo cabeçalho serve
  ao histórico de pendências, então as seções do painel rolam juntas e o rótulo de cada uma fica à vista.
- Lista em duas colunas: rótulo de 88 px em 11 px 600 `text-muted`, valor em 12 px `text`. Identificador, caminho,
  branch e custo em `mono`; caminho longo quebra em qualquer ponto (`overflow-wrap: anywhere`) em vez de alargar o
  painel ou cortar o fim, que é a parte que distingue dois diretórios.
- Linhas, nesta ordem: tipo (com "Ver adaptador"), modelo, esforço, diretório (com "Copiar"), branch, iniciado,
  custo, contexto (número e barra de 2 px), squad · papel · convocação (com "Abrir brief").
- Ações da linha são botões fantasma pequenos (`btn ghost xs`, 22 px) numa coluna própria à direita: o valor
  quebra na coluna dele e a ação não desce de linha.

**Regras.**
- Campo que o adaptador não declara some da lista. Aqui a linha ausente não vira "não informado": o painel lista o
  que existe; quem precisa saber o que falta é a configuração do adaptador.
- Contexto: barra em `text-muted` na largura do uso; de 90% em diante, barra e número em `agent-error`, peso 600 e
  "quase cheio", igual ao rodapé do nó.
- "Copiar" tem largura mínima fixa: trocar para "Copiado" (com `check` em `success`) não mexe no valor ao lado. Volta
  a "Copiar" em 2 s. Sem ícone de copiar: o conjunto de ícones não tem um, e a palavra basta.
- Nada aqui se edita. Trocar modelo ou esforço fica fora do foco (pergunta aberta no contrato de adaptador).

| Estado | Como fica |
|---|---|
| Normal | Todas as linhas que o adaptador declara |
| Campo faltando | A linha some; as outras não mudam de lugar entre si |
| Texto longo | Caminho e branch quebram dentro da coluna do valor |
| Contexto alto | 90% ou mais em `agent-error` |
| Copiar | Hover `tint-hover`; foco por teclado com o anel; pressionado `tint-pressed`; "Copiado" por 2 s |

**Não fazer.** Esconder o diretório atrás de reticências (o fim do caminho é o que importa); pôr campo editável no
painel; mostrar "0" ou "—" para o que o adaptador não informa.
