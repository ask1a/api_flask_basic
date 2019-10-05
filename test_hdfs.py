import hdfs
client = hdfs.InsecureClient("http://127.0.0.1:50070")

# Affichage des données à la racine
# l'appel à "list()" renvoie une liste de noms de fichiers et de
# répertoires
client.list("/")

with client.write("/pouac.txt", overwrite=True) as writer:
     # notez que l'appel à "write()" prend en arguments un bytes et non un str
    writer.write(b"plonk")

# Lecture d'un fichier complet
with client.read("/pouac.txt") as reader:
    print(reader.read())

# Lecture d'un fichier complet
with client.read("/pouac.txt") as reader:
    for line in reader:
        print(line)

