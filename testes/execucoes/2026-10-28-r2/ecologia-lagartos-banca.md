# Banca simulada: Efeito do tamanho dos fragmentos florestais sobre a riqueza e a abundância de lagartos de serrapilheira na Mata Atlântica do sul da Bahia

> Gerado por /banca:revisar em 2026-10-28. Revisão, não redação: aponta e sugere, não reescreve.
> Não substitui orientador nem banca. Verifique se o programa exige declaração de uso de IA.

## Resumo
- Comentários: 20 (5 bloqueantes, 12 importantes, 3 ajustes)
- Por eixo: coerência 4 · hipóteses 1 · metodologia 5 · aderência 1 · ética 3 · referencial 3 · ABNT 1 · viabilidade 2
- Mais urgente: C01 (H1 não pode ser refutada), C02 (modelo com mais parâmetros do que 4 fragmentos comportam), C03 (CEUA declarada dispensada com captura e eutanásia de vertebrados)
- Insumos usados: projeto; ausentes: edital, ementa da linha, Lattes do orientador

## 1. Mapa do projeto (confirmado em 2026-10-28)

Mestrado acadêmico, prazo de 24 meses (confirmado pela pessoa). Sem edital, ementa e Lattes.

| Elemento | Conteúdo |
|---|---|
| Identificação | "Efeito do tamanho dos fragmentos florestais sobre a riqueza e a abundância de lagartos de serrapilheira na Mata Atlântica do sul da Bahia"; mestrado; PPGBC/UESM; "Linha 2, Sistemática e Evolução de Vertebrados"; 24 meses (mar/2027 a fev/2029) |
| Pergunta | "O tamanho dos fragmentos florestais afeta a riqueza e a abundância de lagartos de serrapilheira no sul da Bahia?" (seção 3) |
| Objetivo geral | "Avaliar o efeito do tamanho dos fragmentos florestais sobre a riqueza e a abundância de lagartos de serrapilheira em remanescentes de Mata Atlântica no sul da Bahia." |
| Objetivos específicos | (a) inventário em quatro fragmentos; (b) comparar riqueza e abundância entre pequenos e grandes; (c) relacionar abundância com dossel e serrapilheira; (d) dieta por conteúdo estomacal; (e) sequências COI |
| Hipóteses | H1: fragmentação "podendo aumentar ou diminuir a riqueza e a abundância"; H2: especialistas de interior menos abundantes em fragmentos < 50 ha do que em > 300 ha |
| Matriz objetivo → método → análise | (a) armadilhas de queda (5.2) → lista → rarefação/Chao 1 (5.4); (b) armadilhas (5.2) → contagens → rarefação/Chao 1 e GLMM (5.4); (c) dossel e serrapilheira por linha, trimestral (5.3) → GLMM (5.4); (d) **nenhuma**; (e) tecido enviado a Lisboa (5.2) → sequências; análise: nenhuma |
| Desenho e amostra | Observacional; 4 fragmentos (38, 45, 320, 410 ha); 4 linhas × 10 baldes por fragmento = 160 baldes; 12 campanhas mensais de 10 dias; só armadilha de queda. Unidade declarada: balde. Unidade real do efeito de tamanho: fragmento (2 por classe) |
| Análise | Rarefação por indivíduos, Chao 1; GLMM Poisson com área, isolamento, distância da borda, dossel, serrapilheira, interações da área com as demais, fragmento aleatório; AICc; R ≥ 4.4 |
| Gatilhos éticos | Vertebrados: captura, coleta e eutanásia (até 5 ind./espécie); patrimônio genético: tecido, sequenciamento e remessa ao exterior (Lisboa); propriedades rurais. Sem seres humanos, sem UC citada. CEUA declarada dispensada (seção 6) |
| Cronograma | SISBIO no mês 4; campo meses 2 a 13; qualificação mês 12; sequenciamento e análise 14 a 20; redação 18 a 26; defesa 24. Sem CEUA nem SisGen |
| Referências | 6 entradas; 5 em ABNT, 1 em Vancouver (Haddad); Silva et al. (2019) citado sem entrada |

## 2. Comentários

