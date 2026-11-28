# Estado do agente

Indicador de estado: forma + palavra + número, nunca só cor.

**Anatomia.** Forma de 8 px à esquerda, texto em `caption` (11/14 500) com o tempo em números tabulares. "Esperando
você" e "Erro" vão em peso 600 e na cor do estado; os outros em `text-muted`.

**Regras.**
- O mesmo indicador aparece no cabeçalho do nó, na célula do zoom distante, na caixa de decisões e no leitor de tela.
- Só "esperando você" pulsa (1 600 ms, desligado com movimento reduzido).
- Estado vindo só de padrão de tela leva "(inferido)".
- O tempo é desde o último sinal: "Trabalhando · 12s", "Ocioso · 4 min".
