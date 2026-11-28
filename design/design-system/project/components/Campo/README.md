# Campo

Campo de texto de uma linha (resposta livre) ou de várias (pedido ao coordenador), sempre com o ícone do que ele faz.

**Anatomia.** Fundo `fill-1`, fio `border`, altura `control-md` (32) na versão de uma linha e 56 no mínimo na de
várias. Texto de exemplo em `text-placeholder`, mais claro que `text-muted`, para nunca parecer digitado. `Enter`
envia; `Shift+Enter` quebra linha no pedido ao time.

| Estado | Como fica |
|---|---|
| Vazio | Exemplo em `text-placeholder` dizendo o que cabe ali |
| Hover | Só o fio escurece (`border-hover`) |
| Foco | Anel `focus` de 2 px, só por teclado; com o mouse o cursor basta |
| Preenchido | Texto em `text` |
| Desativado | Fio `divider`, texto `text-disabled`, sem hover |
| Erro | Fio `danger` e a mensagem embaixo, dizendo o que houve e o que fazer |

**Não fazer.** Rótulo só dentro do campo (o exemplo some ao digitar); erro só pela cor do fio.
