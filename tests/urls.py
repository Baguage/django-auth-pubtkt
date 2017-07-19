from django.conf.urls import url, include

from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    # include("django_auth_pubtkt.urls")
]
