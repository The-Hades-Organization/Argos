# Conceitos

O Argos novo tem um vocabulário curto: um **agente** roda numa **sessão** guardada pelo **supervisor**, entra pelo
**adaptador** do seu tipo e aparece no **canvas** como um **nó**. Quando ele para e pede algo, o pedido é uma
**pendência**, e a pendência entra na **fila de esperando você**. Cada termo abaixo tem um nome só, usado igual na
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
| **Pendência** | O que um agente espera do dono. Há três tipos: **permissão** (rodar um comando, escrever um arquivo), **pergunta** (texto livre ou opções) e **plano** (passos para aprovar, recusar ou mudar) |
| **Fila de esperando você** | A lista das pendências abertas, da mais antiga à mais nova, sempre visível na tela principal. É o trabalho número um do Argos ([decisoes.md](decisoes.md#trabalho-número-um-ver-quem-espera-e-responder)) |
| **Responder** | Resolver uma pendência pelo próprio canvas, sem abrir o terminal. O adaptador diz como cada resposta chega ao agente |

## Canvas

| Termo | O que é |
|---|---|
| **Canvas** | A superfície espacial e infinita onde os agentes ficam. Ocupa a janela; os controles flutuam por cima |
| **Nó** | A peça do canvas. O **nó de agente** mostra cabeçalho com nome, tipo e estado, o terminal ao vivo e o rodapé com modelo, custo e contexto. O **nó de nota** guarda texto do dono |
| **Cabo** | A ligação entre dois nós, como uma nota presa ao agente que ela descreve. Reto ou em ângulo reto, nunca decorativo |
| **Grupo** | Um conjunto de nós que se move e se enquadra junto, em geral um por projeto. O nome e a forma finais dependem da direção escolhida para a tela principal |
| **Zoom semântico** | Ao afastar, o nó troca o terminal por um resumo (nome e estado) em vez de só encolher. Com nove ou mais agentes, é o que mantém o canvas legível |
| **Foco** | Abrir um agente grande, com o terminal inteiro e o histórico de pendências, e voltar ao canvas no mesmo lugar |
| **Seleção** | O nó escolhido, marcado com colchetes de canto em cor neutra. Seleção nunca usa cor de estado |

## Ações sobre o agente

| Ação | O que faz |
|---|---|
| **Recrutar** | Criar um agente escolhendo o tipo, o diretório e o prompt inicial. O nó aparece no canvas em "Iniciando" |
| **Mandar prompt** | Escrever para um agente que já existe, pelo campo do nó ou pela CLI |
| **Dispensar** | Encerrar o agente e a sessão dele. O nó sai do canvas e o que ele fez fica no histórico |
