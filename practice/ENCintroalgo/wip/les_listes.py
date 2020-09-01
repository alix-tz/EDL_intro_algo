
print("======================")
print("      Les listes     ")
print("======================")

print("----- Préambule ------")
ma_liste = []
print(ma_liste)
ma_liste.append(1.0)
print(ma_liste)
ma_liste.append(2)
print(ma_liste)
ma_liste.append("trois")
print(ma_liste)
ma_liste.append("4")
print(ma_liste)
ma_liste.append(ma_liste[1] + 3)
print(ma_liste)

# en retirant le dernier élément 
le_cinquieme_element = ma_liste.pop()
print(le_cinquieme_element)
# vérifions le contenu de la liste
print(ma_liste)
ma_liste.append("numéro cinq")
ma_liste.append(le_cinquieme_element + 1)
print(ma_liste)

print("----- Exercice 1 : ajout et suppression -----")
# ================
livre1 = "La République"
livre2 = "Gorgias"
livre3 = "Le Manuel"
livres_dans_les_cartons = [livre2, "Facture de livraison"]
livres_en_rayon = [livre1, livre3]

# 1.a comment mettre en rayon le livre 2 ?
livres_en_rayon.append(livre2)
# 1.b comment procéder pour mettre le livre 2 en seconde position ?
livres_en_rayon = [livre1, livre2,livre3]
# 1.c comment enlever tous les livres en rayon et les mettre dans les cartons ?
livres_dans_les_cartons = livres_en_rayon
livres_en_rayon = []
# 1.d comment supprimer la facture de livraison du carton ? 
livres_dans_les_cartons.pop()

# =================
# parcours de liste
# =================
#print("=====================")
#print("Livres en rayon: ")
#for livre in livres_en_rayon:
#  print("- ", livre)

#print("=====================")
#print("utilisation de la boucle 'while': ")
#while len(livres_dans_les_cartons) > 0:
#  livres_en_rayon.append(livres_dans_les_cartons.pop())
  
#print("Livres en rayon: ")
#for livre in livres_en_rayon:
#  print("- ", livre)

#livres_dans_les_cartons = []
#print("Livres dans les cartons: ")
#for livre in livres_dans_les_cartons:
#  print(livre)

# 1.e Pouvez-vous expliquer l'ordre des livres affiché ?
# 1.f Quelles sont les instructions qui ont vidé la liste livres_dans_les_cartons ?
# 1.g Que se passe-t-il si on exécute l'instruction livres_dans_les_cartons.pop() une nouvelle fois ?

print("----- Exercice 2 : liste d'indexes -----")
# Hypothèse : Parmi les livres en rayons, certains ont été vendus
livres_en_rayon = [livre1, livre2, livre3]
index_des_livres_vendus = [0, 2]
# 3.a Utilisez une boucle "for" pour afficher le nom des livres vendus en utilisant les variables index_des_livres_vendus et livres_en_rayon
for index_livre_vendu in index_des_livres_vendus:
  print(livres_en_rayon[index_livre_vendu])

print("----- Exercice 3 : boucles imbriquées -----")
livres_vendus = ["Livre Vendu1", "Livre Vendu2"]
livres_perdus = ["Livre Perdu1"]
livres_vendus_et_perdus = [livres_vendus, livres_perdus]
# 4.a Quelle est la longueur de livres_vendus_et_perdus ?
print(len(livres_vendus_et_perdus)) # Affiche 2 : la liste est une liste à deux éléments (deux sous-listes)
# 4.b Que va afficher le bloc d'instructions suivant ?
for liste_livres in livres_vendus_et_perdus:
  print("Liste de", len(liste_livres), "élément(s)")
  for livre in liste_livres:
    print("* ", livre)

print(livres_vendus_et_perdus[1])

print("----- Exercice 4 : inversion -----")
liste_nombres_4 = [0,1,2,3,4,5,6,7,8,9]
liste_inversee = []
# À l'aide d'une boucle "for", remplir la variable liste_inversee
# avec les valeurs de liste_nombres_5, dans le sens inverse (du plus grand au plus petit)
index_dernier_element = len(liste_nombres_4) - 1
# la valeur de index_dernier_element est fixe et il s'agit de 10 - 1 = 9
for nombre in liste_nombres_4:
  index_inverse = index_dernier_element - nombre
  liste_inversee.append(liste_nombres_4[index_inverse]) 

print(liste_inversee)

#for numero_iteration in range(1, 1000):
#  print(numero_iteration)

print("----- Exercice 5 : permutation -----")
liste_nombres_5 = [6901, "ABC", 0, 8007, 10, "EF"]
#                   0     1     2   3    4    5
#                 index
liste_permutee = []

# 5.a À l'aide de deux boucles "for", remplir la variable liste_permutee
# avec les valeurs de liste_nombres_5 de manière à ce que la seconde moitié de liste_nombres_5 se retrouve être la première moitié de liste_permutee

# Solution : le principe ici exposé est d'ajouter les éléments en filtrer alternativement la moitié de liste adéquate à l'aide de l'instruction "if"

# Dans cette première partie de l'algorithme on commence par n'ajouter que les éléments dont l'index (numéro de la case) est supérieur à la moitié de la taille de la liste
index = 0
index_moitie_liste = len(liste_nombres_5)/2
for nombre in liste_nombres_5:
  if index >= index_moitie_liste:
    liste_permutee.append(nombre)
  index = index + 1

# dans la seconde partie on recommence mais avec la première moité de la liste seulement
index = 0
for nombre in liste_nombres_5:
  if index < index_moitie_liste:
    liste_permutee.append(nombre)
  index = index + 1

print(liste_permutee)

print("----- Exercice 6 : voyelles & consonnes -----")
# Tout comme les listes, les chaînes de caractère sont des types indexables.
# il est donc possible d'accéder à une lettre en particulier:
texte="Mangez des pommes !"
print(texte[0], texte[5], texte[-1])
# Il est également possible de transformer une valeur textuelle en majuscules en utilisant .upper():
print("prière de ne pas crier".upper())
# Cela permet notamment lorsque l'on compare deux caractères de ne pas avoir à faire un test pour les minuscules et un test pour les majuscules.
caractere_d_exemple = "e"
if caractere_d_exemple.upper() == "E":
  print("je suis un e : ma valeur en majuscle est égale à 'E' ")

# 6.a À l'aide d'une boucle "for", de .upper() et de la possibilité d'accéder individuellement à chaque caractère, compter le nombre de voyelles présentes dans la liste suivante :
mon_texte = ["JeanLebienheureux", "EstFaitChevalier", "SurOrdreDuRoy"]
nombre_voyelles = 0 # au début, il y en a 0. Forcément on n'a pas commencé à compter !

for partie_de_texte in mon_texte:
  for caractere in partie_de_texte:
    # je teste si le caractere mis en majuscule est égale à A ou E ou I ou O ou U ou Y
    if caractere.upper() == "A" or  caractere.upper() == "E" or  caractere.upper() == "I" or  caractere.upper() == "O" or  caractere.upper() == "U" or  caractere.upper() == "Y":
      # si c'est le cas, c'est une voyelle et j'ajoute 1 à mon compteur
      nombre_voyelles = nombre_voyelles + 1
# mon algorithme est terminé, j'affiche le résultat :
print("nombre de voyelles :", nombre_voyelles)

# 6.b En utilisant la réponse à la question précédente, compter le nombre de consonnes sans utiliser de boucle

# la taille de mon texte (c'est-à-dire le nombre de caractères qui le composent) est la somme de la taille des trois parties :
taille_de_mon_texte = len(mon_texte[0]) + len(mon_texte[1]) + len(mon_texte[2])
# le nombre de consonnes est le nombre de caractères - le nombre de voyelles
nombre_consonnes = taille_de_mon_texte - nombre_voyelles
print("nombre de consonnes :", nombre_consonnes)


# ============================================
# Back to basics !
# ============================================
#
print("----- Exercice 7 : Boucles & formes géométriques -----")
#
#     Les exercices suivant vous permettront de vous entrainer à manier les boucles en Python
#     Il vous sera demandé de dessiner des formes géométriques dans le terminal à l'aide de caractères.
#     
#     Attention ! pour dessiner, par exemple, une ligne horizontale composée de 5 étoiles,
#     ne faites pas :
#     print("*****")
#     Ce serait bien trop simple... 
#     Le but ici est de manier les boucles :-). La méthode attendue devra employer le procédé indiqué ci-dessous.
#
#     Pour afficher un nombre donné d'espace avant d'afficher, par exemple, un caractère dollar $ :
#     print(" " * 1, "$")   # ceci affiche 1 espace avant d'afficher $ sur la même ligne
#     print(" " * 2, "$")   # ceci affiche 2 espaces avant d'afficher $ sur la même ligne
#     print(" " * 8, "$")  # ceci affiche 8 espaces avant d'afficher $ sur la même ligne
#     Vous l'aurez compris, en Python, multiplier une chaîne de caractère par un nombre entier permet de dupliquer sa 
#     valeur autant de fois que vous le souhaitez
#
# 7.a Affichez une ligne horizontale de longeur 10 composée du caractère $ dans votre terminal.
#
# 7.b Affichez une ligne verticale de longeur 8 composée du caractère $ dans votre terminal.
#
# 7.c Le but de cet exercice est d'afficher un carré dont les côtés sont de taille 10 dans votre terminal.
#     Un carré de taille 4 sera par exemple représenté ainsi :
#     $$$$
#     $$$$
#     $$$$
#     $$$$
#     Si cela ne vous semble pas très "carré", c'est que la hauteur du caractère est plus grande que sa largeur.
#     Cependant il y a bien 4 caractères en long comme en large : c'est bien un carré.
#
#     Indice : pour répéter 5 fois une opération, vous pouvez faire une boucle for comme ceci:
#     for element in [1,2,3,4,5]:
#       pass #ecrire l'algorithme ici

# SOLUTION :
for etage in [1,2,3,4,5,6,7,8,9,10]:
  print("$" * 10)

