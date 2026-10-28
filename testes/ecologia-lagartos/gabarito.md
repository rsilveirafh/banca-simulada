# Gabarito: projeto fictício de ecologia de campo (lagartos de serrapilheira)

Projeto: [projeto.md](projeto.md). 12 erros plantados: 4 bloqueantes, 6 importantes, 2 ajustes.

Formato lido por `testes/avaliar.py`: cada erro é um bloco `### E..`; a linha de cabeçalho traz o
tipo e a gravidade esperados; cada linha **Trecho** é uma âncora literal do projeto. Um erro conta
como recuperado quando algum comentário da banca cita trecho que coincide com uma das âncoras
(ver critério no script). **Tipos aceitos** lista outros eixos que também valem como acerto de tipo.

Erros extras que a banca pode apontar e que não são falha dela (não plantados de propósito, mas
legítimos): comparação entre fragmentos sem controlar a quantidade de habitat na paisagem (o
próprio referencial cita Fahrig, 2003); n = 2 fragmentos por classe de tamanho; DNA de
material-testemunho sem menção a número de tombo.

### E01 · hipóteses · bloqueante
- **Erro:** hipótese não falseável: qualquer resultado (aumento, redução ou nada) a confirma.
- **Trecho:** "podendo aumentar ou diminuir a riqueza e a abundância de acordo com as condições locais de cada fragmento"
- **Onde:** seção 3, H1
- **Tipos aceitos:** coerência
- **Por que é erro:** sem previsão de direção não há resultado que refute H1; a pergunta central fica sem teste.

### E02 · coerência · importante
- **Erro:** objetivo específico (d), dieta por conteúdo estomacal, sem nenhuma etapa de método nem análise.
- **Trecho:** "(d) Caracterizar a dieta das espécies mais abundantes por meio da análise do conteúdo estomacal"
- **Onde:** seção 3, objetivos específicos
- **Tipos aceitos:** metodologia
- **Por que é erro:** o método não descreve triagem de conteúdo, identificação de presas nem análise; com no máximo cinco testemunhos por espécie, nem haveria amostra.

### E03 · metodologia · bloqueante
- **Erro:** amostra incompatível com a análise: GLMM com cinco preditores fixos e interações, e fragmento como efeito aleatório, com apenas quatro fragmentos. Área e isolamento só têm quatro valores e ficam confundidos com o efeito aleatório.
- **Trecho:** "incluindo como efeitos fixos a área do fragmento, o isolamento, a distância da borda, a cobertura de dossel e a profundidade da serrapilheira, além das interações entre a área e as demais variáveis, e o fragmento como efeito aleatório"
- **Trecho:** "dois fragmentos pequenos (F1, 38 ha; F2, 45 ha) e dois grandes (F3, 320 ha; F4, 410 ha)"
- **Onde:** seção 5.4 (e 5.1)
- **Tipos aceitos:** viabilidade
- **Por que é erro:** a variância do efeito aleatório não se estima com quatro níveis, e as variáveis de nível de fragmento têm n = 4; o teste do objetivo geral não se sustenta.

### E04 · metodologia · importante
- **Erro:** pseudorreplicação: baldes dentro da mesma linha e do mesmo fragmento tratados como unidades independentes.
- **Trecho:** "Cada balde será considerado uma unidade amostral independente, o que resulta em 160 unidades amostrais por campanha e garante poder estatístico às comparações."
- **Onde:** seção 5.4
- **Tipos aceitos:** —
- **Por que é erro:** a unidade de inferência sobre tamanho de fragmento é o fragmento (n = 4); o "poder" prometido é artificial.

### E05 · coerência · importante
- **Erro:** o método (só armadilha de queda) contradiz a crítica que o próprio referencial faz, e os resultados esperados prometem riqueza total.
- **Trecho:** "As armadilhas de queda serão o único método de amostragem, para garantir o mesmo esforço em todos os fragmentos."
- **Trecho:** "amostragens baseadas apenas nelas subestimam espécies arborícolas, de grande porte ou que evitam as armadilhas, o que compromete estimativas de riqueza total"
- **Trecho:** "Espera-se obter a lista completa das espécies de lagartos de serrapilheira dos quatro fragmentos, com estimativas da riqueza total de cada um"
- **Onde:** seções 4, 5.2 e 8
- **Tipos aceitos:** metodologia, referencial
- **Por que é erro:** a banca vai perguntar por que o projeto adota o método que ele mesmo diz ser insuficiente para o que promete.

