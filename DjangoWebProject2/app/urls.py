
from django.conf.urls import *
from app.views import archive
from app.views import books


urlpatterns = patterns ('',
url(r'^$', archive)
)

urlpatterns = patterns ('',
url(r'^$', books)
)