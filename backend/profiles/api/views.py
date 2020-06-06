from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly

from ..models import Profile, ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


# with viewsets allow us to have list an details view
# this way it gives it only one endpoint for same model
# this works with routers, not with normal pathes in urls.py
# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

# next level to make ProfileViewSet accept update
# to so, we inherit from genericviewset & all mixin classes
class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # profile instance should be only updated by their owners (object.user)
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


# with ModeViewSet we don't need to inherit genericviewset
# and its mixin, because it self inherit from it
class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # to connet the status creation with the logged in
    # user who's making the reques, we need to rewrite perform_create
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

# this view let the user to update only the avatar in the profile
class AvatarUpdateViewAPI(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    # no need to query set and no need to
    # pass and id in the url
    # because this get_object to automatically
    # identify and return the profile instance
    # assosiated with request.user
    def get_object(self):
        profile_object= self.request.user.profile
        return profile_object

# 38.Viewsets and Routers