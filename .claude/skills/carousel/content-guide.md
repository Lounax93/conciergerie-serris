# Carousel Content Guide

Rules for extracting carousel content from a YouTube video transcript.

## Extraction Strategy

1. Read the full transcript + video title + description
2. Identify the **single core thesis** (one sentence max)
3. Identify the **main pain point** the video addresses
4. Extract **3-5 key actionable takeaways**
5. Identify any frameworks, steps, or methods presented
6. Note memorable phrases or analogies from the speaker

## Content Mapping to Slides

| Slide | Type | Theme | What to write |
|-------|------|-------|---------------|
| 1 | Hero | light OU photo-overlay | Core thesis rewritten as a bold declaration. Not a question. Stop-the-scroll energy. |
| 2 | Problem | dark | The pain point in "tu" language. Make it visceral. What happens if they don't act. |
| 3 | Solution | gradient | The answer/method. One clear sentence. Optional quote or stat from the video. |
| 4 | Features | light | 3-4 key benefits or components. Each = emoji + label + one-line description. |
| 5 | Details | dark OU photo-overlay | Supporting evidence, stats, or deeper points from the video. |
| 6 | Steps | light | 3 actionable steps the viewer can take today. Numbered. |
| 7 | CTA | gradient | Drive to the video. "Regarde la video complete" + Libreneur branding. |

## Variantes de slides

En plus des types standard, utiliser ces variantes pour creer du rythme visuel :

- **Stat** — Un chiffre geant + contexte ("73%", "2M+", "10x"). Remplace features ou details quand le video contient une stat marquante.
- **Citation** — Quote plein ecran. Quand le speaker a une phrase qui claque. Remplace solution ou details.
- **Split haut/bas** — Photo en haut, texte en bas. Quand une image illustre bien le propos. Pas pour la CTA.
- **Photo circulaire** — Portrait + texte. Pour la CTA "qui suis-je" ou temoignage.

**Regle de rythme** : ne pas faire 7 slides du meme type. Alterner :
- Slides denses (features, steps) et slides aerees (stat, citation, photo)
- Slides avec images (max 2-3) et slides texte-only
- Themes differents (light, dark, gradient, photo-overlay)

## Adapting the Sequence

Not every video supports all 7 slides. Adapt:

- **No clear steps in the video?** Drop slide 6, merge key points into slide 5.
- **Video is a how-to?** Expand steps across slides 4-6.
- **Video is opinion/reflection?** Replace Features with key arguments, replace Steps with "what to do about it".
- **Video has a killer stat?** Use the Stat variant for slide 4 or 5.
- **Video has a memorable quote?** Use the Citation variant for slide 3 or 5.
- **Minimum 5 slides, maximum 10.** Default is 7.

## Writing Rules

### Voice
- Write like you're texting a smart friend
- Conversational, direct, no jargon
- Tutoiement ("tu", "ton", "tes")
- French by default (langue du projet, meme si la source est en anglais)

### Constraints
- **6th grade reading level** — if a 12-year-old can't understand it, simplify
- **1 idea per slide** — no exceptions
- **Maximum white space** — let the text breathe
- **Heading: 3-8 words** — shorter is better
- **Body: 5-7 lines max** per slide
- **Short sentences** — cut every sentence that could be two
- **No em dashes, no semicolons** — periods and line breaks only

### Banned patterns
- "Dans cet article/cette video..." (meta-references)
- "Il est important de..." (empty filler)
- "N'hesitez pas a..." (weak CTA)
- "En effet" / "Par consequent" / "Neanmoins" (academic connectors)
- Any sentence over 20 words
- Passive voice
- Lists of more than 4 items on one slide

### Hook (Slide 1) Formula

Use one of these patterns:
- **Bold claim**: "ARRÊTE DE [action courante]" / "[Nombre] [personnes] FONT CETTE ERREUR"
- **Contrarian**: The opposite of common advice in the niche
- **Result**: "J'AI [resultat] EN [temps/methode]"
- **Question flip**: State the answer, not the question

The hook must make someone think: "Si je lis pas ca, je vais rater quelque chose."

### CTA (Last Slide)

Always:
- Logo lockup (Libreneur)
- "REGARDE LA VIDEO COMPLETE" or similar
- CTA button: "Voir sur YouTube" / "Lien en description"
- No swipe arrow (signals end of carousel)
- Progress bar at 100%

## Self-Critique Checklist

After generating all slide content, run this check internally:

1. **Robot test**: Does any slide sound like AI wrote it? Rewrite it.
2. **Word count**: Does any heading exceed 8 words? Shorten.
3. **Line count**: Does any slide have more than 7 lines? Cut.
4. **Generic test**: Could this slide apply to ANY video? Make it specific.
5. **Read aloud**: Does each heading sound like something a person would say?
6. **Scroll stop**: Would slide 1 make you stop scrolling? If not, rewrite the hook.
7. **Value test**: Does someone learn something from each slide, or is it just filler?
8. **Rhythm test**: Est-ce que deux slides consecutives ont le meme layout/densite? Varier.
9. **Squint test**: En plissant les yeux, est-ce que la hierarchie de chaque slide est claire ? (titre > body > details)

If a slide fails any check, rewrite it before proceeding to HTML generation.

### Improvement Passes

After the checklist above, apply the passes from `content-eval-checklist.md` (same directory):
1. **Anti-guru filter** — find every sentence that sounds like a marketing guru wrote it. Replace with what a best friend would say over coffee.
2. **Open loops** — the hero slide must NOT answer its own question. Leave curiosity unresolved to drive swiping.
3. **Intent check** — for the carousel as a whole: what's the goal, what should it make people feel, what should they notice first, what shouldn't be there.
