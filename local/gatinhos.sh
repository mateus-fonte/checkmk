#!/bin/bash

folder_path="/home/mateuscheckmk/Desktop/mateus_present"
gato_count=$(ls "$folder_path" | wc -l)

if [ "$gato_count" -gt 10 ]; then
    echo "0 \"Numero de fotos de gatinhos\" cat_photos=$gato_count Voce e um amante de gatos!"
elif [ "$gato_count" -gt 5 ]; then
    echo "1 \"Numero de fotos de gatinhos\" cat_photos=$gato_count Voce nao gosta de gatos?"
else
    echo "2 \"Numero de fotos de gatinhos\" cat_photos=$gato_count VOCE ODEIA GATOS! Existe algum problema?"
fi
