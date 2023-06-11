# cassiopee-74
Detection de visages sur flux compressé

1ère étape : Récupération des matrices de luminance sur JM Master

  Ouvrir le logiciel JM Master, faire un build et un run puis lancer les 2 commandes suivantes
  
    - ffmpeg -i Video.mp4 -c:v libx264 Video.264 (pour convertir Video.mp4 en format .264 depuis laquelle nous pouvons extraire nos composantes d'intérêts)
    
    - ./ldecod -i "/path/to/Video.264" -o Video.yuv 
 
 
2ème étape : Conversion en numpy array 

  Ouvrir le script create_mat.py et décommenter les lignes à la fin. 
  
  Donner à la variable filename le nom du fichier contenant la matrice extraite précedemment
  
  Lancer la fonction correct_file(filename)
  
  Donner à corrected_filename le nom du fichier généré par la fonction correct_file(filename)
  
  Lancer la fonction create_matrix(corrected_filename)
  
  
3ème étape : Création des masks


4ème étape : Répéter ce processus pour chaque vidéo et concaténer les frames ensembles, puis les masks ensembles


5ème étape : Filtrage (étape non obligatoire)
  
  
  


