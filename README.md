# <p align = center>Ecomerce-Riwi-Sportsline-API</p>


## Index
- [Gitflow](#git-flow)
- [sintax de commits](#commit-sintax)
   - [Header](#header)
   - [Body](#body)
   - [Footer](#footer)
- [Important](#important)
- [Tips](#tips)

# Ecomerce-Riwi-Sportsline-API
backend repository for advanced route project

## Git flow
To push content into this repository, you need to follow the next flow:
1. Clone the repository.
2. Set on the develop branch with
```
git checkout develop
```
2. Create a feature branch with 

```
git switch -c <corresponding_name>/<feature_name>.
```
the corresponding_name field is the same as the tipe of commit, look for [types](#type) of commit for more information

3. Pull latest changes from the branch you are working in.
4. Stage changes with 
```
git add (selected files)
```
5. Commit with a clear and descriptive message following the given description in this README.
6. Push changes to your current feature branch.
7. Check branch status with git status.
8. If it appears the following message:
<img src = "https://i.sstatic.net/Ggctq.png">
where branch main is the branch you created. There is nothing to commit.
<br>
<br>
If something looking like this appears instead
<img src = "https://www.junosnotes.com/wp-content/uploads/2021/07/Adding-deleted-and-modified-files-only-git-add-deleted-files.png">
It means that files are not being tracked.<br>
<b>Repeat from step 4</b>
<br>
<b>Note:</b> Please know that untracked files will not have the same name as the examples, and the branches won't either
<br>
<div align=right>

  [Back to top](#index)
</div>

## Commit sintax 

### Header
to commit changes into the project, you must create a telling (descriptive) commit, about the changes made following the next estructure</br>

<div align = center>

_____
< type > ( < scope > ): < description >
______
</div>

#### type 
is the change made to the project, it divides in 

<div align = center>
<br>
<br>

| *Type*     | *Meaning*                                                                 |
|--------------|-----------------------------------------------------------------------------|
| feat       | Adds a *new feature*.                                                     |
| fix        | Fixes a *bug*.                                                            |
| docs       | Changes to documentation only.                                              |
| style      | Edition in code sintax, not logic (semicolon(;), whitespaces (' '))         |
| refactor   | Code updates without changing behavior.                                     |
| test       | Adding or modifying tests.                                                  |

<br>
scope is the place where the change was made, in the (scope) part you must write down the specific file where the change appears, following the example

____
` feat(dto): ` 
<br>
<br>
` docs(controllers): `
____
</div>

<div align = "center", background>
description is a summarised description of what is in the commit, no capital letters unless is a noun, no period (.)  at the end and always in third person. Normaly you would make 1, maximum, 2 sentences long unless you want to make a long description but that is outside the head of the commit.
<br>
<br>

___
feat(user): create profile page

docs(readme): update installation steps
___
</div>
<div align=right>

  [Back to top](#index)
</div>

### Optional aditions to commit
### body
this section of the commit is designed to give a detiled explenation on the reazon why was the commit made in the very first place, you can give a little explanation on what was made but do not specifie, just give what it's needed to understand the reason of the commit
<div align=right>

  [Back to top](#index)
</div>

### footer
normaly this sections shows the issue that was given in the very first place and the authors of the commit
<div align=right>

  [Back to top](#index)
</div>

> #### *IMPORTANT:*
> - Always pull before pushing to avoid overwriting coders' work.
> - When merging into develop, open a Pull Request with a clear description of your changes.  
> - **NEVER** use --force, as it may overwrite other developers' work.
> - Every Pull Request must have approval from at least 1 coders before merging (authorized coder only). 
<div align=right>

  [Back to top](#index)
</div>


#### *TIPS*
- Use camelCase or snake_case for branch names for consistency.
- Keep branch names short, descriptive, and lowercase for readability.
<div align=right>

  [Back to top](#index)
</div>