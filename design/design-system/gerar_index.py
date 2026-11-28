#!/usr/bin/env python3
"""Gera design/design-system/index.html: o design system do Argos para abrir localmente.

Lê project/README.md, tokens.json, components/*/{README.md,preview.html} e assets/Icones/*.svg.
Uso: python3 design/design-system/gerar_index.py <raiz do repositório>
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1])
DS = ROOT / "design" / "design-system"
P = DS / "project"


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md(text, shift=1):
    """Markdown mínimo: títulos, parágrafos, listas, citações e tabelas."""
    out, para, lst, table = [], [], [], []

    def flush():
        nonlocal para, lst, table
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
        if lst:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in lst) + "</ul>")
        if table:
            rows = [r for r in table if not re.fullmatch(r"\|?[\s:|-]+\|?", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            head = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:])
            out.append(f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
        para, lst, table = [], [], []

    for line in text.splitlines():
        if not line.strip():
            flush()
            continue
        m = re.match(r"(#+)\s+(.*)", line)
        if m:
            flush()
            n = min(len(m.group(1)) + shift, 6)
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif line.startswith("|"):
            if para or lst:
                flush()
            table.append(line)
        elif re.match(r"\s*[-*]\s+", line):
            if para or table:
                flush()
            lst.append(re.sub(r"^\s*[-*]\s+", "", line))
        elif re.match(r"\s*\d+\.\s+", line):
            if para or table:
                flush()
            lst.append(re.sub(r"^\s*\d+\.\s+", "", line))
        elif line.startswith(">"):
            if out and out[-1].startswith('<p class="note">') and not (para or lst or table):
                out[-1] = out[-1][:-4] + " " + inline(line.lstrip("> ").strip()) + "</p>"
            else:
                flush()
                out.append('<p class="note">' + inline(line.lstrip("> ").strip()) + "</p>")
        elif lst and line.startswith("  "):
            lst[-1] += " " + line.strip()
        else:
            para.append(line.strip())
    flush()
    return "\n".join(out)


def tokens_section():
    d = json.loads((P / "tokens.json").read_text())
    rows = []
    for t in d["color"]["tokens"]:
        rows.append(
            f'<tr><td><span class="sw" style="background:var(--{t["name"]})"></span></td>'
            f'<td><code>{t["name"]}</code></td><td class="mono">{t["value"]["dark"]}</td>'
            f'<td class="mono">{t["value"]["light"]}</td><td>{inline(t.get("usage", ""))}</td></tr>')
    color = ('<div class="tw"><table><thead><tr><th></th><th>Token</th><th>Escuro</th><th>Claro</th><th>Uso</th>'
             "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
    other = []
    for key, label in (("spacing", "Espaço"), ("radius", "Forma"), ("shadow", "Sombra"), ("layout", "Medidas")):
        r = "".join(f'<tr><td><code>{t["name"]}</code></td><td class="mono">{html.escape(t["value"])}</td>'
                    f'<td>{inline(t.get("usage", ""))}</td></tr>' for t in d[key]["tokens"])
        other.append(f'<h3>{label}</h3><div class="tw"><table><tbody>{r}</tbody></table></div>')
    return f'<section id="tokens"><h2>Tokens</h2><h3>Cor</h3>{color}{"".join(other)}</section>'


def components_section():
    items, nav = [], []
    for c in sorted((P / "components").iterdir()):
        prev = c / "preview.html"
        if not c.is_dir() or not prev.exists():
            continue
        src = prev.read_text()
        m = re.search(r'@dsCard(?:\s+group="([^"]+)")?', src)
        group = (m.group(1) if m else None) or "Capa"
        readme = c / "README.md"
        doc = md(readme.read_text(), shift=2) if readme.exists() else ""
        nav.append(f'<a href="#c-{c.name}">{c.name}</a>')
        items.append(f'<article class="comp" id="c-{c.name}"><p class="grp">{group}</p>'
                     f'<div class="card">{src}</div><div class="md">{doc}</div></article>')
    return (f'<section id="componentes"><h2>Componentes</h2><nav class="toc">{"".join(nav)}</nav>'
            + "".join(items) + "</section>")


def icons_section():
    d = P / "assets" / "Icones"
    order = json.loads((P / "design-system.json").read_text())["assetGroups"]["Icones"]["order"]
    tiles = "".join(f'<figure><span class="ic">{(d / n).read_text()}</span><figcaption>{n[:-4]}</figcaption></figure>'
                    for n in order if (d / n).exists())
    readme = d / "README.md"
    doc = md(readme.read_text(), shift=2) if readme.exists() else ""
    return f'<section id="icones"><h2>Ícones</h2><div class="icons">{tiles}</div><div class="md">{doc}</div></section>'


CSS = """
body { margin: 0; background: var(--canvas); color: var(--text); font: 400 14px/21px var(--sans); }
.doc { max-width: 1240px; margin: 0 auto; padding: 32px 16px 64px; display: grid; gap: 40px; }
.doc h1 { font: 400 32px/38px var(--display); margin: 0; }
.doc h2 { font: 400 24px/30px var(--display); margin: 0 0 12px; }
.doc h3 { font: 600 15px/22px var(--sans); margin: 20px 0 8px; }
.doc h4, .doc h5 { font: 600 13px/20px var(--sans); margin: 16px 0 6px; }
.doc p, .doc li { max-width: 80ch; color: var(--text-muted); }
.doc p { margin: 0 0 10px; }
.doc .note { color: var(--text); border-left: 2px solid var(--border); padding-left: 12px; }
.doc a { color: var(--text); }
.doc code, .mono { font: 400 12px/18px var(--mono); }
.dochead { display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between; align-items: flex-start; }
.themes { display: flex; border: 1px solid var(--border); }
.themes button { height: 28px; padding: 0 10px; border: 0; background: transparent; color: var(--text-muted);
  font: 600 12px/16px var(--sans); cursor: pointer; }
