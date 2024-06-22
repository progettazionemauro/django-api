[toc]

# MARKUP HINTS
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