### C01 · bloqueante · hipóteses
- **Onde:** seção 3 (Pergunta, hipóteses e objetivos)
- **Trecho:** "H1: A fragmentação florestal influencia a comunidade de lagartos de serrapilheira, podendo aumentar ou diminuir a riqueza e a abundância de acordo com as condições locais de cada fragmento."
- **Problema:** H1 aceita qualquer resultado: aumento, diminuição e (por "condições locais") até ausência de padrão. Não há resultado que a refute, e é justamente ela que corresponde à pergunta e ao objetivo geral (riqueza e abundância). H2, ao contrário, tem direção, limiares de área e uma variável medida; é testável.
- **Sugestão:** dar a H1 uma direção (ou forma) para riqueza e para abundância, ligada à variável que o método mede (área do fragmento), e dizer qual resultado a contrariaria. Se a intenção for exploratória, declarar isso e justificar.
- **Base:** HI2, HI3

### C02 · bloqueante · metodologia
- **Onde:** seção 5.4 (Análise dos dados)
- **Trecho:** "incluindo como efeitos fixos a área do fragmento, o isolamento, a distância da borda, a cobertura de dossel e a profundidade da serrapilheira, além das interações entre a área e as demais variáveis, e o fragmento como efeito aleatório"
- **Problema:** o modelo completo tem intercepto, 5 efeitos principais e 4 interações, mais a variância do fragmento. Área e isolamento só variam entre fragmentos, e há apenas 4 fragmentos: intercepto, área, isolamento e área × isolamento já consomem os 4 valores, sem sobrar informação para estimar a variância do efeito aleatório. Uma variância estimada com 4 níveis é instável de qualquer forma, e o tamanho do fragmento fica confundido com a identidade de cada fragmento (2 pequenos contra 2 grandes). A conclusão sobre "efeito do tamanho" não se sustenta com esse modelo.
- **Sugestão:** contar os graus de liberdade no nível do fragmento e reduzir o modelo ao que 4 fragmentos comportam; separar o que é testado no nível do fragmento (área) do que é testado no nível da linha ou do balde (borda, dossel, serrapilheira). Discutir com o orientador se é possível aumentar o número de fragmentos, mesmo com menos esforço por fragmento. Conferir em Bolker et al. (2009) o que o guia diz sobre poucos níveis de efeito aleatório e sobre sobredispersão em modelos Poisson.
- **Base:** ME2, ME1

### C03 · bloqueante · ética
- **Onde:** seção 6 (Aspectos éticos e legais)
- **Trecho:** "Por se tratar de estudo observacional de campo, sem experimentação em laboratório, o projeto dispensa avaliação pela Comissão de Ética no Uso de Animais (CEUA)."
- **Problema:** o método captura, manipula, mede, pesa, coleta e eutanasia lagartos (seção 5.2), ou seja, vertebrados em atividade de pesquisa. A lei que rege o uso científico de animais não faz exceção para estudo "de campo" ou "observacional", e a autorização do SISBIO não substitui a CEUA. O método de eutanásia também não está descrito.
- **Sugestão:** prever a submissão do protocolo à CEUA da UESM antes de qualquer captura, descrever o método de eutanásia e o manejo dos animais capturados, e consultar a CEUA sobre as resoluções do CONCEA para estudos de campo e eutanásia (conferir o texto vigente). Retirar a frase que declara a dispensa.
- **Base:** ET3; Lei 11.794/2008, Art. 1º, Art. 2º e Art. 23, I; Portaria ICMBio 748/2022, Art. 60

### C04 · bloqueante · ética
- **Onde:** seção 9 (Cronograma)
- **Trecho:** "Campanhas de campo (12 campanhas mensais) | 2 a 13"
- **Problema:** o campo começa no mês 2, e a autorização do SISBIO só será pedida no mês 4 ("Solicitação de autorização no SISBIO | 4"). As três primeiras campanhas seriam coleta e captura sem autorização. Mesmo pedindo no mês 1, o prazo de emissão do SISBIO e a aprovação da CEUA (C03) não cabem antes do mês 2. A autorização também precisa de revalidação anual com relatório, e o campo dura 12 meses.
- **Sugestão:** pôr a submissão à CEUA e ao SISBIO no início, com folga para a tramitação, e só então começar as campanhas; refazer o cronograma a partir da nova data de início do campo (ver C05). Incluir no cronograma o relatório anual do SISBIO.
- **Base:** ET6, VC3; Portaria ICMBio 748/2022, Art. 1º, § 1º, I e II; Art. 30; Art. 31

