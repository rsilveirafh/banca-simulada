#!/usr/bin/env python3
"""Compara um _banca.md com o gabarito de um projeto fictício.

Uso:
    python testes/avaliar.py <gabarito.md> <_banca.md> <projeto.md>

Critério de acerto (automático): um erro plantado conta como recuperado quando algum comentário
da banca tem trecho que coincide com uma das âncoras do gabarito: uma contém a outra (pedaço com
pelo menos 20 caracteres) ou as duas compartilham um trecho contínuo de pelo menos 40 caracteres
(ou metade da menor, se ela for curta). A comparação usa a mesma normalização da autochecagem.

O resultado automático é um piso: um comentário que aponta o erro certo citando outro trecho não
é contado. Por isso a saída lista os comentários sem par para revisão manual.

Também roda a autochecagem (trecho inexistente) contra o projeto.
Só usa a biblioteca padrão.
"""
from __future__ import annotations

import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "skills" / "revisar" / "scripts"))
from checar_trechos import SEPARADOR, blocos, checar, extrair_trecho, normalizar  # noqa: E402

EIXOS = {"coerência", "hipóteses", "metodologia", "aderência", "ética", "referencial", "abnt",
         "viabilidade"}
GRAVIDADES = {"bloqueante", "importante", "ajuste"}


def cabecalho(linha: str):
    partes = [p.strip().casefold() for p in re.split(r"[·|]", linha)]
    eixo = next((p for p in partes if p in EIXOS), "?")
    grav = next((p for p in partes if p in GRAVIDADES), "?")
    return eixo, grav


def ler_gabarito(texto: str):
    itens = []
    for m in re.finditer(r"^###\s+([A-Z]\d+)\s*(.*)$", texto, re.MULTILINE):
        ini = m.end()
        prox = re.search(r"^###\s", texto[ini:], re.MULTILINE)
        corpo = texto[ini: ini + prox.start()] if prox else texto[ini:]
        eixo, grav = cabecalho(m.group(2))
        ancoras = [extrair_trecho(l) for l in re.findall(r"\*\*Trecho:\*\*\s*(.+)", corpo)]
        aceitos = re.search(r"\*\*Tipos aceitos:\*\*\s*(.+)", corpo)
        tipos = {eixo}
        if aceitos:
            tipos |= {t.strip().casefold() for t in aceitos.group(1).split(",") if t.strip() not in ("—", "-")}
        erro = re.search(r"\*\*Erro:\*\*\s*(.+)", corpo)
        itens.append({"id": m.group(1), "eixo": eixo, "grav": grav, "tipos": tipos,
                      "ancoras": [normalizar(a) for a in ancoras if a],
                      "erro": erro.group(1).strip() if erro else ""})
    return itens


def ler_banca(texto: str):
    comentarios = []
    for cid, corpo in blocos(texto):
        linha_cab = re.search(rf"^###\s+{cid}\b(.*)$", texto, re.MULTILINE).group(1)
        eixo, grav = cabecalho(linha_cab)
        t = re.search(r"\*\*Trecho:\*\*\s*(.+)", corpo)
        trecho = extrair_trecho(t.group(1)) if t else None
        pedacos = [normalizar(p) for p in SEPARADOR.split(trecho)] if trecho else []
        comentarios.append({"id": cid, "eixo": eixo, "grav": grav,
                            "pedacos": [p for p in pedacos if p]})
    return comentarios


def casa(ancora: str, pedaco: str) -> bool:
    menor = min(len(ancora), len(pedaco))
    if menor >= 20 and (ancora in pedaco or pedaco in ancora):
        return True
    m = SequenceMatcher(None, ancora, pedaco, autojunk=False).find_longest_match(
        0, len(ancora), 0, len(pedaco))
    return m.size >= min(40, max(20, menor // 2))


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    gab = ler_gabarito(Path(argv[1]).read_text(encoding="utf-8"))
    banca_txt = Path(argv[2]).read_text(encoding="utf-8")
    projeto_txt = Path(argv[3]).read_text(encoding="utf-8")
    coms = ler_banca(banca_txt)

    usados = set()
    linhas = ["| Erro | Esperado | Recuperado por | Tipo ok | Gravidade dada |",
              "|---|---|---|---|---|"]
    rec_bi = tot_bi = rec_all = 0
    for item in gab:
        pares = [c for c in coms if any(casa(a, p) for a in item["ancoras"] for p in c["pedacos"])]
        usados |= {c["id"] for c in pares}
        ok_tipo = any(c["eixo"] in item["tipos"] for c in pares)
        if item["grav"] in ("bloqueante", "importante"):
            tot_bi += 1
            rec_bi += bool(pares)
        rec_all += bool(pares)
        linhas.append(f"| {item['id']} | {item['eixo']} · {item['grav']} | "
                      f"{', '.join(c['id'] for c in pares) or '**não**'} | "
                      f"{'sim' if ok_tipo else ('não' if pares else '-')} | "
                      f"{', '.join(sorted({c['grav'] for c in pares})) or '-'} |")

    checagem = checar(banca_txt, projeto_txt)
    falhas = [f"{cid} ({detalhe})" for cid, estado, detalhe in checagem if estado in ("FALHA", "SEM TRECHO")]
    sem_par = [f"{c['id']} ({c['eixo']} · {c['grav']})" for c in coms if c["id"] not in usados]

    print("\n".join(linhas))
    print()
    print(f"- Bloqueantes + importantes recuperados: {rec_bi}/{tot_bi} ({100 * rec_bi / max(tot_bi, 1):.0f}%)")
    print(f"- Todos os erros recuperados: {rec_all}/{len(gab)} ({100 * rec_all / max(len(gab), 1):.0f}%)")
    print(f"- Comentários na banca: {len(coms)}")
    print(f"- Trechos inexistentes (autochecagem): {len(falhas)}" + (": " + "; ".join(falhas) if falhas else ""))
    print(f"- Comentários sem par no gabarito (revisar à mão): {', '.join(sem_par) or 'nenhum'}")
    meta = rec_bi / max(tot_bi, 1) >= 0.70 and not falhas
    print(f"- Meta (>= 70% de B+I e zero trecho inexistente): {'ATINGIDA' if meta else 'NÃO ATINGIDA'}")
    return 0 if meta else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
