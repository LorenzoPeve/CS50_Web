from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from markdown2 import Markdown

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