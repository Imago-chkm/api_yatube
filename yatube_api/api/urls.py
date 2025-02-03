from django.urls import include, path

from api.views import PostViewSet

app_name = 'api'

urlpatterns = [
    path('', include(PostViewSet)),
]