from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics, viewsets, permissions, status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskList2(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def GET(request):
        if request.method == 'GET':
            queryset = Task.objects.all()
            serializer = TaskSerializer(queryset, many=True)
            return JsonResponse([], safe=False)
        
class TakeList3(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


# New
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
