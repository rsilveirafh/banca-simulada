# Banca simulada: Qualidade do sono e controle glicêmico em adolescentes com diabetes mellitus tipo 1 atendidos em um ambulatório de referência

> Gerado por /banca:revisar em 2026-10-28. Revisão, não redação: aponta e sugere, não reescreve.
> Não substitui orientador nem banca. Verifique se o programa exige declaração de uso de IA.

## Resumo
- Comentários: 19 (4 bloqueantes, 10 importantes, 5 ajustes)
- Por eixo: coerência 4 · hipóteses 1 · metodologia 5 · aderência 1 · ética 3 · referencial 2 · ABNT 1 · viabilidade 2
- Mais urgente: C01 (regressão com 12 covariáveis para 40 adolescentes), C02 (menores sem consentimento do responsável e sem assentimento), C03 (coleta de prontuário iniciada antes do CEP)
- Insumos usados: projeto (mestrado acadêmico, 24 meses, confirmado pela candidata); ausentes: edital, ementa da Linha 3, Lattes da orientadora

## 1. Mapa do projeto (confirmado em 2026-10-28)

Texto de referência: `projeto.md` (Markdown original; sem paginação, por isso os comentários indicam só a seção).

| Elemento | Conteúdo e trecho literal |
|---|---|
| Identificação | Título: "Qualidade do sono e controle glicêmico em adolescentes com diabetes mellitus tipo 1 atendidos em um ambulatório de referência". Nível: mestrado acadêmico (confirmado). Programa: PPGSC/UFPCM. Linha declarada: "Linha 3, Políticas, Planejamento e Gestão em Saúde". Duração: "24 meses (março de 2027 a fevereiro de 2029)". |
| Pergunta de pesquisa | Seção 3: "A qualidade do sono está relacionada ao controle glicêmico de adolescentes com DM1?" |
| Objetivo geral | Seção 3: "Analisar a relação entre a qualidade do sono e o controle glicêmico em adolescentes com DM1 atendidos em ambulatório de referência." |
| Objetivos específicos | (a) descrever o sono pelo escore global e pelos componentes do PSQI; (b) "Estimar a associação entre má qualidade do sono e controle glicêmico inadequado (HbA1c igual ou maior que 7,0%)"; (c) "Comparar a qualidade do sono entre adolescentes em uso de sistema de infusão contínua de insulina e em esquema de múltiplas doses diárias"; (d) "Verificar se a HbA1c varia entre a primeira e a segunda dosagem conforme a qualidade do sono inicial." |
| Hipóteses | H1: "A má qualidade do sono causa a elevação da hemoglobina glicada (HbA1c) nos adolescentes com DM1." H2: "Adolescentes com mais de duas hipoglicemias noturnas referidas por mês têm pior qualidade do sono (escore global do PSQI mais alto) do que os demais." |
| Matriz objetivo → método → análise | (a) PSQI (5.4) → descrição (5.5). (b) PSQI + 1ª HbA1c → regressão logística com 12 covariáveis (5.5). (c) **nenhuma** (modalidade de insulinoterapia não é coletada nem analisada). (d) 1ª e 2ª HbA1c → teste t (5.5). H2: sem análise própria. HbA1c retrospectiva de prontuário: coletada, sem análise. |
| Desenho e amostra | Observacional, etapa transversal + seguimento de seis meses (5.1). Unidade: adolescente. Cálculo: 151; incluídos: 40, por conveniência (5.3). Local: Ambulatório de Endocrinologia Pediátrica do HU-UFPCM. Inclusão: 12 a 17 anos, DM1 há pelo menos um ano. |
| Análise | Desfecho: HbA1c ≥ 7,0%; exposição: PSQI > 5; 12 covariáveis simultâneas; teste t para a variação da HbA1c; R ≥ 4.4; α = 5% (5.5). PSQI em "tradução livre" (5.4). |
| Gatilhos éticos | Seres humanos; menores de 12 a 17 anos; dados de saúde, cor/raça e prontuário (sensíveis); coleta retrospectiva iniciada em agosto de 2026, antes da submissão ao CEP; dados identificados em Google Drive pessoal. Não se aplicam: indígenas, vertebrados, patrimônio genético, UC. |
| Cronograma | CEP: mês 6; qualificação: 12; recrutamento e 1ª HbA1c: 16 a 19; 2ª HbA1c: 18 a 20; análise: 20 a 22; redação: 20 a 23; defesa: 24. |
| Referências | 6 entradas; padrão predominante ABNT (5 de 6); ADA em estilo APA; "(Moura; Lins, 2021)" sem entrada. |

