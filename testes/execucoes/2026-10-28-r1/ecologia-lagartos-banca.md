# Banca simulada: Efeito do tamanho dos fragmentos florestais sobre a riqueza e a abundância de lagartos de serrapilheira na Mata Atlântica do sul da Bahia

> Gerado por /banca:revisar em 2026-10-28. Revisão, não redação: aponta e sugere, não reescreve.
> Não substitui orientador nem banca. Verifique se o programa exige declaração de uso de IA.

## Resumo
- Comentários: 20 (5 bloqueantes, 9 importantes, 6 ajustes)
- Por eixo: coerência 5 · hipóteses 2 · metodologia 3 · aderência 1 · ética 3 · referencial 3 · ABNT 1 · viabilidade 2
- Mais urgente: C01 (H1 não pode ser refutada), C02 (o n real do efeito da área é 4 fragmentos e o GLMM não se sustenta), C03 (CEUA declarada dispensada apesar de captura, coleta e eutanásia)
- Insumos usados: projeto; ausentes: edital, ementa da Linha 2, Lattes do orientador (a pessoa pediu para seguir sem eles)

## 1. Mapa do projeto (confirmado em 2026-10-28)

Mestrado acadêmico, prazo do curso de 24 meses (confirmado pela pessoa).

| Elemento | Conteúdo |
|---|---|
| Identificação | Título acima. Mestrado acadêmico, PPGBC/UESM. Linha declarada: "Linha 2, Sistemática e Evolução de Vertebrados". 24 meses (mar/2027 a fev/2029). |
| Pergunta de pesquisa | Explícita: "O tamanho dos fragmentos florestais afeta a riqueza e a abundância de lagartos de serrapilheira no sul da Bahia?" (seção 3) |
| Objetivo geral | "Avaliar o efeito do tamanho dos fragmentos florestais sobre a riqueza e a abundância de lagartos de serrapilheira em remanescentes de Mata Atlântica no sul da Bahia." (seção 3) |
| Objetivos específicos | (a) inventariar as espécies; (b) comparar riqueza e abundância entre fragmentos pequenos e grandes; (c) relacionar abundância com dossel e serrapilheira; (d) dieta por conteúdo estomacal; (e) sequências COI (seção 3, literais no texto) |
| Hipóteses | H1: fragmentação "podendo aumentar ou diminuir a riqueza e a abundância"; H2: menor abundância de especialistas de interior em fragmentos < 50 ha do que em > 300 ha (seção 3) |
| Matriz objetivo → método → análise | (a) pitfall (5.2) → lista de espécies → rarefação e Chao 1 (5.4). (b) pitfall (5.2) → contagens → rarefação/Chao 1 e GLMM (5.4). (c) dossel e serrapilheira por linha, trimestral (5.3) → GLMM (5.4). (d) **nenhuma** etapa de método nem análise. (e) tecido enviado a Lisboa (5.2) → sequências → nenhuma análise (só depósito no GenBank/BOLD, seção 8). |
| Desenho e amostra | Observacional; 4 fragmentos (38, 45, 320 e 410 ha); 4 linhas × 10 baldes por fragmento = 160 baldes; 12 campanhas mensais de 10 dias; unidade amostral declarada: o balde (5.4). Critérios de escolha dos fragmentos: não encontrei. |
| Análise | Rarefação por indivíduos e Chao 1; GLMM Poisson com área, isolamento, distância da borda, dossel, serrapilheira e interações da área com as demais; fragmento como efeito aleatório; AICc; R ≥ 4.4 (5.4). Variável resposta do GLMM: não explicitada. |
| Gatilhos éticos | Vertebrados: captura, coleta e eutanásia (5.2). Patrimônio genético: tecido, DNA e remessa a Portugal (5.2). Sem seres humanos, indígenas, dados pessoais ou UC mencionada. |
| Cronograma | Campo meses 2 a 13; SISBIO mês 4; qualificação mês 12; sequenciamento e análise 14 a 20; redação 18 a 26; defesa 24. Sem CEUA e sem SisGen (seção 9). |
| Referências | 6 entradas; ABNT predominante; Haddad et al. (2015) em Vancouver. |

