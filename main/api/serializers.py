from rest_framework import serializers
from main.models import Contact, Projects, About


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'image', 'url']
    

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'description', 'image', 'cv']