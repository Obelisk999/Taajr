# Bienvenue sur le projet Taajr

Ce dépôt contient le code source du projet Taajr. Ce guide vous aidera à démarrer avec le projet et à contribuer efficacement.

## Déploiement sur Vercel

Ce projet peut être déployé sur Vercel pour un hébergement gratuit et facile. Suivez ces étapes :

### Prérequis pour le déploiement
- Un compte Vercel (gratuit) : [https://vercel.com/signup](https://vercel.com/signup)
- Git et GitHub

### Étapes de déploiement

1. **Connectez votre compte GitHub à Vercel :**
   - Allez sur [https://vercel.com](https://vercel.com)
   - Cliquez sur "Sign Up" ou "Login"
   - Connectez-vous avec votre compte GitHub

2. **Importez votre projet :**
   - Dans le dashboard Vercel, cliquez sur "Add New..." puis "Project"
   - Sélectionnez votre dépôt GitHub `Taajr`
   - Vercel détectera automatiquement la configuration grâce au fichier `vercel.json`

3. **Configurez les variables d'environnement :**
   - Dans les paramètres du projet Vercel, allez dans "Settings" > "Environment Variables"
   - Ajoutez les variables suivantes :
     - `SECRET_KEY` : Une clé secrète aléatoire pour les sessions Flask (générez-en une sécurisée)
     - `MAIL_PASSWORD` : Votre mot de passe d'application Gmail (si vous souhaitez utiliser l'email)
   - Les autres configurations email sont déjà dans le code, mais peuvent être overridées si nécessaire

4. **Déployez :**
   - Cliquez sur "Deploy"
   - Vercel construira et déploiera automatiquement votre application
   - Une fois terminé, vous recevrez une URL de production (ex: `https://taajr.vercel.app`)

5. **Déploiements automatiques :**
   - Chaque push sur la branche principale déclenchera un nouveau déploiement automatiquement
   - Les pull requests créeront des prévisualisations de déploiement

### Notes importantes pour Vercel

- **Base de données SQLite** : Sur Vercel, le système de fichiers est éphémère. Pour la production, considérez l'utilisation d'une base de données PostgreSQL ou MySQL hébergée (ex: Vercel Postgres, PlanetScale, Supabase).
- **Fichiers uploadés** : Les fichiers uploadés ne persisteront pas entre les déploiements. Utilisez un service de stockage cloud comme AWS S3, Cloudinary, ou Vercel Blob.
- **Flask-Session** : La session basée sur le système de fichiers ne fonctionnera pas sur Vercel. Utilisez une session basée sur les cookies ou Redis.

## Prérequis pour le développement local

- **Git** (assurez-vous que Git est installé sur votre système Windows. Vous pouvez le télécharger depuis [Git pour Windows](https://git-scm.com/download/win))
- **Visual Studio Code** ou un autre éditeur de code

## Installation

1. **Cloner le dépôt :**

    Ouvrez l'invite de commandes ou PowerShell et exécutez :

    ```cmd
    git clone https://github.com/haki24gamer/Taajr.git
    ```

2. **Accéder au dossier du projet :**

    ```cmd
    cd Taajr
    ```

3. **Créer et activer un environnement virtuel Python :**

    Assurez-vous d'avoir Python installé sur votre système, et l'environnement virtuel est activé.

    Pour activer l'environnement virtuel, exécutez :

    - Sur Windows :

        ```cmd
        .\venv\Scripts\activate
        ```

    - Sur macOS et Linux :

        ```bash
        source venv/bin/activate
        ```

4. **Installer les dépendances :**

    Assurez-vous d'avoir pip installé sur votre système. Ensuite, exécutez :

    ```cmd
    pip install -r requirements.txt
    ```

5. **Installer SQLite3 :**

    Si SQLite3 n'est pas déjà installé sur votre système, vous pouvez le télécharger et l'installer depuis [SQLite Download Page](https://www.sqlite.org/download.html).

## Contribution

1. **Créer une branche pour votre fonctionnalité :**

    ```cmd
    git checkout -b ma-nouvelle-fonctionnalité
    ```

2. **Effectuer vos modifications et les committer :**

    ```cmd
    git add .
    git commit -m "Ajout d'une nouvelle fonctionnalité"
    ```

3. **Pousser vos modifications :**

    ```cmd
    git push origin ma-nouvelle-fonctionnalité
    ```

4. **Ouvrir une Pull Request** sur GitHub.

## Démarrer le serveur SMTP

Pour démarrer un serveur SMTP de débogage local, exécutez la commande suivante :

```bash
python3 -m aiosmtpd -n -l localhost:1025
```

Cela démarrera un serveur SMTP sur `localhost` à l'écoute sur le port `1025`, qui imprimera les messages reçus dans la console pour le débogage.

## Support

Pour toute question, veuillez ouvrir une **issue** sur le dépôt GitHub.

## Licence

Ce projet est sous licence MIT.
