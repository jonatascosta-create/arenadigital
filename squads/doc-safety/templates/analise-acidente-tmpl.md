# Analise de Acidente — {TITULO_CASO}

> Squad doc-safety | Template v1.0 | Dekker (New View) + Reason (Swiss Cheese)

---

## Metadados

| Campo | Valor |
|-------|-------|
| Caso | {DESCRICAO_CASO} |
| Data do acidente | {DATA} |
| Local | {LOCAL} |
| Setor / Industria | {SETOR} |
| Vitimas | {NUMERO_VITIMAS — mortos, feridos} |
| Tipo de acidente | {explosao, queda, esmagamento, intoxicacao, etc.} |
| Briefing recebido de | @doc-chief |
| Autor | @perito-sst |
| Status | DRAFT / EM REVISAO / APROVADO |

---

## PARTE 1: ANALISE DEKKER — NEW VIEW

### Etapa 1: Timeline do Operador

> Mapear segundo a segundo o que o operador fez, viu, ouviu e comunicou.
> NAO o que "deveria" ter feito — o que REALMENTE fez.

| Hora | Acao do Operador | O que via/ouvia | Comunicacao | Nota |
|------|-----------------|----------------|-------------|------|
| {HH:MM} | {acao} | {info sensorial} | {com quem, sobre o que} | {contexto} |
| {HH:MM} | {acao} | {info sensorial} | {comunicacao} | {contexto} |
| {HH:MM} | **{MOMENTO DO ACIDENTE}** | — | — | — |

**Criterio de qualidade:** A timeline e boa quando se consegue "entrar no tunel" do operador — entender por que cada acao fazia sentido NAQUELE momento.

---

### Etapa 2: Knowledge State (Mapa de Informacao)

> Para cada decisao critica: que informacao o operador TINHA? NAO TINHA? Era AMBIGUA?

| Momento Critico | Informacao DISPONIVEL | Informacao INDISPONIVEL | Informacao AMBIGUA |
|----------------|----------------------|------------------------|-------------------|
| {decisao 1} | {o que sabia} | {o que nao sabia} | {o que era confuso} |
| {decisao 2} | {o que sabia} | {o que nao sabia} | {o que era confuso} |

**Hindsight bias eliminado?**
- [ ] Nenhuma afirmacao "ele deveria ter percebido que..." permanece
- [ ] Toda avaliacao usa apenas informacao disponivel NO MOMENTO

---

### Etapa 3: Pressoes Sistemicas

> Rastrear o "campo de forcas" que empurrou o operador para aquela acao.

| Pressao | Evidencia | Origem | Intensidade |
|---------|----------|--------|-------------|
| Producao/prazo | {meta, deadline, cobranca} | {quem decidiu} | {alta/media/baixa} |
| Custo | {corte de orcamento, economia} | {quem decidiu} | {alta/media/baixa} |
| Fadiga | {horas trabalhadas, turnos, pausas} | {escala, politica} | {alta/media/baixa} |
| Treinamento | {inadequado, desatualizado, ausente} | {RH, gestao} | {alta/media/baixa} |
| Equipamento | {defeituoso, inadequado, improvisado} | {manutencao, orcamento} | {alta/media/baixa} |
| Cultura | {"nao parar a linha", "sempre foi assim"} | {organizacional} | {alta/media/baixa} |

---

### Etapa 4: Drift Organizacional

> Degradacao gradual das margens de seguranca. Cada passo parecia razoavel; a trajetoria era perigosa.

| Periodo | O que mudou | Parecia razoavel porque | Risco acumulado |
|---------|-----------|------------------------|----------------|
| {X meses atras} | {mudanca 1} | {justificativa na epoca} | {baixo} |
| {X meses atras} | {mudanca 2} | {justificativa na epoca} | {medio} |
| {X meses atras} | {mudanca 3} | {justificativa na epoca} | {alto} |
| {momento do acidente} | {acumulo final} | — | {critico} |

**Normalizacao de desvio identificada?**
- [ ] Excecao virou regra?
- [ ] "Sempre foi assim" sem incidente reforçou crenca de seguranca?
- [ ] Desvio formalizado informalmente?

---

### Etapa 5: Mudancas Sistemicas Propostas

> NAO "treinar melhor" ou "punir". Redesenhar o SISTEMA.

| # | Recomendacao | Camada que ataca | Tipo | Prazo |
|---|-------------|-----------------|------|-------|
| 1 | {redesenho de barreira, redundancia, processo} | {organizacao/supervisao/regulacao} | {preventiva/mitigadora} | {imediato/curto/medio} |
| 2 | {recomendacao} | {camada} | {tipo} | {prazo} |
| 3 | {recomendacao} | {camada} | {tipo} | {prazo} |

**Criterio:** As recomendacoes tornam o SISTEMA mais seguro, independente de quem opera.

---

## PARTE 2: MAPA REASON — SWISS CHEESE (5 Camadas)

### Camada 1: Ato Inseguro (Active Failure)

| Campo | Conteudo |
|-------|----------|
| O que o operador fez/nao fez | {descricao factual} |
| Classificacao | {slip / lapse / mistake / violation (routine/situational/exceptional)} |
| Ma intencao? | {NAO — violation ≠ ma intencao. Investigar POR QUE procedimento foi violado.} |
| Buraco na defesa | {qual barreira falhou nesta camada} |

