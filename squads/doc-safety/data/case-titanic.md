# Case Study: RMS Titanic — Analise Sistemica para Pipeline doc-safety

> **Gerado por:** @pedro-valerio (integracao), @perito-sst (Dekker+Reason), @roteirista (McKee+Bernard)
> **Pesquisa:** @oracle (especialistas e fontes verificaveis)
> **Data:** 2026-02-25
> **Objetivo:** Validar agentes Lote A + servir de referencia para episodios futuros

---

## 1. Ficha do Caso

| Campo | Valor |
|-------|-------|
| Evento | Naufragio do RMS Titanic |
| Data | 14-15 abril 1912 |
| Local | Atlantico Norte, 41°46'N 50°14'W |
| Vitimas | ~1.500 mortos (de ~2.224 a bordo) |
| Tipo | Desastre maritimo — falha sistemica multipla |
| Principio unificador | O doc MOSTRA o que o sistema ESCONDE e o que a investigacao IGNORA |

---

## 2. Especialistas Reais

### 2.1 Investigadores da Epoca

| Especialista | Papel | Contribuicao | Lente |
|---|---|---|---|
| **Sen. William Alden Smith** | Presidente inquerito americano (1912) | Culpou Board of Trade: "laxity of regulation and hasty inspection." Condenou Capitao Lord. 82 testemunhas, 18 dias. | Regulacao / Accountability |
| **Lord Mersey** | Presidente inquerito britanico (1912) | "Excessive speed" mas NAO culpou Smith: "he was doing what other skilled men would have done." 96 testemunhas, 36 dias, 25.622 perguntas. | Local Rationality (avant la lettre) |
| **Thomas Andrews** | Projetista-chefe (Harland & Wolff) | Propôs bulkheads mais altas + mais botes. Overruled. Morreu no naufragio. | Second Victim / Voz ignorada |
| **Alexander Carlisle** | Projetista original (H&W) | Propôs 48 botes com novos davits Welin. Lord Pirrie vetou por estetica. Aposentou-se. | Whistleblower silenciado |
| **Edward Wilding** | Engenheiro naval (H&W) | Testemunhou que bulkheads sem cap no topo foram fator critico. | Design como latent condition |

### 2.2 Historiadores e Pesquisadores Modernos

| Especialista | Papel | Obra-Chave | Perspectiva Unica |
|---|---|---|---|
| **Walter Lord** (1917-2002) | Historiador | *A Night to Remember* (1955) | Narrativa definitiva. Entrevistou sobreviventes. Bernard diria: "paper edit perfeito." |
| **Dr. Robert Ballard** | Oceanografo (Woods Hole) | Descobriu wreck (1985) | Prova fisica: navio partiu em dois. Missao secreta US Navy (USS Thresher/Scorpion). |
| **James Cameron** | Cineasta/explorador | *Titanic* (1997), *Ghosts of the Abyss* (2003), *The Final Word* (2012) | 33 mergulhos, 60%+ do interior mapeado. Combina narrativa + rigor tecnico. |
| **Daniel Allen Butler** | Historiador maritimo | *Unsinkable* (1998, NYT bestseller) | Analise psicologica do Capitao Smith. WaPo: "the best narrative." |
| **Don Lynch + Ken Marschall** | Historiador + artista visual | *Titanic: An Illustrated History* (1992) | Marschall: visual historian do filme de Cameron, 6 mergulhos ao wreck. |
| **Parks Stephenson** | Analista de sistemas | Expedicoes com Cameron (2002+) | Primeiro CGI preciso das salas Marconi. Analise forense moderna. |
| **John P. Eaton + Charles Haas** | Historiadores | *Titanic: Triumph and Tragedy* | Cronica detalhada. Fundaram Titanic International Society (1989). |
| **Paul Louden-Brown** | Historiador White Star | *The White Star Line: An Illustrated History* | Contexto corporativo e de negocios. |

### 2.3 Especialistas Forenses

