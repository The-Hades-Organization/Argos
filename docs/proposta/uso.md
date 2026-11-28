# Uso

O dono passa o dia na tela principal: à esquerda, a coluna do coordenador com o campo de pedido ao time e a caixa de
decisões; à direita, o canvas, enquadrado no grupo de que se está falando. Responder uma pendência custa uma tecla
quando a opção recomendada serve. Recrutar e montar um squad custam uma frase e um ok. Os termos estão em
[conceitos.md](conceitos.md); as telas, nas páginas de `design/` listadas em [paginas.md](paginas.md).

## Atalhos da tela principal

| Tecla | Faz |
|---|---|
| `/` | Foca o campo de pedido ao coordenador |
| `J`, `K` | Passa para a próxima ou para a decisão anterior; o canvas enquadra o agente dela |
| `Enter` | Aceita a opção recomendada da decisão em foco |
| `1` a `9` | Escolhe a opção pelo número |
| `T` | Abre o terminal do agente da decisão em foco |
| `F` | Abre o foco do agente no lugar do canvas, com a coluna do coordenador ao lado; `Esc` volta ao canvas no mesmo lugar (com o teclado no terminal, `Ctrl+]` e depois `Esc`) |
| `R` | Abre o recrutamento de um agente avulso |
| `P` | Com um nó selecionado, abre o campo para mandar prompt a ele; `Ctrl+Enter` envia, `Enter` quebra linha, `Esc` fecha |
| `Ctrl+]` | Devolve ao canvas o teclado que estava no terminal de um nó (clicar fora do nó também devolve) |

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

**Avulso.** `R` abre o lançador: duas letras filtram o tipo de agente e o diretório, o modelo e o prompt inicial vêm
preenchidos com os do último agente daquele tipo no projeto. `Enter` recruta; `Tab` leva aos campos para editar antes. No campo do prompt, `Enter` quebra linha e
`Ctrl+Enter` recruta.
O nó nasce em "Iniciando" ao lado dos agentes do mesmo projeto, afastando os vizinhos, e o canvas o enquadra.

## Acompanhar

O canvas mostra cada agente com estado, terminal ao vivo, modelo, custo e uso de contexto. Afastando o zoom, o nó troca
o terminal por nome e estado. A barra de estado mostra quantos agentes trabalham, quantos esperam e o custo do dia,
com o custo do coordenador separado. O rodapé do nó tem uma barra de 2 px com o uso de contexto; de 90% em
diante o número fica vermelho com "quase cheio". Um agente que não dá sinal de pronto dentro do prazo que o
adaptador declara passa a erro. Erro aparece na caixa de decisões como "precisa de atenção", com o motivo e o
atalho para as últimas linhas.

## Inspecionar um agente

`F` (agente selecionado ou da decisão em foco) ou clique duplo no cabeçalho do nó abre o foco no lugar do canvas. A
coluna do coordenador fica ao lado, e a caixa de decisões continua mostrando quem mais espera. No foco o terminal
ocupa o espaço, com a rolagem inteira. Acima dele, uma linha com a sessão: modelo e esforço, custo, contexto, branch,
diretório e squad (que abre o brief).

1. Quando o agente espera você, a pendência encaixa no pé do terminal, abaixo da última linha dele, e se responde
   ali, como na caixa de decisões; responder em um lugar resolve os dois. Respondida, ela sai e o terminal recupera
   a altura.
2. `I` abre o balão de Detalhes: modelo, diretório inteiro com Copiar, branch, início da sessão e squad. Numa janela
   estreita a linha da sessão guarda só modelo, custo e contexto, e o resto fica nesse balão.
3. `P` manda prompt, `/` busca na saída, `D` dispensa com 5 s para desfazer, `J` e `K` trocam o foco para o agente
   da próxima ou da decisão anterior.
4. Clicar no terminal dá o teclado a ele; `Ctrl+]` devolve ao foco. `Esc`, com o teclado fora do terminal, volta ao
   canvas no mesmo enquadramento.
5. `L` recolhe a linha da sessão e `M` recolhe a pendência; a mesma tecla expande. Recolhida, a linha some e o
   botão "Sessão" do cabeçalho mostra o contexto quando passa de 90%; a pendência vira uma linha com quem pede, o
   tipo e o comando, e `1` `2` `3` continuam respondendo. O Argos lembra a escolha para todos os agentes.

Comandos do agente: no prompt do foco ou do nó, `/` no começo do campo lista os comandos que o tipo de agente
oferece (no Claude Code, `/compact`, `/model`, `/clear` e os outros; no Codex, Gemini e demais, os deles), com a
descrição de cada um e os comandos do projeto num grupo à parte. Digitar filtra; `Tab` ou `Enter` completam;
`Ctrl+Enter` envia. Comando com argumento mostra a assinatura e, quando o adaptador declara, os valores (os modelos
de `/model`, com o atual marcado). O Argos não executa nada: o comando vai ao agente como qualquer prompt.

Um agente que encerra com o foco aberto não fecha o foco: ele fica cinza, com o motivo e o terminal só para leitura.

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
