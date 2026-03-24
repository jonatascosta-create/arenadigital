# Fase 12 — Revisao de Qualidade (Quality Gate Final)

> Squad doc-safety | Fase 12 — QA Review | @doc-chief
> Autor: @doc-chief | Data: 2026-02-26
> Documento avaliado: `fase-11-roteiro-final.md` (FINAL DRAFT)
> Episodio: RMS Titanic: A Arquitetura do Desastre | Diretor: James Cameron | 90 min

---

## SUMARIO EXECUTIVO

O roteiro final consolidado da Fase 11 e um documento de alta qualidade documental que integra com rigor as nove fases anteriores do pipeline. A estrutura McKee/Bernard esta solidamente implementada, a analise SST funciona como motor narrativo (nao como citacao academica), as licoes aprendidas estao organicamente integradas no tecido do Ato III, e o principio unificador MOSTRA + ESCONDE + IGNORA e verificavel em multiplas sequencias. O roteiro respeita as veto conditions do pipeline de seguranca documental.

Identifico abaixo uma discrepancia aritmetica menor nas duracoes (89 min vs 90 min declarados) e algumas observacoes pontuais que nao comprometem a aprovacao.

---

## STEP 1 + STEP 2: AVALIACAO DE CRITERIOS

### A. Criterios do Roteiro Final (7)

---

#### Criterio RF-1: SST integrada no climax (nao apenas mencionada)

**Veredicto: [x] ATENDIDO**

**Evidencia:** A SEQ 13 ("CLIMAX: O SISTEMA") e inteiramente construida sobre frameworks SST como MOTOR narrativo:

- **Reason (Swiss Cheese):** 5 camadas animadas em CGI, cada camada identificada por nome (Regulacao, Organizacao, Supervisao, Precondicoes, Atos no Momento). Buracos acendendo em vermelho. Alinhamento visual dos buracos como revelacao do sistema. Nao e citacao — e a ESTRUTURA VISUAL do climax.
- **Dekker (Drift + Local Rationality):** Time-lapse de 18 anos (1894-1912). Montagem de entrevistas com Foecke, Stephenson, Butler demonstrando Local Rationality ("Os rebites eram o que sempre usaram" / "Phillips fazia o que a Marconi pagava" / "Smith seguia o procedimento de 40 anos"). Dekker nao e mencionado ao espectador — seus mecanismos sao MOSTRADOS.
- **Schein (Nivel 3):** VO Cameron explicita o pressuposto basico: "O pressuposto do Titanic era: 'Somos grandes demais para falhar.' Ninguem o dizia porque todos o respiravam."
- **Westrum:** Score 6/25 (cultura patologica) aparece em grafismo. A cultura patologica e DEMONSTRADA pelo arco do silenciamento (SEQ 04, 07, 12), nao apenas rotulada.
- **Hopkins:** Indicadores mapeados ao longo do Ato II e convergindo no climax como sintese.

A SST nao e "mencionada" ou "citada" — e a LINGUAGEM VISUAL E NARRATIVA do climax. O Swiss Cheese e set piece visual, nao diagrama academico. Criterio plenamente atendido.

---

#### Criterio RF-2: 4 blocos estruturados com duracao estimada

**Veredicto: [!] PARCIAL**

**Evidencia:** O roteiro apresenta 4 blocos claramente estruturados:

| Bloco | Conteudo | Duracao declarada | Duracao verificada (soma SEQs) |
|-------|----------|-------------------|-------------------------------|
| Bloco 1 — Abertura: Hook + Setup | ATO I, SEQ 01-05 | ~22 min | 22 min (3+6+8+2+3) |
| Bloco 2 — Desenvolvimento: Confrontacao | ATO II, SEQ 06-12 | ~45 min | 44 min (7+7+8+8+4+5+5) |
| Bloco 3 — Climax: Revelacao Sistemica | ATO III parte 1, SEQ 13 | ~7 min | 7 min |
| Bloco 4 — Resolucao: Legado + Licoes | ATO III parte 2, SEQ 14-17 | ~16 min | 16 min (5+4+4+3) |

**Total declarado:** 90 min. **Total verificado:** 89 min.

Existe uma discrepancia de 1 minuto entre o total declarado (90 min) e a soma das duracoes individuais (89 min). Na secao de Validacoes, o documento declara Ato II = 44 min e Ato III = 24 min, mas a soma das SEQs do Ato III da 23 min (7+5+4+4+3). Esta discrepancia e menor e facilmente resolvivel (atribuir 1 minuto adicional a qualquer sequencia ou a transicoes), mas deve ser corrigida para consistencia interna. Os 4 blocos estao claramente definidos com arco cromatico, value-charge e beats McKee. Criterio atendido com ressalva menor.

---

#### Criterio RF-3: Proporcoes Bernard respeitadas (25/50/25, tolerancia 10%)

**Veredicto: [x] ATENDIDO**

**Evidencia (secao "Validacoes" do roteiro, confirmada por verificacao independente):**

| Componente | Meta | Real | Desvio |
|------------|------|------|--------|
| Setup (Ato I) | 25% (22.5 min) | 24.4% (22 min) | -0.6% |
| Confrontacao (Ato II) | 50% (45 min) | 48.9% (44 min) | -1.1% |
| Resolucao (Ato III) | 25% (22.5 min) | 25.6% (23 min)* | +0.6% |