### C05 · bloqueante · viabilidade
- **Onde:** seção 9 (Cronograma)
- **Trecho:** "Redação da dissertação | 18 a 26"
- **Problema:** a defesa está no mês 24 e a redação vai até o mês 26: a dissertação termina depois da defesa e passa do prazo de 24 meses do curso. Além disso, a qualificação (mês 12) acontece antes de terminar o campo (mês 13) e antes de qualquer análise (meses 14 a 20). Se o campo for adiado até sair a autorização (C04), as 12 campanhas mensais empurram tudo mais alguns meses.
- **Sugestão:** recalcular o cronograma de trás para a frente a partir da defesa no mês 24, com o início real do campo depois das autorizações; decidir o que a qualificação vai apresentar e se o número ou a duração das campanhas cabe no prazo.
- **Base:** VC1, VC2

### C06 · importante · referencial
- **Onde:** seção 2 (Justificativa)
- **Trecho:** "Ainda são poucos os estudos sobre o efeito do tamanho dos fragmentos sobre lagartos na porção baiana da Mata Atlântica, e a maior parte dos inventários da região foi feita em unidades de conservação grandes."
- **Problema:** a lacuna que justifica o projeto está afirmada sem nenhuma citação. O referencial não traz estudos com lagartos ou herpetofauna de serrapilheira em fragmentos de Mata Atlântica (nem da Bahia, nem de outras regiões), e a referência mais recente da lista é de 2015.
- **Sugestão:** levantar e citar os estudos sobre herpetofauna de serrapilheira e fragmentação na Mata Atlântica, sobretudo os recentes e os do sul da Bahia, e mostrar com eles o que ainda não se sabe.
- **Base:** RE2, RE4, RE1

### C07 · importante · coerência
- **Onde:** seção 3 (objetivos específicos)
- **Trecho:** "(d) Caracterizar a dieta das espécies mais abundantes por meio da análise do conteúdo estomacal;"
- **Problema:** nenhuma etapa do método nem da análise trata de dieta. Os indivíduos capturados são soltos, e só até cinco por espécie são coletados, então não está claro de onde viriam os estômagos nem com que n. O objetivo também não se liga à pergunta sobre tamanho dos fragmentos.
- **Sugestão:** ou descrever a obtenção do conteúdo estomacal, a identificação das presas, o n por espécie e a análise (e o impacto disso na CEUA, C03), ou retirar o objetivo.
- **Base:** CO2, CO1

### C08 · importante · coerência
- **Onde:** seção 3 (objetivos específicos)
- **Trecho:** "(e) Gerar sequências de DNA (código de barras, gene COI) das espécies registradas."
- **Problema:** o método prevê só a coleta e o envio do tecido; não há tratamento das sequências (edição, alinhamento, comparação com bancos, delimitação de espécies), nem papel delas na resposta à pergunta sobre tamanho dos fragmentos. O objetivo depende inteiramente de um laboratório no exterior, sem plano alternativo.
- **Sugestão:** dizer para que as sequências servem na dissertação (confirmar identificações? compor biblioteca de referência?) e como serão analisadas, ou tratá-las como produto secundário fora dos objetivos. Prever o que acontece se o laboratório parceiro não entregar.
- **Base:** CO1, CO2, CO5, VC5

### C09 · importante · coerência
- **Onde:** seção 4 (Referencial teórico)
- **Trecho:** "comparações entre fragmentos precisam controlar a quantidade de habitat na paisagem do entorno"
- **Problema:** o próprio projeto apresenta essa crítica (Fahrig, 2003), mas o método mede só área, isolamento e distância da borda; a quantidade de floresta (e de cabruca) no entorno de cada fragmento não é medida. Além disso, o título e o objetivo falam em "tamanho" e a H1 fala em "fragmentação", que a introdução diz ser preciso separar da perda de habitat.
- **Sugestão:** medir a cobertura de habitat no entorno dos fragmentos (em um raio definido) ou explicar por que não é necessário; usar um único termo ("tamanho do fragmento") em hipóteses, objetivos e resultados.
- **Base:** CO4, CO6

