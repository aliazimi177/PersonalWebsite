from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *
urlpatterns = [
    path("", PostListView.as_view(), name="blog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
