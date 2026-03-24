# Task: Criar Estrutura Narrativa do Episodio

**Task ID:** estrutura-narrativa-workflow
**Version:** 1.0
**Purpose:** Criar escaleta completa usando McKee (5 beats) + Bernard (3 atos) a partir do briefing e analise SST
**Orchestrator:** @roteirista
**Mode:** Autonomous (requer analise SST aprovada)
**Pre-requisito:** Analise SST do @perito-sst APROVADA pelo @doc-chief

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| briefing | document | Yes | Briefing do @doc-chief |
| analise_sst | document | Yes | Analise Dekker+Reason APROVADA |
| materiais | list | No | Entrevistas, arquivos, imagens disponiveis |

---

## Steps

### Step 1: Definir Controlling Idea (McKee)
**Acao:** Formular o tema central como valor + causa.
- Valor: o que esta em jogo (seguranca, justica, verdade, dignidade)
- Causa: o que produz o resultado (negligencia, normalizacao, pressao, omissao)
- Formato: "[Valor] e [destruido/preservado] quando [causa]"

**Output:** Uma frase de controlling idea com valor e causa explicitos.
**Criterio:** Deve poder ser testada — cada cena reforça ou complica essa ideia.
**Veto:** Controlling idea generica ("acidentes sao ruins") → muito vaga, precisa de causa especifica.

### Step 2: Mapear Arco em 5 Beats (McKee)
**Acao:** Distribuir material nos 5 beats usando a analise SST como base:

| Beat | Conteudo | Fonte SST |
|------|----------|-----------|
| 1. Vida Normal | Contexto pre-acidente | Briefing |
| 2. Inciting Incident | O acidente | Timeline Dekker (Step 1) |
| 3. Progressive Complications | Revelacoes progressivas | Camadas Reason (surface→deep) |
| 4. Climax | Revelacao sistemica | Drift + Latent Conditions |
| 5. Resolution | Consequencias e legado | Recomendacoes + impacto |

Para cada beat definir: value-charge (positivo/negativo/ambiguo).
**Output:** Escaleta em 5 blocos com value-charge.
**Criterio:** Cada beat muda o valor em jogo. Se nao muda, falta conflito.

### Step 3: Identificar Gaps (McKee)
**Acao:** Para cada beat, mapear expectativa do publico vs resultado real.
- Formato: "Expectativa: [X] → Resultado: [Y]"
- Minimo 3 gaps significativos por episodio.

**Output:** Lista de gaps com expectativa vs resultado.

### Step 4: Aprofundar com Negacao da Negacao (McKee)
**Acao:** Identificar a escala tematica completa:
```
POSITIVO → CONTRARIO → NEGACAO → NEGACAO DA NEGACAO
```
O climax deve atingir pelo menos "negacao da negacao."
**Output:** Escala de valores do positivo ao negativo absoluto.

### Step 5: Formular Questao Dramatica (Bernard)
**Acao:** Formular UMA pergunta que o documentario busca responder.
**Criterio:** Se respondivel com sim/nao, e fraca. Deve exigir investigacao.
**Output:** Frase interrogativa clara.

### Step 6: Construir Estrutura 3 Atos (Bernard)
**Acao:** Mapear material nos 3 atos:
- Ato I — Setup (25%): hook, contexto, personagens, questao
- Ato II — Confrontacao (50%): investigacao, complicacoes, reversals, ponto de virada
- Ato III — Resolucao (25%): revelacao, consequencias, reflexao, legado

**Output:** Escaleta em 3 atos com proporcao definida.
**Criterio:** Cada ato tem turning point claro de transicao.

### Step 7: Teste do Trem (Bernard)
**Acao:** Reler escaleta perguntando: "O trem esta andando? Em algum ponto o publico desceria?"
Identificar "estacoes mortas" — pontos sem momentum.
**Output:** Lista de estacoes mortas com solucao (corte, reposicao, ou adicao de tensao).
**Criterio:** Zero momentos onde o publico "desceria do trem."

### Step 8: Compilar Escaleta Final
**Acao:** Integrar McKee (5 beats) + Bernard (3 atos) numa escaleta unica.
**Output:** Escaleta formatada conforme `templates/escaleta-tmpl.md`.

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Sem Controlling Idea definida | VETO — Step 1 obrigatorio | "Sem controlling idea, as cenas nao tem direcao" (McKee) |
| Escaleta nao usa analise SST | VETO — integrar dados do @perito-sst | "Sem SST, o roteiro repete a narrativa oficial" |
| Climax nao atinge negacao da negacao | AVISO — aprofundar Step 4 | "O arco para no negativo simples — falta profundidade" |
| Voice-over previsto >40% | VETO — redesenhar | "If narration dominates, you're telling, not showing" (Bernard) |
| Estacao morta nao resolvida | VETO — resolver antes de avancar | "O trem parou — publico vai descer" |

---

## Output Format

Referencia: `templates/escaleta-tmpl.md`

---

## Completion Criteria

1. Controlling Idea formulada (valor + causa)
2. 5 beats McKee com value-charge definido
3. Minimo 3 gaps identificados
4. Negacao da negacao atingida no climax
5. Questao dramatica formulada (nao sim/nao)
6. 3 atos Bernard com proporcao 25/50/25
7. Teste do Trem: zero estacoes mortas
8. Analise SST integrada na escaleta
