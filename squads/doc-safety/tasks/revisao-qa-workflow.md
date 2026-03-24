# Task: Revisao de Qualidade do Episodio

**Task ID:** revisao-qa-workflow
**Version:** 1.0
**Purpose:** Revisar output de qualquer fase do pipeline e emitir veredicto
**Orchestrator:** @doc-chief
**Mode:** Interactive (apresenta veredicto e aguarda decisao)

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| artefato | document | Yes | Output da fase a ser revisada |
| fase | string | Yes | Qual fase do pipeline (briefing, analise-sst, escaleta, paper-edit, roteiro-final) |
| agente_origem | string | Yes | Qual agente produziu o output |

---

## Steps

### Step 1: Identificar Criterios da Fase
**Acao:** Carregar os completion criteria da fase correspondente:

| Fase | Criterios | Referencia |
|------|-----------|-----------|
| briefing | 5 dimensoes + personagens + pipeline | tasks/briefing-workflow.md |
| analise-sst | 7 criterios Dekker+Reason | tasks/analise-sst-workflow.md |
| escaleta | 8 criterios McKee+Bernard | tasks/estrutura-narrativa-workflow.md |
| paper-edit | 5 criterios Bernard | tasks/paper-edit-workflow.md |
| roteiro-final | 7 criterios integrados | tasks/roteiro-final-workflow.md |

**Output:** Lista de criterios aplicaveis.

### Step 2: Avaliar Cada Criterio
**Acao:** Para cada criterio, avaliar:
- [x] ATENDIDO — criterio satisfeito com evidencia
- [ ] NAO ATENDIDO — criterio nao satisfeito (detalhar o que falta)
- [!] PARCIAL — criterio parcialmente atendido (detalhar o que melhorar)

**Output:** Checklist avaliado com evidencia por item.

### Step 3: Verificar Veto Conditions
**Acao:** Checar se alguma veto condition da fase foi violada.
Se violada: REJEICAO AUTOMATICA independente dos outros criterios.
**Output:** Lista de veto conditions com status (PASS/FAIL).

### Step 4: Verificar Principio Unificador
**Acao:** Para fases de escaleta e roteiro-final, verificar triangulacao:
- O doc MOSTRA (dimensao visual/sensorial)?
- O que o sistema ESCONDE (camadas Reason)?
- O que a investigacao tradicional IGNORA (New View Dekker)?

**Output:** Avaliacao da triangulacao.

### Step 5: Emitir Veredicto
**Acao:** Com base nos steps anteriores:

| Veredicto | Condicao | Acao |
|-----------|----------|------|
| APROVADO | 100% criterios atendidos + 0 vetos violados | Avancar para proxima fase |
| REVISAO | >70% criterios + 0 vetos violados | Devolver para agente com feedback |
| REJEITADO | <70% criterios OU veto violado | Devolver com lista de correcoes obrigatorias |

**Output:** Veredicto formatado:
```
QUALITY GATE — [FASE]
Veredicto: [APROVADO / REVISAO / REJEITADO]
Criterios: [X/Y atendidos]
Vetos: [PASS / N violados]
Feedback: [lista especifica do que corrigir]
Proximo: [acao — avancar ou devolver]
```

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Artefato conclui "erro humano" como causa | REJEICAO automatica | Principio fundamental do squad |
| Artefato nao cita fontes verificaveis | AVISO — pedir citacoes | "Se nao tem [SOURCE:], nao e verificavel" |
| Roteiro nao integra analise SST | REJEICAO automatica | "Doc bonito sem verdade sistemica = entretenimento" |

---

## Output Format

Veredicto formatado (ver Step 5).

---

## Completion Criteria

1. Todos os criterios da fase avaliados
2. Veto conditions verificadas
3. Veredicto emitido com feedback especifico
4. Proximo passo definido (avancar ou devolver)