### C10 · importante · metodologia
- **Onde:** seção 5.2 (Amostragem de lagartos)
- **Trecho:** "As armadilhas de queda serão o único método de amostragem, para garantir o mesmo esforço em todos os fragmentos."
- **Problema:** o referencial afirma que amostragens só com armadilhas de queda "subestimam espécies arborícolas, de grande porte ou que evitam as armadilhas, o que compromete estimativas de riqueza total" (Cechin; Martins, 2000), e mesmo assim o método usa só elas e os resultados esperados prometem "a lista completa das espécies". O gênero *Enyalius*, citado na introdução como típico de interior, tem hábito em parte arborícola. Padronizar o esforço não exige método único: a busca ativa por tempo também pode ser padronizada.
- **Sugestão:** ou incluir um segundo método padronizado, ou reduzir o que se promete (riqueza amostrada por armadilha de queda, não lista completa) e discutir o viés de detecção entre espécies.
- **Base:** CO4, CO5, ME6

### C11 · importante · metodologia
- **Onde:** seção 5.2 (Amostragem de lagartos)
- **Trecho:** "Os indivíduos capturados serão identificados, medidos (comprimento rostro-cloacal, em mm), pesados e soltos no local da captura."
- **Problema:** sem marcação, um mesmo indivíduo recapturado ao longo dos 10 dias e das 12 campanhas entra de novo na contagem. A abundância passa a ser número de capturas, não de indivíduos, e as contagens deixam de ser independentes, o que afeta a rarefação por indivíduos, o Chao 1 e o GLMM.
- **Sugestão:** definir se a variável é captura ou indivíduo; se for indivíduo, prever marcação (o que entra no pedido ao SISBIO e à CEUA) ou justificar por que a recaptura é desprezível.
- **Base:** ME6, ME5

### C12 · importante · ética
- **Onde:** seção 5.2 (Amostragem de lagartos)
- **Trecho:** "As amostras de tecido serão enviadas ao laboratório parceiro na Universidade de Lisboa (Portugal), que fará a extração de DNA e o sequenciamento do gene COI, sem custo para o projeto."
- **Problema:** extração e sequenciamento de DNA de fauna brasileira é acesso ao patrimônio genético, e o envio de tecido ao exterior é remessa. As duas atividades precisam de cadastro no SisGen, feito antes da remessa e antes da divulgação dos resultados (o depósito no GenBank e no BOLD, prometido na seção 8, é divulgação). O SisGen não aparece nem no texto nem no cronograma.
- **Sugestão:** prever o cadastro de acesso e de remessa no SisGen antes do envio, com a documentação de transferência de material exigida (conferir o texto vigente), e pôr essa etapa no cronograma antes do sequenciamento. Confirmar com a pró-reitoria de pesquisa da UESM quem faz o cadastro.
- **Base:** ET4; Lei 13.123/2015, Art. 12 e Art. 12, § 2º; Decreto 8.772/2016, Art. 22 e Art. 25

### C13 · importante · metodologia
- **Onde:** seção 5.3 (Variáveis do habitat)
- **Trecho:** "Em cada linha de armadilhas, uma vez por trimestre, serão medidas a cobertura de dossel (densiômetro esférico, quatro leituras em cada um de cinco pontos) e a profundidade da serrapilheira"
- **Problema:** dossel e serrapilheira são medidos por linha (16 linhas) e por trimestre, mas a análise é feita por balde e por campanha mensal (seção 5.4). Não está dito como os valores trimestrais por linha serão associados às contagens mensais por balde, e o objetivo (c) acaba tendo, na prática, 16 unidades de habitat.
- **Sugestão:** alinhar a escala das medidas de habitat com a unidade de análise (medir por balde, ou analisar por linha) e explicar como meses sem medição são tratados.
- **Base:** ME5, CO2

### C14 · importante · metodologia
- **Onde:** seção 5.4 (Análise dos dados)
- **Trecho:** "Cada balde será considerado uma unidade amostral independente, o que resulta em 160 unidades amostrais por campanha e garante poder estatístico às comparações."
- **Problema:** baldes da mesma linha são ligados pela mesma cerca-guia, linhas ficam no mesmo fragmento e as campanhas se repetem nos mesmos baldes. Para a comparação de tamanho, a réplica é o fragmento (2 por classe), não o balde. Tratar 160 baldes como independentes é pseudorreplicação e infla o "poder" atribuído ao estudo. O próprio referencial reconhece a "estrutura hierárquica" desses dados.
- **Sugestão:** retirar a afirmação de independência, descrever a estrutura (balde dentro de linha dentro de fragmento, campanhas repetidas) e mostrar como ela entra no modelo. Ver também C02.
- **Base:** ME1

