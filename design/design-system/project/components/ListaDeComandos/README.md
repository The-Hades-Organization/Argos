# Lista de comandos

A lista que completa os slash commands do agente no campo de prompt, no foco e no nó. Cada tipo de agente traz os
comandos dele (no Claude Code, `/compact`, `/model`, `/clear`...; os equivalentes no Codex, Gemini e outros): o
contrato de adaptador declara nome, descrição, argumento e, quando houver, os valores do argumento. O Argos não
interpreta o comando; ele vai ao agente como qualquer prompt.

**Anatomia.**
- Peça flutuante: `surface`, fio `border`, sombra `elev-float`, 440 px (no nó, a largura do nó menos 16 px). Abre
  para cima, alinhada à esquerda do campo, sem cobrir o que se digita.
- Cabeçalho "Comandos do <tipo>" em 11 px 600 `text-muted` e a contagem "4 de 20" em `mono`.
- Item de 27 px: nome em 12 px 600 `mono` (`/compact`), argumento em `mono` `text-muted` (`[opcional]`,
  `<obrigatório>`) e a descrição em 12 px `text-muted`, numa linha. Itens com 2 px entre si.
- Comandos do projeto (pasta de comandos que o adaptador declara, como `.claude/commands`) num grupo à parte, com
  fio `divider` e o caminho no rótulo.
- Pé com as teclas: `↑ ↓` escolhem, `Tab` ou `Enter` completam, `Esc` fecha a lista.

**Regras.**
- Abre quando o campo começa com `/`; no meio do texto, `/` é só texto. Fecha com `Esc` (o texto fica), ao apagar
  a barra ou ao completar um comando sem argumento.
- Filtra pelo que vem depois da barra: quem começa com o texto vem primeiro, na ordem do adaptador; depois quem o contém
  no meio do nome. A descrição não filtra: "co" acharia metade da lista.
- Oito itens à vista; acima disso, rola por dentro.
- Completar põe `/nome ` no campo. Se o comando leva argumento, a lista vira a assinatura: com valores declarados,
  eles viram itens (o atual marcado); sem valores, só a assinatura e se o argumento é opcional ou obrigatório.
- Com a lista aberta, `Enter` completa em vez de quebrar linha; `Ctrl+Enter` envia o que está no campo, como sempre.
- O campo é um `combobox` com `aria-activedescendant`: o foco fica no campo e o item escolhido é anunciado.
- Tipo que não declara comandos (shell): digitar `/` mostra uma vez que o tipo não declara comandos e que o `/` vai
  como texto. Comando do projeto com arquivo inválido fica fora e a lista diz qual, em `danger`; o resto carrega.

| Estado | Como fica |
|---|---|
| Aberta | Oito itens, o primeiro escolhido |
| Filtrando | Contagem "n de total"; quem começa com o texto vem primeiro |
| Sem resultado | "Nenhum comando com /texto" e que `Ctrl+Enter` manda o texto como está |
| Item hover | `fill-1`, mais fraco que o escolhido |
| Item escolhido | `tint-selected`; a descrição longa quebra em vez de cortar; o peso não muda |
| Argumento com valores | Assinatura e os valores; o atual marcado "atual" |
| Argumento livre | Só a assinatura, com "Argumento opcional" ou "obrigatório" |
| Sem comandos | Aviso de uma linha, sem lista |
| Comando do projeto inválido | Linha em `danger` com o arquivo e o motivo |

**Não fazer.** Executar comando por conta própria (quem executa é o agente); esconder comandos que o Argos não
entende; abrir a lista no meio do texto; mudar o Enter do campo quando a lista está fechada.
