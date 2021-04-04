from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))


]

"""
as_view() is a standard function that we call to convert
our api view class to be rendered by our urls
"""
