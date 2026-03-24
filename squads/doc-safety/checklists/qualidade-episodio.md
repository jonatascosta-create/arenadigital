# Checklist de Qualidade — Episodio Completo

> Squad doc-safety | Checklist v1.0 | Avaliacao end-to-end do pipeline de 12 fases

---

## Instrucoes de Uso

- Executar pelo @doc-chief na fase 12 (Revisao QA) do pipeline
- Avalia o episodio COMPLETO, nao uma fase individual (use `qualidade-roteiro.md` para o roteiro)
- Cada item: [x] ATENDIDO, [ ] NAO ATENDIDO, [!] PARCIAL
- **Veto conditions** bloqueiam aprovacao independente dos outros criterios

---

## A. PIPELINE — COMPLETUDE DAS FASES

| Fase | Agente | Entregue? | Quality Gate | Notas |
|------|--------|-----------|-------------|-------|
| 1. Briefing | @doc-chief | [ ] | {APROVADO/REVISAO/REJEITADO} | |
| 2. Contexto Historico | @historiador | [ ] | {status} | |
| 3. Analise SST | @perito-sst | [ ] | {status} | |
| 4. Analise Tecnica | @engenheiro-naval | [ ] | {status} | |
| 5. Cultura de Seguranca | @especialista-cultura-seguranca | [ ] | {status} | |
| 6. Estrutura Narrativa | @roteirista | [ ] | {status} | |
| 7. Guia de Entrevistas | @entrevistador | [ ] | {status} | |
| 8. Direcao Visual | @fotografo | [ ] | {status} | |
| 9. Cenografia | @cenografo | [ ] | {status} | |
| 10. Roteiro Final | @roteirista | [ ] | {status} | |
| 11. Licoes Aprendidas | @especialista-cultura-seguranca | [ ] | {status} | |
| 12. Revisao QA | @doc-chief | [ ] | — | |

**Fases completas:** {X}/12

---

## B. QUALITY GATES POR FASE (VETO SECTION)

> Cada fase tem criterios minimos. Um veto em qualquer fase bloqueia aprovacao do episodio.

### B1. Briefing (@doc-chief)
- [ ] Acidente especifico com data, local e vitimas
- [ ] Falha sistemica provavel identificada
- [ ] Personagens mapeados
- [ ] Pipeline definido (completo ou reduzido)
- [ ] Diretor (estilo) definido

### B2. Contexto Historico (@historiador)
- [ ] 6 dimensoes analisadas (politica, economia, tecnologia, classe, zeitgeist, ponte)
- [ ] Fontes verificaveis citadas
- [ ] **[VETO]** Historia NAO e decorativa — removivel sem perda = VETO
- [ ] Ponte presente-passado clara

### B3. Analise SST (@perito-sst)
- [ ] Timeline do operador reconstruida sem hindsight
- [ ] Knowledge state mapeado por momento critico
- [ ] Pressoes sistemicas identificadas com evidencia
- [ ] Drift organizacional rastreado
- [ ] **[VETO]** 3+ camadas Reason mapeadas (active + latent)
- [ ] **[VETO]** Conclusao NAO e "erro humano"
- [ ] Recomendacoes sistemicas (nao "treinar melhor")
- [ ] Second Victim considerado

### B4. Analise Tecnica (@engenheiro-naval)
- [ ] 4 dominios tecnicos abordados
- [ ] Mapa custo vs seguranca
- [ ] **[VETO]** Detalhes tecnicos conectados a decisoes humanas
- [ ] Traducao documental (tecnico → acessivel)

### B5. Cultura de Seguranca (@especialista-cultura-seguranca)
- [ ] Classificacao Westrum (patologica/burocratica/generativa)
- [ ] Hopkins 5 indicadores avaliados
- [ ] Schein 3 niveis analisados (artefatos, valores, pressupostos)
- [ ] **[VETO]** Classificacao com evidencias concretas (nao generica)

### B6. Estrutura Narrativa (@roteirista)
- [ ] Controlling idea formulada (valor + causa)
- [ ] 5 beats McKee com value-charge definido
- [ ] Minimo 3 gaps identificados
- [ ] **[VETO]** Negacao da Negacao atingida no climax
- [ ] Questao dramatica formulada
- [ ] 3 atos Bernard com proporcao ~25/50/25
- [ ] Teste do Trem: zero estacoes mortas
- [ ] **[VETO]** Analise SST integrada na escaleta

### B7. Guia de Entrevistas (@entrevistador)
- [ ] Estrategia por perfil de entrevistado
- [ ] Tecnicas Morris aplicadas (Interrotron, silencio, confronto gentil)
- [ ] **[VETO]** Perguntas NAO sao genericas — especificas ao caso e personagem
- [ ] Reenactment planejado (se aplicavel)

