# Rubrica da banca simulada

Oito eixos, cada um com perguntas objetivas. Cada pergunta tem um código (ex.: `HI2`) que vai na
linha **Base** do comentário. Responda **todas** as perguntas de um eixo antes de passar ao próximo.
Uma pergunta só vira comentário quando há problema **e** um trecho do projeto que o mostre (ou a
seção onde o item deveria estar).

## Gravidade

| Gravidade | Critério | Teste rápido |
|---|---|---|
| **bloqueante** | Sem correção, o projeto não pode ser aprovado ou executado como está, ou a conclusão prometida não se sustenta. | "A banca reprovaria ou exigiria reformulação antes de seguir?" |
| **importante** | Compromete uma parte do projeto ou a credibilidade dele; a banca vai cobrar com certeza; resolve-se revendo uma seção. | "Vai virar pergunta dura na arguição?" |
| **ajuste** | Forma, clareza, normalização, consistência. Não afeta a validade. | "Um parecer listaria isso no fim, em 'pequenas correções'?" |

Regras de desempate:
- Problema ético-legal que impede a coleta (falta de CEP, CEUA, SISBIO, coleta antes da
  aprovação) é **bloqueante**.
- Problema que afeta o objetivo geral ou a hipótese central é, no mínimo, **importante**.
- Na dúvida entre duas gravidades, escolha a menor e diga por quê no comentário.

---

## CO · Coerência interna
O projeto conta uma história só: título → problema → pergunta → objetivos → hipóteses → método →
resultados esperados.

| Código | Pergunta |
|---|---|
| CO1 | O título, a pergunta e o objetivo geral tratam do mesmo recorte (mesmo grupo, variável, lugar e escala)? |
| CO2 | **Cada objetivo específico tem pelo menos uma etapa de método e um produto (dado, análise, resultado)?** Faça a matriz objetivo → método → análise. |
| CO3 | Há etapa de método ou análise que não serve a nenhum objetivo? |
| CO4 | O método contradiz alguma crítica ou limitação que o próprio projeto apresenta no referencial ou na justificativa? |
| CO5 | Os resultados esperados decorrem do método (e não prometem mais do que o desenho permite)? |
| CO6 | Termos centrais são usados com o mesmo sentido do começo ao fim? |

- Bloqueante: o objetivo geral pede algo que nenhuma etapa do método produz.
- Importante: um objetivo específico sem etapa de método; método que contradiz a crítica que o
  próprio projeto faz a outros estudos.
- Ajuste: título com termo que não reaparece no texto; sinônimos trocados para o mesmo conceito.

## HI · Hipóteses e pergunta
| Código | Pergunta |
|---|---|
| HI1 | A pergunta de pesquisa está explícita e é respondível com os dados previstos? |
| HI2 | **Cada hipótese diz o que a refutaria?** Há algum resultado possível que a contrarie? (Hipótese que acomoda qualquer resultado não é testável.) |
| HI3 | A hipótese faz uma previsão com direção ou forma (aumenta, diminui, difere de, se associa a) ligada a uma variável medida no método? |
| HI4 | O tipo de inferência da hipótese cabe no desenho? (causalidade exige desenho experimental ou quase-experimental; estudo transversal sustenta associação) |
| HI5 | Se o projeto é descritivo ou exploratório e não precisa de hipótese, isso está dito e justificado? |

- Bloqueante: hipótese central que nenhum resultado poderia refutar.
- Importante: hipótese causal num desenho que só sustenta associação; hipótese sem variável medida.
- Ajuste: hipótese nula e alternativa redigidas de forma redundante.

## ME · Metodologia e análise
| Código | Pergunta |
|---|---|
| ME1 | A unidade amostral está definida e as réplicas são independentes? (qual é o n de verdade: a parcela, o sítio, o indivíduo? Há pseudorreplicação?) |
| ME2 | **O tamanho da amostra comporta a análise proposta?** (número de níveis do efeito aleatório, eventos por variável na regressão, preditores vs n, poder) |
| ME3 | O cálculo ou a justificativa do tamanho amostral existe e é coerente com a amostra que será de fato coletada? |
| ME4 | Instrumentos, protocolos e medidas são válidos para a população e o idioma (escala validada, calibração, esforço padronizado)? |
| ME5 | Variáveis, critérios de inclusão/exclusão e procedimentos estão descritos com detalhe para alguém repetir? |
| ME6 | Vieses previsíveis (seleção, detecção, confusão, efeito do observador) foram reconhecidos e tratados? |

- Bloqueante: análise que não se sustenta com a amostra (ex.: variância de efeito aleatório
  estimada com pouquíssimos níveis; modelo com mais parâmetros do que os dados comportam).
- Importante: pseudorreplicação; instrumento não validado quando existe versão validada; cálculo
  amostral que não bate com a amostra prevista.
- Ajuste: software ou versão não informados; unidade de medida faltando.

## AD · Aderência ao programa, à linha e ao orientador
| Código | Pergunta |
|---|---|
| AD1 | O projeto declara a linha de pesquisa e justifica a inserção nela com argumento de conteúdo (não só de grupo taxonômico ou de tema genérico)? |
| AD2 | Se a ementa da linha foi fornecida: o objeto, o método ou a pergunta do projeto aparecem na ementa? |
| AD3 | Se o edital foi fornecido: o projeto respeita estrutura, limite de páginas e itens obrigatórios? |
| AD4 | Se o Lattes do orientador foi colado: há produção ou projeto do orientador no tema/método? **Sem o texto colado, não avalie: transforme em pergunta.** |

