from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import MembersSerializer, SquadSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class MembersAPIview(APIView):

    def get(self, request):
        members = Members.objects.all()
        serializer = MembersSerializer(members, many=True)

        return Response(serializer.data)


class SquadAPIview(APIView):
    def get(self, request):
        squad = Squad.objects.all()
        serializer = SquadSerializer(squad, many=True)

        return Response(serializer.data)


class SquadListView(ListAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    # filter_fields = ["members__age"]
    search_fields = ('squadName', 'homeTown', 'formed', 'secretBase', 'active', 'members__name', 'members__age', 'members__secretIdentity', 'members__powers__item')