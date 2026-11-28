# DESIGN.md · Argos

> Se este arquivo e o código discordarem, o código vale até o dono decidir. O conflito vai para Perguntas abertas.

## Produto

App desktop gpui onde um dev acompanha nove ou mais agentes de linha de comando (Claude Code, Codex, Gemini CLI,
OpenCode, agy e os que vierem) num canvas. Trabalho número um da tela principal: **ver quem precisa do dono e
responder**. A tela principal tem uma coluna fixa com o **coordenador** (pedido ao time em texto) e a **caixa de
decisões** (cada pendência com a opção recomendada primeiro), e o canvas à direita, enquadrado no grupo de que se está
falando. Permissão, pergunta, plano e proposta são respondidos sem abrir o terminal. Com nove ou mais agentes vivos, o
canvas agrupa e usa zoom semântico. **Squads** são de primeira classe: times salvos em disco, propostos pelo
coordenador, aprovados pelo dono e convocados de novo para tarefas futuras. Recrutar, acompanhar e dispensar vêm com
menos passos que no Argos atual. Detalhe em `docs/proposta/produto.md`, `conceitos.md` e `uso.md`.

## Público e voz

Um dev só, o dono, técnico, na mesa; acompanha muito pelo celular quando sai dela. Pt-BR, direto, texto curto,
"ferramenta de operação, não vitrine": estado primeiro, sem explicar o que a tela já mostra. Formatos: data `28/11`,
hora `14h05` em 24 h, decimal com vírgula, custo em `US$` (assumido: os agentes cobram em dólar).

## Clima

Palavras: **nítido, quente**. Nunca como: painel SaaS genérico (cartão arredondado, gradiente, ícone colorido em toda
parte), IDE lotada (painel encaixado por todos os lados, barra sobre barra), terminal "hacker" (verde neon sobre preto,
efeito de tela antiga), o Argos atual (faixas de título, abas e filtros antes do canvas; seleção vermelha igual a
"parado"; nó que some no escuro).

## Marca

Família Hades, canvas próprio. Design system de referência em código: `The-Hades-Organization/Hades-UI` v0.3.1 (gpui),
usado pelas outras cinco ferramentas.

- **Herdado do Hades-UI:** fontes Figtree (texto), Marcellus (título) e Geist Mono (terminal e números), OFL; forma
  quadrada (raio 0), separação por fio, sombra só em camada flutuante; ícones do Hades-UI (Lucide ISC + próprios MIT,
  já com `argos`); neutros quentes puxados para o vinho (escuro `#0e050a`, claro `#f8ecf1`); componentes do Hades-UI nas
  telas de configuração; embutível no Hades-Panel.
- **Próprio do Argos:** tokens de estado do agente, de nó, de cabo e de terminal. Eles separam seleção de erro e mantêm
  o nó legível nos dois temas. Valores definidos nas fundações (`craft-system`).

## Referências

Agrupadas por papel, como pediu o dono. As três últimas da lista foram trazidas por ele e lidas por texto e captura da
página pública em 2026-11-28.

**Canvas de agentes**

- **Argos atual** (capturas do painel) · levar: terminal ao vivo dentro do nó, chips de estado compactos, nota ligada
  ao agente por cabo · evitar: faixas acima do canvas, recrutar desenhando retângulo + modal de 8 campos, seleção
  vermelha igual a "parado".
- **tldraw** (quadro infinito) · levar: pan e zoom suaves, seleção e encaixe previsíveis, barra de ferramentas mínima
  que não come o canvas · evitar: traço de mão e paleta pastel.
- **AgentGrid** (agentgrid.sh) · levar: painel do agente com o campo de prompt embutido e modelo e esforço na base;
  estado como texto curto com tempo ("Trabalhando · 12s"); coordenador em linguagem natural numa coluna lateral que
  cria equipe e enquadra painéis; caixa de decisões com a opção recomendada; trilho de 4 ícones; controle de zoom
  pequeno no canto · evitar: canto arredondado e sombra suave; painel branco com área vazia enorme (baixa densidade);
  cabos ondulados decorativos que não dizem nada.

**Terminal**

- **Zed** (editor em gpui) · levar: nitidez de texto e fio fino, terminal embutido rápido, paleta de comandos ·
  evitar: painéis encaixados por todos os lados.

**Recrutar e responder**