(*) Usando a soma verificada de 23 min, nao os 24 declarados no documento.

Todos os desvios estao bem dentro da tolerancia de 10%. Usando 89 min como base: 24.7% / 49.4% / 25.8%. Criterio plenamente atendido.

---

#### Criterio RF-4: VO <= 40%

**Veredicto: [x] ATENDIDO**

**Evidencia:** O roteiro inclui uma tabela detalhada de proporcoes de VO:

| Tipo | Duracao estimada | % do total |
|------|-----------------|-----------|
| VO Cameron | ~15 min | 16.7% |
| Entrevistas (som direto) | ~30 min | 33.3% |
| Arquivo/grafismo/reconst. (sem voz) | ~20 min | 22.2% |
| Silencio + som ambiente | ~10 min | 11.1% |
| CGI/animacao com VO | ~10 min | 11.1% |
| Musica composta | ~2 min | 2.2% |
| Silencio total (marcado) | ~3 min | 3.3% |
| **VO total** | **~25 min** | **~28%** |

VO total estimado em 28%, significativamente abaixo do limite de 40%. O VO e concentrado em momentos-chave (abertura, transicoes entre blocos, fechamento) e nunca substitui a imagem ou o silencio como linguagem primaria. Criterio plenamente atendido.

**Verificacao adicional:** A leitura das 17 sequencias confirma que a narrativa e predominantemente visual (reconstituicoes, grafismos, CGI, arquivo) e sonora (entrevistas, silencios marcados). O VO de Cameron funciona como guia, nao como muleta. Diversas sequencias (SEQ 09 — grafismo mortalidade, SEQ 12 — triptico) sao explicitamente marcadas para silencio durante momentos visuais-chave.

---

#### Criterio RF-5: Checklist qualidade-roteiro APROVADO

**Veredicto: [x] ATENDIDO**

**Evidencia:** O roteiro inclui um checklist de qualidade com 20 criterios (secao "Step 4: Checklist Final de Qualidade"), todos marcados como OK com evidencia especifica. Verifiquei os mais criticos:

1. **Controlling Idea testavel em cada sequencia** — OK. Cada SEQ reforça ou complica "arrogancia tecnologica + silenciamento = destruicao."
2. **Questao Dramatica nunca respondida com sim/nao** — OK. Resposta emerge em camadas.
3. **5 Beats McKee identificaveis** — OK. Beat 1 (SEQ 01-04), Beat 2 (SEQ 05-06), Beat 3 (SEQ 07-12), Beat 4 (SEQ 13), Beat 5 (SEQ 14-17).
4. **Turning Points marcados** — OK. TP1: flash branco SEQ 05 / TP2: Swiss Cheese SEQ 12-13.
5. **Progressive Complications em ordem crescente** — OK. Avisos < Botes < Classe < Californian < DNA < Vozes Silenciadas.
6. **Climax e revelacao SISTEMICA** — OK. SEQ 13: P&B puro, geometria forense.
7. **Resolucao e PERGUNTA, nao "moral da historia"** — OK. SEQ 17 termina com pergunta ao espectador.
8. **Licoes integradas organicamente** — OK. 8 licoes distribuidas em SEQ 14-17 como tecido narrativo.
9. **Arco cromatico coerente** — OK. Ouro → Cinza → Verde → P&B → Azul-Preto. Circularidade SEQ 01/17.
10. **Reconstituicoes fragmentadas** — OK. N1, N2, N3 aplicados. Nenhuma cena completa.

O checklist interno e robusto e esta acompanhado de evidencia verificavel. Criterio plenamente atendido.

---

#### Criterio RF-6: Questao dramatica respondida

**Veredicto: [x] ATENDIDO**

**Evidencia:** A questao dramatica e formulada na abertura do roteiro:

> "Como uma civilizacao inteira — seus engenheiros, seus reguladores, seus capitaes, seus magnatas — construiu, certificou, tripulou e lotou um navio que nao podia salvar metade das pessoas a bordo, e como cada um deles acreditou estar fazendo a coisa certa?"

A resposta emerge progressivamente ao longo dos 3 atos:

- **Ato I:** Planta a semente — Carlisle, Andrews, Ismay como tres visoes de um mesmo navio.
- **Ato II:** Cada complicacao revela uma camada da resposta — de "negligencia" para "design do sistema" para "cultura civilizacional."
- **Ato III (SEQ 13):** O climax materializa a resposta completa via Swiss Cheese — "Nenhum desses decisores planejou matar 1.517 pessoas. Cada um fez o que parecia certo. E foi EXATAMENTE por isso que tantos morreram."

A questao nunca e respondida com sim/nao. A resposta e multiestratificada e exige os 90 minutos para se completar. O espectador recebe parcelas da resposta em cada sequencia, mantendo o "trem" de Bernard em movimento. Criterio plenamente atendido.

---

#### Criterio RF-7: Principio unificador verificavel: MOSTRA + ESCONDE + IGNORA

**Veredicto: [x] ATENDIDO**

**Evidencia:** Ver Step 4 abaixo para analise detalhada da triangulacao. O roteiro opera consistentemente sob o principio de que a narrativa MOSTRA o que o sistema ESCONDE, articula o que a investigacao tradicional IGNORA, e materializa o que a cultura NORMALIZA. Criterio plenamente atendido.