| Especialista | Instituicao | Descoberta | Impacto |
|---|---|---|---|
| **Dr. Tim Foecke** | NIST | Teoria dos rebites (1998): ferro forjado com excesso de escoria na proa/popa | Resident pathogen LITERAL — decisao de custo que enfraqueceu a estrutura |
| **Dr. Jennifer Hooper McCarty** | Johns Hopkins | Primeira analise completa da metalurgia dos rebites (tese doutorado) | Rebites com >3% escoria estouraram sob impacto — casco abriu nas costuras |
| **Tim Maltin** | Pesquisador independente | Teoria da refracao atmosferica | Condicoes atmosfericas criaram miragem que atrasou avistamento do iceberg |

---

## 3. Analise Dekker (New View) — 5 Etapas

### Etapa 1: Timeline

| Hora | Evento | Knowledge State do Ator |
|------|--------|------------------------|
| 14/04 09:00 | Primeiro aviso de gelo (Caronia) | Smith SABIA: gelo na rota |
| 14/04 13:42 | Aviso do Baltic | Ismay GUARDOU no bolso |
| 14/04 19:30 | Aviso do Californian: "three large bergs" | Ponte recebeu |
| 14/04 21:40 | Aviso do Mesaba: "heavy pack ice" | NUNCA chegou a ponte — operador ocupado |
| 14/04 22:00 | Vigias sem binoculos | Sabiam: noite sem lua, mar calmo — pior condicao |
| 14/04 23:39 | Fleet: "Iceberg, right ahead!" | 37 segundos para impacto |
| 14/04 23:40 | Murdoch: "Hard a-starboard" + "Full astern" | Desacelerar REDUZIU eficacia do leme |
| 15/04 00:05 | Ordem: preparar botes | 20 botes para 2.224 pessoas |
| 15/04 00:45 | Bote 7 baixado: 28 pessoas (capacidade 65) | Tripulacao SEM treinamento de evacuacao |
| 15/04 02:20 | Titanic afunda | Californian a ~10 mi — radio desligado |

### Etapa 2: Local Rationality

| Ator | Acao "errada" | Por que fazia sentido NO MOMENTO |
|------|--------------|--------------------------------|
| Capitao Smith | Manter 22.5 nos em zona de gelo | Pratica NORMAL. Todos os capitaes faziam. Pressao de Ismay. "Inafundavel." |
| Operador Phillips | Nao repassar aviso do Mesaba | Sobrecarregado com telegramas de passageiros. Avisos eram rotina. |
| Vigias Fleet/Lee | Sem binoculos | Trancados desde Southampton. Blair (que tinha a chave) remanejado. |
| 1° Oficial Murdoch | "Full astern" | Instinto correto em navio menor. Ninguem treinado para 46.000 ton. |
| Capitao Lord (Californian) | Nao respondeu sinais | "Fogos festivos." Operador Marconi tinha ido dormir (permitido). |

**Dekker:** *"Underneath every simple story about 'human error,' there is a deeper story about the organization."*

### Etapa 3: Pressoes Sistemicas

- **Comercial:** Ismay a bordo — pressao implicita por chegada pontual (competicao Cunard)
- **Cultural:** "Navios modernos sao inafundaveis" — crenca civilizacional
- **Organizacional:** Operadores Marconi empregados da MARCONI COMPANY, nao da White Star
- **Classe social:** Botes de 1a classe acessiveis; 3a classe com portoes trancados
- **Material:** Rebites de ferro forjado com escoria (Foecke/McCarty) — custo sobre qualidade

### Etapa 4: Drift Organizacional (18 anos)

```
1894: Board of Trade define regra de botes para navios ate 10.000 ton

1890s: Navios crescem para 20.000 ton
       Regra NAO atualizada → "afinal, navios sao mais seguros"

1900s: Navios chegam a 30.000 ton
       Regra AINDA de 1894 → nenhum desastre grande → "sistema funciona"

1907: White Star encomenda Olympic-class (46.000 ton)
      Carlisle propoe 48 botes → Pirrie veta → Carlisle aposenta-se
      DAVITS instalados com capacidade para 48 — mas so 20 botes colocados

1911: Olympic (navio-irmao) colide com HMS Hawke
      Licoes herdadas pelo Titanic? NAO.

1912: Titanic zarpa com 20 botes (1.178 lugares) para 2.224 pessoas
      Board of Trade: "CONFORME regulamentacao" ← regra de 18 anos antes

CADA PASSO era "apenas um pouquinho" diferente do anterior.
```

