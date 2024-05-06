import logging
from django.shortcuts import render
# from .utils import encrypt_url_parameter
from django.http import HttpResponse, request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main import models
from main.utils.utils import encrypt_url_parameter


def get_home(request):
    context = {
        'mystring': 'GeoNazi'
    }
    return render(request, 'main/home.html', context)

def get_stats(request):
    context = {}
    return render(request, 'main/stats.html', context)

def get_resources_ik(request):
    data_list = list(models.Resources.objects.all())

    # Set the number of items per page
    items_per_page = int(request.GET.get('records_per_page', 20))  # Default to 10 if not provided

    paginator = Paginator(data_list, items_per_page)

    page = request.GET.get('page')
    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    context_data = {
        'data_list': data_list,
        'paginator': paginator,
    }

    return render(request, 'main/resources_ik.html', context_data)

def get_source(request, pk):
    source = models.Source.objects.get(id=pk)
    data_list = models.Data.objects.filter(source=source)
    context_source = {}
    context_data = {}
    context_source['source'] = source
    context_data['data'] = data_list
    return render(request, 'main/source.html', {'source': source, 'data_list': data_list})


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

def get_source_(request, pk):
    source = models.Source.objects.get(id=pk)
    data = models.Data.objects.get(id=pk)
    context_source = {}
    context_data = {}
    context_source['source'] = source
    context_data['data'] = data
    return render(request, 'main/source.html', context_source)

