# Enciclopédia Cinematográfica para Nano Banana 2

> Fonte: Bíblia do Agente Cinematográfico V7, Guia Spielberg, Relatório Diretores Americanos & DPs
> Este arquivo é carregado pelo nano-banana-prompter quando precisa de referências cinematográficas profundas.

## FILOSOFIA DO AGENTE

O agente é um DIRETOR CRIATIVO — cada palavra desbloqueia um universo. O modelo de geração NÃO tem decisão. Recebe o prompt onde cada token já foi decidido com precisão técnica e artística absoluta.

### Domínios de Maestria Simultâneos
- **Diretor de Cena**: Storytelling, acting, expressões, o que aconteceu 5s antes e depois do frame
- **Diretor de Fotografia (DP)**: Iluminação motivada, IRE, false color, ratio de contraste, qualidade da luz
- **Colorista**: Método das 3 cores (McCurry), sistemas complementares, temperatura emocional, hex colors
- **Estilista/Diretor de Arte**: Tecidos, marcas, cabelos, maquiagens, looks completos
- **Arquiteto**: Todas as escolas (gótica, brutalista, art deco, bauhaus, orgânica, minimalista, etc.)
- **Enciclopédico**: Carros, natureza, história, civilizações, materiais — "o agente ESTAVA LÁ"
- **Engenheiro de Modelos**: Como NB2 lê e interpreta prompts
- **Físico Visual**: Óptica real, motion blur, grain, película, bokeh, focal length compression

## REGRAS DE OURO (Manual Oficial + Testes)

### O que FUNCIONA
1. **Linguagem natural descritiva** — frases completas, não tag soup
2. **Contexto/propósito** — "for a luxury perfume campaign" muda tudo
3. **Materialidade concreta** — "aged leather with patina", "matte finish brushed steel", "crumpled linen"
4. **Restrições negativas** — "No text, no watermarks, no digital artifacts"
5. **Edição conversacional** — se 80% está certo, refinar, NÃO re-gerar
6. **Camera gear como ÂNCORA** — "Shot on full-frame cinema camera" força film grain e óptica real
7. **Descrever EFEITO óptico** — "gentle halation, creamy bokeh, warm organic rendering" > "Cooke S4/i 50mm" sozinho
8. **Motion blur** — "Natural motion blur consistent with 1/48 shutter speed" ancora no cinema
9. **Color grading como resultado** — "Desaturated with muted warm tones pushed toward burnt umber, cool shadows in grey-blue"
10. **Iluminação como efeito** — "Warm directional light from single window, creating volumetric dust shafts"

### O que NÃO FUNCIONA
- Tag soup ("4k, realistic, masterpiece, trending on artstation") — FILLER IGNORADO
- Quality inflation ("8k, hyper-realistic, award-winning") — redundante
- Nomes de câmera/lente SOZINHOS sem efeito descrito — zero impacto
- Render engines ("Unreal Engine 5", "Cinema 4D") — puxa 3D, não cinema
- Frases de cortesia ("Please", "could you") — desperdiçam tokens
- Referências a outros modelos de AI ("Midjourney style") — confunde
- Repetição ("very very detailed extremely detailed") — redundante

### Estrutura que o modelo processa (ORDEM DE PRIORIDADE)
1. **Subject** — Quem/o que + adjetivos específicos + ação
2. **Composition** — Ângulo de câmera, enquadramento, framing
3. **Action** — O que está acontecendo no frame
4. **Location/Context** — Onde + atmosfera + propósito
5. **Style/Media** — Estética visual, referência de estilo
6. **Technical** — Lighting, câmera/lente (como EFEITO), restrições

## DIRETORES DE CINEMA — Referência de Collabs

### Escala Épica / Grandeza
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| Christopher Nolan | Escala prática IMAX. Temporal. Pretos profundos, frio dessaturado. Wide + deep focus | Escala + realismo + peso + tempo |
| Denis Villeneuve | Grandeza silenciosa. Vazio protagonista. Monocromático por cena. Simetria | Paisagem + solidão + escala filosófica |
| Ridley Scott | Épico atmosférico. Fumaça/poeira/chuva sempre. Shafts volumétricos | Épico + atmosfera + partículas |
| David Lean | Épico clássico. Paisagem como personagem | Deserto + escala + cinema clássico |
| James Cameron | Espetáculo tech. Azuis profundos. Alto contraste | Sci-fi + oceano + tecnologia |
| Zack Snyder | Slow-motion épico. Dessaturado + accent color. Composições de pintura | Ação estilizada + heroísmo |
| Francis Ford Coppola | Épico de família. Âmbar profundo. Sombras de poder | Poder + família + amber |

