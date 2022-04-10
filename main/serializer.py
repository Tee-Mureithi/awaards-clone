from rest_framework import fields, serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ('id', 'bio','project','contact','created_at')
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'