from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts', PostViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
]
urlpatterns += router.urls
