# Conciergerie Serris — Site Hostopia

Mini-site production-ready pour la conciergerie Airbnb Hostopia à Serris (77, Seine-et-Marne).

## Structure

```
conciergerie-serris/
├── index.html              # Landing page principale
├── qui-sommes-nous.html    # Page À propos
├── sitemap.xml             # SEO sitemap
├── robots.txt              # SEO robots
├── blog/
│   └── index.html          # Blog (placeholder)
├── assets/
│   ├── logo-blanc.png      # Logo pour fond sombre
│   └── logo-teal.png       # Logo pour fond clair
└── styles/
    └── base.css            # CSS partagé entre toutes les pages
```

## Déployer sur Vercel via GitHub

### 1. Créer le dépôt GitHub

```bash
# Dans le dossier du projet
git init
git add .
git commit -m "feat: init mini-site conciergerie Serris"

# Sur GitHub : créer un nouveau dépôt "conciergerie-serris"
git remote add origin https://github.com/TON_USERNAME/conciergerie-serris.git
git branch -M main
git push -u origin main
```

### 2. Connecter à Vercel

1. Aller sur **vercel.com** → "Add New Project"
2. Importer le dépôt `conciergerie-serris` depuis GitHub
3. Framework Preset : **Other** (site HTML statique)
4. Root Directory : `.` (racine du projet)
5. Cliquer **Deploy**

Vercel détectera automatiquement qu'il s'agit d'un site statique et déploiera `index.html` comme page d'accueil.

### 3. Configurer le domaine personnalisé (optionnel)

Dans le dashboard Vercel → Settings → Domains :
- Ajouter `conciergerie-serris.hostopia.fr`
- Créer un enregistrement CNAME chez votre registrar vers `cname.vercel-dns.com`

### 4. Mises à jour

Chaque `git push origin main` déclenche un redéploiement automatique sur Vercel.

## Personnalisation requise

Avant la mise en production, remplacer :
- `https://wa.me/33XXXXXXXXX` → le vrai numéro WhatsApp (format : `https://wa.me/33612345678`)
- `contact@hostopia.fr` → l'email de contact réel
- `+33XXXXXXXXX` dans le schema.org → le vrai numéro de téléphone

## SEO

- Meta tags complets sur chaque page
- Open Graph pour partages réseaux sociaux
- Schema.org LocalBusiness avec adresse Serris
- Canonical URL sur chaque page
- sitemap.xml + robots.txt configurés
- Structure HTML sémantique (header, main, article, footer)

## Stack technique

- HTML5 sémantique (zéro dépendance JS)
- CSS custom avec variables, animations et glassmorphism
- Google Fonts : Bricolage Grotesque + DM Sans
- Intersection Observer pour les animations au scroll
- WhatsApp floating button
