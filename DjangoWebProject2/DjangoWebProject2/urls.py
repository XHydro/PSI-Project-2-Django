"""
Definition of urls for DjangoWebProject2.
"""
from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from app.views import singlebook
from app.views import new_entry
from app.views import deletebook
from app.views import editbook
import app.urls; #robert

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^books', 'app.views.books', name='books'),
    url(r'^(?P<book_id>\d+)$', singlebook),
    url(r'^nowy/$', new_entry),
    url(r'^delete/(?P<book_id>\d+)$', deletebook),
    url(r'^edit/(?P<book_id>\d+)/$', editbook),
    url(r'^app/', include(app.urls)), #robert
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    #url(r'^login', 'app.views.login', name='login'), #robert

    url(r'^register/$', 'app.views.register', name='register'), #robert

    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

