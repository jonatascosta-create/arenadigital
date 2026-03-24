# Roteiro — {TITULO_EPISODIO}

> Squad doc-safety | Template v1.0 | Roteiro Completo do Episodio

---

## Metadados do Episodio

| Campo | Valor |
|-------|-------|
| Titulo | {TITULO_EPISODIO} |
| Caso | {DESCRICAO_CASO} |
| Data do acidente | {DATA} |
| Local | {LOCAL} |
| Vitimas | {NUMERO_VITIMAS} |
| Diretor (estilo) | {DIRETOR} |
| Duracao estimada | {MINUTOS} min |
| Controlling Idea | "{VALOR} e {destruido/preservado} quando {CAUSA}" |
| Questao Dramatica | "{PERGUNTA}" |
| Status | DRAFT / EM REVISAO / APROVADO |

---

## Fontes do Pipeline

| Fase | Agente | Status | Referencia |
|------|--------|--------|-----------|
| 1. Briefing | @doc-chief | {status} | {ref} |
| 2. Contexto Historico | @historiador | {status} | {ref} |
| 3. Analise SST | @perito-sst | {status} | {ref} |
| 4. Analise Tecnica | @engenheiro-naval | {status} | {ref} |
| 5. Cultura de Seguranca | @especialista-cultura-seguranca | {status} | {ref} |
| 6. Escaleta | @roteirista | {status} | {ref} |
| 7. Guia Entrevistas | @entrevistador | {status} | {ref} |
| 8. Guia Visual | @fotografo | {status} | {ref} |
| 9. Cenografia | @cenografo | {status} | {ref} |

---

## Principio Unificador

> O documentario **MOSTRA** (Storaro) o que o sistema **ESCONDE** (Reason),
> o que a investigacao tradicional **IGNORA** (Dekker),
> o que a historia **EXPLICA** (Larson/Lord),
> o que a cultura **NORMALIZA** (Hopkins/Schein/Westrum),
> e o que a engenharia **MATERIALIZA** (Foecke/McCarty).

---

## BLOCO 1 — ABERTURA (Hook + Setup) | ~25% | {DURACAO} min

### Cena 1.1 — Hook
| Campo | Conteudo |
|-------|----------|
| Tipo | {entrevista / arquivo / reconstituicao / VO / misto} |
| Conteudo | {Descricao da cena de abertura — primeiros 2 min} |
| Funcao narrativa | Capturar publico — plantar questao dramatica |
| Elementos visuais | {paleta, enquadramento, movimento — ref guia visual} |
| Audio | {som ambiente, musica, silencio} |
| Notas de direcao | {estilo do diretor aplicado} |

### Cena 1.2 — Contexto
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {A empresa, o setor, a epoca, a rotina — ref contexto historico} |
| Funcao narrativa | Estabelecer mundo "normal" pre-acidente |
| Fonte historica | {Ref @historiador — dimensoes relevantes} |
| Elementos visuais | {paleta — ref guia visual} |
| Audio | {audio} |

### Cena 1.3 — Personagens
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Vitima(s), familia, colegas — humanizacao} |
| Funcao narrativa | Criar empatia — stakes pessoais |
| Tecnica de entrevista | {Ref @entrevistador — qual tecnica Morris} |
| Elementos visuais | {paleta — ref guia visual} |

### Turning Point → Ato II
> {Evento/revelacao que transiciona para a confrontacao}

---

## BLOCO 2 — DESENVOLVIMENTO (Confrontacao) | ~50% | {DURACAO} min

### Cena 2.1 — O Acidente
| Campo | Conteudo |
|-------|----------|
| Tipo | {reconstituicao / arquivo / entrevista / misto} |
| Conteudo | {Reconstrucao do acidente — timeline Dekker} |
| Funcao narrativa | Inciting Incident — value-charge muda de positivo a negativo |
| Fonte SST | Timeline do operador (Dekker Etapa 1) |
| Cenografia | {Ref @cenografo — nivel de reconstituicao} |
| Elementos visuais | {paleta — mudanca cromatica} |

### Cena 2.2 — Progressive Complication #1
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Primeira revelacao — camada superficial} |
| Funcao narrativa | Complicacao — o quadro piora |
| Fonte SST | Reason Camada {N} — {tipo de falha} |
| Gap | Expectativa: {X} → Resultado: {Y} |
| Elementos visuais | {paleta} |

### Cena 2.3 — Progressive Complication #2
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Segunda revelacao — camada mais profunda} |
| Funcao narrativa | Complicacao crescente |
| Fonte SST | Reason Camada {N} — {tipo de falha} |
| Gap | Expectativa: {X} → Resultado: {Y} |

### Cena 2.4 — Progressive Complication #3
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Terceira revelacao — mais profunda ainda} |
| Funcao narrativa | Complicacao maxima antes do climax |
| Fonte SST | Reason Camada {N} — {tipo de falha} |

### Cena 2.5 — Reversal
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Testemunha-chave muda depoimento / evidencia emerge} |
| Funcao narrativa | Ponto de virada — o que se sabia e insuficiente |
| Tecnica de entrevista | {Ref @entrevistador — qual tecnica Morris} |

