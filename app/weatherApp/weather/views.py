from django.shortcuts import render
from django.views.generic import TemplateView

# def index(request):
#     return render(request, 'weather/index.html') #returns the index.html template

class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
