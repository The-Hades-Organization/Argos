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

## Squads desenhados no canvas

**Decisão:** o squad é uma planta no próprio canvas, com nós tracejados num quadro, ligados por cabos com o nome do
que passa de um para outro. A biblioteca é uma paleta flutuante, e convocar é soltar o squad e dar a tarefa num
balão. **Por quê:** escolha do dono entre três estruturas desenhadas. O squad fica onde os agentes vão trabalhar, e
os nós tracejados viram agentes de verdade. **Custa:** disputa de espaço com os agentes vivos e menos lugar para o
histórico. A proposta trata os dois: ao soltar, os agentes vivos se afastam e nenhum nó fica por baixo de outro;
convocado, o squad recolhe numa faixa de células e desdobra com `F`; a paleta abre as últimas convocações do squad
selecionado, com resultado e custo, e leva ao Histórico filtrado. **Descartadas:** linha de montagem (estações
com barra de custo, numa tela própria) e mesa de composição (uma coluna por papel, convocação em diálogo).

## Recrutar em três teclas

**Decisão:** `R` abre o lançador, duas letras filtram o tipo e `Enter` recruta com o diretório, o modelo e o prompt do
último agente daquele tipo no projeto; `Tab` edita antes. O nó nasce ao lado dos agentes do mesmo projeto, afastando
os vizinhos. **Por quê:** escolha do dono; o Argos atual pedia desenhar um retângulo e preencher oito campos.
**Descartadas:** um segundo `Enter` depois de mostrar os campos; o nó nascer onde estava o ponteiro.

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

## Adaptador editado no arquivo, tela só de leitura

**Decisão:** a tela Adaptadores mostra a lista dos tipos com o estado de cada um e o contrato do escolhido em
leitura; `O` abre o arquivo no editor do dono e a tela recarrega ao salvar. As partes que não reiniciam o processo
(ler estado, responder, comandos, custo e contexto) valem na hora para os agentes vivos; as outras, para os próximos
recrutas. Versão nova que não carrega deixa os vivos na última válida, com o erro à vista. **Por quê:** o arquivo é a
fonte, e um formulário repetiria o formato; consertar um padrão de tela não pode esperar o agente encerrar.
**Descartadas:** formulário de edição na tela; mudança valendo só para recrutas novos.

## Sem o work root, o Argos funciona para agentes avulsos

**Decisão:** sem a pasta de estado do Hades-Core, o canvas abre, recruta e mostra o estado lido do terminal,
marcado como inferido; uma faixa avisa que o loop e o painel não enxergam esses agentes e oferece **Criar em
~/.hades** ([arquitetura.md](arquitetura.md#o-que-vem-do-hades-core)). **Por quê:** o `hades-core` vai dentro do
binário; o que pode faltar é a pasta, e exigir configuração antes do canvas trava quem só quer um agente.
**Descartada:** bloquear o app até o work root existir.

## Erro do sistema numa faixa, sem esconder o último estado

**Decisão:** todo erro do sistema entra numa faixa no topo do canvas, com a causa e a ação. Supervisor que não
responde: os nós ficam com o último estado lido, marcados com a hora e sem digitação, e o Argos tenta reconectar a
cada 5 s. Supervisor que morreu: ele volta sozinho, os agentes ficam encerrados no canvas com o motivo e a opção de
recrutar de novo com a mesma sessão, quando o adaptador sabe retomar. Canvas salvo ilegível: os agentes vivos
aparecem lado a lado, o arquivo não é regravado e a faixa oferece a última cópia boa. **Por quê:** os agentes são
do supervisor, não da janela; dar como encerrado um agente que só está sem contato, ou apagar a arrumação do dono
numa gravação automática, faria a tela mentir. **Descartadas:** esvaziar o canvas quando o supervisor some; diálogo
modal para cada erro.

## Primeira vez sem tour

**Decisão:** o canvas vazio da primeira vez tem uma frase, **Recrutar** (`R`) e um exemplo de pedido ao
coordenador, com o campo do coordenador já focado. **Por quê:** os adaptadores de fábrica já vêm prontos e recrutar é
uma tecla. **Descartadas:** tour guiado; tela de boas-vindas.

## Celular fica em aberto

**Decisão:** a proposta lista as opções e não escolhe ([perguntas-abertas.md](perguntas-abertas.md)). **Por quê:**
decisão do dono.
