from rest_framework.views import APIView
from main.models import (
   
    Projects, 
    About, 
    Contact,  
)
from .serializers import (
    ContactSerializer, 
    ProjectSerializer, 
    AboutSerializer, 
)
from rest_framework.response import Response
from rest_framework import status


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AboutView(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
