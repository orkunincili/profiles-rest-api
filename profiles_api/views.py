from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions





class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_clases = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = (permissions.IsSuperUser,)
        else:
            self.permission_classes = (permissions.UpdateOwnProfile,)

        return super(self.__class__, self).get_permissions()

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profile feed items"""
    queryset = models.ProfileFeedItem.objects.all()
    authentication_clases = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)



    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user.This function
        gets called every HTTP POST to our view set
        """

        serializer.save(user_profile=self.request.user)
