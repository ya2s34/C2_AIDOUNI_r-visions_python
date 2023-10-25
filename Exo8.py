# Exo8
dico = {
    "yass" : 19,
    "kev" : 12,
    "alex" : 14,
    "marine" : 17,
    "jf" : 15,
}

max_note_eleve = max(
    dico, key=lambda eleve : dico[eleve]
)
print(max_note_eleve)