### C15 · importante · aderência
- **Onde:** seção 7 (Aderência à linha de pesquisa)
- **Trecho:** "porque trata de lagartos, que são vertebrados, e porque o inventário contribui para o conhecimento da fauna regional."
- **Problema:** a justificativa é só taxonômica e serviria para qualquer projeto com vertebrados. A pergunta e o método são de ecologia de comunidades e de paisagem; o único elo com sistemática e evolução é o objetivo (e), que não tem análise (C08). Sem a ementa da linha e o Lattes do orientador, não é possível avaliar a aderência: fica como pergunta.
- **Sugestão:** conferir a ementa da Linha 2 e verificar se existe no PPGBC uma linha de ecologia ou conservação mais adequada; se a Linha 2 for mantida, justificar com o conteúdo (pergunta, método) e não com o grupo taxonômico. Verificar a produção do orientador no tema.
- **Base:** AD1, AD4

### C16 · importante · coerência
- **Onde:** seção 8 (Resultados esperados)
- **Trecho:** "demonstrar que fragmentos pequenos têm menor riqueza e menor abundância de espécies de interior de floresta"
- **Problema:** o resultado esperado já está escrito como conclusão, e "demonstrar" um efeito do tamanho com 2 fragmentos por classe, num estudo observacional, promete mais do que o desenho permite (C02, C14).
- **Sugestão:** escrever os resultados esperados como o que será testado e o que cada resultado possível significaria, no limite do que um desenho observacional com 4 fragmentos sustenta.
- **Base:** CO5, HI4

### C17 · importante · viabilidade
- **Onde:** seção 10 (Orçamento)
- **Trecho:** "As despesas de campo serão cobertas pela bolsa da candidata e pelo projeto do orientador."
- **Problema:** o combustível cobre só a ida e volta entre a UESM e a base (cerca de 420 km por campanha), mas a vistoria diária de 160 baldes em 4 fragmentos distantes 15 a 40 km entre si, por 10 dias, exige deslocamento diário que não está orçado. Não há hospedagem, alimentação, auxiliar de campo, nem plano B para o sequenciamento. Também não está dito quantas pessoas vistoriam os baldes nem se os 4 fragmentos são amostrados nos mesmos dias. Bolsa de mestrado não é fonte de custeio de campo.
- **Sugestão:** descrever a logística diária (equipe, rota, ordem dos fragmentos) e refazer o orçamento a partir dela; indicar a fonte de recurso do projeto do orientador; prever o que fazer se faltar recurso ou equipe.
- **Base:** VC4, VC5

### C18 · ajuste · referencial
- **Onde:** seção 1 (Introdução)
- **Trecho:** "populações de espécies florestais tendem a declinar perto das bordas (Silva et al., 2019)"
- **Problema:** Silva et al. (2019) é citado sem entrada nas referências.
- **Sugestão:** incluir a entrada completa ou retirar a citação. Conferir também se as demais citações e entradas batem (hoje as outras seis batem nos dois sentidos).
- **Base:** RE3

### C19 · ajuste · referencial
- **Onde:** seção 4 (Referencial teórico)
- **Trecho:** "A teoria de biogeografia de ilhas e, depois, a ecologia de paisagens forneceram a base para prever que fragmentos menores e mais isolados abrigam menos espécies."
- **Problema:** a base teórica que sustenta a previsão central é afirmada sem citação.
- **Sugestão:** citar as obras de origem da teoria e ao menos uma revisão sobre sua aplicação a fragmentos florestais.
- **Base:** RE4

### C20 · ajuste · ABNT
- **Onde:** Referências
- **Trecho:** "Haddad NM, Brudvig LA, Clobert J, Davies KF, Gonzalez A, Holt RD, et al."
- **Problema:** esta entrada está em estilo Vancouver (iniciais sem ponto, título de periódico abreviado, sem negrito), enquanto as outras cinco seguem o padrão ABNT.
- **Sugestão:** refazer a entrada no mesmo padrão das demais e conferir a edição da NBR 6023 exigida pelo programa.
- **Base:** AB1

