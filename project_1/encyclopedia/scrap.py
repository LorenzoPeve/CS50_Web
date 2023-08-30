import markdown2

from markdown2 import Markdown

markdowner = Markdown()
markdowner.convert("*boo!*")

import os

fpath = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'entries', 'Python.md')
    )
html = markdown2.markdown_path(fpath)
print(html)