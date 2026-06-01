# Carousel Slide Templates

These are the HTML/CSS templates for generating carousel slides. Each slide is a self-contained HTML document rendered at **1080x1350px** (4:5 Instagram standard) via the HCTI API.

---

## Branding — MODIFIER ICI

Tout le branding est concentre ici. L'utilisateur change ces valeurs une seule fois pour adapter le carousel a sa marque.

```
/* === COULEURS === */
BRAND_PRIMARY    = #6BA8A0     /* Teal — accent principal : progress bar, tags, step-num, accent-line */
BRAND_DARK       = #000000     /* Noir — fond sombre, headings sur fond clair */
BRAND_ACCENT     = #E8845A     /* Orange/Saumon — accent secondaire : CTA bouton, tag ponctuel, highlight */

/* === NEUTRALS === */
WARM_WHITE       = #FFFFFF     /* Fond clair — blanc pur */
WARM_LIGHT       = #F5F5F5     /* Fond clair alternatif — gris tres clair */
WARM_BORDER      = #E5E5E5     /* Bordures, separateurs */
WARM_TEXT_SOFT    = #888888     /* Texte secondaire sur fond clair */
WARM_TEXT         = #111111     /* Texte principal sur fond clair */
DARK_BG          = #000000     /* Fond sombre — noir pur */
DARK_SURFACE     = #1A1A1A     /* Surface sur fond sombre (quote box, cards) */
DARK_TEXT_SOFT    = rgba(255,255,255,0.6)  /* Texte secondaire sur fond sombre */
DARK_TEXT         = #FFFFFF     /* Texte principal sur fond sombre */

/* === GRADIENT === */
GRADIENT_BG      = linear-gradient(165deg, #000000 0%, #6BA8A0 100%)

/* === FONTS (Google Fonts) === */
FONT_HEADING     = 'Oswald'     /* Titres — condensed, impact */
FONT_BODY        = 'Poppins'    /* Corps — lisible, moderne */
FONT_IMPORT      = https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Poppins:wght@300;400;600&display=swap

/* === PROFIL === */
PROFILE_NAME     = HOSTOPIA                /* Nom affiche a cote du logo */
PROFILE_PHOTO    =                         /* URL photo de profil. Si vide, affiche le logo */
PROFILE_BG       = #6BA8A0                /* Couleur du cercle si pas de photo */

/* === LOGOS (fonds transparents — OBLIGATOIRE) === */
LOGO_LIGHT       = assets/logo-light.png  /* Wordmark "hostopia" teal, fond 100% transparent — slides claires (light) */
LOGO_DARK        = assets/logo-dark.png   /* Wordmark "hostopia" blanc, fond 100% transparent — slides sombres, gradient, photo-overlay */
/* Source originale : ~/Desktop/Hostopia/logo/CYAN 1sansfond.png et BLANC 1sansfond.png */
/* Ne JAMAIS utiliser des logos avec fond blanc opaque (CYAN 5.png, BLANC 1.png, NOIR 2.png, etc.) */

/* === IMAGES PAR DEFAUT === */
/* Si l'utilisateur ne fournit pas ses propres photos,
   le skill cherche des images stock (Unsplash).
   L'utilisateur peut remplacer n'importe quelle image apres generation. */
```

### Changer de fonts

Pour utiliser d'autres Google Fonts, modifier `FONT_HEADING`, `FONT_BODY` et `FONT_IMPORT`. Exemples de pairings qui fonctionnent bien :

| Style | Heading | Body | Import |
|-------|---------|------|--------|
| **Bold & clean** (defaut) | Oswald | Poppins | `Oswald:wght@400;600;700&family=Poppins:wght@300;400;600` |
| **Tech startup** | Space Grotesk | DM Sans | `Space+Grotesk:wght@400;600;700&family=DM+Sans:wght@300;400;600` |
| **Editorial** | Playfair Display | Source Sans 3 | `Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;600` |
| **Friendly SaaS** | Plus Jakarta Sans | Plus Jakarta Sans | `Plus+Jakarta+Sans:wght@400;600;700` |
| **Minimal** | Outfit | Work Sans | `Outfit:wght@400;600;700&family=Work+Sans:wght@300;400;600` |