### Controle / Simetria / Cor
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| Wes Anderson | Simetria frontal obsessiva. Pastel coordenado. Flat lighting. Tableaux | Whimsical + colorido + controlado |
| Stanley Kubrick | Simetria perturbadora. One-point perspective. Controle obsessivo | Controle + perturbação + perfeição |
| Yorgos Lanthimos | Wide-angle distorcido. Espaços opressivos. Desconforto | Absurdo + desconforto + estranho |
| Alfonso Cuarón | Planos-sequência longos. Profundidade de campo como narrativa | Imersão + plano contínuo + realismo |
| Akira Kurosawa | Composição em camadas. Movimento dentro do frame | Samurai + épico + composição clássica |

### Escuridão / Tensão / Thriller
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| David Fincher | Precisão cirúrgica fria. Low-key. Green-grey-blue. Z-axis blocking | Thriller + controle + frieza |
| Michael Mann | Digital noturno. Luzes urbanas como personagem. Granulado digital | Noite urbana + crime + digital |
| Park Chan-wook | Violência estetizada. Verde jade, vermelho sangue. Barroco | Beleza + violência + estética asiática |
| Bong Joon-ho | Social horror. Arquitetura como classe. Transições tonal | Classe social + tensão + arquitectura |
| David Lynch | Suburbia surreal. O estranho sob o familiar | Surreal + doméstico + perturbador |
| Paul Thomas Anderson | Long takes + ensemble. Steadicam | Ensemble + época + ambição |
| Taylor Sheridan | Paisagem americana como personagem. Luz natural dura | Fronteira + crime + paisagem |

### Neon / Estilização
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| Nicolas Winding Refn | Neon + violência + silêncio. Magenta/cyan/amber | Noturno + neon + tensão estilizada |
| Wong Kar-wai | Nostalgia neon. Motion blur intencional. Step-printing | Melancolia + urbano + nostalgia colorida |
| Gaspar Noé | Neon agressivo. Câmera vertiginosa. Desconforto visual | Extremo + provocação + neon agressivo |
| Spike Lee | Cor como política. Dutch angles. Double dolly. Direto na câmera | Política + urban + confronto |

### Luz Natural / Poesia
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| Terrence Malick | Golden hour eterna. Exclusivamente natural. Wide-angle flutuante | Natureza + espiritualidade + beleza |
| Sofia Coppola | Suave, pastel, feminino. Natural difusa. Rosa/lavanda/branco | Delicadeza + feminino + melancolia |
| Chloé Zhao | Magic hour. Paisagem americana real. Pele real | Realismo + paisagem + dignidade |
| Andrei Tarkovsky | Planos longos. Água, reflexos, neblina. Tempo como matéria | Filosofia + lentidão + água + mistério |

### Excesso / Espetáculo
| Diretor | Assinatura | Gatilho |
|---------|-----------|---------|
| Baz Luhrmann | Excesso total. Spotlights/neon/glitter. Hipersaturado | Festa + excesso + glamour máximo |
| Guillermo del Toro | Fantasia gótica. Dourado + azul profundo. Criaturas orgânicas | Dark fantasy + criaturas + gothic |
| Tim Burton | Gothic whimsical. P&B + accents. Espiral, curva, assimetria | Dark whimsical + gothic + estranho |

## DIRETORES DE FOTOGRAFIA (DPs)

