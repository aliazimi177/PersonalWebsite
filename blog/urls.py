from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path("", PostListView.as_view(), name="blog"),
    path('/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]

