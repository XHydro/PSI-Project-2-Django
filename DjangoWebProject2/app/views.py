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

from app.models import Book

def books(request):
    """Renders the about page."""
    books = Book.objects.all()
    t = loader.get_template("app/books.html")
    c = Context({'books':books})
    return HttpResponse(t.render(c))
    #assert isinstance(request, HttpRequest)
    #return render(
    #    request,
    #    'app/books.html',
    #    context_instance = RequestContext(request,
    #    {
    #        'title':'Books',
    #        'message':'Your application description page.',
    #        'year':datetime.now().year,
    #    })
    #)

from app.views import *
from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from app.models import BookPost
#from app.forms import BookForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

def singlebook(request, book_id):
    print(book_id)
    book = Book.objects.get(id=int(book_id))
    print(book.title)
    return render_to_response('app/single_book.html', {'book':book})

from app.forms import BookForm
from django.core.context_processors import csrf
def new_entry(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            post = Book(title=cd['title'], about=cd['about'], timestamp=cd['timestamp'])
            post.save()
            return HttpResponseRedirect('/books.html')
        else:
            ctx = Context({'form': form})
            ctx.update(csrf(request))
            return render_to_response('app/book_form.html', ctx)
    else:
        form = BookForm()
        ctx = Context({'form': form})
        ctx.update(csrf(request))
        return render_to_response('app/book_form.html', ctx)

def deletebook(request, book_id):
    print(book_id)
    post = Book.objects.get(id=int(book_id))
    post.delete()
    return HttpResponseRedirect('/app/books.html')

def editbook(request, book_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Book(id=book_id, title=cd['title'], about=cd['about'])
            post.save()
            return HttpResponseRedirect('/app/')
        else:
            ctx = Context({'form': form})
            ctx.update(csrf(request))
            return render_to_response('app/book_form.html', ctx)
    else:
        post = Book.objects.get(id=int(book_id))
        data = {'title': post.title, 'about': post.about}
        post_form = BookForm(initial=data)
        ctx = Context({'form': post_form})
        ctx.update(csrf(request))
        return render_to_response('app/book_form.html', ctx)


def register(request):
    """Renders the contact page."""
    if request.method == 'POST': 
        request.POST.get("title", "")
        
        username = request.POST['username'];
        email = request.POST['email'];
        password = request.POST['password'];

        return render(
            request,
            'app/register2.html',
            context_instance = RequestContext(request,
            {
                'title' : 'Register2',
                'username': username,
                'email': email,
                'password' : password,
            })
        )

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


