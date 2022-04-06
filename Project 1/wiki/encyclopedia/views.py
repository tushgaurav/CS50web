from django.shortcuts import render

from . import util


def index(request):
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
