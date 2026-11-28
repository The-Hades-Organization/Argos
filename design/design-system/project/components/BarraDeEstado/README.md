# Barra de estado

Faixa de 26 px no pé da janela com o que vale para tudo: o supervisor, quantos agentes, quantos esperam você, o custo
do dia e a hora.

**Anatomia.** Fundo `surface`, fio `border` em cima, texto `caption` em `text-muted`; números em `mono` tabular.

| Estado | Como fica |
|---|---|
| Normal | Ponto `success` + "Supervisor ligado" |
| Sem supervisor | Triângulo e texto em `danger`: "Supervisor desligado · reconectando", e a hora do último estado. Única situação que vale para o app inteiro |
| Custo alto | O custo do dia em `warn`, com o limite ("acima de US$ 10,00") |

**Regra.** Problema de um agente vai para a caixa de decisões ou para o nó, nunca para a barra.
