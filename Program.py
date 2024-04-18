#Utilisez pymongo pour pouvoir réalisé les commande pour MongoClient
from pymongo import MongoClient

# Connexion à la base de données MongoDB
#vous trouverez votre MongoClient en entrant la commande dans votre terminal en bash: docker exec -it  mongo1 mongosh
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.4')
db = client.rs
users_collection = db.usersCollection

# Fonction pour insérer des données dans la collection users
def insert_data():
    data = [
        {
            "name": "UtilisateurTest",
            "age": 25,
            "email": "user1@example.com",
            "createdAt": "2023-01-01T00:00:00Z"
        },
        {
            "name": "UtilisateurTest2",
            "age": 55,
            "email": "user2@example.com",
            "createdAt": "2020-01-01T00:00:00Z"
        },
    ]
    users_collection.insert_many(data)
    print("Données insérées avec succès.")
    print(data)

# Fonction pour lire et afficher tous les utilisateurs de plus de 30 ans
def find_users_over_30():
    users = users_collection.find({"age": {"$gt": 30}})
    print("Utilisateurs de plus de 30 ans :")
    for user in users:
        print(user)

# Fonction pour mettre à jour l'âge de tous les utilisateurs en ajoutant 5 ans
def update_users_age():
    users_collection.update_many({}, {"$inc": {"age": 5}})
    print("Âge de tous les utilisateurs mis à jour avec succès.")

# Fonction pour supprimer un utilisateur spécifique
def delete_user(email):
    users_collection.delete_one({"email": email})
    print("Utilisateur supprimé avec succès.")

# Exécution des fonctions
insert_data()
#find_users_over_30()
update_users_age()
delete_user("user2@example.com")
