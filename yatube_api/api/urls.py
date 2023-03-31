from api.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                       PostViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='some')
router.register(r'v1/posts/(?P<post_id>\d+)/'
                r'comments/(?P<comment_id>\d+)',
                CommentViewSet, basename='some')
router.register(r'v1/groups/(?P<group_id>\d+)',
                GroupViewSet, basename='group')
router.register(r'v1/follow', FollowViewSet)
router.register(r'v1/users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