---

## Echelle de spacing

Base 4pt. Utiliser uniquement ces valeurs pour tout espacement.

```
XS   =  4px    /* Micro — entre elements inline */
SM   =  8px    /* Petit gap */
MD   = 12px    /* Petit padding */
BASE = 16px    /* Padding de base */
LG   = 24px    /* Entre sections proches */
XL   = 32px    /* Entre sections */
2XL  = 48px    /* Separation majeure */
3XL  = 64px    /* Top padding slide */
4XL  = 80px    /* Padding lateral slide */
```

---

## Base HTML Structure

Chaque slide utilise cette structure. Remplacer `{SLIDE_CONTENT}`, `{THEME_CLASS}`, `{PROGRESS_BAR}`, et `{SWIPE_ARROW}`.

```html
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Poppins:wght@300;400;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  width: 1080px;
  height: 1350px;
  overflow: hidden;
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
}

.slide {
  width: 1080px;
  height: 1350px;
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 64px 72px 100px;
}

/* ==========================================
   THEMES
   ========================================== */

/* --- Light --- */
.light {
  background-color: #FFFFFF;
  background-image: radial-gradient(ellipse at 8% 88%, rgba(107,168,160,0.05) 0%, transparent 52%);
  color: #111111;
}
.light .tag { color: #6BA8A0; }
.light h1, .light h2 { color: #000000; }
.light p { color: #111111; }
.light .text-soft { color: #888888; }
.light .divider { border-color: #E5E5E5; }
.light .surface { background: #F5F5F5; }

/* --- Dark --- */
.dark {
  background-color: #000000;
  background-image: radial-gradient(ellipse at 92% 8%, rgba(107,168,160,0.10) 0%, transparent 48%);
  color: #FFFFFF;
}
.dark .tag { color: #6BA8A0; }
.dark h1, .dark h2 { color: #FFFFFF; }
.dark p { color: rgba(255,255,255,0.75); }
.dark .text-soft { color: rgba(255,255,255,0.5); }
.dark .divider { border-color: rgba(255,255,255,0.1); }
.dark .surface { background: #1A1A1A; }

/* --- Gradient --- */
.gradient {
  background:
    radial-gradient(ellipse at 80% 15%, rgba(138,197,190,0.45) 0%, transparent 45%),
    linear-gradient(160deg, #000000 0%, #1c1c1c 38%, #3a716b 78%, #6BA8A0 100%);
  color: #ffffff;
}
.gradient .tag { color: rgba(255,255,255,0.7); }
.gradient h1, .gradient h2 { color: #ffffff; }
.gradient p { color: rgba(255,255,255,0.85); }
.gradient .text-soft { color: rgba(255,255,255,0.5); }
.gradient .divider { border-color: rgba(255,255,255,0.15); }
.gradient .surface { background: rgba(0,0,0,0.15); }

/* --- Photo overlay (fond image + couche sombre) --- */
.photo-overlay {
  color: #ffffff;
  background-size: cover;
  background-position: center;
}
.photo-overlay::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,
    rgba(0,0,0,0.3) 0%,
    rgba(0,0,0,0.15) 40%,
    rgba(0,0,0,0.6) 100%
  );
  z-index: 1;
}
.photo-overlay .content { position: relative; z-index: 2; }
.photo-overlay .tag { color: rgba(255,255,255,0.8); }
.photo-overlay h1, .photo-overlay h2 { color: #ffffff; }
.photo-overlay p { color: rgba(255,255,255,0.9); }
.photo-overlay .progress-bar { z-index: 2; }
.photo-overlay .swipe-arrow { z-index: 2; }

/* ==========================================
   TYPOGRAPHY
   ========================================== */

.tag {
  font-family: 'Poppins', sans-serif;
  font-size: 17px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 6px;
  margin-bottom: 32px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.dark .tag::before,
.gradient .tag::before {
  content: '';
  display: inline-block;
  width: 22px;
  height: 2px;
  background: rgba(107,168,160,0.7);
  flex-shrink: 0;
}

h1 {
  font-family: 'Oswald', sans-serif;
  font-size: 82px;
  font-weight: 700;
  line-height: 1.0;
  letter-spacing: -2px;
  margin-bottom: 28px;
}

h2 {
  font-family: 'Oswald', sans-serif;
  font-size: 58px;
  font-weight: 600;
  line-height: 1.08;
  letter-spacing: -1.5px;
  margin-bottom: 24px;
}

p {
  font-family: 'Poppins', sans-serif;
  font-size: 26px;
  line-height: 1.65;
  font-weight: 400;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

p.large {
  font-size: 30px;
  line-height: 1.5;
}

/* Chiffre geant (stat slide) */
.big-number {
  font-family: 'Oswald', sans-serif;
  font-size: 160px;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -3px;
}

.light .big-number { color: #6BA8A0; }
.dark .big-number { color: #6BA8A0; text-shadow: 0 0 100px rgba(107,168,160,0.3); }
.gradient .big-number { color: #ffffff; }
.photo-overlay .big-number { color: #ffffff; }

/* Citation */
.quote-mark {
  font-family: 'Oswald', sans-serif;
  font-size: 120px;
  font-weight: 700;
  line-height: 0.6;
  opacity: 0.15;
}

.light .quote-mark { color: #000000; }
.dark .quote-mark { color: #6BA8A0; }

/* ==========================================
   PROGRESS BAR
   ========================================== */

.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 24px 72px 36px;
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 10;
}

.progress-track {
  flex: 1;
  height: 6px;
  border-radius: 3px;
  overflow: hidden;
}

.light .progress-track { background: rgba(0,0,0,0.08); }
.dark .progress-track { background: rgba(255,255,255,0.12); }
.gradient .progress-track { background: rgba(255,255,255,0.2); }
.photo-overlay .progress-track { background: rgba(255,255,255,0.25); }

.progress-fill {
  height: 100%;
  border-radius: 3px;
}

.light .progress-fill { background: #6BA8A0; }
.dark .progress-fill { background: #FFFFFF; }
.gradient .progress-fill { background: #ffffff; }
.photo-overlay .progress-fill { background: #ffffff; }

.progress-label {
  font-size: 20px;
  font-weight: 500;
  white-space: nowrap;
}

.light .progress-label { color: rgba(0,0,0,0.3); }
.dark .progress-label { color: rgba(255,255,255,0.4); }
.gradient .progress-label { color: rgba(255,255,255,0.5); }
.photo-overlay .progress-label { color: rgba(255,255,255,0.5); }

/* ==========================================
   SWIPE ARROW
   ========================================== */

.swipe-arrow {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 72px;
  z-index: 9;
  display: flex;
  align-items: center;
  justify-content: center;
}

.light .swipe-arrow { background: linear-gradient(to right, transparent, rgba(0,0,0,0.04)); }
.dark .swipe-arrow { background: linear-gradient(to right, transparent, rgba(255,255,255,0.05)); }
.gradient .swipe-arrow { background: linear-gradient(to right, transparent, rgba(255,255,255,0.06)); }
.photo-overlay .swipe-arrow { background: linear-gradient(to right, transparent, rgba(0,0,0,0.15)); }

.swipe-arrow svg { opacity: 0.4; }

/* ==========================================
   COMPONENTS
   ========================================== */

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}

.content.bottom {
  justify-content: flex-end;
}

/* --- Feature rows --- */
.feature-row {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 20px 0;
  border-bottom: 1px solid;
}

.feature-icon {
  font-size: 28px;
  width: 36px;
  text-align: center;
  flex-shrink: 0;
  padding-top: 2px;
}

.feature-label {
  font-family: 'Poppins', sans-serif;
  font-size: 24px;
  font-weight: 600;
  display: block;
  margin-bottom: 4px;
}

.light .feature-label { color: #000000; }
.dark .feature-label { color: #FFFFFF; }

.feature-desc {
  font-family: 'Poppins', sans-serif;
  font-size: 20px;
  font-weight: 400;
  display: block;
}

.light .feature-desc { color: #888888; }
.dark .feature-desc { color: rgba(255,255,255,0.5); }

.dark .feature-icon {
  background: rgba(107,168,160,0.10);
  border-radius: 10px;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* --- Step rows --- */
.step-row {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  padding: 22px 0;
  border-bottom: 1px solid;
}

.step-num {
  font-family: 'Oswald', sans-serif;
  font-size: 42px;
  font-weight: 300;
  min-width: 52px;
  line-height: 1;
}

.light .step-num { color: #6BA8A0; }
.dark .step-num { color: #6BA8A0; }

.step-label {
  font-family: 'Poppins', sans-serif;
  font-size: 24px;
  font-weight: 600;
  display: block;
  margin-bottom: 4px;
}

.step-desc {
  font-family: 'Poppins', sans-serif;
  font-size: 20px;
  font-weight: 400;
}

/* --- Quote box (encadre) --- */
.quote-box {
  padding: 28px;
  border-radius: 16px;
  margin-top: 24px;
}

.light .quote-box { background: #F5F5F5; border: 1px solid #E5E5E5; }
.dark .quote-box {
  background: transparent;
  border: none;
  border-left: 3px solid rgba(107,168,160,0.55);
  border-radius: 0;
  padding-left: 24px;
}
.gradient .quote-box {
  background: rgba(0,0,0,0.12);
  border: none;
  border-left: 3px solid rgba(255,255,255,0.35);
  border-radius: 0;
  padding-left: 24px;
}

.quote-label {
  font-size: 18px;
  font-weight: 600;
  opacity: 0.5;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.quote-text {
  font-family: 'Poppins', sans-serif;
  font-size: 24px;
  font-style: italic;
  line-height: 1.5;
}

/* --- Photo containers --- */
.photo-circle {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #6BA8A0;
}

.photo-rounded {
  width: 100%;
  border-radius: 24px;
  object-fit: cover;
}

/* Photo dans le haut de la slide (split haut/bas) */
.photo-top {
  width: 1080px;
  height: 540px;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}

/* Bande coloree derriere la photo (brand touch) */
.photo-accent-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 8px;
  background: #6BA8A0;
  z-index: 5;
}

/* --- CTA button --- */
.cta-button {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 20px 44px;
  background: #FFFFFF;
  color: #000000;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 24px;
  border-radius: 40px;
  margin-top: 32px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.22);
}

/* Sur fond clair, inverser le bouton */
.light .cta-button {
  background: #000000;
  color: #FFFFFF;
}

/* --- Logo lockup (remplace le profile sur les slides hero/CTA) --- */
.logo-lockup {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.logo-img {
  height: 52px;
  width: auto;
  object-fit: contain;
}

/* --- Profile lockup --- */
.profile-lockup {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 40px;
}

.profile-photo {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: cover;
}

/* Fallback si pas de photo : cercle colore + initiale */
.profile-initial {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #6BA8A0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Oswald', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: #ffffff;
}

.profile-name {
  font-family: 'Poppins', sans-serif;
  font-size: 22px;
  font-weight: 600;
  letter-spacing: 1px;
}

.light .profile-name { color: #000000; }
.dark .profile-name { color: #FFFFFF; }
.gradient .profile-name { color: #ffffff; }
.photo-overlay .profile-name { color: #ffffff; }

/* --- Accent line (decoration subtle) --- */
.accent-line {
  width: 64px;
  height: 4px;
  background: #6BA8A0;
  border-radius: 2px;
  margin-bottom: 32px;
}

/* --- Accent orange (#E8845A) --- */
/* Utiliser en remplacement du teal pour varier l'accentuation.
   Ex : .tag.orange, .cta-button.orange, .accent-line.orange */

.tag.orange { color: #E8845A; }
.dark .tag.orange { color: #E8845A; }
.gradient .tag.orange { color: rgba(232,132,90,0.9); }

.accent-line.orange { background: #E8845A; }

/* CTA orange — alternatif au blanc sur gradient/dark */
.cta-button.orange {
  background: #E8845A;
  color: #FFFFFF;
}
.light .cta-button.orange {
  background: #E8845A;
  color: #FFFFFF;
}

/* Highlight ponctuel — encadre un mot ou une stat */
.highlight-orange {
  color: #E8845A;
  font-weight: 600;
}

/* --- Separator dot --- */
.dot-separator {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 24px 0;
}

.dot-separator::before,
.dot-separator::after {
  content: '';
  flex: 1;
  height: 1px;
}

.light .dot-separator::before,
.light .dot-separator::after { background: #E5E5E5; }
.dark .dot-separator::before,
.dark .dot-separator::after { background: rgba(255,255,255,0.1); }

.dot-separator span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #6BA8A0;
}
</style>
</head>
<body>
<div class="slide {THEME_CLASS}">
  <div class="content">
    {SLIDE_CONTENT}
  </div>
  {PROGRESS_BAR}
  {SWIPE_ARROW}
</div>
</body>
</html>
```

