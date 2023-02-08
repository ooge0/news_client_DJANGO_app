from django.shortcuts import render
from django.http import HttpResponse, request
from main import models


def get_home(request):
    context = {
        'mystring': 'This is my home page'
    }
    return render(request, 'main/home.html', context)

def create_source(request):
    print(request.GET['name'])
    src_name = request.GET['name']
    src_context = request.GET['context']
    source = models.Source(name=src_name, context=src_context)
    source.save()
    return HttpResponse('haha')

def get_sources_list(request):
    context = {}
    context['sources'] = list(models.Source.objects.all())
    return render(request, 'main/sources_list.html', context)

def get_sources_table(request):
    context = {}
    context['sources'] = list(models.Source.objects.all())
    return render(request, 'main/sources_table.html', context)

def get_source(request, pk):
    source = models.Source.objects.get(id=pk)
    data = models.Data.objects.get(id=pk)
    context_source = {}
    context_data = {}
    context_source['source'] = source
    context_data['data'] = data
    return render(request, 'main/source.html', context_source)

