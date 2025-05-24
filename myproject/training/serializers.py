from rest_framework import serializers
from .models import Specialist, QualificationCourse, Participation

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

class QualificationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationCourse
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'