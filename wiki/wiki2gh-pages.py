#!/usr/bin/env python3
"""
Move *.md files as *.markdown to gh-pages directory
"""

import os
import argparse
import shutil

def _get_args():
    parser = argparse.ArgumentParser(description='Convert md to markdown  - from wiki to jekyll')
    parser.add_argument('--source', metavar='DIR', type=str,
                        required=True,
                        help='Source directory')
    parser.add_argument('--dirs', metavar='DIR', type=str,
                        nargs="+",
                        help='Dirs to copy')
    parser.add_argument('--target', metavar='DIR', type=str,
                        required=True,
                        help='Target directory')

    args = parser.parse_args()
    return args


def _get_url(target_file):
    if target_file == "index.markdown":
        return ""
    else:
        return os.path.basename(target_file).replace(".markdown", "").lower()


def _get_title(source_file):
    return os.path.basename(source_file).replace(".md", "").replace("-", " ")


def process_md(source_file, target_file):

    with open(source_file) as source:
        with open(target_file, "w") as target:

            title = _get_title(source_file)
            url = _get_url(source_file)

            target.write("\n".join((
                    "---",
                    "layout: page",
                    "title: \"{}\"".format(_get_title(source_file)),
                    "permalink: /{}".format(_get_url(target_file)),
                    "---\n\n"
                    )))
            target.write(source.read())

def md2gh_pages(source, target, dirs):

    for f in os.listdir(source):
        if os.path.abspath(f) == os.path.abspath(target):
            continue

        if os.path.isfile(f) and f.endswith(".md"):

            if f == "README.md":
                target_file = "README_WIKI.markdown"
            elif f == "Home.md":
                target_f = "index.markdown"
            else:
                target_f = f.replace(".md", ".markdown")

            process_md(
                    os.path.join(source, f),
                    os.path.join(target, target_f)
            )



    for d in dirs:
        target_dir = os.path.join(target, d)
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree(d, target_dir)




if __name__ == "__main__":
    args = _get_args()
    md2gh_pages(args.source, args.target, args.dirs)
