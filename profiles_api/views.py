from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions





class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_clases = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
