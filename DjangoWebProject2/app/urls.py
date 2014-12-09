
from django.conf.urls import *
from app.views import archive

urlpatterns = patterns ('',
url(r'^$', archive)
)