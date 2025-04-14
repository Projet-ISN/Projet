# Instructions
## À réaliser qu'une fois avant tout :
### Création d'une clé SSH
Pour créér une clé SSH **sur Linux**, vous devez :  
1. Exécutez la commande suivante dans le terminal  
```bash
ssh-keygen
```
Laissez le chemin standard et touchez Entrée pour la passephrase

2. Copiez le directoire indiqué par "Your public key has been saved in" et exécutez
```bash
cat <directoire>
```
Par exemple, `cat /home/dpinheiroc/.ssh/id_rsa`

3. Copiez ce qui est renvoyé au terminal après l'exécution

4. Allez sur Github, et cliquez sur votre photo de profil en haut à droite.

5. Cliquez sur "Settings" (https://prnt.sc/_9TWL800uCT-)

6. Cliquez sur "SSH and GPG keys" (https://prnt.sc/w8xWyH-iPnAG)

7. Cliquez sur "New SSH key"

8. Donnez un titre à la clé et coller dans le champ "Key" ce que vous avez copié dans l'étape 3

9. Cliquez sur "Add SSH key"

### Gittyup
1. Ouvrez Gittyup

2. Cliquez sur "Clone repository"

3. Collez `git@github.com:Projet-ISN/Projet.git` pour l'URL

4. Choisissez un chemin dans la machine pour cloner le projet localement

### Branch develop

1. Dans Gittyup, cliquez sur "Branch: main" (https://prnt.sc/aT3tIOjbb6-T)

2. Selectionnez l'onglet "Remotes"

3. Cliquez droit sur "origin/develop"

4. Cliquez sur "New Local Branch"

5. Revenez à l'onglet "Branches"

6. Cliquez deux fois sur "develop"

## À faire à chaque fois :

> N'oubliez pas de faire pull avant de modifier le code. Cela peut causer des conflits et perte d'une partie du code fait.

> N'oubliez pas de faire commit & push après avoir modifié le code. Si quelqu'un d'autre fait pull et que votre commit n'a pas été "pushed", son code sera dans une version plus ancienne et vos modifications ne seront pas prises en compte.

### Gittyup
1. Ouvrez Gittyup

2. Cliquez sur "Open Repository"

3. Trouvez le chemin où vous avez cloné le projet

### Pull, commit et push
1. Cliquez sur "Pull", la flèche vers la gauche en haut à gauche. Cela mettra à jour la code dans votre machine locale depuis le code en Github.

Quand vous modifiez le code du projet : (https://prnt.sc/hw-LHEy5n4K0)

1. Cliquez sur "Uncommited changes"

2. Expliquez les modifications dans le champ "Commit Message"

3. Cliquez sur "Stage All"

4. Cliquez sur "Commit"

5. Cliquez sur "Push", la flèche vers la droite en haut à gauche. Cela mettra à jour le code sur Github depuis votre machine locale