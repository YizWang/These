1. corpus.txt 
C'est la sortie du script "data_preprocessing.ipynb".
c'est le contenu texutuel extrait à paritr du corpus monolingue français PANACEA - domaine de l’environnement. On garde uniquement les titres et les paragraphes.

2. ref_RF.csv (1314 paires)
C'est la référence proposée par Colborne et Drouin. Les données sont extraites à partir du dictionnaire DiCoEnviro. 
Le fichier est composé de 5 colonnes: le terme d'entrée, le patron du terme d'entrée, le terme relié au terme d'entrée, le patron du terme relié au terme d'entrée, la relation entre eux.

3. ref_projection.csv (832 paires)
La Ref_Projtion sur laquelle nous appliquerons les règles de projection est basée sur la Ref_CD. Nous avons exclu les verbes (225 paires) et DRV (259 paires) du Ref_CD.
Le fichier est composé de 5 colonnes: le terme d'entrée, le patron du terme d'entrée, le terme relié au terme d'entrée, le patron du terme relié au terme d'entrée, la relation entre eux.

3. output_termsuite.tsv
C'est la sortie de termsuite. On a utilisé TermSuite pour extraire les candidat termes à partir du corpus "corpus.txt". 
La sortie est composé de 6 colonnes: rank du candidat, type, pattern, pilot, fréquence et spécificité.

4. projection_brut.csv (18328 paires)
c'est la sortie du script "projection.py". le fichier est composé de 18328 paires de candidats MWT reliés par trois catégories de relation: ANTI, QSYN et HYP.
Le fichier est composé de 11 colonnes: Candidat1, pattron de candidat1, fréquence de candidat1 dans le corpus, spécificité de candidat1, Candidat2, pattron de candidat2, fréquence de candidat2 dans le corpus, spécificité de candidat2, la paire de termes simples à partir de la quelle est générée cette paire de candidats MWT, information sur la permutation, relation inférée.

5. clean_sym.csv (18328 paires)
C'est la sortie de script "clean_sym.py" dans laquelle, les symétries sont identifiées et se déplacent à la fin du fichier.
Le fichier est composé de 11 colonnes: Candidat1, pattron de candidat1, fréquence de candidat1 dans le corpus, spécificité de candidat1, Candidat2, pattron de candidat2, fréquence de candidat2 dans le corpus, spécificité de candidat2, la paire de termes simples à partir de la quelle est générée cette paire de candidats MWT, information sur la permutation, relation inférée.

6. sym_cleaned.csv (12604 paires)
les symytries sont supprimées à partir du fichier "clean_sym.csv".
Le fichier est composé de 11 colonnes: Candidat1, pattron de candidat1, fréquence de candidat1 dans le corpus, spécificité de candidat1, Candidat2, pattron de candidat2, fréquence de candidat2 dans le corpus, spécificité de candidat2, la paire de termes simples à partir de la quelle est générée cette paire de candidats MWT, information sur la permutation, relation inférée.

7. clean_pos.csv (12604 paires)
C'est la sortie de script "clean_pos.py" dans laquelle, les paires où le mot partagé dans les deux candidats MWT n'a pas la même partie du discours sont identifiées et se déclacent à la fin du fichier.

8. pos_cleaned.csv (12604 paires)
Comme il y a l'erreur d'éttiquetage de treetagger, on a décidé de garder les paires où le mot partagé dans les deux candidats MWT n'a pas la même partie du discours

8. annotation.csv (231 paires)
les données annotées manuellement
Le fichier est composé de 10 colonnes : index du couple, index du terme1, terme1, index du terme2, terme2, dépendance1, dépendance2, relation inférée, annotation sur la préservation, annotation sur la validité.


#############################################################################################
Scripts
1. data_preprocessing.ipynb
Entrée: le corpus PANACEA. Ce sont les documents en format XML.
Sortie: le fichier "corpus.txt"

Le script est utilisé pour extraire le contunu textuel du corpus PANACEA, normaliser les caractères, lemmatizer les mots et mettre les mots en minuscul.

2. projection.py
Entrée: le fichier "ref_projection.csv" et le fichier "output_termsuite.tsv"
Sortie: "projection_brut.csv"

Le script projecte les relations entre les SWTs dans "ref_projection.csv" sur les candidats MWT extraits par TermSuite.

3. clean_sym.py
Entrée: "projection_brut.csv"
Sortie: "clean_sym.csv"

Le script est utilisé pour identifier les symétries et les déplacent à la fin du fichier.

4. clean_pos.py
Entrée: sym_cleaned.csv
Sortie: clean_pos.csv

Le script est utilisé pour identifier les paires où le mot partagé dans les deux candidats MWT n'a pas la même partie du discours et les déplacent à la fin du fichier.

5. add_info.py
Entrée:
Sortie:

6. term_context.py
Entrée: les paires de candidats validés par les ressources terminologiques.
Sortie: un fichier csv où se trouvent 5 contextes différents pour chaqun term validé.

Le script est utilisé pour extraire les contextes pour chaque candidat validé à partir du fichier "corpus.txt"