| DP | Assinatura | Diretores | Gatilho |
|----|-----------|-----------|---------|
| Roger Deakins | Precisão naturalista. Single source. Simplicidade impossível | Coen, Villeneuve, Mendes | Iluminação perfeita naturalista |
| Emmanuel Lubezki | Natural light. Golden hour. Long takes imersivos. Wide-angle | Malick, Cuarón, Iñárritu | Imersão + luz natural + plano longo |
| Hoyte van Hoytema | Large format IMAX. Intimidade em escala. Grain fino | Nolan, Villeneuve | Escala + intimidade |
| Bradford Young | Low-light master. Pele negra luminosa. Shadows que abraçam | DuVernay, Villeneuve | Low-light + pele negra + poesia |
| Robert Richardson | Contrastes extremos. Saturação controlada | Tarantino, Scorsese | Contraste + saturação + ousadia |
| Janusz Kamiński | Backlight + haze + overexposure. Luz etérea | Spielberg | Etéreo + drama + sentimentalismo |
| Greig Fraser | Digital-analog hybrid. Vintage lenses em digital | Villeneuve, Reeves | Digital-analog + atmospheric |
| Marcell Rév | Pro-Mist. Neon. Anamorphic vintage | Levinson (Euphoria) | Neon + juventude + difusão |
| Vittorio Storaro | Luz como escritura. Cor narrativa. Shadows expressivos | Coppola, Bertolucci | Cor narrativa + expressionismo |
| Gordon Willis | "Prince of Darkness". Underexposure. Top light. Amber | Coppola, Allen | Escuridão elegante + amber |
| Darius Khondji | Grain pesado. Escuridão úmida. Green-grey | Fincher, Jeunet | Grain + escuridão + textura |
| Robert Yeoman | Flat lighting + pastel + simetria. Clean | Wes Anderson | Simetria + pastel |
| James Laxton | Pele negra como luz. Warmth. Cor emocional | Barry Jenkins | Pele + warmth + intimidade |
| Jeff Cronenweth | Desaturação controlada. Sombras precisas. Digital pioneer | David Fincher | Frio + preciso + desconfortável |
| Robert Elswit | Escala e intimidade. Long takes fluidos | PTA | Naturalista + ambição |

## COLORISTAS DE CINEMA

| Colorista | Assinatura | Trabalhos | Gatilho |
|-----------|-----------|-----------|---------|
| Stefan Sonnenfeld | Teal & Orange definitivo. Blockbuster | Transformers, 300, Star Trek | Blockbuster + separação cromática |
| Dave Cole | HBO dark. Muted, cold, restrained | True Detective, Chernobyl | HBO + escuridão + restraint |
| Jill Bogdanowicz | Euphoria neon. Glow difuso. Pele luminosa | Euphoria, Moonlight | Neon + juventude + glow |
| Peter Doyle | Bleach bypass digital. Dessaturação épica | LOTR, Matrix | Épico + dessaturação + bleach bypass |
| Joe Walker | Naturalismo preciso. Warmth controlado | Arrival, Dune | Naturalismo + precisão |

## FOTÓGRAFOS — Referência

### Moda / Retrato
| Fotógrafo | Assinatura | Gatilho |
|-----------|-----------|---------|
| Annie Leibovitz | Retrato teatral conceitual. Chiaroscuro. Escala épica | Retrato conceitual + theatrical |
| Richard Avedon | Fundo branco. Movimento capturado. Fashion como performance | Fashion clean + movimento |
| Helmut Newton | Poder feminino. Flash direto. Geometria urbana. P&B alto contraste | Fashion + power + provocação |
| Irving Penn | Simplicidade máxima. Fundo neutro. Luz perfeita | Minimalismo + perfeição |
| Tim Walker | Fantasia tangível. Sets construídos. Props gigantescos | Fantasia + materialidade + storybook |
| Peter Lindbergh | P&B humanista. Anti-glamour. Cenários industriais | P&B + autenticidade + fashion real |
| Mario Testino | Glamour luminoso. Pele perfeita. Cores vivas | Glamour + celebração + cor viva |
| David LaChapelle | Surrealismo pop fluorescente. Neon. Zero sombra | Surreal + pop + neon extremo |

### Documentais / Artísticos
| Fotógrafo | Assinatura | Gatilho |
|-----------|-----------|---------|
| Gregory Crewdson | Suburbia surreal. Cinema congelado. Crepúsculo + tungstênio | Suburban + surreal + cinematographic |
| Steve McCurry | 3 cores. Contato visual direto. Kodachrome. Golden hour | Retrato humanista + cor vibrante |
| Sebastião Salgado | P&B monumental. Escala humana. Grain pesado | Humanismo + paisagem + P&B |
| Fan Ho | Geometria luz/sombra. Hong Kong vintage. Silhuetas | Geometria + luz/sombra + minimalismo |
| William Eggleston | Cor cotidiana monumental. Banal tornado épico. Kodachrome | Cotidiano + cor + monumentalidade |

## ARTISTAS VISUAIS / CONCEPT

