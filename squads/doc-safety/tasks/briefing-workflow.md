# Task: Processar Briefing de Episodio

**Task ID:** briefing-workflow
**Version:** 1.0
**Purpose:** Receber caso de acidente de trabalho e estruturar briefing completo para o pipeline
**Orchestrator:** @doc-chief
**Mode:** Interactive (elicit=true)

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| caso | string | Yes | Descricao do acidente de trabalho (evento, local, data, vitimas) |
| director | string | Yes | Nome do diretor que inspira o estilo cinematografico (ex: Cameron, Morris, Burns, Herzog) |
| materiais | list | No | Materiais disponiveis (laudos, fotos, testemunhos, documentos) |
| contexto | string | No | Contexto adicional (empresa, setor, historico) |

---

## Steps

### Step 1: Validar Caso
**Acao:** Verificar se o input contem um acidente de trabalho especifico com: (a) evento real, (b) data/local identificaveis, (c) vitima(s) ou quase-acidente documentado.
**Output:** Confirmacao de que o caso e valido para o pipeline.
**Veto:** Se nao ha acidente especifico (apenas tema generico como "seguranca do trabalho"), REJEITAR.

### Step 2: Diagnosticar Escopo
**Acao:** Avaliar 5 dimensoes do caso:

| Dimensao | Pergunta | Classificacao |
|----------|----------|---------------|
| Acidente especifico | Ha evento real com data, local, vitima(s)? | CLARO / VAGO / AUSENTE |
| Falha sistemica | Ha indicios de que nao foi "so erro humano"? | ALTA / MEDIA / BAIXA |
| Material disponivel | Ha laudos, testemunhos, imagens, documentos? | ABUNDANTE / PARCIAL / ESCASSO |
| Personagens | Ha vitima, familia, colegas, gestores identificaveis? | FORTE / MEDIO / FRACO |
| Conflito | Ha tensao entre versao oficial e realidade? | POTENTE / PRESENTE / AUSENTE |

**Output:** Tabela de diagnostico com classificacao por dimensao.

### Step 3: Identificar Personagens
**Acao:** Listar todos os personagens potenciais do episodio:
- Vitima(s) direta(s)
- Familiares
- Colegas de trabalho / testemunhas
- Supervisores / gestores
- Responsaveis pela empresa
- Orgaos reguladores / fiscalizadores
- Peritos / investigadores

**Output:** Lista de personagens com papel narrativo potencial.

### Step 4: Definir Pipeline Aplicavel
**Acao:** Com base no diagnostico, definir quais fases do pipeline sao aplicaveis:
- Pipeline COMPLETO (8 fases) — caso com material abundante e personagens fortes
- Pipeline REDUZIDO (5 fases) — caso com material parcial, sem entrevistas possiveis
- Pipeline MINIMO (3 fases) — caso historico, apenas analise + narrativa + roteiro

**Output:** Pipeline definido com fases e agentes responsaveis.

### Step 5: Estruturar Briefing Final
**Acao:** Compilar todos os outputs anteriores em briefing estruturado:

```
BRIEFING DO EPISODIO
====================
Caso: [titulo descritivo]
Data do acidente: [data]
Local: [local]
Vitimas: [numero e tipo]
Setor: [industria/setor]

DIAGNOSTICO:
[tabela de 5 dimensoes]

PERSONAGENS:
[lista com papeis]

PIPELINE: [COMPLETO / REDUZIDO / MINIMO]
Fases: [lista de fases aplicaveis]

ROTEAMENTO:
Proximo: @perito-sst (analise Dekker + Reason)

MATERIAIS DISPONIVEIS:
[lista do que foi fornecido]

MATERIAIS NECESSARIOS:
[lista do que falta para pipeline completo]
```

**Output:** Briefing formatado pronto para rotear para @perito-sst.

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Sem acidente especifico (apenas tema generico) | VETO — nao iniciar pipeline | "Sem evento real, nao ha historia para contar" |
| Todas as 5 dimensoes classificadas como AUSENTE/FRACO | VETO — caso insuficiente | "Material insuficiente para qualquer formato de pipeline" |
| Acidente sem indicios de falha sistemica (acidente genuinamente aleatorio) | AVISO — reavaliar com @perito-sst | "Pode haver falha sistemica nao evidente no briefing" |

---

## Output Format

Referencia: `templates/roteiro-episodio-tmpl.md` (secao de briefing)

---

## Completion Criteria

1. Briefing contem as 5 dimensoes avaliadas
2. Lista de personagens identificados (minimo 3)
3. Pipeline definido (COMPLETO/REDUZIDO/MINIMO)
4. Roteamento para proximo agente definido
5. Materiais disponiveis vs necessarios listados
