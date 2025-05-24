from django.shortcuts import render
import plotly.express as px
from .models import Participation
from django.db.models import Count
from rest_framework import viewsets
from .models import Specialist, QualificationCourse, Participation
from .serializers import SpecialistSerializer, QualificationCourseSerializer, ParticipationSerializer

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

class QualificationCourseViewSet(viewsets.ModelViewSet):
    queryset = QualificationCourse.objects.all()
    serializer_class = QualificationCourseSerializer

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
def participation_chart(request):
    data = (
        Participation.objects
        .values('course__title')
        .annotate(count=Count('id'))
    )
    fig = px.bar(
        x=[entry['course__title'] for entry in data],
        y=[entry['count'] for entry in data],
        labels={'x': 'Курс', 'y': 'Количество участников'},
        title='Статистика участия в курсах'
    )
    chart_html = fig.to_html(full_html=False)
    return render(request, 'training/chart.html', {'chart': chart_html})



# Create your views here.