- **Raycast** (lançador) · levar: uma tecla abre, duas letras filtram, Enter faz; modelo para recrutar e responder em
  poucos passos · evitar: fundo translúcido e borrado (o gpui não faz blur).
- **T3 Code** (t3.codes) · levar: vários tipos de agente na mesma superfície com a assinatura do próprio dono; trocar
  de modelo no meio do trabalho; "commit e PR" como ação do agente; app remoto no celular ligado ao desktop
  (referência para a pergunta do celular) · evitar: o fio de conversa como modelo principal (perde a visão espacial de
  nove agentes); preto puro com texto cinza de baixo contraste, em que botão e subtítulo quase somem.
- **Giga Agent Canvas** (giga.ai/agent-canvas) · editor de política de robô de atendimento, não supervisiona agentes de
  código · levar: identificadores (variável, ferramenta) como pílula monoespaçada com contorno dentro do texto; passos
  com desvio explícito ("se falhar, segue para…"), útil para mostrar um plano a aprovar; estado "rascunho · atualizado
  há 1 min" na barra · evitar: gradiente roxo e botão laranja de marketing; fonte de exibição pixelada.

## Restrições

- **Plataforma:** desktop gpui. Limites do gpui: sem letter-spacing nativo, sem blur, gradiente de 2 paradas, menu
  sem setas.
- **Temas:** claro e escuro completos; escuro como padrão; segue o sistema se o dono não escolher.
- **Telas:** monitor de mesa a partir de 1440 px de largura; janela redimensionável até 1024 px sem quebrar; mais de um
  monitor não é requisito.
- **Densidade:** alta. Texto base 13 px, controle 28 a 32 px, como no Hades-UI.
- **Movimento:** só com sentido: pulso em quem espera o dono, transição curta de câmera ao pular para um agente; nada
  decorativo; tudo desligável.
- **Teclado:** tudo por teclado, mouse opcional; uma tecla leva ao próximo que espera e outra responde; atalhos sem
  conflito com o sistema.
- **Acessibilidade:** WCAG AA, nome acessível em todo controle, estado nunca só por cor (sempre cor + forma ou texto).
- **Ícones:** os do Hades-UI (Lucide ISC + próprios MIT); a escolha da lib e o porquê ficam no design system.

## Registro de decisões

- 2026-11-28: trabalho número um da tela principal é ver quem espera e responder. Por quê: é o gargalo com nove ou mais
  agentes vivos.
- 2026-11-28: clima nítido e quente; calmo e preciso recusados. Por quê: escolha do dono.
- 2026-11-28: marca na família Hades com tokens próprios para o canvas. Por quê: manter o Argos reconhecível ao lado das
  outras ferramentas e corrigir os problemas de estado do canvas atual.
- 2026-11-28: sete referências agrupadas em três papéis. Por quê: o craft pede até cinco; o dono pediu agrupar sem
  descartar.
- 2026-11-28: escuro como tema padrão, densidade alta, movimento só com sentido, teclado primeiro. Por quê: padrões
  propostos e aceitos pelo dono.
- 2026-11-28: fundações do design system aprovadas, com três escolhas próprias do Argos: rosa só para "esperando
  você", anel de foco azul e seleção neutra em colchetes de canto. Por quê: a atenção do canvas tem uma cor só, e
  seleção não se confunde com estado.
- 2026-11-28: tela principal na direção Coordenador: coluna fixa com o pedido ao time e a caixa de decisões, canvas à
  direita enquadrado sozinho. Salas (canvas na janela, fila flutuante) e Triagem (mesa de um pedido por vez)
  descartadas. Por quê: escolha do dono entre três direções desenhadas.
- 2026-11-28: squads de agentes como conceito de primeira classe, com telas próprias (proposta para aprovação,
  biblioteca, convocação). Por quê: pedido do dono, para reaproveitar times especializados sem depender da conversa.
- 2026-11-28: componentes base e ícones aprovados; a ação principal (`primary`) passa a neutro claro no tema escuro
  (fundo claro, texto escuro) e neutro escuro no claro. Texto sobre o rosa ganha token próprio, `on-agent-waiting`.
  Por quê: o botão principal fica dentro dos cartões de decisão, e dois rosas lado a lado se confundiam.
- 2026-11-28: telas de squad como planta no canvas: nós tracejados, paleta flutuante com o histórico e squad
  convocado recolhido numa faixa. Linha de montagem e mesa de composição descartadas. Por quê: escolha do
  dono, que pediu tratar a disputa de espaço com os agentes vivos e o histórico escondido.
- 2026-11-28: dispensar um agente não pede confirmação: dá 5 s para desfazer antes de encerrar o processo. Por
  quê: escolha do dono, um passo a menos no fluxo mais repetido.
- 2026-11-28: nó encerrado sai sozinho do canvas para o Histórico depois de 10 min. Por quê: escolha do dono, o
  canvas fica só com quem está vivo.
- 2026-11-28: canvas principal aprovado como desenhado: padrão, ninguém esperando, muitos, pedido ao time e as
  folhas de dados, sistema, atividade e interação. Por quê: ok do dono sem mudanças.
- 2026-11-28: no lançador de Recrutar, `Enter` recruta direto com os campos preenchidos; `Tab` edita antes. Por
  quê: escolha do dono, recrutar fica em três teclas (`R`, duas letras, `Enter`).
- 2026-11-28: o nó recrutado nasce ao lado dos agentes do mesmo projeto, afastando os vizinhos. Por quê: escolha do
  dono, o canvas continua agrupado por projeto.
- 2026-11-28: no campo do prompt do lançador, `Enter` quebra linha e `Ctrl+Enter` recruta; nos outros campos,
  `Enter` recruta. Por quê: um prompt longo não sai recrutado pela metade; confirmado pelo dono.
- 2026-11-28: agente que falha ao iniciar entra na caixa de decisões no mesmo rosa de "esperando você", sem
  variante nova da peça de decisão. Por quê: escolha do dono; o rosa continua sendo o único sinal de "precisa de
  você".
- 2026-11-28: tela Recrutar aprovada como desenhada, com a folha 2.6 no rosa padrão. Por quê: ok do dono.
- 2026-11-28: o teclado do terminal de um nó volta ao canvas com `Ctrl+]` ou um clique fora do nó; `Esc` fica
  com o agente. Por quê: escolha do dono; vários agentes usam `Esc` para interromper.
- 2026-11-28: contexto quase cheio aparece só no rodapé do nó: barra de 2 px e, de 90% em diante, número em
  vermelho com "quase cheio". Não entra na caixa de decisões. Por quê: escolha do dono.
- 2026-11-28: agente em Iniciando vira erro quando passa do prazo declarado pelo adaptador; antes disso, o nó
  mostra o tempo. Por quê: escolha do dono, nenhum nó fica parado em Iniciando sem fim.
- 2026-11-28: em todo campo de prompt (lançador de Recrutar, campo do nó, pedido ao time), `Enter` quebra linha e
  `Ctrl+Enter` envia; `Esc` fecha o campo do nó sem enviar. Por quê: escolha do dono, um prompt longo não sai pela
  metade e a tecla é a mesma em toda parte.
- 2026-11-28: tela do nó de agente aprovada; a barra de contexto, o aviso de linhas novas, o campo de prompt no
  rodapé e o rodapé "Teclado no terminal" entram no componente Nó de agente do design system. Por quê: ok do dono.
- 2026-11-28: o foco de um agente abre no lugar do canvas, com a coluna do coordenador ao lado. Por quê: escolha
  do dono, a caixa de decisões continua mostrando quem mais espera enquanto ele lê um agente.
- 2026-11-28: sai-se do foco com `Esc` quando o teclado está fora do terminal; com o teclado no terminal, `Ctrl+]`
  e depois `Esc`. Por quê: escolha do dono, `Esc` continua sendo do agente dentro do terminal.
- 2026-11-28: trocar o modelo de um agente no meio do trabalho fica fora da tela de foco, como pergunta aberta
  sobre uma parte opcional futura do contrato de adaptador. Por quê: escolha do dono; o contrato ainda não declara
  a troca.
- 2026-11-28: no foco de um agente, o terminal ocupa o espaço. Sob o cabeçalho, uma linha de 30 px com a
  sessão (modelo e esforço, custo, contexto, branch, diretório copiável, squad com o brief); a pendência atual
  encaixa no pé do terminal, abaixo da última linha do agente; sem coluna fixa nem histórico de pendências.
  Detalhes viram um balão de cinco linhas (`I`) só na janela estreita. Por quê: escolha do dono entre duas
  direções; o que se consulta ao acompanhar fica à vista e nada cobre a saída do agente.
