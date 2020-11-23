from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from rest_framework import mixins
from .serializers import *
from .models import OwesandOwedBy
from django.contrib.auth.models import User
from rest_framework import filters


class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):

    filter_backends = (filters.SearchFilter,)
    serializer_class = OwesandOwedBySerializer
    queryset = OwesandOwedBy.objects.all()
    search_fields = ['name']

    lookup_field = 'id'

    def get(self, request, id=None):
        # print(request.data)
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class GenericUserApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    serializer = UserSerializer(data=serializer_class.data)
    if serializer.is_valid():
        serializer.save()

    def get(self, request, id=None):
        # if id:
        #     return self.retrieve(request)
        # else:
        return self.list(request)

    def post(self, request):
        return self.create(request)
# ****************************************************************


# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def user_creation(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
