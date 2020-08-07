from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request,title):
    return render(request, "wiki/index.html",{
       "title": util.get_entry(title)
    })

list_test=["abc123","ab23","hi"],
new_list =[]

def search(request):
    if request.method == 'GET':
        name = request.GET.get('q')
        new_name = util.get_entry(name)
        entry_list= list(util.list_entries())
        if new_name is not None:
            return HttpResponseRedirect(f'/wiki/{name}')
        elif new_name is None:
            new_list.clear()
            for ele in entry_list:
                if name.capitalize() in ele:
                    new_list.append(ele)
            return render(request, "search/index.html", {
            "new_list":new_list,
            "list_test":util.list_entries(),
            })
            return HttpResponseRedirect('search/index.html')

class newpageForm(forms.Form):
    title   = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

def create_page(request):
    if request.method == 'POST':
        form = newpageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            return HttpResponseRedirect('encyclopedia/index.html',{"var1":title,"var2":content})
    else:
        form = newpageForm()
    

    


        
        





    
    
"""
list_test=["abc123","ab23","hi"]
def search(request):
    if request.method == 'GET':
        name = request.GET.get('q')
        new_name = util.get_entry(name)
        return render(request, "search/index.html", {
        "respons":new_name,
        "key":name.capitalize(),
        "list_test":util.list_entries(),
        })
        

                "key":name.capitalize(),
                "list_test":util.list_entries(),
                "list_testt":list_test

"""


                  
        
            
       
            
            
        
    
