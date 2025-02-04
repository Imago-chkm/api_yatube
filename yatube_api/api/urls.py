from rest_framework import routers
from django.urls import path, re_path
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = routers.SimpleRouter()
router.register(r'group', GroupViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    re_path(
        r'^posts/(?P<post_id>\d+)/comments/$',
        comment_list,
        name='comment-list'
    ),
    re_path(
        r'^posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/$',
        comment_detail,
        name='comment-detail'
    ),
    path('api-token-auth/', views.obtain_auth_token),
]
urlpatterns += router.urls