## 2. Comentários

### C01 · bloqueante · hipóteses
- **Onde:** seção 3
- **Trecho:** "A fragmentação florestal influencia a comunidade de lagartos de serrapilheira, podendo aumentar ou diminuir a riqueza e a abundância de acordo com as condições locais de cada fragmento."
- **Problema:** H1 aceita qualquer resultado: aumento, queda ou ausência de diferença podem ser lidos como "condições locais". Não há resultado possível que a contrarie, então ela não é testável. Como H1 é a hipótese que cobre a pergunta inteira (riqueza e abundância), o projeto fica sem hipótese central testável. Ela também fala em "fragmentação" e "condições locais", que não são as variáveis medidas (a área é).
- **Sugestão:** reformular H1 com direção ou forma ligada à variável que o método mede (área do fragmento) e escrever, para si, qual resultado a refutaria. Se a decisão for não prever direção, assumir o caráter exploratório e justificar isso.
- **Base:** HI2, HI3

### C02 · bloqueante · metodologia
- **Onde:** seção 5.4
- **Trecho:** "Cada balde será considerado uma unidade amostral independente, o que resulta em 160 unidades amostrais por campanha e garante poder estatístico às comparações."
- **Problema:** o tamanho do fragmento é atribuído ao fragmento, não ao balde: para o efeito da área, o n real é 4 (2 pequenos, 2 grandes). Baldes da mesma linha e do mesmo fragmento, vistoriados nas mesmas 12 campanhas, não são independentes; tratá-los como 160 réplicas é pseudorreplicação. O GLMM da seção 5.4 agrava o problema: área, isolamento e a interação área × isolamento são variáveis do fragmento; com o intercepto, são 4 parâmetros para 4 fragmentos, sem grau de liberdade para estimar a variância do efeito aleatório "fragmento", que também tem só 4 níveis. Somam-se nove efeitos fixos (cinco principais e quatro interações). Faltam ainda: a variável resposta (abundância total, por espécie, de especialistas, riqueza?), a estrutura de linha e de campanha, e a checagem de sobredispersão do Poisson. A riqueza, por rarefação e Chao 1, gera 4 valores, sem teste possível entre 2 e 2.
- **Sugestão:** decidir o que é a unidade amostral para cada pergunta e contar os graus de liberdade antes de escolher o modelo. Caminhos possíveis: amostrar mais fragmentos ao longo de um gradiente de área (redistribuindo o esforço de baldes) ou reduzir a pergunta ao que 4 sítios sustentam, sem inferir efeito da área. Rever com o guia que o próprio projeto cita (Bolker et al., 2009) o que ele diz sobre número de níveis de efeito aleatório e sobre sobredispersão. Especificar resposta, efeitos e estrutura hierárquica (balde em linha em fragmento; campanha).
- **Base:** ME1, ME2, ME3, HI1

### C03 · bloqueante · ética
- **Onde:** seção 6
- **Trecho:** "Por se tratar de estudo observacional de campo, sem experimentação em laboratório, o projeto dispensa avaliação pela Comissão de Ética no Uso de Animais (CEUA)."
- **Problema:** o projeto captura, manipula, mede, pesa, coleta e eutanasia lagartos (seção 5.2). A Lei 11.794/2008 regula a utilização de animais em pesquisa científica (Art. 1º) e se aplica ao subfilo Vertebrata (Art. 2º), sem excluir estudos de campo; o CONCEA recomenda indeferir projetos realizados sem aprovação da CEUA (Art. 23, I). A autorização do SISBIO não substitui as demais exigências (Portaria ICMBio 748/2022, Art. 60). O método de eutanásia também não está descrito.
- **Sugestão:** retirar a dispensa, prever a submissão à CEUA da instituição antes do campo e incluí-la no cronograma. Descrever o método de eutanásia e o manejo nos baldes; para as regras do CONCEA sobre campo e eutanásia, consulte a CEUA da instituição.
- **Base:** ET3; Lei 11.794/2008, Art. 1º, Art. 2º e Art. 23, I; Portaria ICMBio 748/2022, Art. 60

