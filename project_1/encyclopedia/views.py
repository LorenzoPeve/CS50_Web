from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from markdown2 import Markdown
import random

markdowner = Markdown()

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):
    """
    Displays an encyclopedia entry if exists. Otherwise, renders error page.
    """

    content = util.get_entry(entry)
    if content is None:
        return render(request, "encyclopedia/404.html", {'entry': entry})
    else:
        html = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
            'entry': entry, 'content': html
        })

def query(request):
    """
    Redirects the search query to the wiki page if it exists or renders a page
    with "close" matches.
    """
    entries = util.list_entries()
    post_data = request.POST
    q = post_data.get('q')

    if q in entries:
        url = reverse('entry', args=[q])
        return redirect(url)
    else:
        entries = [e for e in entries if q in e]
        return render(request, "encyclopedia/search.html", {
            'entry': q, 'entries': entries
        })

def random_page(request):
    """Displays a random encyclopedia entry."""
    entry = random.choice(util.list_entries())
    return display_entry(request, entry)

def newpage(request):
    """
    Redirects the search query to the wiki page if it exists or renders a page
    with "close" matches.
    """
    return render(request, "encyclopedia/create.html")