Hook per sincronizzare un file di testo da stckbit con l'intera directory proveniente dal local. Questo script è molto potente in quanto selettivamente recupera dal remote il file di interesse lo sovrascrive forzatamente nella locale e poi qualsiasi cambio in local sul file non viene considerato

## Mauro 1/5/24 - h. 13:11
#!/bin/bash

# Fetch latest changes from the remote repository
git fetch origin

# Pull the latest version of cheatsheet.md from the remote and overwrite local changes
git pull origin main --force

# Remove any local changes to cheatsheet.md
git checkout -- cheatsheet.md

# Continue with the rest of the script
# Add all changes to the staging area
git add .

# Commit all staged changes
git commit -m "Auto-commit before pushing changes"

# Push the commit to the remote repository
git push origin main