## 3. Arguição provável
1. **Que resultado faria você rejeitar a H1?** (C01). Como se preparar: escrever para si a direção esperada para riqueza e para abundância e o resultado que contrariaria cada uma.
2. **Qual é o seu n para testar o efeito do tamanho do fragmento?** (C02, C14). Como se preparar: saber dizer quantas réplicas independentes existem por classe de tamanho e por que 160 baldes não são 160 réplicas.
3. **Quantos parâmetros tem o seu modelo completo e quantos fragmentos você tem para estimá-los?** (C02). Como se preparar: contar os parâmetros do nível do fragmento e chegar ao modelo mínimo que os dados comportam.
4. **Por que você entendeu que não precisa de CEUA, se vai capturar e eutanasiar lagartos?** (C03). Como se preparar: conhecer o que a CEUA da UESM exige para estudos de campo e qual método de eutanásia será usado.
5. **Como as três primeiras campanhas acontecem antes de você pedir o SISBIO?** (C04, C05). Como se preparar: saber os prazos de tramitação e qual será o mês real de início do campo.
6. **Como a dissertação termina dois meses depois da defesa, e o que você apresenta na qualificação?** (C05). Como se preparar: ter um cronograma refeito, contado de trás para a frente a partir da defesa.
7. **Você cita Fahrig dizendo que é preciso controlar a quantidade de habitat no entorno. Por que o seu desenho não controla?** (C09). Como se preparar: decidir se vai medir cobertura no entorno e em que raio, ou ter o argumento para não medir.
8. **Você mesma cita que armadilha de queda subestima riqueza. Como promete a lista completa usando só armadilha?** (C10). Como se preparar: decidir entre incluir outro método padronizado ou reformular o que será entregue; saber quais espécies da região escapam das armadilhas.
9. **Como você distingue um indivíduo recapturado de um novo?** (C11). Como se preparar: decidir se a variável é captura ou indivíduo e, se for indivíduo, como marcar.
10. **De onde saem os estômagos para o objetivo (d), se os animais são soltos?** (C07). Como se preparar: decidir se mantém o objetivo; se mantiver, saber o n por espécie e o método.
11. **Para que servem as sequências de DNA na resposta à sua pergunta, e quem cadastra a remessa no SisGen?** (C08, C12). Como se preparar: definir o papel das sequências e conhecer o procedimento de cadastro de acesso e remessa na UESM.
12. **Por que este projeto está na linha de Sistemática e Evolução?** (C15). Como se preparar: ler a ementa da Linha 2 e a produção recente do orientador; ter um argumento de conteúdo, não de grupo taxonômico.
13. **Quais estudos já testaram o efeito do tamanho de fragmentos sobre lagartos na Mata Atlântica, e o que eles encontraram?** (C06, C19). Como se preparar: ter levantado e lido esses estudos, com os resultados principais.
14. **Quem vistoria 160 baldes por dia em quatro fragmentos a até 40 km um do outro, e quem paga esse deslocamento?** (C17). Como se preparar: ter a logística diária desenhada e um orçamento coerente com ela.

## 4. Preparação para a entrevista
- Saber de cor: número de fragmentos por classe (2), áreas (38, 45, 320, 410 ha), número de parâmetros do modelo e de níveis do efeito aleatório.
- Decidir antes da arguição: manter ou retirar os objetivos (d) e (e); método único ou combinado; captura ou indivíduo como variável.
- Levar o cronograma refeito com CEUA, SISBIO e SisGen antes do campo e redação terminando antes da defesa.
- Ler a ementa da Linha 2 do PPGBC e o Lattes do orientador e preparar a justificativa de aderência.
- Estudar o que diz Bolker et al. (2009) sobre efeitos aleatórios com poucos níveis e sobredispersão, e Fahrig (2003) sobre quantidade de habitat.

## 5. Registro da autochecagem
- Trechos conferidos: 20 (script `checar_trechos.py`, 20 OK na primeira execução); corrigidos: 0; comentários apagados por trecho inexistente: 0
- Conferência manual: as normas citadas (Lei 11.794/2008, Art. 1º, 2º e 23, I; Portaria ICMBio 748/2022, Art. 1º, § 1º, 30, 31 e 60; Lei 13.123/2015, Art. 12 e § 2º; Decreto 8.772/2016, Art. 22 e 25) estão em `normas.md` com o mesmo número; as 14 perguntas da arguição apontam para comentários existentes; o resumo bate com a contagem (5 + 12 + 3 = 20).
- Itens [conferir] mencionados sem detalhar: resoluções do CONCEA (C03) e documentação de transferência de material na remessa (C12).
