from rest_framework import serializers
from api.models import Questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Questions
        fields= '__all__'
        