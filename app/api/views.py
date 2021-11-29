from django.shortcuts import render
from rest_framework import generics

from .serializers import *
# Create your views here.

def index(request):
	return render(request, 'index.html')


class PlayerListView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerwithForeignSerializer
    
    def get_queryset(self):
        queryset = Player.objects.all()
        name = self.request.query_params.get('name',None)
        
        if name is not None:
            queryset = queryset.filter(player_name_icontains = name)
        return queryset