### C04 · bloqueante · ética
- **Onde:** seção 9 (e seção 6)
- **Trecho:** "| Solicitação de autorização no SISBIO | 4 | [...] | Campanhas de campo (12 campanhas mensais) | 2 a 13 |"
- **Problema:** as campanhas começam no mês 2 e a autorização só é solicitada no mês 4: dois meses de captura e coleta sem autorização. Captura, coleta e transporte de fauna silvestre in situ dependem de autorização no Sisbio (Portaria ICMBio 748/2022, Art. 1º, § 1º, I, II e IV), e o prazo de emissão é de até 45 dias úteis após a submissão (Art. 30). A CEUA (C03) e o SisGen (C12) também não aparecem no cronograma. A autorização tem validade de um ano e exige relatório para revalidação (Art. 31), o que pesa num campo de 12 meses.
- **Sugestão:** mover a submissão ao SISBIO e à CEUA para antes do campo, com a folga de tramitação, e recontar o início das campanhas a partir da aprovação. Refazer em cadeia as etapas que dependem do campo (triagem, sequenciamento, análise, qualificação).
- **Base:** ET6, VC2, VC3; Portaria ICMBio 748/2022, Art. 1º, § 1º, Art. 30 e Art. 31

### C05 · bloqueante · viabilidade
- **Onde:** seção 9
- **Trecho:** "| Redação da dissertação | 18 a 26 |"
- **Problema:** o curso tem 24 meses e a defesa está no mês 24, mas a redação vai até o mês 26, depois da defesa e do prazo. Com o atraso de C04, o fim do campo, a análise e a redação andam ainda mais para frente.
- **Sugestão:** refazer o cronograma a partir da data real de início do campo, terminando a redação antes da defesa, e cortar ou encurtar etapas (ver C08 e C16) se não couber.
- **Base:** VC1, VC2

### C06 · importante · referencial
- **Onde:** seção 2
- **Trecho:** "Ainda são poucos os estudos sobre o efeito do tamanho dos fragmentos sobre lagartos na porção baiana da Mata Atlântica, e a maior parte dos inventários da região foi feita em unidades de conservação grandes."
- **Problema:** é a lacuna que justifica o projeto, e está afirmada sem nenhuma citação. O referencial não traz nenhum estudo sobre lagartos (ou herpetofauna) e tamanho de fragmento na Mata Atlântica; a referência mais recente da lista é de 2015. A banca não tem como saber se a lacuna existe.
- **Sugestão:** levantar e citar os estudos sobre herpetofauna de serrapilheira e fragmentação na Mata Atlântica (inclusive no sul da Bahia e em cabrucas) e mostrar o que eles deixam em aberto que este projeto responde.
- **Base:** RE2, RE4, RE1

### C07 · importante · hipóteses
- **Onde:** seção 3
- **Trecho:** "H2: A abundância de espécies especialistas de interior de floresta é menor nos fragmentos pequenos (menos de 50 ha) do que nos fragmentos grandes (mais de 300 ha)."
- **Problema:** H2 tem direção, mas "especialista de interior de floresta" não está definido no método: a introdução dá exemplos, sem critério de classificação nem fonte. Também não há análise específica para H2 (a resposta do GLMM não é dita, ver C02), e a comparação é de 2 contra 2 fragmentos.
- **Sugestão:** definir o critério (e a fonte) para classificar cada espécie como especialista antes da coleta, dizer qual variável resposta testa H2 e como ela entra na análise.
- **Base:** HI3, ME5, CO2

