# Analise Tecnica — Workflow

> **Agente:** @engenheiro-naval | **Elicit:** true | **Output:** Analise tecnica em 4 dominios

## Pre-requisitos
- Briefing estruturado do @doc-chief (OBRIGATORIO)
- Analise SST do @perito-sst (OBRIGATORIO — identifica onde decisoes org viraram falhas tecnicas)

## Etapas

### Etapa 1: Mapeamento Construtivo
**Input:** Briefing + analise SST
**Acao:** Documentar como o sistema/estrutura foi construido
- Quem construiu? Quando? Com que recursos?
- Quais decisoes construtivas foram tomadas?
- Existiram alternativas rejeitadas? Por quem? Por que?
**Output:** Mapa de decisoes construtivas com fontes

### Etapa 2: Analise de Materiais
**Acao:** Investigar qualidade e adequacao dos materiais
- Que materiais foram usados? Eram os melhores disponiveis?
- Existem evidencias forenses sobre falha de material?
- Decisoes de custo influenciaram escolha de material?
**Output:** Analise de materiais com conexao a falhas
**Elicit:** "Nivel de profundidade tecnica? (a) Acessivel — focado em decisoes, (b) Tecnico — inclui dados metalurgicos/forenses"

### Etapa 3: Analise de Projeto (Design)
**Acao:** Identificar limitacoes de design e decisoes de trade-off
- Quais limitacoes de projeto existiam?
- Quem sabia dessas limitacoes?
- Foram propostas melhorias? Foram vetadas?
- Custo vs seguranca: mapear cada decisao
**Output:** Tabela "Custo vs Seguranca" com decisoes, opcoes, razoes, consequencias

### Etapa 4: Forense Moderna
**Acao:** Compilar evidencias forenses que validam/refutam narrativas
- Que investigacoes modernas existem?
- Que tecnologias foram usadas (mergulhos, CGI, metalurgia)?
- O que as evidencias modernas revelam que nao se sabia na epoca?
**Output:** Lista de evidencias forenses com impacto na narrativa

### Etapa 5: Traduzir para Documentario
**Acao:** Para cada achado tecnico, produzir:
- Versao "escala humana" (comparacao tangivel)
- Versao "decisao como personagem" (quem decidiu, consequencia)
- Versao "ironia reveladora" (quando aplicavel)
**Output:** Guia de traducao tecnica para linguagem documental

### Etapa 6: Consolidar Analise
**Output final:** Documento com 4 dominios + mapa custo vs seguranca + guia de traducao

## Quality Gate (doc-chief valida)
- [ ] 4 dominios analisados com fontes
- [ ] Mapa "Custo vs Seguranca" com minimo 3 decisoes mapeadas
- [ ] Cada detalhe tecnico conectado ao desastre (nao e aula de engenharia)
- [ ] Traducao para linguagem documental (escala humana, comparacoes)
- [ ] Evidencias forenses modernas compiladas

## Handoff
→ Para @roteirista: detalhes tecnicos traduzidos para linguagem narrativa
→ Para @fotografo: guia de visualizacao tecnica (o que precisa CGI, infografico)
