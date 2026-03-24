# Midjourney Knowledge Base — V7/V6.1

> Referência técnica completa para geração de prompts Midjourney.
> Carregado pelo image-master quando `*mj-params` ou prompts Midjourney são solicitados.

## MODELO ATUAL

- **V7** é o modelo padrão desde 17 Jun 2025
- V6.1 requer `--v 6.1` explícito
- V7 é o melhor para fotorealismo nativo

## ESTRUTURA DE PROMPT MIDJOURNEY

```
[Descrição da cena em linguagem natural] --parâmetros
```

**Ordem importa:** O início do prompt tem MAIS peso que o final.

**Regras:**
- Frases descritivas > listas de tags (mesmo no MJ)
- Vírgulas separam conceitos, NÃO são tags
- Sem aspas no prompt (exceto para texto literal com `--no`)
- Parâmetros SEMPRE no final, após a descrição

## PARÂMETROS COMPLETOS

### Essenciais
| Parâmetro | Valores | Descrição |
|-----------|---------|-----------|
| `--ar` | N:N (ex: 16:9) | Aspect ratio |
| `--v` | 6.1, 7 | Versão do modelo (7 = default) |
| `--style raw` | — | Remove embelezamento, mais literal/realista |
| `--s` / `--stylize` | 0-1000 (default 100) | Quanto o MJ "embeleza". 0=literal, 1000=artístico |
| `--c` / `--chaos` | 0-100 (default 0) | Diversidade entre as 4 variações |
| `--q` | 0.25, 0.5, 1, 2 | Qualidade/tempo de renderização |

### Referências
| Parâmetro | Descrição |
|-----------|-----------|
| `--sref [URL ou código]` | Style Reference — mantém estilo visual consistente |
| `--sw` | Style Weight (0-1000, default 100) — peso da referência de estilo |
| `--cref [URL]` | Character Reference — mantém personagem consistente |
| `--cw` | Character Weight (0-100, default 100) — 0=apenas rosto |
| `--p` | Personalization — aplica seu estilo pessoal treinado |

### Controle
| Parâmetro | Descrição |
|-----------|-----------|
| `--no [item]` | Negative prompt — excluir elementos |
| `--seed [número]` | Seed para reprodutibilidade |
| `--repeat` / `--r` | Repetir prompt N vezes |
| `--tile` | Gera padrão tileable/seamless |
| `--iw` | Image Weight (0-3) — peso da imagem de referência |
| `--w` / `--weird` | 0-3000 — resultados mais experimentais |

### Velocidade
| Parâmetro | Descrição |
|-----------|-----------|
| `--fast` | Modo padrão |
| `--turbo` | 2x mais rápido, 2x custo |
| `--relax` | Gratuito mas em fila (planos Standard+) |
| `--draft` | Rápido, menor qualidade |

## COMBOS PARA FOTOREALISMO/CINEMA

### Combo Cinematográfico
```
[cena] --ar 16:9 --style raw --s 50 --v 7
```

### Combo Ultra-Real
```
[cena], shot on [câmera], [lente], [iluminação], [film stock] --ar 16:9 --style raw --s 0 --v 7
```

### Combo Artístico Controlado
```
[cena], [referência artística] --ar 16:9 --s 500 --v 7
```

### Combo Consistência de Personagem
```
[cena com personagem] --cref [URL] --cw 100 --sref [URL] --sw 80 --ar 16:9 --v 7
```

## ASPECT RATIOS CINEMA

| Ratio | Uso |
|-------|-----|
| `--ar 16:9` | Widescreen padrão, YouTube, apresentações |
| `--ar 2.39:1` | Cinemascope, filmes épicos |
| `--ar 2.76:1` | Ultra Panavision 70 (épico clássico) |
| `--ar 1.85:1` | Flat widescreen (drama, comédia) |
| `--ar 1:1` | Instagram, social media |
| `--ar 9:16` | Stories, Reels, TikTok |
| `--ar 4:5` | Instagram portrait |
| `--ar 3:2` | Fotografia clássica |
| `--ar 4:3` | Apresentações, digital art |

## DIFERENÇAS MJ vs NANO BANANA 2

| Aspecto | Midjourney V7 | Nano Banana 2 |
|---------|---------------|---------------|
| Motor | Proprietário MJ | Gemini 3.1 Flash |
| Prompt style | Descritivo + parâmetros no final | Conversacional, frases completas |
| Parâmetros | Via `--flags` | Inline na descrição |
| Texto em imagem | Limitado, melhorando | Excelente (renderiza com precisão) |
| Search Grounding | Não | Sim (busca Google ao vivo) |
| Thinking Mode | Não | Sim (planeja antes de renderizar) |
| Edição de foto | Limitado (vary region) | Completo (upload + instrução natural) |
| Consistência | Via `--cref`/`--sref` | Via upload de referências (até 14) |
| Custo | Assinatura $10-60/mês | ~$0.067/imagem ou gratuito |
| Melhor em | Estética artística, composição, "look MJ" | Fotorealismo, texto, dados ao vivo, edição |
| Negatives | `--no [item]` | Inline: "No text, no watermarks" |
| Aspect ratio | `--ar 16:9` | Inline: "16:9 aspect ratio" |
| Resolução | Fixa (upscale depois) | 512px a 4K nativo |

## KEYWORDS DE ESTILO (TESTADOS EM V7)

### Fotografia
- `photorealistic`, `documentary photography`, `editorial photography`
- `shot on [câmera]`, `[lente] at f/[número]`
- `film grain`, `35mm film`, `medium format`

### Cinema
- `cinematic`, `anamorphic`, `letterboxed`, `film still`
- `Roger Deakins lighting`, `Vilmos Zsigmond atmosphere`
- Film stocks: `Kodak Vision3 500T`, `Fuji Eterna`

### Iluminação
- `volumetric lighting`, `god rays`, `rim light`, `practical lighting`
- `golden hour`, `blue hour`, `overcast diffused light`
- `chiaroscuro`, `Rembrandt lighting`, `butterfly lighting`

### Texturas & Materiais
- `wet asphalt reflections`, `condensation on glass`
- `aged leather`, `brushed steel`, `raw concrete`
- `atmospheric haze`, `dust particles`, `rain streaks`

### Cor/Grade
- `teal and orange color grade`, `desaturated muted tones`
- `cross-processed`, `bleach bypass`, `push processing`
- `warm amber highlights, cool blue shadows`

## DICAS AVANÇADAS

1. **Multi-prompt** com `::` — separa conceitos com pesos: `hot dog:: food --ar 16:9` vs `hot:: dog --ar 16:9`
2. **Pesos negativos** — `trees::2 flowers::-1` (mais árvores, menos flores)
3. **Vary Region** — selecione área da imagem para regenerar parcialmente
4. **Pan** — expanda a imagem em qualquer direção
5. **Zoom Out** — amplie o enquadramento mantendo o centro
6. **Blend** — misture 2-5 imagens: `/blend [img1] [img2]`
7. **Describe** — MJ analisa imagem e sugere prompts: `/describe [img]`
8. **Style raw + baixo stylize** — combo para máximo controle e realismo
9. **Seed para iteração** — use `--seed` para manter composição enquanto ajusta detalhes
10. **sref + cref juntos** — `--cref` mantém o "ator", `--sref` mantém a "direção de arte"
