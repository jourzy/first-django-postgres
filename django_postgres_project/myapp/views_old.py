from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'Emma'
    # return render(request, 'index.html', {'name':name})

    # context = {
    #     'name':'Emma',
    #     'age': 44,
    #     'nationality':'irish'
    # }
    # return render(request, 'index.html', context)

    return render(request, 'index.html')

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount':amount_of_words})