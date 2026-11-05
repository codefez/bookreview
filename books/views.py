from django.shortcuts import render

# Create your views here.
def homepage(request):
    a = 10
    b = "bookclub"

    context = {'number':a,'randomText':b}
    return render(request, 'books/homepage.html', context)