### C08 · importante · coerência
- **Onde:** seção 3
- **Trecho:** "(d) Caracterizar a dieta das espécies mais abundantes por meio da análise do conteúdo estomacal;"
- **Problema:** nenhuma etapa do método nem da análise trata de dieta: não diz de que indivíduos virão os estômagos, como serão triados e identificados os itens, nem que índice será usado. Os únicos animais mortos são os até cinco testemunhos por espécie (5.2), o que dá amostra muito pequena; coletar mais aumentaria a eutanásia, que já não tem CEUA (C03). O objetivo também não se liga à pergunta sobre tamanho do fragmento.
- **Sugestão:** decidir se a dieta fica no projeto. Se ficar, descrever método, n por espécie, análise e a relação com a pergunta, e incluir na CEUA; se sair, retirar o objetivo.
- **Base:** CO2, CO3

### C09 · importante · coerência
- **Onde:** seção 4
- **Trecho:** "Fahrig (2003) argumenta, porém, que muitos estudos confundem perda de habitat com fragmentação, e que comparações entre fragmentos precisam controlar a quantidade de habitat na paisagem do entorno."
- **Problema:** o próprio referencial faz essa exigência, mas o método mede só área e isolamento (5.3), sem quantidade de habitat no entorno. Com 2 fragmentos de cada classe, a área se confunde com município, matriz, histórico e paisagem de cada sítio, e a conclusão sobre "efeito do tamanho" (título e objetivo geral) vira associação em 4 sítios. As hipóteses e os resultados alternam "fragmentação" e "tamanho" como se fossem a mesma coisa, exatamente a confusão que a autora citada critica.
- **Sugestão:** medir a quantidade de habitat no entorno de cada fragmento (definir a escala) e explicar como ela entra no desenho ou na escolha dos fragmentos; usar "tamanho do fragmento" com sentido único em todo o texto; ajustar a linguagem causal ao que o desenho permite.
- **Base:** CO4, CO6, HI4, ME6

### C10 · importante · metodologia
- **Onde:** seção 5.2
- **Trecho:** "As linhas ficarão a pelo menos 100 m da borda e a pelo menos 200 m umas das outras."
- **Problema:** num fragmento circular de 38 ha, a área a mais de 100 m da borda tem cerca de 19 ha; em formato irregular, pode ser muito menor ou nem existir. Não está dito se as quatro linhas cabem em F1 e F2. Além disso, nos fragmentos pequenos a distância da borda varia pouco, enquanto nos grandes pode ser muito maior: "distância da borda" (preditor do GLMM) fica confundida com área. Também não há critério de escolha dos fragmentos nem comprimento das linhas.
- **Sugestão:** verificar em imagem se as linhas cabem em cada fragmento com essas regras e informar o comprimento das linhas; padronizar a faixa de distância da borda entre fragmentos ou explicar como separar borda de área; descrever os critérios de seleção dos quatro fragmentos.
- **Base:** ME5, ME6, VC4

### C11 · importante · coerência
- **Onde:** seção 5.2 (e seções 4 e 8)
- **Trecho:** "As armadilhas de queda serão o único método de amostragem, para garantir o mesmo esforço em todos os fragmentos."
- **Problema:** a seção 4 diz que amostragens só com armadilhas de queda "subestimam espécies arborícolas, de grande porte ou que evitam as armadilhas, o que compromete estimativas de riqueza total (Cechin; Martins, 2000)". Mesmo assim, o método usa só armadilhas de queda e a seção 8 promete "a lista completa das espécies" e "estimativas da riqueza total". O método contradiz a crítica que o próprio projeto faz e os resultados prometem mais do que ele entrega. Vale conferir se alguma espécie citada como típica na introdução (o gênero *Enyalius*, por exemplo) é pouco amostrada por armadilha de queda.
- **Sugestão:** ou incluir um método complementar padronizado por esforço (o que garante a comparabilidade), ou manter só armadilhas de queda e restringir objetivos e resultados ao que elas amostram, explicando a escolha.
- **Base:** CO4, CO5

