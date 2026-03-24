# Task: Consolidar Roteiro Final do Episodio

**Task ID:** roteiro-final-workflow
**Version:** 1.0
**Purpose:** Integrar todos os outputs do pipeline num roteiro completo
**Orchestrator:** @roteirista (com validacao do @doc-chief)
**Mode:** Autonomous (requer TODOS os outputs anteriores aprovados)
**Pre-requisitos:** Analise SST + Escaleta + Paper Edit aprovados. Guia de entrevistas e guia visual se disponiveis.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| briefing | document | Yes | Briefing original do @doc-chief |
| analise_sst | document | Yes | Analise Dekker+Reason aprovada |
| escaleta | document | Yes | Escaleta McKee+Bernard aprovada |
| paper_edit | document | Yes | Paper edit cena-a-cena |
| guia_entrevista | document | No | Guia de entrevistas do @entrevistador |
| guia_visual | document | No | Guia visual do @fotografo |
| plano_cenografia | document | No | Plano de reconstituicao do @cenografo |

---

## Steps

### Step 1: Verificar Integracao SST-Narrativa
**Acao:** Confirmar que a analise SST esta INTEGRADA na narrativa, nao apenas "mencionada":
- [ ] Revelacao sistemica (Dekker/Reason) e o CLIMAX do arco McKee
- [ ] Camadas Reason correspondem a progressive complications
- [ ] Local Rationality aparece na reconstrucao de personagens
- [ ] Drift organizacional serve como backstory/contexto
- [ ] Second Victim tem espaco na narrativa

**Output:** Checklist de integracao SST-Narrativa.
**Veto:** Se analise SST nao aparece no roteiro → REJEITAR. "Doc bonito que nao revela verdade sistemica e entretenimento, nao documentario."

### Step 2: Consolidar Roteiro por Blocos
**Acao:** Montar roteiro seguindo template:

**Bloco 1 — ABERTURA (Hook + Setup)**
- Duracao estimada
- Elementos: entrevista/arquivo/reconstituicao/VO
- Funcao narrativa
- Notas de direcao visual (se guia visual disponivel)

**Bloco 2 — DESENVOLVIMENTO (Confrontacao)**
- Sequencia de cenas do paper edit
- Turning points marcados
- Gaps identificados
- Progressive complications em ordem crescente

**Bloco 3 — CLIMAX (Revelacao Sistemica)**
- A revelacao central do episodio
- Integracao SST + narrativa no ponto de maior impacto

**Bloco 4 — RESOLUCAO (Legado)**
- Consequencias
- Reflexao
- Ponte para proximo episodio (se serie)

**Output:** Roteiro em 4 blocos estruturados.

### Step 3: Validar Proporcoes
**Acao:** Verificar proporcoes Bernard:
- Setup: ~25% do tempo total
- Confrontacao: ~50%
- Resolucao: ~25%
- VO: <= 40% do tempo total

**Output:** Calculo de proporcoes com ajustes se necessario.

### Step 4: Rodar Checklist Final
**Acao:** Executar `checklists/qualidade-roteiro.md` completo.
**Output:** Resultado do checklist com APROVADO/REPROVADO.

### Step 5: Formatar Roteiro Completo
**Acao:** Gerar roteiro final conforme `templates/roteiro-episodio-tmpl.md`.
**Output:** Documento final formatado.

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Analise SST nao integrada no climax | VETO — nao e roteiro doc-safety | "O principio unificador exige que o doc REVELE a verdade sistemica" |
| Proporcao dos atos desbalanceada (>10% de desvio) | AVISO — rebalancear | "All setup and no confrontation fails structurally" (Bernard) |
| VO > 40% | VETO — redesenhar | Bernard |
| Roteiro nao responde a questao dramatica | VETO — revisar resolucao | "O final deve responder (mesmo que de forma aberta)" |
| Roteiro conclui "erro humano" como causa | VETO — refazer integracao SST | Dekker: "Erro humano e o ponto de partida, nao a conclusao" |

---

## Output Format

Referencia: `templates/roteiro-episodio-tmpl.md`

---

## Completion Criteria

1. SST integrada no climax (nao apenas mencionada)
2. 4 blocos estruturados com duracao estimada
3. Proporcoes Bernard respeitadas (25/50/25)
4. VO <= 40%
5. Checklist qualidade-roteiro APROVADO
6. Questao dramatica respondida (mesmo que abertamente)
7. Principio unificador verificavel: MOSTRA + ESCONDE + IGNORA
