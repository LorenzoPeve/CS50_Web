from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from markdown2 import Markdown
import random

markdowner = Markdown()

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):

    content = util.get_entry(entry)

    if content is None:
        return render(request, "encyclopedia/404.html", {'entry': entry})
    else:
        html = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
            'entry': entry, 'content': html
        })
    
# def search_entry(request, entry):

#     content = util.get_entry(entry)

#     if content is None:
#         return render(request, "encyclopedia/404.html", {'entry': entry})
#     else:
#         html = markdowner.convert(content)
#         return render(request, "encyclopedia/entry.html", {
#             'entry': entry, 'content': html
#         })

def random_page(request):
    
    entry = random.choice(util.list_entries())
    return display_entry(request, entry)