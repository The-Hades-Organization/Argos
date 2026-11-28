# Seção do contrato

Uma das sete partes do contrato do adaptador, em leitura humana: Identidade, Iniciar, Mandar prompt, Comandos, Ler
estado, Responder, Custo e contexto. A tela só lê; o arquivo é a fonte.

**Anatomia.**
- Fio `divider` em cima; título 12 px 600; "opcional" em 11 px `text-muted` nas cinco partes não obrigatórias.
- À direita, quando uma mudança no arquivo vale: "vale na hora para os vivos" (Ler estado, Responder, Comandos,
  Custo e contexto) ou "vale para os próximos recrutas" (Identidade, Iniciar, Mandar prompt).
- Corpo na lista do Painel de detalhes (`dl`), com rótulo de 132 px em 12 px `text-muted` e valor em `mono`
  quando é comando, tecla, caminho ou padrão. Fonte do sinal (eventos, arquivo de sessão, padrão de tela) numa
  linha de 11 px `text-muted` sob o valor.
- Texto longo quebra em qualquer ponto: comando de doze argumentos e padrão de 140 caracteres aparecem inteiros.

**Regras.**
- Depois de uma recarga, a seção que mudou ganha o ponto `info` no título e a etiqueta vira "aplicado aos 3 vivos ·
  14h05" (em `info` 600, com `check`) nas partes que valem na hora.
- Campo inválido: linha de erro `danger` com arquivo, linha e campo ("linha 14 · responder.permissao: falta a tecla
  de 'sempre'"), e o valor com problema em `danger`. Nada cai num padrão em silêncio.
- Parte ausente não some: uma linha em `text-muted` diz a consequência ("O nó e o foco não mostram custo").

| Estado | Como fica |
|---|---|
| Normal | Título, etiqueta, lista |
| Recarregada | Ponto `info` no título; etiqueta "aplicado aos N vivos · hora" |
| Campo inválido | Linha de erro com linha e campo; valor em `danger` |
| Ausente | "Não declarada." e a consequência |

**Não fazer.** Campo editável (a edição é no arquivo); esconder a parte ausente; cortar comando ou padrão com
reticências.
