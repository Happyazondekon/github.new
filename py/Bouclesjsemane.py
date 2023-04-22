semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
print("Jours de la semaine:")
for jour in semaine[:5]:
    print(jour)
print("Jours du week-end:")
i = 5
while i < len(semaine):
    print(semaine[i])
    i += 1
