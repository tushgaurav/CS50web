from pydoc import resolve
from django.shortcuts import redirect, render

from . import util

import re
from random import randrange


def index(request):
    if request.method == "POST":
        query = request.POST["q"].upper()
        entry_list = util.list_entries()
        if query in entry_list:
            return redirect("/wiki/" + query)
        for entry in entry_list:
            result = re.search(query, entry)
            if result:
                return redirect("/wiki/" + entry)
            return render(request, "encyclopedia/notexist.html", {"title": query})
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entryview(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/notexist.html", {"title": title})

    return render(
        request,
        "encyclopedia/view.html",
        {"title": title, "content": content},
    )


def random(request):
    entry_list = util.list_entries()
    index = randrange(len(entry_list))
    return redirect("/wiki/" + entry_list[index])
