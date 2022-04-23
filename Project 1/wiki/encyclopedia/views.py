from pydoc import resolve
from django.shortcuts import redirect, render

from . import util

import re
import markdown2
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
        {"title": title, "content": markdown2.markdown(content)},
    )


def random(request):
    entry_list = util.list_entries()
    index = randrange(len(entry_list))
    return redirect("/wiki/" + entry_list[index])


def submit(request):
    if request.method == "POST":
        title = request.POST["name"].capitalize()
        # Checking if the entry already exists or not
        if title in util.list_entries():
            context = {
                "error_title": "Already Exists!",
                "message": "Sorry, This article already exists.",
            }
            return render(request, "encyclopedia/error.html", context)

        article = request.POST["article"]
        util.save_entry(title, article)

    return render(request, "encyclopedia/newpage.html")


def edit(request):
    if request.method == "POST":
        title = request.POST["name"].capitalize()
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("/wiki/" + title)
    title = request.GET.get("title")
    context = {"title": title, "content": util.get_entry(title)}
    return render(request, "encyclopedia/editpage.html", context)
