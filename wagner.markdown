---
layout: page
title: "README"
permalink: /wagner
---

# Wiki projektu ceko.digital p-ucime-online

Wiki je udržováná pomocí standardní GitHub wiki na adrese

https://github.com/cesko-digital/p-ucime-online/wiki/

Pro její publikaci na https://wiki.ucimeonline.cz je ale potřeba udělat několik
kroků.

## Publikace

1. vyklonovat repo `p-ucime-online.wiki`
   ```
   git clone https://github.com/cesko.digital/p-ucime-online.wiki.git
   cd p-ucime-online.wiki
   ```

2. Přidat substree `p-ucime-online` repa
   ```
   git subtree add --prefix=gh-pages https://github.com/cesko.digital/p-ucime-online.git gh-pages
   ```

3. Pustit skript, který vstupní wiki `*.md` soubory překopíruje jako výstupní
   `*.markdown` soubory (viz `wiki2gh-pages.py --help`)

   ```
   python3 wiki2gh-pages.py --source . --target gh-pages/ --dirs images/
   ```

4. Nahrát změny do `gh-pages` projektové wiki

    ```
    git commit -m"update 2020-02-12" gh-pages
    git push
    git subtree push --prefix gh-pages ssh://git@github.com/cesko-digital/p-ucime-online.git gh-page
    ```