### C12 · importante · ética
- **Onde:** seção 5.2
- **Trecho:** "As amostras de tecido serão enviadas ao laboratório parceiro na Universidade de Lisboa (Portugal), que fará a extração de DNA e o sequenciamento do gene COI, sem custo para o projeto."
- **Problema:** sequenciar tecido de espécie nativa é acesso ao patrimônio genético (Lei 13.123/2015, Art. 2º, VIII), e a remessa ao exterior para acesso ou prestação de serviço precisa ser cadastrada (Art. 12). O cadastro deve ser prévio à remessa e à divulgação dos resultados (Art. 12, § 2º), o que inclui o depósito no GenBank e no BOLD previsto na seção 8. O cadastro de acesso e o de remessa são feitos no SisGen (Decreto 8.772/2016, Art. 22 e Art. 25). O projeto não menciona o SisGen nem o prevê no cronograma. Documentos de transferência de material para a remessa: (conferir o texto vigente).
- **Sugestão:** prever o cadastro no SisGen antes da remessa e antes de qualquer divulgação, colocá-lo no cronograma e verificar com o setor responsável da instituição a documentação de remessa e o transporte das amostras.
- **Base:** ET4; Lei 13.123/2015, Art. 2º, VIII, Art. 12 e Art. 12, § 2º; Decreto 8.772/2016, Art. 22 e Art. 25

### C13 · importante · aderência
- **Onde:** seção 7
- **Trecho:** "O projeto se insere na Linha 2 (Sistemática e Evolução de Vertebrados) porque trata de lagartos, que são vertebrados, e porque o inventário contribui para o conhecimento da fauna regional."
- **Problema:** a justificativa é só taxonômica e serviria para qualquer projeto com vertebrados. A pergunta, as hipóteses e a análise são de ecologia de comunidades e de paisagem; nada no projeto trata de sistemática ou evolução, exceto o barcoding, que não tem análise (C16). Sem a ementa da linha e sem o Lattes do orientador, não dá para avaliar a aderência; fica a pergunta.
- **Sugestão:** confirmar com a ementa da Linha 2 se ecologia de comunidades em fragmentos cabe nela, verificar se o programa tem linha mais próxima e reescrever a aderência com argumento de conteúdo (objeto, método ou pergunta). Ter claro qual é a produção do orientador no tema ou no método.
- **Base:** AD1, AD4

### C14 · importante · viabilidade
- **Onde:** seção 10
- **Trecho:** "As despesas de campo serão cobertas pela bolsa da candidata e pelo projeto do orientador."
- **Problema:** o campo soma 120 dias (12 campanhas × 10 dias) a 210 km da UESM, com vistoria diária de 160 baldes em 4 fragmentos que distam 15 a 40 km entre si, nos mesmos meses das disciplinas obrigatórias (1 a 12). O orçamento não prevê hospedagem, alimentação nem auxiliares de campo, e os 420 km por campanha cobrem só ida e volta à base, não o deslocamento diário entre fragmentos. Não diz quem compõe a equipe, e o sequenciamento depende inteiramente do laboratório parceiro, sem plano B.
- **Sugestão:** dimensionar equipe e logística da vistoria diária, completar o orçamento (estadia, alimentação, deslocamento entre fragmentos, auxiliares) com fonte definida para cada item, compatibilizar campo e disciplinas e prever alternativa para o sequenciamento e para perdas de campanha.
- **Base:** VC4, VC5

### C15 · ajuste · referencial
- **Onde:** seção 1
- **Trecho:** "populações de espécies florestais tendem a declinar perto das bordas (Silva et al., 2019)"
- **Problema:** Silva et al. (2019) é citado sem entrada nas referências. As demais citações do texto (Ribeiro et al., 2009; Fahrig, 2003; Haddad et al., 2015; Cechin; Martins, 2000; Gotelli; Colwell, 2001; Bolker et al., 2009) têm entrada, e todas as entradas são citadas.
- **Sugestão:** incluir a entrada completa na lista ou retirar a citação.
- **Base:** RE3

