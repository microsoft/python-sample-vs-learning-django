from django.shortcuts import render
from django.http import HttpResponse  # For tutorial steps 2-1 and 2-2
from datetime import datetime         # For tutorial step 2-2
from django.shortcuts import render   # For tutorial step 2-3

def index(request):
    # Code for tutorial step 2-1
    # return HttpResponse("Hello, Django!")

    # Code for tutorial step 2-2    
    #now = datetime.now()

    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    #return HttpResponse(html_content)
    
    # Code for tutorial step 2-3
    now = datetime.now()

    return render(
        request,
        "index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

# Code for step 3-3

def about(request):
    return render(
        request,
        "about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )