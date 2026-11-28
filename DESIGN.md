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

## Perguntas abertas

- Atalhos do Argos atual que continuam (nenhum pedido pelo dono até agora).
- Custo mostrado em `US$` (assumido).
- Como o dono acompanha e responde pelo celular: opções em `docs/proposta/perguntas-abertas.md`.