---

### Camada 2: Pre-condicoes

| Fator | Status | Evidencia |
|-------|--------|----------|
| Fadiga | {presente/ausente} | {horas de trabalho, turno, pausas} |
| Estado mental | {normal/alterado} | {estresse, pressao, distracao} |
| Pressao de tempo | {presente/ausente} | {meta, deadline, cobranca} |
| Ambiente fisico | {adequado/inadequado} | {iluminacao, ruido, temperatura} |
| Treinamento | {adequado/inadequado} | {ultimo treinamento, conteudo} |
| Experiencia | {suficiente/insuficiente} | {tempo na funcao, familiaridade} |

**Buraco na defesa:** {por que o operador estava vulneravel NAQUELE momento}

---

### Camada 3: Supervisao Inadequada

| Fator | Status | Evidencia |
|-------|--------|----------|
| Supervisor presente | {sim/nao} | {escala, local} |
| Ferramentas para detectar risco | {disponiveis/indisponiveis} | {checklists, sensores, rondas} |
| Pressao para ignorar sinais | {presente/ausente} | {meta, cultura} |
| Treinamento do supervisor | {adequado/inadequado} | {foco: producao vs seguranca} |

**Buraco na defesa:** {como a supervisao falhou como CAMADA — nao como culpa do supervisor}

---

### Camada 4: Falhas Organizacionais (Latent Conditions)

| Decisao Gerencial | Quando foi tomada | Consequencia para seguranca | Quem decidiu |
|-------------------|-------------------|----------------------------|-------------|
| {decisao 1} | {data/periodo} | {impacto na seguranca} | {nivel hierarquico} |
| {decisao 2} | {data/periodo} | {impacto} | {nivel} |
| {decisao 3} | {data/periodo} | {impacto} | {nivel} |

**Latent conditions identificadas:**
- {condicao 1 — dormente ha quanto tempo?}
- {condicao 2}

**Buraco na defesa:** {decisoes ESPECIFICAS que criaram os buracos}

---

### Camada 5: Fatores Regulatorios

| Fator | Status | Evidencia |
|-------|--------|----------|
| Norma aplicavel | {qual NR/lei} | {cobre a situacao? lacunas?} |
| Fiscalizacao | {frequencia, ultima inspecao} | {efetiva? superficial?} |
| Lacunas conhecidas | {sim/nao} | {quais, ha quanto tempo} |
| Adequacao regulatoria | {adequada/deficiente} | {norma acompanhou o risco?} |

**Buraco na defesa:** {a regulacao funcionou como defesa ou tinha buracos?}

---

### Diagrama da Trajetoria de Acidente

```
REGULACAO ──────── [buraco: {lacuna}] ────────────────────┐
                                                           │
ORGANIZACAO ────── [buraco: {latent condition}] ───────────┤
                                                           │
SUPERVISAO ─────── [buraco: {falha}] ─────────────────────┤
                                                           ├──→ ACIDENTE
PRE-CONDICOES ──── [buraco: {vulnerabilidade}] ────────────┤
                                                           │
ATO INSEGURO ───── [buraco: {active failure}] ─────────────┘

Todos os buracos se ALINHARAM → trajetoria atravessou todas as defesas.
```

---

## PARTE 3: DIMENSAO HUMANA

### Second Victim

| Campo | Conteudo |
|-------|----------|
| Operador envolvido | {quem} |
| Impacto pessoal | {psicologico, profissional, social} |
| Suporte recebido | {da empresa, do sistema, da comunidade} |
| Tratamento institucional | {apoio / abandono / punicao} |

> Dekker: "The label 'human error' is misleading and prevents discovery. The operator is not just the last link — they are also a victim."

### Just Culture — Avaliacao

| Pergunta Dekker | Resposta |
|----------------|---------|
| Quem foi ferido? | {vitimas diretas + second victims} |
| Quais sao suas necessidades? | {reparacao, reconhecimento, mudanca} |
| De quem e a obrigacao de atender? | {empresa, regulador, sociedade} |
| A resposta institucional foi restaurativa ou retributiva? | {restaurativa / retributiva / ausente} |

---

## CONCLUSAO

> **LEMBRETE CRITICO:** "Human error is not the conclusion of an investigation. It is the starting point." (Dekker)

**Causa-raiz sistemica:**
{Descricao da causa-raiz como falha ORGANIZACIONAL, nao individual}

**Sintese para roteiro:**
{Como esta analise alimenta o arco narrativo — qual revelacao vira o climax?}

**Peso narrativo por camada:**
| Camada Reason | Potencial dramatico | Recomendacao narrativa |
|--------------|--------------------|-----------------------|
| Ato Inseguro | {alto/medio/baixo} | {como usar no roteiro} |
| Pre-condicoes | {potencial} | {como usar} |
| Supervisao | {potencial} | {como usar} |
| Organizacao | {potencial} | {como usar} |
| Regulacao | {potencial} | {como usar} |

---

*Template: analise-acidente-tmpl v1.0 | Squad doc-safety*
*Frameworks: Dekker New View (5 etapas) + Reason Swiss Cheese (5 camadas)*
*Fontes: Field Guide to Human Error, Human Error (1990), Managing Risks (1997)*
