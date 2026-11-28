# Arquitetura do Argos novo

Proposta de alto nível, sem código. O Argos novo tem quatro peças: o app gpui, um supervisor de sessões que é dono dos
terminais, os adaptadores de agente (arquivos de dados, um por tipo de agente) e os contratos em disco do Hades-Core. O
herdr, o loop da Hades e o `gh` viram integrações opcionais. As decisões e as alternativas descartadas estão em
[decisoes.md](decisoes.md); o que ainda está em aberto, em [perguntas-abertas.md](perguntas-abertas.md).

## Peças e responsabilidades

| Peça | Crate | Faz | Não faz |
|---|---|---|---|
| App | `argos-app` | Desenha o canvas, os nós e o terminal; recebe teclado e mouse; mostra o que o núcleo decide | Decidir estado de agente; abrir processo |
| Núcleo | `argos-core` | Modelo do canvas, máquina de estados do agente, registro de adaptadores, leitura dos sinais, gravação do canvas | Desenhar; falar com gpui |
| Supervisor de sessões | binário próprio (proposta: subcomando `argos serve` do `argos-cli`) | Abre e mantém os PTYs dos agentes, guarda o histórico da tela, entrega bytes e eventos ao app por socket local | Interface; regra de canvas |
| CLI | `argos-cli` | Recrutar, mandar prompt, responder, dispensar, enquadrar e salvar e convocar squads pela linha de comando, para o loop da Hades e para scripts | Desenhar |

O supervisor é processo separado do app porque o agente precisa sobreviver ao app. Hoje um reinício do multiplexador
derrubou um agente (notas de rodada do Argos atual, `argos-canvas.log.md:56`); fechar ou atualizar o app não pode fazer o mesmo.
O contrário não vale: se o supervisor morre, os agentes morrem com ele. O app sobe o supervisor quando não acha um
vivo, na abertura e quando o anterior morre. O app mostra os dois casos de forma
diferente: supervisor que não responde (agentes vivos, último estado à vista, reconexão) e supervisor que morreu
(agentes encerrados com o motivo e, quando o adaptador declara retomada, recrutar de novo com a mesma sessão do
agente).

## Contrato de adaptador

Todo agente entra por um adaptador declarado em arquivo (proposta: TOML em `<config do Argos>/adapters/<id>.toml`,
com os de fábrica embutidos no binário). O núcleo lê o arquivo, valida na carga e trata o agente só pelo contrato.
Nenhum `if claude` espalhado pelo código: o comportamento específico mora no arquivo do adaptador.

O contrato tem sete partes. Só as duas primeiras são obrigatórias; as outras declaram o que o agente oferece.

| Parte | Declara | Exemplo do que cabe |
|---|---|---|
| Identidade | id, nome, ícone, versão do contrato | `codex`, "Codex", ícone, `contrato = 1` |
| Iniciar | comando, argumentos, variáveis de ambiente (por referência, nunca valor de segredo), diretório, como retomar uma sessão, prazo para o primeiro sinal de pronto | comando com `{prompt_inicial}` e `{dir}`; argumento de retomada; `prazo_pronto = 120 s` (passado o prazo sem sinal, o agente vai a erro) |
| Mandar prompt | como o texto chega ao agente | colar entre marcadores de colagem no PTY e mandar Enter; argumento de linha de comando; arquivo |
| Comandos | os slash commands nativos do agente: nome, descrição, argumento (opcional ou obrigatório, com os valores quando forem fixos) e, opcional, a pasta de comandos do projeto | `compact` com `[instruções]`; `model` com `opus`, `sonnet`, `haiku`; `.claude/commands/*.md`; ausente no shell |
| Ler estado | de onde vêm os sinais e como viram estado | eventos estruturados; arquivo de sessão; padrões de tela |
| Responder | como cada tipo de pendência é respondido | permissão: tecla de sim, de não e de "sempre"; pergunta: texto + Enter |
| Custo e contexto | onde ler tokens, custo e uso de contexto | arquivo de sessão e o leitor que o entende; ausente quando o agente não expõe |

O contrato é versionado e só cresce: campo novo entra opcional, e o leitor tolera versão maior, como o diário do
Hades-Core já faz com `v`. Adaptador com campo inválido não carrega e aparece com erro na configuração de
adaptadores; ele não cai num padrão em silêncio.

Recarga: o Argos observa a pasta de adaptadores e relê o arquivo salvo. Ler estado, Responder, Comandos e Custo e
contexto valem na hora também para os agentes vivos daquele tipo; Identidade, Iniciar e Mandar prompt só para os
recrutados depois, porque mudam como o processo nasce. Se a versão nova não carrega, os vivos seguem com a última
versão válida e o erro aparece na tela Adaptadores.

