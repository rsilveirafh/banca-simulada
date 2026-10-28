# Resultados dos testes

Meta: em cada projeto fictício, recuperar **≥ 70%** dos erros bloqueantes e importantes, com
**zero** trecho citado inexistente.

## 2026-10-28: v0.1

**Como foi rodado:**
- Claude Code 2.1.312, modelo padrão da conta, em modo não interativo (`claude -p`), com o plugin
  carregado por `--plugin-dir`.
- Cada projeto ficou numa pasta vazia, só com o `projeto.md`, fora do repositório, para a skill
  não ver o gabarito.
- **Turno 1:** `/banca:revisar projeto.md`. A skill montou o mapa e parou no portão humano nas
  duas execuções.
- **Turno 2** (`--resume` da mesma sessão): "O mapa está correto. É mestrado acadêmico, prazo de
  24 meses. Não tenho edital, ementa da linha nem Lattes da orientação; siga sem eles." É uma
  confirmação neutra, sem pista sobre os erros.
- Pontuação com `python testes/avaliar.py <gabarito> <_banca.md> <projeto>`, seguida de revisão
  manual dos comentários sem par no gabarito.
- As saídas completas estão em [execucoes/](execucoes/).

### Placar

| Execução | Projeto | B + I recuperados | Todos | Comentários (B/I/A) | Trechos inexistentes | Script de autochecagem | Tempo | Custo |
|---|---|---|---|---|---|---|---|---|
| r1 | saude-sono-dm1 | **10/10 (100%)** | 12/12 | 19 (4/10/5) | 0 | rodou | 4,1 min | US$ 1,63 |
| r1 | ecologia-lagartos | **10/10 (100%)** após revisão manual (9/10 automático) | 11/12 automático; 12/12 manual | 20 (5/9/6) | 0 | **não rodou** (ver abaixo) | 5,2 min | US$ 1,85 |
| r2 | ecologia-lagartos | **10/10 (100%)** | 12/12 | 20 (5/12/3) | 0 | rodou | 3,8 min | US$ 1,53 |

**Meta atingida nos dois projetos**, em todas as execuções.

### O que a revisão manual mudou

- **r1, ecologia, E03** (GLMM com 4 fragmentos): o avaliador automático não achou par porque a
  skill juntou E03 e E04 num só comentário (C02), que cita o trecho da pseudorreplicação e
  discute, no texto, os 4 níveis do efeito aleatório e os parâmetros do nível de fragmento.
  Contado como recuperado. Na r2, os dois erros saíram em comentários separados (C02 e C14).

### Tipo e gravidade

- Tipo: bateu com o gabarito (ou com um tipo aceito) em todos os erros recuperados.
- Gravidade: os bloqueantes do gabarito saíram como bloqueantes. **E09** (redação até o mês 26,
  com defesa no 24) saiu como bloqueante nas duas execuções; o gabarito diz importante. A leitura
  da skill é defensável (a etapa termina depois da defesa, critério de bloqueante da rubrica
  VC1). Rever o gabarito ou a rubrica.
- **E04** (pseudorreplicação) saiu como bloqueante na r1, porque foi fundida com E03.

### Comentários além do gabarito

Os comentários sem par foram lidos um a um. Nenhum está errado. A maioria aponta problemas reais
que não foram plantados de propósito:
- **saude:** H2 sem análise própria (C06); lacuna e evidência experimental afirmadas sem citação
  (C08); HbA1c retrospectiva coletada sem uso em nenhuma análise (C11); teste t sobre a variação
  da HbA1c sem ajuste pelo valor inicial (C12); perdas no seguimento (C16); variáveis do Quadro 1
  sem instrumento (C17); nota técnica que vai além do desenho (C18).
- **ecologia:** lacuna sem citação (C06); "especialista de interior" sem critério e H2 sem análise;
  quantidade de habitat no entorno não medida, embora o projeto cite Fahrig (2003); linhas a
  100 m da borda que talvez não caibam em fragmentos de 38 ha; logística de campo e orçamento sem
  hospedagem nem auxiliares; bem-estar nos baldes (afogamento, calor) para a CEUA.

Ou seja: os projetos fictícios têm mais problemas do que os 12 plantados. Para a próxima versão
do gabarito, vale listar esses achados como "extras legítimos" (alguns já estão no topo de cada
gabarito).

### Problema encontrado e corrigido

Na r1 de ecologia, a skill tentou rodar o script de autochecagem com `cd ... && python ...` e
depois pela ferramenta PowerShell. As duas chamadas pediram aprovação, que não existe em modo não
interativo. A skill fez a busca dos trechos à mão e registrou isso no arquivo (o avaliador
confirmou depois: zero trecho inexistente). Correção feita no `SKILL.md`: `allowed-tools` passou a
incluir `PowerShell(python *)`, `PowerShell(py *)` e `PowerShell(markitdown *)`, e a Etapa 7 manda
rodar o script num comando só, com caminhos absolutos, sem `cd`, `&&`, `|` ou redirecionamento.
Na r2 o script rodou na primeira tentativa.

### Limites deste teste

- **Mesmo modelo dos dois lados.** Os projetos e os erros foram escritos com ajuda do mesmo tipo
  de modelo que faz a revisão. Erros plantados assim tendem a ser "legíveis" para ele. 100% aqui
  não garante o mesmo desempenho em projeto real. O próximo teste precisa de projetos que o
  Ricardo escreva à mão e dos projetos antigos dele (mestrado e doutorado).
- **Rubrica escrita junto com os testes.** Os exemplos da rubrica foram generalizados para não
  repetir os erros plantados, mas o autor é o mesmo.
- **Uma execução por projeto** (duas na ecologia). Falta medir a variação entre execuções.
- **Só Markdown.** O caminho de PDF e DOCX (MarkItDown com `-o`, leitura nativa de PDF escaneado)
  não foi exercitado.
- **Portão humano** testado só com confirmação. Falta testar o caso em que a pessoa corrige o mapa.

## Como repetir

Ver a seção "Testes" do [README](../README.md). Registre aqui cada nova execução com a data, a
versão do plugin, o placar e o que mudou.
