from django.shortcuts import render
from .models import Date


# Create your views here.

def store(request):
    dates = Date.objects.all()
    return render(request=request,
                  template_name="store/store.html",
                  context={"dates": dates})
