# ROTEIRO FINAL v2 — RMS Titanic: A Arquitetura do Desastre

> Squad doc-safety | Fase 11 — Roteiro Final Consolidado v2 | McKee (5 beats) + Bernard (3 atos)
> Autor: @roteirista (squad doc-safety) | Data: 2026-03-06
> Apresentadora: Andreza Araujo (squad andreza-araujo) | Squad Creator: @oalanicolas, @thiago-finch, @pedro-valerio
> Consolidacao: Fases 6-10 + melhorias v2 (SOS Morse, historias de passageiros, locacoes Pigeon Forge/NYC, marcacao de erros)

---

## METADADOS DO PROJETO

| Campo | Valor |
|-------|-------|
| **Titulo** | RMS Titanic: A Arquitetura do Desastre |
| **Formato** | Documentario longa-metragem (episodio unico) |
| **Duracao** | 105 minutos |
| **Apresentadora** | Andreza Araujo — consultora senior em cultura de seguranca, 25+ anos, ex-PepsiCo LatAm |
| **Estilo visual** | Inspirado em James Cameron (rigor tecnico + mergulho forense) + Morris (Interrotron) |
| **Metodo entrevista** | Errol Morris — Interrotron, silencio estrategico, confronto gentil |
| **Filosofia visual** | Vittorio Storaro — luz e cor como linguagem, nao decoracao |
| **Filosofia cenografica** | Errol Morris — espaco como linguagem, reconstituicao fragmentada/estilistica |
| **Analise SST** | Dekker 5 etapas + Reason 5 camadas Swiss Cheese |
| **Cultura de seguranca** | Hopkins 5 indicadores + Schein 3 niveis + Westrum tipologia + Reason 4 subculturas + Bradley Curve (5 niveis) + Piramide de Bird |
| **Analise tecnica** | Foecke/McCarty (NIST/JHU) — metalurgia dos rebites |
| **Estrutura** | 3 atos (Bernard) / 5 beats (McKee) / 19 sequencias / 4 blocos |
| **Locacoes em campo** | Museu do Titanic (Sao Paulo), Titanic Museum (Pigeon Forge, TN), Pier 54/Chelsea Piers (NYC) |
| **Status** | FINAL DRAFT v2 |

---

## PREMISSA NARRATIVA

**Controlling Idea (McKee):**
> "Vidas sao destruidas quando uma civilizacao inteira normaliza a arrogancia tecnologica, e o lucro — disfarcado de progresso — silencia sistematicamente cada voz que alerta sobre o perigo."

**Questao Dramatica (Bernard):**
> "Como uma civilizacao inteira — seus engenheiros, seus reguladores, seus capitaes, seus magnatas — construiu, certificou, tripulou e lotou um navio que nao podia salvar metade das pessoas a bordo, e como cada um deles acreditou estar fazendo a coisa certa?"

**Valor em jogo:** Vida humana / Seguranca / Verdade