---

## Progress Bar HTML

Generer pour chaque slide. Remplacer `{PCT}` avec `((slideIndex) / (totalSlides - 1)) * 100` et `{LABEL}` avec `"slideIndex+1/totalSlides"`.

Slide 1 (index 0) = 0%, derniere slide = 100%.

```html
<div class="progress-bar">
  <div class="progress-track">
    <div class="progress-fill" style="width: {PCT}%;"></div>
  </div>
  <span class="progress-label">{LABEL}</span>
</div>
```

---

## Swipe Arrow HTML

Sur chaque slide SAUF la derniere.

```html
<div class="swipe-arrow">
  <svg width="36" height="36" viewBox="0 0 24 24" fill="none">
    <path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
```

---

## Slide Types

### 1. Hero — Light theme

Le hook. Statement bold. Logo en haut.

```html
<div class="profile-lockup">
  <img class="logo-img" src="assets/CYAN 5.png" alt="Hostopia" />
</div>
<span class="tag">{CATEGORY_TAG}</span>
<h1>{HOOK_HEADLINE}</h1>
<p class="large">{SUBTITLE}</p>
```

### 1b. Hero avec photo de fond — Photo-overlay theme

Meme structure mais avec une image plein ecran. Plus impactant visuellement. Utiliser quand une image pertinente est disponible.