---

### B. Criterios da Escaleta (8)

---

#### Criterio E-1: Controlling Idea formulada (valor + causa)

**Veredicto: [x] ATENDIDO**

**Evidencia:** Formulacao presente na secao "Premissa Narrativa":

> "Vidas sao destruidas quando uma civilizacao inteira normaliza a arrogancia tecnologica, e o lucro — disfarcado de progresso — silencia sistematicamente cada voz que alerta sobre o perigo."

- **Valor:** Vida humana / Seguranca / Verdade (explicitamente declarado)
- **Causa:** Normalizacao da arrogancia tecnologica + silenciamento das vozes de alerta (causa especifica, nao generica)
- **Teste:** Cada sequencia reforça ou complica esta ideia (verificado na leitura das 17 SEQs)

A Controlling Idea e McKee-compliant: tem valor em jogo E causa identificada. Nao e generica ("acidentes sao ruins") — identifica o mecanismo especifico.

---

#### Criterio E-2: 5 beats McKee com value-charge

**Veredicto: [x] ATENDIDO**

**Evidencia:**

| Beat | Sequencias | Value-Charge | Verificacao |
|------|-----------|-------------|-------------|
| Beat 1 — Vida Normal | SEQ 01-04 | POSITIVO → NEGATIVO emergente | Progresso edwardiano com sombras (Carlisle, rebites) |
| Beat 2 — Inciting Incident | SEQ 05-06 | NEGATIVO (ruptura total) | Flash branco, 37 segundos, colisao forense |
| Beat 3 — Progressive Complications | SEQ 07-12 | NEGATIVO CRESCENTE → PICO NEGATIVO | 5 complicacoes em ordem crescente + Reversal |
| Beat 4 — Climax | SEQ 13 | NEGACAO DA NEGACAO | Swiss Cheese completo, P&B total |
| Beat 5 — Resolution | SEQ 14-17 | AMBIGUO → URGENCIA → RESPONSABILIDADE | SOLAS + Eastland + Ponte + Epilogo |

Cada beat tem value-charge claramente identificado e progressivo. A trajetoria de valor e coerente: do positivo (progresso) a negacao da negacao (negligencia normalizada como paradigma) e resolucao ambigua.

---

#### Criterio E-3: Minimo 3 gaps identificados

**Veredicto: [x] ATENDIDO**

**Evidencia:** O roteiro identifica 7 gaps (consideravelmente acima do minimo de 3):

| # | Gap | Onde |
|---|-----|------|
| 1 | O que vemos no fundo foi construido com orgulho | SEQ 01 |
| 2 | Os rebites frageis sao o DNA plantado na construcao | SEQ 02 (semente) → SEQ 11 (revelacao) |
| 3 | Nao foi negligencia consciente — foi arquitetura organizacional | SEQ 07 |
| 4 | Os davits tinham capacidade para 48 botes. Foram colocados 20 | SEQ 08 |
| 5 | A segregacao nao era falha do sistema — ERA o sistema | SEQ 09 |
| 6 | Nao ha um culpado. Ha algo PIOR: um sistema onde todos estao certos | SEQ 12 |
| 7 | A "cura" pos-Titanic matou mais num unico evento | SEQ 15 |

Cada gap opera como McKee prescreve: expectativa do publico vs resultado real, gerando impacto emocional e propulsao narrativa.

---

#### Criterio E-4: Negacao da Negacao atingida no climax

**Veredicto: [x] ATENDIDO**

**Evidencia:** A SEQ 13 (Climax) atinge explicitamente a Negacao da Negacao. A escaleta (Fase 6) detalha a escala completa em 4 eixos (Seguranca, Verdade, Justica, Voz/Dissidencia). O roteiro final materializa isso:

```
Seguranca plena → Risco pontual → Negligencia → Negligencia normalizada como PARADIGMA CIVILIZACIONAL
```

O VO de Cameron articula: "O Titanic NUNCA foi seguro. O sistema existia para afirmar que era." Nao se trata apenas de inseguranca (contrario) ou negligencia (negacao), mas de negligencia normalizada como paradigma — a era inteira estruturou suas instituicoes para confirmar a crenca de invencibilidade. A Negacao da Negacao e alcancada no climax e sustentada pela visualizacao do Swiss Cheese.

---

#### Criterio E-5: Questao dramatica formulada (nao sim/nao)

**Veredicto: [x] ATENDIDO**

**Evidencia:** Ja avaliado em RF-6. A questao e:

> "Como uma civilizacao inteira [...] construiu, certificou, tripulou e lotou um navio que nao podia salvar metade das pessoas a bordo, e como cada um deles acreditou estar fazendo a coisa certa?"

Comeca com "Como" — exige investigacao multiestratificada. Nao e respondivel com sim/nao. A resposta emerge ao longo dos 3 atos e nunca se reduz a uma frase simples.

---

#### Criterio E-6: 3 atos Bernard com proporcao 25/50/25

**Veredicto: [x] ATENDIDO**

**Evidencia:** Ja verificado em RF-3. Os 3 atos estao claramente delimitados:

