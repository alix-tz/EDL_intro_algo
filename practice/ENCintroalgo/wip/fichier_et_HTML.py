
# initialisation de deux variables destinées à contenir les données d'en-tête et les données des documents
header = []
documents = []

# Ouverture du fichier adele_wo.tsv qui se situe dans le même dossier que ce script
with open('data/adele_wo.tsv', encoding='utf-8') as csv_file:
    # On parcourt le fichier ouvert ligne par ligne
    for ligne_courante in csv_file.readlines():
      # On commence par supprimer le caractère "nouvelle ligne" qui se trouve à la fin du dernier champ
      ligne_courante = ligne_courante.replace("\n", "")
      # On scinde ensuite chaque ligne en colonnes grâce au délimiteur "\t" (tabulation) qui sépare les champs les uns des autres
      # Le résultat est une liste de champs.
      # Exemple:
      # ma_variable = "a@b@c"
      # ma_variable.split("@") donnera la liste suivante : ["a", "b", "c"]
      ligne_decoupee = ligne_courante.split("\t")
      # On sauvegarde le travail pour la ligne courante en stockant le résultat dans la liste documents
      documents.append(ligne_decoupee)

# La première ligne du fichier (l'en-tête) est séparée du reste des données grâce à "pop"
# En utilisant .pop(0) au lieu de .pop(), je récupère la case numéro 0 de la liste documents (c'est-à-dire la première case)
header = documents.pop(0)

# Informations à propos des documents
print("=========================")
print("Champs disponibles :", header)
print("Nombre de documents :", len(documents))


# Affichage des documents
numero_index = header.index("N°")
types_index = header.index("types")
title_index = header.index("title")
lang_codes_index = header.index("langCodes")
creation_norm_index = header.index("creation_norm")

# Pour chaque document, j'affiche les champs que j'ai choisi au prealable :
for doc in documents:
  print("-------------------------")
  print("Doc ", doc[numero_index], ":")
  print("    Title:", doc[title_index])
  print("    Types:", doc[types_index])
  print("    Lang:", doc[lang_codes_index])
  print("    Creation:", doc[creation_norm_index])


# =============== PARTIE 1 ===============
# Exercices

# 1) Afficher les documents dont le numéro est pair.
#
#    Indice 1 : pour savoir si un nombre est pair, utiliser l'opérateur % (modulo) qui renvoie le reste de la division euclidienne comme dans l'exemple ci-dessous :
#    nombre = 9
#    if nombre % 2 == 0:
#      print("je suis pair car le reste de la division euclidienne par 2 est 0")
#    else:
#      print("je suis impair car la division a laissé un reste")
#
#    Indice 2 : il faut d'abord s'assurer que le numéro de dossier soit une valeur de type Entier (int)
#    Or ici toutes les valeurs du document (qui est un fichier texte) sont par défaut des chaines de caractères
#    Pour (tenter) de convertir une valeur en entier, il est possible de faire comme ceci:
#    mon_numero = int("12345")

# 2) Afficher les documents dont le numéro est impair ET supérieur à 50
# Indice : pour savoir si un nombre est impair, il suffit de vérifier si le reste de la division euclidienne par 2 est différent de 0
#
# 3) Afficher les documents dont le champ creation_norm est supérieur à 1200 et dont la langue est exclusivement "fre". Combien sont-ils ?
#
# 4) Créer une liste documents_quatorzieme_siecle et y placer les documents adéquats en fonction de la valeur du champ creation_norm

# =============== PARTIE 2 ===============
# Création d'une page HTML des résultats

# Initialisation d'une variable de type chaine de caractères contenant le squelette d'une page HTML :
# La chaine de caractère a pu être étalée sur plusieurs lignes car elle est entourée par une paire de trois guillemets doubles consécutifs
squelette_html = """
<!doctype HTML>
<html>
    <head>
    {titre_html}
    </head>
    <body>
    {contenu_html}
    </body>
</html>
"""

# il possible de remplacer ultérieurement les termes entre accolades {title} et {contenu_html} avec les données que l'on souhaite grâce à .format :
#ma_page_html = squelette_html.format(contenu_html="Document 1, Document2, etc. Toutes les données que je souhaite", titre_html="MON_TITRE")
#print(ma_page_html)

# il est nécessaire de fournir toutes les variables attendues {titre_html} et {contenu_html}, sinon une erreur se produit :
#ma_page_html = squelette_html.format(contenu_html="MES DOCUMENTS")

# Le but de l'exercice est de produire une page HTML listant tous les documents du quatorzième sicèle issus de l'exercice précédent
# Il est demandé que la page ainsi produite soit valide au sens HTML (utiliser l'outil de validation vu en cour)

# Exercices

# 1) Utiliser une boucle "for" pour remplir une variable nommée numeros_dossiers avec les numéros des dossiers des documents de la liste documents_quatorzieme_siecle.
#    Grâce au squelette HTML et à la fonction .format ci-dessus, produire une page HTML affichant la liste des numéros de dossiers du quatorzième siècle
#    * Les numéros de dossier seront affichés séparés par une virgule.
#    * Le titre de la page web devra être "Mes documents du XIVème siècle"
#    Indice : à l'inverse de .split('\t') qui permet de séparer une chaîne de caractères en une liste de valeurs,
#             la fonction "join" permet de joindre toutes les valeurs d'une liste pour produire une chaîne de caractères.
#             numero_telephone_factice = ".".join(["06", "08", "10", "40", "50"]) va ainsi joindre toutes les valeurs de la_liste_en une chaine de caractères "06.08.10.40.50"

# 2) Afficher les numéros de dossier est intéressant mais cela n'est pas suffisant.
#    Pour afficher une liste de documents dans une page HTML, il faut d'abord décider des données que l'ont souhaite voir affichées :
#    Numéro de document, titre de document, sous-titre, date de création, langues et institution de conservation
#    Nous pouvons structurer ces informations en HTML et décider que chaque document sera représenté par une balise <article></article>
#    Le but de cet exercice est de trouver une représentaion HTML adéquate pour un document donné. La page web finale sera produite lors du prochain exercice.
#    Indice : tout comme il est possible de stocker le squelette d'une page web dans une variable, il est possible de stocker le squelette d'un article dans une variable
#             essayez d'agrémenter la variable squelette_article en lui ajoutant un titre (balise <h1>),
#
# Voici les données de test à exploiter :
numero_doc = 100
titre_doc = "Je suis le titre du document 100"
date_creation_doc = 1234
langues_doc = "lat"
sous_titre_doc = "Je suis le sous-tire du document 100"
institution_doc = "Archives nationales (France)"

squelette_article = """
<article>
  A vous de jouer
</article>
"""

# 3) En reprenant le squelette de l'article précédemment crée ainsi que le squelette de la page web, produire une page HTML listant tous les articles du quatorizième siècle
#    Indice : vous devez joindre tous les articles <articles></articles> entre eux avec la fonction "join" avant de les utiliser dans le squelette de la page HTML
articles_du_xiveme_siecle = []

