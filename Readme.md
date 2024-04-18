## MongoDB Replica Set

## 1. Configuration de MongoDB en Mode Replica Set

    Utilisez Docker pour créer un environnement MongoDB Replica Set. Voici un exemple de configuration de docker-compose.yml 

    Assurez-vous que le Replica Set fonctionne correctement en exécutant les commandes suivantes dans votre terminal :

        ```shell
        docker compose up -d
        ```
    
    Après avoir démarré les services MongoDB avec Docker, vous pouvez initialiser le Replica Set en exécutant la commande suivante dans votre terminal :

        ```shell
        docker exec -it mongo1 mongosh --eval "rs.initiate({

            _id: 'myReplicaSet',
            members: [
                {_id: 0, host: 'mongo1'},
                {_id: 1, host: 'mongo2'},
                {_id: 2, host: 'mongo3'}
            ]
        })"
        ```
    Assurez-vous d'exécuter cette commande après avoir démarré les conteneurs MongoDB.

    Cette commande initialise le Replica Set avec le nom "myReplicaSet" et définit trois membres : "mongo1", "mongo2" et "mongo3".



## 2. Génération de Fausses Données

    Par la suite, nous allons générer les fausses données utilisateurs et les stocker dans un fichier users.json avec la structure de données suivantes.

        ```shell
        {
        _id: new ObjectId('661d0f6a9eac75371bab12d1'),
        name: 'Entrer_un_nom',
        age: Entrer_un_age,
        email: 'Entrer_un_email',
        createAt: 'Entrer_une_date_de_création'
        }
        ```
    
    Pour le suite, j'utiliserai Faker pour générer les donnée d'utilisateur

    Maintenant nous allons créer un fichier importmongo.sh qui va nous premettre de créer un fichier user.json avec plusieur donnée d'utilister.
    Vous écrirez les lignes de commande suivante:

        ```shell
        #!/bin/bash

        current_position=$(pwd)
        docker exec -i mongo1 mongoimport --db rs --collection usersCollection --drop --jsonArray < "$current_position/users.json" 
        ```
    
    dans mon cas, j'appellerai ma base de donnée "rs", ma colléction d'utilisateur "usersCollection" le fichier json qui stockera les donnée s'appelera user (je ne lui est pas donnée d'adresse de fichier spécifique, mais cela ne vous empéchera ps dele faire celon votre organistion).

    pour finire pour pouvoir importer les données qui ont été crée nous allon sutilisé cette commande:
        
        ```shell
        ./importmongo.sh
        ```
    
    La commande aure marché si votre terminale affiche ceci:

        ```shell
        connected to: mongodb://localhost/
        dropping: nosql.usersCollection
        100 document(s) imported successfully. 0 document(s) failed to import.
        ```

## 3. Manipulations via la CLI MongoDB

    Atention pour cette exo d'ouvrire un terminal en docker

    Pour commencer, il va falloir accéder au Cli de MongoDB et pour cela nous allons exécuter la commande suivante.

        ```shell
        docker exec -i mongo1 mongoimport --db rs --collection usersCollection --drop --jsonArray < "$current_position/users.json"

        use sr
        ```

    Veillez à adapté le nom de votre base de donnée ainsi que de votre collection et le fichier json selon ce que vous avez mit.

    Maintenant je vais réaliser un ecommande pour insérer une nouvelle donnée précise avec la command insertOne 

        ```shell
        db.usersCollection.insertOne({"name": "Guillaume Pham"})
        ```
    
    Voici le résultat attendu:

        ```shell
        {
        acknowledged: true,
        insertedId: ObjectId('662175a4047e679b5ec934df')
        }
        ```

    Maintenant nous allont afficher les données des utilisateurs qui ont plus de 30 ans, pour cela nous allons faire un file en rajoutant la condition "age" > 30 (> est représenté pas "$gt"):

        ```shell
        db.usersCollection.find({"age":{$gt:30}})
        ```

    Vous devrez normalement voir une liste de donnée d'utilisateur dont l'age dépasse 30.

    Maintenant nous allons entrer un ecommande pour ajouter 5 aux ages de tout les utilisateurs, c'est donc un update que nous allons réaliser et l'action ajouter sera représenter par la commande $inc:

        ```shell
        db.usersCollection.updateMany({}, { $inc: { age: 5 } });
        ```
    
    Vous pourrez vérifiez le résultat en faisant un find de toute votre db.

    Enfin nous allons utiliser la commande deleteOne pour suprimer un utilisateur:


        ```shell
        db.usersCollection.deleteOne({ "name": "Guillaume Pham" })
        ```
    
    Voici le résultat attendu:

        ```shell
        { acknowledged: true, deletedCount: 0 }
        ```
    
    Vous pouvez toujours faire un find de l'utilisateur que vous avez suprimé pour être sur que la commande à bien marché

## 4. Automatisation avec le Langage de Programmation de votre Choix

    Pour finire je vais automatiser toute les commande présenté dans la partie précédante en les codants.
    Vous pouvez utilisé le language de votre choix mais cette documentation ne vous montrera uniquement comment la réaliser en python.
    Vous trouverez mon code documenter dans le fichier Program.py