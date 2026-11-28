# Botão

Botão de texto ou de ícone; a primária é uma só por tela e diz o que acontece.

**Anatomia.** Altura `control-sm` (28) na coluna e no nó, `control-md` (32) em diálogo. Rótulo em `label` (12/16 600),
verbo no infinitivo ("Aprovar plano", "Recrutar 3"). Tecla de atalho opcional à direita, em `kbd`.

| Variante | Quando | Tokens |
|---|---|---|
| Primária | A ação que o dono mais faz naquela decisão. Uma por tela | `primary`, `on-primary`, `primary-hover`, `primary-pressed` |
| Secundária | Alternativas da mesma decisão ("Pedir mudança", "Negar") | `fill-1`, `border`, `border-hover`, `tint-pressed` |
| Fantasma | Sair sem decidir ("Cancelar", "Ver todos") | `tint-hover`, `tint-pressed`, `text-muted` |
| Ícone | Ação de barra (zoom, enquadrar, ferramenta do canvas). Sempre com nome acessível | `tint-hover`, `tint-selected` |

**Estados.** Seguem as regras de interação do README: hover só escurece o fio (com borda) ou põe `tint-hover` (sem
borda); foco é o anel azul de 2 px e só aparece por teclado; desativado usa `text-disabled`; carregando mantém a
largura exata e troca o rótulo pelo giro, para nada pular. Botão de ícone que liga e desliga (ferramenta do canvas)
tem também **selecionado**, em `tint-selected`.

**Não fazer.** Duas primárias na mesma decisão; primária em rosa de "esperando você"; rótulo genérico ("OK", "Enviar").