## 2. Comentários

### C01 · bloqueante · metodologia
- **Onde:** seção 5.5 (Análise dos dados)
- **Trecho:** "A associação entre má qualidade do sono (PSQI maior que 5) e o desfecho será estimada por regressão logística múltipla com as 12 covariáveis do Quadro 1 incluídas simultaneamente"
- **Problema:** com 40 adolescentes o modelo não se sustenta. As 12 covariáveis, somadas à exposição (PSQI) e com cor/raça em cinco categorias do IBGE, exigem cerca de 16 parâmetros além do intercepto. Na logística, o limite é dado pelo número de casos na categoria menos frequente do desfecho. Como a própria introdução diz que "grande parte dos adolescentes não a atinge" (a meta de HbA1c), o grupo com HbA1c < 7,0% deve ser pequeno, talvez uma dezena de adolescentes. Isso dá menos de um evento por parâmetro, muito abaixo das regras práticas usuais (da ordem de 10 eventos por parâmetro). O resultado provável é separação completa, estimativas instáveis e intervalos de confiança enormes. Há ainda uma contradição interna: o referencial (seção 4) pede "atenção ao número de eventos disponível para cada variável incluída no modelo", e o método ignora essa recomendação.
- **Sugestão:** estime quantos adolescentes do ambulatório têm HbA1c < 7,0% (o prontuário dá esse número, depois da aprovação do CEP) e calcule quantos parâmetros a amostra comporta. A partir daí, há três caminhos: reduzir as covariáveis a um conjunto mínimo definido antes, por um critério explícito de confusão (por exemplo, um diagrama causal); aumentar a amostra (ver C09); ou analisar a HbA1c como variável contínua. Justifique a escolha citando o próprio Hosmer, Lemeshow e Sturdivant.
- **Base:** ME2; CO4

### C02 · bloqueante · ética
- **Onde:** seção 6 (Aspectos éticos)
- **Trecho:** "Todos os participantes assinarão o Termo de Consentimento Livre e Esclarecido (TCLE) antes da aplicação dos questionários."
- **Problema:** os participantes têm de 12 a 17 anos. O projeto prevê que eles mesmos assinem o TCLE, sem mencionar o consentimento do responsável legal nem o assentimento do adolescente. Do jeito que está, a pesquisa inclui menores sem os dois registros que a resolução prevê.
- **Sugestão:** preveja dois documentos: o TCLE assinado pelo responsável legal e o Termo de Assentimento em linguagem adequada à faixa etária. Descreva também como e onde serão obtidos (a sala de espera exige que o responsável esteja presente). Confirme com o CEP do HU os modelos que ele exige.
- **Base:** ET1; Res. CNS 466/2012, item II.2; Res. CNS 466/2012, item II.23

### C03 · bloqueante · ética
- **Onde:** seção 6 (Aspectos éticos)
- **Trecho:** "Para adiantar o cronograma, a coleta dos dados retrospectivos de prontuário (HbA1c dos últimos 12 meses) já foi iniciada em agosto de 2026, antes da submissão ao CEP."
- **Problema:** consultar prontuários para pesquisa é pesquisa com seres humanos. O próprio texto declara que a coleta começou antes de o protocolo ser submetido, e o projeto ainda nem começou (março de 2027). Uma banca não aprova o projeto com essa frase, e o CEP pode recusar o uso desses dados. O motivo alegado ("adiantar o cronograma") também não se sustenta: esses dados não entram em nenhuma análise (ver C11).
- **Sugestão:** interrompa a coleta já. Leve a situação à orientadora e ao CEP e pergunte o que fazer com o que já foi registrado: descartar ou incluir no protocolo de forma regularizada. Coloque toda a coleta de prontuário no cronograma depois da aprovação. As regras específicas sobre uso de prontuário e dispensa de TCLE devem ser confirmadas com o CEP (conferir o texto vigente).
- **Base:** ET1; ET6; Res. CNS 466/2012, item VII.1; Res. CNS 466/2012, item XI.2, alínea a

