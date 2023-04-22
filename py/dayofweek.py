Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> jours_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
>>> jours_de_semaine = jours_de_la_semaine[:5]
>>> jours_weekend = jours_de_la_semaine[5:]
>>> jours_de_semaine = jours_de_la_semaine[:-2]
>>> jours_weekend = jours_de_la_semaine[-2:]
>>> dernier_jour = jours_de_la_semaine[-1]
>>> dernier_jour_2 = jours_de_la_semaine.pop()
