# ===================================
#  3 Conditions
# ===================================

# -----------------------------------
# Variables définies pour le reste de l'exercice :
# Ouvrage A
titre_A = 'A'
tradition_A = 'Copie'
temoin_A = 'Copie. Bibl. nat., Dupuy 350. fol. 57.'
institution_A = 'Paris, Bibl. nat. Fr.'
nb_pages_A = 234

# Ouvrage B
titre_B = 'B'
tradition_B = 'Original'
temoin_B = 'Aut. Bibl. nat., Fonds français, n° 3387, f° 5.'
institution_B = 'Turin, Archivio di Stato'
nb_pages_B = 100

# Ouvrage C
titre_C = 'C'
tradition_C = 'Original'
temoin_C = 'Aut. Bibl. nat., Fonds français, n° 3387, f° 5.'
institution_C = 'Inconnue'
nb_pages_C = 51
# -----------------------------------


print('\n--------- exo 3.1 ---------')
# 3.1 exo : pour chaque ouvrage, afficher "l'ouvrage {titre} est conservé à Turin" si son institution est "Turin". Sinon, ne rien faire.


print('\n--------- exo 3.2 ---------')
# 3.2 exo : pour chaque ouvrage, tester si sa tradition est différente de 'Copie'. Si oui, afficher son titre et son instution de conservation, sinon, afficher afficher le titre de l'ouvrage, son instution de conservation et sa tradition.


print('\n--------- exo 3.3 ---------')
# 3.3 exo : tester si le nombre total de pages (tout ouvrage confondu) est supérieur à 300
# Si oui, afficher le nombre de pages excedentaires
# S'il est inférieur à 300 afficher le nombre de pages manquantes pour atteindre ce chiffre
# Sinon, afficher 300


print('\n--------- exo 3.4 ---------')
# 3.4 exo : Avec une seule expression 'if', tester si parmi les ouvrages il existe au moins une 'Copie'


print('\n--------- exo 3.5 ---------')
# 3.5 exo : Seuls les ouvrages de Paris et de Turin sont disponibles à la consultation. Pour chaque ouvrage,
# * S'il est conservé à Paris, Bibl. nat. Fr. OU à Turin, Archivio di Stato, afficher toutes les informations dont vous disposez.
# * Sinon, afficher le message 'Ouvrage {titre} non disponible'


print('\n--------- exo 3.6 ---------')
# 3.6 exo : Pour chaque ouvrage, tester si la tradition est 'Original'. 
# * Si tel est le cas, tester si le nombre de page est supérieur ou égal à 100
#    * Si tel est le cas, afficher le témoin. Sinon, afficher le message "L'ouvrage comporte moins de 100 pages"
# * Si la tradition n'est pas 'Original', afficher le message "L'ouvrage XXX n'est pas un original"


print('\n--------- exo 3.7 ---------')
# 3.7 exo : tester si la tradition de l'ouvrage C est 'Original' ET s'il possède plus de 100 pages. Afficher l'institution de conservation le cas échéant, afficher un message à caractère informatif pour l'utilisateur dans le cas contraire.


print('\n--------- exo 3.8 ---------')
# 3.8 exo : tester si parmi les ouvrages il existe au moins un ouvrage de plus de 10 pages dont l'insitution est 'Inconnue'


print('\n--------- exo 3.9 ---------')
# 3.9 exo : pour chaque ouvrage, tester si le nombre de pages est inférieur à 200 et si l'institution n'est pas 'Inconnue'. Afficher un message pertinent si l'une des deux conditions n'est pas remplie.


print('\n--------- exo 3.10 ---------')
# 3.10 exo : afficher le témoin des ouvrages respectant AU MOINS une des contraintes suivantes :
#   * plus de 50 pages mais de moins de 100 pages
#   * l'institution est 'Inconnue'
