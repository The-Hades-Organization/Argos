# Decisões

Decisões da proposta, com as alternativas descartadas. As de design visual ficam no registro de decisões do
[DESIGN.md](../../DESIGN.md); as que ainda dependem do dono, em [perguntas-abertas.md](perguntas-abertas.md).

## Trabalho número um: ver quem espera e responder

**Decisão:** a tela principal otimiza achar o agente que espera o dono e responder ali mesmo (permissão, pergunta,
plano). **Por quê:** com nove ou mais agentes vivos, é o gargalo; o dono escolheu este trabalho entre quatro.
**Descartadas:** visão geral de progresso como foco; terminal de um agente como foco; montagem do time como foco.

## Tela principal com coordenador e caixa de decisões

**Decisão:** a tela principal tem uma coluna fixa com o coordenador, onde o dono pede ao time em texto, e a caixa de
decisões, onde cada pendência chega com a opção recomendada primeiro. O canvas fica à direita e se enquadra na equipe
de que se está falando. **Por quê:** escolha do dono entre três direções desenhadas. **Custa:** um agente coordenador
sempre vivo, com custo próprio, e pendências que nem todo agente entrega com opções. **Descartadas:** canvas na janela
inteira com fila flutuante e resposta em balão; mesa de triagem com um pedido por vez ocupando metade da tela.

## Squads como time salvo e reutilizável

**Decisão:** o dono pede ao coordenador um squad; o coordenador propõe membros, papéis, modelos, o que cada um lê e
entrega; depois do ok, grava um manifesto e um brief autocontido por membro
([arquitetura.md](arquitetura.md#coordenador-e-squads)). **Por quê:** pedido do dono, para reaproveitar times
especializados (um módulo, um tipo de bug, frontend) sem remontar o prompt de cada agente. **Custa:** mais um formato
em disco para versionar, e briefs que envelhecem quando o código muda. **Descartadas:** equipe montada só na conversa
com o coordenador (some com o contexto); predefinição de um agente só, como no Argos atual.

## Supervisor de sessões separado do app

**Decisão:** um processo próprio abre e mantém os PTYs; o app gpui se liga a ele por socket local
([arquitetura.md](arquitetura.md#peças-e-responsabilidades)). **Por quê:** fechar ou atualizar o app não pode derrubar
agente, como um reinício do multiplexador já fez. **Custa:** mais um processo para subir, vigiar e versionar.
**Descartadas:** PTY dentro do app (agente morre com o app); multiplexador externo obrigatório (limites de tecla,
cursor, tamanho e polling).

## Adaptador de agente como arquivo de dados

**Decisão:** cada tipo de agente é um arquivo declarado e versionado (iniciar, mandar prompt, ler estado, responder,
custo e contexto) ([arquitetura.md](arquitetura.md#contrato-de-adaptador)). **Por quê:** agente novo entra sem
recompilar e sem código específico espalhado. **Custa:** o contrato precisa cobrir agentes que só se leem pela tela,
com estado marcado como inferido. **Descartadas:** um módulo Rust por agente; suporte só ao Claude Code.

## Estado por três fontes, da mais confiável à menos

**Decisão:** eventos estruturados no diário, depois arquivo de sessão, depois padrões de tela; o app mostra quando o
estado é inferido. **Por quê:** heurística de tela sozinha erra e não se generaliza a outros agentes. **Descartada:**
estado só pela tela e pelo multiplexador.

## Contratos em disco do Hades-Core

**Decisão:** o Argos depende do `hades-core` por tag e usa registro de agentes, diário, work root, escrita atômica,
lock e relógio sem reescrever ([arquitetura.md](arquitetura.md#o-que-vem-do-hades-core)). **Por quê:** o loop, o painel
e os outros apps enxergam o mesmo agente. **Descartada:** formato próprio de registro de agentes.

## Integrações opcionais

**Decisão:** herdr, loop da Hades e `gh` viram integrações que o Argos usa quando existem. **Por quê:** o dono quer
menos dependência externa; o terminal embutido cobre o caso de uso sem elas.

## Celular fica em aberto

**Decisão:** a proposta lista as opções e não escolhe ([perguntas-abertas.md](perguntas-abertas.md)). **Por quê:**
decisão do dono.