- Ato I (SEQ 01-05): 22 min / 24.4%
- Ato II (SEQ 06-12): 44 min / 48.9%
- Ato III (SEQ 13-17): 23 min / 25.6%

Turning points claramente marcados (visual + narrativo + textual com ">>> TURNING POINT <<<"). Proporcoes dentro da tolerancia.

---

#### Criterio E-7: Teste do Trem: zero estacoes mortas

**Veredicto: [x] ATENDIDO**

**Evidencia:** A Fase 6 (Escaleta) identificou 6 estacoes de risco e resolveu cada uma com estrategias especificas. O roteiro final implementou TODAS essas solucoes:

1. **Contexto Era Edwardiana (6 min)** — Resolvido: entrelaçado com construcao do navio (SEQ 02). Nunca separa "historia" de "acao."
2. **Excesso de personagens** — Resolvido: apenas 3 no Ato I (Andrews, Carlisle, Ismay). Demais entram com FUNCAO.
3. **Board of Trade (regulamentacao abstrata)** — Resolvido: grafismo do navio crescendo vs regra parada (SEQ 08). Concretizado.
4. **Californian (desvio narrativo)** — Resolvido: 4 minutos, posicionado como espelho do sistema (SEQ 10).
5. **Swiss Cheese (aula teorica)** — Resolvido: visualizacao CGI, nao diagrama. Cada camada e decisao humana com rosto (SEQ 13).
6. **Ponte contemporanea (colada)** — Resolvido: montagem paralela VISUAL, nao discursiva (SEQ 16). 4 minutos.

Cada sequencia tem funcao narrativa clara. Nenhuma e removivel sem colapso do arco. O "trem" nao para.

---

#### Criterio E-8: Analise SST integrada

**Veredicto: [x] ATENDIDO**

**Evidencia:** O roteiro inclui um mapa detalhado de frameworks SST por sequencia (17 SEQs x 5 frameworks), demonstrando cobertura sistematica:

- **Dekker:** Presente em 11 das 17 sequencias (Local Rationality, Drift, Second Victim, Etapas 1-5)
- **Reason:** Presente em 13 das 17 sequencias (5 camadas + 4 subculturas)
- **Schein:** Presente em 7 das 17 sequencias (3 niveis)
- **Westrum:** Presente em 4 das 17 sequencias (diagnostico patologico)
- **Hopkins:** Presente em 6 das 17 sequencias (5 indicadores)

A integracao e NARRATIVA, nao academica. Os frameworks sao MOSTRADOS (reconstituicoes, grafismos, entrevistas) e nao EXPLICADOS ao espectador (exceto Swiss Cheese no climax, onde Cameron o nomeia explicitamente como ferramenta de compreensao).

---

### C. Criterios de Licoes Aprendidas (6)

---

#### Criterio L-1: Minimo 5 licoes com template completo

**Veredicto: [x] ATENDIDO**

**Evidencia:** O roteiro integra 8 licoes (acima do minimo de 5), todas provenientes da Fase 10 com template completo (Mecanismo, No Caso, Hoje, Pergunta, Visual):

1. L1 — A Regra Que Protegia Era a Que Matava
2. L2 — O Luxo Como Anestesia
3. L3 — Ninguem Acorda de Manha Planejando Matar 1.517 Pessoas
4. L4 — O Sistema Que Silencia o Alarme
5. L5 — 18 Anos de Decisoes Razoaveis
6. L6 — A Cura Que Mata
7. L7 — O Preco da Classe
8. L8 — Voce Esta Dentro de um Drift Agora

Cada licao e rastreavel a frameworks SST e personagens historicos. O mapa de integracao (secao "MAPA DE INTEGRACAO — LICOES NAS SEQUENCIAS") documenta onde e como cada licao aparece no roteiro.

---

#### Criterio L-2: Cada licao rastreavel a input de outro agente

**Veredicto: [x] ATENDIDO**

**Evidencia:** O mapa de convergencia da Fase 10 (Etapa 1) cruza cada licao com inputs de 5 fases:

| Licao | Fase 3 (SST) | Fase 4 (Tecnica) | Fase 5 (Cultura) | Fase 2 (Contexto) | Fase 6 (Escaleta) |
|-------|-------------|-----------------|-----------------|-------------------|-------------------|
| L1 | Reason Camada 1 | Rule 12 | Reporting FALHA | Captura regulatoria | SEQ 08, 14 |
| L2 | — | Custo rebites <0.3% | Schein Nivel 1 vs 3 | Era Edwardiana | SEQ 02-03, 14 |
| L3 | Swiss Cheese | — | Westrum PATOLOGICA | — | SEQ 12, 13 |
| L4 | — | Carlisle/Andrews | Hopkins Ind. #1 | Hierarquia edwardiana | SEQ 04, 07, 12 |
| L5 | Dekker Etapa 4 | Rebites "sempre assim" | Schein Nivel 3 | Nenhum navio afundou | SEQ 08, 13 |
| L6 | Dekker Etapa 5 | SOLAS → Eastland | Learning FALHA | Regulacao reativa | SEQ 15 |
| L7 | Reason Camada 5 | Grades/corredores | Hopkins Ind. #5 | Classe social edwardiana | SEQ 09 |
| L8 | TODOS | — | TODOS | — | SEQ 16-17 |

Cada licao converge de multiplos inputs, nao de um unico agente. A rastreabilidade e robusta.

