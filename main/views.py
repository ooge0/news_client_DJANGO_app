from django.shortcuts import render
from django.http import HttpResponse, request
from main import models


def home(request):
    # source = models.Source(name='name1', context='context1')
    # source.save()

    source = models.Source.objects.get(name='name1')
    print(source)
    
    context = {
        'mystring': 'haha'
    }
    return render(request, 'main/home.html', context)

def create_source(request):
    print(request.GET['name'])
    src_name = request.GET['name']
    src_context = request.GET['context']
    source = models.Source(name=src_name, context=src_context)
    source.save()
    return HttpResponse('haha')

def get_sources(request):
    context = {}
    context['sources'] = list(models.Source.objects.all())
    return render(request, 'main/sources.html', context)

def get_sources_table(request):
    context = {}
    context['sources'] = list(models.Source.objects.all())
    return render(request, 'main/sources_table.html', context)

def get_source(request, pk):
    source = models.Source.objects.get(id=pk)
    context = {}
    context['source'] = source
    return render(request, 'main/source.html', context)

