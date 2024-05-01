[toc]


# MARKUP HINTS
By Mauro
I have my README.md inside my project. Here are a method to work with your README.md separately while working on your vsc local project: Use an external Markdown editor like 

[Typora]: (https://typora.io/#feature)

** (a minimal markdown editor and reader) **. These editors provide a live preview feature by default. 

# BASH

- trovare la oporta occupata:
  - `lsof -i :8000`
  
- chiudere la porta occupata forzatamente:
  - `kill -9 32394(esempio)`
  
- vedere i comandi che iniziano per una determinata strina effettuati in precedenza:
  -  `history | grep "kill (esempio)"`

- trovare la porta occupata:
  - `lsof -i :8000`
  
- chiudere la porta occupata forzatamente:
  - `kill -9 32394(esempio)`
  
- vedere i comandi che iniziano per una determinata strina effettuati in precedenza:
  -  `history | grep "kill (esempio)"`
  
- Azione Bash - Quello che segue è uno script molto importante che permette nell'ordine di 1) verificare se la porta 8000 (che viene utilizzata normalmente in fase di sviluppo) è occupata ed eventualmente chiuderla; 2) aprire Django 3) aprire hugo. Al momento sono presenti due file separati per una migliore comprensione:
```bash
- check_ports.sh

  \#!/bin/bash

  \# Check if any process is listening on port 8000

  if lsof -i :8000 >/dev/null 2>&1; then

  ​    echo "Port 8000 is in use."

  ​    \# Get the PID of the process using port 8000

  ​    pid=$(lsof -ti :8000)

  ​    \# Kill the process

  ​    echo "Killing process with PID $pid"

  ​    kill -9 "$pid"

  ​    echo "Process killed."

  else

  ​    echo "Port 8000 is not in use."

  fi
```






- ```bash
  run_project.sh
  #!/bin/bash
  
  # Navigate to the Django project directory and run the server
  # cd /progetto_api
  python3 manage.py runserver &
  
  # Navigate to the Hugo project directory and run the server
  cd ./sgb_start/
  hugo server -D
  

Per cui lo script generare **APRIRE I DUE PROGRAMMI**  DJANGO E HUGO è il seguente (ADA PERFEZIONARE!!):

```bash
#!/bin/bash

# Check if any process is listening on port 8000
if lsof -i :8000 >/dev/null 2>&1; then
    echo "Port 8000 is in use."

    # Get the PID of the process using port 8000
    pid=$(lsof -ti :8000)

    # Kill the process
    echo "Killing process with PID $pid"
    kill -9 "$pid"

    echo "Process killed."
else
    echo "Port 8000 is not in use."
fi


# Navigate to the Django project directory and run the server
# cd /progetto_api
python3 manage.py runserver &

# Navigate to the Hugo project directory and run the server
cd ./sgb_start/
hugo server -D
```

Mentre il codice per chiudere i due programmi DJANGO e HUGO è il seguente (da perfezionare)!!!:

```bash
# Find Django PID and send SIGTERM signal
django_pid=$(pidof python) && kill "$django_pid" && echo "Django process terminated"

# Find Hugo PID and send SIGTERM signal
hugo_pid=$(pidof hugo) && kill "$hugo_pid" && echo "Hugo process terminated"
ps aux | grep "python manage.py runserver"; reset


```







# GIT & GITHUB

Riferimenti [Mastering MarkDown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
### Ricordarsi di aggiungere .gitgnore
**- git add .gitignore**
**- git commit -m "Add .gitignore to exclude compiled Python files"**
### Per effettuare il push da origine a remoto 
**- git push origin implementazione-pagina**
### Switch to the New Branch:
**- git checkout new-branch-name**

### Creare una nuova branch e posizionarsi sulla stessa
- git checkout -b new-branch-name *(Il comando può essere visto come la sintesi dei due seguenti comandi:)*

**- git branch new-branch-name  # Create a new branch**
**- git checkout new-branch-name  # Switch to the new branch**

## You've created a new branch (template-tutorial) without committing changes on your existing branch (implementazione-pagina) ##

To address this, you'll need to follow these steps to commit your changes on the implementazione-pagina branch and then switch back to the template-tutorial branch. Here's a step-by-step guide:

- Commit Changes on implementazione-pagina:
Assuming you are currently on the template-tutorial branch, ** switch back to the implementazione-pagina branch:**

`git checkout implementazione-pagina`

Now, add and commit your changes:

`git add .`
`git commit -m "Your commit message here"`

- **Push Changes to Remote (implementazione-pagina):**
Assuming the remote branch is named implementazione-pagina:

`git push origin implementazione-pagina`

- ** Switch Back to template-tutorial:**
Now, switch back to the template-tutorial branch:

`git checkout template-tutorial`


**If you haven't pushed the template-tutorial branch yet, you can push it to the remote repository when you're ready:**

`git push origin template-tutorial`

**How can see from my vsc local if a git branch is present also in the remote github?**

`git fetch --all
git branch -a
`
This fetches all branches from the remote repository and lists both local and remote branches. Remote branches are prefixed with "remotes/origin/". Check if your branch is listed among the remotes.

**Come posso creare una nuova branch in local, e poi crearla anche in Github, poi effettuare il push e rendere questa branch principale?**

Create a new branch locally and switch to it (chimiamo la nuova branch template-tutorial):
`git checkout -b template-tutorial`

Push the new branch to GitHub:

`git push origin template-tutorial`

Set the upstream for the new branch:

`git branch --set-upstream-to=origin/template-tutorial template-tutorial`![alt]( '{"class": "", "title": ""}')

Now, further pushes can be simplified to:

`git push`

To revert the changes and go back to the original commit before the changes, you can use the following commands:
`git reset --hard HEAD
git clean -fd`


The first command (git reset --hard HEAD) resets your branch to the latest commit, discarding changes. The second command (git clean -fd) removes untracked files and directories. Use them with caution, as they are not reversible.

-fd stands for what?
In the context of the git clean command:

-f stands for force.
-d stands for directory.
Together, -fd means force removal of untracked directories. This option is used to remove untracked files and directories forcefully.

## delete a local branch and also delete it on the remote repository on GitHub 

Delete the local branch:

`git branch -d branch_name`![alt]( '{"class": "", "title": ""}')

Replace branch_name with the name of the branch you want to delete.

If the branch contains unmerged changes, you might need to force delete it:

`git branch -D branch_name`

Delete the remote branch:

`git push origin --delete branch_name`

This will delete the branch on the remote repository (GitHub).

Update your local repository to reflect the changes on the remote:

`git fetch --prune`

The --prune flag removes any remote tracking branches that no longer exist on the remote.

## I want to synch another an oldest branch named "template-tutorial" with a newest branch named template-sheetlike and after delete this last one (template-sheetlike)

Switch to the template-tutorial branch:
`git switch template-tutorial`

Rebase template-sheetlike onto template-tutorial:
`git rebase template-sheetlike`

Push the changes to the remote repository:
`git push origin template-tutorial --force`
Note: Force-pushing after a rebase rewrites the commit history. Use it with caution, especially if the branch has already been shared with others

Delete the template-sheetlike branch:
`git branch -d template-sheetlike`
`git push origin --delete template-sheetlike`



## Automate the copy of a file from a repo to another when pushing the commit 

So let's say that i have cheatsheet.md that i update regularly as it would be a wiki page. This file with the same name is present on different local repo. Let's say that i am working into my local repo named /home/mauro/Scrivania/dJANGO_apI/progetto_api/cheatsheet.md.md. When I do a commit adn after a push into github repo https://github.com/progettazionemauro/django-api I want automatically copy this file and update the commit also into my https://github.com/progettazionemauro/wiki-wag How can do that automatically?



To automatically copy and update the `cheatsheet.md` file in another GitHub repository whenever you push changes to the first repository, you can use GitHub Actions. GitHub Actions allows you to define workflows that run in response to various events, such as pushing to a repository. Here's a simple example:

## Theory

1. ### **Create a GitHub Actions Workflow:**

   In your Django API repository (`https://github.com/progettazionemauro/django-api`), create a directory named `.github/workflows` if it doesn't already exist.

   Inside this directory, create a file named, for example, `sync_cheatsheet.yml` with the following content:

   ```
   name: Sync Cheatsheet
   
   on:
     push:
       branches:
         - main
   
   jobs:
     sync:
       runs-on: ubuntu-latest
   
       steps:
       - name: Checkout repository
         uses: actions/checkout@v2
   
       - name: Copy cheatsheet to other repository
         run: |
           cp cheatsheet.md /path/to/wiki-wag-repo
           cd /path/to/wiki-wag-repo
           git config user.email "your-email@example.com"
           git config user.name "Your Name"
           git add cheatsheet.md
           git commit -m "Sync cheatsheet from django-api repository"
           git push origin main
   ```

   Replace `/path/to/wiki-wag-repo` with the actual path to your local `wiki-wag` repository.

2. **Commit and Push Workflow:**

   Commit the changes and push them to your Django API repository:

   ```bash
   git add .github/workflows/sync_cheatsheet.yml
   git commit -m "Add sync cheatsheet workflow"
   git push origin main
   ```

3. **Run the Workflow:**

   The workflow will run automatically when you push changes to the `main` branch. It will copy the `cheatsheet.md` file to the specified path in the `wiki-wag` repository and commit the changes there.

Make sure to replace the placeholder values in the workflow file (`your-email@example.com`, `Your Name`, and `/path/to/wiki-wag-repo`) with your actual email, name, and the path to the `wiki-wag` repository.



Here are step-by-step instructions to set up the GitHub Actions workflow for syncing the `cheatsheet.md` file from the Django API repository to the `wiki-wag` repository:

#### Step 1: Create the Workflow File

1. Open your Django API repository in your code editor or on GitHub.

2. Inside the `.github/workflows` directory (create it if it doesn't exist), create a new file named, for example, `sync_cheatsheet.yml`.

3. Copy and paste the following content into `sync_cheatsheet.yml`:

   ```
   yamlCopy codename: Sync Cheatsheet
   
   on:
     push:
       branches:
         - main
   
   jobs:
     sync:
       runs-on: ubuntu-latest
   
       steps:
       - name: Checkout repository
         uses: actions/checkout@v2
   
       - name: Copy cheatsheet to other repository
         run: |
           cp cheatsheet.md /path/to/wiki-wag-repo
           cd /path/to/wiki-wag-repo
           git config user.email "your-email@example.com"
           git config user.name "Your Name"
           git add cheatsheet.md
           git commit -m "Sync cheatsheet from django-api repository"
           git push origin main
   ```

   Replace `/path/to/wiki-wag-repo`, `"your-email@example.com"`, and `"Your Name"` with the actual path to your local `wiki-wag` repository, your email, and your GitHub username.

#### Step 2: Commit and Push Workflow File

1. In your terminal, navigate to the Django API repository.

2. Run the following commands to stage, commit, and push the workflow file:

   ```
   bashCopy codegit add .github/workflows/sync_cheatsheet.yml
   git commit -m "Add sync cheatsheet workflow"
   git push origin main
   ```

#### Step 3: Run the Workflow

1. Visit the Actions tab on your GitHub repository to see the status of your workflow. You should see the "Sync Cheatsheet" workflow running or completed.

#### Step 4: Verify Changes in the `wiki-wag` Repository

1. After the workflow completes, check your `wiki-wag` repository for the synced changes to the `cheatsheet.md` file.

   If there are any issues or changes are not reflected as expected, review the GitHub Actions logs for the workflow to identify potential errors.

That's it! You've set up a GitHub Actions workflow to automatically sync the `cheatsheet.md` file from the Django API repository to the `wiki-wag` repository on each push to the `main` branch.



##### Break down the content of the GitHub Actions workflow file step by step:

```yaml
name: Sync Cheatsheet
```

- This line sets the name of the GitHub Actions workflow to "Sync Cheatsheet."

```yaml
  push:
    branches:
      - main
```

- This section specifies the trigger for the workflow. The workflow will be triggered on each push to the `main` branch.

```yaml
  sync:
    runs-on: ubuntu-latest
```

- Here, we define a job named "sync" that will run on the latest version of the Ubuntu operating system.

```yaml
steps:
    - name: Checkout repository
      uses: actions/checkout@v2
```

- This step checks out the code from the repository, allowing subsequent steps to operate on the repository's contents.
- `uses: actions/checkout@v2`: This part specifies the action that will be used for this step. In GitHub Actions, an action is a reusable unit of code. The `actions/checkout` action is provided by GitHub and is commonly used to check out the source code of the repository.
  - `@v2`: This refers to the version of the `actions/checkout` action to use. In this case, it's version 2 of the action. The `@v2` is a version tag that indicates a specific release or version of the action. Using a version tag ensures that the workflow is using a stable and known version of the action, making it less prone to unexpected changes.

```yaml
- name: Copy cheatsheet to other repository
      run: |
        cp cheatsheet.md /path/to/wiki-wag-repo
        cd /path/to/wiki-wag-repo
```

- In this step, the `cheatsheet.md` file is copied from the current repository to the specified path (`/path/to/wiki-wag-repo`). The subsequent commands are executed within the `wiki-wag` repository.

```yaml
git config user.email "your-email@example.com"
        git config user.name "Your Name"
```

- These commands set the global Git configuration for the user's email and name in the `wiki-wag` repository.

```bash
        git add cheatsheet.md
```

- This command stages the changes to the `cheatsheet.md` file for the next commit.

```bash
        git commit -m "Sync cheatsheet from django-api repository"
```

- This command creates a new commit with a commit message indicating that the `cheatsheet.md` file is being synced from the `django-api` repository.

```bash
        git push origin main
```

- Finally, this command pushes the changes to the remote repository (`origin`) on the `main` branch.

  ## Real Case: If I have another branch othe then main in repo2 I can do it:

  ```yaml
  name: Sync Cheatsheet 
  on:  
  	push:    
  		branches:      
  			- main 
  jobs:  
  	sync:    
  		runs-on: ubuntu-latest     
  		steps:    
  		- name: Checkout repository      
  		uses: actions/checkout@v2      
  		with:        
  		ref: opzione-pagina  # Specify the branch you want to sync
  ```

  

### Summary

The GitHub Actions workflow automates the process of syncing the `cheatsheet.md` file from the `django-api` repository to the `wiki-wag` repository. It does so by copying the file, committing the changes, and pushing the commit to the `main` branch of the `wiki-wag` repository whenever changes are pushed to the `main` branch of the `django-api` repository.

### Some useful notes 

Merge:
Creates Merge Commits: When you merge one branch into another, Git creates a new merge commit that has two parent commits: **one from the branch you're merging and another from the branch you're merging into.
This results in a non-linear history with multiple branches merging into each other**
Preserves Original History:

The original commits from both branches remain unchanged. This approach keeps a clear record of when changes were made on each branch.

Rebase:
Linearizes History:

Rebase is used to linearize the commit history. It moves or combines a sequence of commits to a new base commit.
When you rebase one branch onto another, it effectively transplants the entire branch onto the tip of the other branch, creating a linear history.
No Merge Commits:

Unlike merge, rebase doesn't create additional merge commits.
It can result in a cleaner, more linear history.
When to Choose Each Approach:
Merge:

Use merge when you want to preserve the original commit history, especially when collaborating with others.
Good for feature branches and when you want to maintain a clear record of branch integration points.
Rebase:

Use rebase when you want a clean, linear history and don't mind rewriting commits.
Useful for feature branches before merging into a shared branch to avoid unnecessary merge commits.
Switch vs. Checkout:
git switch is a more modern and user-friendly command introduced in recent versions of Git. It is designed specifically for branch switching. If you're using a version of Git that supports git switch, you can replace git checkout with git switch:

Switching Branch:
git switch template-tutorial
Both commands essentially do the same thing in this context, but git switch provides a clearer and more explicit syntax for branch-related operations. If your Git version supports it, feel free to use git switch instead of git checkout.

## GIT CHEATSHEET

git command to see the last 3 commit with oneline : 

```bash
git log --oneline -n 3
```
## HOOKS
### Hook per sincronizzare un file di testo da stckbit con l'intera directory proveniente dal local

   ```bash
#!/bin/bash

  

# Path to the cheatsheet.md file

CHEATSHEET_FILE="./cheatsheet.md.md"

  

# Function to check if a file has been modified

file_modified() {

git  diff  --quiet  "$1"  ||  return  1

}

  

# Add all changes to the staging area

git  add  .

  

# Commit all staged changes

git  commit  -m  "Auto-commit before pulling latest version of cheatsheet.md"

  

# Push the commit to the remote repository

git  push  origin  main

  

# Check if cheatsheet.md has been modified

if  !  file_modified  "$CHEATSHEET_FILE"; then

# Pull the latest version of cheatsheet.md

git  pull  origin  main  --no-edit  --no-rebase  "$CHEATSHEET_FILE"

fi
```

# WAGTAIL
### [How to use StreamField for mixed content](https://docs.wagtail.org/en/v5.2.1/topics/streamfield.html)

---
### [StreamField block reference](https://docs.wagtail.org/en/v5.2.1/reference/streamfield/blocks.html#streamfield-block-reference) ### 

### [Templating - Jinja](https://docs.wagtail.org/en/v5.2.2/reference/jinja2.html)

#### [Wrinting Templates](https://docs.wagtail.org/en/v5.2.2/topics/writing_templates.html#writing-templates)

La regola da seguire è questa:

 

<span style="background-color: #FFFFCC; color: #000000; padding: 5px;">`code: class wagtail.fields.StreamField(blocks, use_json_field=None, blank=False, min_num=None, max_num=None, block_counts=None, collapsed=False)`</span>

E questa la spiegazione:

**class wagtail.fields.StreamField**: This line defines a class named StreamField in the wagtail.fields module.

**(blocks, use_json_field=None, blank=False, min_num=None, max_num=None, block_counts=None, collapsed=False)**: These are the parameters that the StreamField class constructor (__init__ method) accepts. Let's go through each one:

**blocks**: This is a required parameter. It represents the blocks that can be used in the stream. It seems like it should be provided when creating an instance of StreamField.

**use_json_field**=None: This is an optional parameter with a default value of None. It allows you to specify whether to use a JSON field for storage. If not provided, it defaults to None.

**blank**=False: This is an optional parameter with a default value of False. It indicates whether the field is allowed to be blank when used in a form. If not provided, it defaults to False.

**min_num**=None: This is an optional parameter with a default value of None. It specifies the minimum number of blocks required. If not provided, it defaults to None.

**max_num**=None: This is an optional parameter with a default value of None. It specifies the maximum number of blocks allowed. If not provided, it defaults to None.

**block_counts**=None: This is an optional parameter with a default value of None. It seems related to counting blocks. If not provided, it defaults to None.

**collapsed**=False: This is an optional parameter with a default value of False. It indicates whether the blocks should be collapsed in the Wagtail admin interface. If not provided, it defaults to False

Così ad esempio per questo codice. Possiamo effettuare il breakdown di questo codice in base alla regola definita:

`class BlogPage(Page):
    author = models.CharField(max_length=255, default='Default Author')
    date = models.DateField("Post date")
    
    body = StreamField(
        [
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('code', CodeBlock()),
            ('raw_html', RawHTMLBlock()),
        ],
        use_json_field=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]
`

**author** = models.CharField(max_length=255, default='Default Author'): This line defines a character field named author in the BlogPage class. It has a maximum length of 255 characters and a default value of 'Default Author'.

**date** = models.DateField("Post date"): This line defines a date field named date in the BlogPage class with a human-readable name "Post date".

**body** = StreamField([...], use_json_field=True): This line defines a stream field named body in the BlogPage class. It allows the inclusion of different block types, such as CharBlock, RichTextBlock, ImageChooserBlock, CodeBlock, and RawHTMLBlock. **The use_json_field parameter is set to True, indicating that a JSON field will be used for storage.**

**content_panels** = Page.content_panels + [...]: This line defines the content panels for the Wagtail admin interface. It includes panels for 'author', 'date', and 'body'.

Poi in particolare:
## content_panels definition in the BlogPage class:

`content_panels = Page.content_panels + [
    FieldPanel('author'),
    FieldPanel('date'),
    FieldPanel('body'),
]`

**Page.content_panels**: This part includes the content panels defined in the parent Page class. It allows the inclusion of standard page fields, such as title, slug, publish date, etc.

**FieldPanel('author')**: This adds a panel for the author field to the content panels. It's likely a simple text input for the author's name.

**FieldPanel('date')**: This adds a panel for the date field, probably a date picker for selecting the post date.

**FieldPanel('body')**: This adds a panel for the body field. Since it's a StreamField, it might include a dynamic set of blocks like headings, paragraphs, images, code blocks, and raw HTML.

## Uso dello StructBox in Wagtail

Example Model with StructBlock
Consider a simple model for a page with a StreamField containing a StructBlock named 'person':

<span style="background-color: #FFFFCC; color: #000000; padding: 5px;">` # models.py
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class BlogPage(Page):
    body = StreamField([
        ('person', blocks.StructBlock([
            ('first_name', blocks.CharBlock()),
            ('surname', blocks.CharBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('biography', blocks.RichTextBlock()),
        ])),
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ] `</span>
Diagram Explanation
Blog Page with StreamField and StructBlock:

A BlogPage contains a StreamField named 'body'.
'body' includes various block types, one of which is a StructBlock named 'person'.
Person StructBlock:

The 'person' block is a StructBlock containing fields like 'first_name', 'surname', 'photo', and 'biography'.
Block Instances:

When editing a BlogPage, you can add multiple instances of different block types, including 'person'. Each 'person' block instance can have its own 'first_name', 'surname', 'photo', and 'biography' 

***Template Implementation***

To render this in a template, you can use the following:
```
`<!-- templates/blog_page.html -->
{% extends "base.html" %}

{% block content %}
    <article>
        {% for block in page.body %}
            {% if block.block_type == 'person' %}
                <div class="person">
                    {% if block.value.photo %}
                        {% image block.value.photo width-400 %}
                    {% endif %}
                    <h2>{{ block.value.first_name }} {{ block.value.surname }}</h2>
                    {{ block.value.biography }}
                </div>
            {% else %}
                {# Rendering for other block types #}
                <section class="{{ block.block_type }}">
                    {% include_block block %}
                </section>
            {% endif %}
        {% endfor %}
    </article>
{% endblock %} 
```

---

***Database Initialization***

When you run makemigrations and migrate after adding the StructBlock to your model, the necessary database tables and fields are created. The use_json_field=True parameter in the StreamField indicates that the data for the StreamField will be stored as JSON in the database.

Here's how you perform the migration:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
After migration, you can create or edit a BlogPage instance through the Wagtail admin interface. The StructBlock fields will be part of the form for each 'person' block within the 'body' StreamField.

### Riferimenti Rapidi Wagtail
 - [Caso Studio web page](https://www.outreachy.org/docs/internship/)
 - [How to use Streamfield for mixed content](https://docs.wagtail.org/en/v5.2.1/topics/streamfield.html)
 - [StreamFieldBlock Reference](https://docs.wagtail.org/en/v5.2.1/reference/streamfield/blocks.html#streamfield-block-reference)
- 


## Caratteristiche avanzate di Diango - Wagtail
Uno dei porblemi che si incontrano effettuando delle tabelle all'interno di wagtail ma in generale anche in Django è il caso pratico della renderizzazione degli headers di una tabella se si vogliono recuperare ad esempio i dati all'interno delle celle della tabella.

Questo codice di esempio effettua il debug su ciò che è successo:

`<thead>
    <tr>
        {% for column in block.value.columns %}
            <th>
                {{ column.header|default:"Column Header" }}
                
                <!-- Debugging statements -->
                <p>block.value.rows: {{ block.value.rows|list }}</p>
                <p>block.value.rows.1: {{ block.value.rows|list.1|default:"" }}</p>
                
                {% with block.value.rows|list.1|default:"" as row_values %}
                    {{ row_values.0|default:"" }}
                {% endwith %}
            </th>
        {% endfor %}
    </tr>
</thead>
`
Un estratto di codice generato è questo 
`   <div class="table-wrapper">
                    <input type="text" id="search_1" placeholder="Search Table">
                    <table id="datatable_1" class="display nowrap datatable">
                        <thead>
                            <tr>
                                
                                    <th>
                                        Column Header
                                        
                                        <!-- Debugging statements -->
                                        <p>block.value.rows: &lt;generator object TypedTable.rows at 0x7f08958de2e0&gt;</p>
                                        <p>block.value.rows.1: </p> `

Approfondendo la ricerca si artriva a tale indicazione
:::caution
The issue seems to be related to the fact that block.value.rows is a generator object. In Python, generators are lazy and can be consumed only once. If you try to iterate through the generator more than once, you will get an empty result on subsequent iterations.

In your case, it seems like the generator has been consumed once, which is why when you try to access block.value.rows.1, it doesn't contain any values.

To address this issue, you might want to convert the generator to a list so that you can iterate through it multiple times. However, since you are using the TypedTableBlock from wagtail.contrib.typed_table_block, you might need to adjust how you access the rows.

Here is a modification that converts the generator to a list before using it:

django
Copy code
<thead>
    <tr>
        {% for column in block.value.columns %}
            <th>
                {{ column.header|default:"Column Header" }}
                
                <!-- Debugging statements -->
                <p>block.value.rows: {{ block.value.rows|list }}</p>
                <p>block.value.rows.1: {{ block.value.rows|list.1|default:"" }}</p>
                
                {% with block.value.rows|list.1|default:"" as row_values %}
                    {{ row_values.0|default:"" }}
                {% endwith %}
            </th>
        {% endfor %}
    </tr>
</thead>
This uses the |list filter to convert the generator to a list before accessing the second row. Please note that this might not be the most efficient solution, especially if your table has a large number of rows. If efficiency is a concern, you may want to explore other ways to handle this situation.
:::

## WAGTAIL Upgrade process
We recommend upgrading one feature release at a time, even if your project is several versions behind the current one. This has a number of advantages over skipping directly to the newest release:

If anything breaks as a result of the upgrade, you will know which version caused it, and will be able to troubleshoot accordingly;

Deprecation warnings shown in the console output will notify you of any code changes you need to make before upgrading to the following version;

Some releases make database schema changes that need to be reflected on your project by running ./manage.py makemigrations - this is liable to fail if too many schema changes happen in one go.

Before upgrading to a new feature release:

Check your project’s console output for any deprecation warnings, and fix them where necessary;

Check the new version’s release notes, and the Compatible Django / Python versions table below, for any dependencies that need upgrading first;

Make a backup of your database.

To upgrade:

Update the wagtail line in your project’s requirements.txt file to specify the latest patch release of the version you wish to install. For example, to upgrade to version 1.8.x, the line should read:
`wagtail>=1.8,<1.9
Run:

pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate`

Make any necessary code changes as directed in the “Upgrade considerations” section of the release notes.

Test that your project is working as expected.

Remember that the JavaScript and CSS files used in the Wagtail admin may have changed between releases - if you encounter erratic behaviour on upgrading, ensure that you have cleared your browser cache. When deploying the upgrade to a production server, be sure to run ./manage.py collectstatic to make the updated static files available to the web server. In production, we recommend enabling ManifestStaticFilesStorage in the STATICFILES_STORAGE setting - this ensures that different versions of files are assigned distinct URLs.


### WAGTAIL COMPATIBILITY WITH DJANGO - [link](https://docs.wagtail.org/en/latest/releases/upgrading.html)



# PYTHON

## Spiegazione attraverso codice di __init__, __getattribute__ e super 
Spesso nei moduli di wagtail si fa riferimento alla classazione e subclassazione. Avere chiri alcuni termini è necessario. Questa è la breve sintesi attraverso un sempio


`class Vehicle:
    def `__init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")`

This is a simple class representing a vehicle with a brand.
It has an __init__ method that initializes the brand attribute and a start method to print a message when the vehicle starts.
Car (inherits from Vehicle):

python
Copy code
class Car(Vehicle):
    def __init__(self, brand, model):
        # No use of super()
​        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")
This class represents a specific type of vehicle, a Car, inheriting from the Vehicle class.
It has its own __init__ method, but it doesn't use super(), and it has a start method that overrides the start method in the Vehicle class.
CarWithSuper (inherits from Car):

class CarWithSuper(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")
    
    def __getattribute__(self, name):
        # Modifying __getattribute__ to add a prefix to the brand attribute
        if name == "brand":
            return "Awesome " + super().__getattribute__(name)
        else:
            return super().__getattribute__(name)

This class inherits from Car and introduces a new attribute color.
It uses super() in the __init__ method to call the __init__ method of the parent class (Car).
It overrides the start method, calls the parent's start method using super(), and adds an additional message.
It also modifies __getattribute__ to add a prefix ("Awesome") to the brand attribute.
Examples:
Example without super(), __init__, and __getattribute__:

` car_without_super = Car(brand="Toyota", model="Camry")
print(car_without_super.model)  # Output: Camry
An instance of Car is created without using super().
__init__ in Car is called, but __init__ of the parent (Vehicle) is not called.
start method from Vehicle is not available in car_without_super.
Example with super(), __init__, and __getattribute__:
car_with_super = CarWithSuper(brand="Ford", model="Mustang", color="red")
print(car_with_super.brand)  # Output: Awesome Ford
car_with_super.start()  # Output: Ford Mustang car started. The red car is ready to go.
`

An instance of CarWithSuper is created using super() to call __init__ of the parent (Car).
__getattribute__ is modified to add a prefix to the brand attribute.
start method calls the parent's (Car) start method using super() and adds an additional message.
Roles:

***__init__:*** 
Used for initializing the attributes of an object.
In the inheritance chain, it's common to use super().__init__(...) to call the initializer of the parent class.

***__getattribute__:*** Called whenever an attribute of an object is accessed.
Can be modified to customize attribute access.
Used here to modify the behavior of accessing the brand attribute.

***super():*** Used to refer to the parent class.
In __init__, it's used to call the initializer of the parent class.
In methods, it's used to call methods from the parent class.
In the provided example, super() helps maintain the hierarchy in inheritance, ensuring that the methods of the parent classes are appropriately called. __init__ is used for object initialization, and __getattribute__ is modified to customize attribute access.

### Vediamo ora cosa succede se non utilizziamo i metodi 

### Assenza di __init__ 

If you don't use the __init__ method in the Vehicle class, the class will still be valid, but instances of the class won't have a constructor to initialize their state. The __init__ method is a special method in Python classes that is automatically called when an object is created. It is used for initializing the attributes of the object.

Here's what happens when you don't include __init__:

python
Copy code
class Vehicle:
    def start(self):
        print("Vehicle started.")

### Creating an instance without __init__
vehicle_instance = Vehicle()

### This will not raise an error, but the instance won't have a 'brand' attribute.
### If you try to access 'brand', it will result in an AttributeError.
print(vehicle_instance.start())  # Output: Vehicle started.
print(vehicle_instance.brand)  # AttributeError: 'Vehicle' object has no attribute 'brand'
In the example above, creating an instance of Vehicle without an __init__ method is allowed. However, without an __init__ method, instances won't have any attributes initialized during instantiation. If you try to access an attribute that hasn't been defined, you will get an AttributeError.

Including the __init__ method allows you to initialize the state of an object when it is created. For example:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

### Creating an instance with __init__
vehicle_instance = Vehicle(brand="Toyota")

`Now, the 'brand' attribute is initialized during instantiation.`
print(vehicle_instance.start())  # Output: Toyota vehicle started.
print(vehicle_instance.brand)  # Output: Toyota
In the second example, the __init__ method is used to initialize the brand attribute when a Vehicle instance is created. This ensures that the instance has a properly initialized state from the beginning.

## Ed ora quando posso usare e non usare __getattribute__?
If you don't define the __getattribute__ method in a class, Python will use the default behavior for attribute access. The default behavior involves looking up the attribute in the object's dictionary and returning its value if found. If the attribute is not found in the object's dictionary, Python looks for the attribute in the class hierarchy.

Here's what happens if you don't use __getattribute__:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

## Creating an instance without __getattribute__
vehicle_instance = Vehicle(brand="Toyota")

### Accessing the 'brand' attribute without a custom __getattribute__
print(vehicle_instance.brand)  # Output: Toyota

### The default behavior is used, and there is no need for a custom __getattribute__ in this case.
In the example above, we create a Vehicle class with an __init__ method to initialize the brand attribute. When we access the brand attribute, the default attribute access behavior is used, and there is no need for a custom __getattribute__. The attribute is found in the instance's dictionary, and its value is returned.

The __getattribute__ method is a powerful tool for customizing attribute access, and it allows you to intercept attribute access calls and customize the behavior. However, in many cases, you may not need to override it, and the default behavior is sufficient for basic attribute access. Only when you need to customize the attribute access behavior should you consider defining a __getattribute__ method.


In the example provided, the __getattribute__ method is used to customize the behavior of accessing the brand attribute in the CarWithSuper class. Specifically, it adds a prefix ("Awesome") to the value of the brand attribute before returning it.

Here's the relevant part of the code:

python
Copy code
class CarWithSuper(Car):
    # ...

    def __getattribute__(self, name):
        # Modifying __getattribute__ to add a prefix to the brand attribute
        if name == "brand":
            return "Awesome " + super().__getattribute__(name)
        else:
            return super().__getattribute__(name)
In this case, the __getattribute__ method is modifying the behavior of accessing the brand attribute. Without this customization, accessing car_with_super.brand would simply return the value of the brand attribute. With the custom __getattribute__, it returns the value with the added prefix.

So, you might need to use __getattribute__ when you want to customize or intercept attribute access calls and modify the behavior based on your specific requirements. It's a powerful tool, but it should be used judiciously, as unnecessary or incorrect use may lead to unexpected behavior and potential issues.

## MIXIN
L'esempio esposto e che di seguito si ripropone risulta anche un ottimo esempio di mixin

Yes, the provided example with Vehicle, Car, and CarWithSuper can be considered an example of mixin-like behavior. Let me break it down:

Vehicle Class:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")
This is the base class representing a generic vehicle. It has an __init__ method to initialize the brand attribute and a start method.

Car Class (Inherits from Vehicle):

python
Copy code
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")
The Car class inherits from Vehicle. It has its own __init__ method but uses super() to call the __init__ method of the parent class (Vehicle). It also has its own start method, overriding the start method of Vehicle.

CarWithSuper Class (Inherits from Car):

python
Copy code
class CarWithSuper(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")
    
    def __getattribute__(self, name):
        if name == "brand":
            return "Awesome " + super().__getattribute__('brand')
        else:
            return super().__getattribute__(name)
The CarWithSuper class inherits from Car and introduces a new attribute (color). It uses super() to call the __init__ method of the parent class (Car). It also overrides the start method, calling the parent's (Car) start method using super() and adding an additional message. Additionally, it modifies __getattribute__ to add a prefix ("Awesome") to the brand attribute.

So, in this example, the classes are organized in a way that exhibits mixin-like behavior. The CarWithSuper class enhances the behavior of the Car class by adding attributes and modifying methods, and it uses super() to maintain the hierarchy and call methods from parent classes. While it may not strictly adhere to the classic definition of a mixin, it shares some characteristics of mixin-like behavior.

### Definizione di mixin ##


In object-oriented programming, a mixin is a class that provides a certain functionality to be inherited by a subclass, but is not meant to stand alone. Mixins are used to enhance the functionality of a class without the need for multiple inheritance.

Here are some key characteristics and features of mixins:

Purpose-Specific Functionality: Mixins are designed to provide a specific set of functionalities or behaviors that can be easily added to other classes. They encapsulate a piece of behavior.

Reusability: Mixins promote code reuse. Instead of duplicating code in multiple classes, you can create a mixin and include it in various classes that need that particular behavior.

No Standalone Use: Mixins are not meant to be instantiated or used independently. They lack the complete implementation to be used as standalone classes. They are intended to be combined with other classes.

Flexible Composition: Since a class can inherit from multiple mixins, it allows for flexible composition of functionalities. This is in contrast to languages that do not support multiple inheritance directly.

Avoids Diamond Problem: Mixins can help avoid the "diamond problem" that arises in languages with multiple inheritance, where a class inherits from two classes that have a common ancestor.

Small and Focused: Mixins are typically small and focused on a specific task. This makes them easy to understand, maintain, and reuse.

# STANDARD COMMANDS IN DJANGO INSTALLATION#

1) python3 -m venv venv

# USEFUL PROPERTY AND METHOD IN DJANGO #

## L'uso di Queryset ##

Django querysets have several notable properties and methods that provide flexibility and ease of use when interacting with the database. Here are some key properties and methods of querysets:

Chaining:

Querysets are lazy, meaning they don't hit the database until an action is performed.
Multiple filters and operations can be chained together to build complex queries.
Example:

python
Copy code
queryset = Model.objects.filter(field1=value1).exclude(field2=value2).order_by('-date_created')
Slicing:

Querysets can be sliced to retrieve a specific range of objects.
Example:

python
Copy code
queryset = Model.objects.all()
result_slice = queryset[5:10]  # Retrieve objects 5 through 9
Count:

The count method returns the number of objects in the queryset without fetching the actual objects.
Example:

python
Copy code
count = queryset.count()
Distinct:

The distinct method eliminates duplicate rows from the queryset.
Example:

python
Copy code
distinct_values = Model.objects.values('field').distinct()
Aggregate:

The aggregate method allows for the calculation of aggregate values (e.g., sum, average) on the queryset.
Example:

python
Copy code
from django.db.models import Avg
average_value = Model.objects.aggregate(avg_value=Avg('numeric_field'))
Values and ValuesList:

The values method returns a queryset of dictionaries representing the values of specific fields.
The values_list method returns a queryset of tuples representing the values of specific fields.
Example:

python
Copy code
values_queryset = Model.objects.values('field1', 'field2')
values_list_queryset = Model.objects.values_list('field1', 'field2')
Exists:

The exists method checks if there are any records in the queryset.
Example:


queryset_exists = Model.objects.filter(field=value).exists()
Update and Delete:

The update method modifies multiple records in the database without fetching them.
The delete method deletes records from the database without fetching them.
Example:

python
Copy code
Model.objects.filter(field=value).update(status='new_status')
Model.objects.filter(field=value).delete()
These are just a few of the many properties and methods provided by Django querysets. They offer a powerful and expressive way to interact with the database.

### Esempio in wagtail ###

from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from wagtail.core.models import Page
from your_app.models import RoundPage  # Replace 'your_app' with the actual name of your app
from path.to.get_deadline_date_for import get_deadline_date_for  # Replace 'path.to' with the actual path

def docs_internship(request):
    now = datetime.now(timezone.utc)
    today = get_deadline_date_for(now)
    five_weeks_ago = today - timedelta(days=7 * 5)

    applicant_round = RoundPage.objects.filter(
        pingnew__lte=today,
        internannounce__gt=today,
    ).first()
    
    intern_round = RoundPage.objects.filter(
        internannounce__lte=today,
        internends__gt=five_weeks_ago,
    ).first()
    
    return render(request, 'home/docs/internship_guide.html', {
        'applicant_round': applicant_round,
        'intern_round': intern_round,
    })



# GIT & GITHUB
Riferimenti [Mastering MarkDown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
### Ricordarsi di aggiungere .gitgnore
**- git add .gitignore**
**- git commit -m "Add .gitignore to exclude compiled Python files"**
### Per effettuare il push da origine a remoto 
**- git push origin implementazione-pagina**
### Switch to the New Branch:
**- git checkout new-branch-name**
### Creare una nuova branch e posizionarsi sulla stessa
**- git checkout -b new-branch-name**
---
*Il comando può essere visto come la sintesi dei due seguenti comandi:*
---
**- git branch new-branch-name  # Create a new branch**
**- git checkout new-branch-name  # Switch to the new branch**

## You've created a new branch (template-tutorial) without committing changes on your existing branch (implementazione-pagina) ##

To address this, you'll need to follow these steps to commit your changes on the implementazione-pagina branch and then switch back to the template-tutorial branch. Here's a step-by-step guide:

- Commit Changes on implementazione-pagina:
Assuming you are currently on the template-tutorial branch, ** switch back to the implementazione-pagina branch:**

`git checkout implementazione-pagina`

Now, add and commit your changes:

`git add .`
`git commit -m "Your commit message here"`

- **Push Changes to Remote (implementazione-pagina):**
Assuming the remote branch is named implementazione-pagina:

`git push origin implementazione-pagina`

- ** Switch Back to template-tutorial:**
Now, switch back to the template-tutorial branch:

`git checkout template-tutorial`


*** If you haven't pushed the template-tutorial branch yet, you can push it to the remote repository when you're ready:***

`git push origin template-tutorial`

*** How can see from my vsc local if a git branch is present also in the remote github? ***

`git fetch --all
git branch -a
`
This fetches all branches from the remote repository and lists both local and remote branches. Remote branches are prefixed with "remotes/origin/". Check if your branch is listed among the remotes.

*** Come posso creare una nuova branch in local, e poi crearla anche in Github, poi effettuare il push e rendere questa branch principale? ***

Create a new branch locally and switch to it (chimiamo la nuova branch template-tutorial):
`git checkout -b template-tutorial`

Push the new branch to GitHub - *** If you want to make sure that the new branch on GitHub exactly matches your local branch, you can use the -u (or --set-upstream) option when pushing for the first time ***

`git push -u origin template-tutorial`

Set the upstream for the new branch:

`git branch --set-upstream-to=origin/template-tutorial template-tutorial`![alt]( '{"class": "", "title": ""}')

Now, further pushes can be simplified to:

`git push`

To revert the changes and go back to the original commit before the changes, you can use the following commands:
`git reset --hard HEAD
git clean -fd`


The first command (git reset --hard HEAD) resets your branch to the latest commit, discarding changes. The second command (git clean -fd) removes untracked files and directories. Use them with caution, as they are not reversible.

-fd stands for what?
In the context of the git clean command:

-f stands for force.
-d stands for directory.
Together, -fd means force removal of untracked directories. This option is used to remove untracked files and directories forcefully.

## delete a local branch and also delete it on the remote repository on GitHub #

Delete the local branch:

`git branch -d branch_name`![alt]( '{"class": "", "title": ""}')

Replace branch_name with the name of the branch you want to delete.

If the branch contains unmerged changes, you might need to force delete it:

`git branch -D branch_name`

Delete the remote branch:

`git push origin --delete branch_name`

This will delete the branch on the remote repository (GitHub).

Update your local repository to reflect the changes on the remote:

`git fetch --prune`

The --prune flag removes any remote tracking branches that no longer exist on the remote.

## I want to synch another an oldest branch named "template-tutorial" with a newest branch named template-sheetlike and after delete this last one (template-sheetlike) ## 

Switch to the template-tutorial branch:
`git switch template-tutorial`

Rebase template-sheetlike onto template-tutorial:
`git rebase template-sheetlike`

Push the changes to the remote repository:
`git push origin template-tutorial --force`
Note: Force-pushing after a rebase rewrites the commit history. Use it with caution, especially if the branch has already been shared with others

Delete the template-sheetlike branch:
`git branch -d template-sheetlike`
`git push origin --delete template-sheetlike`

### some useful notes ###

Merge:
Creates Merge Commits: When you merge one branch into another, Git creates a new merge commit that has two parent commits: **one from the branch you're merging and another from the branch you're merging into.
This results in a non-linear history with multiple branches merging into each other**
Preserves Original History:

The original commits from both branches remain unchanged. This approach keeps a clear record of when changes were made on each branch.

###### Rebase:

Linearizes History:

Rebase is used to linearize the commit history. It moves or combines a sequence of commits to a new base commit.
When you rebase one branch onto another, it effectively transplants the entire branch onto the tip of the other branch, creating a linear history.
No Merge Commits:

Unlike merge, rebase doesn't create additional merge commits.
It can result in a cleaner, more linear history.
When to Choose Each Approach:

###### Merge:

Use merge when you want to preserve the original commit history, especially when collaborating with others.
Good for feature branches and when you want to maintain a clear record of branch integration points.
Rebase:

Use rebase when you want a clean, linear history and don't mind rewriting commits.
Useful for feature branches before merging into a shared branch to avoid unnecessary merge commits.
Switch vs. Checkout:
git switch is a more modern and user-friendly command introduced in recent versions of Git. It is designed specifically for branch switching. If you're using a version of Git that supports git switch, you can replace git checkout with git switch:

###### Switching Branch:

git switch template-tutorial
Both commands essentially do the same thing in this context, but git switch provides a clearer and more explicit syntax for branch-related operations. If your Git version supports it, feel free to use git switch instead of git checkout.

# YAML PROTOCOL

YAML (YAML Ain't Markup Language) is a human-readable data serialization format that is often used for configuration files and data exchange between languages with different data structures. In a YAML file, indentation is crucial, as it determines the structure of the data. Here are some details on writing YAML files:

### 1. **Indentation:**

- YAML uses indentation to represent the structure of the data. Spaces are recommended for indentation (not tabs), and the number of spaces is significant. Typically, two spaces or four spaces are used for each level of indentation.

```yaml
codekey1:
  key2: value
  key3:
    - item1
    - item2
```

### 2. **Key-Value Pairs:**

- YAML uses a simple key-value format. Keys and values are separated by a colon, and the key-value pair is represented on a new line.

```yaml
codename: John Doe
age: 30
```

### 3. **Lists:**

- Lists are represented using a hyphen followed by a space (`- `). Lists can contain any combination of values, and each item is indented under the list key.

```yaml
codefruits:
  - apple
  - banana
  - orange
```

### 4. **Dictionaries (Mappings):**

- Dictionaries or mappings are represented using key-value pairs, and the key-value pairs are indented under the dictionary key.

```yaml
  name: John Doe
  age: 30
```

### 5. **Strings:**

- Strings can be written without quotes. However, quotes are used when a string contains special characters or reserved words.

```yaml
message: Hello, World!
```

### 6. **Multiline Strings:**

- Multiline strings can be represented using the `|` or `>` characters. The `|` preserves newlines, while `>` folds newlines.

```yaml
codemultiline: |
  This is a multiline
  string in YAML.
```

### 7. **Comments:**

- Comments start with the `#` character and continue to the end of the line.

```yaml
code# This is a comment
key: value
```

### 8. **Anchors and Aliases:**

- YAML supports anchors (`&`) and aliases (`*`) for creating references to the same data in multiple places.

```yaml
codefirst: &anchor_name John Doe
second: *anchor_name
```

These are some basic conventions for writing YAML files. Ensure that you are consistent with indentation, use proper syntax for key-value pairs, lists, and dictionaries, and pay attention to the structure of your YAML documents. Many programming languages and tools use YAML, and understanding its syntax is beneficial for working with various configurations and data files.


# WAGTAIL
### [How to use StreamField for mixed content](https://docs.wagtail.org/en/v5.2.1/topics/streamfield.html) ###

---
### [StreamField block reference](https://docs.wagtail.org/en/v5.2.1/reference/streamfield/blocks.html#streamfield-block-reference) ### 

### [Templating - Jinja](https://docs.wagtail.org/en/v5.2.2/reference/jinja2.html)

#### [Wrinting Templates](https://docs.wagtail.org/en/v5.2.2/topics/writing_templates.html#writing-templates)

La regola da seguire è questa:

 

<span style="background-color: #FFFFCC; color: #000000; padding: 5px;">`code: class wagtail.fields.StreamField(blocks, use_json_field=None, blank=False, min_num=None, max_num=None, block_counts=None, collapsed=False)`</span>

E questa la spiegazione:

**class wagtail.fields.StreamField**: This line defines a class named StreamField in the wagtail.fields module.

**(blocks, use_json_field=None, blank=False, min_num=None, max_num=None, block_counts=None, collapsed=False)**: These are the parameters that the StreamField class constructor (__init__ method) accepts. Let's go through each one:

**blocks**: This is a required parameter. It represents the blocks that can be used in the stream. It seems like it should be provided when creating an instance of StreamField.

**use_json_field**=None: This is an optional parameter with a default value of None. It allows you to specify whether to use a JSON field for storage. If not provided, it defaults to None.

**blank**=False: This is an optional parameter with a default value of False. It indicates whether the field is allowed to be blank when used in a form. If not provided, it defaults to False.

**min_num**=None: This is an optional parameter with a default value of None. It specifies the minimum number of blocks required. If not provided, it defaults to None.

**max_num**=None: This is an optional parameter with a default value of None. It specifies the maximum number of blocks allowed. If not provided, it defaults to None.

**block_counts**=None: This is an optional parameter with a default value of None. It seems related to counting blocks. If not provided, it defaults to None.

**collapsed**=False: This is an optional parameter with a default value of False. It indicates whether the blocks should be collapsed in the Wagtail admin interface. If not provided, it defaults to False

Così ad esempio per questo codice. Possiamo effettuare il breakdown di questo codice in base alla regola definita:

`class BlogPage(Page):
    author = models.CharField(max_length=255, default='Default Author')
    date = models.DateField("Post date")
    
    body = StreamField(
        [
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('code', CodeBlock()),
            ('raw_html', RawHTMLBlock()),
        ],
        use_json_field=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]
`

**author** = models.CharField(max_length=255, default='Default Author'): This line defines a character field named author in the BlogPage class. It has a maximum length of 255 characters and a default value of 'Default Author'.

**date** = models.DateField("Post date"): This line defines a date field named date in the BlogPage class with a human-readable name "Post date".

**body** = StreamField([...], use_json_field=True): This line defines a stream field named body in the BlogPage class. It allows the inclusion of different block types, such as CharBlock, RichTextBlock, ImageChooserBlock, CodeBlock, and RawHTMLBlock. **The use_json_field parameter is set to True, indicating that a JSON field will be used for storage.**

**content_panels** = Page.content_panels + [...]: This line defines the content panels for the Wagtail admin interface. It includes panels for 'author', 'date', and 'body'.

Poi in particolare:
#### content_panels definition in the BlogPage class:####

`content_panels = Page.content_panels + [
    FieldPanel('author'),
    FieldPanel('date'),
    FieldPanel('body'),
]`

**Page.content_panels**: This part includes the content panels defined in the parent Page class. It allows the inclusion of standard page fields, such as title, slug, publish date, etc.

**FieldPanel('author')**: This adds a panel for the author field to the content panels. It's likely a simple text input for the author's name.

**FieldPanel('date')**: This adds a panel for the date field, probably a date picker for selecting the post date.

**FieldPanel('body')**: This adds a panel for the body field. Since it's a StreamField, it might include a dynamic set of blocks like headings, paragraphs, images, code blocks, and raw HTML.

## Uso dello StructBox in Wagtail ##

Example Model with StructBlock
Consider a simple model for a page with a StreamField containing a StructBlock named 'person':

<span style="background-color: #FFFFCC; color: #000000; padding: 5px;">` # models.py
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class BlogPage(Page):
    body = StreamField([
        ('person', blocks.StructBlock([
            ('first_name', blocks.CharBlock()),
            ('surname', blocks.CharBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('biography', blocks.RichTextBlock()),
        ])),
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ] `</span>
Diagram Explanation
Blog Page with StreamField and StructBlock:

A BlogPage contains a StreamField named 'body'.
'body' includes various block types, one of which is a StructBlock named 'person'.
Person StructBlock:

The 'person' block is a StructBlock containing fields like 'first_name', 'surname', 'photo', and 'biography'.
Block Instances:

When editing a BlogPage, you can add multiple instances of different block types, including 'person'. Each 'person' block instance can have its own 'first_name', 'surname', 'photo', and 'biography' 

***Template Implementation***

To render this in a template, you can use the following:
```
`<!-- templates/blog_page.html -->
{% extends "base.html" %}

{% block content %}
    <article>
        {% for block in page.body %}
            {% if block.block_type == 'person' %}
                <div class="person">
                    {% if block.value.photo %}
                        {% image block.value.photo width-400 %}
                    {% endif %}
                    <h2>{{ block.value.first_name }} {{ block.value.surname }}</h2>
                    {{ block.value.biography }}
                </div>
            {% else %}
                {# Rendering for other block types #}
                <section class="{{ block.block_type }}">
                    {% include_block block %}
                </section>
            {% endif %}
        {% endfor %}
    </article>
{% endblock %} 
```

---

***Database Initialization***

When you run makemigrations and migrate after adding the StructBlock to your model, the necessary database tables and fields are created. The use_json_field=True parameter in the StreamField indicates that the data for the StreamField will be stored as JSON in the database.

Here's how you perform the migration:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
After migration, you can create or edit a BlogPage instance through the Wagtail admin interface. The StructBlock fields will be part of the form for each 'person' block within the 'body' StreamField.

### Riferimenti Rapidi Wagtail ###
 - [Caso Studio web page](https://www.outreachy.org/docs/internship/)

 - [How to use Streamfield for mixed content](https://docs.wagtail.org/en/v5.2.1/topics/streamfield.html)

 - [StreamFieldBlock Reference](https://docs.wagtail.org/en/v5.2.1/reference/streamfield/blocks.html#streamfield-block-reference)

   


# Caratteristiche avanzate di Diango - Wagtail 
Uno dei porblemi che si incontrano effettuando delle tabelle all'interno di wagtail ma in generale anche in Django è il caso pratico della renderizzazione degli headers di una tabella se si vogliono recuperare ad esempio i dati all'interno delle celle della tabella.

**Attenzione!**: questo progetto è illustrato al solo fine didattico. Infatti nell'applicazione concreta vi sono notevoli problemi nell'effettuare il passaggio dei dati da Django a Wagtail. Per cui ai fini applicativi la via migliore per rendere i dati da Django a Wagtail è quella della costruzione di un API attraverso serializer (vedere capitolo)

Questo codice di esempio effettua il debug su ciò che è successo:

`<thead>
    <tr>
        {% for column in block.value.columns %}
            <th>
                {{ column.header|default:"Column Header" }}
                

                <!-- Debugging statements -->
                <p>block.value.rows: {{ block.value.rows|list }}</p>
                <p>block.value.rows.1: {{ block.value.rows|list.1|default:"" }}</p>
                
                {% with block.value.rows|list.1|default:"" as row_values %}
                    {{ row_values.0|default:"" }}
                {% endwith %}
            </th>
        {% endfor %}
    </tr>
</thead>
`
Un estratto di codice generato è questo 
`   <div class="table-wrapper">
                    <input type="text" id="search_1" placeholder="Search Table">
                    <table id="datatable_1" class="display nowrap datatable">
                        <thead>
                            <tr>
                                
                                    <th>
                                        Column Header
                                        
                                        <!-- Debugging statements -->
                                        <p>block.value.rows: &lt;generator object TypedTable.rows at 0x7f08958de2e0&gt;</p>
                                        <p>block.value.rows.1: </p> `

Approfondendo la ricerca si artriva a tale indicazione
:::caution
The issue seems to be related to the fact that block.value.rows is a generator object. In Python, generators are lazy and can be consumed only once. If you try to iterate through the generator more than once, you will get an empty result on subsequent iterations.

In your case, it seems like the generator has been consumed once, which is why when you try to access block.value.rows.1, it doesn't contain any values.

To address this issue, you might want to convert the generator to a list so that you can iterate through it multiple times. However, since you are using the TypedTableBlock from wagtail.contrib.typed_table_block, you might need to adjust how you access the rows.

Here is a modification that converts the generator to a list before using it:

django
Copy code
<thead>
    <tr>
        {% for column in block.value.columns %}
            <th>
                {{ column.header|default:"Column Header" }}
                
                <!-- Debugging statements -->
                <p>block.value.rows: {{ block.value.rows|list }}</p>
                <p>block.value.rows.1: {{ block.value.rows|list.1|default:"" }}</p>
                
                {% with block.value.rows|list.1|default:"" as row_values %}
                    {{ row_values.0|default:"" }}
                {% endwith %}
            </th>
        {% endfor %}
    </tr>
</thead>
This uses the |list filter to convert the generator to a list before accessing the second row. Please note that this might not be the most efficient solution, especially if your table has a large number of rows. If efficiency is a concern, you may want to explore other ways to handle this situation.
:::

## HOW TO FEED A TABLE FROM DJANGO ADMIN PANEL, OPEN IN AS BLOCK INTO WAGTAIL ADMIN PANEL AND RENDER IT INTO THE WAGTAIL FRONTEND 

Premessa: prima di effettuare questa complessa operazione va tenuto in conto che i due progetti uno django e l'altro wagtail derivano da due repository differenti. Quindi il problema iniziale sarà quello di renedere omogenei i file .git. Per fare ciò dunque di seguito si descrive il metodo migliore individuato:

If you want to consolidate both the Django and Wagtail projects into a single Git repository, and you've already initialized separate repositories in each project's directory, you have a couple of options:

Option 1: Delete Existing Git Repositories

1. **Delete Git repositories in directory and subdirectories:**

   - Navigate to each subdirectory (e.g., `django_general_template2` and `blog_wiki_wag/blog_page_wiki_wag/wiki-wag`) containing a Git repository.
   - Run `rm -rf .git` to delete the existing Git repository.

2. **Initialize a new Git repository in the root directory:**

   - Run `cd /path/to/django_general_template2` (replace `/path/to/django_general_template2` with your actual path).
   - Run `git init` to initialize a new Git repository.

3. **Add, commit, and push:**

   - Add all files with `git add .`.
   - Commit the changes with `git commit -m "Initial commit"`.
   - If you've already set up a remote repository, push the changes to it.

   Great! Since you've deleted the existing Git repositories and initialized a new one in the root directory, here are the steps to create a new GitHub repository (`django-wiki-wag`) and push your local changes to it:

   1. **Create a New GitHub Repository:**

      - Go to [GitHub](https://github.com/).
      - Log in to your account.
      - Click the "+" icon in the top right corner and select "New repository."
      - Fill in the repository name (e.g., `django-wiki-wag`), add a description if you want, and choose other repository settings.
      - Click "Create repository."

   2. **Set the Remote Origin for Your Local Repository:**

      - In your local terminal, navigate to the root directory of your project.

      - Run the following commands, replacing the repository URL with your newly created repository URL:

        ```
        bashCopy code
        git remote add origin https://github.com/your-username/django-wiki-wag.git
        ```

   3. **Add, Commit, and Push:**

      - Run the following commands to add all files, commit your changes, and push to GitHub:

        ```
        bashCopy codegit add .
        git commit -m "Initial commit"
        git push -u origin main
        ```

      - Note: Replace `main` with the name of the branch you are working on (it could be `master` or another branch).

   4. **Verify on GitHub:**

      - Visit your GitHub repository (`https://github.com/your-username/django-wiki-wag`).
      - Confirm that your files and project structure are visible.

   Now, your local project should be synchronized with the new GitHub repository. If you encounter any issues during the process, feel free to ask for further assistance!

To achieve your goal, you'll need to follow a series of steps. I'll provide you with a step-by-step guide to make the necessary changes and additions to your Django admin, Wagtail models, and HTML template.

- **Step 1: Adjust Wagtail Settings**

  In the `settings.py` of your Wagtail project (`wiki-wag`), ensure that the `ALLOWED_HOSTS` setting includes the appropriate values for your Django project. Update other settings if needed.

  ```python
  pythonCopy code# wiki-wag/settings/base.py
  
  ALLOWED_HOSTS = ['yourdjangoapp.com', 'localhost', '127.0.0.1']
  ```

- **Step 2: Add Wagtail settings to Django settings.py**
  
  In your Django project (`general_template 1), include the Wagtail settings by updating settings.py:
  
  ```python
  """
  Django settings for general_template1 project.
  
  Generated by 'django-admin startproject' using Django 4.2.2.
  
  For more information on this file, see
  https://docs.djangoproject.com/en/4.2/topics/settings/
  
  For the full list of settings and their values, see
  https://docs.djangoproject.com/en/4.2/ref/settings/
  """
  
  from pathlib import Path
  
  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent
  
  
  # Quick-start development settings - unsuitable for production
  # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
  
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-2-yc!0z!mcv#w$3vk6#s5i635l+bg#x3+24w2!26ikg4o-dj4u'
  
  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True
  
  # ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '146.190.169.21'] # tiene conto delle attività su droplet
  ALLOWED_HOSTS = ['app.sgbh.org', 'www.sgbh.org', '127.0.0.1', 'localhost', '146.190.169.21']
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
  
  
  # Application definition
  
  INSTALLED_APPS = [
      
      'wagtail.contrib.forms',
      'wagtail.contrib.redirects',
      'wagtail.embeds',
      'wagtail.sites',
      'wagtail.users',
      'wagtail.snippets',
      'wagtail.documents',
      'wagtail.images',
      'wagtail.search',
      'wagtail.admin',
      
      'taggit',
      'modelcluster',
    
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'sgq',
      'wagtail',
  ]
  
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      'wagtail.contrib.redirects.middleware.RedirectMiddleware',
  ]
  
  ROOT_URLCONF = 'general_template1.urls'
  
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  
  WSGI_APPLICATION = 'general_template1.wsgi.application'
  WSGI_SERVER_PORT = 443
  
  
  # Database
  # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  
  
  # Password validation
  # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
  
  AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]
  
  
  # Internationalization
  # https://docs.djangoproject.com/en/4.2/topics/i18n/
  
  LANGUAGE_CODE = 'en-us'
  
  TIME_ZONE = 'UTC'
  
  USE_I18N = True
  
  USE_TZ = True
  
  
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/4.2/howto/static-files/
  
  STATIC_URL = 'static/'
  
  # Default primary key field type
  # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
  
  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  ```
  
- **Step 3: Add Wagtail URLs to Django URLs**
  
  In your Django project (`general_template 1), include the Wagtail urls by updating urls.py:
  
  ```python
  from django.contrib import admin
  from django.urls import path, include
  from wagtail import urls as wagtail_urls
  
  urlpatterns = [
      path('', include('sgq.urls')),  # Include the app-level URLs
      path('admin/', admin.site.urls),
      # path('wagtail/', include('wagtail.core.urls')), # nuovo inserimento
      path('wagtail/', include(wagtail_urls)), # nuovo inserimento
     
  ]
  ```
  
- **Step 4: Add a Fixed Table Block to Your Models **and Update BlogPage Model **
  In your **blog/models.py**, add the FixedTableBlock to the list of available blocks. This block will represent the fixed table content. Include the FixedTableBlock in the StreamField of your BlogPage model.
  
  - The key changes here are adding the import for `FixedTableBlock` and including it in the `StreamField` under the name `'fixed_table'`.
  

```python

from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.models import Page
from wagtail import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from django.db import models
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from .blocks import PublicationBlock # rif 1 - Adding in rendering get_absolute_url
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.images.blocks import ImageChooserBlock

class RawHTMLBlock(blocks.RawHTMLBlock):
    class Meta:
        icon = "code"  # Set a suitable icon from available Wagtail icons
        template = 'blog/raw_html_block.html'

class CodeBlock(blocks.StructBlock):
    code = blocks.TextBlock()
    class Meta:
        template = 'blog/code_block.html'

class FixedTableBlock(blocks.StructBlock):
    fixed_table_text = blocks.CharBlock()

    class Meta:
        icon = 'table'  # Set an icon for the block
        template = 'blog/fixed_table_block.html'  # Create this template for rendering the block

class BlogPage(Page):
    author = models.CharField(max_length=255, default='Default Author')
    date = models.DateField("Post date")
    
    # New field for content choice
    content_choice = models.CharField(
        max_length=20,
        choices=[
            ('choice_one', 'Choice One'),
            ('choice_two', 'Choice Two'),
        ],
        default='choice_one',  # Set a default choice
        help_text="Select the content to be displayed on the page."
    )
    
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock()),
        ('raw_html', RawHTMLBlock()),
        ('publication', PublicationBlock()), # rif 1 - Adding in rendering get_absolute_url
        ('table', TypedTableBlock([
            ('text', blocks.CharBlock()),
            ('numeric', blocks.FloatBlock()),
            ('rich_text', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('country', blocks.ChoiceBlock(choices=[
                ('be', 'Belgium'),
                ('fr', 'France'),
                ('de', 'Germany'),
                ('nl', 'Netherlands'),
                ('pl', 'Poland'),
                ('uk', 'United Kingdom'),
            ])),
        ])),
        ('fixed_table', FixedTableBlock()),  # Add the FixedTableBlock
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('content_choice'),
        FieldPanel('body'),
    ]

```
[^Removal of special-purpose field panel types]: Removal of special-purpose field panel typesThe panel types `StreamFieldPanel`, `RichTextFieldPanel`, `ImageChooserPanel`, `DocumentChooserPanel` and `SnippetChooserPanel` have been phased out, and can now be replaced with `FieldPanel`. Additionally, `PageChooserPanel` is only required when passing a `page_type` or `can_choose_root`, and can otherwise be replaced with `FieldPanel`. In all cases, `FieldPanel` will now automatically select the most appropriate form element. This feature was developed by Matt Westcott.

**Step 5: **Go in the **Wagtail manage.py level** and make sure to run migrations after making these changes:

```
python3 manage.py makemigrations
python3 manage.py migrate
```



Now you can use the Wagtail admin to add and edit the content for the `fixed_table` block in your `BlogPage`. This content should then be rendered in your `blog_page.html` 

> At this stage you go into Wagtail Project via **python3 manage.py runserver ** into admin panel and if all works you can access and add the table. In the wagtail preview mode you receive a visualization error because the **blog/fixed_table_block.html** does not exists!



**Step 6 - Creation of blog/fixed_table_block.html**

So before to jump to Django admin level to create an input data entry let's try to enter the data from **FixedTableBlock()**. In this manner sure that all is working fine just until now.   To do this First, update the `FixedTableBlock` in `models.py`:

```python
pythonCopy codefrom wagtail.core import blocks

class FixedTableBlock(blocks.StructBlock):
    nation = blocks.CharBlock(required=True, help_text='Enter nation')
    capital = blocks.CharBlock(required=True, help_text='Enter capital')

    class Meta:
        template = 'blog/fixed_table_block.html'
```

Then, create or update the template file at **blog/templates/blog/fixed_table_block.html**:

```html
htmlCopy code<div>
    <table class="table table-bordered table-striped">
        <thead>
            <tr>
                <th>Nation</th>
                <th>Capital</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{{ value.nation }}</td>
                <td>{{ value.capital }}</td>
            </tr>
        </tbody>
    </table>
</div>
```



**Go in the Wagtail manage.py level** and make sure to run migrations after making these changes:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate
```

If all works you are able to input the data and see the table in Wagtail preview mode

> **Always remeber to conslidate you commmit pushing on Github**



**Step 7 - Implementation models.py - Django side**

**Create a Django model for the content you want to manage:**

Define a Django model in your `models.py` that represents the content you want to associate with the `FixedTableBlock`

```python
pythonCopy code# models.py

from django.db import models

class FixedTableContent(models.Model):
    nation = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)

    def __str__(self):
        return self.nation
```



**Step 8 - Implementation admin.py - Django side**

**Create an admin class for the new model:**

Create an admin class for your new model in the `admin.py` file:

```python
# admin.py

from django.contrib import admin
from .models import FixedTableContent

@admin.register(FixedTableContent)
class FixedTableContentAdmin(admin.ModelAdmin):
    list_display = ('nation', 'capital')
```

This admin class will allow you to manage instances of `FixedTableContent` in the Django admin.

--------- FINO A QUI --

template.Step 3: Create Template for FixedTableBlock
Create a template file at blog/templates/blog/fixed_table_block.html for rendering the FixedTableBlock. This template will be used to display the fixed table content.

html
Copy code
<span>{{ value.fixed_table_text }}</span>
Step 4: Run Migrations
Run the following commands to apply the model changes:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Step 5: Update Django Admin
Create an admin class for BlogPage in blog/wagtail_hooks.py:

python
Copy code
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup
)
from .models import BlogPage

class BlogPageAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'Blog Pages'
    menu_icon = 'doc-full-inverse'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'author', 'date', 'content_choice')
    search_fields = ('title', 'author', 'date', 'content_choice')

modeladmin_register(BlogPageAdmin)
Step 6: Include Admin CSS
In your blog/static/css/admin.css file, add the following CSS to improve the display of the custom block in the admin.

css
Copy code
.wagtail-edit-handler-fixed_table .field-content textarea {
    height: 100px; /* Adjust the height as needed */
}
Step 7: Update BlogPage Admin Panels
Update the content_panels in BlogPage to include the new block:

python
Copy code
# ...

class BlogPage(Page):
    # ...

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('content_choice'),
        FieldPanel('body'),
    ]
Step 8: Update blog_page.html
Update blog/templates/blog/blog_page.html to render the new FixedTableBlock.

html
Copy code
<!-- ... existing code ... -->

{% for block in page.body %}
    {% if block.block_type == 'fixed_table' %}
        {% include_block block %}
    {% elif block.block_type == 'table' %}
        <!-- ... existing table code ... -->
    {% elif block.block_type == 'heading' %}
        <!-- ... existing heading code ... -->
    {% elif block.block_type == 'publication' %}
        <!-- ... existing publication code ... -->
    {% else %}
        <!-- ... existing block code ... -->
    {% endif %}
{% endfor %}

<!-- ... existing code ... -->
Step 9: Restart Server
Restart your development server to see the changes:

bash
Copy code
python manage.py runserver
Now you should be able to add and edit the fixed table content in the Django admin and see it rendered on your blog_page.html. Adjust the styles and templates according to your design preferences.

This guide assumes a basic project structure, so adjust the paths if your project structure is different. Let me know if you have any questions or if there's anything specific you'd like to clarify!

-----------------

### WAGTAIL Upgrade process ###
We recommend upgrading one feature release at a time, even if your project is several versions behind the current one. This has a number of advantages over skipping directly to the newest release:

If anything breaks as a result of the upgrade, you will know which version caused it, and will be able to troubleshoot accordingly;

Deprecation warnings shown in the console output will notify you of any code changes you need to make before upgrading to the following version;

Some releases make database schema changes that need to be reflected on your project by running ./manage.py makemigrations - this is liable to fail if too many schema changes happen in one go.

Before upgrading to a new feature release:

Check your project’s console output for any deprecation warnings, and fix them where necessary;

Check the new version’s release notes, and the Compatible Django / Python versions table below, for any dependencies that need upgrading first;

Make a backup of your database.

To upgrade:

Update the wagtail line in your project’s requirements.txt file to specify the latest patch release of the version you wish to install. For example, to upgrade to version 1.8.x, the line should read:
`wagtail>=1.8,<1.9
Run:

pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate`

Make any necessary code changes as directed in the “Upgrade considerations” section of the release notes.

Test that your project is working as expected.

Remember that the JavaScript and CSS files used in the Wagtail admin may have changed between releases - if you encounter erratic behaviour on upgrading, ensure that you have cleared your browser cache. When deploying the upgrade to a production server, be sure to run ./manage.py collectstatic to make the updated static files available to the web server. In production, we recommend enabling ManifestStaticFilesStorage in the STATICFILES_STORAGE setting - this ensures that different versions of files are assigned distinct URLs.



# FEEDING DATA FROM DJANGO TO WAGATAIL VIA API

Steps:


To create a Django API app and expose the data to your Wagtail project, you can follow these steps:

### Step 1: Create Django API App ([create a Django app from 0)](#create-a-django-app-from-0)

1. Open your terminal and navigate to the root directory of your Django project.

2. Run the following command to create a new Django app for your API:

   ```python
   python manage.py startapp django_api_for_wagtail
   ```

3. Install the Django REST framework to use it in your Django API app. Django REST framework is a powerful and flexible toolkit for building Web APIs in Django.

   You can install it using `pip`. Open your terminal and navigate to your project's root directory. Then, run the following command:

   ```python
   pip3 install djangorestframework
   ```

4. After installing, you'll need to add `'rest_framework'` to the `INSTALLED_APPS` in your project's `settings.py`:

   ```python
   # myproject/settings.py
   INSTALLED_APPS = [
       # ...
       'rest_framework',
       # ...
   ]
   ```

   Now that you have a separate app named `django_api_for_wagtail` for the purpose, let's create a data input example. Assuming you've created your `Nation` model within this app, here are the corrected steps:

   ### Django API (Django Side):

   #### models.py in `django_api_for_wagtail` app:

   ```python
   # django_api_for_wagtail/models.py
   from django.db import models
   
   class Nation(models.Model):
       name = models.CharField(max_length=255, unique=True)
       capital = models.CharField(max_length=255)
   
       def __str__(self):
           return self.name
   ```

   #### serializers.py in `django_api_for_wagtail` app:

   ```python
   # django_api_for_wagtail/serializers.py
   from rest_framework import serializers
   from .models import Nation
   
   class NationSerializer(serializers.ModelSerializer):
       class Meta:
           model = Nation
           fields = '__all__'
   ```

   #### views.py in `django_api_for_wagtail` app:

   ```python
   #django_api_for_wagtail/views.py
   from rest_framework import generics
   from .models import Nation
   from .serializers import NationSerializer
   
   class NationAPIView(generics.ListCreateAPIView):
       queryset = Nation.objects.all()
       serializer_class = NationSerializer
   ```

   #### urls.py in `django_api_for_wagtail` app:

   ```python
   # django_api_for_wagtail/urls.py
   from django.urls import path
   from .views import NationAPIView
   
   urlpatterns = [
       path('nations/', NationAPIView.as_view(), name='nation-api'),
       # Add more URL patterns as needed
   ]
   
   
   ```

   #### admin.py in django_api_for_wagtail app:

   Here's an example of how you should register the `Nation` model in the admin.py file:

   ```python
   # django_api_for_wagtail/admin.py
   from django.contrib import admin
   from .models import Nation
   
   @admin.register(Nation)
   class NationAdmin(admin.ModelAdmin):
       list_display = ('name', 'capital')
   ```

   #### urls.py in progetto_api project:
   
   To make Django recognize the URLs of your `django_api_for_wagtail` app, you need to include the URLs of your app in the `urls.py` file at the project level. You can do this using Django’s `include()` function, which allows you to reference other URL configurations.
   
   Here’s how you might update your `urls.py` file at the project level:Python
   
   
   
   ```python
   from django.contrib import admin
   from django.urls import include, path
   
   urlpatterns = [
       path("admin/", admin.site.urls),
       path("django_api_for_wagtail/", include('django_api_for_wagtail.urls')),
   ]
   ```

### Test if the steps are correct

```python
python3 manage.py makemigrations
```

```python
python3 manage.py migrate
```

If all is ok you can try:

http://127.0.0.1:8000/django_api_for_wagtail/nations/ (frontend side - with json results)

 http://127.0.0.1:8000/admin/django_api_for_wagtail/nation/ (backend side - with admin panel)

In this way, I can verify the correct data entry on the backend side and the correct management in JSON on the frontend side. 



### Step 2: Create Views for API

1. In the `api` app directory, create a `views.py` file.

2. Define a view for your API in `views.py`. For example:

   ```python
   from rest_framework import generics
   from blog.models import BlogPage
   from .serializers import BlogPageSerializer
   
   class BlogPageAPIView(generics.ListAPIView):
       queryset = BlogPage.objects.all()
       serializer_class = BlogPageSerializer
   ```

### Step 3: Configure URLs for API

1. In the `api` app directory, create a `urls.py` file.

2. Define the URL patterns for your API in `urls.py`. For example:

   ```python
   from django.urls import path
   from .views import BlogPageAPIView
   
   urlpatterns = [
       path('blog/', BlogPageAPIView.as_view(), name='blog-api'),
       # Add more URL patterns as needed
   ]
   ```

### Step 4: Configure Main Project URLs

1. In the main project directory, open the `urls.py` file.

2. Include the URLs of your API app in the project's URL configuration. Update the `urlpatterns`:

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('api.urls')),  # Adjust the URL pattern as needed
       # Add other URL patterns as needed
   ]
   ```

### Step 5: Run Migrations and Start the Development Server

1. Run the following commands to apply migrations and start the development server:

   ```bash
   manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## Definitive Code for mini Django project API

### Step 6: create the a frontend (to see the data )

To create a simple frontend to visualize the results from your Django API, you can use Django's built-in templates. Here's a step-by-step guide:

1. Create a `templates` directory within your `django_api_for_wagtail` app.

2. Inside the `templates` directory, create an HTML file for rendering the nation data. Let's call it `nations_list.html`.

   ```html
   <!-- django_api_for_wagtail/templates/nations_list.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Nations List</title>
   </head>
   <body>
       <h1>Nations List</h1>
       <ul>
           {% for nation in nations %}
               <li>{{ nation.name }} - {{ nation.capital }}</li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

3. Update your `views.py` to use this template:

   ```python
   # django_api_for_wagtail/views.py
   from django.shortcuts import render
   from rest_framework import generics
   from .models import Nation
   from .serializers import NationSerializer
   
   class NationAPIView(generics.ListCreateAPIView):
       queryset = Nation.objects.all()
       serializer_class = NationSerializer
   
       def list(self, request, *args, **kwargs):
           nations = self.get_queryset()
           return render(request, 'nations_list.html', {'nations': nations})
   ```

   It is worth to breakdown the code above: 

   Let's break down the `list` method in the `NationAPIView` class:

   ```python
   # django_api_for_wagtail/views.py
   
   from django.shortcuts import render
   from rest_framework import generics
   from .models import Nation
   from .serializers import NationSerializer
   
   class NationAPIView(generics.ListCreateAPIView):
       queryset = Nation.objects.all()
       serializer_class = NationSerializer
   
       def list(self, request, *args, **kwargs):
           nations = self.get_queryset()
           return render(request, 'nations_list.html', {'nations': nations})
   ```

   1. **`queryset` and `serializer_class`**: These are attributes of the `NationAPIView` class. `queryset` defines the initial query set of nations, and `serializer_class` specifies the serializer to be used for serializing the data.
   2. **`list` method**: This method is part of the `ListCreateAPIView` class provided by Django REST Framework. It handles the HTTP GET request for the list view.
   3. **`self.get_queryset()`**: This method retrieves the query set of nations. In this case, it gets all the objects from the `Nation` model specified in the `queryset` attribute.
   4. **`render` function**: This function is used to render an HTML template. It takes the following parameters:
      - `request`: The HTTP request object.
      - `'nations_list.html'`: The name of the template file to be rendered.
      - `{'nations': nations}`: A dictionary containing data to be passed to the template. In this case, it includes the retrieved nations from the query set.
   5. **`return render(...)`**: This line returns the rendered HTML content as an HTTP response. The rendered content will be the result of applying the data from the `nations` query set to the 'nations_list.html' template.

   In summary, when a user accesses the URL associated with the `NationAPIView`, the `list` method is called. It retrieves the list of nations, passes them to the 'nations_list.html' template, renders the HTML content, and returns it as an HTTP response. This allows you to view a list of nations in a web browser when accessing the corresponding URL.

   

   Let's break down the `list` method in more detail:

   ```python
   list(self, request, *args, **kwargs):
       nations = self.get_queryset()
       return render(request, 'nations_list.html', {'nations': nations})
   ```

   1. **`self`**: In Python, `self` is a convention for referring to the instance of the class. In this context, it represents an instance of the `NationAPIView` class.

   2. **`request`**: This is the HTTP request object that is passed to the view. It contains information about the incoming request, such as the method (GET, POST, etc.), headers, and any data sent in the request.

   3. **`\*args` and `\**kwargs`**: These are used to collect additional positional and keyword arguments. In this case, they are not used in the method body, but the method signature includes them to allow flexibility.The usage of `*args` and `**kwargs` provides flexibility when defining functions or methods that can accept a variable number of arguments.

      ###### 	**Using `\*args` for Variable Positional Arguments:**

      ```python
      example_function(*args):
          for arg in args:
              print(arg)
      
      example_function(1, 2, 3, 'four')
      ```

      In this example, `*args` allows the function to accept any number of positional arguments. It collects them into a tuple named `args`, and the function can iterate over them.

      1. **Using `\**kwargs` for Variable Keyword Arguments:**

         ```python
         example_function(**kwargs):
             for key, value in kwargs.items():
                 print(f"{key}: {value}")
         
         example_function(name='John', age=25, city='New York')
         ```

         In this example, `**kwargs` allows the function to accept any number of keyword arguments. It collects them into a dictionary named `kwargs`, and the function can iterate over the key-value pairs.

      2. **Combining `\*args` and `\**kwargs`:**

         ```
         example_function(arg1, arg2, *args, **kwargs):
             print(f"arg1: {arg1}")
             print(f"arg2: {arg2}")
             print(f"Additional positional arguments: {args}")
             print(f"Additional keyword arguments: {kwargs}")
         
         example_function(1, 2, 3, 4, key1='value1', key2='value2')
         ```

         In this example, `arg1` and `arg2` are regular positional arguments, `*args` collects additional positional arguments into a tuple, and `**kwargs` collects additional keyword arguments into a dictionary.

      Using `*args` and `**kwargs` allows a function or method to be more flexible and accommodate a varying number of arguments without explicitly specifying them in the function signature. This is particularly useful in cases where the number of arguments might change or when writing functions that need to work with a wide range of inputs.

   5. **`self.get_queryset()`**: This method is inherited from the `ListCreateAPIView` class of Django REST Framework. It retrieves the queryset of nations. The `get_queryset` method is responsible for returning the list of objects that will be used in the view.

   6. **`nations`**: This variable stores the queryset of nations obtained from `self.get_queryset()`.

   7. **`render(request, 'nations_list.html', {'nations': nations})`**: The `render` function is a shortcut provided by Django for rendering an HTML template. It takes the following arguments:

      - `request`: The HTTP request object.
   - `'nations_list.html'`: The name of the HTML template file to be rendered.
      - `{'nations': nations}`: A dictionary containing data to be passed to the template. In this case, it includes the list of nations obtained from the queryset.

   8. **`return render(...)`**: This line returns the rendered HTML content as an HTTP response. The rendered content will be the result of applying the data from the `nations` queryset to the 'nations_list.html' template.
   
   In summary, the `list` method is responsible for retrieving a queryset of nations and rendering an HTML template ('nations_list.html') with the nations' data. The rendered HTML content is then returned as an HTTP response. This is a common pattern for providing a list view in a Django REST Framework API.

4. #### Update your `urls.py` to include a URL pattern for rendering the nations list:

   ```python
   # django_api_for_wagtail/urls.py
   from django.urls import path
   from .views import NationAPIView
   
   urlpatterns = [
       path('nations/', NationAPIView.as_view(), name='nation-api'),
       path('nations/list/', NationAPIView.as_view(), name='nations-list'),
       # Add more URL patterns as needed
   ]
   ```

5. Finally, update your `urls.py` at the project level to include the `django_api_for_wagtail` URLs:

   ```python
   # progetto_api/urls.py
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('django_api_for_wagtail/', include('django_api_for_wagtail.urls')),
   ]
   ```

Now, when you visit the URL http://127.0.0.1:8000/django_api_for_wagtail/nations/list/, it should render the nations list using the template.

------

Fino a qui

### Step 6: Access the API

1. Open your web browser and navigate to `http://127.0.0.1:8000/api/blog/` (or the URL you configured).
2. You should see the serialized data from your Wagtail model.

### Step 7: Integrate with Wagtail

1. In your Wagtail project, you can now fetch data from the API endpoint (`http://127.0.0.1:8000/api/blog/`) using Django's `requests` library or any other method you prefer.
2. Use the retrieved data to populate your Wagtail views/templates as needed.

This is a basic setup, and you may need to customize it based on your specific requirements. Additionally, you might want to add authentication and permission controls to secure your API.


### WAGTAIL COMPATIBILITY WITH DJANGO ## - [link](https://docs.wagtail.org/en/latest/releases/upgrading.html)



# PYTHON

## Spiegazione attraverso codice di __init__, __getattribute__ e super ##
Spesso nei moduli di wagtail si fa riferimento alla classazione e subclassazione. Avere chiri alcuni termini è necessario. Questa è la breve sintesi attraverso un sempio

`class Vehicle:
    def `__init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")`

This is a simple class representing a vehicle with a brand.
It has an __init__ method that initializes the brand attribute and a start method to print a message when the vehicle starts.
Car (inherits from Vehicle):

python
Copy code
class Car(Vehicle):
    def __init__(self, brand, model):
        # No use of super()
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")
This class represents a specific type of vehicle, a Car, inheriting from the Vehicle class.
It has its own __init__ method, but it doesn't use super(), and it has a start method that overrides the start method in the Vehicle class.
CarWithSuper (inherits from Car):

class CarWithSuper(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")
    
    def __getattribute__(self, name):
        # Modifying __getattribute__ to add a prefix to the brand attribute
        if name == "brand":
            return "Awesome " + super().__getattribute__(name)
        else:
            return super().__getattribute__(name)

This class inherits from Car and introduces a new attribute color.
It uses super() in the __init__ method to call the __init__ method of the parent class (Car).
It overrides the start method, calls the parent's start method using super(), and adds an additional message.
It also modifies __getattribute__ to add a prefix ("Awesome") to the brand attribute.
Examples:
Example without super(), __init__, and __getattribute__:

` car_without_super = Car(brand="Toyota", model="Camry")
print(car_without_super.model)  # Output: Camry
An instance of Car is created without using super().
__init__ in Car is called, but __init__ of the parent (Vehicle) is not called.
start method from Vehicle is not available in car_without_super.
Example with super(), __init__, and __getattribute__:
car_with_super = CarWithSuper(brand="Ford", model="Mustang", color="red")
print(car_with_super.brand)  # Output: Awesome Ford
car_with_super.start()  # Output: Ford Mustang car started. The red car is ready to go.
`

An instance of CarWithSuper is created using super() to call __init__ of the parent (Car).
__getattribute__ is modified to add a prefix to the brand attribute.
start method calls the parent's (Car) start method using super() and adds an additional message.
Roles:

***__init__:*** 
Used for initializing the attributes of an object.
In the inheritance chain, it's common to use super().__init__(...) to call the initializer of the parent class.

***__getattribute__:*** Called whenever an attribute of an object is accessed.
Can be modified to customize attribute access.
Used here to modify the behavior of accessing the brand attribute.

***super():*** Used to refer to the parent class.
In __init__, it's used to call the initializer of the parent class.
In methods, it's used to call methods from the parent class.
In the provided example, super() helps maintain the hierarchy in inheritance, ensuring that the methods of the parent classes are appropriately called. __init__ is used for object initialization, and __getattribute__ is modified to customize attribute access.

### Vediamo ora cosa succede se non utilizziamo i metodi ##

### Assenza di __init__ ###

If you don't use the __init__ method in the Vehicle class, the class will still be valid, but instances of the class won't have a constructor to initialize their state. The __init__ method is a special method in Python classes that is automatically called when an object is created. It is used for initializing the attributes of the object.

Here's what happens when you don't include __init__:

python
Copy code
class Vehicle:
    def start(self):
        print("Vehicle started.")

## Creating an instance without __init__
vehicle_instance = Vehicle()

## This will not raise an error, but the instance won't have a 'brand' attribute.
### If you try to access 'brand', it will result in an AttributeError.
print(vehicle_instance.start())  # Output: Vehicle started.
print(vehicle_instance.brand)  # AttributeError: 'Vehicle' object has no attribute 'brand'
In the example above, creating an instance of Vehicle without an __init__ method is allowed. However, without an __init__ method, instances won't have any attributes initialized during instantiation. If you try to access an attribute that hasn't been defined, you will get an AttributeError.

Including the __init__ method allows you to initialize the state of an object when it is created. For example:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

# Creating an instance with __init__
vehicle_instance = Vehicle(brand="Toyota")

# Now, the 'brand' attribute is initialized during instantiation.
print(vehicle_instance.start())  # Output: Toyota vehicle started.
print(vehicle_instance.brand)  # Output: Toyota
In the second example, the __init__ method is used to initialize the brand attribute when a Vehicle instance is created. This ensures that the instance has a properly initialized state from the beginning.

#### Ed ora quando posso usare e non usare __getattribute__?###
If you don't define the __getattribute__ method in a class, Python will use the default behavior for attribute access. The default behavior involves looking up the attribute in the object's dictionary and returning its value if found. If the attribute is not found in the object's dictionary, Python looks for the attribute in the class hierarchy.

Here's what happens if you don't use __getattribute__:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

## Creating an instance without __getattribute__
vehicle_instance = Vehicle(brand="Toyota")

## Accessing the 'brand' attribute without a custom __getattribute__
print(vehicle_instance.brand)  # Output: Toyota

### The default behavior is used, and there is no need for a custom __getattribute__ in this case.
In the example above, we create a Vehicle class with an __init__ method to initialize the brand attribute. When we access the brand attribute, the default attribute access behavior is used, and there is no need for a custom __getattribute__. The attribute is found in the instance's dictionary, and its value is returned.

The __getattribute__ method is a powerful tool for customizing attribute access, and it allows you to intercept attribute access calls and customize the behavior. However, in many cases, you may not need to override it, and the default behavior is sufficient for basic attribute access. Only when you need to customize the attribute access behavior should you consider defining a __getattribute__ method.


In the example provided, the __getattribute__ method is used to customize the behavior of accessing the brand attribute in the CarWithSuper class. Specifically, it adds a prefix ("Awesome") to the value of the brand attribute before returning it.

Here's the relevant part of the code:

python
Copy code
class CarWithSuper(Car):
    # ...

    def __getattribute__(self, name):
        # Modifying __getattribute__ to add a prefix to the brand attribute
        if name == "brand":
            return "Awesome " + super().__getattribute__(name)
        else:
            return super().__getattribute__(name)
In this case, the __getattribute__ method is modifying the behavior of accessing the brand attribute. Without this customization, accessing car_with_super.brand would simply return the value of the brand attribute. With the custom __getattribute__, it returns the value with the added prefix.

So, you might need to use __getattribute__ when you want to customize or intercept attribute access calls and modify the behavior based on your specific requirements. It's a powerful tool, but it should be used judiciously, as unnecessary or incorrect use may lead to unexpected behavior and potential issues.

## MIXIN ##
L'esempio esposto e che di seguito si ripropone risulta anche un ottimo esempio di mixin

Yes, the provided example with Vehicle, Car, and CarWithSuper can be considered an example of mixin-like behavior. Let me break it down:

Vehicle Class:

python
Copy code
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")
This is the base class representing a generic vehicle. It has an __init__ method to initialize the brand attribute and a start method.

Car Class (Inherits from Vehicle):

python
Copy code
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")
The Car class inherits from Vehicle. It has its own __init__ method but uses super() to call the __init__ method of the parent class (Vehicle). It also has its own start method, overriding the start method of Vehicle.

CarWithSuper Class (Inherits from Car):

python
Copy code
class CarWithSuper(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")
    
    def __getattribute__(self, name):
        if name == "brand":
            return "Awesome " + super().__getattribute__('brand')
        else:
            return super().__getattribute__(name)
The CarWithSuper class inherits from Car and introduces a new attribute (color). It uses super() to call the __init__ method of the parent class (Car). It also overrides the start method, calling the parent's (Car) start method using super() and adding an additional message. Additionally, it modifies __getattribute__ to add a prefix ("Awesome") to the brand attribute.

So, in this example, the classes are organized in a way that exhibits mixin-like behavior. The CarWithSuper class enhances the behavior of the Car class by adding attributes and modifying methods, and it uses super() to maintain the hierarchy and call methods from parent classes. While it may not strictly adhere to the classic definition of a mixin, it shares some characteristics of mixin-like behavior.

### Definizione di mixin ##


In object-oriented programming, a mixin is a class that provides a certain functionality to be inherited by a subclass, but is not meant to stand alone. Mixins are used to enhance the functionality of a class without the need for multiple inheritance.

Here are some key characteristics and features of mixins:

Purpose-Specific Functionality: Mixins are designed to provide a specific set of functionalities or behaviors that can be easily added to other classes. They encapsulate a piece of behavior.

Reusability: Mixins promote code reuse. Instead of duplicating code in multiple classes, you can create a mixin and include it in various classes that need that particular behavior.

No Standalone Use: Mixins are not meant to be instantiated or used independently. They lack the complete implementation to be used as standalone classes. They are intended to be combined with other classes.

Flexible Composition: Since a class can inherit from multiple mixins, it allows for flexible composition of functionalities. This is in contrast to languages that do not support multiple inheritance directly.

Avoids Diamond Problem: Mixins can help avoid the "diamond problem" that arises in languages with multiple inheritance, where a class inherits from two classes that have a common ancestor.

Small and Focused: Mixins are typically small and focused on a specific task. This makes them easy to understand, maintain, and reuse.

# STANDARD COMMANDS IN DJANGO INSTALLATION#

1) python3 -m venv venv

# USEFUL PROPERTY AND METHOD IN DJANGO #

## L'uso di Queryset ##

Django querysets have several notable properties and methods that provide flexibility and ease of use when interacting with the database. Here are some key properties and methods of querysets:

Chaining:

Querysets are lazy, meaning they don't hit the database until an action is performed.
Multiple filters and operations can be chained together to build complex queries.
Example:

python
Copy code
queryset = Model.objects.filter(field1=value1).exclude(field2=value2).order_by('-date_created')
Slicing:

Querysets can be sliced to retrieve a specific range of objects.
Example:

python
Copy code
queryset = Model.objects.all()
result_slice = queryset[5:10]  # Retrieve objects 5 through 9
Count:

The count method returns the number of objects in the queryset without fetching the actual objects.
Example:

python
Copy code
count = queryset.count()
Distinct:

The distinct method eliminates duplicate rows from the queryset.
Example:

python
Copy code
distinct_values = Model.objects.values('field').distinct()
Aggregate:

The aggregate method allows for the calculation of aggregate values (e.g., sum, average) on the queryset.
Example:

python
Copy code
from django.db.models import Avg
average_value = Model.objects.aggregate(avg_value=Avg('numeric_field'))
Values and ValuesList:

The values method returns a queryset of dictionaries representing the values of specific fields.
The values_list method returns a queryset of tuples representing the values of specific fields.
Example:

python
Copy code
values_queryset = Model.objects.values('field1', 'field2')
values_list_queryset = Model.objects.values_list('field1', 'field2')
Exists:

The exists method checks if there are any records in the queryset.
Example:


queryset_exists = Model.objects.filter(field=value).exists()
Update and Delete:

The update method modifies multiple records in the database without fetching them.
The delete method deletes records from the database without fetching them.
Example:

python
Copy code
Model.objects.filter(field=value).update(status='new_status')
Model.objects.filter(field=value).delete()
These are just a few of the many properties and methods provided by Django querysets. They offer a powerful and expressive way to interact with the database.

### Esempio in wagtail ###

from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from wagtail.core.models import Page
from your_app.models import RoundPage  # Replace 'your_app' with the actual name of your app
from path.to.get_deadline_date_for import get_deadline_date_for  # Replace 'path.to' with the actual path

def docs_internship(request):
    now = datetime.now(timezone.utc)
    today = get_deadline_date_for(now)
    five_weeks_ago = today - timedelta(days=7 * 5)

    applicant_round = RoundPage.objects.filter(
        pingnew__lte=today,
        internannounce__gt=today,
    ).first()
    
    intern_round = RoundPage.objects.filter(
        internannounce__lte=today,
        internends__gt=five_weeks_ago,
    ).first()
    
    return render(request, 'home/docs/internship_guide.html', {
        'applicant_round': applicant_round,
        'intern_round': intern_round,
    })

## # Strumenti avanzati: Creare una pagina wagtail all'interno di un sito Django  ## 

- (link)[https://docs.wagtail.org/en/latest/advanced_topics/add_to_django_project.html]
- Installazione in Django al pari livello di manage.py: `python3 manage.py startapp blog_wiki_wag`
- Verifica in Wagtail di requirements.txt della compatibilità delle versioni tra Django e Wagtail. Nel caso specifico Django>=4.2,<4.3 - wagtail>=5.1,<5.2
- Verifica in Django di requirements.txt: Django==4.2.2
- Se vi è compatibilità in Wagtal: `pip3 freeze requriments.txt`
- *** Verifica del motore Database in Wagtail in base.py: *** 
- `DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
    }`
- *** Verifica del motore database in Django in settings.py: ***
- `DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }`

- Come si può vedere sopra i due motori DB sono identici
- Ora creare la subdirectory di progetto wagtail che conterrà tutti i file dell'app wagtail (quella con il quale si effettuato il requirements.txt)

 - effettuare il clone del branch da GB del progetto wagtail (vedere git e github per i dettagli)
 - a questo punto lanciare il comando Install the Project:

Navigate to the wagtail-wag directory in your terminal: `pip install -r requirements.txt`
-  Add Wagtail URLs to Django URLs: `path('wagtail/', include('wiki-wag.wagtail_urls')), # nuovo inserimento`
-  Add the required wagtail modules in setting.py: `INSTALLED_APPS = [
   
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    
    'taggit',
    'modelcluster',
  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sgq',
    'wagtail',
   ]`

-  Add'wiki-wag' app in your Django INSTALLED_APPS as well. Add it if it's not present.

INSTALLED_APPS = [
    # ...
    'wiki-wag',
    # ...
]

- add in Django settings this: 
  ` MIDDLEWARE = [
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',

  'wagtail.contrib.redirects.middleware.RedirectMiddleware',
  ] `

A questo punto dvrebbe apparire un Warning che indica qualcosa di questo genere
:::caution
WARNINGS:
?: (wagtailadmin.W003) The WAGTAILADMIN_BASE_URL setting is not defined
        HINT: This should be the base URL used to access the Wagtail admin site. Without this, URLs in notification emails will not display correctly
:::

Proseguire e verificare se in admin panel appaiono gli elementi di inpunt in Admin Panel

## So now update the urls and run makemirgations and migrate ##

from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('', include('sgq.urls')),  # Include the app-level URLs
    path('admin/', admin.site.urls),
    # path('wagtail/', include('wagtail.core.urls')), # nuovo inserimento
    path('wagtail/', include(wagtail_urls)), # nuovo inserimento

]



# DJANGO

## Create a Django App from 0 (from [Create Django API App](#create-django-api-app) )

### Step 1: Create a Virtual Environment (Optional but recommended)

Open your terminal and navigate to the directory where you want to create your Django project. Run the following commands:

```python
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Django

While in the activated virtual environment, install Django using the following command:

```python
pip3 install django
```

Step 3: Create a Django Project

Run the following command to create a new Django project:

```python
django-admin startproject progetto_api
```

Replace `myproject` with the desired name for your project.

### Step 4: Navigate to the Project Directory

Change into the project directory:

```python
cd progetto_api
```

### Step 5: Create a Django App

Run the following command to create a new Django app:

```python
python3 manage.py startapp django_api_for_wagtail
```

### Step 6: Configure Database

Open the `myproject/settings.py` file and configure the app and the database settings. By default, Django uses SQLite for development (if not already configured):

```python
# myproject/settings.py
INSTALLED_APPS = [
    # ...
    'django_api_for_wagtail',
    # ...
]

# .... #


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

### Step 7: Apply Migrations

Run the following commands to apply initial migrations:

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

### Step 8: Create a Superuser (Optional but recommended)

Run the following command to create a superuser account for the Django admin:

```
bashCopy code
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### Step 9: Run the Development Server

Start the Django development server:

```python3
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to see the Django welcome page.

### Step 10: Create a Superuser

1. After running the development server return e to your project directory (at manage.py level).

2. Run the following command to create a superuser account:

   ```python
   python3 manage.py createsuperuser
   ```

3. Follow the prompts to set a username, email, and password for the superuser account.

### Step 11: Run the Development Server

Ensure that the development server is still running:

```python
python3 manage.py runserver
```

### Step 12: Open the Admin Interface

Visit `http://127.0.0.1:8000/admin/` in your web browser. Log in with the superuser credentials you just created.

### Step 13: Verify Admin Interface

Verify that the Django admin interface is working correctly

### Step 14: Initialize a Git Repository

1. Open a new terminal window in your project directory

2. The Git commands to initialize a repository, add files, and make an initial commit should be executed at the root level of your project, where your `manage.py` file is located. The `manage.py` file is typically located at the top level of your Django project, not within the virtual environment (`venv`).

3. Run the following commands to initialize a Git repository, add all files, and make an initial commit:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

### Step 15: Create a GitHub Repository

1. Go to the [GitHub website](https://github.com/) and log in or create a new account.
2. Click on the "+" icon in the top right corner and select "New repository."
3. Follow the instructions to create a new repository on GitHub.
4. git repo name https://github.com/progettazionemauro/django-api

### Step 16: Connect Local Repository to GitHub

1. After creating the GitHub repository follow those instructions.

   - `git remote add origin https://github.com/progettazionemauro/django-api`

   - git branch -M main

     note: The `git branch -M main` command is used to rename the current branch. In Git, it's a way to both rename the current branch and force-update the tracking branches.

     Here's what the command does:

     - `git branch`: This command is used for creating, listing, renaming, and deleting branches in Git. When used without additional options, it lists all the local branches.
     - `-M main`: This option is used to rename the current branch to "main". The `-M` flag is a shortcut for `--move`, which is used for renaming branches.

     When you create a new Git repository or clone an existing one, the default branch is usually named "master." However, in recent years, there has been a movement in the Git community to use more inclusive and neutral terminology. As a result, many projects are now using "main" instead of "master" as the default branch name.

     The `git branch -M main` command is often used after creating a new repository or when transitioning from "master" to "main" to update the branch name.

     It's important to note that if you're renaming the branch you are currently on, you might need to update the remote repository to reflect the new branch name. 

     

   ```
   git remote add origin https://github.com/progettazionemauro/django-api
   git branch -M main
   git push -u origin main
   ```

   Make sure to replace "your-username" and "your-repo" with your GitHub username and repository name.

   ## Step 16 bis: problems with git push

   In doing push it can happen to find issues related to pushing for the first time into Github. For example when you created the repo and added readme.md and it is not present into local repo this can generate a misealignment that che lead to generate an error likse that:

   ```bash
   git push origin main
   `To https://github.com/progettazionemauro/django-api`
    `! [rejected]        main -> main (non-fast-forward)`
   `error: push di alcuni riferimenti su 'https://github.com/progettazionemauro/django-api' non riuscito`
   `suggerimento: Gli aggiornamenti sono stati rifiutati perché l'ultimo commit del branch`
   `suggerimento: attuale è rimasto indietro rispetto alla sua controparte remota.`
   `suggerimento: Integra le modifiche remote (ad es. con 'git pull ...') prima di`
   `suggerimento: eseguire nuovamente il push.`
   `suggerimento: Vedi la 'Nota sui fast forward' in 'git push --help' per ulteriori`
   `suggerimento: dettagli.`
   ```

   So it this is the case the best option if to do this: 

   In alternativa, puoi anche eseguire il comando:`git push --force` per forzare il push delle tue modifiche, anche se non sono un fast forward. Tuttavia, questa è una soluzione rischiosa perché potrebbe sovrascrivere le modifiche remote che non hai ancora integrato nel tuo branch locale.

   Per capire meglio cosa significa "non-fast-forward", è necessario comprendere il concetto di fast forward. Un fast forward è un tipo di push che aggiorna un branch locale con le ultime modifiche apportate a un branch remoto. Il fast forward è possibile solo se le modifiche apportate ai due branch sono consecutive.

### Step 16: Verify GitHub Repository

Go to your GitHub repository in the web browser and verify that your code has been pushed successfully.

That's it! Now you have a Django project with a superuser account, and your code is version-controlled using Git and hosted on GitHub.

### Step 10: Create Models, Views, and Templates (Optional)

You can now start building your Django app by creating models, views, and templates. Define your models in the `models.py` file, create views in the `views.py` file, and add templates in the `templates` directory.

### Step 11: Create API App (Optional)

If you want to create a separate app for your API, follow the instructions provided in the previous response to create an `api` app and set up serializers, views, and URLs.

That's it! You now have a basic Django project and app set up. Customize it based on your specific requirements and integrate it with your Wagtail project as needed.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5MTIwNTE4OV19
-->