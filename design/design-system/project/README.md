# Argos

Design system do Argos, o canvas de agentes da Hades: um app desktop gpui onde um dev acompanha nove ou mais agentes
de linha de comando e responde o que cada um pede. Família Hades (fontes, forma quadrada, ícones e neutros quentes do
Hades-UI v0.3.1), com tokens próprios para estado do agente, nó, cabo e terminal. O brief que manda nestas escolhas é o
`DESIGN.md` do repositório Argos.

> **Estado:** fundações, regras de interação, nove componentes base e os ícones aprovados pelo dono em 28/11. A
> tela principal segue a direção Coordenador.

## Princípios

- **Quem espera você aparece primeiro.** `agent-waiting` é a única cor de atenção do canvas. Nada mais usa esse rosa:
  nem seleção, nem foco, nem decoração.
- **Nítido.** Fio fino (`border`), contraste alto, texto no mínimo 4,5:1 nos dois temas, nada borrado. O gpui não faz
  blur, e o Argos não finge que faz.
- **Quente.** Neutros puxados para o vinho, herdados do Hades-UI. Cinza puro não entra.
- **Ferramenta de operação.** Estado primeiro, texto curto, nada que explique o que a tela já mostra. O canvas ocupa a
  janela; controles flutuam por cima dele.
- **Quadrado.** `radius-none` em tudo; `radius-full` só no ponto de estado e no indicador de giro. Separação por fio e
  por tom de superfície; sombra só em camada flutuante.

## Voz e escrita

Pt-BR, direto, para um dev que conhece o assunto.

- Botão diz o que acontece: **Responder**, **Recrutar**, **Dispensar**. Depois, o resultado: "Respondido", "Codex
  recrutado".
- Estado é palavra curta + número: "Trabalhando · 12s", "Esperando você · permissão", "Erro · saiu com código 1".
- Erro diz o que houve e o que fazer: "O agente saiu com código 1. Ver as últimas linhas" (nunca `graph_failed` cru).
- Formatos: data `28/11`, hora `14h05`, decimal com vírgula (`1,5 mil tokens`), custo `US$ 0,42`.
- Um nome por conceito: **agente** (nunca worker ou sessão para a mesma coisa), **recrutar**, **dispensar**,
  **esperando você**.

## Cor

Os componentes pedem papéis, nunca valores. Os valores estão em `tokens.json`, com tema escuro (padrão) e claro.

| Grupo | Tokens | Regra |
|---|---|---|
| Superfícies | `canvas`, `surface`, `fill-1`, `rail` | `canvas` é o chão; nó e painel em `surface`; campo e área recuada em `fill-1`. `rail` é escuro nos dois temas |
| Texto | `text`, `text-muted`, `text-placeholder`, `text-disabled`, `on-rail` | `text-placeholder` é mais claro que `text-muted`, para nunca parecer texto digitado |
| Linhas | `border`, `border-hover`, `divider` | Um peso de fio; `divider` mais leve, para lista não virar caixa |
| Camadas | `tint-hover`, `tint-selected`, `tint-pressed` | Translúcidas: servem em qualquer chão |
| Ação | `primary`, `primary-hover`, `primary-pressed`, `on-primary` | Uma ação principal por tela. Neutra (claro no escuro, escuro no claro): o rosa é só de quem espera |
| Foco e seleção | `focus`, `select-mark` | Foco é azul e só aparece por teclado; seleção é neutra, em colchetes de canto |
| Sistema | `success`, `warn`, `danger`, `info` e os `-bg` | Estado de operação (custo alto, falha de gravação); nunca decoração |
| Terminal | `term-bg`, `term-fg`, `term-muted`, `term-cursor`, `term-selection` | Escuro nos dois temas, como no Hades |
| Canvas | `node-header`, `cable`, `cable-active`, `canvas-grid` | Cabo do nó selecionado em `cable-active`; os outros recuam |

### Estado do agente

Estado nunca é só cor: cada um tem forma e palavra. A palavra aparece no cabeçalho do nó, na fila e no leitor de tela.

| Estado | Token | Forma | Texto |
|---|---|---|---|
| Iniciando | `agent-starting` | Anel tracejado | Iniciando |
| Trabalhando | `agent-working` | Ponto cheio | Trabalhando · 12s |
| Ocioso | `agent-idle` | Ponto vazado | Ocioso · 4 min |
| Esperando você | `agent-waiting` + `agent-waiting-bg` (texto por cima em `on-agent-waiting`) | Faixa no topo do nó, ponto cheio, pulso | Esperando você · permissão |
| Erro | `agent-error` | Triângulo; borda do nó em `agent-error` | Erro · saiu com código 1 |
| Encerrado | `agent-ended` | Ponto com x; nó em `text-disabled` | Encerrado |

Estado vindo só de padrão de tela (sem evento do agente) leva o sufixo "(inferido)" no texto.

## Tipografia

Figtree para a interface, Marcellus para títulos de painel e de página, Geist Mono para terminal, custo e qualquer
número que se alinha em coluna (`font-variant-numeric: tabular-nums`). Densidade alta: `body` 13/18.

| Estilo | Uso |
|---|---|
| `caption` 11/14 | Chip, metadado do nó |
| `small` 12/16, `label` 12/16 600 | Texto auxiliar; rótulo de campo e de coluna |
| `body` 13/18, `body-strong` | Texto corrido da interface |
| `node-title` 14/20 600 | Nome do agente no cabeçalho do nó |
| `panel-title` 15/20 600 | Título de painel e diálogo |
| `section` 18/24, `page-title` 24/30, `display` 40/44 (Marcellus) | Título de seção, de tela, de estado vazio |
| `mono-small`, `mono`, `term` 13/17 | Identificadores, custo, terminal |

