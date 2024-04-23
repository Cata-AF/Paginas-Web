from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id':'1',
        'title':"Ecommerce Website",
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':"Portafolio Website",
        'description':'This was a project where I built out my portafolio'
    
    },
    {
        'id':'3',
        'title':"Social Network",
        'description':'Awesome open source project I am still working on'
    },
]

def products(request):
    page = 'products'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'products.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'single-project.html', {'projectObj':projectObj})