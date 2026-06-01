# Carousel Generator

## Purpose
Generate branded Instagram/YouTube carousel slides from a YouTube video URL. One command, full carousel output as PNGs ready to post.

## When to Use
When the user asks to create a carousel, generate carousel slides, or says `/carousel`. Also when a workflow requires turning a video into carousel posts.

## How It Works

### Step 1: Extract Video Data

Run the youtube_extract tool on the provided URL:

```bash
python tools/youtube_extract.py "<URL>" --lang fr,en --max-comments 20
```

The JSON output lands in `tmp/youtube/`. Read it to get the transcript, title, description, and metadata.

If an extraction already exists for this video ID (check `tmp/youtube/`), ask the user whether to reuse it or re-extract.

### Step 2: Source Images

Avant de generer le contenu, preparer les images pour le carousel.

**A) Images de l'utilisateur (prioritaire)**

Demander : "Tu as des photos a integrer ? (portrait, produit, setup) Sinon je cherche des images stock."

Si oui : l'utilisateur donne des URLs ou des chemins locaux. Les stocker dans `tmp/carousel/{video-slug}/images/`.

**B) Images stock (Unsplash — fallback automatique)**

Si l'utilisateur n'a pas de photos, chercher 3-5 images pertinentes sur Unsplash :

```bash
python tools/fetch_stock_images.py --query "{keywords}" --count 5 --out tmp/carousel/{video-slug}/images/
```

Si le tool `fetch_stock_images.py` n'existe pas encore, utiliser l'API Unsplash directement :
- Endpoint : `https://api.unsplash.com/search/photos?query={keywords}&orientation=portrait&per_page=5`
- Header : `Authorization: Client-ID {UNSPLASH_ACCESS_KEY}` (depuis `.env`)
- Utiliser les URLs `raw` avec parametres `&w=1080&q=80` pour la bonne resolution

**Regles images :**
- Maximum 2-3 slides avec images sur un carousel de 7
- Privilegier les images avec de l'espace "vide" pour poser du texte (photo-overlay)
- Pas d'images generiques type "personne devant un laptop" — chercher des images avec du caractere
- Resolution minimum 1080px de large

### Step 3: Generate Carousel Content

> **LECTURE OBLIGATOIRE — ne pas sauter.**
> Avant de générer le moindre contenu, lire ces deux fichiers en entier via l'outil Read :
> 1. `content-guide.md` — règles éditoriales, writing rules, séquence de slides, self-critique checklist
> 2. `content-eval-checklist.md` — 10 critères binaires, passes d'amélioration (Voice DNA, Open loops, Anti-guru, Intent check)
>
> Générer du contenu sans avoir lu ces deux fichiers est une erreur de process. Aucune exception.

Read the full transcript + metadata. Then generate structured content for 7 slides following the rules in `content-guide.md`.

**Slide sequence (par defaut) :**

| # | Type | Theme | Purpose |
|---|------|-------|---------|
| 1 | Hero | light OU photo-overlay | Hook — bold statement from the video's core thesis |
| 2 | Problem | dark | Pain point the video addresses |
| 3 | Solution | gradient | The answer/method — with optional quote box |
| 4 | Features | light | 3-4 key takeaways with emoji icons |
| 5 | Details | dark OU photo-overlay | Supporting evidence or deeper points |
| 6 | Steps | light | 3 actionable steps |
| 7 | CTA | gradient | Drive to video — no swipe arrow, progress 100% |

**Variantes disponibles** (voir `templates.md` pour le HTML) :
- **Stat** — chiffre geant + contexte. Remplace features ou details.
- **Citation** — quote plein ecran. Remplace solution ou details.
- **Split haut/bas** — photo en haut, texte en bas. Remplace n'importe quelle slide sauf CTA.
- **Photo circulaire** — portrait + texte. Bon pour CTA ou "qui suis-je".

**Rythme visuel** : varier les types. Pas 7 slides texte-only identiques. Si des images sont disponibles, les placer sur la slide hero (1) et une slide milieu (4 ou 5). Alterner slides denses et slides aerees.

Adapt the sequence if the video content doesn't fit all 7 types (see content-guide.md for rules). Minimum 5 slides.

Save the content as JSON to `tmp/carousel/{video-slug}/content.json`:

