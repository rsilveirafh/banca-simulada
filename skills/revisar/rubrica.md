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

## Calibração por tipo de projeto

Os eixos e as perguntas são os mesmos para todos os tipos. O que muda é o **prazo de referência**,
**contra o que a aderência é medida** e o **nível de exigência**. Use a linha do tipo confirmado no
mapa. Os prazos são referências comuns; o edital, o regulamento ou a pessoa têm a palavra final.

| Tipo | Prazo de referência | Aderência medida contra | Pesa mais | Pesa menos |
|---|---|---|---|---|
| **TCC** | 6 a 12 meses | orientador e curso | viabilidade, clareza da pergunta, método descrito para repetir | originalidade; profundidade do estado da arte |
| **Iniciação científica** (PIBIC, PIBITI e afins) | 12 meses (com relatório parcial) | projeto do orientador e edital da bolsa | viabilidade, plano de trabalho do estudante ligado ao projeto do orientador | originalidade; hipóteses sofisticadas |
| **Seleção de mestrado ou doutorado** | 24 (mestrado) ou 48 meses (doutorado) | linha, ementa e edital do programa | aderência à linha, pergunta clara, viabilidade no prazo, itens eliminatórios do edital | detalhe de análise que o orientador ainda vai ajustar |
| **Qualificação** (mestrado ou doutorado) | o que resta do prazo do curso | linha e banca do programa | método e análise prontos para executar, cronograma até a defesa, ética resolvida | — |
| **Pós-doutorado** | 12 a 24 meses (conforme a bolsa) | supervisor, grupo e edital da bolsa | originalidade, independência do candidato, produtos e publicações previstos | etapas básicas de formação |
| **Edital de fomento** (CNPq, FAPs, chamadas temáticas) | o da chamada | objetivo, linhas e itens de avaliação da chamada | mérito, metas e indicadores verificáveis, equipe, orçamento coerente, impacto, itens eliminatórios | — |
| **Concurso docente** (prova de projeto) | em geral 2 a 4 anos, como primeiro projeto na instituição | área e subárea do concurso, perfil do departamento | encaixe na área, viabilidade com a estrutura disponível ou financiável, ligação com ensino, extensão e orientação, capacidade de captar recurso | detalhe operacional fino |

Regras da calibração:
- Problema no que **pesa mais** sobe um nível de gravidade quando ficar em dúvida entre dois; no que
  **pesa menos**, desce um nível ou vira pergunta da arguição.
- Em TCC e iniciação científica, não cobre originalidade de doutorado: cobre pergunta respondível,
  método executável e ética resolvida.
- No edital de fomento e no concurso, descumprir item eliminatório do edital é **bloqueante**.

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

## AD · Aderência (programa, linha, orientador, chamada ou concurso)
Use as perguntas que valem para o tipo de projeto (ver a calibração). AD5 só para edital de
fomento; AD6 só para concurso docente.

| Código | Pergunta |
|---|---|
| AD1 | O projeto declara a linha de pesquisa (ou a área do concurso, ou o tema da chamada) e justifica a inserção nela com argumento de conteúdo (não só de grupo taxonômico ou de tema genérico)? |
| AD2 | Se a ementa da linha ou a descrição da área foi fornecida: o objeto, o método ou a pergunta do projeto aparecem nela? |
| AD3 | Se o edital foi fornecido: o projeto respeita estrutura, limite de páginas e itens obrigatórios? |
| AD4 | Se o Lattes do orientador ou supervisor foi colado: há produção ou projeto dele no tema/método? **Sem o texto colado, não avalie: transforme em pergunta.** |
| AD5 | **Edital de fomento:** o projeto responde ao objetivo da chamada e aos critérios de julgamento dela (mérito, equipe, metas e indicadores, orçamento, impacto)? Cada critério tem onde ser pontuado no texto? |
| AD6 | **Concurso docente:** o projeto cabe na área e subárea do concurso, é executável com a estrutura do departamento (ou diz como financiar o que falta) e conversa com ensino, extensão e orientação? |

- Bloqueante: projeto fora do escopo do programa, da chamada ou da área do concurso, ou que
  descumpre item eliminatório do edital.
- Importante: justificativa de aderência genérica, que serviria para qualquer projeto; critério de
  julgamento da chamada sem resposta no texto.
- Ajuste: linha ou área citada com nome diferente do oficial.

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
| VC1 | **O cronograma cabe no prazo de referência do tipo de projeto** (ver a calibração; confirme com a pessoa), incluindo os marcos dele (qualificação e defesa, relatório parcial e final, prestação de contas)? |
| VC2 | As etapas respeitam a ordem lógica e os prazos internos do próprio projeto (ex.: uma etapa que depende de outra começa antes dela terminar)? |
| VC3 | Há folga para tramitação de CEP, CEUA, SISBIO e SisGen antes da coleta? |
| VC4 | O esforço de campo ou de coleta é factível com a equipe, o deslocamento e o orçamento descritos? |
| VC5 | Há plano B para o risco principal (estação seca, baixa adesão, equipamento)? |
| VC6 | **Edital de fomento:** o orçamento é coerente com as atividades, usa só itens financiáveis pela chamada e respeita o teto? |

- Bloqueante: etapa impossível no tempo previsto ou que termina depois da defesa ou do fim da
  vigência; orçamento acima do teto da chamada.
- Importante: cronograma apertado sem folga para tramitação ética; orçamento que não cobre o campo;
  item de orçamento que a chamada não financia.
- Ajuste: cronograma sem a qualificação ou sem a entrega do relatório parcial.