**Important** : ajouter `style="background-image: url('{IMAGE_URL}');"` sur la div `.slide`.

```html
<!-- Sur la div .slide, ajouter : class="slide photo-overlay" style="background-image: url('{IMAGE_URL}');" -->
<div class="content bottom">
  <div class="logo-lockup">
    <img class="logo-img" src="assets/BLANC 1.png" alt="Hostopia" />
  </div>
  <span class="tag">{CATEGORY_TAG}</span>
  <h1>{HOOK_HEADLINE}</h1>
  <p class="large">{SUBTITLE}</p>
</div>
```

### 2. Problem — Dark theme

Le probleme. Visceral.

```html
<span class="tag">{TAG}</span>
<h2>{PROBLEM_HEADLINE}</h2>
<p>{PROBLEM_BODY}</p>
```

### 3. Solution / Shift — Gradient theme

La reponse. Claire et concise.

```html
<span class="tag">{TAG}</span>
<h2>{SOLUTION_HEADLINE}</h2>
<p>{SOLUTION_BODY}</p>
<div class="quote-box">
  <div class="quote-label">{QUOTE_LABEL}</div>
  <div class="quote-text">"{QUOTE_TEXT}"</div>
</div>
```

La quote box est optionnelle — seulement si une citation, stat ou exemple pertinent existe.

