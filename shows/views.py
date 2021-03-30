from django.shortcuts import render, redirect
from django.contrib import messages
from shows.models import *

# Create your views here.
def index (request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render (request, 'home.html', context)

def add_show_page(request):
    return render (request, 'add_show.html')

def add_show(request):
    
    errors = Show.objects.basic_validators(request.POST)
    
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request, v)
            
        return redirect('/show/new')
    
    else:
    
        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['date'], description = request.POST['description'])
        show_id = new_show.id
        return redirect (f'/show/{show_id}')

def show(request, show_id):
    show = Show.objects.get(id = show_id)
    context = {
        'show': show
    }
    return render (request, 'show_page.html', context)

def show_edit_page(request, show_id):
    context = {
        'show': Show.objects.get(id = show_id)
    }
    return render (request, 'edit_show.html', context)

def edit_show (request, show_id):
    show = Show.objects.get(id = show_id)
    errors = Show.objects.basic_validators(request.POST)
    
    if show.title == request.POST['title']:
        errors['title_unique'] = 'Enter a unique title'
        
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request, v)
        return redirect (f'/show/{show_id}/edit')
    
    else:
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.description = request.POST['description']
        show.save()
        return redirect (f'/show/{show_id}')

def delete_show (request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/show')