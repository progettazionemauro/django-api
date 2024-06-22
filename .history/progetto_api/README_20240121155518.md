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