### 4. Features / Key Points — Light theme

3-4 takeaways avec emojis.

```html
<span class="tag">{TAG}</span>
<h2>{FEATURES_HEADLINE}</h2>

<div class="feature-row divider">
  <span class="feature-icon">{EMOJI}</span>
  <div>
    <span class="feature-label">{LABEL}</span>
    <span class="feature-desc">{DESCRIPTION}</span>
  </div>
</div>
<!-- Repeter pour chaque feature (3-4 max) -->
```

### 5. Details / Depth — Dark theme

Points de support. Feature rows ou paragraphes.

```html
<span class="tag">{TAG}</span>
<h2>{DETAILS_HEADLINE}</h2>
<p>{DETAILS_BODY_1}</p>
<p style="margin-top: 20px;">{DETAILS_BODY_2}</p>
```

### 6. Steps / How-to — Light theme

Etapes actionnables. 3 max.

```html
<span class="tag">{TAG}</span>
<h2>{STEPS_HEADLINE}</h2>

<div class="step-row divider">
  <span class="step-num">01</span>
  <div>
    <span class="step-label">{STEP_TITLE}</span>
    <span class="step-desc">{STEP_DESCRIPTION}</span>
  </div>
</div>
<!-- Repeter pour chaque etape (3 max) -->
```

