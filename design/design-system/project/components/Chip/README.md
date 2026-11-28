# Chip

Pílula monoespaçada para identificadores dentro do texto (crate, arquivo, campo, worktree) e para o tipo de agente.

**Anatomia.** `mono-small` (11/14), altura 20, fio `border`, raio 0. O identificador usa `text`; o tipo de agente usa
`text-muted`. O contador é a única peça redonda além do ponto de estado: `radius-full`, fundo `agent-waiting`, texto
`on-primary`, e só conta quem espera você.

**Regras.** Chip não é botão: quando é clicável (abrir o arquivo, filtrar pelo tipo), ganha hover `border-hover` e foco
`focus`, sem mudar de tamanho. Nada de chip colorido por tipo de agente: o tipo é texto.