O gpui não tem letter-spacing nativo; rótulo em caixa alta usa o espaçamento do Hades-UI (`Tracked`).

## Espaço, forma, sombra e medidas

- **Espaço:** base 4 px. `space-1` 4, `space-2` 8, `space-3` 12, `space-4` 16, `space-6` 24.
- **Forma:** `radius-none` em tudo; `radius-full` só em ponto de estado e giro.
- **Sombra:** duas. `elev-float` para menu, popover e balão de resposta; `elev-dialog` para diálogo, lançador de
  recrutar e toast. Nó no canvas não tem sombra.
- **Medidas:** controle `control-sm` 28 e `control-md` 32; trilho `rail-width` 64 (248 aberto); fila
  `queue-width` 320 (assumido); barra de estado 26; grade `grid-step` 20; nó de agente 480 × 320.

## Movimento

Só com sentido, e tudo desligável (movimento reduzido desliga os três).

| Movimento | Duração | Uso |
|---|---|---|
| Pulso | 1 600 ms, em laço | Ponto e faixa de quem espera você. Nenhum outro elemento pulsa |
| Câmera | 250 ms ao abrir foco, 200 ms ao voltar | Pular para um agente, enquadrar |
| Camada | 150 ms | Abrir menu, popover, balão; fechar é mais rápido que abrir |

## Regras de interação

Escritas uma vez; os componentes seguem estas regras em vez de inventar as suas.

| Estado | Peça com borda (nó, campo, botão secundário) | Peça sem borda (item de lista, aba, ícone) | Ação principal |
|---|---|---|---|
| Hover | Só o fio escurece: `border` → `border-hover` | `tint-hover` por cima | `primary-hover` |
| Pressionado | `fill-1` no fundo | `tint-pressed` | `primary-pressed` |
| Foco (só teclado) | Anel de 2 px em `focus`, 2 px para fora | Anel de 2 px em `focus` | Anel de 2 px em `focus` |
| Desativado | Fio em `divider`, texto em `text-disabled` | Texto em `text-disabled`, sem hover | Fundo `fill-1`, texto `text-disabled` |
| Carregando | Mesmo tamanho; giro de 12 px no lugar do ícone | Mesmo tamanho; giro no lugar do ícone | Mesmo tamanho; giro em `on-primary` no lugar do rótulo |
| Selecionado | Nó: colchetes de canto em `select-mark` e cabos em `cable-active`; campo: não se aplica | `tint-selected`; o peso da fonte não muda | Não se aplica |

- Hover é mais fraco que selecionado, para nunca parecer que dois itens foram escolhidos.
- Itens empilhados (fila, menu) têm 2 px de vão entre si; os realces não se fundem.
- Seleção nunca usa cor de estado. A seleção do Argos atual era vermelha e se confundia com "parado".

## Iconografia

Um conjunto só: os ícones do Hades-UI v0.3.1. Os de linha são do Lucide v0.460.0 (licença ISC) e os desenhos próprios
da Hades, como `argos`, estão sob MIT. As duas licenças são permissivas e compatíveis com a GPL-3.0 do Argos; basta
manter o aviso, que está em `assets/Icones/LICENSE.txt`. O gpui já carrega o conjunto pelo `IconName` do Hades-UI, sem
dependência nova, e o Argos fica igual às outras cinco ferramentas.

Traço de 2 em 24 (cerca de 1,3 px a 16 px), ponta quadrada e junta em ângulo. 16 px na interface, 14 px em chip. A
tinta é `currentColor`: o ícone herda a cor do texto. Ícone sozinho leva nome acessível; ícone ao lado de rótulo some
do leitor de tela. Os 25 que o Argos usa estão no grupo Ícones, com o uso de cada um.

## Componentes

Cada componente tem anatomia, regra com o porquê e matriz de estados na própria página. O CSS deles está em
`components/bundle.css` e usa só os papéis de token acima. No app, os mesmos papéis viram o tema gpui.

| Componente | Grupo | Para quê |
|---|---|---|
| Botão | Ações | Primária, secundária, fantasma e ícone, com os seis estados |
| Campo | Entrada | Resposta de uma linha e pedido ao time de várias |
| Chip | Conteúdo | Identificador dentro do texto, tipo de agente, contador de quem espera |
| Estado do agente | Agente | Forma, palavra e tempo dos seis estados, mais "(inferido)" |
| Nó de agente | Agente | A peça do canvas, nos seis estados, selecionado, hover, foco e zoom distante |
| Painel de detalhes | Agente | O que se sabe do agente no foco: tipo, modelo, diretório, custo, contexto, squad; campo ausente some |
| Decisão | Decisões | Cartão de permissão, pergunta, plano e proposta, com a opção recomendada |
| Coluna do coordenador | Decisões | Pedido ao time, caixa de decisões e atalhos; vazia e com erro |
| Trilho | Navegação | Canvas, Squads, Histórico, Adaptadores e Configuração |
| Barra de estado | Navegação | Supervisor, contagem, custo do dia; sem supervisor e custo alto |
| Planta do squad | Squad | Quadro, nó tracejado e cabo com rótulo: proposta, mudou, a recrutar, hover, seleção e foco |
| Paleta de squads | Squad | Biblioteca flutuante com o histórico do selecionado; arrastar, vazia, sem resultado, manifesto inválido |
| Balão de tarefa | Squad | Pede a tarefa ao soltar o squad: vazio, preenchido, convocando e erro |
| Faixa do squad | Squad | Squad convocado recolhido em células: em andamento, esperando você, erro e pronto |

As peças de squad seguem a direção planta no canvas, escolhida pelo dono em 28/11; componentes aprovados no mesmo dia.