- Bloqueante: projeto fora do escopo do programa (ex.: área de outra grande área) ou que descumpre
  item eliminatório do edital.
- Importante: justificativa de aderência genérica, que serviria para qualquer projeto.
- Ajuste: linha citada com nome diferente do oficial.

## ET · Ética e regulação
Use **só** `referencias/normas.md`. Primeiro detecte; depois aponte.

| Código | Pergunta |
|---|---|
| ET1 | Há **seres humanos** (entrevista, questionário, prontuário, amostra biológica, imagem)? Então: CEP/CONEP (Res. 466/2012; 510/2016 para ciências humanas e sociais), TCLE, e assentimento se houver menores ou incapazes. |
| ET2 | Há **povos indígenas**? Então: Res. 304/2000 (anuência da comunidade, CONEP). |
| ET3 | Há **vertebrados** capturados, manipulados, marcados, coletados ou eutanasiados? Então: CEUA (Lei 11.794/2008) e, para fauna silvestre in situ, SISBIO (Portaria ICMBio 748/2022). |
| ET4 | Há **patrimônio genético** (tecido, DNA, extrato) com pesquisa, sequenciamento ou remessa ao exterior? Então: cadastro no SisGen (Lei 13.123/2015, Art. 12; Decreto 8.772/2016). |
| ET5 | Há **dados pessoais** ou sensíveis (saúde, etnia, prontuário)? Então: plano de anonimização ou pseudonimização, guarda institucional (LGPD, Art. 7º, 11 e 13). |
| ET6 | O cronograma põe a coleta **depois** da aprovação/autorização e com folga para a tramitação? |

- Bloqueante: aprovação necessária ausente ou declarada dispensada sem base; coleta prevista ou
  iniciada antes da aprovação; menores sem consentimento do responsável e sem assentimento.
- Importante: SisGen ausente quando há sequenciamento ou remessa; dado identificável guardado
  fora da instituição, sem pseudonimização.
- Ajuste: número do parecer ou da autorização a incluir quando já existe.

## RE · Referencial teórico e citações
| Código | Pergunta |
|---|---|
| RE1 | O referencial sustenta a pergunta e a hipótese (e não só o tema em geral)? |
| RE2 | O estado da arte mostra a lacuna que o projeto preenche, com estudos recentes da área? |
| RE3 | **Toda citação no texto tem entrada nas referências** (mesmo autor, mesmo ano)? E toda referência é citada? |
| RE4 | Afirmações fortes ("é consenso", "nenhum estudo") têm citação? |
| RE5 | Há citação de fonte secundária ("apud") onde a primária é acessível, ou dependência de uma só fonte? |

Nunca diga que uma referência "não existe". Diga "citado sem entrada nas referências"
(checável) ou "não consegui confirmar esta referência".

- Bloqueante: raro; só quando a lacuna que justifica o projeto não existe segundo o próprio texto.
- Importante: lacuna afirmada sem citação; referencial que não toca a hipótese.
- Ajuste: citação sem entrada nas referências; ano divergente entre texto e lista.

## AB · Normalização (ABNT)
Ver a seção 5 de `referencias/normas.md`: o texto das NBR não foi conferido, então só se aponta o
que é checável dentro do próprio projeto.

| Código | Pergunta |
|---|---|
| AB1 | A lista de referências segue um padrão único? Alguma entrada está em outro estilo (Vancouver, APA)? |
| AB2 | Cada entrada tem os elementos essenciais (autor, título, ano, fonte: periódico com volume e páginas, ou editora)? |
| AB3 | O padrão das citações no texto é o mesmo em todo o documento (autor-data ou numérico, não os dois)? |
| AB4 | Se o edital exige estrutura ou elementos (resumo, cronograma, orçamento), eles estão presentes? |

- Bloqueante: nunca por normalização, exceto item eliminatório do edital.
- Importante: lista de referências inteira fora de qualquer padrão.
- Ajuste: uma entrada fora do padrão; elemento faltando numa entrada.

## VC · Viabilidade, cronograma e orçamento
| Código | Pergunta |
|---|---|
| VC1 | **O cronograma cabe no prazo do curso** (mestrado: em geral 24 meses; doutorado: 48; confirme com a pessoa) incluindo qualificação, análise, redação e defesa? |
| VC2 | As etapas respeitam a ordem lógica e os prazos internos do próprio projeto (ex.: uma etapa que depende de outra começa antes dela terminar)? |
| VC3 | Há folga para tramitação de CEP, CEUA, SISBIO e SisGen antes da coleta? |
| VC4 | O esforço de campo ou de coleta é factível com a equipe, o deslocamento e o orçamento descritos? |
| VC5 | Há plano B para o risco principal (estação seca, baixa adesão, equipamento)? |

- Bloqueante: etapa impossível no tempo previsto ou que termina depois da defesa.
- Importante: cronograma apertado sem folga para tramitação ética; orçamento que não cobre o campo.
- Ajuste: cronograma sem a qualificação ou sem a entrega do relatório parcial.