### C04 · bloqueante · viabilidade
- **Onde:** seção 9 (Cronograma)
- **Trecho:** "2ª dosagem de HbA1c (seis meses após a 1ª) | 18 a 20"
- **Problema:** se a 1ª dosagem acontece nos meses 16 a 19, a 2ª, seis meses depois, cai nos meses 22 a 25, e não nos meses 18 a 20. Os adolescentes recrutados no fim do período só teriam a 2ª dosagem depois da defesa (mês 24). Além disso, a análise (meses 20 a 22) e a redação (meses 20 a 23) começam antes do fim do seguimento. Do jeito que está, o objetivo (d) não chega a tempo da defesa.
- **Sugestão:** refaça o cronograma de trás para frente a partir da defesa: última 2ª dosagem, menos seis meses, dá o fim do recrutamento. Preveja tempo para limpeza dos dados, análise e redação depois disso. Se não couber, há três opções: antecipar o recrutamento (o CEP está previsto para o mês 6, então há margem), encurtar o intervalo do seguimento ou rever o objetivo (d).
- **Base:** VC1; VC2

### C05 · importante · hipóteses
- **Onde:** seção 3 (Hipóteses)
- **Trecho:** "H1: A má qualidade do sono causa a elevação da hemoglobina glicada (HbA1c) nos adolescentes com DM1."
- **Problema:** a hipótese é causal, mas o desenho é observacional e o sono é medido uma vez só. O desenho sustenta associação, não causa. O próprio referencial (seção 4) diz que "o controle ruim pode piorar o sono [...] tanto quanto o sono ruim pode piorar o controle". Com isso, uma associação positiva seria compatível com as duas direções, e o estudo não consegue distinguir uma da outra. A hipótese central do projeto pede uma inferência que o método não entrega.
- **Sugestão:** ajuste a hipótese ao que o desenho permite (direção e forma da associação) e discuta a causalidade reversa como limitação. Se a direção temporal for essencial, o desenho precisa medir o sono antes da mudança da HbA1c e também no seguimento. Decida isso com a orientadora.
- **Base:** HI4; CO4

### C06 · importante · coerência
- **Onde:** seção 3 (Hipóteses) e seção 5.5
- **Trecho:** "H2: Adolescentes com mais de duas hipoglicemias noturnas referidas por mês têm pior qualidade do sono (escore global do PSQI mais alto) do que os demais."
- **Problema:** a variável existe ("Hipoglicemias noturnas referidas | número no último mês", Quadro 1), mas a seção 5.5 não prevê nenhum teste para H2. Ela entra só como covariável de um modelo em que o PSQI é exposição, enquanto em H2 o PSQI é o desfecho. Do jeito que está, a hipótese não seria testada.
- **Sugestão:** inclua na seção 5.5 a análise de H2: dois grupos definidos pelo ponto de corte de duas hipoglicemias, desfecho no escore global do PSQI, teste escolhido conforme a distribuição. Justifique também o ponto de corte "mais de duas". Avalie ainda se faz sentido manter as hipoglicemias como covariável em C01, já que elas podem estar no caminho entre o controle glicêmico e o sono.
- **Base:** CO2; HI1