### Cena 2.6 — Analise Tecnica
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Detalhes tecnicos que conectam a decisoes humanas} |
| Funcao narrativa | Materializar a falha — engenharia como evidencia |
| Fonte tecnica | {Ref @engenheiro-naval — dominio relevante} |
| Elementos visuais | {Visualizacoes tecnicas — ref guia visual} |

### Turning Point → Ato III
> {Revelacao que leva diretamente ao climax}

---

## BLOCO 3 — CLIMAX (Revelacao Sistemica) | transicao | {DURACAO} min

### Cena 3.1 — A Revelacao
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {NAO foi "erro humano" — foi falha organizacional sistematizada} |
| Funcao narrativa | CLIMAX — Negacao da Negacao atingida |
| Fonte SST | Drift organizacional (Dekker Etapa 4) + Latent Conditions (Reason Camada 4) |
| Cultura | {Ref @especialista-cultura-seguranca — classificacao Westrum + insights} |
| Value-Charge | Negacao da Negacao: {valor especifico} |
| Elementos visuais | {Pico do arco cromatico — ref guia visual} |

### Cena 3.2 — Second Victim (se aplicavel)
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {O operador envolvido tambem e vitima — dimensao humana} |
| Funcao narrativa | Complexidade emocional — nao ha vilao simples |
| Fonte SST | Dekker — Second Victim |

---

## BLOCO 4 — RESOLUCAO (Legado) | ~25% | {DURACAO} min

### Cena 4.1 — Consequencias
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Consequencias legais, regulatorias, humanas} |
| Funcao narrativa | O que aconteceu DEPOIS |

### Cena 4.2 — Reflexao
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {O que mudou (ou nao) no setor / na regulacao} |
| Funcao narrativa | Avaliar impacto real — mudanca ou estagnacao? |

### Cena 4.3 — Licoes Aprendidas
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Licoes com mecanismo + exemplo + aplicacao contemporanea + pergunta} |
| Funcao narrativa | Conclusao — ponte para o presente |
| Fonte | {Ref @especialista-cultura-seguranca — licoes aprendidas} |
| Formato por licao | Mecanismo → Exemplo historico → Aplicacao hoje → Pergunta ao publico |

### Cena 4.4 — Legado / Encerramento
| Campo | Conteudo |
|-------|----------|
| Tipo | {tipo} |
| Conteudo | {Impacto duradouro — familias, industria, memoria} |
| Funcao narrativa | Fechar o arco — responder questao dramatica (mesmo que abertamente) |
| Elementos visuais | {Resolucao do arco cromatico — ref guia visual} |

---

## Proporcoes Finais (Bernard)

| Ato | % Previsto | % Real | Duracao | Status |
|-----|-----------|--------|---------|--------|
| I — Setup | 25% | {X}% | {min} | {OK / AJUSTAR} |
| II — Confrontacao | 50% | {X}% | {min} | {OK / AJUSTAR} |
| III — Resolucao | 25% | {X}% | {min} | {OK / AJUSTAR} |
| **Total** | 100% | 100% | {min} | — |
| Voice-Over | <=40% | {X}% | {min} | {OK / EXCEDE} |

---

## Integracao SST → Narrativa (Checklist Obrigatorio)

- [ ] Revelacao sistemica (Dekker/Reason) e o CLIMAX do arco McKee
- [ ] Camadas Reason correspondem a progressive complications
- [ ] Local Rationality aparece na reconstrucao de personagens
- [ ] Drift organizacional serve como backstory/contexto
- [ ] Second Victim tem espaco na narrativa
- [ ] Conclusao NAO e "erro humano"
- [ ] Licoes aprendidas integradas no ATO III

---

## Triangulacao — Principio Unificador

| Dimensao | Verificacao | Status |
|----------|------------|--------|
| MOSTRA (Storaro) | {Como o visual conta a historia?} | [ ] |
| ESCONDE (Reason) | {Quais camadas de defesa falharam?} | [ ] |
| IGNORA (Dekker) | {O que a investigacao tradicional nao viu?} | [ ] |
| EXPLICA (Larson/Lord) | {Qual contexto historico esclarece?} | [ ] |
| NORMALIZA (Hopkins/Schein/Westrum) | {Como a cultura permitiu?} | [ ] |
| MATERIALIZA (Foecke/McCarty) | {Como a engenharia evidencia?} | [ ] |

---

## Notas de Producao

**Diretor ({DIRETOR}) — impacto no estilo:**
{Como o estilo do diretor molda o roteiro}

**Material necessario:**
- [ ] {Entrevistas a realizar}
- [ ] {Material de arquivo a obter}
- [ ] {Reconstituicoes a planejar}
- [ ] {Locacoes a visitar}
- [ ] {Peritos a consultar}

**Riscos de producao:**
- {risco 1}
- {risco 2}

---

*Template: roteiro-episodio-tmpl v1.0 | Squad doc-safety*
*Pipeline: 12 fases | 9 agentes | Principio unificador integrado*