```json
{
  "video_id": "abc123",
  "video_title": "Original title",
  "video_url": "https://youtube.com/watch?v=abc123",
  "total_slides": 7,
  "slides": [
    {
      "index": 1,
      "type": "hero",
      "variant": "photo-overlay",
      "theme": "photo-overlay",
      "image_url": "https://images.unsplash.com/photo-xxx?w=1080&q=80",
      "tag": "CREATION DE CONTENU",
      "heading": "ARRETE DE CHERCHER QUOI POSTER",
      "body": "Ton contenu est deja dans tes videos. Il suffit de l'extraire."
    }
  ]
}
```

### Step 4: Self-Critique

Appliquer les deux checklists sur le contenu généré (les fichiers ont été lus en Step 3) :

**A) `content-eval-checklist.md`** — 10 critères binaires. Seuil 8/10. Critères 1, 5 et 8 non-négociables. Puis appliquer les 4 passes : Voice DNA, Open loops, Anti-guru, Intent check.

**B) Self-critique de `content-guide.md`** — 9 points :
1. Robot test — une slide sonne-t-elle comme écrite par une IA ?
2. Word count — un heading dépasse 8 mots ?
3. Line count — une slide dépasse 7 lignes ?
4. Generic test — une slide pourrait s'appliquer à n'importe quelle vidéo ?
5. Read aloud — chaque heading sonne naturel à voix haute ?
6. Scroll stop — la slide 1 arrêterait-elle un scroll ?
7. Value test — chaque slide apprend-elle quelque chose ?
8. Rhythm test — deux slides consécutives ont le même layout/densité ?
9. Squint test — la hiérarchie de chaque slide est-elle claire en plissant les yeux ?

Réécrire tout ce qui échoue. Cette étape est non-négociable.

### Step 5: Generate HTML Slides

For each slide, build a self-contained HTML file using the templates in `templates.md` (same directory as this file).

**Key rules:**
- Each HTML file is a complete document at 1080x1350px
- Include the Google Fonts @import in every file
- Include the progress bar on every slide (fill = slideIndex / (totalSlides - 1) * 100%)
- Include the swipe arrow on every slide EXCEPT the last
- Alternate themes: light -> dark -> gradient -> light -> dark -> light -> gradient

**Qualité visuelle — principes frontend-design appliqués aux slides statiques**

Le plugin `frontend-design` définit le standard de qualité à atteindre. Pour les slides (HTML statique rendu en PNG, sans JS ni animations), appliquer ces principes :

- **Typographie** : La hiérarchie doit être immédiatement lisible. Contraste fort entre le heading (Oswald, 52-72px, 700) et le body (Poppins, 26px, 400). Le tag (22px, 600, uppercase, letter-spacing 4px) doit agir comme un signal visuel discret avant le heading. Ne jamais mettre deux éléments de poids identique côte à côte — l'œil doit savoir où aller en moins d'une seconde.

- **Hiérarchie visuelle** : Chaque slide a UN centre de gravité (le heading ou le big-number). Tout le reste est subordonné. Un body trop long compète avec le heading — le couper ou le reformuler. Jamais plus de 3 niveaux visuels par slide (tag → heading → body).

- **Espacement et respiration** : Le slide doit respirer. Si le contenu occupe plus de 70% de la hauteur, le reformuler pour le réduire — une slide dense sans espace vide paraît chargée sur mobile. L'espace vide EST du design, pas un oubli. Utiliser les valeurs de spacing définies dans `templates.md` (base 4pt), jamais de valeurs arbitraires.

- **Rapport dominant/accent** : La couleur brand teal (`#6BA8A0`) doit apparaître sur max 2-3 éléments par slide (tag, accent-line, step-num, progress-fill). Saturer une slide en teal dilue l'impact. Sur les slides dark, le blanc est la couleur dominante — le teal est l'accent.

- **Cohérence du pairing typographique** : Oswald pour les headings (condensé, impact, autorité) + Poppins pour le body (lisibilité, modernité). Ce pairing est fixé par le branding Hostopia. Ne jamais substituer d'autres fonts sans instruction explicite.

Avant de générer chaque slide, valider mentalement : *"Est-ce qu'on sait exactement où regarder en premier ? Le slide respire-t-il ?"* Si non, retravailler le layout ou le contenu avant de produire le HTML.

Save HTML files to `tmp/carousel/{video-slug}/slide-1.html` through `slide-N.html`.

### Step 6: Render PNGs