Comandos: o prompt do foco e do nó usa a lista para completar o que se digita depois de `/`, e o comando vai ao agente
pelo mesmo caminho de "Mandar prompt"; o Argos não o interpreta. O efeito volta pelos sinais de sempre (um `/model`
muda o modelo que o leitor de custo e contexto informa). Comando de projeto com arquivo inválido fica fora da lista com
o motivo; a lista do adaptador segue a regra geral: inválida, o adaptador não carrega.

### Sinais de estado, por confiança

O estado de cada agente é um destes seis: iniciando, trabalhando, ocioso, esperando você, erro, encerrado. "Esperando
você" carrega o tipo da pendência (permissão, pergunta, plano, proposta). O núcleo combina três fontes, da mais confiável
para a menos:

1. **Eventos estruturados.** O agente avisa por hook ou notificação e o evento cai no diário do Hades-Core. O Claude
   Code já faz isso pelos hooks `Notification`, `PreToolUse`, `PostToolUse` e `Stop` (Hades-Skill, `reference/argos.md:38-42`).
2. **Arquivo de sessão.** Transcript ou log que o agente grava; serve para custo, contexto e última ação.
3. **Padrões de tela.** Expressões declaradas no adaptador e aplicadas às últimas linhas do terminal. É o último
   recurso e o app mostra o estado vindo dele como inferido.

Saída do processo é sinal universal: qualquer agente, mesmo sem adaptador próprio, tem iniciando, trabalhando (houve
saída de tela nos últimos N segundos), ocioso e encerrado. O adaptador genérico "shell" usa só isso.

### Adaptadores de fábrica

Claude Code, Codex, Gemini CLI, OpenCode, agy e shell genérico. Cada um é um arquivo de dados; o dono adiciona outro
copiando um e editando, sem recompilar. O que cada agente expõe (hooks, arquivo de sessão, retomada) precisa ser
conferido agente por agente na implementação; esta proposta não afirma o que os agentes além do Claude Code oferecem.

## Terminal embutido

O Argos desenha o terminal com o próprio gpui, sobre um PTY aberto pelo supervisor. Isso tira do caminho os limites que
o multiplexador impõe hoje (Hades-Skill, `reference/argos.md`):

- teclas recusadas (Home, End, PgUp, PgDn, Delete) e cursor ausente (:3006-3011);
- tamanho por sessão em que vence o último cliente (:2684-2700);
- argumento com quebra de linha recusado (:3107-3111);
- leitura por polling, sem assinatura de saída (:2911-2922);
- tela inteira redesenhada a cada quadro (:2658-2668).

O supervisor guarda o histórico de rolagem de cada sessão e um tamanho por cliente; o app pede só o trecho visível.
Candidatos para o parser de terminal e o PTY: crates Rust maduras de emulação VT e de PTY portátil; versão e licença
(compatível com GPL-3.0) conferidas ao escolher.

## Coordenador e squads