### Etapa 5: Mudancas Sistemicas (pos-desastre)

| Mudanca | Tipo | Camada Reason |
|---------|------|---------------|
| SOLAS 1914 | Regulamentacao maritima global | Regulacao |
| Botes para 100% dos passageiros | Redesenho obrigatorio | Organizacao |
| International Ice Patrol (US Coast Guard) | Monitoramento permanente | Supervisao |
| Radio 24h obrigatorio | Comunicacao continua | Supervisao |
| Exercicios de evacuacao obrigatorios | Treinamento | Pre-condicoes |
| Foguetes como sinal de socorro exclusivo | Protocolo padrao | Regulacao |

**IRONIA SISTEMICA — O SS Eastland (1915):**
Apos Titanic, mais botes foram obrigatorios. O SS Eastland — ja instavel — capotou no rio Chicago pelo peso extra dos botes. 848 mortos. Dekker: "A fix que ataca o sintoma sem entender o sistema cria NOVO desastre."

---

## 4. Mapa Reason (Swiss Cheese) — 5 Camadas

```
CAMADA 5: REGULACAO
  Board of Trade: regra de 1894 para navio de 1912
  Rule 12: compartimentos "reduzem" necessidade de botes (loophole)
  Captura regulatoria: inquerito britanico leniente com Board of Trade
  BURACO: Regulacao obsoleta + loophole + auto-regulacao

CAMADA 4: ORGANIZACAO (White Star + Harland & Wolff)
  Ismay: pressao comercial por velocidade
  Pirrie: vetou 48 botes por estetica do deck
  H&W: rebites de ferro forjado com escoria na proa (custo/prazo)
  Andrews: propôs bulkheads mais altas — overruled
  Marconi: operadores empregados da Marconi, nao da White Star
  BURACO: Decisoes comerciais > seguranca em CADA nivel

CAMADA 3: SUPERVISAO
  Smith: ultima viagem, modo rotina
  Sem protocolo formal para avisos de gelo
  Exercicio de evacuacao CANCELADO (14/04 manha)
  Binoculos trancados — ninguem escalou
  BURACO: "Business as usual" em condicoes excepcionais

CAMADA 2: PRE-CONDICOES
  Noite sem lua, mar calmo (sem ondas no gelo)
  Vigias sem binoculos
  Phillips sobrecarregado (mandou Californian "calar a boca")
  Tripulacao sem treinamento de evacuacao
  Rebites frageis na proa (latent condition fisica)
  BURACO: Pior combinacao possivel de condicoes

CAMADA 1: ATO INSEGURO (Active Failures)
  Smith manteve 22.5 nos (pratica normal da era)
  Phillips nao repassou aviso do Mesaba
  Murdoch: "full astern" reduziu manobrabilidade
  Botes lancados com 40-60% de capacidade
  BURACO: Erros na linha de frente — todos racionais no contexto
```

**Trajetoria:** Todos os buracos se alinharam as 23:40 de 14 de abril. A regra de 1894 dormiu 18 anos como resident pathogen ate combinar com active failures de uma noite sem lua.

---

## 5. Estrutura Narrativa (McKee + Bernard)

### Controlling Idea

"Vidas sao destruidas quando uma era inteira normaliza a arrogancia tecnologica e o lucro silencia sistematicamente as vozes que alertam sobre o perigo."

### Escaleta McKee (5 Beats)

| Beat | Conteudo | Valor-Charge | Gap |
|------|----------|-------------|-----|
| 1. Vida Normal | Belfast 1909-1912. A construcao. "Nem Deus afunda." | Positivo (progresso) | Expectativa: tecnologia venceu natureza |
| 2. Inciting Incident | 23:40 — 37 segundos. Metal rasgando. 6 compartimentos (projetado para 4). Andrews: "2 horas." | Negativo (perigo) | Resultado: natureza nunca foi vencida |
| 3. Progressive Comp. | 20 botes para 2.224. Exercicio cancelado. Avisos ignorados. Binoculos trancados. Regra de 1894. Rebites frageis. Californian a 10 milhas. | Negativo crescente | "Como isso foi permitido?" |
| 4. Climax | NAO foi o iceberg. Foi Carlisle silenciado. Board of Trade carimbando "CONFORME." 18 anos de drift. Rebites baratos. Arrogancia civilizacional. | Negacao da negacao | "O iceberg nao afundou o Titanic. O sistema afundou." |
| 5. Resolution | SOLAS 1914. Ice Patrol. 1.500 mortos para aprender o que Carlisle ja sabia em 1907. E a ironia do Eastland. | Ambiguo | O Titanic mudou o mar. E o chao de fabrica? |

