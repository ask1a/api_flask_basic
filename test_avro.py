import fastavro

# Définition des personnages
characters = [
    {
        "id": 1,
        "name": "Martin Riggs"
    },
    {
        "id": 2,
        "name": "John Wick"
    },
    {
        "id": 3,
        "name": "Ripley"
    }

]

# Définition du schéma des données
schema = {
    "type": "record",
    "namespace": "com.badassmoviecharacters",
    "name": "Character",
    "doc": "Seriously badass characters",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "id", "type": "int"}
    ]
}

# Ouverture d'un fichier binaire en mode écriture
with open("characters.avro", 'wb') as avro_file:
    # Ecriture des données
    fastavro.writer(avro_file, schema, characters)
