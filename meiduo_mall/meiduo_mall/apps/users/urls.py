from . import views
from django.conf.urls import url

from .views import RegisterView

urlpatterns=[
    url(r'^register/$',views.RegisterView.as_view(),name='register')
]