### C07 · importante · coerência
- **Onde:** seção 3 (objetivo específico c)
- **Trecho:** "(c) Comparar a qualidade do sono entre adolescentes em uso de sistema de infusão contínua de insulina e em esquema de múltiplas doses diárias"
- **Problema:** nenhuma etapa do método atende a este objetivo. A modalidade de insulinoterapia não está no Quadro 1, não é coletada nem do prontuário nem do questionário, e a seção 5.5 não prevê comparação. Com 40 adolescentes, o grupo em bomba de insulina pode ser muito pequeno ou nem existir.
- **Sugestão:** decida se o objetivo fica. Se ficar, inclua a variável na coleta, informe quantos adolescentes do ambulatório usam sistema de infusão e preveja a análise. Se esse número for pequeno demais, retire o objetivo.
- **Base:** CO2

### C08 · importante · referencial
- **Onde:** seção 4 (Referencial teórico)
- **Trecho:** "A relação entre sono e metabolismo da glicose é sustentada por estudos experimentais em adultos, que mostram redução da sensibilidade à insulina após restrição de sono. Em adolescentes com DM1, os estudos são quase todos transversais"
- **Problema:** as duas afirmações que sustentam o projeto aparecem sem nenhuma citação: a evidência experimental em adultos e a lacuna ("quase todos transversais"). O referencial inteiro tem 6 entradas, e só uma trata de sono em adolescentes com DM1 (e ela não está nas referências, ver C15). Não há revisões nem estudos recentes da área. Assim, a lacuna que justifica o projeto fica afirmada, mas não demonstrada.
- **Sugestão:** cite os estudos experimentais e uma revisão sobre sono e controle glicêmico em DM1 pediátrico. Mostre o que já se sabe (inclusive estudos longitudinais ou com medidas objetivas de sono, se existirem) e em que ponto exatamente este projeto acrescenta algo. A lacuna precisa sair da literatura, não da afirmação.
- **Base:** RE2; RE4; RE1

### C09 · importante · metodologia
- **Onde:** seção 5.3 (Tamanho da amostra)
- **Trecho:** "resultou em 151 participantes. Serão incluídos 40 adolescentes, número médio de atendimentos do ambulatório em dois meses, recrutados por conveniência nas consultas de rotina."
- **Problema:** o cálculo pede 151, e o projeto inclui 40 sem explicar o que muda. Com 40, a margem de erro para uma prevalência de 50% fica em torno de 15 pontos percentuais, não 8. Além disso, o cálculo serve à estimativa de prevalência (objetivo a), não à associação do objetivo (b). Há ainda inconsistências internas: se a população-alvo são os "cerca de 240 adolescentes" da seção 2, a correção para população finita muda o n do cálculo; e o recrutamento dura quatro meses no cronograma (meses 16 a 19), não dois. Por fim, a conveniência nas consultas tende a selecionar quem comparece mais, ou seja, provavelmente os adolescentes com melhor adesão, o que enviesa a prevalência e a associação.
- **Sugestão:** refaça o cálculo para o objetivo principal (a associação) e diga com que precisão ou poder o estudo conta. Use a população real de cerca de 240 adolescentes e todo o período de recrutamento. Considere a inclusão consecutiva de todos os elegíveis no período, ou uma amostra a partir da lista do ambulatório, e descreva como vai comparar quem entrou com quem não entrou.
- **Base:** ME3; ME6; ME2

### C10 · importante · metodologia
- **Onde:** seção 5.4 (Coleta de dados)
- **Trecho:** "O PSQI será aplicado na versão original em inglês, traduzida livremente pela pesquisadora para o português."
- **Problema:** existe versão brasileira validada, e o próprio projeto a cita: "a versão em português foi traduzida, adaptada e validada por Bertolazi et al. (2011)". Uma tradução livre perde a comparabilidade com outros estudos e invalida o ponto de corte "PSQI maior que 5", que é a base da exposição em C01. A banca vai perguntar por que não usar a versão que o referencial apresenta.
- **Sugestão:** use a versão validada de Bertolazi et al. e veja se é preciso autorização para o uso. Verifique também se essa validação incluiu adolescentes. Se não incluiu, discuta isso como limitação.
- **Base:** ME4; CO4

