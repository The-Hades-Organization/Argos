# Painel de detalhes

Balão com o que a linha da sessão não mostra inteiro: modelo e esforço, diretório inteiro com Copiar, branch,
quando começou e o squad com o brief. Abre com `I` ou com "Detalhes" na linha da sessão.

**Anatomia.**
- `balloon` do bundle (superfície, fio `border`, sombra `elev-float`), 380 px, sem título: o botão que o abriu já
  diz o que é.
- Lista em duas colunas: rótulo de 76 px em 11 px 600 `text-muted`, valor em 12 px `text`. Modelo, caminho e
  branch em `mono`; caminho longo quebra em qualquer ponto (`overflow-wrap: anywhere`): no balão nada corta.
- Cinco linhas, nesta ordem: Modelo (· esforço), Diretório (com Copiar), Branch, Iniciado, Squad (com "Abrir
  brief"). Tipo e estado estão no cabeçalho do foco; custo e contexto, na linha da sessão.
- Ações da linha são botões fantasma pequenos (`btn ghost xs`, 22 px) numa coluna à direita: o valor quebra na
  coluna dele e a ação não desce.

**Regras.**
- Ancorado no botão Detalhes: canto superior direito 4 px abaixo da linha da sessão, alinhado ao fim dela. Com a
  janela larga (sem o botão), `I` abre no mesmo lugar.
- É um diálogo leve: recebe o foco na primeira ação, fecha com `Esc`, `I` ou clique fora e devolve o foco a quem o
  abriu. Não bloqueia o terminal nem a coluna do coordenador.
- Campo que o adaptador não declara some da lista.
- "Copiar" com largura mínima fixa; "Copiado" por 2 s.

| Estado | Como fica |
|---|---|
| Normal | Cinco linhas |
| Campo faltando | A linha some (shell: diretório e iniciado) |
| Texto longo | Caminho e branch quebram dentro da coluna do valor |
| Copiar | Hover `tint-hover`; foco por teclado com o anel; pressionado `tint-pressed`; "Copiado" por 2 s |

**Não fazer.** Esconder o diretório atrás de reticências aqui (é o único lugar onde ele aparece inteiro); pôr campo
editável; repetir custo e contexto, que já estão na linha.