### C16 · ajuste · coerência
- **Onde:** seção 3
- **Trecho:** "(e) Gerar sequências de DNA (código de barras, gene COI) das espécies registradas."
- **Problema:** o objetivo tem método (5.2) e produto (depósito no GenBank e no BOLD), mas nenhuma análise, e não se liga à pergunta nem ao objetivo geral. Ele acrescenta exigência regulatória (C12) e dependência de laboratório externo (C14) num cronograma que já não cabe (C05). Classifiquei como ajuste, e não como importante, porque o objetivo tem método e produto; o custo dele aparece nos outros comentários.
- **Sugestão:** decidir se o barcoding é essencial à dissertação. Se ficar, dizer como as sequências ajudam a responder a pergunta (por exemplo, na identificação das espécies) ou tratá-lo como produto secundário declarado.
- **Base:** CO2, CO3

### C17 · ajuste · referencial
- **Onde:** seção 4
- **Trecho:** "A teoria de biogeografia de ilhas e, depois, a ecologia de paisagens forneceram a base para prever que fragmentos menores e mais isolados abrigam menos espécies."
- **Problema:** é a base teórica da previsão central e está sem nenhuma citação.
- **Sugestão:** citar as obras de referência da teoria de biogeografia de ilhas e da ecologia de paisagens que sustentam a previsão.
- **Base:** RE4, RE1

### C18 · ajuste · metodologia
- **Onde:** seção 5.2
- **Trecho:** "Serão feitas 12 campanhas mensais, de dez dias cada, com vistoria diária dos baldes pela manhã."
- **Problema:** não diz se os baldes ficam fechados entre campanhas, nem as medidas contra afogamento, predação e calor nos baldes (furos, abrigo, cobertura), que importam para o bem-estar e para a CEUA. O esforço total também não aparece em unidade comparável (160 baldes × 10 dias × 12 campanhas = 19.200 baldes-dia).
- **Sugestão:** descrever o manejo dos baldes durante e entre campanhas e informar o esforço em baldes-dia por fragmento e no total.
- **Base:** ME5

### C19 · ajuste · coerência
- **Onde:** seção 8
- **Trecho:** "demonstrar que fragmentos pequenos têm menor riqueza e menor abundância de espécies de interior de floresta"
- **Problema:** o resultado esperado é dado como certo ("demonstrar") e tem direção definida, enquanto H1 diz que a riqueza e a abundância podem "aumentar ou diminuir". As duas seções não falam a mesma coisa. Classifiquei como ajuste porque a correção de H1 (C01) resolve a maior parte.
- **Sugestão:** alinhar os resultados esperados às hipóteses corrigidas e tratá-los como previsão a testar, não como conclusão.
- **Base:** CO5, CO6

### C20 · ajuste · ABNT
- **Onde:** Referências
- **Trecho:** "Haddad NM, Brudvig LA, Clobert J, Davies KF, Gonzalez A, Holt RD, et al. Habitat fragmentation and its lasting impact on Earth's ecosystems. Sci Adv. 2015;1(2):e1500052."
- **Problema:** é a única entrada em estilo Vancouver (nomes sem caixa alta, periódico abreviado, sem "v." e "n.") numa lista em que as outras cinco seguem a ABNT.
- **Sugestão:** padronizar a entrada no mesmo formato das demais e conferir a edição da NBR 6023 exigida pelo programa (conferir o texto vigente).
- **Base:** AB1

