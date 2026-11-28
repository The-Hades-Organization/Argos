# Conceitos

O Argos novo tem um vocabulário curto: um **agente** roda numa **sessão** guardada pelo **supervisor**, entra pelo
**adaptador** do seu tipo e aparece no **canvas** como um **nó**. Quando ele para e pede algo, o pedido é uma
**pendência**, e a pendência entra na **caixa de decisões**. O dono fala com o time pelo **coordenador**, que monta
**squads**: times salvos em disco e convocados de novo para tarefas futuras. Cada termo abaixo tem um nome só, usado igual na
interface, na documentação e na CLI. Como as peças se ligam está em [arquitetura.md](arquitetura.md).

## Agente e o que o roda

| Termo | O que é | Não confundir com |
|---|---|---|
| **Agente** | Um processo de linha de comando que trabalha sozinho (Claude Code, Codex, Gemini CLI, OpenCode, agy) e que o Argos acompanha | A sessão em que ele roda |
| **Tipo de agente** | A ferramenta por trás do agente, como `claude-code` ou `codex`. Cada tipo tem um adaptador | O modelo que o agente usa (`sonnet`, `gpt-5`) |
| **Adaptador** | Arquivo de dados versionado que diz como iniciar um tipo de agente, mandar prompt, ler estado, responder e ler custo ([contrato](arquitetura.md#contrato-de-adaptador)) | Código específico por agente, que a proposta descarta |
| **Sessão** | O terminal (PTY) em que o agente roda, aberto e mantido pelo supervisor. Sobrevive ao fechar o app | O agente: uma sessão pode ser retomada por um agente novo do mesmo tipo |
| **Supervisor** | O processo separado do app que é dono das sessões (`argos serve`) | O app gpui, que só desenha e manda comandos |

## Estado do agente

Todo agente está em um de seis estados. Cada estado tem cor, forma e palavra, para nunca depender só da cor
(tabela no design system).

| Estado | Quando |
|---|---|
| **Iniciando** | A sessão abriu e o agente ainda não deu o primeiro sinal de pronto |
| **Trabalhando** | O agente está produzindo; o tempo desde o último sinal aparece junto ("Trabalhando · 12s") |
| **Ocioso** | O agente terminou o que tinha e não pediu nada |
| **Esperando você** | O agente parou numa pendência que só o dono resolve |
| **Erro** | O processo saiu com código diferente de zero ou o adaptador não consegue ler o estado |
| **Encerrado** | O agente foi dispensado ou terminou; o nó sai do canvas e fica no histórico |

O estado vem de três fontes, da mais confiável à menos: eventos estruturados, arquivo de sessão e padrões de tela.
Quando só a tela sustenta o estado, ele aparece com o sufixo **(inferido)**
([sinais de estado](arquitetura.md#sinais-de-estado-por-confiança)).

## Pendência e fila

| Termo | O que é |
|---|---|
| **Pendência** | O que um agente espera do dono. Há quatro tipos: **permissão** (rodar um comando, escrever um arquivo), **pergunta** (texto livre ou opções), **plano** (passos para aprovar, recusar ou mudar) e **proposta** (o que o coordenador quer fazer, como recrutar três agentes ou salvar um squad) |
| **Caixa de decisões** | A lista das pendências abertas, da mais antiga à mais nova, sempre visível na coluna do coordenador. Cada uma traz a opção recomendada primeiro quando o agente a dá. É o trabalho número um do Argos ([decisoes.md](decisoes.md#trabalho-número-um-ver-quem-espera-e-responder)) |
| **Opção recomendada** | A resposta que o agente, ou o coordenador, indica como a melhor. Fica destacada e é aceita com Enter; nunca é aplicada sem o dono |
| **Responder** | Resolver uma pendência pelo próprio canvas, sem abrir o terminal. O adaptador diz como cada resposta chega ao agente |

## Canvas

| Termo | O que é |
|---|---|
| **Canvas** | A superfície espacial e infinita onde os agentes ficam. Ocupa a janela; os controles flutuam por cima |
| **Nó** | A peça do canvas. O **nó de agente** mostra cabeçalho com nome, tipo e estado, o terminal ao vivo e o rodapé com modelo, custo e contexto. O **nó de nota** guarda texto do dono |
| **Cabo** | A ligação entre dois nós, como uma nota presa ao agente que ela descreve. Reto ou em ângulo reto, nunca decorativo |
| **Grupo** | Um conjunto de nós que se move e se enquadra junto: os agentes de uma convocação de squad, ou os agentes avulsos de um projeto |
| **Enquadrar** | Mover a câmera do canvas para mostrar um grupo ou um agente inteiro. O coordenador enquadra sozinho o grupo de que se está falando |
| **Zoom semântico** | Ao afastar, o nó troca o terminal por um resumo (nome e estado) em vez de só encolher. Com nove ou mais agentes, é o que mantém o canvas legível |
| **Foco** | Abrir um agente grande, com o terminal ocupando o espaço e a pendência atual no pé dele, e voltar ao canvas no mesmo lugar |
| **Seleção** | O nó escolhido, marcado com colchetes de canto em cor neutra. Seleção nunca usa cor de estado |

## Ações sobre o agente

| Ação | O que faz |
|---|---|
| **Recrutar** | Criar um agente escolhendo o tipo, o diretório e o prompt inicial. O nó aparece no canvas em "Iniciando" |
| **Mandar prompt** | Escrever para um agente que já existe, pelo campo do nó ou pela CLI |
| **Dispensar** | Encerrar o agente e a sessão dele. O nó sai do canvas e o que ele fez fica no histórico |

## Coordenador e squads

| Termo | O que é |
|---|---|
| **Coordenador** | Um agente sempre vivo que recebe os pedidos do dono em texto ("recrute três revisores para a PR #1") e age pelo `argos-cli`. O que ele quer fazer chega antes como proposta na caixa de decisões |
| **Squad** | Um time salvo em disco, especializado em algo (um módulo, um tipo de bug, frontend). Tem membros com papel, tipo de agente, modelo, o que leem e o que entregam. Não depende da conversa que o criou |
| **Membro** | Um papel dentro do squad, como "revisor de testes" ou "autor da correção". Na convocação, vira um agente |
| **Brief do membro** | O texto autocontido que o membro segue: objetivo, o que lê, o que entrega, quando está pronto e o que não toca ([formato](arquitetura.md#brief-do-membro)) |
| **Biblioteca de squads** | A lista dos squads salvos, globais e do projeto, com especialidade, membros, última convocação e custo médio |
| **Convocação** | Uma tarefa entregue a um squad. Cria um agente por membro, agrupa os nós no canvas e guarda as entregas numa pasta própria |

O squad tem um ciclo de vida de sete passos ([uso.md](uso.md#squads)):

| Passo | O que acontece |
|---|---|
| **Criar** | O dono pede ao coordenador um squad para uma especialidade |
| **Propor** | O coordenador apresenta quantos membros, o papel, o modelo, o que cada um lê e entrega |
| **Aprovar** | O dono aceita, pede mudança ou recusa a proposta |
| **Salvar** | Com o ok, o coordenador grava o manifesto e os briefs em disco |
| **Convocar** | O dono entrega uma tarefa ao squad; os membros viram agentes no canvas |
| **Editar** | Uma mudança no squad passa por proposta e aprovação de novo, e sobe a revisão |
| **Aposentar** | O squad sai da lista principal da biblioteca; os arquivos e o histórico ficam |
