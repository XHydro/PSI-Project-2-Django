"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def register(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/register.html',
        context_instance = RequestContext(request,
        {
            'title':'Register',
            'message':'Register Your account.',
        })
    )

def register2(request):#in progres..
    username = request.POST['username'];
    email = request.POST['email'];
    password = request.POST['password'];

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/register.html',
        context_instance = RequestContext(request,
        {
            'title':'Register',
            'message':'Register Your account.',
        })
    )

#from django.contrib.auth import authenticate, login

#def my_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            # Redirect to a success page.
#        else:
#            # Return a 'disabled account' error message
#    else:
#        # Return an 'invalid login' error message.

        
from django.template import loader, Context
from django.http import HttpResponse
from app.models import app
def archive(request):
    posts = app.objects.all()
    t = loa
    der.get_template("my_template.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))