# 7.d Le but de cet exercice est d'afficher un triangle rectangle de hauteur 5 et de largeur 5 dans votre terminal.
#     Le triangle rectangle doit être représenté avec des caractères étoiles (*) de la manière suivante :
#     *
#     **
#     ***
#     ****
#     *****

# SOLUTION :
for etage in [1, 2, 3, 4, 5]: 
  print("*" * etage)


# 7.e Affichez un triangle isocèle non rectangle dont la base contient 7 fois le caractère $ comme ceci :
#       $
#      $$$
#     $$$$$
#    $$$$$$$   <--- 7 fois le caractère $
#    Indice : la difficulté par rapport à l'exemple précédent est de bien aligner les $ en fonction de "l'étage" 
#             sur lequel on se trouve. C'est-à-dire de calculer le nombre d'espaces avant le $.

# SOLUTION :
largeur_base = 7
#nb_etages = 5              # on aurait pu écrire : int(math.ceil(largeur_base / 2))
for etage in [0, 1, 2, 3]: # on aurait pu écrire : range(0, nb_etages - 1)
  nb_dollars = 1 + 2 * etage  # 1 au premier étage puis on en ajoute 2 à chaque fois
  nb_espaces_a_gauche = (largeur_base - nb_dollars) / 2 
  print(" " * int(nb_espaces_a_gauche) + "$" * nb_dollars)

# 7.f Affichez un rectangle creux de hauteur 4 et de largeur 9 devant être représenté comme ceci :
#    *********
#    *       *
#    *       *
#    *********
#    Indice : vous pouvez afficher plusieurs choses sur une même ligne de la manière suivante 
#    avec une seule instruction print :
#    print("****", "Mon texte est entouré par 4 étoiles à gauche et 3 à droites", "***")

# SOLUTION :
largeur = 9
hauteur = 4
for etage in [1,2,3,4]:  # [1,2,3,4] peut être écrit range(1, etage+1)
  if etage == 1 or etage == hauteur:
    print("*" * largeur) 
  else:
    print("*" + " " * (largeur - 2) + "*")


print("----- Exercice 8 : Recherche de données -----")
#    Dans cette série d'exercice, nous allons nous atteler à chercher des éléments dans des listes
#    Chercher un élément dans une liste signifie "A quel position de la liste se trouve-t-il ?"
#    
#    Prenons par exemple l'alphabet découpé de manière arbitraire :
#    alphabet = ["AB", "CD", "EF", "GHIJKLM", "NOPQRST", "UVW", "X", "Y", "Z"]
#
#    Trouver l'élément "UVW" est simple : il s'agit de vérifier une à une
#    les portions d'alphabet (càd les éléments de la liste alphabet).
#
#    position = 0
#    for portion_d_alphabet in alphabet:
#      if portion_d_alphabet == "UVW":
#        print("Trouvé ! La position est :", position)
#      position = position + 1  # je déplace mon curseur d'un cran et je passe à la suite
#
# 8.a Trouvez la position de l'élément "@" dans la liste suivante :
adresse_mail_decomposee = ["jean", "rochefort", "@", "chartes", ".", "psl", ".", "eu"]

# SOLUTION sans boucle :
#position = adresse_mail_decomposee.index("@")
#print("position de @:", position)

# SOLUTION avec boucle :
position = -1
p = 0
for partie in adresse_mail_decomposee:
  if partie == "@":
    position = p
  p = p + 1

if position == - 1:
  print("@ non trouvé !")
else:
  print("position de @ :", position)

# 8.b Trouvez les positions de tous les éléments points "." dans la liste adresse_mail_decomposee précédente et stockez
#     ces positions dans une liste. Affichez ensuite celle liste à la fin de l'algorithme.

# SOLUTION
p = 0
points = []
for partie in adresse_mail_decomposee:
  if partie == '.':
    points.append(p)
  p = p + 1

print("position des points :", points)

# 8.c Trouvez dans la liste suivante la position de tous les caractères de ponctuations :
liste_ponctuee = ["Hey!", "Rien ne sert de courir", ",", "il faut partir à point", "."]  
#  
# Indice : le premier caractère de ponctuation se trouve dans l'élément 0

# SOLUTION
ponctuation = ["!", ",", "."]
p = 0
positions = []
for partie in liste_ponctuee:
  for caractere in partie:
    if caractere in ponctuation:
      positions.append(p)
    p = p + 1

print("position des caractères de ponctuation :", positions)

# 8.d Comptez le nombre de lettres contenues dans l'ensemble des vers suivant :
vers1 = "Once upon a midnight dreary, while I pondered weak and weary,"
vers2 = "Over many a quaint and curious volume of forgotten lore"
#
# Indice : les espaces et les virgules ne sont pas des lettres

# SOLUTION :
compteur = 0
caracteres_indesirables = [" ", ","]
for vers in [vers1, vers2]:
  for caractere in vers:
    if caractere not in caracteres_indesirables:
      compteur = compteur + 1
print("nombre de lettres :", compteur)
