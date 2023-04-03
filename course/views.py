from django.shortcuts import render
from .models import Course
from .serializer import CourseSerializers
from rest_framework import viewsets

# Create your views here.



class CourseView(viewsets.ModelViewSet):
      queryset = Course.objects.all()
      serializer_class = CourseSerializers