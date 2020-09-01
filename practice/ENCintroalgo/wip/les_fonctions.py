
print("============================================")
print("  Exemples simples")
print("============================================")

def fonction_absolument_inutile():
  """
  je ne fais rien de particulier
  """
  return

print("appel de fonction_absolument_inutile :")
fonction_absolument_inutile()

def afficher_expression(expression1, expression2):
  """
  expression: une chaîne de caractères à afficher
  algorithme: j'affiche l'expression sans la modifier
  valeur de retour: rien du tout 
  """
  print(expression1)
  print(expression2)
  return

print("appel de afficher_expression :")
expression_a_afficher = "Je suis une expression intacte."
afficher_expression(10, 12)

# fonction qui affiche une expression en majuscules
def afficher_expression_majuscules(expression):
  """
  j'affiche l'expression en majuscules
  """
  print(expression.upper())
  return

print("appel de afficher_expression_majuscules :")
afficher_expression_majuscules("Je suis une expression intacte.")


# fonction qui affiche  une expression N fois
def repeter_expression(expression, n):
  """
  fonction qui affiche  une expression N fois
  """
  print(n * expression)
  return

print("appel de repeter_expression :")
repeter_expression("Boumbo ", 3)

def retourner_expression_repetee(expression, n):
  """
  fonction qui répète une expression N fois
  """
  expression_repetee = n * expression
  return expression_repetee

#boumbo = retourner_expression_repetee("Boumbo", 10)
#print(boumbo)

def afficher_trois_fois(expression):
  expression_repetee_trois_fois = retourner_expression_repetee(expression, 3)
  print(expression_repetee_trois_fois)
  return

#afficher_trois_fois("AEIOU_")

def afficher_neuf_fois(expression):
  expression_3x = retourner_expression_repetee(expression, 3)
  expression_9x = retourner_expression_repetee(expression_3x, 3)
  print(expression_9x)
  return

#afficher_neuf_fois("XYZ_")


print("============================================")
print("  Exemples de fonction avec valeur de retour")
print("============================================")


def ajouter_deux(nombre):
  """
  nombre: un nombre entier
  algorithme: fonction qui retourne la valeur de nombre + 2
  valeur de retour: nombre  + 2
  """
  nouveau_nombre = nombre + 2
  return nouveau_nombre

print("appel de ajouter_deux :", ajouter_deux(10))

def ajouter_quatre(nombre):
  """
  fonction qui retourne la valeur de nombre + 4
  """
  nouveau_nombre = ajouter_deux(nombre)
  nouveau_nombre = ajouter_deux(nouveau_nombre)
  return nouveau_nombre

print("appel de ajouter_quatre :", ajouter_quatre(10))


def ajouter_cent(nombre):
  """
  fonction qui retourne la valeur de nombre + 100
  """
  nouveau_nombre = nombre
  for etape in range(50):
    nouveau_nombre = ajouter_deux(nouveau_nombre)
  return nouveau_nombre

print("appel de ajouter_cent :", ajouter_cent(999))


def ajouter_n(nombre, n):
  """
  fonction qui retourne la valeur de nombre + n
  Cette fonction est moins rigide que les précédentes car on
  peut spécifier le nombre à ajouter en second paramètre !
  """
  return nombre + n

#ajouter_n(12, 12)
resultat_de_la_fonction = ajouter_n(999, 100)
print("appel de ajouter_n avec n=100 :", resultat_de_la_fonction)
print("appel de ajouter_n avec n=-500 :", ajouter_n(999, -500))
print("appel de ajouter_n avec n=123456 :", ajouter_n(999, 123456))


def dessiner_un_rectangle(largeur, hauteur):
   # ici est défini l’algorithme de dessin
   for y in range(0, hauteur):
    print("*" * largeur)
   # voilà, le rectangle est dessiné à l’écran;
   # je n’ai pas de résultat spécifique à donner à l’utilisateur
   return

print("appel de dessiner_un_rectangle :")
dessiner_un_rectangle(3, 2)


def saluer_utilisateurs(utilisateur1, utilisateur2, langue):
  if langue == "fr":
    formule_salutation = "Bonjour"
  else:
    formule_salutation = "Hello"
  print(formule_salutation, utilisateur1, ",", utilisateur2)

print("appel de saluer_utilisateurs :")
saluer_utilisateurs("Alice", "Bob", "fr")
saluer_utilisateurs("Alice", "Bob", "cz")



print("----- Exercice 9 -----")

# 9.a Écrire une fonction qui renvoie le double d'un nombre passé en paramètre
# 9.a.bis Écrire une fonction qui renvoie le produit de deux nombres passés en paramètres
# 9.a.ter Écrire une fonction est_pair qui renvoie True si un nombre passé en paramètre est pair et 
#         False dans le cas contraire

# 9.b Écrire une fonction qui affiche tous les éléments d'une liste passée en paramètre façon "liste à puce" avec une étoile :
#  exemple :  afficher_liste_a_puces(["Patrick", "Jackie", "Corbier"])
#  * Patrick
#  * Jackie
#  * Corbier

# 9.c Écrire une fonction similaire à la précédente mais qui permet de changer, grâce à un paramètre, le caractère utilisé comme puce

# 9.d Écrire une fonction qui renvoie le nombre de voyelles dans un mot passé en paramètres

# 9.e Écrire une fonction qui utilise la fonction précédement écrite et qui renvoie le nombre de consonnes dans un mot passé en paramètres

# 9.f Écrire une fonction qui affiche à l'écran une expression passée en paramètre mise entre balises HTML. Le nom de la balise sera également passé en paramètre de la fonction.
# exemples : 
# afficher_html("ceci est un paragraphe", "p")
# <p>ceci est un paragraphe</p>
# afficher_html("ceci est une division", "div")
# <div>ceci est un paragraphe</div>

# 9.f En utilisant la fonction précédente, écrire une fonction qui écrit en HTML le contenu d'une liste Python
# exemple :
# afficher_liste_html(["oeuf", "salade", "crouton"])
# <ul><li>oeuf</li><li>salade</li><li>crouton</li></ul>