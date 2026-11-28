# Produto: o Argos novo

O Argos novo é um app desktop gpui onde um dev acompanha nove ou mais agentes de linha de comando ao mesmo tempo e
responde, sem abrir o terminal, o que cada um pede. O trabalho número um da tela principal é mostrar quem está
esperando o dono e deixar a resposta a um passo. Recrutar, acompanhar e dispensar vêm depois, e cada um custa menos
passos que hoje.

## Problema

O dono roda vários agentes em paralelo, cada um num terminal. A maior parte do tempo eles trabalham sozinhos. O que
custa caro é o momento em que um deles para e espera: uma permissão, uma pergunta, um plano para aprovar. Com nove ou
mais agentes vivos, achar quem espera e responder vira o gargalo.

No Argos atual (página do painel web da Hades), esse momento custa caro por quatro motivos, levantados na leitura do
código e das notas de rodada:

- **Responder exige ir ao terminal.** Só a permissão simples ("Yes") de cinco ferramentas do Claude Code é respondida
  pelo canvas; plano e pergunta pedem abrir o terminal (Hades-Skill, `reference/argos.md:121-129`). Uma pergunta
  registrada custa cerca de cinco interações.
- **Achar quem espera é procurar.** O sinal é cor, chip e borda pulsando num canvas com 176 nós gravados, dos quais 3
  ativos e 158 arquivados (notas da rodada de poda, `argos-canvas-p12-poda.notas.md:13-14`).
- **O canvas começa espremido.** Título, três faixas de abas e filtros e uma barra própria ocupam 13,5% da tela antes
  do canvas; no celular o canvas começava a 3,1% do topo (auditoria de design do Argos atual).
- **O estado é adivinhado.** Vem do estado do pane no multiplexador, de hooks do Claude Code e de heurística sobre a
  tela; gravação de canvas já foi perdida em silêncio e há terminais órfãos.

A raiz das três últimas é a dependência de duas ferramentas externas: o multiplexador de terminais para processo e
tela, e o Claude Code como único agente cujo estado o Argos entende.

## Para quem

Um dev só, o dono, na mesa, com nove ou mais agentes vivos ao mesmo tempo, de tipos diferentes (Claude Code, Codex,
Gemini CLI, OpenCode, agy e os que vierem). Ele acompanha muito pelo celular quando sai da mesa. Fala pt-BR, lê texto
técnico e quer a interface curta e direta.

## O que o Argos novo faz

- Mostra sempre a fila de quem espera o dono, com o tipo da pendência, e responde permissão, pergunta e plano ali
  mesmo.
- Aceita qualquer agente de linha de comando por um adaptador declarado em arquivo ([arquitetura.md](arquitetura.md)).
- Tem terminal próprio, desenhado pelo app, sobre sessões que sobrevivem ao fechar o app.
- Mantém o canvas, com agrupamento e zoom semântico para nove ou mais agentes, e com menos passos para recrutar,
  acompanhar, responder e dispensar.

## O que sai do Argos atual

| Sai | Por quê |
|---|---|
| Multiplexador de terminais como dependência obrigatória | Limita teclas, cursor e tamanho, lê por polling e derruba agente ao reiniciar; vira backend opcional |
| Estado lido só pelo Claude Code e pela tela | Impede outros agentes; o estado passa a vir do contrato de adaptador |
| Recrutar desenhando um retângulo e preenchendo um modal de 8 campos | Custa 4 ou mais interações para a ação mais comum depois de responder |
| Faixas de título, abas e filtros acima do canvas | Ocupam 13,5% da tela; o canvas passa a ocupar a janela |
| Nós arquivados que continuam no canvas | Poluem a busca por quem espera; o que acabou sai do canvas e fica no histórico |
| Interface no painel web | O app é gpui, como as outras ferramentas da Hades; o celular é tratado à parte ([perguntas-abertas.md](perguntas-abertas.md)) |