| Artista | Assinatura | Gatilho |
|---------|-----------|---------|
| Alberto Mielgo | Realismo pictórico. Motion blur como arte. Saturação extrema | Artistic + painterly + motion |
| Moebius | Sci-fi orgânico. Linhas limpas. Paisagens alienígenas | Sci-fi + orgânico + alien |
| H.R. Giger | Biomecânico. Orgânico + máquina. Preto/bone | Alien + biomecânico + dark |
| Syd Mead | Futurismo industrial. Design de veículos/cidades. Chrome + neon | Futuro + design + veículos |
| Simon Stålenhag | Sci-fi suburbano. Máquinas em cotidiano. Cinza nórdico + ferrugem | Sci-fi + cotidiano + melancolia |
| Makoto Shinkai | Céus foto-realistas. Chuva como personagem. Azul + dourado | Anime + céu + nostalgia |
| Caravaggio | Chiaroscuro. Luz direcional extrema. Drama barroco | Escuridão + luz direcional + sagrado |
| Vermeer | Luz de janela. Intimidade doméstica. Azul + âmbar | Janela + intimidade + period |
| Edward Hopper | Isolamento urbano. Luz artificial. Solidão em espaços públicos | Solidão + urbano + luz artificial |

## ERAS E ESTÉTICAS

| Era | Paleta | Textura | Referências |
|-----|--------|---------|-------------|
| Renascença | Terra, ouro, azul lápis-lazúli | Óleo sobre tela, craquelure | da Vinci, Botticelli |
| Barroco | Dourado, vermelho profundo, preto | Chiaroscuro | Rembrandt, Vermeer |
| Art Deco (1920-40) | Gold, black, silver, geometric | Metal polido, marble | Gatsby, Metropolis |
| Film Noir (1940-50) | P&B alto contraste | Venetian blinds | Double Indemnity |
| Technicolor (1950-60) | Saturação teatral pura | 35mm limpo | Vertigo, Singin' in the Rain |
| New Hollywood (1960-70) | Âmbar, mostarda, olive | Grain pesado, flares | Godfather, Taxi Driver |
| Neon 80s | Pink neon, electric blue, chrome | VHS, haze, reflexos | Blade Runner, Miami Vice |
| Grunge 90s | Green doentio, beige, grey | 16mm grain, handheld | Fight Club, Trainspotting |
| Y2K (2000s) | Teal & Orange, digital clean | Transição film→digital | Matrix, Gladiator |
| Neo-Noir | Minimal + accent neon/vermelho | Digital dark | Blade Runner 2049, Drive |
| Cyberpunk | Neon pink/cyan/amber vs. preto | Grain digital, chromatic aberration | Ghost in Shell |
| Cottagecore | Green, cream, warm brown, floral | Natural, suave | Bucólico, natureza |
| Dark Academia | Brown, navy, gold, burgundy | Livro, madeira, couro | Oxford, bibliotecas |
| Afrofuturismo | Gold, purple, azul profundo | Tech + tribal + orgânico | Black Panther |
| Solarpunk | Green vivo, dourado, terracota | Orgânico + tech | Utopia ecológica |

## PALETAS POR EMOÇÃO

| Emoção | Dominante | Accent | Shadows | Referência |
|--------|-----------|--------|---------|------------|
| Terror | Preto 70% | Vermelho sangue | Azul-preto | Fincher, Aster |
| Melancolia | Grey-blue | Nenhum | Blue-grey | Villeneuve, Tarkovsky |
| Nostalgia | Âmbar | Sepia | Brown warm | Coppola, 70s |
| Euforia | Neon multi | Todos | Preto profundo | Refn, Euphoria |
| Poder | Gold | Vermelho escuro | Preto | Godfather |
| Inocência | Pastel soft | Rosa | Lavanda | Coppola, Anderson |
| Violência | Vermelho | Preto | Deep teal | Park, Tarantino |
| Sagrado | Gold | Azul | Preto rico | Caravaggio, Baroque |
| Celebração | Multi saturado | Gold | Warm | Luhrmann |
| Solidão | Desaturado | Accent mínimo | Neutro frio | Hopper, WKW |

## MARCAS E MODA

| Marca | Paleta | Styling | Mood |
|-------|--------|---------|------|
| Gucci (Michele) | Red, green, gold, floral | Maximalismo eclético | Opulência vintage |
| Prada | Neutros + 1 accent neon | Minimal + twist intelectual | Cerebral |
| Chanel | Black, white, gold, tweed | Clássico atemporal | Elegância |
| Balenciaga | Black, oversized | Futurista industrial | Provocação |
| Louis Vuitton | Monogram brown, warm | Heritage + contemporâneo | Herança |
| Versace | Gold, baroque, saturado | Bold, sexy, ornamental | Excesso confiante |
| Dior | Soft pink, grey, silver | Haute couture, floral | Feminino poderoso |
| Hermès | Orange, leather brown, cream | Artesanal luxury | Artesanato premium |
| Saint Laurent | Black, gold, sequins | Rock'n'roll luxury | Rebellious glamour |
| Bottega Veneta | Green, leather tan, subtle | Quiet luxury, woven | Understatement |
| Rick Owens | Black, grey, drape | Apocalyptic luxury | Dystopian elegance |

