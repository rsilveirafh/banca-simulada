#!/usr/bin/env python3
"""Autochecagem da banca simulada: confere se cada trecho citado existe no texto do projeto.

Uso:
    python checar_trechos.py <_banca.md> <projeto.md>

Lê cada bloco de comentário (cabeçalho "### C01 ...") do arquivo da banca, extrai a linha
"- **Trecho:**" e procura o trecho no Markdown do projeto. Um trecho pode juntar pedaços do
mesmo parágrafo com "[...]"; cada pedaço precisa existir, na ordem.

A comparação ignora diferenças que não mudam o texto: maiúsculas/minúsculas, espaços e quebras
de linha, aspas curvas/retas, travessões, marcação Markdown (*, _, `, |, #) e hifenização de fim
de linha. Qualquer outra diferença conta como trecho inexistente.

Saída: uma linha por comentário (OK, FALHA, AUSENTE, SEM TRECHO) e um resumo.
Código de saída: 0 se todos os trechos foram achados (ou declarados ausentes); 1 caso contrário.
Só usa a biblioteca padrão.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

CABECALHO = re.compile(r"^###\s+(C\d+)\b.*$", re.MULTILINE)
LINHA_TRECHO = re.compile(r"^\s*[-*]\s*\*\*Trecho:\*\*\s*(.+)$", re.MULTILINE)
SEPARADOR = re.compile(r"\s*\[\s*(?:\.\.\.|…)\s*\]\s*")
ASPAS = {"“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
         "‘": "'", "’": "'", "´": "'", "`": "'"}
TRACOS = {"–": "-", "—": "-", "−": "-", "‐": "-", "‑": "-"}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFC", texto)
    texto = texto.replace("­", "")              # hífen discreto
    texto = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", texto)  # hifenização de fim de linha
    for antigo, novo in {**ASPAS, **TRACOS}.items():
        texto = texto.replace(antigo, novo)
    texto = texto.replace(" ", " ").replace("…", "...")
    texto = re.sub(r"[*_|#>]", " ", texto)            # marcação Markdown e tabelas
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip().casefold()


def extrair_trecho(linha: str) -> str | None:
    """Devolve o conteúdo entre a primeira e a última aspa da linha, ou None."""
    linha = linha.strip()
    for abre, fecha in (('"', '"'), ("“", "”")):
        i, j = linha.find(abre), linha.rfind(fecha)
        if i != -1 and j > i:
            return linha[i + 1:j]
    return None


def blocos(banca: str):
    marcas = list(CABECALHO.finditer(banca))
    for n, m in enumerate(marcas):
        fim = marcas[n + 1].start() if n + 1 < len(marcas) else len(banca)
        corpo = banca[m.end():fim]
        # o bloco termina no próximo título de seção (## ...), se houver
        corte = re.search(r"^##\s", corpo, re.MULTILINE)
        if corte:
            corpo = corpo[:corte.start()]
        yield m.group(1), corpo


def checar(banca: str, projeto: str):
    alvo = normalizar(projeto)
    resultados = []
    for cid, corpo in blocos(banca):
        achado = LINHA_TRECHO.search(corpo)
        if not achado:
            resultados.append((cid, "SEM TRECHO", "bloco sem linha '- **Trecho:**'"))
            continue
        bruto = achado.group(1)
        if bruto.strip().lower().startswith("[ausente]"):
            resultados.append((cid, "AUSENTE", bruto.strip()))
            continue
        trecho = extrair_trecho(bruto)
        if not trecho or not trecho.strip():
            resultados.append((cid, "SEM TRECHO", "trecho sem aspas ou vazio"))
            continue
        pos = 0
        falhou = None
        for pedaco in SEPARADOR.split(trecho):
            p = normalizar(pedaco)
            if not p:
                continue
            k = alvo.find(p, pos)
            if k == -1:
                falhou = pedaco.strip()
                break
            pos = k + len(p)
        if falhou is None:
            resultados.append((cid, "OK", ""))
        else:
            resultados.append((cid, "FALHA", f"não encontrado: \"{falhou[:160]}\""))
    return resultados


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    banca = Path(argv[1]).read_text(encoding="utf-8")
    projeto = Path(argv[2]).read_text(encoding="utf-8")
    resultados = checar(banca, projeto)
    if not resultados:
        print("Nenhum comentário encontrado (cabeçalhos '### C01 ...').")
        return 1
    for cid, estado, detalhe in resultados:
        print(f"{estado:10} {cid}  {detalhe}".rstrip())
    contagem = {}
    for _, estado, _ in resultados:
        contagem[estado] = contagem.get(estado, 0) + 1
    print("---")
    print("Resumo: " + ", ".join(f"{k}={v}" for k, v in sorted(contagem.items())))
    ruins = contagem.get("FALHA", 0) + contagem.get("SEM TRECHO", 0)
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
