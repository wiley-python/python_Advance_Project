from django.shortcuts import render

from .models import flightDetails


# Create your views here.
def display(request):
    ft = flightDetails.objects.all()
    # Collect all records from table
    return render(request, 'display.html', {' ft': ft})
