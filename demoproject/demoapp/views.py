from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'log.html')


def home(request):
    return render(request, 'home.html')


def my_view(request):
    name_list = ['Alice', 'Bob', 'Charlie']
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    return render(request, 'my_template.html', {'name_list': name_list, 'data': data})