---

#### Criterio L-3: Licoes ordenadas por impacto narrativo

**Veredicto: [x] ATENDIDO**

**Evidencia:** A Fase 10 (Etapa 3) justifica a ordenacao como "Escada Provocativa" em 3 movimentos:

1. **Movimento 1 (L1-L2):** O SISTEMA FALHOU — acessivel, confortavel.
2. **Movimento 2 (L3-L5):** NINGUEM ERROU — desconfortavel, remove o vilao.
3. **Movimento 3 (L6-L8):** VOCE ESTA LA DENTRO — pessoal, espelho final.

No roteiro final, esta progressao e respeitada: L1-L2 integradas na SEQ 14 (consequencias), L3-L5 no climax (SEQ 13) e transicoes, L6-L8 nas SEQ 15-17 (resolucao). A escala de provocacao e crescente e culmina no espelho do epilogo.

---

#### Criterio L-4: "E Voce?" com tom adequado

**Veredicto: [x] ATENDIDO**

**Evidencia:** O "E Voce?" (Call to Action) aparece na SEQ 17 (Epilogo) com tom preciso:

> "Voce nao e Carlisle. Provavelmente nao esta projetando navios nem certificando avioes. Mas voce ESTA dentro de um sistema."

> "Na proxima reuniao em que alguem disser 'acho que isso pode dar errado' — observe o que acontece."

> "O mar nao mudou. A pergunta e: e voce?"

O tom e:
- **Nao moralizante** — nao diz "mude o mundo," diz "olhe para o seu."
- **Nao pessimista** — nao diz "estamos condenados," diz "observe."
- **Convite, nao ordem** — transfere responsabilidade sem culpar.
- **Tom Cameron nos mergulhos** — calmo, preciso, respeitoso.