### 7. CTA — Gradient theme

Appel a l'action. Pas de swipe arrow. Progress a 100%.

```html
<div class="content" style="justify-content: center; align-items: center; text-align: center;">
  <div class="logo-lockup" style="justify-content: center;">
    <img class="logo-img" src="assets/BLANC 1.png" alt="Hostopia" />
  </div>
  <h2>{CTA_HEADLINE}</h2>
  <p>{CTA_BODY}</p>
  <div class="cta-button">{CTA_TEXT}</div>
</div>
```

---

## Variantes de layout

Ces variantes peuvent remplacer ou completer les slides standard pour casser la monotonie et creer du rythme visuel.

### Stat / Chiffre-cle

Un chiffre qui claque + contexte. Scroll-stopper. Bon pour slides 4 ou 5.

```html
<span class="tag">{TAG}</span>
<div class="big-number">{NUMBER}</div>
<h2 style="margin-top: 16px;">{STAT_LABEL}</h2>
<p class="text-soft">{CONTEXT}</p>
```

Exemples : "73%", "2M+", "10x", "45 min"

### Citation plein ecran

Grande citation. Minimaliste. Bon pour slides 3 ou 5.

```html
<div class="content" style="justify-content: center;">
  <div class="quote-mark">"</div>
  <p class="large" style="margin-top: 16px; font-style: italic;">{QUOTE_TEXT}</p>
  <div class="accent-line" style="margin-top: 32px;"></div>
  <p class="text-soft" style="font-size: 22px;">{ATTRIBUTION}</p>
</div>
```

### Split haut/bas (photo + texte)

Photo dans la moitie haute, texte dans la moitie basse. Bon pour slides 2, 4 ou 5.

**Important** : la photo est positionnee en absolu. Le contenu texte doit etre en bas.

```html
<!-- Ajouter avant .content : -->
<img class="photo-top" src="{IMAGE_URL}" alt="" />

<div class="content" style="justify-content: flex-end; padding-top: 560px;">
  <span class="tag">{TAG}</span>
  <h2>{HEADLINE}</h2>
  <p>{BODY}</p>
</div>
```

