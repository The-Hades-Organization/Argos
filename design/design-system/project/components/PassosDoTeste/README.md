# Passos do teste

O progresso de "Testar" na tela Adaptadores: um agente de prova sobe num terminal à parte e cada passo do contrato é
conferido em ordem.

**Anatomia.**
- Lista numerada (`ol`) de cinco passos: iniciou o processo, sinal de pronto, mandou o prompt de prova, leu o
  estado, leu custo e contexto. Coluna de 16 px com a forma, texto 12 px, tempo em `mono` 11 px à direita.
- Formas: concluído `check` em `success`; em andamento, giro, texto 600 e "14 s de 120"; falhou `circle-x`, texto
  `danger` 600, motivo embaixo e as últimas quatro linhas do terminal; à espera `circle-dashed` em `text-disabled`.
- Resultado no topo depois do fim: "Passou · 14h05" com tempo e custo, ou "Falhou no <passo>".

**Regras.**
- Falhou num passo: os seguintes viram "não testado", nunca "ok".
- Passo opcional que o adaptador não declara (custo e contexto no shell) não entra na lista.
- O custo aparece só ao fim, junto do resultado.
- Com movimento reduzido, o giro vira o círculo tracejado parado e o texto em 600 marca o passo atual.

| Estado | Como fica |
|---|---|
| Rodando | Concluídos com `check`, o atual com giro e tempo, o resto tracejado |
| Passou | Resultado `success`, os cinco com `check` |
| Falhou | Resultado `danger`, passo com motivo e últimas linhas, os seguintes "não testado" |

**Não fazer.** Barra de progresso em percentual (os passos não duram o mesmo); esconder as linhas do terminal na
falha.
