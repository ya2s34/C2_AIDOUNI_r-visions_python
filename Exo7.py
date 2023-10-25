# Exo7
fichier = open("test.txt", "r")
lecture = fichier.readline()
mots = lecture.split()
nombre = len(mots)
print("le nombre de mot du fichier txt est : " , nombre)

str_mots = str(nombre)

result_fich = open("result.txt", "a")

result_fich.write("le nombre de mots dans le fichier est" + str_mots)
