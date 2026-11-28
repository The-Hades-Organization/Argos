#!/usr/bin/env python3
"""Peças da tela Vazio e erro no design system.

Uso: python3 gen_ds_vazio.py <raiz da worktree>
- Nó de agente ganha dois estados: desatualizado (supervisor não responde: o último estado lido, sem entrada) e
  esqueleto (abrindo um canvas grande: o nó na posição salva, antes do primeiro estado).
- Vazio ganha um cartão próprio, com as variantes na lista (a que já existia), no canvas e a tela de falha.
- Barra de estado: "Sem supervisor" passa a ser classe (a prévia usava estilo solto).
Escreve o bloco do bundle.css (entre START e END, antes do bloco do nó), as prévias e os READMEs. Idempotente.
A tela (gen_vazio.py) importa daqui as peças.
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_canvas as C  # noqa: E402  (ic, kbd, st)
import gen_ds_foco as D  # noqa: E402  (btn, copy_btn, page, cell, row, box)

COMP = ROOT / "design/design-system/project/components"
START = "/* Vazio e erro · nó desatualizado, esqueleto, vazio no canvas, tela de falha, barra sem supervisor */"
END = "/* fim: Vazio e erro */"
NO_MARK = "/* NoDeAgente · contexto, linhas novas, prompt e teclado */"
PV_START, PV_END = "<!-- vazio:inicio -->", "<!-- vazio:fim -->"

ic, kbd, st, btn = C.ic, C.kbd, C.st, D.btn

CSS = START + """
.status .off { display: inline-flex; align-items: center; gap: 6px; color: var(--danger); font-weight: 600; }
.status .off .tri { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 9px solid var(--danger); }
.node .seen { display: inline-flex; align-items: center; gap: 4px; flex: none; font: 400 11px/14px var(--mono); color: var(--text-muted); white-space: nowrap; font-variant-numeric: tabular-nums; }
.node .seen svg.ic { width: 12px; height: 12px; }
.node.stale .pulse { animation: none; }
.node.stale .term { color: var(--term-muted); }
.node.stale .term .frozen { position: absolute; left: 0; right: 0; bottom: 0; padding: 3px 10px; background: var(--term-bg); border-top: 1px solid color-mix(in srgb, var(--term-fg) 14%, transparent); color: var(--term-fg); font: 400 11px/14px var(--sans); white-space: normal; }
.node.stale .ft { color: var(--text-disabled); }
.node.skel .hd .nm { color: var(--text-muted); }
.node.skel .term { display: grid; align-content: start; gap: 8px; padding-top: 12px; }
.skb { display: block; height: 8px; background: color-mix(in srgb, var(--term-fg) 12%, transparent); }
.node.skel .ft .skb { width: 88px; height: 6px; background: var(--fill-1); }
.node.skel .ft .r.skb { width: 64px; }
@media (prefers-reduced-motion: no-preference) {
  .skb { animation: skel 1600ms ease-in-out infinite; }
  @keyframes skel { 50% { opacity: .45; } }
}
.empty.big { width: 440px; max-width: 100%; padding: 28px 28px 24px; gap: 10px; border: 1px solid var(--border); background: var(--surface); font-size: 13px; line-height: 18px; }
.empty.big .ttl { display: flex; align-items: center; gap: 10px; font: 400 24px/30px var(--display); color: var(--text); }
.empty.big .ttl svg.ic { width: 20px; height: 20px; flex: none; }
.empty.big .acts { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
.empty.big .btn { margin-left: 0; }
.empty.big .ex { display: grid; gap: 4px; width: 100%; margin-top: 8px; padding-top: 12px; border-top: 1px solid var(--divider); font-size: 12px; line-height: 17px; }
.empty.big .ex .say { font: 400 12px/17px var(--mono); color: var(--text); }
.empty.big .dl { width: 100%; padding: 6px 0 0; grid-template-columns: 64px minmax(0, 1fr); }
.empty.big.slim { width: 360px; padding: 20px; gap: 8px; }
.empty.big.slim .ttl { font-size: 18px; line-height: 24px; }
.empty.big.fail { border-left: 2px solid var(--danger); }
.empty.big.fail .ttl svg.ic { color: var(--danger); }
""" + END + "\n"


# ---------- peças (a tela importa daqui) ----------

def status_off(since, right=""):
    """Barra de estado sem supervisor. `since` é a hora do último estado lido."""
    return (f'<footer class="status"><span class="off"><span class="tri"></span>Supervisor desligado · reconectando'
            f'</span><span class="mono">estado de {since}</span><span class="grow"></span>{right}</footer>')


def seen(at):
    return f'<span class="seen">{ic("circle-dashed", 12)}às {at}</span>'


def stale_node(name, kind, state_html, term, ft_left, ft_right, box, at, cls=""):
    """Nó com o último estado lido: estado congelado, marca da hora, terminal sem entrada."""
    left, top, w, h = box
    pos = f"left:{left}px;top:{top}px;" if left is not None else "position:relative;"
    return (f'<article class="node stale{cls}" style="{pos}width:{w}px;height:{h}px">'
            f'<div class="hd"><span class="nm">{name}</span><span class="tp">{kind}</span>{state_html}{seen(at)}</div>'
            f'<div class="term">{term}<span class="frozen">Parado na tela de {at} · não aceita digitação</span></div>'
            f'<div class="ft"><span>{ft_left}</span><span class="r">{ft_right}</span></div></article>')


def skel_node(name, kind, box, lines=(86, 62, 74, 40)):
    left, top, w, h = box
    pos = f"left:{left}px;top:{top}px;" if left is not None else "position:relative;"
    bars = "".join(f'<span class="skb" style="width:{p}%"></span>' for p in lines)
    return (f'<article class="node skel" style="{pos}width:{w}px;height:{h}px" aria-busy="true">'
            f'<div class="hd"><span class="nm">{name}</span><span class="tp">{kind}</span>{st("starting", "Lendo")}</div>'
            f'<div class="term">{bars}</div>'
            f'<div class="ft"><span class="skb"></span><span class="r skb"></span></div></article>')


def empty_big(title, text, acts="", extra="", icon="", cls=""):
    a = f'<div class="acts">{acts}</div>' if acts else ""
    i = ic(icon, 20) if icon else ""
    role = ' role="alert"' if "fail" in cls else ""
    return (f'<div class="empty big{cls}"{role}><span class="ttl">{i}{title}</span><span>{text}</span>'
            f'{extra}{a}</div>')


def say(text):
    return f'<span class="say">{text}</span>'


def first_time(slim=False):
    acts = btn("Recrutar", ("R",), "primary md")
    ex = ('<div class="ex"><span>Ou peça ao coordenador, na coluna ao lado:</span>'
          f'{say("recrute um claude-code para revisar a PR 12")}</div>')
    if slim:
        return empty_big("Nenhum agente ainda", "Recrute o primeiro agente.", acts, cls=" slim")
    return empty_big("Nenhum agente ainda",
                     "Cada agente roda num terminal aqui no canvas. Os tipos de fábrica já estão prontos.", acts, ex)


def after_use():
    return empty_big("Nenhum agente no canvas",
                     f'Os 6 dispensados hoje estão no <span class="btn ghost xs">Histórico{ic("chevron-right", 12)}'
                     "</span>", btn("Recrutar", ("R",), "primary md"), cls=" slim")


LOG = "~/.local/state/argos/supervisor.log"


def fail_screen():
    dl = ('<dl class="dl">'
          f'<dt>Motivo</dt><dd><span class="v mono">o socket /run/user/1000/argos/supervisor.sock já está em uso '
          f'(pid 18822)</span></dd>'
          f'<dt>Log</dt><dd><span class="v mono">{LOG}</span>{D.copy_btn()}</dd></dl>')
    acts = btn("Tentar de novo", ("Enter",), "primary md") + btn("Abrir o log", (), "secondary md")
    return empty_big("O supervisor não subiu",
                     "Sem ele, o Argos não inicia terminais nem lê o estado dos agentes. Nada foi perdido: o canvas "
                     "salvo abre quando ele subir.", acts, dl, icon="triangle-alert", cls=" fail")


# ---------- prévias ----------

cell, row, box = D.cell, D.row, D.box

TERM = ('<span class="m">$ cargo test -p hades-core lock</span>\nrunning 18 tests\n'
        'test lock::expira_sem_dono ... ok\ntest lock::renova_antes_do_ttl ... ok')


def preview_node():
    w = 360
    cells = [
        cell("Desatualizado · trabalhando", box(stale_node(
            "lock-ttl", "agy", st("working", "Trabalhando · 3 min"), TERM, "agy · padrão", "US$ 0,31 · 44%",
            (None, None, w, 170), "14h31"), w + 2), w + 2),
        cell("Desatualizado · esperando você", box(stale_node(
            "diario-v2", "opencode", st("waiting", "Esperando você", pulse=True),
            "Pergunta: manter o campo \"ts\" em segundos\nou passar para milissegundos?", "qwen3-coder · alto",
            "US$ 0,09 · 17%", (None, None, w, 170), "14h31", " waiting"), w + 2), w + 2),
        cell("Esqueleto", box(skel_node("proposta", "claude-code", (None, None, w, 170)), w + 2), w + 2),
    ]
    return f'{PV_START}\n<div style="display:grid;gap:28px;margin-top:28px">{row("Sem o supervisor", cells)}</div>\n{PV_END}'


def preview_empty():
    lst = ('<div class="empty"><b>Ninguém espera você</b><span>9 agentes trabalhando. A última decisão foi '
           'respondida às 14h05.</span></div>')
    cells = [
        cell("Na lista ou na coluna", box(lst, 320), 320),
        cell("No canvas · primeira vez", box(first_time(), 442), 442),
        cell("No canvas · depois de uso", box(after_use(), 362), 362),
        cell("No canvas · janela estreita", box(first_time(slim=True), 362), 362),
        cell("Tela de falha", box(fail_screen(), 442), 442),
    ]
    return '<div style="display:grid;gap:28px;padding:16px">' + row("Vazio", cells, 3) + "</div>"


def preview_status():
    right = '<span class="mono">14h33</span>'
    on = ('<footer class="status" style="width:820px;height:26px"><span><span class="ok-dot"></span>Supervisor ligado'
          '</span><span class="mono">9 agentes + coordenador · 3 esperando você</span><span class="grow"></span>'
          '<span class="mono">US$ 4,18 hoje · coordenador US$ 0,36</span><span class="mono">14h07</span></footer>')
    off = status_off("14h31", right).replace('class="status"', 'class="status" style="width:820px;height:26px"', 1)
    high = ('<footer class="status" style="width:820px;height:26px"><span><span class="ok-dot"></span>Supervisor '
            'ligado</span><span class="mono">14 agentes · 4 esperando você</span><span class="grow"></span>'
            '<span class="mono" style="color:var(--warn)">US$ 12,40 hoje · acima de US$ 10,00</span>'
            '<span class="mono">14h07</span></footer>')
    return (f'<div class="mx" style="grid-template-columns:120px max-content"><span class="rh">Normal</span>{on}'
            f'<span class="rh">Sem supervisor</span>{off}<span class="rh">Custo alto</span>{high}</div>')


README_EMPTY = """# Vazio

O que aparece no lugar de uma lista, de uma área ou do canvas quando não há nada a mostrar, ou quando o que
deveria estar ali não pôde ser lido. Diz o que falta e a próxima ação, nunca só "nada aqui".

**Anatomia.**
- Na lista ou na coluna: fio tracejado `border-hover`, título 13 px 600 `text`, texto 12 px `text-muted`, ação
  fantasma opcional. Encosta à esquerda.
- No canvas (`big`): cartão `surface` com fio `border`, centrado no canvas; título 24/30 na fonte de exibição,
  texto 13 px `text-muted`, uma ação primária e, na primeira vez, um exemplo do que pedir ao coordenador, em `mono`,
  sob um fio `divider`.
- Janela estreita ou depois de uso (`big slim`): título 18/24, uma frase e a ação. Sem exemplo.
- Tela de falha (`big fail`): no lugar do canvas, quando o app não tem estado nenhum para mostrar. Fio de 2 px
  `danger` à esquerda, ícone `triangle-alert` em `danger` antes do título, o motivo e o caminho do log numa lista
  (`dl`) com Copiar, e "Tentar de novo" como primária. Anuncia ao leitor de tela (`role="alert"`).

**Regras.**
- Uma ação primária no máximo, e ela é a que resolve (Recrutar, Tentar de novo).
- O vazio da primeira vez é enxuto: uma frase, Recrutar e o exemplo. Sem tour nem passos.
- Vazio depois de uso não repete a explicação; aponta onde o que saiu foi parar (Histórico).
- Falha que deixa ver alguma coisa usa a Faixa no topo da área, não esta tela.

| Variante | Como fica |
|---|---|
| Lista ou coluna | Tracejado, à esquerda, ação fantasma |
| Canvas · primeira vez | Cartão central, título de exibição, Recrutar e o exemplo |
| Canvas · depois de uso, estreito | Cartão menor, uma frase e Recrutar |
| Tela de falha | Fio `danger`, ícone, motivo, log com Copiar, Tentar de novo |

**Não fazer.** Ilustração ou mascote; "Nada por aqui!"; duas primárias; esconder o caminho do log na falha.
"""

NODE_ROWS = [
    ("| Desatualizado |", "| Desatualizado | O supervisor não responde: o último estado lido, sem pulso, com a marca "
                          "`circle-dashed` e a hora (\"às 14h31\"); terminal em `term-muted` com \"Parado na tela de "
                          "14h31 · não aceita digitação\" no pé; rodapé em `text-disabled`. Mantém fio e fundo do "
                          "estado, para quem esperava continuar à vista |\n"),
    ("| Esqueleto |", "| Esqueleto | Abrindo um canvas que passa de 1 s: o nó na posição e no tamanho salvos, com "
                      "nome e tipo, \"Lendo\", e barras no lugar do terminal e do rodapé. Sem tela branca; com "
                      "movimento reduzido as barras não pulsam |\n"),
]

INDEX_LINE = ("| Vazio |", "| Vazio | Conteúdo | Na lista, no canvas (primeira vez, depois de uso, estreito) e a "
                           "tela de falha, sempre com a próxima ação |\n", "| Faixa |")


def main():
    comp = COMP
    bundle = comp / "bundle.css"
    b = bundle.read_text()
    if START in b:
        b = b[:b.index(START)] + b[b.index(END) + len(END):].lstrip("\n")
    i = b.index(NO_MARK)
    bundle.write_text(b[:i] + CSS + "\n" + b[i:])

    d = comp / "Vazio"
    d.mkdir(exist_ok=True)
    (d / "README.md").write_text(README_EMPTY)
    (d / "preview.html").write_text(D.page("Conteúdo", 900, preview_empty()))

    n = comp / "NoDeAgente"
    p = (n / "preview.html").read_text()
    if PV_START in p:
        p = p[:p.index(PV_START)] + preview_node() + p[p.index(PV_END) + len(PV_END):]
    else:
        j = p.rindex("</div>")
        p = p[:j] + preview_node() + "\n" + p[j:]
    p = p.replace('@dsCard group="Agente" height=1500', '@dsCard group="Agente" height=1760')
    (n / "preview.html").write_text(p)
    r = (n / "README.md").read_text()
    for mark, line in NODE_ROWS:
        if mark not in r:
            k = r.index("\n", r.index("| Encerrado |")) + 1
            r = r[:k] + line + r[k:]
    (n / "README.md").write_text(r)

    s = comp / "BarraDeEstado"
    sp = (s / "preview.html").read_text()
    head, _, _ = sp.partition('<div class="mx"')
    (s / "preview.html").write_text(head + preview_status() + "\n</div>\n")
    sr = (s / "README.md").read_text()
    sr = sr.replace('| Sem supervisor | Triângulo e texto em `danger`: "Supervisor desligado · reconectando", e a hora '
                    'do último estado. Única situação que vale para o app inteiro |',
                    '| Sem supervisor | Classe `off`: triângulo e texto em `danger` 600, "Supervisor desligado · '
                    'reconectando", e "estado de 14h31" (a hora do último estado lido). Única situação que vale '
                    'para o app inteiro |')
    (s / "README.md").write_text(sr)

    idx = ROOT / "design/design-system/project/README.md"
    t = idx.read_text()
    mark, line, anchor = INDEX_LINE
    if mark not in t:
        j = t.index("\n", t.index(anchor)) + 1
        t = t[:j] + line + t[j:]
    t = t.replace("| Nó de agente | Agente | A peça do canvas, nos seis estados, selecionado, hover, foco e zoom "
                  "distante |", "| Nó de agente | Agente | A peça do canvas, nos seis estados, selecionado, hover, "
                  "foco, zoom distante, desatualizado e esqueleto |")
    idx.write_text(t)
    print("ok: bundle.css (Vazio e erro), Vazio, NoDeAgente, BarraDeEstado")


if __name__ == "__main__":
    main()