O checklist interno confirma (criterio #17): "Call to Action nao e moralizante — e convite."

---

#### Criterio L-5: Sugestoes visuais para ao menos 3 licoes

**Veredicto: [x] ATENDIDO**

**Evidencia:** TODAS as 8 licoes tem sugestoes visuais detalhadas na Fase 10, e o roteiro final as implementa:

| Licao | Visual no roteiro |
|-------|--------------------|
| L1 | Split-screen triplo (Merchant Shipping Act / Titanic / FAA) — implementado na SEQ 15 como grafismo comparativo |
| L2 | Justaposicao ouro Ato I como ironia cromatica — implementado na SEQ 14 (ouro subexposto nos inqueritos) |
| L3 | Swiss Cheese com 5 rostos calmos — implementado na SEQ 13 |
| L4 | Triptico das Vozes Silenciadas — implementado na SEQ 12 |
| L5 | Time-lapse drift 18 anos — implementado na SEQ 13 e referenciado na SEQ 08 (grafismo navios vs regra) |
| L6 | Sequencia em dois tempos (progresso → Eastland) — implementado na SEQ 15 |
| L7 | Grades entre decks com sombras de prisao — implementado na SEQ 09 |
| L8 | Espelho + fade para wreck — implementado na SEQ 17 |

8 de 8 licoes com visual implementado, muito acima do minimo de 3.

---

#### Criterio L-6: Paralelos contemporaneos concretos

**Veredicto: [x] ATENDIDO**

**Evidencia:** Os paralelos contemporaneos sao concretos, nomeados e com fontes verificaveis:

| Paralelo | Dados concretos | Fonte verificavel |
|----------|----------------|-------------------|
| Boeing 737 MAX | 346 mortos (Lion Air + Ethiopian). MCAS certificado pela propria Boeing. FAA delegou | Transportation Committee Report, 2020 |
| Grenfell Tower | 72 mortos. Revestimento ACM inflamavel. Moradores alertaram desde 2013 | Grenfell Tower Inquiry, 2019-2024 |
| SS Eastland | 848 mortos. Botes adicionais pos-Titanic causaram instabilidade | Registro historico verificado |
| Crise financeira 2008 | CDOs, CDS, subprime. Glass-Steagall revogado 1999. Lehman Brothers | Financial Crisis Inquiry Commission, 2011 |
| Deepwater Horizon | 11 mortos. Maior vazamento de petroleo dos EUA | National Commission Report, 2011 |
| TSMC/semicondutores | 90% dos chips avancados. Uma fabrica, uma ilha | Multiplas fontes (BIS, industria) |
| Derivativos globais | ~600 trilhoes em valor nocional | BIS Annual Report 2024 |

Todos os paralelos sao verificaveis com fontes primarias. Nao ha paralelos inventados ou genericos.

---

## STEP 3: VERIFICACAO DE VETO CONDITIONS

---

#### Veto 1: NAO conclui "erro humano" como causa

**Veredicto: [x] PASS**

**Evidencia:** O roteiro explicitamente rejeita "erro humano" como causa em multiplos pontos:

- SEQ 12, VO Cameron: "Nenhum desses decisores planejou matar 1.517 pessoas. Cada um fez o que parecia certo."
- SEQ 13, VO Cameron: "Dekker chamou de Local Rationality. Cada decisor agia racionalmente dentro do seu contexto. Ninguem errou."
- SEQ 13: "O Titanic NUNCA foi seguro. O sistema existia para afirmar que era."
- Frase-climax: "O Titanic nao foi destruido por um iceberg. Foi destruido por 18 anos de decisoes razoaveis."

A causa e identificada como SISTEMICA (cultura patologica, drift, Swiss Cheese, pressupostos basicos) em todos os momentos-chave. Nenhum individuo e tratado como vilao. Ismay e "produto do sistema." Smith "fazia o que todos faziam." Phillips "seguia as regras do sistema." Board of Trade "seguia a lei vigente." O veto e integralmente respeitado.

---

#### Veto 2: Fontes verificaveis presentes

**Veredicto: [x] PASS**

**Evidencia:** O roteiro referencia fontes verificaveis ao longo do texto:

- **Foecke/McCarty (NIST/JHU):** Analise metalurgica de rebites recuperados, publicada em estudos academicos
- **Pergunta 21370 do inquerito britanico:** Transcricao de Carlisle
- **Inquerito americano (senador Smith):** Citacao direta: "Laxity of regulation..."
- **Inquerito britanico (Lord Mersey):** Citacao: "He was doing what other skilled men would have done"
- **Transportation Committee Report, 2020** (Boeing MAX)
- **Grenfell Tower Inquiry, 2019-2024**
- **Financial Crisis Inquiry Commission, 2011**
- **BIS Annual Report 2024**
- **Dados historicos verificaveis:** SOLAS 1914, SS Eastland 1915, International Ice Patrol

Todas as afirmacoes factuais sao rastrevaeis a fontes primarias ou secundarias verificaveis.

---

#### Veto 3: Analise SST integrada (nao apenas citada)

**Veredicto: [x] PASS**

**Evidencia:** Ja extensamente documentado nos criterios RF-1 e E-8. A SST e o MOTOR narrativo do documentario, nao uma citacao. O Swiss Cheese e a estrutura visual do climax. O drift e o arco do Ato II inteiro. Local Rationality e a logica de cada personagem. O arco cromatico de Schein (artefatos → pressupostos) e mapeado na transicao Ouro → P&B. Westrum e DEMONSTRADO pelo arco do silenciamento. A SST serve a narrativa, nao o contrario.

---

#### Veto 4: Nenhum reenactment pretende ser "verdade"

**Veredicto: [x] PASS**

**Evidencia:** O roteiro define 3 niveis de reconstituicao e os aplica rigorosamente:

| Nivel | Descricao | Uso |
|-------|-----------|-----|
| N1 — Simbolico | Apenas superficies, objetos, close em documentos | Board of Trade, inqueritos |
| N2 — Fragmentado | Maos, silhuetas, dessaturacao 60-65%, grain | Andrews, Carlisle, Ismay na sala de projetos |
| N3 — Estilistico | Construcao completa mas com marcadores de artificio (dessaturacao, dutch angle, iluminacao expressionista) | Ninho-de-corvo, sala Marconi, grades, Californian |

Nenhuma reconstituicao pretende ser naturalista. Todas carregam marcadores visuais explicitos de que sao reconstituicoes: dessaturacao, camera lenta, silhuetas sem rosto identificavel, close em maos (nao em rostos completos), grain de filme. A decisao moral sobre o Eastland (foto mantida em sepia, NAO colorizada) demonstra consciencia etica. A SEQ 09 (grades entre decks) mostra "figuras humanas" com rostos parcialmente visiveis, nunca identificaveis. O veto e integralmente respeitado.

---

## STEP 4: VERIFICACAO DO PRINCIPIO UNIFICADOR

### Triangulacao: MOSTRA + ESCONDE + IGNORA

---

#### MOSTRA (Storaro) o que o sistema ESCONDE (Reason)

**Verificacao: CONFIRMADO**

O arco cromatico funciona como revelacao visual do que o sistema oculta:

- **Ouro Edwardiano (Ato I):** MOSTRA a fachada do progresso que ESCONDE a fragilidade (rebites baratos, botes insuficientes).
- **Cinza Aco (Ato II):** A cor drena a medida que as camadas sao reveladas. O sistema perde sua fachada.
- **P&B puro (Ato III, climax):** Toda cor e removida. A ESTRUTURA (Swiss Cheese) e revelada sem emocao — pura compreensao.
- **SEQ 07 (sala Marconi):** O ambar e uma ARMADILHA cromatica — parece calor, e pressao. MOSTRA a claustrofobia que o sistema ESCONDE sob "eficiencia."
- **SEQ 09:** Split cromatico — MESMO navio em DUAS temperaturas. A cor MOSTRA a segregacao que o sistema ESCONDE sob "regulamentacao sanitaria."

A filosofia visual de Storaro ("luz e cor como linguagem, nao decoracao") e implementada como revelacao das camadas de Reason. Cada mudanca cromatica corresponde a uma camada do Swiss Cheese sendo exposta.

---

#### O que a investigacao tradicional IGNORA (Dekker)

**Verificacao: CONFIRMADO**

O roteiro ataca explicitamente as narrativas tradicionais que a investigacao convencional privilegia:

- **"O iceberg afundou o Titanic"** → IGNORADO. O roteiro mostra que o iceberg explorou fraquezas PRE-EXISTENTES (rebites frageis, costuras rebitadas).
- **"O capitao errou"** → IGNORADO. Smith e tratado como Local Rationality — fazia o que TODOS faziam.
- **"Ismay e o vilao"** → IGNORADO. Ismay e "produto do sistema," nao antagonista.
- **"Stanley Lord e culpado"** → IGNORADO pela narrativa convencional como Second Victim; o roteiro o reconhece como vitima do sistema.
- **"A solucao e mais botes"** → IGNORADO pelo Eastland. A fix sem entendimento sistemico cria NOVO desastre.

A investigacao Dekkeriana substitui "quem errou?" por "como fazia sentido para cada decisor agir como agiu?" — e essa e a espinha dorsal do Ato II inteiro.

---

#### O que a historia EXPLICA (Larson/Lord)

**Verificacao: CONFIRMADO**

O contexto historico funciona como substrato da analise sistemica:

- **Era Edwardiana como ecossistema:** A fe na tecnologia nao e anedota — e o pressuposto basico (Schein Nivel 3) que permeia todas as decisoes.
- **Hierarquia de classe:** Nao e "cor local" — e a CAUSA da mortalidade diferenciada. A historia EXPLICA por que as grades existiam (regulamentacao de imigracao) e como se tornaram barreiras letais.
- **Corrida transatlantica (White Star vs Cunard):** EXPLICA a pressao comercial que silenciou Carlisle e reduziu botes.
- **Cultura de deferencia britanica:** EXPLICA o inquerito de Lord Mersey (captura regulatoria).

O contexto historico nao e decorativo — e causal.

---

#### O que a cultura NORMALIZA (Hopkins/Schein/Westrum)

**Verificacao: CONFIRMADO**

A cultura de seguranca e o nivel mais profundo da analise:

- **Schein Nivel 3 (pressupostos basicos):** "Somos grandes demais para falhar" — nunca articulado, respirado por todos. Explicitado no climax pelo VO de Cameron.
- **Westrum (cultura patologica):** Score 6/25. "Quem traz ma noticia e o problema." DEMONSTRADO pelo arco Carlisle-Andrews-Phillips (SEQ 04-07-12).
- **Hopkins (5 indicadores em FALHA):** Mapeados nos personagens e complicacoes. Indicador #1 (reportabilidade) = Carlisle/Andrews. #2 (compromisso gestao) = Board of Trade. #4 (prioridade seguranca) = luxo vs botes. #5 (comunicacao) = grades 3a classe.
- **Reason (4 subculturas em FALHA):** Reporting = SEQ 07/12. Just = Carlisle silenciado. Learning = Eastland/SEQ 15. Flexible = Phillips/sistema Marconi.

A cultura NORMALIZAVA a fragilidade ao ponto de torna-la INVISIVEL. O roteiro MOSTRA essa normalizacao atraves do arco cromatico (ouro como anestesia), das reconstituicoes (decisoes "razoaveis" filmadas em tom quotidiano) e da progressao das complicacoes (cada revelacao surpreende o publico mas era "normal" para os decisores).

---

#### O que a engenharia MATERIALIZA (Foecke/McCarty)

**Verificacao: CONFIRMADO**

A materialidade tecnica e central e nao e abstrata:

- **Rebites de ferro forjado com escoria >3%:** O "DNA do desastre" — SEQ 02 (semente), SEQ 06 (revelacao parcial), SEQ 11 (revelacao completa). Microscopia real no NIST. Objeto fisico manuseado por Foecke em camera.
- **Anteparas construidas um deck abaixo do proposto:** Decisao que Andrews alertou e foi overruled. Materializada na reconstituicao (mao apagando linha, SEQ 03).
- **Davits Welin com capacidade para 48 botes, 20 instalados:** A engenharia TINHA a solucao. A decisao IMPEDIU a implementacao.
- **Distribuicao aco (centro) vs ferro (proa/popa):** Mapeada em CGI. Zona de impacto COINCIDE com zona de ferro. O mapa fala.
- **Custo: <0.3% do navio para rebites de aco em toda a extensao:** "Centavos por passageiro" — o dado mais devastador do documentario.

A engenharia nao e contexto — e EVIDENCIA FORENSE. Foecke e McCarty sao os forenses que ouviram o que o casco tinha a dizer 86 anos depois.

---

### Veredicto do Principio Unificador

A triangulacao MOSTRA + ESCONDE + IGNORA + EXPLICA + NORMALIZA + MATERIALIZA e verificavel em TODAS as 17 sequencias do roteiro. O principio nao e declarado — e PRATICADO. Cada sequencia opera simultaneamente em multiplos niveis: visual (Storaro), narrativo (McKee/Bernard), analitico (Dekker/Reason), cultural (Hopkins/Schein/Westrum) e tecnico (Foecke/McCarty). O principio unificador e robusto.

---

## STEP 5: VEREDICTO FINAL

---

```
╔══════════════════════════════════════════════════════════════╗
║           QUALITY GATE — ROTEIRO FINAL                       ║
║                                                              ║
║  Veredicto:  APROVADO                                        ║
║                                                              ║
║  Criterios:  21/21 atendidos (20 plenos + 1 parcial*)        ║
║  Vetos:      4/4 PASS (zero violacoes)                       ║
║  Principio:  VERIFICADO (5/5 eixos confirmados)              ║
║                                                              ║
║  * RF-2 parcial: discrepancia de 1 min na soma de duracoes   ║
║    (89 min verificado vs 90 min declarado). Nao compromete   ║
║    aprovacao — correcao trivial.                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

### Feedback Detalhado

#### Pontos Fortes (o que funciona excepcionalmente bem)

1. **Integracao SST-Narrativa:** Este e o maior trunfo do roteiro. Os frameworks SST nao sao citados como autoridade academica — sao PRATICADOS como linguagem cinematografica. O Swiss Cheese de Reason e set piece visual. O drift de Dekker e arco temporal. Local Rationality e construcao de personagem. Schein e arco cromatico. Esta integracao e rara e sofisticada.

2. **Arco cromatico como linguagem:** A progressao Ouro → Cinza → Verde → P&B → Azul-Preto nao e decorativa — e epistemologica. Cada mudanca de cor corresponde a uma mudanca de compreensao do espectador. A decisao de ir a P&B total no climax e radical e justificada: "quando voce remove a cor, voce remove a emocao — e voce ve o SISTEMA."

3. **Silencio como recurso dramatico:** Os silencios marcados (3, 5, 7, 10 segundos) nas entrevistas sao uma decisao corajosa e Morrisiana. O silencio de 10 segundos de Foecke apos "centavos por passageiro" e potencialmente o momento mais poderoso do documentario inteiro.

4. **Licoes como tecido, nao como lista:** As 8 licoes da Fase 10 estao distribuidas organicamente nas SEQ 14-17. Nenhuma e apresentada como "Licao #N." Todas emergem do fluxo narrativo. A escada provocativa (conforto → desconforto → espelho) e preservada.

5. **Circularidade estrutural:** Mar abre, mar fecha. Azul abre, azul fecha. Mesmos sons, significado transformado. O espectador regressa ao ponto de partida mas com 90 minutos de compreensao acumulada. A circularidade e tecnica narrativa de alto nivel.

6. **Reconstituicoes eticas:** O sistema de 3 niveis (N1 simbolico, N2 fragmentado, N3 estilistico) garante que nenhuma cena pretende ser "verdade." A decisao de manter a foto do Eastland em sepia (nao colorizar) demonstra consciencia etica exemplar.

7. **Escala das complicacoes:** As 5 complicacoes progressivas (Avisos → Botes → Classe → Californian → DNA) seguem ordem crescente de profundidade (superfice → raiz), espelhando as camadas de Reason. Cada complicacao complica a anterior e prepara a revelacao do climax.

#### Ressalvas Menores (nao impeditivas)

1. **Discrepancia aritmetica (1 min):** A soma das duracoes das 17 SEQs da 89 minutos, nao 90. Na secao de Validacoes, o Ato III e declarado como 24 min, mas a soma das SEQs 13-17 da 23 min (7+5+4+4+3). Recomendacao: atribuir 1 minuto adicional a uma sequencia de transicao (sugestao: SEQ 13 de 7 para 8 min, dada a complexidade do climax) ou declarar 89 min como duracao total.

2. **Entrevistado #5 ("Especialista em Seguranca Moderna — a definir"):** O roteiro referencia este entrevistado em SEQ 14, 15 e 16 como ponte para o presente. O nome e perfil ainda estao como "a definir." Recomendacao: definir o casting deste entrevistado na fase de pre-producao, assegurando que seja alguem com credencial academica E experiencia pratica em safety science (sugestoes: Sidney Dekker, Nancy Leveson, Erik Hollnagel, Drew Rae).

3. **Musica composta (2 min):** O roteiro e quase inteiramente sem musica composta (99% silencio + som ambiente + som pratico), exceto ~2 minutos na transicao SOLAS/Eastland (SEQ 15). Esta e uma escolha corajosa e coerente. A ressalva e que a "musica ascendente" na transicao SOLAS precisa ser cuidadosamente calibrada para nao contradizer o tom geral de austeridade sonora. Recomendacao: que a musica seja mais textura que melodia — talvez cordas em unissono, sem harmonia, como respiracao antes do corte seco para o Eastland.

#### Recomendacoes para Fase de Pre-Producao

1. Resolver a discrepancia de 1 minuto nas duracoes.
2. Definir o Entrevistado #5 (Especialista em Seguranca Moderna).
3. Testar a montagem paralela da SEQ 16 em storyboard para garantir que a rima visual (Titanic/Boeing, Carlisle/engenheiro) funciona sem narracaco explicativa.
4. Validar a disponibilidade do acervo submarino de Cameron (33 mergulhos) para as SEQs 01 e 17.
5. Alinhar com a equipe de CGI a complexidade das 15 visualizacoes tecnicas previstas na ficha tecnica.

---

### Proximo Passo

**APROVADO para producao.** O roteiro final esta pronto para avancar para a fase de pre-producao (storyboard, casting de entrevistados, locacoes, orcamento de CGI).

---

*Fase 12 — Revisao de Qualidade | @doc-chief | 2026-02-26 | APROVADO*
*Criterios avaliados: 21/21 (20 plenos + 1 parcial menor)*
*Veto conditions: 4/4 PASS*
*Principio unificador: 5/5 eixos VERIFICADOS*

> "O Titanic nao foi destruido por um iceberg. Foi destruido por 18 anos de decisoes razoaveis. Este roteiro nao conta essa historia — ele a MOSTRA."
