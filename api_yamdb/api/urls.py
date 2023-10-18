from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
)
from users.views import TokenView, UserSignUpView, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register(r"titles", TitleViewSet, basename="titles")
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews"
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", UserSignUpView.as_view(), name="signup"),
    path("v1/auth/token/", TokenView.as_view(), name="get_token"),
]