## SISTEMA AUTÔNOMO DE COLLABS (7 Dimensões)

O agente analisa o input em 7 dimensões e cruza automaticamente:

| Dimensão | Espectro (low → high) | Exemplo |
|----------|----------------------|---------|
| Escala | Íntima → Monumental | Coppola → Nolan |
| Luz | Natural → Estilizada | Malick → Refn |
| Cor | Restrita → Saturada | Fincher → Luhrmann |
| Emoção | Tensão → Beleza | Fincher → Malick |
| Realismo | Real → Fantasia | McQueen → del Toro |
| Movimento | Estático → Ação | Kubrick → Scott |
| Era | Histórico → Futuro | Lean → Cameron |

### Collabs Validadas
| Fórmula | Resultado | Para qual cena |
|---------|----------|----------------|
| Nolan + McCurry | Escala IMAX + 3 cores + dignidade | Retrato épico em paisagem |
| Refn + Wong Kar-wai | Neon + melancolia + solidão | Personagem solo à noite |
| Villeneuve + Malick | Grandeza + luz natural filosófica | Paisagem vasta + contemplação |
| Anderson + LaChapelle | Simetria pastel + surreal pop | Whimsical surreal controlado |
| Fincher + HBO (Dave Cole) | Precisão + crueza | Thriller doméstico |
| Scott + McCurry | Atmosfera épica + humanismo | Guerra/conflito com dignidade |
| Jenkins + Bradford Young | Intimidade + pele luminosa | Retrato íntimo pele negra |
| Kubrick + Tarkovsky | Simetria + contemplação | Sci-fi filosófico |
| del Toro + Gothic | Opulência + criaturas | Dark fantasy interior |
| Mann + Refn | Digital noturno + neon | Crime noturno estilizado |

### Regras de Collab
1. Máximo 2-3 referências por cena (mais dilui identidade)
2. Cruzar dimensões COMPLEMENTARES, não redundantes
3. Referência IMPLÍCITA no prompt > explícita (descrever EFEITO, não nomear diretor)
4. A collab serve a cena — se nenhuma se encaixa, construir do zero
5. "Visual lineage: X meets Y" como tag semântica

## SPIELBERG — Técnicas Específicas

### Lentes
- **21mm (Super 35)** — "a visão de mundo de Spielberg". Distorção perspectiva, profundidade aumentada, proximidade dramática
- Abertura típica: **T5.6 - T8** (deep focus, sweet spot óptico)
- Panavision Anamorphic, Cooke S4, Zeiss Standard Speeds, PVintage

### Técnicas de Composição
- **Deep Space Composition**: Ação em múltiplos planos de profundidade simultâneos
- **Over-the-Shoulder Dramático**: Wide lens para dominância visual
- **Frame Within Frame**: Janelas, portas, espelhos como enquadramento
- **Spielberg Face**: Close-up de reação emocional ANTES de revelar o espetáculo
- **Reflexos**: Personagem e objeto de atenção no mesmo frame

### Movimentos de Câmera
- **Spielberg Push In**: Track-in gradual durante momento emocional (21mm, focus pull)
- **Sideways Tracking**: Objetos entre câmera e sujeito = textura + profundidade
- **Long Takes**: "In-frame editing" via movimento de câmera e blocking
- **Multidirecional**: Lateral + crane + pan + tilt combinados

### Kamiński (DP) Style
- **Backlight como segundo key light** + haze/smoke
- **Key light focado** no personagem (sujeito = parte mais brilhante do frame)
- **Haze** para shafts de luz visíveis, bloom, profundidade 3D
- **Overexposure controlada** em janelas/vents (luz branca neutra)
- **Diffusion filters + CTO/CTS gels**

## PRINCÍPIOS INVIOLÁVEIS

1. O agente decide 100%, o modelo executa 100%
2. Cada palavra desbloqueia um universo criativo. Zero filler
3. Cruza antes de criar. Referências antes da escrita
4. Imperfeição É precisão. Poros, vincos, sujeira, pátina
5. Paleta serve história. Cor é narrativa, nunca decorativa
6. Motion blur = vida. Sempre em ação
7. O vazio é composição. Espaço negativo é deliberado
8. Captação pelo lado da sombra. Sombra conta mais que luz
9. O agente estava lá. Precisão enciclopédica absoluta
10. Descrever EFEITO visual > nomear equipamento
