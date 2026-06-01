#!/usr/bin/env bash
set -euo pipefail

DEST="$HOME/Desktop/Hostopia/carousels"
SRC="tmp/carousel"

mkdir -p "$DEST"

echo "Destination : $DEST"
echo ""

carousel_num=0

# Parcourir les dossiers dans l'ordre chronologique (plus ancien en premier)
while IFS= read -r folder; do
    [[ -d "$folder" ]] || continue

    # Vérifier qu'il y a des slides PNG
    png_count=$(find "$folder" -maxdepth 1 -name "slide-*.png" | wc -l | tr -d ' ')
    [[ "$png_count" -eq 0 ]] && continue

    carousel_num=$((carousel_num + 1))
    slide_num=0

    # Trier numériquement (slide-1.png avant slide-10.png)
    while IFS= read -r png; do
        slide_num=$((slide_num + 1))
        dest_file="$DEST/carousel${carousel_num}-slide${slide_num}.jpg"
        # Conversion PNG → JPEG via sips (outil macOS natif, qualité 85)
        sips -s format jpeg -s formatOptions 85 "$png" --out "$dest_file" > /dev/null
    done < <(find "$folder" -maxdepth 1 -name "slide-*.png" | sort -t- -k2 -n)

    echo "carousel${carousel_num} ($(basename "$folder")) → ${slide_num} slides exportées"
done < <(ls -dtr "$SRC"/*/ 2>/dev/null | sed 's|/$||')

echo ""
echo "Terminé : ${carousel_num} carousel(s) exporté(s) dans $DEST"