### C11 · importante · coerência
- **Onde:** seção 5.4 (Coleta de dados)
- **Trecho:** "Também serão registrados os valores de HbA1c dos 12 meses anteriores, a partir dos prontuários."
- **Problema:** esses valores não aparecem em nenhum objetivo, hipótese ou análise da seção 5.5. Coletar dado sensível de saúde sem finalidade definida enfraquece o protocolo ético. É justamente essa coleta que já foi iniciada antes do CEP (C03).
- **Sugestão:** defina o uso desses valores (por exemplo, caracterizar o controle glicêmico anterior ou ajustar a análise do objetivo d) e preveja a análise correspondente. Se não houver uso, retire a coleta.
- **Base:** CO3; ET5

### C12 · importante · metodologia
- **Onde:** seção 5.5 (Análise dos dados)
- **Trecho:** "A variação da HbA1c entre as duas dosagens será comparada entre os grupos de boa e má qualidade do sono pelo teste t para amostras independentes."
- **Problema:** a variação da HbA1c depende do valor inicial: quem começa muito alto tende a cair, por regressão à média e por ajuste de tratamento. Se o sono ruim estiver associado a uma HbA1c inicial mais alta (é a hipótese H1), o teste t sobre a diferença pode mostrar até uma "melhora" no grupo de sono ruim que não tem relação com o sono. O teste também não considera ajustes de insulina, troca de modalidade de tratamento ou perdas de seguimento entre as duas dosagens.
- **Sugestão:** considere uma análise da 2ª HbA1c ajustada pela 1ª (e por poucos fatores definidos antes) em vez do teste t na diferença. Registre as mudanças de tratamento no período. Diga quantos adolescentes por grupo você espera ter na 2ª dosagem.
- **Base:** ME6; ME2

### C13 · importante · ética
- **Onde:** seção 6 (Aspectos éticos)
- **Trecho:** "Os dados serão digitados em planilha no Google Drive pessoal da pesquisadora, identificados pelo nome completo e pelo número do prontuário de cada participante, para facilitar a conferência."
- **Problema:** são dados sensíveis (saúde, cor ou raça) de menores, identificados por nome e prontuário e guardados numa conta pessoal, fora do controle da instituição. Não há plano de pseudonimização nem de controle de acesso. A conferência não exige o nome completo na planilha de análise.
- **Sugestão:** separe a chave de identificação (nome e prontuário associados a um código) da planilha de análise, que deve trazer só o código. Guarde as duas em ambiente institucional e com acesso restrito. Descreva quem acessa, por quanto tempo os dados ficam guardados e como serão descartados. Consulte o encarregado de dados (DPO) da UFPCM ou do HU.
- **Base:** ET5; Lei 13.709/2018, Art. 5º, II; Lei 13.709/2018, Art. 11, II, "c"; Lei 13.709/2018, Art. 13; Lei 13.709/2018, Art. 13, § 4º

### C14 · importante · aderência
- **Onde:** seção 7 (Aderência à linha de pesquisa)
- **Trecho:** "O projeto insere-se na Linha 3 (Políticas, Planejamento e Gestão em Saúde) por abordar o diabetes, um problema de saúde pública de grande magnitude no Brasil."
- **Problema:** a justificativa é genérica e serviria para qualquer projeto sobre diabetes, em qualquer linha. O projeto é um estudo clínico-epidemiológico de associação: não estuda política, planejamento nem gestão. O único ponto de contato com gestão (a nota técnica para incluir o PSQI na rotina) não é avaliado pelo método (ver C18). Sem a ementa da linha, não dá para dizer se ela acolhe estudos desse tipo. A banca vai perguntar.
- **Sugestão:** leia a ementa da Linha 3 e as linhas do PPGSC. Se o projeto ficar na Linha 3, mostre com argumento de conteúdo o que ele produz para o planejamento ou a gestão do serviço. Se outra linha (por exemplo, de epidemiologia) acolher melhor o projeto, discuta a mudança com a orientadora.
- **Base:** AD1

