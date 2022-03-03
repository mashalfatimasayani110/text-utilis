
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import text

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                print("No")
        print("pre",analyzed)
        params = {'purpose':'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == 'on'):
        analyzed = len(djtext)
        params = {'purpose':'Count Number of Characters', 'analyzed_text': analyzed}
        djtext = analyzed
    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)