**Arco cromatico:** Ouro Edwardiano (#C8A25C) --> Sepia Belfast (#8B7355) --> Azul Atlantico (#1B3A5C) --> Cinza Aco (#6B7B8D) --> Verde Laboratorio (#4A6B5A) --> Branco Analitico (#E8E8E8) --> Preto Abissal (#0A0A0F)

---

## ELENCO DE ENTREVISTADOS

| # | Nome | Funcao | Sequencias | Setup de Entrevista |
|---|------|--------|-----------|---------------------|
| 1 | Dr. Tim Foecke (NIST) | Metalurgista forense — o DNA do desastre | SEQ 02, 06, 12 | Interrotron. Laboratorio NIST. Key light lateral 4800K. Bancada com rebites ao fundo. Ratio 4:1 |
| 2 | Parks Stephenson | Historiador naval — sistema Marconi | SEQ 08, 11 | Interrotron. Equipamento de comunicacao ao fundo. Key frontal-lateral 3800K. Telas com ambar Marconi |
| 3 | Dr. Jennifer Hooper McCarty (JHU) | Historiadora da metalurgia — arquivos H&W | SEQ 12 | Interrotron. Mesa academica. Documentos H&W. Iluminacao quente de biblioteca |
| 4 | Daniel Allen Butler | Historiador — psicologia de Smith, cultura edwardiana | SEQ 02, 04, 06, 10 | Entrevista longa. Rembrandt lighting 3200K. Escritorio com mapas e livros |
| 5 | Andreza Araujo (squad andreza-araujo) | Consultora senior em cultura de seguranca — 25+ anos, ex-PepsiCo LatAm, ponte passado-presente | APRESENTADORA em todas as SEQ + campo (Pigeon Forge, NYC, Sao Paulo) | Interrotron. Escritorio moderno. Key lateral 5600K. Tambem em campo (museus, locacoes industriais, Pier 54) |
| 6 | Don Lynch / Ken Marschall | Visual history — expedicoes ao wreck | SEQ 01, 19 | Marschall: pinturas ao fundo. Lynch: artefatos THS. Soft box 3800K |

---

## PERSONAGENS HISTORICOS (RECONSTITUICAO)

| Personagem | Funcao narrativa | Tipo reconstituicao | Sequencias |
|------------|------------------|---------------------|-----------|
| Thomas Andrews | Protagonista tragico — sabia e nao podia mudar | N2 (fragmentado) | SEQ 04, 07, 13 |
| Alexander Carlisle | Whistleblower silenciado — Cassandra do Titanic | N2 (fragmentado) | SEQ 04, 05, 09, 13 |
| J. Bruce Ismay | Antagonista sistemico — pressao comercial | N2 (fragmentado) | SEQ 04, 06, 10 |
| Capitao Edward Smith | Local Rationality encarnada — 40 anos de experiencia como armadilha | N3 (estilistico) | SEQ 06, 10 |
| Jack Phillips | Vitima do sistema duplo — Marconi vs White Star | N3 (estilistico) | SEQ 01, 08, 13 |
| Frederick Fleet | Ultima defesa num sistema quebrado | N3 (estilistico) | SEQ 06 |
| Board of Trade | Regulacao capturada — camada organizacional Reason | N1 (simbolico) | SEQ 09, 15 |

---

## PASSAGEIROS — HISTORIAS HUMANAS

| Personagem | Classe | Historia | Tipo | Sequencia |
|------------|--------|----------|------|-----------|
| John Jacob Astor IV | 1a | Homem mais rico a bordo ($87M). Ajudou esposa gravida ao bote. Perguntou se podia acompanha-la. "Nenhum homem antes que todas as mulheres." Ficou. | Arquivo + VO | SEQ 03 |
| Benjamin Guggenheim | 1a | Trocou o colete salva-vidas por smoking. "Nos vestimos com nossas melhores roupas e estamos preparados para afundar como cavalheiros." | Arquivo + VO | SEQ 03 |
| Isidor & Ida Straus | 1a | Donos da Macy's. Ida recusou o bote: "Vivi com meu marido 40 anos. Nao vou deixa-lo agora." Sentaram juntos no deck. | Arquivo + VO | SEQ 03 |
| Margaret "Molly" Brown | 1a | Forcou o remador do bote 6 a voltar para resgatar. Chamada "insubmissa." A voz que NAO foi silenciada. | Arquivo + VO | SEQ 03 |
| Wallace Hartley (banda) | Tripulacao | 8 musicos tocaram ate o final. Nenhum sobreviveu. "Nearer, My God, to Thee" ou "Autumn"? O dever alem do contrato. | Arquivo + VO | SEQ 03 |
| Familias da 3a classe | 3a | Imigrantes — irlandeses, suecos, libaneses, italianos. Muitos sem falar ingles. Corredores sem sinalizacao. Grades trancadas. 75% de mortalidade. | Grafismo + reconstituicao | SEQ 10 |

---

## PALETA CROMATICA — 7 CORES FUNDADORAS

| # | Nome | Hex | Significado | Ato(s) |
|---|------|-----|------------|--------|
| 1 | Ouro Edwardiano | #C8A25C | Brilho do progresso, riqueza que cega | I |
| 2 | Sepia Belfast | #8B7355 | Passado como materia, trabalho e ferrugem | I |
| 3 | Azul Atlantico | #1B3A5C | Oceano como entidade ameacadora | I, III |
| 4 | Cinza Aco Frio | #6B7B8D | Drenagem da esperanca, navio como evidencia | II |
| 5 | Verde Laboratorio | #4A6B5A | Analise forense, autopsial | II |
| 6 | Branco Analitico | #E8E8E8 | Compreensao pura, sistema revelado | III |
| 7 | Preto Abissal | #0A0A0F | Fundo do oceano, o desconhecido | III |

**Cores auxiliares:** Vermelho Alerta (#8B2500) — foguetes, Swiss Cheese, overlays de erro. Ambar Marconi (#D4A017) — sala de radio. Branco Flash (#FFFFFF) — instante da colisao.

---

## DISPOSITIVO VISUAL RECORRENTE: MARCACAO DE ERROS

Ao longo do documentario, quando cada erro e revelado, um OVERLAY discreto aparece no canto inferior esquerdo:

| Tipo | Icone | Cor | Significado |
|------|-------|-----|-------------|
| ERRO DE PROCESSO | Engrenagem | Vermelho Alerta #8B2500 | Falha de procedimento, design, regra |
| ERRO HUMANO | Silhueta | Vermelho Alerta #8B2500 | Decisao individual no momento |
| FALHA SISTEMICA | Rede/malha | Vermelho Alerta #8B2500 | Arquitetura organizacional que permite/incentiva o erro |

**Comportamento:** Aparece por 3 segundos com som de clique seco (carimbo). Discreto — nao interrompe o fluxo. No CLIMAX (SEQ 14), todos os overlays reaparecem simultaneamente, empilham-se, e se reorganizam no Swiss Cheese.

**Mapa completo de overlays:**

| SEQ | Tipo | Descricao do erro |
|-----|------|-------------------|
| 04 | PROCESSO | Anteparas rebaixadas — comercial > seguranca |
| 04 | PROCESSO | 48 botes reduzidos a 16 — estetica > sobrevivencia |
| 06 | HUMANO | Velocidade mantida apesar de 7 avisos de gelo |
| 06 | PROCESSO | Binoculos trancados — chave saiu com Blair em Southampton |
| 08 | SISTEMICO | Operador Marconi = funcionario comercial, nao de seguranca |
| 08 | HUMANO | Phillips ignora aviso do Mesaba — prioriza telegramas pagos |
| 09 | SISTEMICO | Merchant Shipping Act de 1894 — 18 anos sem atualizacao |
| 10 | PROCESSO | Botes arriados parcialmente — sem treinamento de evacuacao |
| 10 | SISTEMICO | Grades de classe = barreiras de evacuacao |
| 11 | HUMANO | Lord interpreta foguetes como "fogos festivos" |
| 11 | PROCESSO | Operador Marconi do Californian autorizado a dormir |
| 12 | PROCESSO | Rebites de ferro na proa — custo < 0.3% a mais para aco |
| 13 | SISTEMICO | 3 alarmes dados (Carlisle, Andrews, Phillips), 0 ouvidos |

---

---

# BLOCO 1 — ABERTURA: HOOK + SETUP

**ATO I | ~28 minutos | Beat 1 (Vida Normal) + inicio Beat 2 (Inciting Incident)**
**Value-Charge: POSITIVO --> NEGATIVO**
**Arco cromatico: PRETO --> Azul Abissal --> Ouro Edwardiano --> Sepia Belfast --> FLASH BRANCO --> Escuridao**

---

## SEQ 01 — PROLOGO: SOS + O CRIME SCENE

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 4 minutos |
| **Tipo de material** | Som Morse (reconstruido) + arquivo submarino (acervo Cameron, 33 mergulhos) + VO |
| **Paleta** | Preto Abissal #0A0A0F --> Azul Atlantico #1B3A5C |
| **Entrevistados** | Nenhum (VO). Ken Marschall como fonte visual complementar |
| **Props/cenografia** | Nenhuma construcao — som Morse + imagens reais do wreck |
| **Value-charge** | Ambiguo --> Positivo |
| **Beat McKee** | Beat 1 — abertura |
| **GAP plantado** | O que vemos no fundo foi construido com orgulho |

**IMAGEM:**

Tela preta. Silencio total — tres segundos.

Depois: um clique. Metalico, seco. O manipulador Morse.

··· ——— ···

SOS.

O ritmo e lento no inicio — quase cerimonial. Cada ponto e traco aparece como TEXTO branco sobre preto, sincronizado com o som:

**TEXTO (letra por letra, branco sobre preto):**
"CQD CQD SOS SOS de MGY"

Pausa. O Morse recomeça — mais rapido agora. Mais urgente. As maos de Phillips (reconstituicao N3 — close extremo, apenas as maos e o manipulador) batem o codigo com crescente desespero.

**TEXTO:**
"We are sinking fast. Passengers being put into boats."
— Jack Phillips, operador Marconi do RMS Titanic
15 de abril de 1912, 00:45

O Morse continua — mas agora o som se DEFORMA. O clique metalico vai se misturando com pressao de agua. O codigo vira eco. O eco vira abismo. A transicao e gradual: estamos descendo ao fundo do mar.

**TRANSICAO SONORA:** Morse --> eco submarino --> silencio abissal.

A luz dos ROVs (veiculos subaquaticos de Cameron) recorta a proa do Titanic como um bisturi. O metal esta coberto de rusticles — formacoes biologicas ferrosas que parecem estalactites de ferrugem. A escala e revelada lentamente: a camera recua, recua, e o navio emerge do escuro como uma catedral submarina.

**APRESENTADORA (Andreza Araujo):** "Eu trabalho com seguranca ha mais de 25 anos. Ja entrei em fabricas, plataformas, canteiros de obra em 19 paises. E em cada lugar, encontrei a mesma coisa: nao um defeito, nao uma negligencia — uma pergunta. A mesma pergunta, em qualquer lingua, em qualquer continente: como foi possivel? O Titanic esta a 3.800 metros de profundidade no Atlantico Norte. Mas a resposta nao esta la embaixo. Esta aqui em cima — nas decisoes que tomamos todo dia."

A camera continua a recuar. Os sapatos enfileirados no leito oceanico — marca de corpos que se desfizeram ha mais de um seculo. As luminarias art deco cobertas de vida marinha. O silencio absoluto do fundo do Atlantico Norte.

**APRESENTADORA (Andreza Araujo):** "Este nao e um navio naufragado. E uma cena de crime. E como toda investigacao, a gente nao procura culpados — procura causas."

**CORTE SECO.**

**SOM:** O estrondo de um martelo sobre metal. Aco brilhante. Belfast, 1909.

**NOTA DE DIRECAO VISUAL:** O episodio abre no PRETO TOTAL — nao no azul. O primeiro estimulo e SONORO: o Morse. O espectador ouve antes de ver. Quando a imagem aparece (ROVs no wreck), o codigo Morse ja plantou a urgencia. A transicao Morse --> abismo e o primeiro arco sonoro do documentario: comunicacao humana dissolve-se em silencio oceanico. Quando Cameron diz "crime scene," a palavra redefine o que o azul significa. O contraste entre SEQ 01 e SEQ 02 e o MAIOR do episodio — do azul abissal para o dourado industrial. Corte SECO, nao fade.

**SOM/MUSICA:** Codigo Morse (reconstruido com equipamento de epoca). Transicao para sons subaquaticos naturais (gravados em mergulho). Nenhuma musica. O Morse E a musica do desespero. O silencio do fundo do mar E a musica da consequencia. O corte para Belfast traz o metalico industrial como ruptura sonora.

---

## SEQ 02 — A ERA DOS TITANS

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 6 minutos |
| **Tipo de material** | Arquivo historico + reconstituicao N2 (estaleiro) + grafismo + entrevista (Foecke — semente) |
| **Paleta** | Ouro Edwardiano #C8A25C dominante + Sepia Belfast #8B7355 |
| **Entrevistados** | Dr. Tim Foecke (semente plantada — nao revelada), Daniel Allen Butler (contexto edwardiano) |
| **Props/cenografia** | Reconstituicao parcial estaleiro Belfast: fornalha + rebites sendo martelados. Operarios como SILHUETAS contra fogo e metal. Iluminacao chiaroscuro (Caravaggio industrial) |
| **Value-charge** | Positivo (progresso, grandiosidade) |
| **Beat McKee** | Beat 1 — vida normal |

**IMAGEM:**

A Era Edwardiana em todo seu esplendor industrial. O Imperio Britanico no zenite. A corrida transatlantica: White Star Line contra Cunard. A Cunard tem o Lusitania (1907) e o Mauretania — rapidos, elegantes, vencedores do Blue Riband. A White Star responde com uma aposta diferente: nao o mais rapido, mas o MAIOR. O mais luxuoso. O mais impressionante.

Belfast, estaleiro Harland & Wolff. Rio Lagan. Guindastes Arrol — os maiores da epoca — recortam o ceu irlandes. 15.000 operarios. A maior estrutura movel ja construida pelo homem comeca a tomar forma.

**RECONSTITUICAO (N2 — fragmentada):** Close em rebites sendo martelados na proa por equipes de rebitadores manuais. Quatro homens por equipe: um aquece o rebite na fornalha (laranja incandescente), passa com tenazes ao segundo, que o posiciona no furo, o terceiro segura a contra-cavilha, o quarto martela. Silhuetas contra o fogo da fornalha. As maos sao a unica parte visivel — maos de operarios, maos que constroem, maos que sem saber plantam a semente do desastre.

**GRAFISMO:** O crescimento do navio em cross-section animada — quilha, cavernas, chapas, rebites. 3 milhoes de rebites. O numero aparece e permanece na tela.

**ENTREVISTA (Foecke — SEMENTE):** Close no rosto de Foecke, Interrotron, luz lateral fria do laboratorio NIST.

**Foecke:** "Quando analisamos esses rebites em 1998, o que encontramos no microscopio foi..."

CORTE. A frase fica suspensa. Nao revelamos. O espectador recebe a semente do conflito — sera cultivada por 50 minutos antes de florescer na SEQ 12.

**ENTREVISTA (Butler — CONTEXTO):** Rembrandt lighting. Escritorio com livros ao fundo.

**Butler:** "Para entender o Titanic, voce precisa entender a era. Nao era apenas um navio. Era a prova de que a tecnologia havia vencido a natureza. E se a tecnologia venceu a natureza — para que se preocupar com botes salva-vidas?"

**SOM/MUSICA:** Metal sendo martelado — ritmo industrial como percussao. Fornalha rugindo. O som do progresso e identico ao som da construcao do desastre. Sem musica composta — o estaleiro E a musica.

**NOTA DE DIRECAO VISUAL:** O choque cromatico com SEQ 01 e deliberado. O espectador e arrancado do fundo do mar e jogado num mundo de ouro. Belfast brilha. Os dourados sao quentes mas nao acolhedores — sao o brilho do METAL, nao do sol. Elegancia como fachada (Storaro). A reconstituicao e IMPRESSIONISTA: operarios como formas contra o fogo. Nao tentamos recriar Belfast — evocamos.

---

## SEQ 03 — AS VIDAS A BORDO

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 6 minutos |
| **Tipo de material** | Arquivo fotografico + grafismo + VO + locacao Pigeon Forge (Andreza) |
| **Paleta** | Ouro Edwardiano #C8A25C (1a classe) degradando para Sepia #8B7355 (3a classe). Quente mas melancolico — o espectador ja sabe o que vem |
| **Entrevistados** | Andreza Araujo (em campo — Titanic Museum, Pigeon Forge) |
| **Props/cenografia** | Locacao real: Titanic Museum, Pigeon Forge, TN. Replicas de cabines, corredores, artefatos. Bloco de gelo (-2C) |
| **Value-charge** | Positivo --> melancolico (ironia dramatica — o espectador sabe, os personagens nao) |
| **Beat McKee** | Beat 1 — complicacao emocional / investimento no elenco |
| **Funcao Bernard** | O publico PRECISA se importar com as pessoas antes de conhecer os erros |

**IMAGEM:**

10 de abril de 1912. Southampton. O Titanic zarpa com 2.224 almas.

**ANDREZA EM CAMPO (Pigeon Forge, Titanic Museum):** Andreza caminha por uma replica do corredor de primeira classe. Lustres. Mogno. Carpete. O luxo e tangivel.

**APRESENTADORA (Andreza Araujo):** "Quando a gente fala de seguranca, a gente fala de numeros. Taxa de acidentalidade. Frequencia. Gravidade. Mas seguranca nao e sobre numeros. E sobre gente. Cada numero e uma pessoa. Uma historia. Uma familia esperando em casa."

**TRANSICAO:** Andreza para diante de um painel com fotografias de passageiros. Close nas fotos.

**VO (narrador — registro documental, sobre fotografias de arquivo):**

**HISTORIA 1 — John Jacob Astor IV:**
Fotografia de arquivo: Astor com esposa Madeleine, gravida de 5 meses. O homem mais rico a bordo — fortuna estimada em 87 milhoes de dolares (equivalente a 2.5 bilhoes hoje). Quando os botes comecaram a ser arriados, Astor ajudou Madeleine a entrar no bote 4. Perguntou ao oficial Lightoller se podia acompanha-la — "dada a condicao dela." Lightoller respondeu: "Nenhum homem antes que todas as mulheres e criancas." Astor recuou. Acendeu um cigarro. Ficou.

**HISTORIA 2 — Benjamin Guggenheim:**
Fotografia de arquivo: Guggenheim em traje formal. Magnata do minerio. Quando percebeu que o navio afundava, desceu ao camarote com seu valete Victor Giglio. Tiraram os coletes salva-vidas. Vestiram smokings. Voltaram ao salao.

**VO:** "Nos vestimos com nossas melhores roupas e estamos preparados para afundar como cavalheiros. Diga a minha esposa que fiz o meu melhor no cumprimento do meu dever."

**HISTORIA 3 — Isidor e Ida Straus:**
Fotografia de arquivo: o casal Straus. Fundadores da Macy's. 67 e 63 anos. Casados ha 41 anos. Um oficial ofereceu lugar a Ida no bote 8. Ida comecou a entrar — parou. Voltou. Tomou o braco do marido.

**VO:** "Vivi com meu marido por 40 anos. Nao vou deixa-lo agora."

Isidor recusou entrar em qualquer bote enquanto houvesse mulheres e criancas a bordo. Foram vistos pela ultima vez sentados juntos em cadeiras de deck, de maos dadas, enquanto a agua subia.

**HISTORIA 4 — Margaret "Molly" Brown:**
Fotografia de arquivo: Brown com expressao determinada. Herdeira de mineracao. No bote 6, com apenas 28 pessoas para 65 vagas, Brown exigiu que o remador Quartermaster Hichens voltasse para resgatar mais pessoas. Hichens recusou — "o bote sera sugado." Brown ameacou joga-lo ao mar. Assumiu os remos. O bote voltou.

**APRESENTADORA (Andreza Araujo):** "Molly Brown fez o que Carlisle tentou fazer cinco anos antes. Levantou a voz. A diferenca? No bote, nao havia sistema para silencia-la. Na sala de reunioes de 1907, havia."

**HISTORIA 5 — Wallace Hartley e a Banda:**
Fotografia de arquivo: os 8 musicos. Contratados pela agencia C.W. & F.N. Black — nao eram tripulantes da White Star. Tocaram no salao enquanto os botes eram arriados. Quando a inclinacao tornou impossivel ficar de pe, moveram-se para o deck externo. Tocaram ate que as ondas os levaram. Nenhum sobreviveu.

**VO:** "A ultima musica ouvida no Titanic permanece debatida — 'Nearer, My God, to Thee' ou 'Autumn.' O que nao se debate: oito homens escolheram a musica quando o silencio teria sido mais facil."

**ANDREZA EM CAMPO (Pigeon Forge — bloco de gelo):** Andreza coloca a mao no bloco de gelo do museu (replica a -2C, a temperatura da agua do Atlantico naquela noite). Segura por alguns segundos. Retira. Olha para a camera.

**APRESENTADORA (Andreza Araujo):** "A agua do Atlantico estava a menos dois graus naquela noite. Voce consegue segurar a mao aqui por 15 segundos. Quem caiu na agua tinha 15 minutos ate a hipotermia. 30 minutos ate a inconsciencia. A maioria dos 1.517 nao morreu afogada. Morreu de frio. No escuro. Esperando um bote que nao voltou."

[SILENCIO — 5 segundos]

**APRESENTADORA (Andreza Araujo):** "2.224 pessoas. Cada uma com uma historia, uma familia, um motivo para estar naquele navio. Quando eu falo de cultura de seguranca, nao estou falando de normas — estou falando de gente como Ida Straus, como os musicos, como as criancas da terceira classe que nunca tiveram nome nos jornais."

**SOM/MUSICA:** Nenhuma musica composta. Sons de porto (apitos, vento, multidao) nas transicoes entre historias. Nas historias em si: silencio respeitoso com VO sobre ele. No momento do bloco de gelo: APENAS o som do museu — passos, respiracao de Andreza, o zumbido do refrigerador do bloco. Realidade nua.

**NOTA DE DIRECAO VISUAL:** A sequencia oscila entre ARQUIVO (sepia, grao, textura de epoca) e CAMPO (Pigeon Forge, cor moderna mas desaturada — presente olhando para o passado). A alternancia diz: estas historias sao reais E estao aqui, preservadas. As fotos de arquivo sao apresentadas em CLOSE LENTO (Ken Burns effect contido, sem exagero). O bloco de gelo e filmado em close EXTREMO — cristais de gelo, pele da mao de Andreza, a umidade condensando. O frio e VISIVEL.

---

## SEQ 04 — TRES HOMENS E UM NAVIO

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 8 minutos |
| **Tipo de material** | Reconstituicao N2 (sala projetos H&W, reuniao 1907) + arquivo + entrevistas |
| **Paleta** | Ouro Edwardiano #C8A25C + Sepia Belfast #8B7355. Cinza Aco #6B7B8D comeca a aparecer nas sombras |
| **Entrevistados** | Butler (psicologia dos tres), possivelmente Foecke (contexto tecnico Andrews) |
| **Props/cenografia** | Mesa de projetos de madeira escura (mogno). Blueprints do Titanic. Lampada de mesa com abajur verde. Compasso, lapis, borracha. Mesa de conferencia longa para reuniao de 1907. Cadeiras de couro. Relogio de parede |
| **Value-charge** | Positivo com sombras |
| **Beat McKee** | Beat 1 — complicacao inicial |
| **OVERLAYS** | PROCESSO: Anteparas rebaixadas / PROCESSO: 48 botes reduzidos a 16 |

**IMAGEM:**

Tres homens. Tres visoes. Um navio.

**Thomas Andrews** — o genio tecnico. Projetista-chefe de Harland & Wolff. Sobrinho de Lord Pirrie. O homem que conhecia cada rebite, cada antepara, cada centimetro do Titanic. Propôs anteparas mais altas — ate o conves E (o "deck de botes") — para garantir estanqueidade real. Foram construidas ate o conves F (um deck abaixo). Motivo: espaco interno para areas comerciais.

**RECONSTITUICAO R1 (N2 — fragmentada):** Mesa de projetos coberta de blueprints. Close nas maos de Andrews desenhando a linha das anteparas. Outra mao (Ismay? Pirrie?) traca uma linha MAIS BAIXA por cima. Close no lapis apagando a linha de Andrews. Dessaturacao 65%. Grain moderado. Camera lenta sutil nos dedos que apagam. Som: lapis no papel. Respiracao. Relogio de parede (tic-tac constante — o tempo passando enquanto a seguranca e apagada).

> **[OVERLAY: ERRO DE PROCESSO]** Anteparas rebaixadas de conves E para conves F — espaco comercial priorizado sobre estanqueidade

**Alexander Carlisle** — o whistleblower. Projetista-chefe anterior a Andrews, cunhado de Lord Pirrie. Em 1907, propôs 48 botes salva-vidas usando os novos davits Welin — que JA estavam sendo instalados com capacidade para suporta-los. Lord Pirrie vetou: botes no deck de passeio obstruiriam a vista dos passageiros de primeira classe.

**RECONSTITUICAO R2 (N2 — fragmentada):** Mesa de reuniao longa. Planta do deck de botes com 48 marcas. Uma mao risca marcas com lapis vermelho ate sobrar 16. Relogio na parede mostra cinco minutos passando. Cadeira empurrada para tras — Carlisle saindo. Dessaturacao 60%. Camera lenta quando a mao risca as marcas — cada risco e uma vida futura. Som: silencio quase total. Relogio. Lapis riscando. Cadeira arrastada. A porta que se fecha.

> **[OVERLAY: ERRO DE PROCESSO]** 48 botes reduzidos a 16 em reuniao de 5 minutos — estetica de 1a classe prevalece sobre capacidade de resgate

**J. Bruce Ismay** — presidente da White Star Line. Nao vilao, mas produto do sistema. Pressao comercial personificada. Responde aos acionistas, nao aos engenheiros. O tamanho do navio e o argumento de venda. O luxo e a evidencia de seguranca.

**ENTREVISTA (Butler):** "Andrews via o navio como engenharia. Carlisle via como risco. Ismay via como produto. Nenhum dos tres estava errado — e exatamente isso que torna a historia terrificante."

**NOTA DE DIRECAO VISUAL:** Andrews e filmado em reconstituicao com luz mais quente (criador). Carlisle com sombras mais pronunciadas (silenciado). Ismay com highlights mais duros (ambicao). A iluminacao DIFERENCIA os tres ANTES que o texto o faca. O Cinza Aco comeca a infiltrar as sombras — presagio cromatico.

**SOM/MUSICA:** Relogio de parede como leitmotiv. Lapis e papel. O som da decisao — banal, quotidiano, letal.

---

## SEQ 05 — A VOZ QUE NINGUEM OUVIU

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 2 minutos |
| **Tipo de material** | Arquivo inquerito + reconstituicao N1 (simbolica) + VO |
| **Paleta** | Sepia Belfast #8B7355 dominante. O Ouro SOME. Tons terrosos, papeis envelhecidos |
| **Entrevistados** | Nenhum (arquivo sonoro + VO) |
| **Props/cenografia** | Reconstituicao simbolica: cadeira vazia num espaco grande demais. Luz de tribunal — direcional de cima, sombras duras. Transcricao do inquerito como prop-evidencia |
| **Value-charge** | Negativo emergente |
| **Beat McKee** | Beat 1 — semente dramatica |
| **Funcao Bernard** | O publico PRECISA saber mais. O trem arrancou |

**IMAGEM:**

1912. Inquerito britanico pos-desastre. Alexander Carlisle na cadeira de testemunhas.

**ARQUIVO/RECONSTITUICAO (N1):** A transcricao do inquerito, pergunta 21370. Close no documento. Luz rasante revela a textura do papel — dobras, tinta de epoca, carimbos oficiais. Temperatura 2800K (sepia-quente).

**VO (narrador, Tom em registro de leitura documental):**
"I suggested 48 boats. The meeting lasted five minutes. My proposals were not discussed."

Silencio. Tres segundos.

**APRESENTADORA (Andreza Araujo):** "Cinco anos antes do naufragio, Alexander Carlisle sentou-se numa sala e disse o que era preciso fazer. A sala nao ouviu. Eu vi isso acontecer em dezenas de empresas — o tecnico que reporta o risco e encontra o olhar de 'voce de novo?' A pergunta nao e por que Carlisle falou. A pergunta e por que ninguem ouviu. E essa pergunta eu faco todo dia no meu trabalho."

A Questao Dramatica esta plantada. O espectador foi fisgado. De agora em diante, quer entender COMO foi possivel.

**SOM/MUSICA:** O eco de uma sala vazia. Passos afastando-se. Silencio.

**NOTA DE DIRECAO VISUAL:** Reducao cromatica radical: de tres tons quentes para um. O ouro do progresso evaporou. Estamos no terroso do documento, do registro. A cor diz: "isto e prova, nao celebracao." Luz de tribunal — dura, de cima, sem misericordia.

---

## SEQ 06 — INCITING INCIDENT: 37 SEGUNDOS

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 3 minutos |
| **Tipo de material** | Reconstituicao N3 (estilistico — ninho-de-corvo, ponte de comando) + CGI |
| **Paleta** | Azul Atlantico #1B3A5C + Branco Flash #FFFFFF (instante colisao) + Preto Abissal #0A0A0F |
| **Entrevistados** | Butler (contexto psicologico de Smith, posicionado antes ou apos a sequencia) |
| **Props/cenografia** | **Ninho-de-corvo (construcao completa):** Plataforma circular (~1.2m diametro). Parapeito metalico. Sino de bronze com corda. Armario de binoculos TRANCADO (cadeado visivel, sem chave — a chave saiu com o segundo oficial Blair em Southampton). Telefone de comunicacao com a ponte. Ceu preto (fundo infinito). **Ponte de comando (parcial):** Silhueta de Smith contra vidro |
| **Value-charge** | NEGATIVO (ruptura total) |
| **Beat McKee** | Beat 2 — Inciting Incident |
| **TURNING POINT** | ATO I --> ATO II |
| **OVERLAYS** | HUMANO: Velocidade mantida / PROCESSO: Binoculos trancados |

**IMAGEM:**

14 de abril de 1912. 23:39.

**RECONSTITUICAO R4 (N3 — estilistico):** POV do ninho-de-corvo. Escuridao quase total. Noite sem lua. Mar como espelho negro — "mar de vidro," relataram sobreviventes. Frederick Fleet no parapeito, maos vazias. Sem binoculos.

**DISPOSITIVO VISUAL (contrafactual):** Alternancia — SEM binoculos (escuridao total, o iceberg e invisivel) / COM binoculos (o iceberg aparece a 2 milhas, fantasmatico, branco contra preto). O espectador VE o que Fleet nao pode ver. Cada alternancia e uma faca: a diferenca entre ver e nao ver e a diferenca entre um cadeado e uma chave que nao esta la.

Close na FECHADURA do armario de binoculos. Um reflexo estelar minimo a ilumina — o espectador a ve e entende. O cadeado E o sistema.

> **[OVERLAY: ERRO DE PROCESSO]** Binoculos trancados no armario — chave saiu com 2o oficial Blair em Southampton, nunca transferida

Sino. Tres batidas. Metalico, reverberante. "Iceberg, right ahead!"

37 segundos. Contagem em tempo dilatado (camera lenta). "Hard a-starboard." "Full astern."

> **[OVERLAY: ERRO HUMANO]** Velocidade mantida a 22.5 nos apesar de 7 avisos de gelo em 24h — procedimento padrao da epoca

**CGI:** Metal range contra gelo. Nao perfuracao — SEPARACAO de placas. Os rebites estourando nas costuras. Seis compartimentos abertos ao mar. A proa comeca a inclinar.

Silhueta de Smith na ponte. Azul-preto. Forma humana contra o infinito. Ele ja pertence ao oceano — a luz e a mesma cor do mar.

Andrews com bloco de notas. Calculando. "Uma hora. Duas no maximo." Numero na tela: 2.224 a bordo. 1.178 lugares nos botes. A aritmetica e implacavel.

**FLASH BRANCO** — 1 frame, no instante exato do impacto metal-gelo. Depois: ESCURIDAO. Depois: azul da agua entrando.

**SOM/MUSICA:** Vento leve e constante no ninho-de-corvo. Mar distante. Respiracao de Fleet. SILENCIO crescente. Sino: tres batidas. Depois: o som do metal sob pressao — estalar de rebites, gemido do casco, rugido da agua. Nenhuma musica composta. O som do desastre e toda a musica necessaria.

**NOTA DE DIRECAO VISUAL:** O flash branco e o marco cromatico do episodio inteiro. Ate aqui, cores quentes dominaram. A partir daqui, cores frias dominam. O sistema cromatico COLAPSA no Inciting Incident: flash (claridade violenta) --> escuridao --> azul (agua entrando). A temperatura de cor cai ~2000K em 3 minutos de tela. O espectador sente frio — literal e metaforicamente.

> **>>> TURNING POINT ATO I --> ATO II <<<**
> O mundo do progresso se despedacou. A investigacao comeca.

---

---

# BLOCO 2 — DESENVOLVIMENTO: CONFRONTACAO

**ATO II | ~48 minutos | Beat 2 (continuacao) + Beat 3 (Progressive Complications)**
**Value-Charge: NEGATIVO --> NEGATIVO CRESCENTE --> PICO NEGATIVO**
**Arco cromatico: Cinza Aco + Azul --> Verde Laboratorio --> Quase P&B**

---

## SEQ 07 — ANATOMIA DA COLISAO

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 7 minutos |
| **Tipo de material** | CGI forense (modelo 3D Cameron) + reconstituicao N1 (inserts rebites) + entrevistas Foecke/McCarty |
| **Paleta** | Cinza Aco #6B7B8D + Azul Atlantico #1B3A5C. Verde Laboratorio #4A6B5A comeca a infiltrar-se |
| **Entrevistados** | Dr. Tim Foecke (NIST), Daniel Allen Butler |
| **Props/cenografia** | Props: rebites reais de ferro forjado (replicas metalurgicamente precisas) filmados em macro sobre fundo preto. Mao de Foecke segurando rebite como transicao para CGI |
| **Value-charge** | Negativo (a verdade fisica do desastre) |
| **Beat McKee** | Beat 2 continuacao |

**IMAGEM:**

O impacto como a ciencia o mostra. Nao como Hollywood o conta.

**CGI FORENSE (modelo 3D Cameron):** O casco do Titanic em corte transversal. Cinza metalico para o casco, azul para a agua. Iluminacao fria (3200K simulado). O modelo nao e bonito — e AUTOPSIAL. Cameron o usa como ferramenta forense.

A colisao em slow motion extremo: o iceberg nao "rasga" o casco. Os rebites de ferro forjado na zona da proa, sob pressao lateral, ESTOURARAM — suas cabecas saltaram e as placas de aco se SEPARARAM nas costuras. A agua do Atlantico Norte (temperatura: -2C) entrou pelas fendas com pressao hidraulica.

**RECONSTITUICAO R5 (N1 — simbolica + CGI):** Close microscopico em CGI de rebite sob stress. Animacao: verde (estavel) --> amarelo (stress) --> vermelho (falha) --> azul (agua). Cada rebite que estoura e nomeado no CGI (numero, posicao, material). Slow motion extremo — o que aconteceu em milissegundos dura 8 segundos de animacao.

**ENTREVISTA (Foecke):** Interrotron. Luz lateral fria 4800K. Laboratorio NIST.

**Foecke:** "O iceberg nao perfurou o casco do Titanic. Isso e um mito. O que aconteceu foi separacao de placas — os rebites cederam, e as costuras se abriram. E se abriram porque os rebites na proa e na popa eram de FERRO FORJADO, nao de aco. Ferro com teores de escoria muito acima do aceitavel."

**Pergunta do entrevistador:** "Por que ferro na proa e aco no meio?"

[SILENCIO — 5 segundos]

**Foecke:** "Custo. Logistica. Harland & Wolff nao tinha rebitadores hidraulicos suficientes para as secoes curvas da proa e da popa. A rebitagem manual exigia rebites menores e mais macios. Ferro era mais barato e mais facil de trabalhar. Funcionava — em TODOS os navios anteriores."

**CGI (grafismo distribuicao):** Planta lateral do Titanic. Aco em Azul Atlantico (resistente) no centro. Ferro em Vermelho Alerta (fragil) na proa e popa. A zona de impacto COINCIDE com a zona vermelha. O espectador ve: o ponto mais fraco foi o primeiro a ser atingido.

**SOM/MUSICA:** Metalico. Estalo seco de rebite estourando. Rugido da agua. Repetitivo, ritmico, IMPLACAVEL — como um relogio contando mortes. Nenhuma musica.

**NOTA DE DIRECAO VISUAL:** A temperatura de cor caiu drasticamente desde o Ato I. O casco 3D nao e dourado como o estaleiro — e cinza como um cadaver. O CGI e impiedoso em sua clareza: a beleza e forense, nao estetica.

---

## SEQ 08 — COMPLICACAO 1: OS AVISOS SILENCIADOS

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 7 minutos |
| **Tipo de material** | Grafismo animado (mapa Atlantico) + reconstituicao N3 (sala Marconi) + entrevista Stephenson |
| **Paleta** | Cinza Aco #6B7B8D dominante. Ambar Marconi #D4A017 APENAS na sala de radio — unico ponto de calor no Ato II |
| **Entrevistados** | Parks Stephenson (Interrotron, 3800K, telas de equipamento ao fundo) |
| **Props/cenografia** | **Sala de Radio Marconi (construcao completa):** ~3m x 2.5m. Paredes de madeira com isolamento. Transmissor/receptor Marconi (replica). Fones metalicos. Manipulador Morse. Lampada fraca. Pilha de telegramas de passageiros. Aviso de gelo com "ICE" visivel. Logbook. Copo de agua VAZIO |
| **Value-charge** | Negativo crescente (de "negligencia" a "design do sistema") |
| **Beat McKee** | Beat 3 — Progressive Complication 1 |
| **GAP 3** | Nao foi negligencia consciente — foi arquitetura organizacional |
| **OVERLAYS** | SISTEMICO: Operador Marconi = funcionario comercial / HUMANO: Phillips ignora aviso do Mesaba |

**IMAGEM:**

Sete avisos de gelo em 24 horas. Sete vezes o sistema foi alertado. Sete vezes o alerta se perdeu.

**GRAFISMO (Mapa Atlantico Norte):** Fundo em Azul Atlantico escuro. Navios como pontos luminosos. Avisos de gelo como pulsos brancos que se acendem um a um com timestamps. A rota do Titanic em ambar — uma flecha que nao desvia. O espectador ve o tempo ENCURTAR enquanto os avisos se acumulam. A rota ambar e uma sentenca.

O aviso do Baltic — Ismay o recebe e GUARDA no bolso. Exibe para passageiras como curiosidade de salao. O aviso de gelo como objeto social, nao como alerta de seguranca.

O aviso do Mesaba — o mais critico, o mais urgente, o que descrevia gelo EXATAMENTE na rota do Titanic. NUNCA chegou a ponte.

**RECONSTITUICAO R3 (N3 — estilistico):** Sala Marconi construida. Phillips de costas, fones, mao no manipulador Morse. Source UNICA: brilho dos equipamentos (ambar, de baixo para cima — sombras ascendentes no rosto). Ratio extremo 8:1. A pilha de telegramas de passageiros cresce. Cada telegrama e receita para a Marconi Company. O aviso de gelo chega. Phillips o coloca de LADO sem ler — a mao com o aviso fica a tres palmos da mao no manipulador. Camera lenta nesse gesto. O aviso em COR FRIA (azulado — perigo). Os telegramas em COR QUENTE (ambar — dinheiro).

> **[OVERLAY: FALHA SISTEMICA]** Operador Marconi = funcionario comercial — avisos de gelo nao geram receita, telegramas de passageiros sim

> **[OVERLAY: ERRO HUMANO]** Phillips ignora aviso do Mesaba — o mais critico — prioriza telegramas pagos. "Keep out! Shut up!"

**ENTREVISTA (Stephenson):** Interrotron. Equipamento de comunicacao ao fundo.

**Stephenson:** "Phillips nao era tripulante do Titanic. Era empregado da Marconi Company. A Marconi cobrava por telegrama de passageiro transmitido. Os avisos de gelo nao geravam receita. Phillips nao IGNOROU o aviso — o sistema nao permitia que ele o PRIORIZASSE."

**Pergunta:** "O sistema Marconi no Titanic era um sistema de seguranca ou comercial?"

[SILENCIO — 7 segundos]

**Stephenson:** "Comercial. Absolutamente comercial. Com uma funcao de seguranca acidental."

**APRESENTADORA (Andreza Araujo):** "Jack Phillips nao era negligente. Era um trabalhador de 25 anos seguindo as regras do sistema que o empregava. A Marconi Company pagava por telegrama — o aviso de gelo nao valia nada. Eu digo sempre: erro e inerente ao ser humano. O que nao pode ser inerente e um sistema que impede o humano de fazer a coisa certa. Phillips nao PODIA priorizar seguranca. O sistema nao permitia."

**SOM/MUSICA:** Clique-clique do Morse — ritmo nervoso, incessante. Estatica constante (sisssss). Som distante do mar contra o casco. NENHUMA musica. A sala Marconi tem sua propria sinfonia — monotona, claustrofobica, letal.

**NOTA DE DIRECAO VISUAL:** O ambar da sala Marconi e uma ARMADILHA cromatica. E o unico ponto de calor em todo o Ato II — e essa luz quente nao e conforto, e a pressao de um homem encurralado. O dutch angle de 5 graus no enquadramento diz: o mundo de Phillips esta desalinhado.

---

## SEQ 09 — COMPLICACAO 2: OS BOTES FANTASMA

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 8 minutos |
| **Tipo de material** | Grafismo animado + reconstituicao N1 (Board of Trade) + arquivo + entrevista |
| **Paleta** | Cinza Aco #6B7B8D + Sepia documental dessaturado |
| **Entrevistados** | Butler (contexto), possivelmente Stephenson (regulacao maritima) |
| **Props/cenografia** | **Board of Trade (N1 — simbolico):** Apenas superficie de mesa visivel. Feltro verde escuro. Replica Merchant Shipping Act 1894. Caneta tinteiro. Mata-borroes. Carimbo Board of Trade |
| **Value-charge** | Negativo crescente (indignacao — foi DECISAO, nao esquecimento) |
| **Beat McKee** | Beat 3 — Progressive Complication 2 |
| **GAP 4** | Os davits tinham capacidade para 48 botes. Foram colocados 20 |
| **OVERLAY** | SISTEMICO: Merchant Shipping Act de 1894 — 18 anos sem atualizacao |

**IMAGEM:**

A aritmetica que matou.

**RECONSTITUICAO R6 (N1 — simbolico):** Close extremo no Merchant Shipping Act de 1894. Maos virando paginas. Dedo para na tabela de botes salva-vidas. Outra mao escreve "46.328 tons." A tabela nao tem coluna para esse numero. Pausa. Documento fechado. Dessaturacao 80% (quase P&B — burocracia e incolor). Camera absolutamente ESTATICA — como a regra. Se a regra nao se move, a camera nao se move. Som: papel. Caneta tinteiro riscando. O silencio de quem nao questiona uma regra.

> **[OVERLAY: FALHA SISTEMICA]** Merchant Shipping Act de 1894 — 18 anos sem atualizacao. Regra para navios de 10.000 tons aplicada a um de 46.000

**GRAFISMO ANIMADO (DRIFT VISUALIZADO — Dekker):** Navio crescendo, regra parada. Uma regua fixa na tela — a regra de 1894, 10.000 toneladas, imovel. Debaixo, navios CRESCEM:

10.000 tons (1894) — cabe na regra.
14.000 tons (Kaiser Wilhelm, 1897) — aperta.
20.000 tons (Celtic, 1901) — transborda.
31.500 tons (Lusitania, 1907) — a regra e minuscula.
46.000 tons (Titanic, 1912) — quatro vezes MAIOR que a regra.

A regua nao se move. O gap alarga como uma fissura. Estetica monocromatica: navios em cinza claro, regra como fio branco sobre fundo preto.

20 botes para 2.224 pessoas. "Faca a conta."

**ENTREVISTA (Butler):** "Os davits Welin foram instalados com capacidade para 48 botes. Os davits estavam la. A engenharia estava la. A decisao NAO estava la."

**APRESENTADORA (Andreza Araujo):** "O Board of Trade nao errou por incompetencia. Errou por coerencia — foi coerente com uma regra que ninguem questionava. Eu chamo isso de Indicador Melancia: verde por fora, vermelho por dentro. A regra era verde — certificada, legal, conforme. Por dentro, era vermelha — desatualizada, capturada, letal. Funcionou por 18 anos. Funcionou ate a noite de 14 de abril."

**SOM/MUSICA:** O som do grafismo e MECANICO — engrenagens de um sistema relojoeiro. Cada ano que passa sem atualizacao da regra e um clique a mais no mecanismo. O som e o drift.

---

## SEQ 10 — COMPLICACAO 3: A ARITMETICA DA CLASSE

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 8 minutos |
| **Tipo de material** | Reconstituicao N3 (grades entre decks — CRITICA) + grafismo mortalidade + arquivo + entrevista + locacao Pigeon Forge |
| **Paleta** | Cinza Aco #6B7B8D BIFURCADO: cinza-quente (1a classe, ultimo suspiro do ouro) vs cinza-frio (3a classe, prenuncio do fundo do mar). Azul frio para 3a classe. Vermelho Alerta para lampadas de emergencia |
| **Entrevistados** | Butler (contexto de classe edwardiana, Interrotron), Andreza em campo (Pigeon Forge) |
| **Props/cenografia** | **Grades entre decks (construcao completa):** Grade de ferro com barras verticais e horizontais. Corredor 1a classe (mais largo, iluminado). Corredor 3a classe (estreito, sombrio, labirintico). Tranca/cadeado na grade. Mao de comissario na tranca. Lampadas de corredor fracas. Sinalizacao minima ou ausente para 3a classe |
| **Value-charge** | Negativo crescente (furia — "galanteria" era privilegio) |
| **Beat McKee** | Beat 3 — Progressive Complication 3 |
| **GAP 5** | A segregacao nao era falha do sistema — ERA o sistema |
| **OVERLAYS** | PROCESSO: Botes arriados parcialmente / SISTEMICO: Grades de classe = barreiras de evacuacao |

**IMAGEM:**

00:45. Os botes comecam a ser arriados.

**GRAFISMO:** Bote 7: sai com 28 de 65 lugares. Bote 1: sai com 12 pessoas para 40 vagas — incluindo Sir Cosmo Duff-Gordon, que depois seria acusado de subornar remadores para nao voltar. Bote 6: sai com 28 de 65. Os numeros aparecem um a um. A capacidade nao utilizada ACUMULA-SE na tela como uma divida.

> **[OVERLAY: ERRO DE PROCESSO]** Botes arriados parcialmente — exercicio de evacuacao do domingo cancelado pelo Cap. Smith. Tripulacao sem treinamento nos davits

**RECONSTITUICAO (grades entre decks — N3 estilistico):** A imagem mais poderosa do documentario. Grade de ferro em primeiro plano, DESFOCADA. Figuras humanas atras, NITIDAS — o metal esta entre nos e eles. Sombras das grades projetadas nos rostos — padrao de prisao. De um lado: corredor iluminado, espaco aberto, direcao dos botes. Do outro: corredor estreito, escuro, sem sinalizacao, sem saida visivel. Close na tranca. Close na mao do comissario. Close nos olhos de uma crianca — os olhos sao a unica parte totalmente visivel do rosto, e NAO olham para a camera; olham para a grade.

> **[OVERLAY: FALHA SISTEMICA]** Grades de classe entre decks = barreiras de evacuacao. Regulamentacao de imigracao transformada em sentenca de morte

**ANDREZA EM CAMPO (Pigeon Forge — replica dos corredores):** Andreza caminha por uma replica do corredor de terceira classe no museu. Estreito. Sinalizacao minima. Compara com o corredor de primeira classe que visitou na SEQ 03.

**APRESENTADORA (Andreza Araujo):** "Olha a diferenca. O corredor de primeira classe: largo, iluminado, sinalizacao clara, acesso direto ao deck de botes. Aqui na terceira classe: estreito, escuro, sem indicacao de saida. Em 1912, a justificativa era regulamentacao de imigracao — separar passageiros para inspecao sanitaria em Ellis Island. Na noite de 14 de abril, essas grades viraram barreiras de evacuacao."

**GRAFISMO MORTALIDADE:** Infografico limpo, cirurgico. Tres circulos representando as tres classes, tamanho proporcional a mortalidade. Barras em escala de cinza — nenhuma cor emocional. Os numeros falam sozinhos:

- Primeira classe: 37% mortalidade (62% sobreviveram)
- Segunda classe: 58% mortalidade (42% sobreviveram)
- Terceira classe: 75% mortalidade (25% sobreviveram)

"Uma crianca de terceira classe tinha mais chance de morrer do que um homem adulto de primeira classe."

Dentro de cada circulo: silhuetas humanas que DESAPARECEM uma a uma, mais rapido no circulo maior. Som: agua subindo. Nenhum narrador durante o grafismo.

**ENTREVISTA (Butler):** "As grades entre decks tinham uma justificativa legal: regulamentacao americana de imigracao exigia separacao sanitaria para inspecao em Ellis Island. Mas na noite de 14 de abril, essas grades se tornaram barreiras de evacuacao. O design que separava por higiene matou por classe."

[SILENCIO — 7 segundos]

**Butler:** "O navio foi PROJETADO para que uns morressem mais que outros. Nao por maldade. Por arquitetura."

**SOM/MUSICA:** Som de agua subindo — lento, inexoravel. Metal da grade vibrando. Nenhuma musica. A aritmetica nao precisa de trilha sonora.

**NOTA DE DIRECAO VISUAL:** Split cromatico: o MESMO navio filmado em DUAS temperaturas de cor. 1a classe com cinza levemente ambar. 3a classe com cinza azulado (prenuncio da agua que vira). A cor SEPARA antes que a narrativa separe.

---

## SEQ 11 — COMPLICACAO 4: O NAVIO QUE VIU E NAO AGIU

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 4 minutos |
| **Tipo de material** | Reconstituicao N3 (ponte Californian — construcao completa) + grafismo distancia + entrevista |
| **Paleta** | Azul Atlantico #1B3A5C (noturno). Vermelho Alerta #8B2500 (foguetes — unica cor saturada) |
| **Entrevistados** | Stephenson (contexto tecnico/regulamentar) |
| **Props/cenografia** | **Ponte do Californian (construcao completa):** Janelas de vidro. Instrumentos de navegacao minimos. Binoculos. Mapa de navegacao. Iluminacao noturna azul frio. Foguetes visiveis pela janela (efeito pratico + CGI) |
| **Value-charge** | Negativo (o sistema falha em MULTIPLOS pontos simultaneamente) |
| **Beat McKee** | Beat 3 — Progressive Complication 4 |
| **OVERLAYS** | HUMANO: Lord interpreta foguetes como festivos / PROCESSO: Operador Marconi autorizado a dormir |

**IMAGEM:**

Dez milhas nauticas. O SS Californian esta parado — seu capitao, Stanley Lord, parou por gelo. Decisao prudente. O operador Marconi do Californian, Cyril Evans, tenta avisar o Titanic sobre o campo de gelo. Phillips responde: "Keep out! Shut up! I'm working Cape Race!"

35 minutos depois, o Titanic bate no iceberg.

Evans vai dormir as 23:30 — permitido pela regulamentacao. Dez minutos antes da colisao.

> **[OVERLAY: ERRO DE PROCESSO]** Regulamentacao permite operador Marconi unico dormir a noite — Californian fica surdo no momento critico

**RECONSTITUICAO (ponte Californian — N3):** Lord na ponte. Azul noturno frio — quase identico a temperatura da agua. Foguetes do Titanic visiveis pela janela — a UNICA cor saturada na sequencia. Vermelhos contra o azul-preto da noite. Pontos de cor que ninguem interpreta. Lord: "Fogos festivos." Ou: "Nao sao foguetes de socorro." Ou: "Nao e comigo." Local Rationality — foguetes nao eram exclusivos de emergencia na epoca.

> **[OVERLAY: ERRO HUMANO]** Cap. Lord interpreta foguetes do Titanic como "fogos festivos" — nao exclusivos de emergencia pela regulamentacao vigente

**ENTREVISTA (Stephenson):** "Lord parou por gelo. Isso e prudencia. Evans avisou o Titanic — e foi mandado calar. Quem e culpado? O capitao que parou? O operador que dormiu? Ou o sistema que permitia que o operador dormisse?"

[SILENCIO — 5 segundos]

**Stephenson:** "Stanley Lord foi condenado pela historia. Viveu o resto da vida tentando limpar seu nome. Morreu sem conseguir. O sistema precisava de um culpado individual. Lord serviu. E enquanto todos olhavam para Lord, ninguem olhava para o sistema."

**SOM/MUSICA:** Silencio noturno. Vento. Um foguete: o assobio da subida, o estalo da detonacao, a chuva das faiscas. Depois: silencio de novo. Ninguem responde.

---

## SEQ 12 — COMPLICACAO 5: O DNA DO DESASTRE

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 5 minutos |
| **Tipo de material** | Filmagem in situ (laboratorio NIST) + microscopia real + modelo 3D + entrevistas Foecke/McCarty |
| **Paleta** | Verde Laboratorio #4A6B5A dominante + Branco Analitico #E8E8E8 (microscopia) |
| **Entrevistados** | Dr. Tim Foecke (momento-chave da entrevista), Dr. Jennifer Hooper McCarty |
| **Props/cenografia** | Laboratorio real NIST — nao construido. Bancada com amostras de rebites recuperados do fundo do mar. Microscopio eletronico. Imagens de microscopia projetadas. Documentos H&W (McCarty) |
| **Value-charge** | Negativo crescente (o "DNA" era economico) |
| **Beat McKee** | Beat 3 — Progressive Complication 5 |
| **GAPs 1+2** | O inimigo estava DENTRO do navio desde o primeiro dia |
| **OVERLAY** | PROCESSO: Rebites de ferro na proa — custo < 0.3% a mais para aco |

**IMAGEM:**

A semente plantada na SEQ 02 finalmente floresce.

**LOCACAO (NIST, Gaithersburg, Maryland):** O laboratorio real de Foecke. Sem cenario construido — o cenario E a locacao. Paredes institucionais. Bancada metalica. Microscopios. A verdade sobre o Titanic esta nesta sala.

**ENTREVISTA (Foecke — MOMENTO-CHAVE):** Interrotron. Close extremo nas maos de Foecke quando descreve os rebites. Camera lenta no rosto quando diz a palavra "centavos."

**Foecke:** "Recuperamos rebites das expedicoes de Cameron ao wreck. Colocamos sob o microscopio. O teor de escoria nos rebites de ferro forjado da proa excedia 3% — em alguns casos, 9%. Isso e... muito. Um rebite com 9% de escoria e fragil. Quebradico. Quando o gelo empurrou as placas, esses rebites nao resistiram."

**MICROSCOPIA REAL:** Imagem de microscopio eletronico. A estrutura cristalina do ferro forjado. As inclusoes de escoria — manchas escuras no metal. A imagem e clinica, impiedosa. E autopsial: o navio e o paciente, o diagnostico e terminal — e foi dado 86 anos depois da morte.

**Pergunta:** "Quanto custaria ter usado rebites de aco em todo o navio?"

[SILENCIO — 7 segundos]

**Foecke:** "Menos de 0.3% do custo total do navio."

> **[OVERLAY: ERRO DE PROCESSO]** Rebites de ferro forjado na proa e popa — economia de menos de 0.3% do custo total. H&W sabia da qualidade inferior (reclamacoes documentadas ao fornecedor)

**Pergunta:** "Quando voce faz essa conta — centavos por passageiro — o que acontece dentro de voce?"

[SILENCIO — 10 segundos. Este e o momento-chave da entrevista inteira. Nao preencher. A camera fica no rosto de Foecke. O espectador ve o cientista processar a emocao do dado.]

**ENTREVISTA (McCarty):** Interrotron. Mesa academica. Documentos de arquivo.

**McCarty:** "Fui aos arquivos de Harland & Wolff em Belfast. Encontrei as reclamacoes sobre a qualidade dos rebites. Eles SABIAM. Harland & Wolff reclamou ao fornecedor. O fornecedor respondeu. E nada mudou. Os rebites foram instalados."

**MODELO 3D:** Distribuicao aco vs ferro no navio. Aco no centro (azul). Ferro na proa e na popa (vermelho). A zona de impacto coincide com a zona vermelha. O mapa fala: economia matou.

**SOM/MUSICA:** Laboratorio: silencio clinico. O zumbido dos equipamentos. O clique da lente do microscopio mudando de aumento. O som da VERDADE sendo extraida — paciente, metodico, irreversivel.

**NOTA DE DIRECAO VISUAL:** Transicao COMPLETA para ambiente cientifico. O verde institucional domina. Nao ha calor nesta imagem. A luz e clinica, impiedosa. O modelo 3D mostrando ferro vs aco usa Vermelho (fragil = perigo) e Azul (resistente).

---

## SEQ 13 — REVERSAL: AS TRES VOZES SILENCIADAS

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 5 minutos |
| **Tipo de material** | Montagem ritmica + reconstituicao N2 (triptico) + entrevista + VO |
| **Paleta** | Monocromatico: Cinza Aco #6B7B8D drenando para quase P&B. Vermelho Alerta #8B2500 sutil nos rostos — o humano resistindo a drenagem |
| **Entrevistados** | Nenhum novo (montagem de material ja captado + VO) |
| **Props/cenografia** | Triptico de tres espacos: (1) Carlisle — perfil, mao sobre planta de botes, marcas sendo apagadas; (2) Andrews — de costas, olhando anteparas, mao apontando para linha que deveria ser mais alta; (3) Phillips — fones, manipulador Morse, papel com "ICE" a centimetros da mao |
| **Value-charge** | PICO NEGATIVO (o sistema funciona — contra a seguranca) |
| **Beat McKee** | Beat 3 — climax das complicacoes |
| **GAP 6** | Nao ha um culpado. Ha algo PIOR: um sistema onde todos estao certos |
| **OVERLAY** | SISTEMICO: 3 alarmes dados, 0 ouvidos — o sistema funciona para silenciar |

**IMAGEM:**

As complicacoes convergem. O Reversal de McKee.

**MONTAGEM RITMICA — O TRIPTICO DAS VOZES SILENCIADAS:**

Tres telas verticais (ou tres momentos montados em sequencia). Cada rosto progressivamente mais desaturado. O sistema drena cor das pessoas como drena a voz.

**TELA 1 — Carlisle (1907):** Perfil. Cabelo grisalho. Mao sobre planta de botes. As 48 marcas dos botes vao sendo APAGADAS uma a uma, como se uma borracha invisivel as removesse. "48 botes." Silencio. "16 botes." Silencio.

**TELA 2 — Andrews:** De costas, olhando para quadro de anteparas. Mao apontando para a linha que deveria ser MAIS ALTA. A linha permanece baixa. A mao cai.

**TELA 3 — Phillips:** De costas, fones de ouvido, mao no manipulador Morse. Papel com "ICE" visivel a centimetros da mao. A mao nao o alcanca — esta ocupada com outro telegrama. Clique do Morse nao para.

> **[OVERLAY: FALHA SISTEMICA]** 3 alarmes dados (Carlisle 1907, Andrews 1911, Phillips 1912). 0 ouvidos. O sistema funciona — para silenciar

**SOM:** Silencio. Depois, um a um, tres sons: o lapis riscando (Carlisle), a regua batendo na mesa (Andrews), o Morse clicando (Phillips). Tres alarmes dados. Zero alarmes ouvidos.

**APRESENTADORA (Andreza Araujo):** "Carlisle propôs 48 botes. Andrews propôs anteparas mais altas. Evans avisou sobre o gelo. Tres homens. Tres alarmes. Tres vezes o sistema fez o que sistemas patologicos fazem: silenciou. Na Bradley Curve, o nivel mais baixo e o patologico — 'quem se importa enquanto nao somos pegos?' O Titanic nao falhou em comunicar. Funcionou como desenhado — para silenciar. E o oposto disso tem nome: celebrar o vermelho. Valorizar quem reporta o problema."

[SILENCIO — 5 segundos]

**APRESENTADORA (Andreza Araujo):** "Nenhum desses decisores planejou matar 1.517 pessoas. Cada um fez o que parecia certo. Na Piramide de Bird, para cada acidente grave existem 600 quase-acidentes e 30.000 desvios. Todos esses desvios pareciam normais. E foi EXATAMENTE por isso que tantos morreram. Investigacao busca causas, nao culpados."

**NOTA DE DIRECAO VISUAL:** A sequencia mais desaturada do Ato II. Quase P&B. A cor esta sendo eliminada — como as vozes. A narrativa drena cor e drena voz ao mesmo tempo. O Vermelho Alerta sobrevive apenas nos rostos — nos labios, nos olhos — o humano resiste a drenagem cromatica, mesmo quando o sistema o cala.

> **>>> TURNING POINT ATO II --> ATO III <<<**
> A evidencia nao e UMA peca — e o PADRAO.
> Camera recua. Swiss Cheese aparece. 5 camadas. Os buracos se alinham.

---

---

# BLOCO 3 — CLIMAX: REVELACAO SISTEMICA

**ATO III (parte 1) | ~7 minutos | Beat 4 (Climax)**
**Value-Charge: NEGACAO DA NEGACAO**
**Arco cromatico: PRETO E BRANCO PURO — a cor morreu**

---

## SEQ 14 — CLIMAX: O SISTEMA

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 7 minutos |
| **Tipo de material** | CGI Swiss Cheese animado + time-lapse drift + entrevista (montagem) + VO |
| **Paleta** | **P&B TOTAL.** Preto Abissal + Branco Analitico. Unica excecao: Vermelho Alerta #8B2500 para os "buracos" do Swiss Cheese acendendo + TODOS os overlays de erro reaparecem |
| **Entrevistados** | Montagem de Foecke, Stephenson, Butler — nenhuma entrevista nova, montagem de material ja captado convergindo para a revelacao |
| **Props/cenografia** | Nenhum cenario fisico — inteiramente CGI/animacao. P&B e a linguagem da analise |
| **Value-charge** | NEGACAO DA NEGACAO |
| **Beat McKee** | Beat 4 — Climax |
| **Integracao SST** | Swiss Cheese de Reason (5 camadas), Dekker (drift, local rationality), Schein (pressupostos basicos), Westrum (score 6/25, cultura patologica) |
| ***** CLIMAX DO ARCO McKEE *** | |

**IMAGEM:**

Tudo converge. O sistema se revela.

**DISPOSITIVO — REAPARECEM TODOS OS OVERLAYS:** Antes do Swiss Cheese, todos os 13 overlays de erro marcados ao longo do documentario reaparecem na tela, um a um, empilhando-se no canto inferior. Engrenagens, silhuetas, redes — acumulam-se como evidencia num tribunal. Quando todos estao visiveis (5 segundos), eles se REORGANIZAM — voam para suas posicoes nas 5 camadas do Swiss Cheese. Os erros de processo viram buracos nas camadas. O espectador VE a anatomia do desastre montada diante dos seus olhos.

**CGI — SWISS CHEESE DE REASON (animacao):** Fundo preto. Cinco camadas em branco translucido, suspensas verticalmente como fatias de queijo. Cada camada representa um nivel do modelo de Reason:

**Camada 1 — Regulacao (Board of Trade):** Regra de 1894. 18 anos sem atualizacao. Um buraco ACENDE em vermelho quando a regra e nomeada.

**Camada 2 — Organizacao (White Star Line):** Pressao comercial. Custo sobre seguranca. Carlisle vetado. Um buraco acende.

**Camada 3 — Supervisao (Capitao Smith, Ponte):** Velocidade mantida. Avisos ignorados. Procedimento padrao. Um buraco acende.

**Camada 4 — Precondicoes (Phillips/Marconi, tripulacao):** Operador comercial, nao de seguranca. Exercicio de botes cancelado. Tripulacao sem treinamento. Um buraco acende.

**Camada 5 — Atos no Momento (Fleet, Murdoch):** Sem binoculos. 37 segundos. Botes lancados parcialmente. Grades trancadas. Um buraco acende.

Os cinco buracos PULAM em vermelho. A camera RECUA. Os buracos se alinham — um unico feixe vermelho atravessa as cinco camadas. O vermelho e a unica cor no frame. E a cor do alerta que ninguem ouviu.

**TIME-LAPSE DRIFT (1894 --> 1912):** P&B. Linha temporal em branco. Eventos como nodos. 18 anos comprimidos em 30 segundos. Cada decisao alimenta a seguinte. O drift nao e inercia — e aceleracao. Quanto mais tempo sem acidente, mais rapido o drift. A visualizacao mostra o que Dekker descreve: normalizacao do desvio.

**MONTAGEM DE ENTREVISTAS (fragmentos):**

**Foecke:** "Os rebites eram o que sempre usaram."
**Stephenson:** "Phillips fazia o que a Marconi pagava para fazer."
**Butler:** "Smith seguia o procedimento de 40 anos."

**APRESENTADORA (Andreza Araujo):** "Dekker chamou de Local Rationality. Cada decisor agia racionalmente dentro do seu contexto. Na PepsiCo, quando comecei o trabalho de transformacao cultural, encontrei a mesma coisa: ninguem fazia nada 'errado' — cada um seguia seu procedimento, sua meta, sua rotina. E as pessoas se machucavam. Porque o sistema estava errado, nao as pessoas."

[SILENCIO — 3 segundos]

**APRESENTADORA (Andreza Araujo):** "Schein disse: o pressuposto mais perigoso e o que nunca precisa ser articulado. E a Cebola da Cultura que eu uso nos meus diagnosticos — o comportamento e a camada de fora, a que voce ve. Mas o pressuposto esta no nucleo, invisivel. O pressuposto do Titanic era: 'Somos grandes demais para falhar.' Ninguem o dizia porque todos o respiravam."

**GRAFISMO:** Score Westrum: 6 de 25 — cultura PATOLOGICA. O numero aparece em branco sobre preto.

**APRESENTADORA (Andreza Araujo):** "O Titanic NUNCA foi seguro. O sistema existia para afirmar que era. E eu digo sempre: a ausencia de acidentes nao significa cultura forte de seguranca. As vezes significa que ninguem esta reportando."

**SOM/MUSICA:** Silencio quase total. O som do Swiss Cheese e geometrico — cliques suaves quando os buracos acendem, como um mecanismo de relogio. Quando os buracos se alinham: um tom grave, continuo, ressonante — o som de uma estrutura que cede. Depois: agua. O rugido da agua entrando. Mesmo som da SEQ 07 — mas agora o espectador entende o que ELE significa.

**NOTA DE DIRECAO VISUAL:** O P&B total e a decisao cromatica mais radical do documentario. A cor MORREU. O que resta e ESTRUTURA: camadas, buracos, alinhamento. Storaro em Reds: "When you remove color, you remove emotion — and you see the SYSTEM." A ausencia de cor diz ao espectador: aqui nao ha emocao — ha compreensao.

---

---

# BLOCO 4 — RESOLUCAO: LEGADO + LICOES

**ATO III (parte 2) | ~22 minutos | Beat 5 (Resolution/Legado)**
**Value-Charge: AMBIGUO --> URGENCIA --> RESPONSABILIDADE**
**Arco cromatico: Retorno parcial de cor (Sepia dessaturado) --> Cinza editorial --> Azul Atlantico --> Preto Abissal**
**LICOES APRENDIDAS integradas organicamente (nao como lista)**

---

## SEQ 15 — CONSEQUENCIAS: O QUE O MUNDO FEZ

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 5 minutos |
| **Tipo de material** | Arquivo + grafismo + reconstituicao N1 (inqueritos) + VO |
| **Paleta** | Retorno PARCIAL de cor: Sepia documental + Cinza Aco. Ouro Edwardiano em flashbacks dos inqueritos — mas 2 stops subexposto, opaco. O ouro voltou como NOSTALGIA, nao como progresso |
| **Entrevistados** | Andreza Araujo (ponte para hoje) |
| **Props/cenografia** | Reconstituicao inqueritos (N1 — simbolica): cadeira, mesa, documentos. Paleta do Ato I mas envergonhada |
| **Value-charge** | Ambiguo positivo (mudancas reais, mas justica parcial) |
| **Beat McKee** | Beat 5 — Resolucao (inicio) |
| **Licoes integradas** | Licao 1 ("A Regra Que Protegia Era a Que Matava") como CONTEXTO. Licao 2 ("O Luxo Como Anestesia") como IRONIA |

**IMAGEM:**

O mundo reagiu. Mas como?

**ARQUIVO + GRAFISMO:** SOLAS 1914 — Safety of Life at Sea. A primeira convencao internacional de seguranca maritima. Botes salva-vidas para TODOS. Radio telegrafia 24 horas com operador dedicado. International Ice Patrol (US Coast Guard, ativa ate hoje — 2026). Exercicios de evacuacao obrigatorios. Reformas reais. Vidas salvas.

**RECONSTITUICAO (inqueritos — N1):** O inquerito americano do senador Smith — direto, agressivo, sem reverencia pela hierarquia britanica. "Laxity of regulation, indifference to danger, overconfidence, inadequate equipment."

O inquerito britanico de Lord Mersey — cauteloso, deferente ao establishment. Absolve o Board of Trade. Sobre Smith: "He was doing what other skilled men would have done." A instituicao que regulava julgou que a instituicao que regulava nao havia errado.

**APRESENTADORA (Andreza Araujo):** "A ironia do inquerito britanico e que ele praticou EXATAMENTE o mecanismo que deveria condenar. O juiz fez o que juizes fazem — protegeu a instituicao. Na linguagem de Hopkins, e o indicador #2 em FALHA: compromisso da alta gestao com seguranca. Mas que compromisso pode existir quando a 'alta gestao' INCLUI o regulador? Quando eu faco diagnostico cultural numa empresa, a primeira coisa que pergunto e: quem audita quem? Se a resposta for 'nos mesmos' — ja sei onde esta o problema."

A Licao 1 emerge NAO como titulo, mas como COMPREENSAO. O espectador entende: a regra que protegia — a Merchant Shipping Act de 1894 — era a regra que matava. E o inquerito que deveria expor essa falha a reproduziu.

A Licao 2 se insinua visualmente — nao como texto, mas como IRONIA cromatica. O ouro do Ato I retorna nos flashbacks dos inqueritos, mas esta opaco, subexposto. O luxo do Titanic — os lustres, os saloes, a grandiosidade que anestesiava a percepcao de risco — ecoa na pompa dos inqueritos. A mesma fachada, a mesma funcao: parecer que o sistema esta sendo consertado.

**SOM/MUSICA:** Som de tribunal — murmurio, martelo do juiz. Depois: silencio. O silencio de uma conclusao insuficiente.

---

## SEQ 16 — A FIX QUE MATA: EASTLAND + BOEING MAX

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 4 minutos |
| **Tipo de material** | Arquivo fotografico (Eastland 1915 — sepia, NAO colorizado) + grafismo comparativo + entrevista |
| **Paleta** | Sepia fotografico (arquivo 1915) + Cinza Aco. Progressao temporal: sepia 1912 --> P&B 1915 --> cor desaturada 2018. A ESTRUTURA do frame permanece identica: destrocos, agua, consequencias |
| **Entrevistados** | Andreza Araujo (momento-chave) |
| **Props/cenografia** | Nenhuma construcao — arquivo e grafismo |
| **Value-charge** | Negativo (a licao NAO foi aprendida) |
| **Beat McKee** | Beat 5 — complicacao na resolucao |
| **GAP 7** | A "cura" pos-Titanic matou mais num unico evento |
| **Licao integrada** | Licao 6 ("A Cura Que Mata") como REVELACAO DO PARADOXO |

**IMAGEM:**

**TEMPO 1 — PROGRESSO:** Montagem rapida das reformas SOLAS. Botes sendo instalados em navios. Operadores de radio permanentes. Ice Patrol. Sensacao de PROGRESSO. Musica ascendente (a unica musica composta do documentario — breve, esperancosa). Paleta recuperando tons dourados.

**CORTE SECO.**

**TEMPO 2 — PARADOXO:**

1915. Rio Chicago. 24 de julho. O SS Eastland — um navio de passageiros que JA ERA conhecido por problemas de estabilidade — recebe botes salva-vidas adicionais como parte das novas exigencias pos-Titanic. O peso extra, adicionado ao conves superior, agrava a instabilidade.

2.572 passageiros a bordo — trabalhadores da Western Electric e suas familias, a caminho de um piquenique de empresa. O Eastland adernou no cais. Tombou. 848 mortos.

**ARQUIVO:** Fotografia do Eastland tombado no rio Chicago. Corpos sendo retirados da agua. A foto e mantida em SEPIA REAL — decisao moral: nao colorizar. Manter em sepia e ato de respeito.

Texto sobreposto, letra por letra: "24 julho 1915. 848 mortos. A 'cura' para o Titanic."

**SILENCIO TOTAL — 5 segundos.** Sem som, sem narrador, sem musica. O espectador SENTE o paradoxo antes de processa-lo intelectualmente.

**APRESENTADORA (Andreza Araujo):** "Dekker disse: a fix que ataca o sintoma sem entender o sistema cria NOVO desastre. O SOLAS exigiu botes para todos. Ninguem perguntou: e se o peso dos botes matar antes do naufragio? E a Cebola da Cultura ao contrario — mudaram a casca sem tocar no nucleo. Na minha experiencia, licoes aprendidas representam 25% dos acidentes evitaveis. Mas so quando a licao muda crenca, nao formulario."

**TRANSICAO — Boeing 737 MAX:** A mesma anatomia, 106 anos depois.

**APRESENTADORA (Andreza Araujo):** "Em 2018, a FAA delegou ao proprio fabricante — a Boeing — a certificacao do sistema MCAS. A Boeing classificou como 'nao critico.' Dois avioes cairam. Lion Air 610, outubro de 2018: 189 mortos. Ethiopian Airlines 302, marco de 2019: 157 mortos. 346 vidas."

**Pergunta (off):** "A FAA aprendeu O QUE aconteceu ou POR QUE aconteceu?"

[SILENCIO — 7 segundos]

**APRESENTADORA (Andreza Araujo):** "Reformaram o processo de certificacao. Mais supervisores da FAA. Revisao do ODA. Reformas reais. Mas o modelo fundamental — onde o fabricante desenvolve E certifica — permanece. Os incentivos estruturais permanecem. Se aprenderam apenas 'o que,' o proximo 'Eastland' pode ser o proximo aviao com um sistema que a reforma nao previu."

**GRAFISMO COMPARATIVO:** Split-screen triplo. ESQUERDA: Merchant Shipping Act 1894, close na Rule 12. CENTRO: Titanic em perfil, transbordando a regra. DIREITA: documento FAA com selo "DELEGATED." Uma LINHA VERMELHA continua conecta as tres imagens — a mesma falha, 106 anos de distancia. A linha pulsa como batimento cardiaco. Quando as tres imagens se alinham, o pulso PARA.

**SOM/MUSICA:** Musica ascendente breve (Tempo 1 — esperanca). Corte seco para silencio (Eastland). Estatica de comunicacao (transicao para MAX). Depois: silencio de novo. O padrao.

---

## SEQ 17 — PONTE: OS TITANICS DE HOJE

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 4 minutos |
| **Tipo de material** | Montagem paralela (arquivo + grafismo editorial). VISUAL, nao discursivo |
| **Paleta** | Cor moderna DESATURADA: cinza-azulado com pontos de Vermelho Alerta. Nao e P&B historico — e presente drenado. O mundo de HOJE tem cor, mas cor sem vida |
| **Entrevistados** | Andreza Araujo (provocacao final) |
| **Props/cenografia** | Nenhuma construcao — montagem editorial. Andreza em campo (locacao industrial moderna) |
| **Value-charge** | Negativo --> urgencia presente |
| **Beat McKee** | Beat 5 — ponte para o publico |
| **Licoes integradas** | Licoes 3, 4, 5, 7, 8 como TECIDO NARRATIVO (nao como lista) |

**IMAGEM:**

A montagem mais provocativa do documentario. VISUAL — as imagens falam. Lado a lado, MESMA composicao, MESMA escala, so a epoca muda:

**Proa do Titanic (azul) / Fuselagem do 737 MAX (cinza).** O mesmo perfil aerodinamico. A mesma aposta na velocidade. A mesma confianca no tamanho.

**Rebites de ferro do Titanic (sepia) / Revestimento ACM da Grenfell Tower (cinza).** O mesmo material barato. A mesma decisao economica. A mesma fatalidade.

**Carlisle em silencio no inquerito (monocromatico) / Engenheiro da Boeing em mensagem interna: "This airplane is designed by clowns" (cor desaturada).** O mesmo silenciamento. 106 anos de distancia.

**Board of Trade 1894 (sepia) / FAA 2018 (cor):** "Conforme." "Delegated." O mesmo carimbo. A mesma captura.

As imagens RIMAM visualmente. A composicao e identica; so a epoca muda. A cor diz: "diferente epoca, mesmo silencio."

**APRESENTADORA (Andreza Araujo):** Nao narra. Cede a voz ao SILENCIO da montagem. As perguntas emergem dos paralelos visuais — nao precisam ser articuladas. A apresentadora aparece BREVEMENTE em campo — numa fabrica moderna, capacete, olhando para a camera — sem falar. O olhar diz: voce reconhece isso?

**APRESENTADORA (Andreza Araujo — provocacao final):**

"A TSMC produz 90% dos chips avancados do mundo. Uma fabrica. Uma ilha. Um ponto de falha. O mercado de derivativos excede 600 trilhoes de dolares em valor nocional — nenhum regulador individual compreende o sistema inteiro. A inteligencia artificial esta sendo integrada em sistemas criticos com processos de certificacao que estao sendo escritos ENQUANTO a tecnologia e implantada."

[SILENCIO — 5 segundos]

"Estamos em 1907. Os davits estao instalados. Os botes ainda nao foram colocados. E ninguem esta prestando atencao porque o navio e lindo e o mar esta calmo."

**SOM/MUSICA:** Nenhuma musica. Os paralelos visuais se sucedem em silencio. A normalidade sonora AMPLIFICA o horror do conteudo. O ordinario e o terrificante.

**NOTA DE DIRECAO VISUAL:** A estetica e de COR EDITORIAL: desaturada mas reconhecivel. O mundo de HOJE tem cor — mas cor sem vida. Quando a composicao e identica entre Titanic e Boeing, entre Carlisle e o engenheiro, a cor diz: "diferente epoca, mesmo silencio."

---

## SEQ 18 — O PIER: ONDE A HISTORIA TERMINOU

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 4 minutos |
| **Tipo de material** | Locacao real (Pier 54/Chelsea Piers, NYC) + arquivo fotografico + VO |
| **Paleta** | Cor moderna com sobreposicao sepia (passado e presente no mesmo frame). Azul do rio Hudson. Cinza do concreto de Manhattan |
| **Entrevistados** | Andreza Araujo (em campo — NYC) |
| **Props/cenografia** | Locacao real: Pier 54, Chelsea, Manhattan. O pier onde o RMS Carpathia atracou com 710 sobreviventes em 18 de abril de 1912 |
| **Value-charge** | Melancolico --> esperanca fragil |
| **Beat McKee** | Beat 5 — transicao para fechamento |
| **Funcao narrativa** | Localizar a historia no ESPACO real — nao e mito, aconteceu AQUI |

**IMAGEM:**

**ANDREZA EM CAMPO (Pier 54, NYC):** Andreza caminha pelo pier — hoje um parque publico sobre o Hudson River. Atras dela, Manhattan. O pier esta transformado — onde antes atracavam transatlanticos, hoje ha pessoas correndo, andando de bicicleta, tomando cafe. A normalidade do presente sobre o trauma do passado.

**APRESENTADORA (Andreza Araujo):** "Aqui. Neste pier. Na madrugada de 18 de abril de 1912, o RMS Carpathia atracou com 710 sobreviventes. Trinta mil pessoas esperavam no cais. Familias com cartazes. Nomes escritos em papel. E a cada passageiro que descia, um nome era chamado. E para cada nome chamado, dezenas nao eram."

**ARQUIVO:** Fotografias de 1912 — o Carpathia atracado, multidoes no pier, rostos na espera. As fotos se sobrepõem levemente a imagem moderna do pier — transparencia a 30%. Passado e presente coexistem no mesmo frame. As silhuetas de 1912 caminham onde hoje correm joggers.

**APRESENTADORA (Andreza Araujo):** "Os sobreviventes desciam em silencio. Muitos ainda em roupas de dormir. Alguns enrolados em cobertores do Carpathia. As mulheres procuravam maridos. As criancas procuravam pais. A banda do Salvation Army tocava hinos. E a chuva comecou."

[SILENCIO — 5 segundos. Andreza olha para o rio.]

**APRESENTADORA (Andreza Araujo):** "Ida Straus nao desceu. Benjamin Guggenheim nao desceu. John Jacob Astor nao desceu. Wallace Hartley e seus musicos nao desceram. E 1.517 familias comecaram a entender que ninguem mais ia descer."

**ARQUIVO:** Close numa fotografia: lista manuscrita de sobreviventes afixada no escritorio da White Star Line em Nova York. Fila de pessoas consultando a lista. A mesma fila — em foto ao lado — consultando lista de mortos.

**APRESENTADORA (Andreza Araujo):** "Eu comeco todo diagnostico de cultura de seguranca com uma pergunta: quem pagou o preco? Nao o preco financeiro — o preco humano. Porque quando a gente esquece quem pagou, a gente comeca a normalizar de novo."

**SOM/MUSICA:** Som ambiente do pier moderno — vento do Hudson, passos, bicicletas, vozes distantes. Sobre ele, em volume MUITO baixo, quase subliminar: o som do Morse da SEQ 01. O espectador talvez nao o perceba conscientemente — mas o corpo reconhece. Circularidade sonora.

**NOTA DE DIRECAO VISUAL:** A sobreposicao sepia/cor e o dispositivo-chave: o passado nao "esta la" — esta AQUI. As mesmas pedras, o mesmo rio, o mesmo ceu. Quando Andreza caminha sobre o pier, ela caminha sobre historia. A camera alterna entre planos abertos (o pier hoje, luminoso) e closes nas fotos de 1912 (escuras, granuladas, intimas). A tensao visual e entre ESPACO (o mesmo) e TEMPO (diferente).

---

## SEQ 19 — EPILOGO: O MAR

| Campo | Detalhe |
|-------|---------|
| **Duracao** | 3 minutos |
| **Tipo de material** | Arquivo submarino (acervo Cameron) + texto + silencio + VO |
| **Paleta** | Azul Atlantico #1B3A5C --> Preto Abissal #0A0A0F. Circularidade cromatica COMPLETA: azul-abissal abre (SEQ 01), azul-abissal fecha (SEQ 19). Mas a funcao mudou: na abertura era convite, no fechamento e despedida |
| **Entrevistados** | Nenhum. Andreza fecha sozinha |
| **Props/cenografia** | Nenhuma construcao — o cenario e o oceano real |
| **Value-charge** | Ambiguo --> responsabilidade transferida ao publico |
| **Beat McKee** | Beat 5 — fechamento |
| **Licao integrada** | Licao 8 ("Voce Esta Dentro de um Drift Agora") + Call to Action ("E Voce?") como FECHAMENTO |

**IMAGEM:**

Retorno ao fundo do mar. A mesma luz dos ROVs do prologo. Os mesmos azuis. O mesmo silencio. Mas agora o espectador SABE o que o azul contem.

Os sapatos enfileirados no leito oceanico — marca de corpos que se desfizeram. As luminarias art deco cobertas de rusticles. Elementos de mogno preservados pelo frio e pela pressao. O silencio absoluto de 3.800 metros.

**TELA PRETA — 3 segundos.**

Depois: o som do Morse — ··· ——— ··· — uma ultima vez. Fraco. Distante. Como eco de algo que nunca deveria ter sido necessario.

Depois: ESPELHO. A camera filma uma superficie reflexiva — agua? metal polido? — que devolve o olhar. O conceito de reflexo. O espectador e olhado de volta.

**APRESENTADORA (Andreza Araujo):** "Este navio conta uma historia. Nao a historia de um iceberg. A historia de um sistema. De decisoes que pareciam razoaveis. De vozes que foram silenciadas. De uma civilizacao tao apaixonada pelo seu progresso que esqueceu de perguntar: 'e se estivermos errados?' Eu comecei como engenheira civil. Descobri seguranca pela porta dos fundos. E aprendi que seguranca nao e sobre normas. E sobre gente. E sobre cuidar de gente."

[SILENCIO — 5 segundos]

**APRESENTADORA (Andreza Araujo):** "Voce nao e Carlisle. Provavelmente nao esta projetando navios nem certificando avioes. Mas voce ESTA dentro de um sistema. Eu atendi 33 mil funcionarios em 19 paises na PepsiCo. Cada fabrica, cada pais, cada cultura — e em TODOS encontrei a mesma coisa: regras que 'funcionam' porque nunca foram testadas. Sinais de alarme que ninguem ouve. Drifts lentos e invisiveis movendo o baseline do 'normal' para mais perto do iceberg. Em 180 dias, mudando a cultura — nao o formulario —, reduzimos a acidentalidade em 52%. Em cinco anos, 94%. Nao porque as pessoas passaram a seguir regras. Porque passaram a CUIDAR umas das outras."

Fade lento para imagens submarinas do wreck — os sapatos, as luminarias, o silencio.

**APRESENTADORA (Andreza Araujo):** "Na proxima reuniao em que alguem disser 'acho que isso pode dar errado' — observe o que acontece. Observe os rostos. Observe o silencio. Celebre o vermelho. Valorize quem reporta o problema. Pergunte todo dia: o que pode me matar hoje? Como evitar isso? Seguranca e um valor, nao uma prioridade que muda conforme a situacao. Valores sao transcircunstanciais — estao acima das circunstancias. Temos uma pagina em branco para escrever. Tenha coragem para fazer a diferenca. O mar nao mudou. A pergunta e: e voce?"

**TEXTO (branco sobre preto — as duas cores mais honestas):**

"1.517 mortos."

"Alexander Carlisle propôs 48 botes em 1907."

"Foram instalados 20."

"A regra que permitiu tinha 18 anos."

[PAUSA — 5 segundos]

"Na sua industria, quantas regras estao esperando seu iceberg?"

**Tela preta.**

**O mar nao mudou. A pergunta e: e voce?**

**FIM.**

**SOM/MUSICA:** Codigo Morse — ··· ——— ··· — fraco, como eco distante. Depois sons subaquaticos naturais — identicos ao prologo. Circularidade sonora completa. O mesmo murmúrio abissal. Calma, precisa, respeitosa com o que esta no fundo do mar. Absolutamente determinada a que a verdade suba a superficie. Nenhuma musica. O silencio final e total — dura ate o espectador sair da sala.

---

---

# VALIDACOES

## Step 1: Checklist de Integracao SST-Narrativa

| Criterio | Status | Evidencia |
|----------|--------|-----------|
| Dekker (5 etapas) integrado como MOTOR narrativo, nao como citacao | OK | Etapa 4 (drift) e o arco do Ato II inteiro. Local Rationality e a logica de cada personagem. Etapa 5 (mudancas sistemicas) e SEQ 15-16 |
| Reason (Swiss Cheese) e o CLIMAX visual | OK | SEQ 14 e inteiramente construida sobre o modelo. 5 camadas animadas. Buracos acendendo em vermelho. Overlays reorganizados no queijo |
| Schein (3 niveis) integrado no arco cromatico | OK | Nivel 1 (artefatos/luxo) = ouro Ato I. Nivel 3 (pressupostos) = P&B Ato III. A transicao cromatica E a transicao de Schein |
| Westrum (tipologia) usada para diagnostico, nao para rotulo | OK | Score 6/25 aparece no climax. A cultura patologica e DEMONSTRADA pelo silenciamento (SEQ 13), nao apenas mencionada |
| Hopkins (5 indicadores) mapeados nos personagens | OK | Indicador #1 (reportabilidade) = Carlisle/Andrews. #2 (compromisso gestao) = Board of Trade. #4 (prioridade seguranca) = luxo vs botes. #5 (comunicacao) = grades 3a classe |
| Reason (4 subculturas) presentes nas complicacoes | OK | Reporting = SEQ 08/13. Just = Carlisle silenciado. Learning = Eastland/SEQ 16. Flexible = Phillips/sistema Marconi |
| Paralelos contemporaneos VERIFICAVEIS (fontes reais) | OK | Boeing MAX: Transportation Committee Report 2020. Grenfell: Inquiry 2019-2024. Eastland: historico verificado |
| SST serve a NARRATIVA, nao o contrario | OK | Nenhum framework e mencionado por nome ao espectador (exceto Swiss Cheese no climax). Os mecanismos sao MOSTRADOS, nao explicados |
| Historias de passageiros humanizam ANTES dos erros | OK | SEQ 03 inteira dedicada a Astor, Guggenheim, Straus, Molly Brown, banda — antes de entrar nos erros (SEQ 04+) |
| Locacoes em campo enriquecem a narrativa | OK | Pigeon Forge (SEQ 03, 10), NYC Pier 54 (SEQ 18) — conexao fisica com a historia |
| Abertura com SOS Morse cria urgencia imediata | OK | SEQ 01 abre com Morse antes do mergulho — circularidade com SEQ 19 (Morse final) |
| Marcacao de erros visivel ao longo do documentario | OK | 13 overlays marcados, reorganizados no Swiss Cheese do climax (SEQ 14) |

## Step 2: Validacao Proporcoes Bernard

| Componente | Meta | Real | Status |
|------------|------|------|--------|
| **Setup (Ato I)** | ~25% (~26 min) | 29 min (SEQ 01-06) | 27.6% — OK |
| **Confrontacao (Ato II)** | ~50% (~52 min) | 44 min (SEQ 07-13) | 41.9% — ACEITAVEL (comprimido pelas novas SEQ no Ato I e III) |
| **Resolucao (Ato III)** | ~25% (~26 min) | 32 min (SEQ 14-19) | 30.5% — OK (expandido por SEQ 18 NYC) |
| **TOTAL** | 105 min | 105 min | OK |

### Proporcao de VO (Voice-Over)

| Tipo | Duracao estimada | % do total |
|------|-----------------|-----------|
| Apresentadora (Andreza) | ~25 min | 23.8% |
| Entrevistas (som direto) | ~25 min | 23.8% |
| VO narrador | ~5 min | 4.8% |
| Arquivo/grafismo/reconst. (sem voz) | ~20 min | 19.0% |
| Silencio + som ambiente | ~12 min | 11.4% |
| CGI/animacao com VO | ~10 min | 9.5% |
| Locacao campo (Andreza) | ~6 min | 5.7% |
| Musica composta | ~2 min | 1.9% |
| **VO total (Andreza + narrador)** | **~30 min** | **~28.6%** | **< 40% — OK** |

## Step 3: Checklist Final de Qualidade

| # | Criterio | Status | Nota |
|---|----------|--------|------|
| 1 | Controlling Idea testavel em cada sequencia | OK | Cada SEQ reforca ou complica "arrogancia tecnologica + silenciamento = destruicao" |
| 2 | Questao Dramatica nunca respondida com sim/nao | OK | Resposta emerge em camadas ao longo dos 3 atos — nunca redutivel |
| 3 | 5 Beats McKee claramente identificaveis | OK | Beat 1 (SEQ 01-05), Beat 2 (SEQ 06-07), Beat 3 (SEQ 08-13), Beat 4 (SEQ 14), Beat 5 (SEQ 15-19) |
| 4 | Turning Points bem marcados (visual + narrativo) | OK | TP1: flash branco SEQ 06 / TP2: Swiss Cheese SEQ 13-14 |
| 5 | Progressive Complications em ordem crescente | OK | Avisos < Botes < Classe < Californian < DNA < Vozes Silenciadas — cada complicacao pior |
| 6 | Climax e revelacao SISTEMICA, nao espetacular | OK | SEQ 14: P&B puro, geometria forense, overlays reorganizados — compreensao |
| 7 | Resolucao nao e "moral da historia" — e PERGUNTA | OK | SEQ 19 termina com pergunta ao espectador, nao com conclusao |
| 8 | Licoes Aprendidas integradas organicamente | OK | 8 licoes distribuidas em SEQ 15-19 como tecido narrativo, nao como lista |
| 9 | Arco cromatico coerente | OK | Preto (Morse) --> Ouro --> Cinza --> Verde --> P&B --> Azul-Preto. Circularidade SEQ 01/19 |
| 10 | Reconstituicoes FRAGMENTADAS, nunca naturalistas | OK | N1, N2, N3 aplicados. Nenhuma cena completa. Espectador sabe que e reconstituicao |
| 11 | Entrevistas com pontos de [SILENCIO] | OK | Silencios de 3, 5, 7, 10 segundos marcados em cada entrevista |
| 12 | Props-evidencia presentes | OK | Rebites, cadeado binoculos, blueprints, telegrama, Merchant Shipping Act, relogio, grade, bloco de gelo |
| 13 | VO <= 40% | OK | ~28.6% estimado |
| 14 | Proporcoes Bernard respeitadas | OK | 27.6% / 41.9% / 30.5% |
| 15 | Teste do Trem funcional | OK | Cada estacao narrativa tem funcao — nenhuma removivel sem colapso do arco |
| 16 | Negacao da Negacao alcancada no climax | OK | SEQ 14: nao negligencia, nao incompetencia — negligencia NORMALIZADA como paradigma |
| 17 | Call to Action nao e moralizante — e convite | OK | "Observe o que acontece" — nao "mude o mundo" |
| 18 | Paralelos contemporaneos verificaveis | OK | Fontes primarias citadas: Transportation Committee, Grenfell Inquiry |
| 19 | Circularidade narrativa (abertura/fechamento) | OK | Morse abre (SOS), Morse fecha (eco). Mar abre, mar fecha. Preto abre, preto fecha |
| 20 | Historias humanas investem o espectador ANTES dos erros | OK | SEQ 03 humaniza. SEQ 18 (NYC) localiza. Os erros (SEQ 04+) doem MAIS |
| 21 | Overlays de erro acumulam e convergem no climax | OK | 13 overlays marcados ao longo do doc reorganizam-se no Swiss Cheese |
| 22 | Locacoes em campo (Pigeon Forge, NYC) integradas | OK | Pigeon Forge (SEQ 03 bloco gelo, SEQ 10 corredores), NYC (SEQ 18 pier) |
| 23 | SOS Morse como moldura sonora | OK | Abre (urgencia), fecha (eco/memoria). Circularidade |

---

## MAPA DE INTEGRACAO — LICOES NAS SEQUENCIAS

| Licao | Onde aparece | Como aparece |
|-------|-------------|--------------|
| L1 — A Regra Que Protegia Era a Que Matava | SEQ 09 (setup), SEQ 15 (contexto) | Grafismo drift + VO sobre captura regulatoria |
| L2 — O Luxo Como Anestesia | SEQ 02-03 (implicita), SEQ 15 (ironia cromatica) | Ouro Ato I como fachada; retorno opaco nos inqueritos |
| L3 — Ninguem Acorda Planejando Matar 1.517 Pessoas | SEQ 13 (reversal), SEQ 14 (climax) | Swiss Cheese + "Todos estavam certos. 1.517 morreram." |
| L4 — O Sistema Que Silencia o Alarme | SEQ 05, 08, 13 (arco do silenciamento) | Carlisle/Andrews/Phillips — triptico progressivo |
| L5 — 18 Anos de Decisoes Razoaveis | SEQ 09 (grafismo drift), SEQ 14 (time-lapse) | Regra imovel, navio crescendo — o drift visualizado |
| L6 — A Cura Que Mata | SEQ 16 (revelacao central da sequencia) | Eastland como paradoxo visceral + transicao para Boeing MAX |
| L7 — O Preco da Classe | SEQ 10 (centro da sequencia) | Grades entre decks + grafismo mortalidade + Pigeon Forge |
| L8 — Voce Esta Dentro de um Drift Agora | SEQ 17-19 (ponte + pier + epilogo) | Montagem paralela + NYC pier + espelho + call to action |

---

## MAPA DE FRAMEWORKS SST POR SEQUENCIA

| SEQ | Dekker | Reason | Schein | Westrum | Hopkins |
|-----|--------|--------|--------|---------|---------|
| 01 | — | — | — | — | — |
| 02 | Etapa 1 (contexto) | — | Nivel 1 (artefatos) | — | — |
| 03 | — | — | Nivel 1 (luxo como crenca) | — | — |
| 04 | Etapa 2 (Andrews SABIA) | — | Nivel 2 vs 3 | — | Ind. #4 |
| 05 | — | — | — | Mensageiro punido | Ind. #1 |
| 06 | Local Rationality | Camada 5 (atos) | — | — | — |
| 07 | Etapa 2 | Camada 4 (precondicoes) | — | — | — |
| 08 | Local Rationality | Camada 3 (supervisao) + Reporting FALHA | — | — | Ind. #1 |
| 09 | Etapa 4 (drift) | Camada 1 (regulacao) | — | — | Ind. #2 |
| 10 | — | Camada 2 (organizacao) | Nivel 3 (pressupostos) | — | Ind. #5 |
| 11 | Local Rationality + Second Victim | Camada 3 + Flexible FALHA | — | — | — |
| 12 | Etapa 3 (evidencia) | — | — | — | — |
| 13 | — | Reporting + Just FALHA | — | PATOLOGICA | Ind. #1 |
| 14 | Drift + Local Rationality | Swiss Cheese COMPLETO | Nivel 3 | Score 6/25 | — |
| 15 | Etapa 5 (mudancas) | Learning FALHA | Nivel 2 vs 3 | — | Ind. #2 |
| 16 | Etapa 5 (paradoxo) | Learning FALHA | — | — | — |
| 17 | Drift PRESENTE | — | — | PATOLOGICA (hoje) | Todos |
| 18 | — | — | — | — | — |
| 19 | — | — | Nivel 3 (inconsciente) | — | — |

---

## FICHA TECNICA RESUMIDA

| Item | Especificacao |
|------|--------------|
| Cenarios a construir (completos) | 4: Sala Marconi, grades entre decks, ninho-de-corvo, ponte Californian |
| Cenarios parciais | 3: sala projetos H&W, estaleiro Belfast (fornalha), sala inquerito |
| Locacoes reais | 3: laboratorio NIST (Gaithersburg, MD), Titanic Museum (Pigeon Forge, TN), Pier 54/Chelsea Piers (NYC) |
| Locacoes gravadas anteriormente | 1: Museu do Titanic (Sao Paulo) — acervo de gravacoes com Andreza |
| Props-evidencia | 18+: rebites, cadeado, blueprints, Merchant Shipping Act, telegrama, manipulador Morse, sino, relogio, bloco de gelo, fotos de passageiros, lista de sobreviventes, etc. |
| Visualizacoes tecnicas (CGI) | 15: modelo 3D Titanic, Swiss Cheese, rebites microscopio, distribuicao aco/ferro, drift time-lapse, mapa Atlantico, grafismo mortalidade, crescimento navios vs regra, overlays de erro, etc. |
| Entrevistas a filmar | 5 sessoes (Foecke, Stephenson, McCarty, Butler, Lynch/Marschall) + Andreza em campo (3 locacoes) |
| Horas brutas estimadas | 22-28 horas |
| Reconstituicoes | 7 momentos (R1-R6 + grades entre decks) em 3 niveis (N1 simbolico, N2 fragmentado, N3 estilistico) |
| Arquivo submarino | Acervo Cameron (33 mergulhos) |
| Musica composta | ~2 minutos (apenas na transicao SOLAS/Eastland — esperanca breve) |
| **Novidades v2** | SOS Morse (abertura/fechamento), SEQ 03 (passageiros), SEQ 18 (NYC pier), 13 overlays de erro, locacoes Pigeon Forge e NYC |

---

## CHANGELOG v1 --> v2

| Alteracao | Descricao | Impacto |
|-----------|-----------|---------|
| SEQ 01 reescrita | Abertura com SOS em codigo Morse antes do mergulho | +1 min. Circularidade Morse inicio/fim |
| SEQ 03 nova | "As Vidas a Bordo" — historias de Astor, Guggenheim, Straus, Molly Brown, banda + Andreza em Pigeon Forge (bloco de gelo) | +6 min. Humanizacao ANTES dos erros |
| SEQ 10 expandida | Andreza em campo no Titanic Museum Pigeon Forge (corredores 3a classe) | +1 min. Locacao real enriquece |
| SEQ 18 nova | "O Pier" — Andreza no Pier 54, NYC, onde o Carpathia atracou | +4 min. Localiza a historia no espaco real |
| SEQ 19 modificada | Retorno do Morse (eco) no epilogo. Circularidade sonora completa | Neutral. Fechamento mais potente |
| Overlays de erro | 13 marcacoes visuais ao longo do doc (PROCESSO/HUMANO/SISTEMICO) | Neutral. Dispositivo recorrente que converge no climax |
| Numeracao | 17 SEQ --> 19 SEQ. Renumeracao completa | Estrutural |
| Duracao | 90 min --> 105 min | +15 min |
| "Especialista em Seguranca Moderna" | Removido como personagem separado — falas absorvidas pela Andreza | Coerencia. Andreza E a especialista |

---

*Fase 11 — Roteiro Final Consolidado v2 | @roteirista (squad doc-safety) | 2026-03-06 | FINAL DRAFT v2*
*Apresentadora: Andreza Araujo (squad andreza-araujo) | Squad Creator: @oalanicolas, @thiago-finch, @pedro-valerio*
*Consolidacao: Fases 6-10 + melhorias v2 (SOS Morse, historias de passageiros, locacoes Pigeon Forge/NYC, marcacao de erros)*

> "O Titanic nao foi destruido por um iceberg. Foi destruido por 18 anos de decisoes razoaveis. A pergunta nao e se voce esta num navio — voce esta. A pergunta e: quem esta falando, e quem esta ouvindo?"