### Negacao da Negacao

```
Seguranca    → Risco       → Negligencia      → Negligencia normalizada
("inafundavel") (gelo na rota) (20 botes/2224)   como CIVILIZACAO INDUSTRIAL

Verdade      → Duvida      → Mentira           → Mentira como PARADIGMA
(avisos)       (sao muitos?)  (Ismay no bolso)    (Board of Trade certifica regra de 18 anos)
```

### Estrutura Bernard (3 Atos)

```
ATO I — SETUP (25%)
  Hook: O som do metal rasgando. Escuridao. Gritos.
  Contexto: Belfast 1909-1912. Construcao. Orgulho.
  Personagens: Andrews, Carlisle, Ismay, Smith, Phillips, Fleet
  Questao Dramatica: "Como 1.500 morreram num navio inafundavel?"

ATO II — CONFRONTACAO (50%)
  Complicacao 1: Carlisle propôs 48 botes → cortaram para 20
  Complicacao 2: Board of Trade: "conforme" regra de 1894
  Complicacao 3: Phillips mandou Californian calar a boca (10 min antes)
  Complicacao 4: Rebites frageis — decisao de custo (Foecke/McCarty)
  Reversal: Chave dos binoculos — Blair levou consigo
  Ponto de virada: Calculo de Andrews: "2 horas"

ATO III — RESOLUCAO (25%)
  Revelacao: Swiss Cheese — 5 camadas, 18 anos de drift
  SOLAS 1914 + Ice Patrol
  As vozes ignoradas: Carlisle morreu sem ver recomendacoes aceitas
  Ironia: Eastland — a "fix" matou 848
  Ponte: "E os Titanics do chao de fabrica?"
```

---

## 6. Documentarios de Referencia

| Documentario | Ano | Abordagem | Relevancia doc-safety |
|---|---|---|---|
| *A Night to Remember* (docudrama) | 1958 | Cronologico, multiplos personagens | Modelo Bernard: paper edit classico |
| *Secrets of the Titanic* (NatGeo) | 1987 | Expedicao Ballard — descoberta do wreck | Prova fisica como turning point |
| *Ghosts of the Abyss* (Cameron) | 2003 | IMAX 3D + CGI sobre decay | Storaro: visual como narrativa |
| *Titanic: The Final Word* (Cameron) | 2012 | "Cold case" forense — re-analise | Reason: Swiss Cheese em acao |
| *Titanic: The Digital Resurrection* (NatGeo) | 2025 | Digital twin 3D (715.000 imagens) | Tecnologia mais recente |

---

## 7. Valor como Case-Study para doc-safety

| Dimensao | Por que o Titanic funciona | Aplicacao SST |
|---|---|---|
| Drift | 18 anos de regra obsoleta | Normas NR desatualizadas no Brasil |
| Whistleblower | Carlisle alertou, foi ignorado | Trabalhador que reporta risco e punido |
| Resident Pathogen | Rebites frageis DENTRO da estrutura | EPI inadequado DENTRO do processo |
| Local Rationality | Smith fazia o que todos faziam | Operador segue pratica normalizada |
| Negacao da Negacao | "Inafundavel" como crenca civilizacional | "Sempre fizemos assim" como cultura |
| Fix que mata | Eastland: mais botes → capotou | Solucoes reativas sem analise sistemica |
| Second Victim | Capitao Lord viveu perseguido ate morrer | Operador envolvido vira bode expiatorio |

---

*Case study gerado pelo pipeline doc-safety (doc-chief + perito-sst + roteirista + oracle)*
*Fontes primarias: Inqueritos britanico/americano (1912), NIST, JHU, Encyclopedia Titanica*
*1.500 vidas para que o mundo aprendesse. Quantos "Titanics" acontecem todo dia no chao de fabrica?*
