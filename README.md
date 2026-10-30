# banca-simulada: revisão de projeto de pesquisa como uma banca faria

Plugin do Claude Code que lê um projeto de pesquisa e faz o que uma banca ou um comitê avaliador
faria: aponta problemas de coerência, hipóteses, método, aderência, ética, referencial,
normalização e cronograma, cada um com o **trecho exato** do projeto, a **gravidade** e uma
sugestão. No fim, lista as perguntas prováveis da arguição ou do parecer.

**Revisão, não redação.** A skill aponta e sugere. Não reescreve o projeto, não entrega texto
pronto e não "melhora" a sua redação.

> Versão 0.2. A 0.1 foi testada com projetos de mestrado; a calibração para os outros tipos é nova
> e ainda não tem projeto de teste próprio.

## Tipos de projeto

Os oito eixos são os mesmos para todos. O tipo muda o prazo de referência, contra o que a
aderência é medida e o que pesa mais (detalhes na [rubrica](skills/revisar/rubrica.md)).

| Tipo | Aderência medida contra | O que pesa mais |
|---|---|---|
| TCC | orientador e curso | viabilidade, pergunta clara, método repetível |
| Iniciação científica | projeto do orientador e edital da bolsa | viabilidade, plano de trabalho do estudante |
| Seleção de mestrado ou doutorado | linha, ementa e edital do programa | aderência à linha, viabilidade no prazo |
| Qualificação | linha e banca do programa | método pronto para executar, cronograma até a defesa |
| Pós-doutorado | supervisor, grupo e edital da bolsa | originalidade, independência, produtos previstos |
| Edital de fomento | objetivo e critérios da chamada | mérito, metas e indicadores, equipe, orçamento |
| Concurso docente | área e subárea do concurso | encaixe na área, viabilidade no departamento, ensino e extensão |

## O que ela entrega

Um arquivo `_banca.md`, ao lado do projeto, com:

1. **Mapa do projeto**: pergunta, objetivos, hipóteses, matriz objetivo → método → análise,
   amostra, gatilhos éticos e cronograma, confirmado por você antes da revisão.
2. **Comentários numerados**, cada um com eixo (coerência, hipóteses, metodologia, aderência,
   ética, referencial, ABNT, viabilidade), gravidade (bloqueante, importante, ajuste), trecho
   literal, problema, sugestão e base (pergunta da rubrica e, quando houver, a norma).
3. **Arguição provável**: 10 a 15 perguntas ligadas aos comentários, com o que preparar.
4. **Preparação para a entrevista** e o **registro da autochecagem**.

### Exemplo (projeto fictício de teste)

Trecho do projeto:

> H1: A fragmentação florestal influencia a comunidade de lagartos de serrapilheira, podendo
> aumentar ou diminuir a riqueza e a abundância de acordo com as condições locais de cada fragmento.

Comentário que a skill escreveu no teste de 2026-10-28 (copiado do `_banca.md`):

```markdown
### C01 · bloqueante · hipóteses
- **Onde:** seção 3
- **Trecho:** "A fragmentação florestal influencia a comunidade de lagartos de serrapilheira, podendo aumentar ou diminuir a riqueza e a abundância de acordo com as condições locais de cada fragmento."
- **Problema:** H1 aceita qualquer resultado: aumento, queda ou ausência de diferença podem ser lidos como "condições locais". Não há resultado possível que a contrarie, então ela não é testável. Como H1 é a hipótese que cobre a pergunta inteira (riqueza e abundância), o projeto fica sem hipótese central testável. Ela também fala em "fragmentação" e "condições locais", que não são as variáveis medidas (a área é).
- **Sugestão:** reformular H1 com direção ou forma ligada à variável que o método mede (área do fragmento) e escrever, para si, qual resultado a refutaria. Se a decisão for não prever direção, assumir o caráter exploratório e justificar isso.
- **Base:** HI2, HI3
```

As saídas completas dos testes estão em [testes/execucoes/](testes/execucoes/).

## Como funciona

1. Converte o projeto para Markdown (MarkItDown, gravando em arquivo; PDF também pela leitura
   nativa, inclusive escaneado).
2. Monta o mapa e **para**: você confirma ou corrige. Projeto mal lido gera comentário errado.
3. Revisa um eixo por vez com a [rubrica](skills/revisar/rubrica.md) (8 eixos, 4 a 6 perguntas
   cada).
4. Na ética, detecta seres humanos, menores, povos indígenas, dados pessoais, vertebrados e
   patrimônio genético, e só cita norma que está em
   [referencias/normas.md](skills/revisar/referencias/normas.md), conferida na fonte, com data.
5. Classifica, junta duplicados e ordena por gravidade.
6. Escreve a arguição a partir dos bloqueantes e importantes.
7. **Autochecagem**: um script procura cada trecho citado no texto do projeto e o comentário cujo
   trecho não existe é corrigido ou apagado.

## Instalação

