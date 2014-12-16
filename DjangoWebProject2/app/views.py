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
            'message':'Adress',
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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/books.html',
        context_instance = RequestContext(request,
        {
            'books':books,
        })
    )


from app.views import *
from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
    #request.method == 'GET':

    print(book_id)
    post = Book.objects.get(id=int(book_id))
    post.delete()
    return HttpResponseRedirect('/app/books.html')

def editbook(request, book_id):
    if request.method == 'GET':
        print(request.GET)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Book(id=book_id, title=cd['title'], about=cd['about'], timestamp=cd['timestamp'])
            post.save()
            return HttpResponseRedirect('../../books')
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



from django.template import loader, Context
from django.http import HttpResponse
from app.models import app
def archive(request):
    posts = app.objects.all()
    t = loa
    der.get_template("my_template.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))


#Logowanie z tutoriala

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('app/login2.html',c);

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/invalid')

def log_in(request):
    return render_to_response('app/log_in.html')

def invalid_login(request):
    return render_to_response('app/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('app/logout.html');

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render_to_response('app/register.html',args)

def register_success(request):
    return render_to_response('app/register_success.html')