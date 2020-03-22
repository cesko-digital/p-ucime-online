---
layout: page
title: "README"
permalink: /readme_wiki
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
   git submodule add -b gh-pages https://github.com/cesko.digital/p-ucime-online.git
   ```

3. Pustit skript, který vstupní wiki `*.md` soubory překopíruje jako výstupní
   `*.markdown` soubory (viz `wiki2gh-pages.py --help`)

   ```
   python3 wiki2gh-pages.py --source . --target p-ucime-online/ --dirs images/
   ```

4. Nahrát změny do `p-ucime-online` vypublikované wiki "pro lidi"

    ```
    cd p-ucime-online
    git commit -m"update 2020-02-12" -a
    git push
    ```

