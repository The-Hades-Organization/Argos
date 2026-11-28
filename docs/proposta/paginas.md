# Páginas de design

O design do Argos novo está em páginas HTML no repositório, em `design/`, para abrir no navegador. Cada página tem
um seletor de tema (Sistema, Escuro, Claro) no canto de cima. A página de entrada é `design/index.html`.

Para abrir, sirva a pasta num servidor local e abra o endereço:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory design
# http://127.0.0.1:8765/
```

Abrir o arquivo direto (`xdg-open design/index.html`) também funciona; as fontes vêm do Google Fonts, então sem
rede o navegador usa as fontes de reserva.

| Página | O que mostra | Arquivo |
|---|---|---|
| Design system | Princípios, voz, tokens nos temas escuro e claro, componentes com seus estados e ícones | `design/design-system/index.html` (fonte em `design/design-system/project/`) |
| Direção Coordenador | A direção escolhida para a tela principal: caixa de decisões e pedido ao time em texto | `design/direcoes/coordenador.html` |
| Telas de squad: planta no canvas | Proposta de squad para aprovação, paleta com histórico, convocar soltando no canvas e squad recolhido | `design/direcoes/squads-planta.html` |
| Foco de um agente: direções | Duas direções para o foco de um agente com o terminal ocupando o espaço: a sessão numa linha, ou o terminal inteiro com gaveta só para a pendência | `design/direcoes/foco.html` |
| Canvas principal | Estado padrão, ninguém esperando, muitos agentes, pedido ao time em andamento e folhas de dados, sistema, atividade e interação, com a janela de 1024 px | `design/telas/canvas-principal.html` |
| Recrutar | Lançador de tipos de agente: padrão, primeira vez no projeto, recrutado agora e folhas de dados, sistema, atividade e interação | `design/telas/recrutar.html` |
| Nó de agente | Os seis estados a 100%, o nó ao afastar o zoom e folhas de dados, sistema, atividade e interação | `design/telas/no.html` |
| Foco de um agente | Direção A: trabalhando, esperando você com a pendência no pé do terminal, janela de 1024 px com o balão de Detalhes e folhas de dados, sistema, atividade e interação | `design/telas/foco.html` |

A página do design system é gerada a partir de `design/design-system/project/` (README, `tokens.json`, prévias e
READMEs dos componentes, ícones) por `python3 design/design-system/gerar_index.py .`; edite a fonte e rode de novo, não
o `index.html`.