Requisitos: [Claude Code](https://code.claude.com/docs), Python 3 e, para PDF e DOCX,
[MarkItDown](https://github.com/microsoft/markitdown):

```bash
pip install "markitdown[pdf,docx]"
```

Pelo catálogo de plugins [rsilveirafh/claude-plugins](https://github.com/rsilveirafh/claude-plugins):

```bash
claude plugin marketplace add rsilveirafh/claude-plugins
claude plugin install banca-simulada@rsilveirafh-plugins
```

Para testar sem instalar, a partir de um clone deste repositório:

```bash
claude --plugin-dir ./banca-simulada
```

Confira o manifesto com `claude plugin validate ./banca-simulada`.

## Uso

Dentro do Claude Code, na pasta do projeto:

```text
/banca-simulada:revisar meu-projeto.pdf
/banca-simulada:revisar meu-projeto.docx edital.pdf ementa-linha.txt
/banca-simulada:revisar projeto-concurso.pdf edital-concurso.pdf area-do-concurso.txt
```

Argumentos: o projeto (PDF, DOCX ou Markdown) e, opcionalmente, o edital (do programa, da chamada
ou do concurso), a ementa da linha ou a descrição da área do concurso, e o resumo do Lattes do
orientador ou supervisor (arquivo ou texto colado). A skill pergunta o tipo de projeto ao mostrar
o mapa. Sem a ementa e o Lattes, a aderência vira pergunta, não julgamento.

A skill cria `_banca/` (arquivos intermediários) e `_banca.md` (resultado). Edite ou apague à
vontade.

## O que ela não faz

- **Não substitui orientador nem banca.** É um ensaio antes da banca de verdade.
- **Não escreve o projeto por você.** Se você pedir, ela recusa essa parte.
- **Não dá parecer ético nem jurídico.** Aponta onde o projeto precisa de CEP, CEUA, SISBIO,
  SisGen ou cuidado com dados pessoais; quem decide é o comitê da sua instituição.
- **Não confere o texto das normas ABNT**, que são pagas. No eixo ABNT, aponta só o que é
  checável no próprio projeto (citação sem referência, estilo misturado, elemento faltando).
- **Não afirma que uma referência não existe.** Diz "citado sem entrada nas referências" ou
  "não consegui confirmar".
- **Uso de IA em seleção:** alguns programas exigem declaração de uso de IA no projeto. Leia o
  edital do seu programa e declare quando for o caso.
- Seu projeto é enviado ao modelo de linguagem que o Claude Code usa. Não use com projeto de
  terceiros sem autorização.

## Testes

`testes/` tem dois projetos **fictícios**, escritos para o teste, cada um com 12 erros plantados
e um gabarito (erro, tipo, gravidade, trecho exato):

| Projeto | Área | Normas envolvidas |
|---|---|---|
| [ecologia-lagartos](testes/ecologia-lagartos/projeto.md) | ecologia de campo, captura e coleta de lagartos | CEUA (Lei 11.794/2008), SISBIO (Portaria ICMBio 748/2022), SisGen (Lei 13.123/2015) |
| [saude-sono-dm1](testes/saude-sono-dm1/projeto.md) | saúde, adolescentes com diabetes tipo 1 | CEP (Res. CNS 466/2012), LGPD |

**Meta:** recuperar pelo menos 70% dos erros bloqueantes e importantes de cada projeto, com
**zero** trecho citado inexistente.

Para rodar:

1. Copie **só** o `projeto.md` para uma pasta vazia (a skill não pode ver o gabarito).
2. Nessa pasta, rode `/banca-simulada:revisar projeto.md`, confirme o mapa e informe "mestrado, 24 meses,
   sem edital, ementa ou Lattes". Em modo não interativo:
   ```bash
   claude -p "/banca-simulada:revisar projeto.md" --plugin-dir <caminho>/banca-simulada --output-format json
   claude -p "O mapa está correto. ..." --resume <session_id> --plugin-dir <caminho>/banca-simulada
   ```
3. Compare com o gabarito:
   ```bash
   python testes/avaliar.py testes/ecologia-lagartos/gabarito.md <pasta>/_banca.md testes/ecologia-lagartos/projeto.md
   ```
   O script mostra quais erros foram recuperados, por qual comentário, se o tipo bateu, a taxa
   de acerto e os trechos inexistentes. O acerto automático é um piso: comentários sem par no
   gabarito são revistos à mão.

Resultados das execuções em [testes/resultados.md](testes/resultados.md).

Para conferir só os trechos de um `_banca.md` qualquer:

```bash
python skills/revisar/scripts/checar_trechos.py _banca.md projeto.md
```

## Estrutura

```text
banca-simulada/
├── .claude-plugin/
│   └── plugin.json          manifesto do plugin
├── skills/revisar/
│   ├── SKILL.md             etapas da skill /banca-simulada:revisar
│   ├── rubrica.md           calibração por tipo, 8 eixos, perguntas e critérios de gravidade
│   ├── referencias/normas.md normas citáveis, com fonte e data de conferência
│   └── scripts/checar_trechos.py  autochecagem de trechos
└── testes/                  projetos fictícios, gabaritos, avaliador e resultados
```

## In English

`banca-simulada` is a Claude Code plugin that reviews a Brazilian research proposal the way a
committee would: undergraduate thesis, undergraduate research grant, master's or PhD (selection or
qualifying exam), postdoc, funding call, or the research-project exam in a faculty hiring contest. It maps the proposal (question, aims, hypotheses, methods, timeline),
asks the author to confirm the map, then reviews it along eight axes (internal coherence,
hypotheses, methods, fit with the research line, call or contest area, research ethics under Brazilian rules, literature,
ABNT formatting, feasibility), quoting the exact passage for every comment, rating its severity and
listing the questions the committee is likely to ask. A script drops any comment whose quote is not
in the text. It reviews; it does not rewrite the proposal, and it does not replace an advisor or a
committee. Prompts and output are in Portuguese.

## Licença

MIT. Os projetos de teste são fictícios; as normas citadas são de domínio público e as
referências bibliográficas dos projetos de teste apontam para trabalhos reais usados só como
contexto.