- 2026-11-28: tela de foco aprovada na direção A, com a forma curta da linha da sessão quando a área do foco fica
  abaixo de 900 px e a pendência no pé ocupando até metade da área (acima disso, rola por dentro). A linha da
  sessão e a pendência podem ser recolhidas e expandidas pelo dono, com tecla, e o Argos lembra o estado. Por quê:
  escolha do dono; as duas regras só valem se o dono puder devolver o espaço ao terminal.
- 2026-11-28: o prompt do foco e do nó aceita os slash commands nativos de cada tipo de agente (`/compact`,
  `/model` no Claude Code e os equivalentes no Codex, Gemini e outros). O contrato de adaptador declara a lista de
  comandos com descrição, e digitar `/` no prompt lista e completa. Por quê: pedido do dono; o prompt do Argos não
  pode ser mais pobre que o do próprio agente.
- 2026-11-28: recolher no foco pelo botão "Sessão" do cabeçalho (`L`), que mostra o contexto de 90% em diante, e
  pela cabeça da pendência (`M`), que recolhida vira a cabeça da Decisão com o resumo; estado global e lembrado. A
  lista de comandos é peça do design system, compartilhada pelo foco e pelo nó, e filtra só pelo nome. Por quê: um
  fio de poucos pixels é alvo difícil, e o alerta de contexto não pode sumir com a linha.
- 2026-11-28: a tela Adaptadores é só de leitura: edita-se o arquivo, com "Abrir o arquivo" e recarga ao salvar.
  Abre no lugar do canvas, com a coluna do coordenador ao lado. O teste roda só pelo botão, com o custo mostrado ao
  fim. Por quê: o arquivo é a fonte e um formulário repetiria o TOML; quem espera o dono continua à vista.
- 2026-11-28: mudança no arquivo de um adaptador vale na hora para os agentes vivos nas partes que não reiniciam o
  processo (ler estado, responder, comandos, custo e contexto); identidade, iniciar e mandar prompt valem para os
  recrutados depois. A tela mostra o que foi aplicado aos vivos. Versão nova que não carrega: os vivos seguem com a
  última versão válida e o erro fica à vista. Por quê: escolha do dono; consertar um padrão de tela não pode esperar
  o agente encerrar.
- 2026-11-28: desenho da tela Adaptadores, aprovado. Cada parte do contrato diz quando uma mudança
  vale ("vale na hora para os vivos" ou "vale para os próximos recrutas"); a recarga marca com ponto e etiqueta as
  partes aplicadas. A tela não tem ação primária, exceto no adaptador que não carrega, em que "Abrir o arquivo na
  linha N" vira primária. Quatro peças novas no design system: Lista de adaptadores, Seção do contrato, Passos do
  teste e Faixa. Oito ícones novos do Hades-UI. Por quê: tela de leitura não tem uma ação que se destaque; no erro,
  só uma ação resolve; a faixa vai servir também às telas de vazio e erro.
- 2026-11-28: sem o work root do Hades, o Argos funciona para agentes avulsos, com faixa de aviso e o botão "Criar
  em ~/.hades". Por quê: o `hades-core` vai dentro do binário; o que pode faltar é a pasta de estado, e exigir
  configuração antes do canvas trava quem só quer um agente.
- 2026-11-28: supervisor parado tem dois casos desenhados: não responde (agentes vivos nele, último estado à
  vista, reconexão) e morreu (agentes encerrados com o motivo e "Recrutar de novo com a mesma sessão" quando o
  adaptador declara retomada). Por quê: o supervisor existe para os agentes sobreviverem ao app; se ele morre,
  eles morrem, e a tela não pode fingir o contrário.
- 2026-11-28: canvas da primeira vez é um vazio enxuto: uma frase, Recrutar e um exemplo de pedido ao
  coordenador, sem tour nem boas-vindas. Por quê: os adaptadores de fábrica já vêm prontos e recrutar é uma tecla.

## Perguntas abertas

- Atalhos do Argos atual que continuam (nenhum pedido pelo dono até agora).
- Custo mostrado em `US$` (assumido).
- Como o dono acompanha e responde pelo celular: opções em `docs/proposta/perguntas-abertas.md`.
- Trocar o modelo de um agente no meio do trabalho: opções em `docs/proposta/perguntas-abertas.md`.
