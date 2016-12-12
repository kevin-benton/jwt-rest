from django.conf.urls import url, include

from .base import *

urlpatterns += [
    url(r'^auth/', include('rest_framework.urls'))
]