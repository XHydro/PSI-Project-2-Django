
from django.conf.urls import *
from app.views import archive
from app.views import books
from app.views import singlebook


urlpatterns = patterns ('',
url(r'^$', archive)
)

urlpatterns = patterns ('',
url(r'^$', books)
)

urlpatterns = patterns ('',
url(r'^$', singlebook)
)