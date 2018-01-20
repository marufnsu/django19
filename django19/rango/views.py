from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}
    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says hey here is the about page.")