Run the HCTI rendering tool:

```bash
python tools/render_hcti.py tmp/carousel/{video-slug}/
```

This sends each HTML file to the HCTI API and downloads the resulting PNGs to the same directory.

### Step 7: Present Results

Show the user the rendered PNG files by reading them. Ask if adjustments are needed.

If the user wants changes:
- Regenerate only the affected slide(s) — don't rebuild everything
- Re-run `render_hcti.py` on just the modified HTML file(s):
  ```bash
  python tools/render_hcti.py tmp/carousel/{video-slug}/slide-3.html
  ```
- Après chaque re-rendu, relancer immédiatement l'export (Step 8) pour que le Desktop reste à jour.

### Step 8: Export JPEG — OBLIGATOIRE, AUTOMATIQUE

**Cette étape s'exécute systématiquement** après Step 6, et après chaque re-rendu en Step 7. Ne pas demander confirmation à l'utilisateur.

```bash
bash export_carousels.sh
```

Ce script (à la racine du projet) convertit tous les PNG en JPEG et les copie dans `~/Desktop/Hostopia/carousels/` avec la nomenclature `carousel{N}-slide{M}.jpg`.

Si le script n'existe pas à la racine du projet, signaler l'erreur à l'utilisateur.

## Output

```
tmp/carousel/{video-slug}/
  images/               # Images sources (stock ou perso)
  content.json          # Structured content for all slides
  slide-1.html          # HTML source (for debugging/iteration)
  slide-1.png           # Final PNG — 1080x1350px, ready to post
  slide-2.html
  slide-2.png
  ...
```

## Configuration

### Required in `.env`
```
HCTI_USER_ID=<from htmlcsstoimage.com/dashboard>
HCTI_API_KEY=<from htmlcsstoimage.com/dashboard>
GOOGLE_YOUTUBE_KEY=<for youtube_extract.py comments>
UNSPLASH_ACCESS_KEY=<from unsplash.com/developers — gratuit>
```

### Brand

Tout le branding est dans la section "Branding — MODIFIER ICI" de `templates.md`.
L'utilisateur change ses couleurs, fonts, nom et photo de profil a un seul endroit.
Si PROFILE_PHOTO est fourni (URL), le slide affiche la photo en rond. Sinon, affiche l'initiale du PROFILE_NAME dans un cercle colore.

## Règles de production — Non-négociables

Ces trois règles s'appliquent à chaque génération, sans exception.

### 1. Logos transparents uniquement

Toujours utiliser `assets/logo-light.png` (slides `.light`) et `assets/logo-dark.png` (slides `.dark`, `.gradient`, `.photo-overlay`).
Ces fichiers sont des PNG à fond 100% transparent.
Ne jamais utiliser un logo avec fond blanc opaque (CYAN 5.png, BLANC 1.png, NOIR 2.png, etc.) — le carré blanc est visible sur les fonds sombres et les photos.

### 2. Pas de référence à la source vidéo

Le carousel doit toujours sembler être du contenu original de la marque, pas une adaptation de vidéo YouTube.
Interdit dans les slides : "Extrait de la vidéo", "Citation YouTube", "D'après la vidéo", "Source :", toute mention d'un créateur externe.
Pour les quote box, utiliser des labels neutres : "Le constat", "En pratique", "Retour terrain", "Ce que ça change", "À retenir".

### 3. Couleur orange en accent secondaire

Le teal `#6BA8A0` est l'accent principal. L'orange `#E8845A` est disponible en accent secondaire ponctuel.
Classes disponibles dans `templates.md` : `.tag.orange`, `.accent-line.orange`, `.cta-button.orange`, `.highlight-orange`.
Règle d'usage : max 1-2 éléments orange par carousel. Ne pas mélanger teal et orange sur la même slide.

## Limitations
- HCTI: 1000 images/month (paid plan), 50/month (free). 7 slides = 1 carousel.
- Auto-generated YouTube transcripts have no punctuation — treat as raw speech and restructure.
- Langue du contenu = langue du projet (francais par defaut), meme si la source est en anglais.
- Images stock : necessite une cle Unsplash (gratuite). Si pas de cle, le skill fonctionne en mode texte-only.

## Dependencies
- `tools/youtube_extract.py` — upstream extraction (must exist)
- `tools/render_hcti.py` — HCTI rendering (created with this skill)
- Python `requests` package
