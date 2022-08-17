from random import choice
from django.shortcuts import render, redirect
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    entry = util.get_entry(title)
    
    if entry != None:

        content = Markdown().convert(entry)

        return render(request, 'encyclopedia/entry.html',{
            'title':title,
            'content':content,
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def new(request):
    return render(request, 'encyclopedia/newpage.html')

def entrySave(request):
    title = request.POST['title']
    entry = util.get_entry(title)
    if entry == None:
        util.save_entry(request.POST['title'], request.POST['content'])
        return redirect("entry", title=request.POST['title'])
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "exists": True
        })

def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/editpage.html", {
            "title": title,
            "content": content
        })
    
def entryEdit(request):
    title = request.POST['title']
    content = request.POST['content']

    util.save_entry(title, content)
    return redirect("entry", title=title)
    

def randomEntry(request):
    allEntries = util.list_entries()
    randomEntry = choice(allEntries)
    
    return redirect("entry", title=randomEntry)

def search(request):
    q = request.GET['q']
    entries = util.list_entries()
    searchResults = []
    for entry in entries:
        if q.upper == entry.upper:
            return redirect("entry", title=entry)

        elif q.upper() in entry.upper():
            searchResults.append(entry)
            
                                
    return render(request, "encyclopedia/searchResults.html", {
                "query": q,
                "entries":searchResults
            })