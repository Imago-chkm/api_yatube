from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet)
router.register(r'group', GroupViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
