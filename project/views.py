from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyModel

def form_view(request):
    if request.method == 'POST':
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')

        # Save the data to the database
        MyModel.objects.create(field1=field1, field2=field2, field3=field3)
        return HttpResponse("Data submitted successfully!")

    return render(request, 'main.html')