O coordenador é um agente como os outros, recrutado por um adaptador, com um papel a mais: ele recebe os pedidos do
dono em texto e age pelo `argos-cli` (recrutar, enquadrar, dispensar, propor e salvar squad, convocar). Tudo o que ele
quer fazer e muda o canvas ou o disco chega primeiro ao dono como pendência do tipo **proposta**, na caixa de decisões.
Os termos estão em [conceitos.md](conceitos.md#coordenador-e-squads); o fluxo, em [uso.md](uso.md#squads).

Um squad é um time salvo em disco e reutilizável. Os arquivos não dependem da conversa que criou o squad: cada membro
recebe um brief autocontido, e o squad pode ser convocado meses depois por outro coordenador, ou pela CLI, com o mesmo
resultado.

### Onde fica

| Escopo | Pasta | Uso |
|---|---|---|
| Global | `<config do Argos>/squads/<id>/` | Squad que serve a qualquer projeto (revisão de PR, triagem de bug) |
| Projeto | `<work root>/.argos/squads/<id>/` | Squad especializado num módulo ou numa base de código; vence o global de mesmo `id` |

Cada pasta de squad tem um manifesto (`squad.toml`) e um brief por membro (`membros/<papel>.md`). Nada mais é lido.

### Manifesto do squad

| Campo | Obrigatório | Declara |
|---|---|---|
| `contrato` | sim | Versão do formato. Só cresce, como o contrato de adaptador |
| `id`, `nome` | sim | Identificador estável e nome mostrado |
| `especialidade` | sim | Uma frase: em que o squad é bom ("bugs de concorrência no `hades-core`") |
| `estado` | sim | `ativo` ou `aposentado` |
| `revisao` | sim | Número que sobe a cada edição gravada; a convocação registra a revisão usada |
| `entrada` | sim | O que a convocação pede: a tarefa em texto e o diretório; branch e referências são opcionais |
| `membros` | sim | Lista de membros: `papel`, `adaptador`, `modelo`, `esforco`, `brief` (caminho do brief), `le` (o que lê), `entrega` (o que produz e onde), `depende_de` (papéis cuja entrega ele espera) |
| `pronto_quando` | sim | Critério de pronto do squad inteiro, verificável sem perguntar ao coordenador |
| `orcamento` | não | Custo máximo estimado por convocação, em US$; passar dele vira pendência |

Variáveis de ambiente entram por referência, nunca por valor, como no adaptador. Segredo não entra em arquivo de
squad.

### Brief do membro

Markdown com seções fixas, para que o núcleo confira a estrutura ao carregar:

| Seção | Conteúdo |
|---|---|
| Objetivo | O que este papel faz no squad, numa frase |
| O que lê | Caminhos, tipos de arquivo e entregas de outros papéis. Nunca "o que foi conversado" |
| O que entrega | Arquivo, relatório ou PR, com formato e destino |
| Pronto quando | Critério verificável deste papel |
| Limites | O que não toca e quando para e pergunta ao dono |

O brief usa só três marcadores, preenchidos na convocação: `{tarefa}`, `{dir}` e `{entrega:<papel>}`. Marcador
desconhecido ou seção faltando impede a carga, e o squad aparece com erro na biblioteca; ele não é convocado pela
metade.

### Gravação e convocação

- **Gravar.** O coordenador grava pelo `argos-cli squad salvar`. Pelo coordenador, o núcleo só aceita a gravação de uma
  proposta que o dono aprovou; a aprovação fica no diário. A pasta é escrita de forma atômica, com o lock do Hades-Core.
- **Editar.** Uma edição é uma proposta nova com a diferença para a revisão atual. Edição à mão nos arquivos também
  vale: o núcleo relê, confere a estrutura e sobe a `revisao`.
- **Aposentar.** Muda `estado` para `aposentado`. Os arquivos ficam, e as convocações antigas continuam apontando para
  a revisão que usaram.
- **Convocar.** Cria um agente por membro com o brief preenchido como prompt inicial, na ordem de `depende_de`. Os
  agentes aparecem juntos no canvas, como um grupo da convocação. As entregas vão para
  `<work root>/.argos/convocacoes/<id>/`, e o diário registra a convocação, o squad, a revisão e o custo.

## O que vem do Hades-Core

O Argos depende do `hades-core` por tag, como os outros cinco apps gpui. Usa, sem reescrever:

| Contrato | Uso no Argos |
|---|---|
| Work root e caminhos (`paths.rs`, `work.rs`) | Achar o projeto e as pastas de estado |
| Registro de agentes (`orchestration/agents/<nome>.json`) | Ler e gravar o agente que o Argos recruta, para o loop e o painel enxergarem o mesmo agente |
| Diário (`journal/<agente>.jsonl`, v1, só aditivo) | Fonte 1 dos sinais de estado; o Argos lê e grava eventos próprios (recrutado, respondido, dispensado) |
| Escrita atômica e lock (`atomic.rs`, `lock.rs`) | Gravar o canvas e o registro sem corromper nem perder escrita |
| Relógio (`clock.rs`, `HADES_NOW`) | Tempo injetado nos testes |

Sem o work root (máquina nova, pasta apagada), o Argos funciona para agentes avulsos: o estado vem só do terminal
e do arquivo de sessão, o loop e o painel não enxergam esses agentes, e uma faixa oferece criar o work root em
`~/.hades`.

O estado do canvas (posições, notas, grupos, ligações) fica num arquivo próprio do Argos, com campo de versão e
revisão. Conflito de gravação aparece para o dono com as duas versões; ele não some.

## Integrações opcionais

| Integração | Papel | Sem ela |
|---|---|---|
| herdr | Backend de terminal alternativo, para quem já tem agentes em panes do herdr | O terminal embutido cobre tudo |
| Loop da Hades | Orquestrador recruta e dispensa pelo `argos-cli`; nós de unidade, PR e gate | O Argos funciona como canvas de agentes avulsos |
| `gh` | Nós e estado de PR e CI | Sem nós de PR |
| Hades-UI | Tema e componentes gpui compartilhados (decisão de marca em [perguntas-abertas.md](perguntas-abertas.md)) | O Argos usa o próprio sistema |

## Acesso pelo celular

O app é desktop. O supervisor de sessões é o ponto natural para o celular, porque já tem o estado e o canal de resposta
de cada agente. As opções estão em [perguntas-abertas.md](perguntas-abertas.md); a escolha é do dono. Qualquer uma
delas expõe uma operação que muda estado (responder permissão de um agente que roda comando), então precisa de
autenticação conferida no supervisor, limite de taxa e registro no diário de quem respondeu o quê.
