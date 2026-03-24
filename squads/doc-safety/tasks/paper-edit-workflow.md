# Task: Montar Paper Edit

**Task ID:** paper-edit-workflow
**Version:** 1.0
**Purpose:** Criar paper edit cena-a-cena a partir da escaleta e materiais disponiveis
**Orchestrator:** @roteirista
**Mode:** Autonomous (requer escaleta aprovada)
**Pre-requisito:** Escaleta aprovada pelo @doc-chief

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| escaleta | document | Yes | Escaleta McKee+Bernard aprovada |
| transcricoes | list | No | Transcricoes de entrevistas |
| arquivos | list | No | Material de arquivo (fotos, videos, documentos) |
| analise_sst | document | Yes | Analise Dekker+Reason para referencia |

---

## Steps

### Step 1: Inventariar Elementos Narrativos
**Acao:** Listar TODOS os elementos disponiveis:
- Entrevistas (transcritas ou planejadas)
- Arquivos visuais (fotos, videos, documentos)
- Dados/estatisticas
- Reconstituicoes planejadas
- Narracao (voice-over)

Para cada elemento classificar: "avanca a historia" ou "informa mas nao avanca."
**Output:** Tabela de elementos com classificacao.
**Criterio:** Pelo menos 60% devem "avancar a historia." Se menos, falta material narrativo.

### Step 2: Sequenciar Cenas
**Acao:** Para cada cena da escaleta, definir:

| Campo | Descricao |
|-------|-----------|
| Numero da cena | Sequencial |
| Ato + beat | Ex: "Ato II, Beat 3" |
| Minuto estimado | Ex: "12-16 min" |
| Tipo | Entrevista, arquivo, reconstituicao, VO, misto |
| Fonte | Que material especifico usa |
| Funcao narrativa | Que papel na historia (progressive complication, turning point, etc.) |
| Informacao | O que o publico aprende |
| Avanca o trem? | SIM/NAO — se NAO, cortar ou reposicionar |
| Turning point | Momento onde valor muda na cena |
| Value-charge | De que para que (ex: negativo → negativo crescente) |
| VO necessario? | SIM/NAO — se SIM, justificar |
| Transicao | Como conecta com proxima cena |

**Output:** Tabela de sequenciamento cena-a-cena.

### Step 3: Balancear Voice-Over
**Acao:** Calcular proporcao de VO no paper edit.
- Contar cenas com VO vs sem VO
- Estimar tempo de VO vs tempo total
- Se VO > 40%: identificar cenas onde VO pode ser substituido por entrevista ou imagem

**Output:** Proporcao de VO com ajustes se necessario.
**Veto:** VO > 40% do tempo total → redesenhar.

### Step 4: Verificar Checklist Bernard
**Acao:** Rodar checklist de qualidade narrativa (ver `checklists/qualidade-roteiro.md`):
- Questao dramatica clara?
- Hook captura nos primeiros 2 min?
- Personagens com desejo e stakes?
- Conflito com forca antagonista?
- Entrevistas avancam o trem?
- 3 atos proporcionais?

**Output:** Checklist com status por item.

### Step 5: Compilar Paper Edit Final
**Acao:** Gerar documento final com todas as cenas sequenciadas.
**Output:** Paper edit formatado.

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Menos de 60% elementos "avancam a historia" | VETO — falta material narrativo | Bernard: "Every element must earn its place" |
| VO > 40% do tempo total | VETO — redesenhar distribuicao | Bernard: "If narration dominates, you're telling, not showing" |
| Cena sem turning point no Ato II | AVISO — revisar | McKee: "If nothing changes, nothing happens" |
| Paper edit parece palestra ao ler em voz alta | VETO — reescrever | Bernard: "You are not making an illustrated lecture" |

---

## Output Format

Documento estruturado com tabela cena-a-cena (ver Step 2).

---

## Completion Criteria

1. Todos os elementos inventariados e classificados
2. Sequenciamento cena-a-cena completo
3. VO <= 40% do tempo total
4. Checklist Bernard rodado
5. Zero cenas que "nao avancam o trem"