### Photo circulaire + texte (temoignage, apropos)

Photo ronde a gauche du heading. Bon pour CTA ou slide "qui suis-je".

```html
<div class="content" style="justify-content: center; align-items: center; text-align: center;">
  <img class="photo-circle" src="{PHOTO_URL}" alt="" />
  <h2 style="margin-top: 32px;">{HEADLINE}</h2>
  <p>{BODY}</p>
</div>
```

---

## Images

### Sources d'images

Par ordre de priorite :
1. **Photos de l'utilisateur** — les plus authentiques (portrait, setup, produit)
2. **Images stock** — Unsplash API (gratuit, haute qualite, pas de watermark)

### Integration technique

Les images peuvent etre integrees de deux facons :

**URL directe** (Unsplash, image hebergee) :
```html
<img src="https://images.unsplash.com/photo-xxx?w=1080&q=80" alt="" />
```

**Background image** (pour photo-overlay) :
```html
<div class="slide photo-overlay" style="background-image: url('https://images.unsplash.com/photo-xxx?w=1080&q=80');">
```

### Regles images

- Format carre ou portrait (pas de paysage etire)
- Resolution minimum 1080px de large
- Pour les photos de fond : choisir des images avec de l'espace "vide" ou le texte peut se poser
- Ne pas mettre d'image sur chaque slide — alterner slides texte-only et slides avec images pour creer du rythme
- Maximum 2-3 slides avec images sur un carousel de 7

---

## Rules

1. **Alterner les themes** : light -> dark -> gradient -> light -> dark -> light -> gradient. La variante photo-overlay remplace n'importe quel theme quand une image pertinente est disponible.
2. **Progress bar sur chaque slide**. Formule : `((slideIndex) / (totalSlides - 1)) * 100` ou slideIndex commence a 0. Slide 1 = 0%, derniere slide = 100%.
3. **Swipe arrow sur chaque slide sauf la derniere**.
4. **Max contenu par slide** : 1 heading + 1 paragraphe court, OU 1 heading + 3-4 feature/step rows, OU 1 big-number + contexte.
5. **Ne jamais chevaucher la progress bar** : padding bottom de 100px minimum.
6. **Google Fonts** : toujours inclure le @import dans chaque fichier HTML — HCTI les charge nativement.
7. **Rythme visuel** : varier les types de slides. Pas 7 slides identiques. Alterner densite (texte dense vs. slide aeree), presence d'images, et types de layout.
8. **Langue** : toujours ecrire dans la langue du projet (francais par defaut), meme si la source est en anglais ou autre.
9. **Contraste minimum** : tout texte doit avoir un ratio de contraste de 4.5:1 minimum sur son fond. Sur photo-overlay, le gradient sombre garantit la lisibilite.
10. **1 idee par slide** : pas d'exception.
11. **Logos — fonds transparents obligatoires** : utiliser `assets/logo-light.png` (wordmark teal transparent) sur les slides `.light`, et `assets/logo-dark.png` (wordmark blanc transparent) sur les slides `.dark`, `.gradient` et `.photo-overlay`. Ne jamais utiliser un logo avec fond blanc opaque — le carré blanc est visible sur les slides sombres et les photos.
12. **Pas de référence YouTube ou à la source vidéo** : le carousel doit sembler être du contenu original de la marque. Les labels de quote box doivent être `"Le constat"`, `"En pratique"`, `"Retour terrain"`, etc. — jamais `"Extrait de la vidéo"`, `"Citation YouTube"`, ou toute mention d'une source externe.
13. **Couleur orange (#E8845A)** : disponible en accent secondaire via `.tag.orange`, `.accent-line.orange`, `.cta-button.orange`, `.highlight-orange`. Utiliser sur 1-2 éléments max par carousel pour créer un contraste ponctuel avec le teal. Ne pas mélanger teal et orange sur la même slide.
