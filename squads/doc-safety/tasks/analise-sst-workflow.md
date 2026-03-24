# Task: Analise de Seguranca do Trabalho

**Task ID:** analise-sst-workflow
**Version:** 1.0
**Purpose:** Decompor acidente de trabalho usando Dekker (New View, 5 etapas) + Reason (Swiss Cheese, 5 camadas)
**Orchestrator:** @perito-sst
**Mode:** Autonomous (a partir do briefing do @doc-chief)

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| briefing | document | Yes | Briefing estruturado do @doc-chief |
| materiais | list | No | Laudos, relatorios, testemunhos, fotos |

---

## Steps

### Step 1: Reconstruir Timeline do Operador (Dekker Etapa 1)
**Acao:** Mapear segundo a segundo o que o operador fez, viu, ouviu e comunicou. NAO o que "deveria" ter feito — o que REALMENTE fez.
**Output:** Timeline factual sem julgamento, documentando cada acao e informacao disponivel.
**Criterio:** A timeline e boa quando voce consegue "entrar no tunel" do operador.
**Fonte DNA:** Dekker, Local Rationality Principle.

### Step 2: Mapear Knowledge State (Dekker Etapa 2)
**Acao:** Para cada decisao na timeline: que informacao o operador TINHA? NAO TINHA? Era AMBIGUA?
**Output:** Mapa de knowledge state por momento critico — separando hindsight de foresight.
**Criterio:** Elimina todas as afirmacoes "ele deveria ter percebido que..." (hindsight bias).
**Veto parcial:** Se a analise usa informacao posterior para julgar decisao do momento → reescrever.

### Step 3: Identificar Pressoes Sistemicas (Dekker Etapa 3)
**Acao:** Rastrear pressoes organizacionais: prazo, custo, producao, fadiga, treinamento inadequado, equipamento, cultura.
**Output:** Lista de pressoes com evidencia (politicas, metas, turnos, historico).
**Criterio:** Revela o "campo de forcas" que empurrou o operador para aquela acao.

### Step 4: Rastrear Drift Organizacional (Dekker Etapa 4)
**Acao:** Investigar historico de degradacao gradual. Procedimentos "adaptados"? Excecao virou regra?
**Output:** Linha do tempo de drift mostrando normalizacao de desvios incrementais.
**Criterio:** Cada passo individualmente parecia razoavel, mas trajetoria acumulada era perigosa.
**Fonte DNA:** Dekker, Drift into Failure + Diane Vaughan, Normalization of Deviance.

### Step 5: Mapear Swiss Cheese — 5 Camadas (Reason)
**Acao:** Decompor o acidente nas 5 camadas de defesa:

| Camada | O que Investigar | Perguntas-Chave |
|--------|-----------------|-----------------|
| 1. Ato Inseguro | O que o operador fez/nao fez | Slip, lapse, mistake ou violation? |
| 2. Pre-condicoes | Fadiga, pressao, ambiente, estado mental | Por que vulneravel NAQUELE momento? |
| 3. Supervisao | Presenca, eficacia, ferramentas | A supervisao funcionou como barreira? |
| 4. Organizacao | Decisoes de gestao, cultura, recursos | Quais latent conditions foram criadas? |
| 5. Regulacao | Normas, fiscalizacao, lacunas | A regulacao cobria a situacao? |

**Output:** Mapa de 5 camadas com buracos identificados (active failure vs latent condition).
**Criterio:** Para cada camada, identificar se o buraco era temporario (active) ou permanente (latent).

### Step 6: Propor Mudancas Sistemicas (Dekker Etapa 5)
**Acao:** Em vez de "treinar melhor" ou "punir": redesenho de barreiras, redundancias, processo, incentivos.
**Output:** Lista de recomendacoes que atacam causas SISTEMICAS, nao sintomas individuais.
**Criterio:** As recomendacoes tornam o SISTEMA mais seguro, independente de quem opera.

### Step 7: Compilar Analise SST Completa
**Acao:** Integrar todos os outputs num documento unico seguindo template.
**Output:** Analise SST formatada conforme `templates/analise-acidente-tmpl.md`.

---

## Veto Conditions

| Condition | Action | Reason |
|-----------|--------|--------|
| Conclusao final e "erro humano" | VETO — reabrir analise | "Human error is not the conclusion. It is the starting point." (Dekker) |
| Menos de 3 camadas Reason mapeadas | VETO — analise incompleta | "Nearly all adverse events involve a combination of active failures and latent conditions" (Reason) |
| Timeline usa informacao posterior para julgar | VETO — reescrever sem hindsight | "What looks like negligence in hindsight looked reasonable at the time" (Dekker) |
| Recomendacoes sao apenas "treinar melhor" | VETO — propor redesenho sistemico | "Punishing people does not fix the system" (Dekker) |
| Second Victim nao mencionado | AVISO — incluir dimensao humana | O operador envolvido tambem e vitima |

---

## Output Format

Referencia: `templates/analise-acidente-tmpl.md`

---

## Completion Criteria

1. Timeline do operador reconstruida sem julgamento retrospectivo
2. Knowledge state mapeado por momento critico
3. Pressoes sistemicas identificadas com evidencia
4. Drift organizacional rastreado com linha do tempo
5. 5 camadas Reason mapeadas com classificacao active/latent
6. Recomendacoes sistemicas (nao punitivas)
7. Conclusao final NAO e "erro humano"
