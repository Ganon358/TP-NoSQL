from faker import Faker
import json
from datetime import datetime

# Initialisation de Faker
fake = Faker()

# Fonction pour générer un utilisateur aléatoire
def generate_user():
    user = {
        "name": fake.name(),
        "age": fake.random_int(min=18, max=80),
        "email": fake.email(),
        "createdAt": fake.date_time_this_decade().isoformat()
    }
    return user

# Génération de 100 utilisateurs
users = [generate_user() for _ in range(100)]

# Écriture des données dans un fichier JSON
with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)

print("Données des utilisateurs générées avec succès.")
