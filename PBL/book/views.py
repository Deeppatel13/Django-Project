from django.shortcuts import render
from .forms import FormBookForm

def showform(request):
    form= FormBookForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'Book.html', context)