## 3. Arguição provável
1. **Que resultado da sua coleta faria você concluir que H1 é falsa?** (C01, C19). Como se preparar: ter uma H1 com direção e saber dizer qual padrão nos dados a contraria.
2. **Qual é o n do seu teste do efeito da área?** (C02). Como se preparar: saber quantos fragmentos, linhas e baldes há, e quantos graus de liberdade sobram no nível do fragmento no modelo proposto.
3. **Como você estima a variância de um efeito aleatório com quatro níveis e ainda ajusta área, isolamento e a interação entre eles?** (C02). Como se preparar: rever o modelo, contar parâmetros por nível e decidir o que sai.
4. **Por que dois fragmentos de cada tamanho, e não um gradiente de área? Como separar a área da paisagem de cada local?** (C02, C09, C10). Como se preparar: ter a justificativa da escolha dos fragmentos ou uma proposta de redesenho.
5. **Você cita Fahrig sobre controlar a quantidade de habitat no entorno. Onde isso está no seu método?** (C09). Como se preparar: ter lido Fahrig (2003) inteiro e definido a escala de paisagem.
6. **Por que o projeto dispensa a CEUA se há captura, coleta e eutanásia? Qual é o método de eutanásia?** (C03, C18). Como se preparar: conhecer as exigências da CEUA da instituição para estudos de campo e o protocolo que vai usar.
7. **Em que mês o campo começa de verdade, com SISBIO e CEUA aprovados? O que acontece com a qualificação e com a defesa?** (C04, C05). Como se preparar: trazer o cronograma refeito com os prazos de tramitação.
8. **Como cabe uma redação até o mês 26 num curso de 24 meses?** (C05). Como se preparar: decidir o que encurtar ou cortar.
9. **Como você classifica uma espécie como especialista de interior?** (C07). Como se preparar: critério e fonte definidos, com a lista provável das espécies em cada classe.
10. **Com até cinco estômagos por espécie, o que dá para dizer sobre dieta? E como isso se liga ao tamanho do fragmento?** (C08). Como se preparar: decidir se o objetivo fica e, se ficar, com que n e método.
11. **Seu referencial diz que armadilha de queda sozinha subestima a riqueza. Por que usá-la como único método e prometer a lista completa?** (C11, C19). Como se preparar: conhecer Cechin e Martins (2000) e ter a justificativa da escolha ou o método complementar.
12. **Quando e por quem será feito o cadastro no SisGen e a remessa para Lisboa?** (C12, C16). Como se preparar: saber o caminho na instituição e o que precisa estar pronto antes do envio e antes do depósito no GenBank.
13. **O que neste projeto é sistemática ou evolução? Qual é a experiência do orientador com ecologia de fragmentos?** (C13, C16). Como se preparar: ler a ementa da Linha 2 e conhecer a produção do orientador.
14. **Quem vai vistoriar 160 baldes todos os dias, por 120 dias, durante as disciplinas, e com que recurso?** (C14, C18). Como se preparar: equipe, logística e orçamento completos.
15. **Que estudos já mediram o efeito do tamanho de fragmento sobre lagartos na Mata Atlântica, e o que falta neles?** (C06, C15, C17). Como se preparar: levantamento bibliográfico recente sobre o tema e a região.

## 4. Preparação para a entrevista
- Saber de cor os números do desenho: 4 fragmentos (38, 45, 320 e 410 ha), 16 linhas, 160 baldes, 19.200 baldes-dia, e quantas unidades independentes há para cada pergunta.
- Chegar com a decisão sobre o desenho tomada: mais fragmentos num gradiente de área ou pergunta reduzida ao que 4 sítios sustentam.
- Levar o cronograma refeito: CEUA e SISBIO (até 45 dias úteis) antes do campo, SisGen antes da remessa e da divulgação, redação terminando antes da defesa.
- Ler a fundo Fahrig (2003), Cechin e Martins (2000) e Bolker et al. (2009), e ter estudos recentes sobre herpetofauna e fragmentação na Mata Atlântica.
- Confirmar com a ementa da Linha 2 e com o orientador a inserção do projeto, e decidir o destino dos objetivos (d) e (e).
- Ter o orçamento completo do campo, com fonte para cada item.

## 5. Registro da autochecagem
- Trechos conferidos: 20; corrigidos: 0; comentários apagados por trecho inexistente: 0
- O script `checar_trechos.py` não rodou nesta sessão (a execução de Python ficou pendente de aprovação). Os 20 trechos foram conferidos por busca literal no `projeto.md` e todos foram encontrados. O trecho de C04 junta duas linhas da mesma tabela do cronograma.
- Conferência manual: as normas citadas estão em `referencias/normas.md` com o mesmo número; todas as perguntas da arguição apontam para comentários que existem; o resumo bate com a contagem (5 + 9 + 6 = 20).