### E06 · ética · bloqueante
- **Erro:** CEUA declarada dispensada, embora haja captura, manipulação, eutanásia e coleta de vertebrados para pesquisa (Lei 11.794/2008, Art. 1º e 2º; Art. 23, I).
- **Trecho:** "Por se tratar de estudo observacional de campo, sem experimentação em laboratório, o projeto dispensa avaliação pela Comissão de Ética no Uso de Animais (CEUA)."
- **Onde:** seção 6
- **Tipos aceitos:** —
- **Por que é erro:** "observacional" não descreve um estudo com captura e eutanásia; sem CEUA a coleta não pode começar.

### E07 · ética · bloqueante
- **Erro:** coleta começa antes da autorização: campo nos meses 2 a 13, pedido ao SISBIO só no mês 4 (e a análise leva até 45 dias úteis, Portaria ICMBio 748/2022, Art. 30).
- **Trecho:** "Solicitação de autorização no SISBIO | 4"
- **Trecho:** "Campanhas de campo (12 campanhas mensais) | 2 a 13"
- **Trecho:** "a ser solicitada no início do projeto"
- **Onde:** seções 6 e 9
- **Tipos aceitos:** viabilidade
- **Por que é erro:** captura e coleta in situ dependem de autorização prévia (Portaria 748/2022, Art. 1º, § 1º, I e II).

### E08 · ética · importante
- **Erro:** remessa de tecido ao exterior e sequenciamento (acesso a patrimônio genético) sem cadastro no SisGen previsto (Lei 13.123/2015, Art. 12 e § 2º; Decreto 8.772/2016).
- **Trecho:** "As amostras de tecido serão enviadas ao laboratório parceiro na Universidade de Lisboa (Portugal), que fará a extração de DNA e o sequenciamento do gene COI, sem custo para o projeto."
- **Onde:** seção 5.2 (e ausência na seção 6)
- **Tipos aceitos:** —
- **Por que é erro:** o cadastro é prévio à remessa e à divulgação dos resultados; o projeto nem menciona o SisGen.

### E09 · viabilidade · importante
- **Erro:** cronograma impossível: redação vai até o mês 26 num mestrado de 24 meses com defesa no mês 24.
- **Trecho:** "Redação da dissertação | 18 a 26"
- **Trecho:** "Defesa | 24"
- **Onde:** seção 9
- **Tipos aceitos:** —
- **Por que é erro:** a defesa acontece antes de terminar a redação; o prazo do curso estoura.

### E10 · aderência · importante
- **Erro:** aderência fraca: o projeto é de ecologia de comunidades e paisagem, e a justificativa de inserção na linha de Sistemática e Evolução é só o grupo taxonômico.
- **Trecho:** "O projeto se insere na Linha 2 (Sistemática e Evolução de Vertebrados) porque trata de lagartos, que são vertebrados, e porque o inventário contribui para o conhecimento da fauna regional."
- **Onde:** seção 7
- **Tipos aceitos:** —
- **Por que é erro:** a justificativa serviria para qualquer projeto com vertebrados; a pergunta e o método não são de sistemática nem de evolução.

### E11 · referencial · ajuste
- **Erro:** citação sem entrada nas referências.
- **Trecho:** "populações de espécies florestais tendem a declinar perto das bordas (Silva et al., 2019)"
- **Onde:** seção 1
- **Tipos aceitos:** ABNT
- **Por que é erro:** "Silva et al., 2019" não aparece na lista de referências.

### E12 · ABNT · ajuste
- **Erro:** referência em estilo Vancouver no meio de uma lista em ABNT.
- **Trecho:** "Haddad NM, Brudvig LA, Clobert J, Davies KF, Gonzalez A, Holt RD, et al. Habitat fragmentation and its lasting impact on Earth's ecosystems. Sci Adv. 2015;1(2):e1500052."
- **Onde:** Referências
- **Tipos aceitos:** referencial
- **Por que é erro:** a lista não segue um padrão único.
