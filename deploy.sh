#!/bin/bash

git clone https://github.com/p-ucime-online-wiki.git wiki
cd wiki
git submodule init
git submodule update 

python3 wiki2gh-pages.py --source . --target p-ucime-online --dirs images

cd p-ucime-online
git add *
git add images/*
git commit -m"updating to date `date`"
git push