### C15 · ajuste · referencial
- **Onde:** seção 1 (Introdução)
- **Trecho:** "No Brasil, estudo em ambulatório universitário encontrou má qualidade do sono em cerca de metade dos adolescentes com DM1 (Moura; Lins, 2021)."
- **Problema:** Moura e Lins (2021) é citado sem entrada nas referências. É o único estudo sobre o tema central e também fundamenta a prevalência de 50% usada no cálculo amostral (5.3), o que aumenta o peso da falta. As demais citações batem com a lista, e toda entrada da lista é citada.
- **Sugestão:** inclua a entrada completa na lista e cite o estudo também na seção 5.3, como fonte da prevalência esperada.
- **Base:** RE3

### C16 · ajuste · viabilidade
- **Onde:** seção 5.4 (Coleta de dados)
- **Trecho:** "e na consulta de seguimento, seis meses após a primeira (segunda dosagem)"
- **Problema:** o projeto não prevê perdas no seguimento nem o que fazer se a consulta não cair exatamente seis meses depois. Adolescentes faltam a consultas, mudam de serviço ou passam para o atendimento adulto (quem tem 17 anos na entrada). Com 40 participantes, poucas perdas já esvaziam a comparação do objetivo (d). O comentário é um ajuste porque o risco é previsível e se resolve com uma janela de tolerância e um plano de contato. Ele se soma a C04 e C12.
- **Sugestão:** defina uma janela aceitável para a 2ª dosagem, estime a perda esperada (o prontuário mostra a frequência de retorno) e descreva como os adolescentes serão contatados e como as perdas entram na análise.
- **Base:** VC5; ME6

### C17 · ajuste · metodologia
- **Onde:** seção 5.4 (Quadro 1)
- **Trecho:** "Sintomas depressivos referidos | sim; não"
- **Problema:** o quadro não diz como se mede esta variável nem outras parecidas (uso de telas, atividade física em minutos por semana): não há pergunta, instrumento nem período de referência. Para sintomas depressivos, uma resposta "sim/não" sem instrumento tende a classificar mal. Faltam também os critérios operacionais de "acompanhamento regular" e de "asma grave" (seção 5.2).
- **Sugestão:** para cada variável do Quadro 1, informe a fonte (prontuário ou questionário) e a pergunta ou o instrumento usado. Para sintomas depressivos e atividade física, considere instrumentos validados para adolescentes. Defina os critérios de inclusão e exclusão de forma que outra pessoa consiga aplicá-los.
- **Base:** ME4; ME5

### C18 · ajuste · coerência
- **Onde:** seção 8 (Resultados esperados)
- **Trecho:** "produzir uma nota técnica para a equipe do ambulatório, propondo a inclusão do PSQI na consulta de rotina"
- **Problema:** um estudo de associação num único serviço, com 40 adolescentes, não avalia se rastrear o sono na consulta melhora o controle glicêmico. A recomendação vai além do que o desenho permite. Classifiquei como ajuste, e não como importante, porque o produto pode ser mantido se o texto deixar claro que é uma proposta a ser avaliada, e não um resultado do estudo.
- **Sugestão:** ajuste o alcance da nota técnica ao que o estudo vai de fato mostrar (frequência do problema e associação observada), indicando o que ainda precisaria ser avaliado antes de adotar a medida na rotina.
- **Base:** CO5

### C19 · ajuste · ABNT
- **Onde:** Referências
- **Trecho:** "American Diabetes Association. (2024). Standards of Care in Diabetes—2024. Diabetes Care, 47(Supplement 1)."
- **Problema:** esta entrada está em estilo APA (ano entre parênteses depois do autor, sem destaque no título do periódico), enquanto as outras cinco seguem o padrão ABNT. Faltam também as páginas.
- **Sugestão:** padronize esta entrada no mesmo formato das demais e complete os elementos que faltam. Confira a edição da NBR 6023 exigida pelo programa (conferir o texto vigente).
- **Base:** AB1; AB2