.themes button[aria-pressed="true"] { background: var(--tint-selected); color: var(--text); }
.toc { display: flex; flex-wrap: wrap; gap: 4px 16px; margin-bottom: 24px; }
.tw { overflow-x: auto; margin-bottom: 12px; }
table { border-collapse: collapse; font-size: 13px; line-height: 19px; }
th, td { text-align: left; vertical-align: top; padding: 6px 12px 6px 0; border-bottom: 1px solid var(--border); }
th { font-weight: 600; color: var(--text); }
td { color: var(--text-muted); }
.sw { display: block; width: 28px; height: 20px; border: 1px solid var(--border); }
.comp { border-top: 1px solid var(--border); padding-top: 20px; margin-top: 28px; display: grid; gap: 16px; }
.comp .grp { font: 600 12px/16px var(--sans); color: var(--text-muted); margin: 0; }
.comp .card { border: 1px solid var(--border); overflow-x: auto; }
.icons { display: grid; grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); gap: 8px; margin-bottom: 16px; }
.icons figure { margin: 0; border: 1px solid var(--border); padding: 12px 8px; display: grid; gap: 8px;
  justify-items: center; }
.icons .ic svg { width: 24px; height: 24px; color: var(--text); }
.icons figcaption { font: 400 11px/14px var(--mono); color: var(--text-muted); }
"""

SCRIPT = """
(function () {
  function setTheme(t) {
    if (t) document.documentElement.setAttribute('data-theme', t);
    else document.documentElement.removeAttribute('data-theme');
    document.querySelectorAll('.themes button').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-set') === t));
    });
  }
  var saved = '';
  try { saved = localStorage.getItem('argos-tema') || ''; } catch (e) { saved = ''; }
  saved = saved || document.documentElement.getAttribute('data-theme') || '';
  setTheme(saved);
  document.querySelectorAll('.themes button').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-set');
      setTheme(t);
      try { localStorage.setItem('argos-tema', t); } catch (e) { /* tema só desta visita */ }
    });
  });
})();
"""


def main():
    readme = (P / "README.md").read_text()
    readme = re.sub(r"\A#\s+.*\n", "", readme)
    page = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Design system do Argos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Geist+Mono:wght@400;500;600&family=Marcellus&display=swap">
<link rel="stylesheet" href="../telas/tokens.css">
<link rel="stylesheet" href="project/components/bundle.css">
<style>{CSS}</style>
<main class="doc">
  <header class="dochead">
    <div>
      <h1>Design system do Argos</h1>
      <p class="mono">Gerado de <code>design/design-system/project/</code>. Não editar à mão.</p>
      <nav class="toc"><a href="#principios">Princípios</a><a href="#tokens">Tokens</a>
      <a href="#componentes">Componentes</a><a href="#icones">Ícones</a><a href="../index.html">Todas as páginas</a></nav>
    </div>
    <div class="themes" role="group" aria-label="Tema">
      <button type="button" data-set="">Sistema</button><button type="button" data-set="dark">Escuro</button><button type="button" data-set="light">Claro</button>
    </div>
  </header>
  <section id="principios" class="md">{md(readme)}</section>
  {tokens_section()}
  {components_section()}
  {icons_section()}
</main>
<script>{SCRIPT}</script>
"""
    (DS / "index.html").write_text(page)
    print("ok:", DS / "index.html")


main()
