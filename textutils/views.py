# i have created this file - gautam

from django.http import HttpResponse
from django.shortcuts import render

# code for chapeter 6
# def index(request):
#     return HttpResponse('''<h1> Gautam </h1> <a href="https://gautamk1512.blogspot.com/" > LEARNING EINSTEIN </a>''')


# def new(request):
#     return HttpResponse('''<h1>raj </h1> <a href="https://youtube.com/" > youtub</a>''')


# def about(request):
#     return HttpResponse("about Gautam bahi")


# code for video 7
def index(request):
    # return HttpResponse("Home")

    return render(request, 'index.html')


# def analyze(request):
#     # gat the text
#     Djtext = request.GET.get('text', 'default')
#     removepunc = request.GET.get('removepunc', 'default')

#     print(removepunc)
#     print(Djtext)
#     # Analyze the text
#     return render(request, 'analyze.html',params)

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
# def capfirst(request):
#     return HttpResponse("capitalizefirst")


# def newlineremove(request):
#     return HttpResponse("newlineremove")


# def spaceremove(request):
#     return HttpResponse("spaceremove")


# def charcount(request):
#     return HttpResponse("charcount")
