# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed,'alert':'success','message':'Task Performed please check result'}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed,'alert':'success','message':'Task Performed please check result'}
        # Analyze the text
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed,'alert':'success','message':'Task Performed please check result'}
        # Analyze the text
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed,'alert':'success','message':'Task Performed please check result'}
        # Analyze the text
        djtext = analyzed
    
    # give if conditon for all above conditons are when false to give error message
    if removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on":
        params = {'purpose': 'Nothing Removed',
              'analyzed_text': 'Sorry No options selected','alert':'danger','message':'Sorry Nothing Analyzed please check atleast one option'}
        return render(request, 'index.html', params)
    if removepunc == "on" and fullcaps == "on" and extraspaceremover == "on" and newlineremover == "on":
        params = {'purpose': 'All conditions checked', 'analyzed_text': djtext,'alert':'success','message':'All Tasks Performed please check result'}
    return render(request, 'index.html', params)
