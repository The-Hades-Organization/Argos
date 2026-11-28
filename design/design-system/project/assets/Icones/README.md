# Ícones

O Argos usa os ícones do Hades-UI v0.3.1 (`crates/hades-ui/assets/icons/`), os mesmos das outras ferramentas da Hades.
Aqui estão os 25 que as telas do Argos usam; os 171 do conjunto estão no Hades-UI, pelo mesmo nome.

**Por que este conjunto.** O Argos é GPL-3.0. Os ícones de linha são do Lucide v0.460.0, sob a licença ISC, que é
permissiva e compatível com a GPL-3.0: basta manter o aviso de copyright, que está em `LICENSE.txt`. Os desenhos
próprios da Hades (como `argos`) estão sob a licença MIT do Hades-UI, também compatível. Um conjunto só mantém o Argos
igual às outras cinco ferramentas, e o gpui já os carrega pelo `IconName` do Hades-UI, sem dependência nova.

**Como usar.** Traço de 2 em 24 (cerca de 1,3 px a 16 px), ponta quadrada e junta em ângulo, ajustados ao painel da
Hades. 16 px na interface, 14 px em chip e no trilho recolhido. A tinta é `currentColor`: o ícone herda a cor do texto
(`text`, `text-muted` ou `on-rail`), nunca uma cor própria. Ícone sozinho leva nome acessível; ícone ao lado de rótulo
some do leitor de tela. Nas pré-visualizações desta página os arquivos aparecem em preto, porque imagem não herda cor.

| Ícone | Uso no Argos |
|---|---|
| `argos` | Marca do app no trilho |
| `layout-dashboard` | Canvas (trilho) |
| `messages-square` | Coordenador |
| `users` | Squads e biblioteca de squads |
| `history` | Histórico |
| `plug` | Adaptadores |
| `sliders-horizontal` | Configuração |
| `plus`, `minus`, `maximize` | Recrutar; zoom; enquadrar tudo |
| `mouse-pointer-click`, `sticky-note` | Ferramentas do canvas: selecionar, nota |
| `play`, `pencil`, `power-off` | Convocar, editar e aposentar squad |
| `check`, `x`, `chevron-right` | Opção recomendada; fechar; abrir detalhe |
| `corner-down-left` | Responder com texto (Enter) |
| `square-terminal`, `bot` | Abrir terminal; agente |
| `triangle-alert`, `circle-dashed`, `loader-circle` | Erro; iniciando; carregando |
| `coins` | Custo |