## 3. Arguição provável
1. **Com 40 adolescentes, quantos devem ter HbA1c abaixo de 7,0%, e quantos parâmetros o seu modelo logístico comporta?** (C01, C09). Como se preparar: tenha a estimativa da distribuição da HbA1c no ambulatório e saiba calcular eventos por parâmetro. Decida antes quais covariáveis ficam e por qual critério.
2. **Por que traduzir o PSQI se você mesma cita a versão validada de Bertolazi et al.?** (C10). Como se preparar: leia a validação brasileira (amostra, consistência interna, ponto de corte) e saiba se ela inclui adolescentes.
3. **O seu desenho permite dizer que o sono "causa" a elevação da HbA1c? E a causalidade reversa que o seu próprio referencial descreve?** (C05, C08). Como se preparar: entenda a diferença entre associação e causalidade neste desenho e saiba o que um seguimento precisaria medir para dizer algo sobre a direção.
4. **Com que autorização os prontuários foram consultados em agosto de 2026, e o que será feito com esses dados?** (C03, C11). Como se preparar: converse com a orientadora e o CEP antes da arguição e leve a decisão tomada.
5. **Quem consente pelos adolescentes, e como será o assentimento deles na sala de espera?** (C02). Como se preparar: tenha os dois termos previstos e saiba descrever o procedimento de obtenção.
6. **Como H2 será testada, e por que o corte em "mais de duas" hipoglicemias?** (C06). Como se preparar: defina o teste, o desfecho e a origem do ponto de corte.
7. **Quantos adolescentes do ambulatório usam bomba de insulina? De onde vem esse dado no seu método?** (C07). Como se preparar: levante o número no serviço e decida se o objetivo (c) continua.
8. **Se a última 1ª dosagem for no mês 19, quando sai a 2ª? E a defesa?** (C04, C16). Como se preparar: refaça o cronograma mês a mês e saiba dizer qual etapa você corta ou antecipa.
9. **Por que um teste t na variação da HbA1c, sem considerar o valor inicial?** (C12). Como se preparar: entenda regressão à média e as alternativas de análise ajustada pela medida basal.
10. **O cálculo deu 151 e você inclui 40. Que precisão sobra, e o que justifica a conveniência num serviço com 240 adolescentes?** (C09). Como se preparar: tenha a margem de erro com n = 40 e uma alternativa de recrutamento que reduza o viés de seleção.
11. **Onde ficarão os dados identificados, e quem tem acesso a eles?** (C13). Como se preparar: tenha um plano de pseudonimização e de guarda institucional, validado com o DPO.
12. **O que este projeto tem de política, planejamento ou gestão em saúde?** (C14, C18). Como se preparar: leia a ementa da Linha 3 e saiba apontar o que o estudo produz para a gestão do serviço, ou por que outra linha seria mais adequada.
13. **A orientadora tem produção sobre sono, diabetes ou saúde do adolescente?** (C14). Como se preparar: não avaliei esse ponto, porque o Lattes não foi fornecido. Saiba situar o projeto na produção e nos projetos da orientadora.
14. **Quais estudos sustentam que a literatura em adolescentes com DM1 é "quase toda transversal"? Existem coortes?** (C08, C15). Como se preparar: faça uma busca sistemática curta e conheça os principais estudos, inclusive o de Moura e Lins.

## 4. Preparação para a entrevista
- Saber de cor: n previsto, n do cálculo, número esperado de adolescentes com HbA1c < 7,0% no ambulatório, número de parâmetros do modelo e margem de erro com n = 40.
- Ter decidido, com a orientadora, o que fazer com os dados de prontuário já coletados e como o CEP foi ou será informado.
- Levar o cronograma refeito, com a 2ª dosagem calculada a partir da 1ª e a defesa no mês 24.
- Conhecer a validação brasileira do PSQI (componentes, ponto de corte, população validada).
- Ter lido a ementa da Linha 3 e ter uma resposta curta sobre a aderência à linha e à orientadora.
- Conhecer de 5 a 10 estudos recentes sobre sono e controle glicêmico em adolescentes com DM1, e saber quais são longitudinais.

## 5. Registro da autochecagem
- Trechos conferidos: 19; corrigidos: 0; comentários apagados por trecho inexistente: 0.
