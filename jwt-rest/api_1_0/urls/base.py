from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api_1_0.views import UserRegistrationView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^auth/register/$', UserRegistrationView.as_view(), name='register'),
    url(r'^auth/token/obtain/$', obtain_jwt_token, name='obtain_toke'),
    url(r'^auth/token/refresh/$', refresh_jwt_token, name='refresh_token')
]