### B8. Direcao Visual (@fotografo)
- [ ] Arco cromatico Storaro definido
- [ ] Paleta vinculada a beats narrativos
- [ ] **[VETO]** Cor como linguagem narrativa (nao apenas estetica)
- [ ] Visualizacoes tecnicas planejadas

### B9. Cenografia (@cenografo)
- [ ] Nivel de reconstituicao definido (simbolico/fragmentado/estilistico)
- [ ] Props-evidencia identificados
- [ ] **[VETO]** Reconstituicao NAO pretende ser verdade — e versao (Morris)
- [ ] Cenografia documental planejada

### B10. Roteiro Final (@roteirista)
- [ ] **[VETO]** SST integrada no climax (nao apenas mencionada)
- [ ] 4 blocos estruturados com duracao estimada
- [ ] Proporcoes Bernard respeitadas (~25/50/25)
- [ ] **[VETO]** VO <= 40%
- [ ] Questao dramatica respondida (mesmo que abertamente)

### B11. Licoes Aprendidas (@especialista-cultura-seguranca)
- [ ] Minimo 5 licoes
- [ ] Cada licao: mecanismo + exemplo + aplicacao + pergunta
- [ ] Paralelo contemporaneo para cada licao
- [ ] **[VETO]** Licoes NAO sao genericas — especificas ao caso

---

## C. INTEGRACAO ENTRE AGENTES

> O valor do pipeline esta na integracao — cada fase alimenta a proxima.

- [ ] SST do @perito-sst alimenta a escaleta do @roteirista
- [ ] Contexto do @historiador enriquece o roteiro (nao e apendice)
- [ ] Analise tecnica do @engenheiro-naval aparece nas progressive complications
- [ ] Cultura do @especialista-cultura-seguranca fundamenta o climax
- [ ] Escaleta do @roteirista guia entrevistas do @entrevistador
- [ ] Escaleta guia paleta visual do @fotografo
- [ ] Guia visual do @fotografo guia cenografia do @cenografo
- [ ] Licoes do @especialista-cultura-seguranca integradas no ATO III

---

## D. PRINCIPIO UNIFICADOR — TRIANGULACAO

| Dimensao | Agente Responsavel | Presente no Roteiro? | Evidencia |
|----------|-------------------|---------------------|----------|
| MOSTRA (visual) | @fotografo + @cenografo | [ ] | {como} |
| ESCONDE (sistema) | @perito-sst (Reason) | [ ] | {como} |
| IGNORA (investigacao) | @perito-sst (Dekker) | [ ] | {como} |
| EXPLICA (historia) | @historiador | [ ] | {como} |
| NORMALIZA (cultura) | @especialista-cultura-seguranca | [ ] | {como} |
| MATERIALIZA (engenharia) | @engenheiro-naval | [ ] | {como} |

---

## E. COERENCIA DO DIRETOR

| Criterio | Status |
|----------|--------|
| Estilo do diretor ({DIRETOR}) consistente ao longo do episodio | [ ] |
| Impacto do diretor visivel em: entrevistas, visual, cenografia | [ ] |
| Tom narrativo coerente com o perfil do diretor | [ ] |

---

## F. ANTI-PATTERNS (nenhum deve estar presente)

- [ ] NAO e documentario-palestra (Bernard: "You are not making an illustrated lecture")
- [ ] NAO culpa individuo (Dekker: "Human error is the starting point, not the conclusion")
- [ ] Visual NAO e generico (Storaro: cor como linguagem, nao decoracao)
- [ ] Entrevistas NAO sao superficiais (Morris: provocar verdade)
- [ ] Pipeline NAO foi executado fora de ordem
- [ ] Reconstituicao NAO pretende ser verdade

---

## RESULTADO

| Secao | Atendidos | Total | % |
|-------|----------|-------|---|
| A. Completude | {X} | 12 | {X}% |
| B. Quality Gates | {X} | {total} | {X}% |
| C. Integracao | {X} | 8 | {X}% |
| D. Principio | {X} | 6 | {X}% |
| E. Diretor | {X} | 3 | {X}% |
| F. Anti-patterns | {X} | 6 | {X}% |

**Vetos violados:** {0 / lista com detalhes}

### Veredicto

| Resultado | Condicao |
|-----------|----------|
| **APROVADO** | Todas fases completas + 0 vetos + integracao verificada |
| **REVISAO** | >80% criterios + 0 vetos + issues menores listados |
| **REJEITADO** | <80% criterios OU veto violado OU integracao falha |

**Veredicto final:** {APROVADO / REVISAO / REJEITADO}

**Feedback especifico:**
{Lista de correcoes obrigatorias, se houver}

**Proximo passo:**
{Avancar para publicacao / Devolver para {agente} com {feedback}}

---

*Checklist: qualidade-episodio v1.0 | Squad doc-safety*
*Pipeline: 12 fases | 9 agentes | Avaliacao end-to-end*
