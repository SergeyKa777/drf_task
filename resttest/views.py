from django.contrib.auth.models import User, Group
from .models import Game, Probe,Ss,Album,Track
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, GameSerializer, GameSerializer2, ProbeSerializer , SsSerializer,TrackSerializer,AlbumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameViewSet2(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer2


class ProbeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Probe.objects.all()
    serializer_class = ProbeSerializer


####################

class SsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Ss.objects.all()
    serializer_class = SsSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


###############

def ddd(request):
    print(Ss.objects.all())
    for item in Ss.objects.filter(parent__isnull=True):
        print(item.name+"===="+str(item.id))
        for child in item.children.all():

            print(child.name+"===="+str(child.id))

            for child2 in child.children.all():

                print(child2.name +"===="+str(child2.id))
                for child3 in child2.children.all():
                    print(child3.name + "====" + str(child3.id))

    template_name = 'test.html'
    context = {'a': 22}
    return render(request, template_name, context)

