# Uso

O dono passa o dia na tela principal: à esquerda, a coluna do coordenador com o campo de pedido ao time e a caixa de
decisões; à direita, o canvas, enquadrado no grupo de que se está falando. Responder uma pendência custa uma tecla
quando a opção recomendada serve. Recrutar e montar um squad custam uma frase e um ok. Os termos estão em
[conceitos.md](conceitos.md); as telas, nos Artifacts listados em [artifacts.md](artifacts.md).

## Atalhos da tela principal

| Tecla | Faz |
|---|---|
| `/` | Foca o campo de pedido ao coordenador |
| `J`, `K` | Passa para a próxima ou para a decisão anterior; o canvas enquadra o agente dela |
| `Enter` | Aceita a opção recomendada da decisão em foco |
| `1` a `9` | Escolhe a opção pelo número |
| `T` | Abre o terminal do agente da decisão em foco |
| `F` | Abre o foco do agente; `Esc` volta ao canvas no mesmo lugar |
| `R` | Abre o recrutamento de um agente avulso |

Nenhum atalho do Argos atual foi pedido pelo dono para continuar (pergunta aberta no [DESIGN.md](../../DESIGN.md)).

## Responder

1. Uma pendência nova entra no fim da caixa de decisões, com o agente, o tipo e há quanto tempo espera. O nó do agente
   ganha a faixa de "esperando você" no canvas.
2. `J` leva até ela. O canvas enquadra o agente, com o terminal legível.
3. Permissão: **Permitir uma vez**, **Sempre neste projeto** ou **Negar**. Pergunta: a opção recomendada, outra opção
   pelo número, ou texto livre. Plano: **Aprovar plano**, **Pedir mudança** (com texto) ou **Recusar**. Proposta do
   coordenador: **Aceitar**, **Mudar** ou **Cancelar**.
4. A decisão sai da caixa, o agente volta a "Trabalhando" e o diário registra quem respondeu o quê.

Quando o agente não entrega opções, a decisão mostra as últimas linhas do terminal e um campo de texto. Quando o estado
veio só da tela, a decisão diz "(inferido)" e oferece abrir o terminal antes de responder.

## Recrutar

**Pelo coordenador.** O dono escreve o pedido ("recrute um revisor de testes para a PR #1"). O coordenador mostra a
proposta: quantos agentes, tipo, modelo, esforço, diretório e custo estimado. Os nós aparecem tracejados no canvas até
o dono aceitar.

**Avulso.** `R` abre o lançador: duas letras filtram o tipo de agente, `Enter` escolhe, o diretório e o prompt inicial
vêm preenchidos com o do último agente do projeto. O nó entra no canvas em "Iniciando".

## Acompanhar

O canvas mostra cada agente com estado, terminal ao vivo, modelo, custo e uso de contexto. Afastando o zoom, o nó troca
o terminal por nome e estado. A barra de estado mostra quantos agentes trabalham, quantos esperam e o custo do dia,
com o custo do coordenador separado. Erro aparece na caixa de decisões como "precisa de atenção", com o motivo e o
atalho para as últimas linhas.

## Dispensar

Pelo menu do nó, pela tecla no foco do agente ou pedindo ao coordenador ("dispense os revisores da PR #1"). Pedido ao
coordenador vira proposta. O agente sai do canvas, a sessão fecha e o que ele fez fica no histórico.

## Squads

Um squad passa por sete passos. Os quatro primeiros acontecem uma vez; convocar se repete a cada tarefa.

1. **Criar.** O dono pede ao coordenador: "monte um squad para bugs de concorrência no `hades-core`".
2. **Propor.** O coordenador lê o projeto e devolve a proposta na caixa de decisões: nome, especialidade, membros
   (papel, tipo de agente, modelo, o que lê, o que entrega, de quem depende), critério de pronto e custo estimado por
   convocação. Cada brief pode ser aberto antes de aprovar.
3. **Aprovar.** **Aceitar**, **Mudar** (com texto: "troque o revisor por um codex") ou **Cancelar**. Uma mudança volta
   como proposta nova.
4. **Salvar.** Com o ok, o coordenador grava o manifesto e um brief por membro, no escopo global ou do projeto
   ([formato](arquitetura.md#coordenador-e-squads)). O squad entra na biblioteca.
5. **Convocar.** Pela biblioteca ou pelo coordenador ("convoque o squad de concorrência para o issue #212"). O dono
   confere a tarefa, o diretório e o custo estimado e confirma. Os membros viram agentes, agrupados no canvas, na ordem
   em que dependem uns dos outros. As entregas ficam na pasta da convocação.
6. **Editar.** Pela biblioteca ou pelo coordenador. A mudança vem como proposta com a diferença para a revisão atual.
   Editar os arquivos à mão também vale; o Argos relê e sobe a revisão.
7. **Aposentar.** Pela biblioteca. O squad some da lista principal e continua consultável com as convocações que fez.

## Pelo celular

Ainda não decidido. As opções e o que cada uma exige estão em [perguntas-abertas.md](perguntas-abertas.md).
