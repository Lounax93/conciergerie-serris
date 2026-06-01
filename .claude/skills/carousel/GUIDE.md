# Carousel Generator — Guide d'installation

Tu veux generer des carousels prets a poster en une commande ? Voici comment installer le systeme.

**Temps d'installation : ~5 minutes.**
**Format : Instagram (1080x1350) et YouTube Community Posts (jusqu'a 10 images).**

---

## Ce qu'il te faut

1. **Claude Code** installe sur ton ordi ([claude.ai/code](https://claude.ai/code))
2. **Un compte HCTI** (gratuit ou payant) sur [htmlcsstoimage.com](https://htmlcsstoimage.com) — c'est l'API qui transforme le HTML en images PNG
3. **Un compte Unsplash Developer** (gratuit) sur [unsplash.com/developers](https://unsplash.com/developers) — pour les images stock automatiques (optionnel)

---

## Installation

### 1. Copier les fichiers

Copie le dossier `carousel/` dans `.claude/skills/` de ton projet :

```
ton-projet/
  .claude/
    skills/
      carousel/
        SKILL.md
        templates.md
        content-guide.md
        content-eval-checklist.md
        GUIDE.md (ce fichier)
```

### 2. Configurer les cles API

Cree un fichier `.env` a la racine de ton projet et colle tes cles dedans :

```
HCTI_USER_ID=ton_user_id
HCTI_API_KEY=ta_cle_api
UNSPLASH_ACCESS_KEY=ta_cle_unsplash
```

- **HCTI** : connecte-toi sur htmlcsstoimage.com/dashboard, tu trouveras tes cles dans les settings
- **Unsplash** : cree une app sur unsplash.com/developers, copie l'Access Key

### 3. Installer les outils

Dis a Claude :

> Installe les outils necessaires pour le skill carousel : cree un dossier tools/ s'il n'existe pas, installe le package Python requests, et verifie que youtube_extract.py et render_hcti.py sont en place. S'ils manquent, cree-les.

Claude se charge du reste.

### 4. Personnaliser ton branding

Dis a Claude :

> Change le branding du carousel avec mes couleurs : primaire [ta couleur], sombre [ta couleur], accent [ta couleur]. Ma font de titre est [ta font], ma font de body est [ta font]. Mon nom c'est [TON NOM] et ma photo de profil est [URL de ta photo Instagram/Twitter/site].

Exemple :

> Change le branding du carousel avec mes couleurs : primaire #FF6B35, sombre #1A1A2E, accent #E94560. Mes fonts sont Montserrat pour les titres et Inter pour le body. Mon nom c'est SOPHIE MARTIN et ma photo de profil est https://monsite.com/photo.jpg

Si tu n'as pas d'URL de photo, Claude affichera l'initiale de ton nom dans un cercle colore.

Claude modifie `templates.md` pour toi — tu n'as pas besoin d'ouvrir le fichier.

### 5. Changer la langue (si necessaire)

Par defaut, les carousels sont generes en francais. Si tu veux une autre langue, dis a Claude :

> Change la langue par defaut du carousel en [anglais/espagnol/etc.]

---

## Utilisation

### Generer un carousel

Dis a Claude :

> /carousel https://youtube.com/watch?v=VIDEO_ID

Le systeme va :
1. Extraire le contenu de la video
2. Chercher des images pertinentes
3. Generer le contenu de 5 a 10 slides
4. Creer les images PNG pretes a poster

Les fichiers sortent dans `tmp/carousel/{nom-de-la-video}/`.

### Utiliser tes propres photos

Quand Claude te demande si tu as des photos, reponds :

> Utilise ma photo [URL ou chemin] pour la slide 1, et [URL ou chemin] pour la slide 5.

Ou :

> J'ai mis mes photos dans tmp/carousel/images/, utilise-les.

Tes photos remplaceront les images stock sur les slides concernees.

### Modifier une slide

Dis a Claude :

> Change le titre de la slide 3
> Remplace l'image de la slide 1 par ma photo [URL]
> La slide 5 est trop chargee, simplifie
> Ajoute une slide stat avec le chiffre 73%

Seule la slide modifiee sera regeneree.

### Changer le nombre de slides

> Fais-moi un carousel de 10 slides (pour YouTube Community)
> Je veux seulement 5 slides

---

## Limites

- **HCTI gratuit** : 50 images/mois (= ~7 carousels). Le plan payant monte a 1000/mois.
- **Unsplash** : 50 requetes/heure en mode gratuit. Largement suffisant.
- **Sans Unsplash** : le skill fonctionne en mode texte-only. C'est deja tres bien.
- **Source** : pour l'instant le skill fonctionne a partir de videos YouTube. D'autres sources arrivent.

---

## FAQ

**Je peux changer les fonts apres coup ?**
Oui. Dis a Claude "change les fonts du carousel en [font titre] et [font body]".

**Ca marche pour d'autres langues que le francais ?**
Oui. Dis a Claude de changer la langue par defaut.

**Je peux poster sur YouTube Community aussi ?**
Oui. Le format 1080x1350 fonctionne sur Instagram ET YouTube. Tu peux aller jusqu'a 10 slides pour YouTube.

**Je dois etre technique pour utiliser ca ?**
Non. Tu copies un dossier, tu colles 3 cles API, et tu parles a Claude. C'est tout.
