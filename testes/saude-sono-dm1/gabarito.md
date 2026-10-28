# Gabarito: projeto fictício de saúde com seres humanos (sono e DM1 em adolescentes)

Projeto: [projeto.md](projeto.md). 12 erros plantados: 4 bloqueantes, 6 importantes, 2 ajustes.

Formato lido por `testes/avaliar.py` (ver o gabarito do projeto de ecologia para a explicação).

Erros extras que a banca pode apontar e que não são falha dela (não plantados de propósito, mas
legítimos): direção da associação (o próprio referencial diz que o controle ruim pode piorar o
sono); coleta na sala de espera sem privacidade; teste t sobre variação de HbA1c com perdas de
seguimento não previstas; ausência de plano para as perdas no seguimento.

### S01 · ética · bloqueante
- **Erro:** participantes de 12 a 17 anos, mas o projeto prevê só o TCLE "dos participantes": falta o consentimento do responsável legal e o assentimento do adolescente (Res. CNS 466/2012, itens II.2 e II.23).
- **Trecho:** "Todos os participantes assinarão o Termo de Consentimento Livre e Esclarecido (TCLE) antes da aplicação dos questionários."
- **Onde:** seção 6
- **Tipos aceitos:** —
- **Por que é erro:** menores de idade não consentem sozinhos; sem termo do responsável e assentimento, o CEP não aprova.

### S02 · ética · bloqueante
- **Erro:** coleta de dados de prontuário iniciada antes da submissão e da aprovação do CEP (Res. CNS 466/2012, item XI.2, alínea a).
- **Trecho:** "Para adiantar o cronograma, a coleta dos dados retrospectivos de prontuário (HbA1c dos últimos 12 meses) já foi iniciada em agosto de 2026, antes da submissão ao CEP."
- **Onde:** seção 6
- **Tipos aceitos:** viabilidade
- **Por que é erro:** dados coletados sem aprovação não podem ser usados; o problema é ético e compromete o projeto.

### S03 · ética · importante
- **Erro:** dados de saúde (sensíveis) identificados por nome e prontuário, guardados no Google Drive pessoal, sem anonimização ou pseudonimização (LGPD, Art. 5º, II; Art. 11, II, "c"; Art. 13).
- **Trecho:** "Os dados serão digitados em planilha no Google Drive pessoal da pesquisadora, identificados pelo nome completo e pelo número do prontuário de cada participante, para facilitar a conferência."
- **Onde:** seção 6
- **Tipos aceitos:** metodologia
- **Por que é erro:** a lei pede tratamento dentro do órgão de pesquisa e pseudonimização sempre que possível; o CEP vai exigir plano de guarda.

### S04 · hipóteses · importante
- **Erro:** hipótese causal ("causa") num desenho observacional que só sustenta associação; o próprio referencial reconhece que a direção pode ser a inversa.
- **Trecho:** "H1: A má qualidade do sono causa a elevação da hemoglobina glicada (HbA1c) nos adolescentes com DM1."
- **Onde:** seção 3
- **Tipos aceitos:** coerência, metodologia
- **Por que é erro:** o desenho não permite inferir causalidade; a hipótese deveria ser de associação.

### S05 · metodologia · bloqueante
- **Erro:** amostra incompatível com a análise: regressão logística com 12 covariáveis simultâneas e 40 participantes (poucos eventos por variável; o modelo não converge ou superajusta).
- **Trecho:** "regressão logística múltipla com as 12 covariáveis do Quadro 1 incluídas simultaneamente"
- **Trecho:** "Serão incluídos 40 adolescentes, número médio de atendimentos do ambulatório em dois meses, recrutados por conveniência nas consultas de rotina."
- **Onde:** seções 5.3 e 5.5
- **Tipos aceitos:** viabilidade
- **Por que é erro:** com 40 participantes, mesmo com metade de eventos, há menos de dois eventos por covariável; o objetivo (b) não se sustenta.

### S06 · metodologia · importante
- **Erro:** cálculo amostral (151) ignorado: a amostra prevista é de 40, sem justificativa estatística.
- **Trecho:** "resultou em 151 participantes"
- **Onde:** seção 5.3
- **Tipos aceitos:** viabilidade
- **Por que é erro:** o próprio cálculo mostra que 40 não dá a precisão desejada; a escolha vem da conveniência do serviço.

### S07 · coerência · importante
- **Erro:** objetivo específico (c) sem dado nem método: o esquema de insulina (bomba vs múltiplas doses) não está entre as variáveis coletadas nem na análise.
- **Trecho:** "(c) Comparar a qualidade do sono entre adolescentes em uso de sistema de infusão contínua de insulina e em esquema de múltiplas doses diárias"
- **Onde:** seção 3 (e Quadro 1)
- **Tipos aceitos:** metodologia
- **Por que é erro:** nenhuma etapa do método produz o dado que o objetivo pede.

### S08 · metodologia · importante
- **Erro:** instrumento não validado: tradução livre do PSQI, quando o próprio projeto cita a versão brasileira validada (Bertolazi et al., 2011).
- **Trecho:** "O PSQI será aplicado na versão original em inglês, traduzida livremente pela pesquisadora para o português."
- **Onde:** seção 5.4 (contra a seção 4)
- **Tipos aceitos:** coerência
- **Por que é erro:** a medida perde validade e comparabilidade; contradiz o referencial do próprio projeto.

### S09 · viabilidade · bloqueante
- **Erro:** cronograma impossível: com recrutamento nos meses 16 a 19 e segunda dosagem seis meses depois, as segundas dosagens cairiam nos meses 22 a 25, não 18 a 20; a última passa da defesa (mês 24).
- **Trecho:** "2ª dosagem de HbA1c (seis meses após a 1ª) | 18 a 20"
- **Trecho:** "Recrutamento, questionários e 1ª dosagem de HbA1c | 16 a 19"
- **Onde:** seção 9
- **Tipos aceitos:** —
- **Por que é erro:** o seguimento (objetivo d) não cabe no prazo do mestrado.

### S10 · aderência · importante
- **Erro:** aderência fraca: estudo clínico-epidemiológico de associação, justificado na linha de Políticas, Planejamento e Gestão só por "ser problema de saúde pública".
- **Trecho:** "O projeto insere-se na Linha 3 (Políticas, Planejamento e Gestão em Saúde) por abordar o diabetes, um problema de saúde pública de grande magnitude no Brasil."
- **Onde:** seção 7
- **Tipos aceitos:** —
- **Por que é erro:** a justificativa serviria para qualquer doença; o projeto não analisa política, planejamento nem gestão.

### S11 · referencial · ajuste
- **Erro:** citação sem entrada nas referências.
- **Trecho:** "encontrou má qualidade do sono em cerca de metade dos adolescentes com DM1 (Moura; Lins, 2021)"
- **Onde:** seção 1
- **Tipos aceitos:** ABNT
- **Por que é erro:** "Moura; Lins, 2021" não está na lista; e é a base da prevalência usada no cálculo amostral.

### S12 · ABNT · ajuste
- **Erro:** referência em estilo APA no meio de uma lista em ABNT.
- **Trecho:** "American Diabetes Association. (2024). Standards of Care in Diabetes—2024. Diabetes Care, 47(Supplement 1)."
- **Onde:** Referências
- **Tipos aceitos:** referencial
- **Por que é erro:** a lista não segue um padrão único.
